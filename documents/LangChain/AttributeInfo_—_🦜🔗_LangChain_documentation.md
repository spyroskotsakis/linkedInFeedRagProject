# AttributeInfo — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chains/langchain.chains.query_constructor.schema.AttributeInfo.html
**Word Count:** 75
**Links Count:** 220
**Scraped:** 2025-07-21 07:49:32
**Status:** completed

---

# AttributeInfo\#

_class _langchain.chains.query\_constructor.schema.AttributeInfo[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/query_constructor/schema.html#AttributeInfo)\#     

Bases: `BaseModel`

Information about a data source attribute.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _description _: str_ _\[Required\]_\#     

_param _name _: str_ _\[Required\]_\#     

_param _type _: str_ _\[Required\]_\#     

Examples using AttributeInfo

  * [Astra DB \(Cassandra\)](https://python.langchain.com/docs/integrations/retrievers/self_query/astradb/)

  * [Chroma](https://python.langchain.com/docs/integrations/retrievers/self_query/chroma_self_query/)

  * [DashVector](https://python.langchain.com/docs/integrations/retrievers/self_query/dashvector/)

  * [Databricks Vector Search](https://python.langchain.com/docs/integrations/retrievers/self_query/databricks_vector_search/)

  * [Deep Lake](https://python.langchain.com/docs/integrations/retrievers/self_query/activeloop_deeplake_self_query/)

  * [DingoDB](https://python.langchain.com/docs/integrations/retrievers/self_query/dingo/)

  * [Docugami](https://python.langchain.com/docs/integrations/document_loaders/docugami/)

  * [Elasticsearch](https://python.langchain.com/docs/integrations/retrievers/self_query/elasticsearch_self_query/)

  * [How to add scores to retriever results](https://python.langchain.com/docs/how_to/add_scores_retriever/)

  * [How to do “self-querying” retrieval](https://python.langchain.com/docs/how_to/self_query/)

  * [Milvus](https://python.langchain.com/docs/integrations/retrievers/self_query/milvus_self_query/)

  * [MongoDB Atlas](https://python.langchain.com/docs/integrations/retrievers/self_query/mongodb_atlas/)

  * [MyScale](https://python.langchain.com/docs/integrations/retrievers/self_query/myscale_self_query/)

  * [OpenSearch](https://python.langchain.com/docs/integrations/retrievers/self_query/opensearch_self_query/)

  * [PGVector \(Postgres\)](https://python.langchain.com/docs/integrations/retrievers/self_query/pgvector_self_query/)

  * [Pinecone](https://python.langchain.com/docs/integrations/retrievers/self_query/pinecone/)

  * [Qdrant](https://python.langchain.com/docs/integrations/retrievers/self_query/qdrant_self_query/)

  * [Redis](https://python.langchain.com/docs/integrations/retrievers/self_query/redis_self_query/)

  * [SAP HANA Cloud Vector Engine](https://python.langchain.com/docs/integrations/retrievers/self_query/hanavector_self_query/)

  * [Supabase \(Postgres\)](https://python.langchain.com/docs/integrations/retrievers/self_query/supabase_self_query/)

  * [Tencent Cloud VectorDB](https://python.langchain.com/docs/integrations/retrievers/self_query/tencentvectordb/)

  * [Timescale Vector \(Postgres\)](https://python.langchain.com/docs/integrations/vectorstores/timescalevector/)

  * [Timescale Vector \(Postgres\) ](https://python.langchain.com/docs/integrations/retrievers/self_query/timescalevector_self_query/)

  * [Vectara self-querying ](https://python.langchain.com/docs/integrations/retrievers/self_query/vectara_self_query/)

  * [Weaviate](https://python.langchain.com/docs/integrations/retrievers/self_query/weaviate_self_query/)

  * [self-query-qdrant](https://python.langchain.com/docs/templates/self-query-qdrant/)

__On this page