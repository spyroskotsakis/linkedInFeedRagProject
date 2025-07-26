# langchain_community.retrievers.rememberizer — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/retrievers/rememberizer.html
**Word Count:** 17
**Links Count:** 13
**Scraped:** 2025-07-21 09:16:02
**Status:** completed

---

# Source code for langchain\_community.retrievers.rememberizer               from typing import List          from langchain_core.callbacks import CallbackManagerForRetrieverRun     from langchain_core.documents import Document     from langchain_core.retrievers import BaseRetriever          from langchain_community.utilities.rememberizer import RememberizerAPIWrapper                              [[docs]](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.rememberizer.RememberizerRetriever.html#langchain_community.retrievers.rememberizer.RememberizerRetriever)     class RememberizerRetriever(BaseRetriever, RememberizerAPIWrapper):         """`Rememberizer` retriever.              It wraps load() to get_relevant_documents().         It uses all RememberizerAPIWrapper arguments without any change.         """              def _get_relevant_documents(             self, query: str, *, run_manager: CallbackManagerForRetrieverRun         ) -> List[Document]:             return self.load(query=query)