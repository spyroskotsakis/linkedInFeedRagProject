# langchain_community.retrievers.pubmed — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/retrievers/pubmed.html
**Word Count:** 18
**Links Count:** 13
**Scraped:** 2025-07-21 09:13:23
**Status:** completed

---

# Source code for langchain\_community.retrievers.pubmed               from typing import List          from langchain_core.callbacks import CallbackManagerForRetrieverRun     from langchain_core.documents import Document     from langchain_core.retrievers import BaseRetriever          from langchain_community.utilities.pubmed import PubMedAPIWrapper                              [[docs]](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.pubmed.PubMedRetriever.html#langchain_community.retrievers.pubmed.PubMedRetriever)     class PubMedRetriever(BaseRetriever, PubMedAPIWrapper):         """`PubMed API` retriever.              It wraps load() to get_relevant_documents().         It uses all PubMedAPIWrapper arguments without any change.         """              def _get_relevant_documents(             self, query: str, *, run_manager: CallbackManagerForRetrieverRun         ) -> List[Document]:             return self.load_docs(query=query)