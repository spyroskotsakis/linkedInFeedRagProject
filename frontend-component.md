# Streamlit Front-End Specification for LinkedIn Feed Explorer & RAG Search  

A professional developer hand-off detailing architecture, technology choices, phased delivery, acceptance tests, and reference code for turning existing JSON/CSV exports into a rich Streamlit interface with production-grade Retrieval-Augmented Generation (RAG) powered by LangGraph, switchable LLM back-ends (Ollama +mistral-nemo:12b and Azure OpenAI), and performant data exploration tools.

## Overview  

Your scraper already lands fully structured exports in `data//…`. This spec adds a **stand-alone UI module** (`ui_feed_explorer`) that:

- Auto-discovers any export folder inside `data/`.
- Streams large post sets (>200,000 rows) responsively with Arrow-backed frames[1][2].
- Surfaced through multiple, lazy-rendered views (table, cards, engagement chart, JSON diff).
- Embeds a **RAG Search drawer**: user queries → vector retrieval → LangGraph self-refining chain → answer with citations to original posts.

All code is pure Python 3.11, no impact on existing scraper jobs.

## 1 🎯 Goals & Non-Functional Requirements  

| Goal | KPI | Acceptance Gate |
|------|-----|-----------------|
| Fast initial load of 200,000-row export | 0.75 on test set |
| 7. Provider Switcher & Secrets UI | 4-5 | Settings page toggle; Ollama health-check; Azure key input | Smoke: toggle 10×, no crash |
| 8. End-to-End & Hardening | 5 | Docker compose with optional `ollama serve`; st.session_state init patch | Locust load 20 users, error  pl.DataFrame:
    # Convert CSV→Parquet once for speed
    csv_path = folder / "linkedin_feed.csv"
    pq_path  = folder / "linkedin_feed.parquet"
    if not pq_path.exists() or pq_path.stat().st_mtime < csv_path.stat().st_mtime:
        df = pl.read_csv(csv_path)
        df.write_parquet(pq_path)
    return pl.read_parquet(pq_path)  # Arrow-backed[11]
```
Arrow cuts serialization latency by ~10× on 5 k×50 frames[1].

### 6.2 ag-Grid Wrapper with Server-Side Pagination  

```python
from st_aggrid import AgGrid, GridOptionsBuilder
import streamlit as st

def render_grid(df):
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_default_column(filter=True)
    gb.configure_pagination(paginationAutoPageSize=False,
                            paginationPageSize=100)
    gb.configure_grid_options(serverSideRowModel=True)
    st.caption(f"{len(df):,} rows")
    AgGrid(df, gridOptions=gb.build(),
           update_mode="NO_UPDATE", height=500,
           columns_auto_size_mode="FIT_CONTENTS")
```

ServerMode avoids WS payload explosion on Cloud[4][7].

### 6.3 Session-State Safe `st.data_editor`  

```python
def editable_settings():
    if "raw_cfg" not in st.session_state:
        st.session_state.raw_cfg = {"provider": "ollama",
                                    "temperature": 0.1}
    edited = st.data_editor(st.session_state.raw_cfg,
                            num_rows="dynamic",
                            key="cfg_editor")
    st.session_state.raw_cfg = edited  # patch for lost edits[29]
```

### 6.4 LLM Provider Factory  

```python
from langchain_openai import AzureChatOpenAI, ChatOpenAI
import ollama
import os

def get_llm(state):
    if state["provider"] == "azure":
        return AzureChatOpenAI(
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
            temperature=state["temperature"])
    elif state["provider"] == "ollama":
        return ollama.Chat(model="mistral-nemo:12b")  # auto local[22][27]
    else:
        raise ValueError("Unknown provider")
```

Toggle via Settings page; state kept in Session State.

### 6.5 LangGraph Self-RAG Blueprint  

```python
from langgraph.graph import END, StateGraph
from rag.retriever import get_retriever

def build_graph(llm, vs):
    g = StateGraph(name="feed_rag")

    @g.node
    def retrieve(state):
        q = state["query"]
        docs = get_retriever(vs).invoke(q, k=8)
        return {"docs": docs}

    @g.node
    def rank(state):
        docs = state["docs"]
        scored = [d for d in docs if "relevant" in llm(f"Is this relevant? {d.page_content}").lower()]
        return {"docs": scored or docs[:3]}

    @g.node
    def answer(state):
        prompt = "\n\n".join([d.page_content for d in state["docs"]])
        reply = llm(f"Answer based ONLY on:\n{prompt}\n\nQ:{state['query']}")
        return {"answer": reply}

    g.edge("start", retrieve).edge(retrieve, rank).edge(rank, answer).edge(answer, END)
    return g.compile()
```
Implements retrieval, self-grading relevance gate per Self-RAG[13].

### 6.6 Provider Health-Check  

```python
def check_ollama():
    try:
        return "mistral-nemo" in ollama.list()["models"]
    except Exception:
        return False
```

If offline, Settings page disables local option.

## 7 🧪 Testing Strategy  

### 7.1 Unit Tests  

| Module | Case | Tool |
|--------|------|------|
| `load_export` | Parquet newer flag | `pytest-tmpdir` |
| Retriever | kNN returns ≥k docs | `pytest` |
| Provider factory | Wrong key raises `ValueError` | — |

### 7.2 Integration  

1. Spin Docker with sidecar `ollama serve -p 11434`.  
2. POST `/v1/chat/completions` smoke[19].  
3. Graph QA returns citation string containing `urn:li:`.

### 7.3 End-to-End  

- **Locust**: 20 virtual users, random filter clicks, RAG queries.  
- Pass: 95-th pct Table TPS ≥5, error <1%.

### 7.4 LLM Evaluation  

- 50 manually-curated “expected answer” pairs.  
- Metric: Rouge-L ≥0.4, groundedness check by Self-RAG ranker flag.

### 7.5 Performance Budget Tests  

| Scenario | Device | Metric | Pass |
|----------|--------|--------|------|
| 200 k rows load | M1 Air | Time To First Byte ≤3 s | ✅ |
| Scroll 10 pages | Chrome 125 | CPU ≤70% | ✅ |
| 8 query burst | 4060 Ti + mistral | <9 s p95 | ✅ |

## 8 🚀 Deployment Instructions  

### 8.1 Local Dev  

```bash
conda env create -f environment.yml
conda activate feed-ui
ollama pull mistral-nemo          # once[22]
streamlit run streamlit_app.py
```

### 8.2 Docker (prod)  

```bash
docker compose up -d
# docker-compose.yaml includes:
#  - ui service (port 8501)
#  - optional ollama service (port 11434, volumes:/models)
```

On Azure Container Apps without GPU, set `PROVIDER=azure` and mount key vault.

## 9 📄 Security & Compliance  

- No outgoing calls unless provider = “azure” (`*.openai.azure.com`).  
- Local Ollama runs only on 127.0.0.1; CORS disabled[15].  
- `secrets.toml` loaded via Streamlit secrets; **never git-add**.  
- GDPR: exports reside on same host; request deletion pipeline ready.  
- License scan via `reuse lint`.

## 10 🐞 Known Edge Cases & Mitigations  

| Issue | Symptom | Fix |
|-------|---------|-----|
| DataEditor lost edits | Cell reverts first click[10] | Session-state patch in §6.3 |
| ag-Grid freeze on 50 k rows | Cloud WebSocket drop[7] | Fallback to `pagination.py` |
| Ollama “model not found” | 404 JSON | instruct user to `ollama pull mistral-nemo`[16] |
| Azure 429 | Throttle quota | Retry-after header + exponential backoff |

## 11 📚 Developer “Cheat Sheet”  

| Task | Snippet |
|------|---------|
| Add new export dir | `mv new_run/ data/posts_…/` (auto-discovered) |
| Re-index vectors only | Settings → “Rebuild Index” button |
| Switch LLM | Settings → Provider select   |
| Run all tests | `pytest -q` |
| Profile slow renders | `streamlit --logger.level=debug` |

## 12 ✅ Definition of Done Checklist  

- [ ] README updated with env + usage.  
- [ ] Phases 0-9 merged to `main`, CI green.  
- [ ] Sprint demo shows dropdown → table → RAG answer.  
- [ ] Test artifacts in `htmlcov/` & `junit.xml`.  
- [ ] Docker image pushed `ghcr.io/…/feed-ui:sha`.  

## 13 📈 Future Enhancements (Backlog)  

1. **Delta Lake** output option for analytic exports.  
2. Bring-your-own embeddings (E5-Mistral) toggle.  
3. Web RTC remote Ollama pooling.  
4. Fine-grained row-level permissions (Streamlit Auth).  
5. Edge-cached vector store via Qdrant Cloud.
