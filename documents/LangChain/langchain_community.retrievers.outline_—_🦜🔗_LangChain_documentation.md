# langchain_community.retrievers.outline — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/retrievers/outline.html
**Word Count:** 19
**Links Count:** 13
**Scraped:** 2025-07-21 09:15:18
**Status:** completed

---

# Source code for langchain\_community.retrievers.outline               from typing import List          from langchain_core.callbacks import CallbackManagerForRetrieverRun     from langchain_core.documents import Document     from langchain_core.retrievers import BaseRetriever          from langchain_community.utilities.outline import OutlineAPIWrapper                              [[docs]](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.outline.OutlineRetriever.html#langchain_community.retrievers.outline.OutlineRetriever)     class OutlineRetriever(BaseRetriever, OutlineAPIWrapper):         """Retriever for Outline API.              It wraps run() to get_relevant_documents().         It uses all OutlineAPIWrapper arguments without any change.         """              def _get_relevant_documents(             self, query: str, *, run_manager: CallbackManagerForRetrieverRun         ) -> List[Document]:             return self.run(query=query)