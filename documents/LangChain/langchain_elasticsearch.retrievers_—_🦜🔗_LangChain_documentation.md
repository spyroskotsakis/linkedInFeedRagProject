# langchain_elasticsearch.retrievers — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/retrievers.html
**Word Count:** 53
**Links Count:** 14
**Scraped:** 2025-07-21 09:19:50
**Status:** completed

---

# Source code for langchain\_elasticsearch.retrievers               from typing import Any, List          from langchain_core.callbacks import CallbackManagerForRetrieverRun     from langchain_core.documents import Document          from langchain_elasticsearch._async.retrievers import (         AsyncElasticsearchRetriever as _AsyncElasticsearchRetriever,     )     from langchain_elasticsearch._sync.retrievers import (         ElasticsearchRetriever as _ElasticsearchRetriever,     )               # langchain defines some sync methods as abstract in its base class     # so we have to add dummy methods for them, even though we only use the async versions                    [[docs]](https://python.langchain.com/api_reference/elasticsearch/retrievers/langchain_elasticsearch.retrievers.AsyncElasticsearchRetriever.html#langchain_elasticsearch.retrievers.AsyncElasticsearchRetriever)     class AsyncElasticsearchRetriever(_AsyncElasticsearchRetriever):         def _get_relevant_documents(             self, query: str, *, run_manager: CallbackManagerForRetrieverRun, **kwargs: Any         ) -> List[Document]:             raise NotImplementedError(                 "This class is asynchronous, use _aget_relevant_documents()"             )                              # this is only defined here so that it is picked up by Langchain's docs generator                    [[docs]](https://python.langchain.com/api_reference/elasticsearch/retrievers/langchain_elasticsearch.retrievers.ElasticsearchRetriever.html#langchain_elasticsearch.retrievers.ElasticsearchRetriever)     class ElasticsearchRetriever(_ElasticsearchRetriever):         pass