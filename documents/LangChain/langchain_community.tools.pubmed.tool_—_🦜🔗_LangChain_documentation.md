# langchain_community.tools.pubmed.tool — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/tools/pubmed/tool.html
**Word Count:** 48
**Links Count:** 13
**Scraped:** 2025-07-21 09:13:00
**Status:** completed

---

# Source code for langchain\_community.tools.pubmed.tool               from typing import Optional          from langchain_core.callbacks import CallbackManagerForToolRun     from langchain_core.tools import BaseTool     from pydantic import Field          from langchain_community.utilities.pubmed import PubMedAPIWrapper                              [[docs]](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.pubmed.tool.PubmedQueryRun.html#langchain_community.tools.pubmed.tool.PubmedQueryRun)     class PubmedQueryRun(BaseTool):         """Tool that searches the PubMed API."""              name: str = "pub_med"         description: str = (             "A wrapper around PubMed. "             "Useful for when you need to answer questions about medicine, health, "             "and biomedical topics "             "from biomedical literature, MEDLINE, life science journals, and online books. "             "Input should be a search query."         )         api_wrapper: PubMedAPIWrapper = Field(default_factory=PubMedAPIWrapper)  # type: ignore[arg-type]              def _run(             self,             query: str,             run_manager: Optional[CallbackManagerForToolRun] = None,         ) -> str:             """Use the PubMed tool."""             return self.api_wrapper.run(query)