# Document — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html
**Word Count:** 288
**Links Count:** 217
**Scraped:** 2025-07-21 07:55:26
**Status:** completed

---

# Document\#

_class _langchain\_core.documents.base.Document[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/documents/base.html#Document)\#     

Bases: [`BaseMedia`](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.BaseMedia.html#langchain_core.documents.base.BaseMedia "langchain_core.documents.base.BaseMedia")

Class for storing a piece of text and associated metadata.

Example               from langchain_core.documents import Document          document = Document(         page_content="Hello, world!",         metadata={"source": "https://example.com"}     )     

Pass page\_content in as positional or named arg.

_param _id _: str | None_ _ = None_\#     

An optional identifier for the document.

Ideally this should be unique across the document collection and formatted as a UUID, but this will not be enforced.

Added in version 0.2.11.

Constraints:     

  * **coerce\_numbers\_to\_str** = True

_param _metadata _: dict_ _\[Optional\]_\#     

Arbitrary metadata associated with the content.

_param _page\_content _: str_ _\[Required\]_\#     

String text.

_param _type _: Literal\['Document'\]__ = 'Document'_\#     

Examples using Document

  * [\# Basic example \(short documents\)](https://python.langchain.com/docs/versions/migrating_chains/map_reduce_chain/)

  * [\# Example](https://python.langchain.com/docs/versions/migrating_chains/map_rerank_docs_chain/)

  * [AI21SemanticTextSplitter](https://python.langchain.com/docs/integrations/document_transformers/ai21_semantic_text_splitter/)

  * [Airbyte CDK \(Deprecated\)](https://python.langchain.com/docs/integrations/document_loaders/airbyte_cdk/)

  * [Airbyte Gong \(Deprecated\)](https://python.langchain.com/docs/integrations/document_loaders/airbyte_gong/)

  * [Airbyte Hubspot \(Deprecated\)](https://python.langchain.com/docs/integrations/document_loaders/airbyte_hubspot/)

  * [Airbyte Salesforce \(Deprecated\)](https://python.langchain.com/docs/integrations/document_loaders/airbyte_salesforce/)

  * [Airbyte Shopify \(Deprecated\)](https://python.langchain.com/docs/integrations/document_loaders/airbyte_shopify/)

  * [Airbyte Stripe \(Deprecated\)](https://python.langchain.com/docs/integrations/document_loaders/airbyte_stripe/)

  * [Airbyte Typeform \(Deprecated\)](https://python.langchain.com/docs/integrations/document_loaders/airbyte_typeform/)

  * [Airbyte Zendesk Support \(Deprecated\)](https://python.langchain.com/docs/integrations/document_loaders/airbyte_zendesk_support/)

  * [Annoy](https://python.langchain.com/docs/integrations/vectorstores/annoy/)

  * [Apache Cassandra](https://python.langchain.com/docs/integrations/vectorstores/cassandra/)

  * [Apify Dataset](https://python.langchain.com/docs/integrations/document_loaders/apify_dataset/)

  * [Astra DB \(Cassandra\)](https://python.langchain.com/docs/integrations/retrievers/self_query/astradb/)

  * [Astra DB Vector Store](https://python.langchain.com/docs/integrations/vectorstores/astradb/)

  * [Azure Cosmos DB for Apache Gremlin](https://python.langchain.com/docs/integrations/graphs/azure_cosmosdb_gremlin/)

  * [BM25](https://python.langchain.com/docs/integrations/retrievers/bm25/)

  * [Build a Query Analysis System](https://python.langchain.com/docs/tutorials/query_analysis/)

  * [ChatGPT plugin](https://python.langchain.com/docs/integrations/retrievers/chatgpt-plugin/)

  * [Chroma](https://python.langchain.com/docs/integrations/vectorstores/chroma/)

  * [ClickHouse](https://python.langchain.com/docs/integrations/vectorstores/clickhouse/)

  * [Cohere](https://python.langchain.com/docs/integrations/providers/cohere/)

  * [Cohere RAG](https://python.langchain.com/docs/integrations/retrievers/cohere/)

  * [Copy Paste](https://python.langchain.com/docs/integrations/document_loaders/copypaste/)

  * [Couchbase ](https://python.langchain.com/docs/integrations/vectorstores/couchbase/)

  * [DashVector](https://python.langchain.com/docs/integrations/retrievers/self_query/dashvector/)

  * [Databricks Vector Search](https://python.langchain.com/docs/integrations/retrievers/self_query/databricks_vector_search/)

  * [Deep Lake](https://python.langchain.com/docs/integrations/retrievers/self_query/activeloop_deeplake_self_query/)

  * [DingoDB](https://python.langchain.com/docs/integrations/retrievers/self_query/dingo/)

  * [Doctran: extract properties](https://python.langchain.com/docs/integrations/document_transformers/doctran_extract_properties/)

  * [Doctran: interrogate documents](https://python.langchain.com/docs/integrations/document_transformers/doctran_interrogate_document/)

  * [Doctran: language translation](https://python.langchain.com/docs/integrations/document_transformers/doctran_translate_document/)

  * [Docugami](https://python.langchain.com/docs/integrations/document_loaders/docugami/)

  * [Elasticsearch](https://python.langchain.com/docs/integrations/vectorstores/elasticsearch/)

  * [ElasticsearchRetriever](https://python.langchain.com/docs/integrations/retrievers/elasticsearch_retriever/)

  * [Faiss](https://python.langchain.com/docs/integrations/vectorstores/faiss/)

  * [Faiss \(Async\)](https://python.langchain.com/docs/integrations/vectorstores/faiss_async/)

  * [Fleet AI Context](https://python.langchain.com/docs/integrations/retrievers/fleet_context/)

  * [Google Bigtable](https://python.langchain.com/docs/integrations/document_loaders/google_bigtable/)

  * [Google Cloud SQL for MySQL](https://python.langchain.com/docs/integrations/document_loaders/google_cloud_sql_mysql/)

  * [Google Cloud SQL for SQL server](https://python.langchain.com/docs/integrations/document_loaders/google_cloud_sql_mssql/)

  * [Google Cloud Vertex AI Reranker](https://python.langchain.com/docs/integrations/document_transformers/google_cloud_vertexai_rerank/)

  * [Google El Carro for Oracle Workloads](https://python.langchain.com/docs/integrations/document_loaders/google_el_carro/)

  * [Google Firestore \(Native Mode\)](https://python.langchain.com/docs/integrations/document_loaders/google_firestore/)

  * [Google Firestore in Datastore Mode](https://python.langchain.com/docs/integrations/document_loaders/google_datastore/)

  * [Google Memorystore for Redis](https://python.langchain.com/docs/integrations/document_loaders/google_memorystore_redis/)

  * [Google Spanner](https://python.langchain.com/docs/integrations/document_loaders/google_spanner/)

  * [Google Translate](https://python.langchain.com/docs/integrations/document_transformers/google_translate/)

  * [How to add scores to retriever results](https://python.langchain.com/docs/how_to/add_scores_retriever/)

  * [How to construct knowledge graphs](https://python.langchain.com/docs/how_to/graph_constructing/)

  * [How to convert Runnables as Tools](https://python.langchain.com/docs/how_to/convert_runnable_to_tool/)

  * [How to create a custom Document Loader](https://python.langchain.com/docs/how_to/document_loader_custom/)

  * [How to create a custom Retriever](https://python.langchain.com/docs/how_to/custom_retriever/)

  * [How to do “self-querying” retrieval](https://python.langchain.com/docs/how_to/self_query/)

  * [How to get a RAG application to add citations](https://python.langchain.com/docs/how_to/qa_citations/)

  * [How to handle long text when doing extraction](https://python.langchain.com/docs/how_to/extraction_long_text/)

  * [How to load Markdown](https://python.langchain.com/docs/how_to/document_loader_markdown/)

  * [How to retrieve using multiple vectors per document](https://python.langchain.com/docs/how_to/multi_vector/)

  * [How to summarize text in a single LLM call](https://python.langchain.com/docs/how_to/summarize_stuff/)

  * [How to summarize text through iterative refinement](https://python.langchain.com/docs/how_to/summarize_refine/)

  * [How to summarize text through parallelization](https://python.langchain.com/docs/how_to/summarize_map_reduce/)

  * [How to use a time-weighted vector store retriever](https://python.langchain.com/docs/how_to/time_weighted_vectorstore/)

  * [How to use the LangChain indexing API](https://python.langchain.com/docs/how_to/indexing/)

  * [Identity-enabled RAG using PebbloRetrievalQA](https://python.langchain.com/docs/integrations/providers/pebblo/pebblo_retrieval_qa/)

  * [Kinetica Vectorstore API](https://python.langchain.com/docs/integrations/vectorstores/kinetica/)

  * [Kinetica Vectorstore based Retriever](https://python.langchain.com/docs/integrations/retrievers/kinetica/)

  * [Lantern](https://python.langchain.com/docs/integrations/vectorstores/lantern/)

  * [Milvus](https://python.langchain.com/docs/integrations/vectorstores/milvus/)

  * [Model caches](https://python.langchain.com/docs/integrations/llm_caching/)

  * [MongoDB Atlas](https://python.langchain.com/docs/integrations/vectorstores/mongodb_atlas/)

  * [MyScale](https://python.langchain.com/docs/integrations/retrievers/self_query/myscale_self_query/)

  * [Neo4j Vector Index](https://python.langchain.com/docs/integrations/vectorstores/neo4jvector/)

  * [Nuclia](https://python.langchain.com/docs/integrations/document_transformers/nuclia_transformer/)

  * [OpenAI metadata tagger](https://python.langchain.com/docs/integrations/document_transformers/openai_metadata_tagger/)

  * [OpenSearch](https://python.langchain.com/docs/integrations/retrievers/self_query/opensearch_self_query/)

  * [Oracle AI Vector Search: Document Processing](https://python.langchain.com/docs/integrations/document_loaders/oracleai/)

  * [Oracle AI Vector Search: Generate Embeddings](https://python.langchain.com/docs/integrations/text_embedding/oracleai/)

  * [Oracle AI Vector Search: Generate Summary](https://python.langchain.com/docs/integrations/tools/oracleai/)

  * [Oracle AI Vector Search: Vector Store](https://python.langchain.com/docs/integrations/vectorstores/oracle/)

  * [PDFMiner](https://python.langchain.com/docs/integrations/document_loaders/pdfminer/)

  * [PGVecto.rs](https://python.langchain.com/docs/integrations/vectorstores/pgvecto_rs/)

  * [PGVector](https://python.langchain.com/docs/integrations/vectorstores/pgvector/)

  * [PGVector \(Postgres\)](https://python.langchain.com/docs/integrations/retrievers/self_query/pgvector_self_query/)

  * [Pinecone](https://python.langchain.com/docs/integrations/vectorstores/pinecone/)

  * [Postgres Embedding](https://python.langchain.com/docs/integrations/vectorstores/pgembedding/)

  * [Qdrant](https://python.langchain.com/docs/integrations/vectorstores/qdrant/)

  * [Qdrant Sparse Vector](https://python.langchain.com/docs/integrations/retrievers/qdrant-sparse/)

  * [Redis](https://python.langchain.com/docs/integrations/vectorstores/redis/)

  * [SAP HANA Cloud Vector Engine](https://python.langchain.com/docs/integrations/vectorstores/sap_hanavector/)

  * [SageMakerEndpoint](https://python.langchain.com/docs/integrations/llms/sagemaker/)

  * [SingleStoreDB](https://python.langchain.com/docs/integrations/vectorstores/singlestoredb/)

  * [Summarize Text](https://python.langchain.com/docs/tutorials/summarization/)

  * [Supabase \(Postgres\)](https://python.langchain.com/docs/integrations/retrievers/self_query/supabase_self_query/)

  * [TF-IDF](https://python.langchain.com/docs/integrations/retrievers/tf_idf/)

  * [Tencent Cloud VectorDB](https://python.langchain.com/docs/integrations/vectorstores/tencentvectordb/)

  * [TensorFlow Datasets](https://python.langchain.com/docs/integrations/document_loaders/tensorflow_datasets/)

  * [Timescale Vector \(Postgres\)](https://python.langchain.com/docs/integrations/vectorstores/timescalevector/)

  * [Timescale Vector \(Postgres\) ](https://python.langchain.com/docs/integrations/retrievers/self_query/timescalevector_self_query/)

  * [Vectara self-querying ](https://python.langchain.com/docs/integrations/retrievers/self_query/vectara_self_query/)

  * [Vector stores and retrievers](https://python.langchain.com/docs/tutorials/retrievers/)

  * [Weaviate](https://python.langchain.com/docs/integrations/retrievers/self_query/weaviate_self_query/)

  * [Weaviate Hybrid Search](https://python.langchain.com/docs/integrations/retrievers/weaviate-hybrid/)

  * [Yellowbrick](https://python.langchain.com/docs/integrations/vectorstores/yellowbrick/)

  * [self-query-qdrant](https://python.langchain.com/docs/templates/self-query-qdrant/)

__On this page