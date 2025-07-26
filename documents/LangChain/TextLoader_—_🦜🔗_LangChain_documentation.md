# TextLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.text.TextLoader.html
**Word Count:** 243
**Links Count:** 509
**Scraped:** 2025-07-21 08:11:39
**Status:** completed

---

# TextLoader\#

_class _langchain\_community.document\_loaders.text.TextLoader\(

    _file\_path : str | Path_,     _encoding : str | None = None_,     _autodetect\_encoding : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/text.html#TextLoader)\#     

Load text file.

Parameters:     

  * **file\_path** \(_str_ _|__Path_\) – Path to the file to load.

  * **encoding** \(_str_ _|__None_\) – File encoding to use. If None, the file will be loaded

  * **encoding.** \(_with the default system_\)

  * **autodetect\_encoding** \(_bool_\) – Whether to try to autodetect the file encoding if the specified encoding fails.

Initialize with file path.

Methods

`__init__`\(file\_path\[, encoding, ...\]\) | Initialize with file path.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Load from file path.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _file\_path : str | Path_,     _encoding : str | None = None_,     _autodetect\_encoding : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/text.html#TextLoader.__init__)\#     

Initialize with file path.

Parameters:     

  * **file\_path** \(_str_ _|__Path_\)

  * **encoding** \(_str_ _|__None_\)

  * **autodetect\_encoding** \(_bool_\)

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/text.html#TextLoader.lazy_load)\#     

Load from file path.

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\_and\_split\(

    _text\_splitter : [TextSplitter](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html#langchain_text_splitters.base.TextSplitter "langchain_text_splitters.base.TextSplitter") | None = None_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load Documents and split into chunks. Chunks are returned as Documents.

Do not override this method. It should be considered to be deprecated\!

Parameters:     

**text\_splitter** \(_Optional_ _\[_[_TextSplitter_](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html#langchain_text_splitters.base.TextSplitter "langchain_text_splitters.base.TextSplitter") _\]_\) – TextSplitter instance to use for splitting documents. Defaults to RecursiveCharacterTextSplitter.

Returns:     

List of Documents.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Examples using TextLoader

  * [Activeloop Deep Lake](https://python.langchain.com/docs/integrations/vectorstores/activeloop_deeplake/)

  * [Alibaba Cloud OpenSearch](https://python.langchain.com/docs/integrations/vectorstores/alibabacloud_opensearch/)

  * [Amazon Document DB](https://python.langchain.com/docs/integrations/vectorstores/documentdb/)

  * [AnalyticDB](https://python.langchain.com/docs/integrations/vectorstores/analyticdb/)

  * [Annoy](https://python.langchain.com/docs/integrations/vectorstores/annoy/)

  * [Atlas](https://python.langchain.com/docs/integrations/vectorstores/atlas/)

  * [AwaDB](https://python.langchain.com/docs/integrations/vectorstores/awadb/)

  * [Azure AI Search](https://python.langchain.com/docs/integrations/vectorstores/azuresearch/)

  * [Azure Cosmos DB Mongo vCore](https://python.langchain.com/docs/integrations/vectorstores/azure_cosmos_db/)

  * [AzureAISearchRetriever](https://python.langchain.com/docs/integrations/retrievers/azure_ai_search/)

  * [Bagel](https://python.langchain.com/docs/integrations/vectorstores/bagel/)

  * [BagelDB](https://python.langchain.com/docs/integrations/vectorstores/bageldb/)

  * [Baidu Cloud ElasticSearch VectorSearch](https://python.langchain.com/docs/integrations/vectorstores/baiducloud_vector_search/)

  * [Baidu VectorDB](https://python.langchain.com/docs/integrations/vectorstores/baiduvectordb/)

  * [Caching](https://python.langchain.com/docs/how_to/caching_embeddings/)

  * [China Mobile ECloud ElasticSearch VectorSearch](https://python.langchain.com/docs/integrations/vectorstores/ecloud_vector_search/)

  * [Clarifai](https://python.langchain.com/docs/integrations/vectorstores/clarifai/)

  * [Cohere reranker](https://python.langchain.com/docs/integrations/retrievers/cohere-reranker/)

  * [Confident](https://python.langchain.com/docs/integrations/callbacks/confident/)

  * [Couchbase ](https://python.langchain.com/docs/integrations/vectorstores/couchbase/)

  * [Cross Encoder Reranker](https://python.langchain.com/docs/integrations/document_transformers/cross_encoder_reranker/)

  * [DashScope Reranker](https://python.langchain.com/docs/integrations/document_transformers/dashscope_rerank/)

  * [DashVector](https://python.langchain.com/docs/integrations/vectorstores/dashvector/)

  * [Databricks Vector Search](https://python.langchain.com/docs/integrations/vectorstores/databricks_vector_search/)

  * [DingoDB](https://python.langchain.com/docs/integrations/vectorstores/dingo/)

  * [DocArray HnswSearch](https://python.langchain.com/docs/integrations/vectorstores/docarray_hnsw/)

  * [DocArray InMemorySearch](https://python.langchain.com/docs/integrations/vectorstores/docarray_in_memory/)

  * [DuckDB](https://python.langchain.com/docs/integrations/vectorstores/duckdb/)

  * [Epsilla](https://python.langchain.com/docs/integrations/vectorstores/epsilla/)

  * [Faiss \(Async\)](https://python.langchain.com/docs/integrations/vectorstores/faiss_async/)

  * [FlashRank reranker](https://python.langchain.com/docs/integrations/retrievers/flashrank-reranker/)

  * [Google Memorystore for Redis](https://python.langchain.com/docs/integrations/vectorstores/google_memorystore_redis/)

  * [Hippo](https://python.langchain.com/docs/integrations/vectorstores/hippo/)

  * [Hologres](https://python.langchain.com/docs/integrations/vectorstores/hologres/)

  * [How to create and query vector stores](https://python.langchain.com/docs/how_to/vectorstores/)

  * [How to do retrieval with contextual compression](https://python.langchain.com/docs/how_to/contextual_compression/)

  * [How to load documents from a directory](https://python.langchain.com/docs/how_to/document_loader_directory/)

  * [How to retrieve using multiple vectors per document](https://python.langchain.com/docs/how_to/multi_vector/)

  * [How to use a vectorstore as a retriever](https://python.langchain.com/docs/how_to/vectorstore_retriever/)

  * [How to use the Parent Document Retriever](https://python.langchain.com/docs/how_to/parent_document_retriever/)

  * [Intel’s Visual Data Management System \(VDMS\)](https://python.langchain.com/docs/integrations/vectorstores/vdms/)

  * [Jaguar Vector Database](https://python.langchain.com/docs/integrations/vectorstores/jaguar/)

  * [JaguarDB Vector Database](https://python.langchain.com/docs/integrations/retrievers/jaguar/)

  * [Jina Reranker](https://python.langchain.com/docs/integrations/document_transformers/jina_rerank/)

  * [Kinetica Vectorstore API](https://python.langchain.com/docs/integrations/vectorstores/kinetica/)

  * [Kinetica Vectorstore based Retriever](https://python.langchain.com/docs/integrations/retrievers/kinetica/)

  * [LLMLingua Document Compressor](https://python.langchain.com/docs/integrations/retrievers/llmlingua/)

  * [LanceDB](https://python.langchain.com/docs/integrations/vectorstores/lancedb/)

  * [Lantern](https://python.langchain.com/docs/integrations/vectorstores/lantern/)

  * [ManticoreSearch VectorStore](https://python.langchain.com/docs/integrations/vectorstores/manticore_search/)

  * [Marqo](https://python.langchain.com/docs/integrations/vectorstores/marqo/)

  * [Meilisearch](https://python.langchain.com/docs/integrations/vectorstores/meilisearch/)

  * [Momento Vector Index \(MVI\)](https://python.langchain.com/docs/integrations/vectorstores/momento_vector_index/)

  * [MyScale](https://python.langchain.com/docs/integrations/vectorstores/myscale/)

  * [Neo4j Vector Index](https://python.langchain.com/docs/integrations/vectorstores/neo4jvector/)

  * [OpenSearch](https://python.langchain.com/docs/integrations/vectorstores/opensearch/)

  * [OpenVINO Reranker](https://python.langchain.com/docs/integrations/document_transformers/openvino_rerank/)

  * [PGVecto.rs](https://python.langchain.com/docs/integrations/vectorstores/pgvecto_rs/)

  * [Postgres Embedding](https://python.langchain.com/docs/integrations/vectorstores/pgembedding/)

  * [RankLLM Reranker](https://python.langchain.com/docs/integrations/document_transformers/rankllm-reranker/)

  * [Relyt](https://python.langchain.com/docs/integrations/vectorstores/relyt/)

  * [Rockset](https://python.langchain.com/docs/integrations/vectorstores/rockset/)

  * [SAP HANA Cloud Vector Engine](https://python.langchain.com/docs/integrations/vectorstores/sap_hanavector/)

  * [SQLite-VSS](https://python.langchain.com/docs/integrations/vectorstores/sqlitevss/)

  * [ScaNN](https://python.langchain.com/docs/integrations/vectorstores/scann/)

  * [SemaDB](https://python.langchain.com/docs/integrations/vectorstores/semadb/)

  * [SingleStoreDB](https://python.langchain.com/docs/integrations/retrievers/singlestoredb/)

  * [Supabase \(Postgres\)](https://python.langchain.com/docs/integrations/vectorstores/supabase/)

  * [SurrealDB](https://python.langchain.com/docs/integrations/vectorstores/surrealdb/)

  * [Tair](https://python.langchain.com/docs/integrations/vectorstores/tair/)

  * [Tencent Cloud VectorDB](https://python.langchain.com/docs/integrations/vectorstores/tencentvectordb/)

  * [TiDB Vector](https://python.langchain.com/docs/integrations/vectorstores/tidb_vector/)

  * [Tigris](https://python.langchain.com/docs/integrations/vectorstores/tigris/)

  * [TileDB](https://python.langchain.com/docs/integrations/vectorstores/tiledb/)

  * [Timescale Vector \(Postgres\)](https://python.langchain.com/docs/integrations/vectorstores/timescalevector/)

  * [Typesense](https://python.langchain.com/docs/integrations/vectorstores/typesense/)

  * [USearch](https://python.langchain.com/docs/integrations/vectorstores/usearch/)

  * [UpTrain](https://python.langchain.com/docs/integrations/callbacks/uptrain/)

  * [Upstash Vector](https://python.langchain.com/docs/integrations/vectorstores/upstash/)

  * [VDMS](https://python.langchain.com/docs/integrations/providers/vdms/)

  * [Vald](https://python.langchain.com/docs/integrations/vectorstores/vald/)

  * [Vearch](https://python.langchain.com/docs/integrations/vectorstores/vearch/)

  * [Vectara Chat](https://python.langchain.com/docs/integrations/providers/vectara/vectara_chat/)

  * [Vespa](https://python.langchain.com/docs/integrations/vectorstores/vespa/)

  * [Volcengine Reranker](https://python.langchain.com/docs/integrations/document_transformers/volcengine_rerank/)

  * [VoyageAI Reranker](https://python.langchain.com/docs/integrations/document_transformers/voyageai-reranker/)

  * [Weaviate](https://python.langchain.com/docs/integrations/vectorstores/weaviate/)

  * [Xata](https://python.langchain.com/docs/integrations/vectorstores/xata/)

  * [Zilliz](https://python.langchain.com/docs/integrations/vectorstores/zilliz/)

  * [scikit-learn](https://python.langchain.com/docs/integrations/vectorstores/sklearn/)

  * [viking DB](https://python.langchain.com/docs/integrations/vectorstores/vikingdb/)

  * [vlite](https://python.langchain.com/docs/integrations/vectorstores/vlite/)

__On this page