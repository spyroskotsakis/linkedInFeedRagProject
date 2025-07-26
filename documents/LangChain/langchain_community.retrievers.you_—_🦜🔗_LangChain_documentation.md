# langchain_community.retrievers.you — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/retrievers/you.html
**Word Count:** 19
**Links Count:** 13
**Scraped:** 2025-07-21 09:11:53
**Status:** completed

---

# Source code for langchain\_community.retrievers.you               from typing import Any, List          from langchain_core.callbacks import (         AsyncCallbackManagerForRetrieverRun,         CallbackManagerForRetrieverRun,     )     from langchain_core.documents import Document     from langchain_core.retrievers import BaseRetriever          from langchain_community.utilities import YouSearchAPIWrapper                              [[docs]](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.you.YouRetriever.html#langchain_community.retrievers.you.YouRetriever)     class YouRetriever(BaseRetriever, YouSearchAPIWrapper):         """You.com Search API retriever.              It wraps results() to get_relevant_documents         It uses all YouSearchAPIWrapper arguments without any change.         """              def _get_relevant_documents(             self,             query: str,             *,             run_manager: CallbackManagerForRetrieverRun,             **kwargs: Any,         ) -> List[Document]:             return self.results(query, run_manager=run_manager.get_child(), **kwargs)              async def _aget_relevant_documents(             self,             query: str,             *,             run_manager: AsyncCallbackManagerForRetrieverRun,             **kwargs: Any,         ) -> List[Document]:             results = await self.results_async(                 query, run_manager=run_manager.get_child(), **kwargs             )             return results