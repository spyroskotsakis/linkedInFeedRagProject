# OpenAIEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/openai/embeddings/langchain_openai.embeddings.base.OpenAIEmbeddings.html
**Word Count:** 977
**Links Count:** 276
**Scraped:** 2025-07-21 08:27:44
**Status:** completed

---

# OpenAIEmbeddings\#

_class _langchain\_openai.embeddings.base.OpenAIEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_openai/embeddings/base.html#OpenAIEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

OpenAI embedding model integration.

Setup:     

Install `langchain_openai` and set environment variable `OPENAI_API_KEY`.               pip install -U langchain_openai     export OPENAI_API_KEY="your-api-key"     

Key init args — embedding params:     

model: str     

Name of OpenAI model to use.

dimensions: Optional\[int\] = None     

The number of dimensions the resulting output embeddings should have. Only supported in `'text-embedding-3'` and later models.

Key init args — client params:     

api\_key: Optional\[SecretStr\] = None     

OpenAI API key.

organization: Optional\[str\] = None     

OpenAI organization ID. If not passed in will be read from env var `OPENAI_ORG_ID`.

max\_retries: int = 2     

Maximum number of retries to make when generating.

request\_timeout: Optional\[Union\[float, Tuple\[float, float\], Any\]\] = None     

Timeout for requests to OpenAI completion API

See full list of supported init args and their descriptions in the params section.

Instantiate:                    from langchain_openai import OpenAIEmbeddings          embed = OpenAIEmbeddings(         model="text-embedding-3-large"         # With the `text-embedding-3` class         # of models, you can specify the size         # of the embeddings you want returned.         # dimensions=1024     )     

Embed single text:                    input_text = "The meaning of life is 42"     vector = embeddings.embed_query("hello")     print(vector[:3])                    [-0.024603435769677162, -0.007543657906353474, 0.0039630369283258915]     

Embed multiple texts:                    vectors = embeddings.embed_documents(["hello", "goodbye"])     # Showing only the first 3 coordinates     print(len(vectors))     print(vectors[0][:3])                    2     [-0.024603435769677162, -0.007543657906353474, 0.0039630369283258915]     

Async:                    await embed.aembed_query(input_text)     print(vector[:3])          # multiple:     # await embed.aembed_documents(input_texts)                    [-0.009100092574954033, 0.005071679595857859, -0.0029193938244134188]     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _allowed\_special _: Literal\['all'\] | set\[str\] | None_ _ = None_\#     

_param _check\_embedding\_ctx\_length _: bool_ _ = True_\#     

Whether to check the token length of inputs and automatically split inputs longer than embedding\_ctx\_length.

_param _chunk\_size _: int_ _ = 1000_\#     

Maximum number of texts to embed in each batch

_param _default\_headers _: Mapping\[str, str\] | None_ _ = None_\#     

_param _default\_query _: Mapping\[str, object\] | None_ _ = None_\#     

_param _deployment _: str | None_ _ = 'text-embedding-ada-002'_\#     

_param _dimensions _: int | None_ _ = None_\#     

The number of dimensions the resulting output embeddings should have.

Only supported in text-embedding-3 and later models.

_param _disallowed\_special _: Literal\['all'\] | set\[str\] | Sequence\[str\] | None_ _ = None_\#     

_param _embedding\_ctx\_length _: int_ _ = 8191_\#     

The maximum number of tokens to embed at once.

_param _headers _: Any_ _ = None_\#     

_param _http\_async\_client _: Any | None_ _ = None_\#     

Optional `httpx.AsyncClient`. Only used for async invocations. Must specify `http_client` as well if you’d like a custom client for sync invocations.

_param _http\_client _: Any | None_ _ = None_\#     

Optional `httpx.Client`. Only used for sync invocations. Must specify `http_async_client` as well if you’d like a custom client for async invocations.

_param _max\_retries _: int_ _ = 2_\#     

Maximum number of retries to make when generating.

_param _model _: str_ _ = 'text-embedding-ada-002'_\#     

_param _model\_kwargs _: dict\[str, Any\]__\[Optional\]_\#     

Holds any model parameters valid for create call not explicitly specified.

_param _openai\_api\_base _: str | None_ _\[Optional\]__\(alias 'base\_url'\)_\#     

Base URL path for API requests, leave blank if not using a proxy or service emulator.

_param _openai\_api\_key _: SecretStr | None_ _\[Optional\]__\(alias 'api\_key'\)_\#     

Automatically inferred from env var `OPENAI_API_KEY` if not provided.

_param _openai\_api\_type _: str | None_ _\[Optional\]_\#     

_param _openai\_api\_version _: str | None_ _\[Optional\]__\(alias 'api\_version'\)_\#     

Automatically inferred from env var OPENAI\_API\_VERSION if not provided.

_param _openai\_organization _: str | None_ _\[Optional\]__\(alias 'organization'\)_\#     

Automatically inferred from env var `OPENAI_ORG_ID` if not provided.

_param _openai\_proxy _: str | None_ _\[Optional\]_\#     

_param _request\_timeout _: float | tuple\[float, float\] | Any | None_ _ = None_ _\(alias 'timeout'\)_\#     

Timeout for requests to OpenAI completion API. Can be float, `httpx.Timeout` or None.

_param _retry\_max\_seconds _: int_ _ = 20_\#     

Max number of seconds to wait between retries

_param _retry\_min\_seconds _: int_ _ = 4_\#     

Min number of seconds to wait between retries

_param _show\_progress\_bar _: bool_ _ = False_\#     

Whether to show a progress bar when embedding.

_param _skip\_empty _: bool_ _ = False_\#     

Whether to skip empty strings when embedding or raise an error. Defaults to not skipping.

_param _tiktoken\_enabled _: bool_ _ = True_\#     

Set this to False for non-OpenAI implementations of the embeddings API, e.g. the `--extensions openai` extension for `text-generation-webui`

_param _tiktoken\_model\_name _: str | None_ _ = None_\#     

The model name to pass to tiktoken when using this class. Tiktoken is used to count the number of tokens in documents to constrain them to be under a certain limit. By default, when set to None, this will be the same as the embedding model name. However, there are some cases where you may want to use this Embedding class with a model name not supported by tiktoken. This can include when using Azure embeddings or when using one of the many model providers that expose an OpenAI-like API but with different models. In those cases, in order to avoid erroring when tiktoken is called, you can specify a model name to use here.

_async _aembed\_documents\(

    _texts : list\[str\]_,     _chunk\_size : int | None = None_,     _\*\* kwargs: Any_, \) → list\[list\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_openai/embeddings/base.html#OpenAIEmbeddings.aembed_documents)\#     

Call out to OpenAI’s embedding endpoint async for embedding search docs.

Parameters:     

  * **texts** \(_list_ _\[__str_ _\]_\) – The list of texts to embed.

  * **chunk\_size** \(_int_ _|__None_\) – The chunk size of embeddings. If None, will use the chunk size specified by the class.

  * **kwargs** \(_Any_\) – Additional keyword arguments to pass to the embedding API.

Returns:     

List of embeddings, one for each text.

Return type:     

list\[list\[float\]\]

_async _aembed\_query\(

    _text : str_,     _\*\* kwargs: Any_, \) → list\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_openai/embeddings/base.html#OpenAIEmbeddings.aembed_query)\#     

Call out to OpenAI’s embedding endpoint async for embedding query text.

Parameters:     

  * **text** \(_str_\) – The text to embed.

  * **kwargs** \(_Any_\) – Additional keyword arguments to pass to the embedding API.

Returns:     

Embedding for the text.

Return type:     

list\[float\]

embed\_documents\(

    _texts : list\[str\]_,     _chunk\_size : int | None = None_,     _\*\* kwargs: Any_, \) → list\[list\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_openai/embeddings/base.html#OpenAIEmbeddings.embed_documents)\#     

Call out to OpenAI’s embedding endpoint for embedding search docs.

Parameters:     

  * **texts** \(_list_ _\[__str_ _\]_\) – The list of texts to embed.

  * **chunk\_size** \(_int_ _|__None_\) – The chunk size of embeddings. If None, will use the chunk size specified by the class.

  * **kwargs** \(_Any_\) – Additional keyword arguments to pass to the embedding API.

Returns:     

List of embeddings, one for each text.

Return type:     

list\[list\[float\]\]

embed\_query\(

    _text : str_,     _\*\* kwargs: Any_, \) → list\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_openai/embeddings/base.html#OpenAIEmbeddings.embed_query)\#     

Call out to OpenAI’s embedding endpoint for embedding query text.

Parameters:     

  * **text** \(_str_\) – The text to embed.

  * **kwargs** \(_Any_\) – Additional keyword arguments to pass to the embedding API.

Returns:     

Embedding for the text.

Return type:     

list\[float\]

Examples using OpenAIEmbeddings

  * [Activeloop Deep Lake](https://python.langchain.com/docs/integrations/vectorstores/activeloop_deeplake/)

  * [Activeloop Deep Memory](https://python.langchain.com/docs/integrations/retrievers/activeloop/)

  * [Alibaba Cloud OpenSearch](https://python.langchain.com/docs/integrations/vectorstores/alibabacloud_opensearch/)

  * [Amazon Document DB](https://python.langchain.com/docs/integrations/vectorstores/documentdb/)

  * [AnalyticDB](https://python.langchain.com/docs/integrations/vectorstores/analyticdb/)

  * [Apache Cassandra](https://python.langchain.com/docs/integrations/vectorstores/cassandra/)

  * [Apache Doris](https://python.langchain.com/docs/integrations/vectorstores/apache_doris/)

  * [Apify Dataset](https://python.langchain.com/docs/integrations/document_loaders/apify_dataset/)

  * [Astra DB \(Cassandra\)](https://python.langchain.com/docs/integrations/retrievers/self_query/astradb/)

  * [Azure AI Search](https://python.langchain.com/docs/integrations/vectorstores/azuresearch/)

  * [Azure Cosmos DB Mongo vCore](https://python.langchain.com/docs/integrations/vectorstores/azure_cosmos_db/)

  * [AzureAISearchRetriever](https://python.langchain.com/docs/integrations/retrievers/azure_ai_search/)

  * [Build a PDF ingestion and Question/Answering system](https://python.langchain.com/docs/tutorials/pdf_qa/)

  * [Build a Query Analysis System](https://python.langchain.com/docs/tutorials/query_analysis/)

  * [Build a Question/Answering system over SQL data](https://python.langchain.com/docs/tutorials/sql_qa/)

  * [Build a Retrieval Augmented Generation \(RAG\) App](https://python.langchain.com/docs/tutorials/rag/)

  * [Build an Agent with AgentExecutor \(Legacy\)](https://python.langchain.com/docs/how_to/agent_executor/)

  * [Caching](https://python.langchain.com/docs/how_to/caching_embeddings/)

  * [China Mobile ECloud ElasticSearch VectorSearch](https://python.langchain.com/docs/integrations/vectorstores/ecloud_vector_search/)

  * [Chroma](https://python.langchain.com/docs/integrations/retrievers/self_query/chroma_self_query/)

  * [Confident](https://python.langchain.com/docs/integrations/callbacks/confident/)

  * [Conversational RAG](https://python.langchain.com/docs/tutorials/qa_chat_history/)

  * [Databricks Vector Search](https://python.langchain.com/docs/integrations/vectorstores/databricks_vector_search/)

  * [Deep Lake](https://python.langchain.com/docs/integrations/retrievers/self_query/activeloop_deeplake_self_query/)

  * [DingoDB](https://python.langchain.com/docs/integrations/vectorstores/dingo/)

  * [DocArray](https://python.langchain.com/docs/integrations/retrievers/docarray_retriever/)

  * [DocArray HnswSearch](https://python.langchain.com/docs/integrations/vectorstores/docarray_hnsw/)

  * [DocArray InMemorySearch](https://python.langchain.com/docs/integrations/vectorstores/docarray_in_memory/)

  * [Docugami](https://python.langchain.com/docs/integrations/document_loaders/docugami/)

  * [DuckDB](https://python.langchain.com/docs/integrations/vectorstores/duckdb/)

  * [Elasticsearch](https://python.langchain.com/docs/integrations/retrievers/self_query/elasticsearch_self_query/)

  * [Epsilla](https://python.langchain.com/docs/integrations/vectorstores/epsilla/)

  * [Faiss \(Async\)](https://python.langchain.com/docs/integrations/vectorstores/faiss_async/)

  * [FlashRank reranker](https://python.langchain.com/docs/integrations/retrievers/flashrank-reranker/)

  * [Fleet AI Context](https://python.langchain.com/docs/integrations/retrievers/fleet_context/)

  * [Hippo](https://python.langchain.com/docs/integrations/vectorstores/hippo/)

  * [Hologres](https://python.langchain.com/docs/integrations/vectorstores/hologres/)

  * [How deal with high cardinality categoricals when doing query analysis](https://python.langchain.com/docs/how_to/query_high_cardinality/)

  * [How to add chat history](https://python.langchain.com/docs/how_to/qa_chat_history_how_to/)

  * [How to add retrieval to chatbots](https://python.langchain.com/docs/how_to/chatbots_retrieval/)

  * [How to add scores to retriever results](https://python.langchain.com/docs/how_to/add_scores_retriever/)

  * [How to add values to a chain’s state](https://python.langchain.com/docs/how_to/assign/)

  * [How to best prompt for Graph-RAG](https://python.langchain.com/docs/how_to/graph_prompting/)

  * [How to better prompt when doing SQL question-answering](https://python.langchain.com/docs/how_to/sql_prompting/)

  * [How to combine results from multiple retrievers](https://python.langchain.com/docs/how_to/ensemble_retriever/)

  * [How to convert Runnables as Tools](https://python.langchain.com/docs/how_to/convert_runnable_to_tool/)

  * [How to create and query vector stores](https://python.langchain.com/docs/how_to/vectorstores/)

  * [How to deal with large databases when doing SQL question-answering](https://python.langchain.com/docs/how_to/sql_large_db/)

  * [How to do “self-querying” retrieval](https://python.langchain.com/docs/how_to/self_query/)

  * [How to do per-user retrieval](https://python.langchain.com/docs/how_to/qa_per_user/)

  * [How to do retrieval with contextual compression](https://python.langchain.com/docs/how_to/contextual_compression/)

  * [How to get a RAG application to add citations](https://python.langchain.com/docs/how_to/qa_citations/)

  * [How to get your RAG application to return sources](https://python.langchain.com/docs/how_to/qa_sources/)

  * [How to handle cases where no queries are generated](https://python.langchain.com/docs/how_to/query_no_queries/)

  * [How to handle long text when doing extraction](https://python.langchain.com/docs/how_to/extraction_long_text/)

  * [How to handle multiple queries when doing query analysis](https://python.langchain.com/docs/how_to/query_multiple_queries/)

  * [How to handle multiple retrievers when doing query analysis](https://python.langchain.com/docs/how_to/query_multiple_retrievers/)

  * [How to inspect runnables](https://python.langchain.com/docs/how_to/inspect/)

  * [How to invoke runnables in parallel](https://python.langchain.com/docs/how_to/parallel/)

  * [How to load PDFs](https://python.langchain.com/docs/how_to/document_loader_pdf/)

  * [How to pass through arguments from one step to the next](https://python.langchain.com/docs/how_to/passthrough/)

  * [How to retrieve using multiple vectors per document](https://python.langchain.com/docs/how_to/multi_vector/)

  * [How to route between sub-chains](https://python.langchain.com/docs/how_to/routing/)

  * [How to select examples by maximal marginal relevance \(MMR\)](https://python.langchain.com/docs/how_to/example_selectors_mmr/)

  * [How to select examples by similarity](https://python.langchain.com/docs/how_to/example_selectors_similarity/)

  * [How to split text based on semantic similarity](https://python.langchain.com/docs/how_to/semantic-chunker/)

  * [How to stream results from your RAG application](https://python.langchain.com/docs/how_to/qa_streaming/)

  * [How to stream runnables](https://python.langchain.com/docs/how_to/streaming/)

  * [How to use a time-weighted vector store retriever](https://python.langchain.com/docs/how_to/time_weighted_vectorstore/)

  * [How to use a vectorstore as a retriever](https://python.langchain.com/docs/how_to/vectorstore_retriever/)

  * [How to use few shot examples](https://python.langchain.com/docs/how_to/few_shot_examples/)

  * [How to use few shot examples in chat models](https://python.langchain.com/docs/how_to/few_shot_examples_chat/)

  * [How to use the LangChain indexing API](https://python.langchain.com/docs/how_to/indexing/)

  * [How to use the MultiQueryRetriever](https://python.langchain.com/docs/how_to/MultiQueryRetriever/)

  * [How to use the Parent Document Retriever](https://python.langchain.com/docs/how_to/parent_document_retriever/)

  * [Hybrid Search](https://python.langchain.com/docs/how_to/hybrid/)

  * [Identity-enabled RAG using PebbloRetrievalQA](https://python.langchain.com/docs/integrations/providers/pebblo/pebblo_retrieval_qa/)

  * [Image captions](https://python.langchain.com/docs/integrations/document_loaders/image_captions/)

  * [Jaguar Vector Database](https://python.langchain.com/docs/integrations/vectorstores/jaguar/)

  * [JaguarDB Vector Database](https://python.langchain.com/docs/integrations/retrievers/jaguar/)

  * [Javelin AI Gateway](https://python.langchain.com/docs/integrations/providers/javelin_ai_gateway/)

  * [KDB.AI](https://python.langchain.com/docs/integrations/vectorstores/kdbai/)

  * [Kinetica Vectorstore API](https://python.langchain.com/docs/integrations/vectorstores/kinetica/)

  * [Kinetica Vectorstore based Retriever](https://python.langchain.com/docs/integrations/retrievers/kinetica/)

  * [LLMLingua Document Compressor](https://python.langchain.com/docs/integrations/retrievers/llmlingua/)

  * [LOTR \(Merger Retriever\)](https://python.langchain.com/docs/integrations/retrievers/merger_retriever/)

  * [LanceDB](https://python.langchain.com/docs/integrations/vectorstores/lancedb/)

  * [Lantern](https://python.langchain.com/docs/integrations/vectorstores/lantern/)

  * [Load docs](https://python.langchain.com/docs/versions/migrating_chains/retrieval_qa/)

  * [Meilisearch](https://python.langchain.com/docs/integrations/vectorstores/meilisearch/)

  * [Milvus](https://python.langchain.com/docs/integrations/retrievers/self_query/milvus_self_query/)

  * [Milvus Hybrid Search Retriever](https://python.langchain.com/docs/integrations/retrievers/milvus_hybrid_search/)

  * [Model caches](https://python.langchain.com/docs/integrations/llm_caching/)

  * [Momento Vector Index \(MVI\)](https://python.langchain.com/docs/integrations/vectorstores/momento_vector_index/)

  * [MongoDB Atlas](https://python.langchain.com/docs/integrations/retrievers/self_query/mongodb_atlas/)

  * [MyScale](https://python.langchain.com/docs/integrations/vectorstores/myscale/)

  * [Neo4j Vector Index](https://python.langchain.com/docs/integrations/vectorstores/neo4jvector/)

  * [OpenAI](https://python.langchain.com/docs/integrations/providers/openai/)

  * [OpenAIEmbeddings](https://python.langchain.com/docs/integrations/text_embedding/openai/)

  * [OpenSearch](https://python.langchain.com/docs/integrations/vectorstores/opensearch/)

  * [PGVector \(Postgres\)](https://python.langchain.com/docs/integrations/retrievers/self_query/pgvector_self_query/)

  * [Pinecone](https://python.langchain.com/docs/integrations/retrievers/self_query/pinecone/)

  * [Pinecone Hybrid Search](https://python.langchain.com/docs/integrations/retrievers/pinecone_hybrid_search/)

  * [Postgres Embedding](https://python.langchain.com/docs/integrations/vectorstores/pgembedding/)

  * [Psychic](https://python.langchain.com/docs/integrations/document_loaders/psychic/)

  * [Qdrant](https://python.langchain.com/docs/integrations/retrievers/self_query/qdrant_self_query/)

  * [RAGatouille](https://python.langchain.com/docs/integrations/providers/ragatouille/)

  * [RankLLM Reranker](https://python.langchain.com/docs/integrations/document_transformers/rankllm-reranker/)

  * [RePhraseQuery](https://python.langchain.com/docs/integrations/retrievers/re_phrase/)

  * [Redis](https://python.langchain.com/docs/integrations/retrievers/self_query/redis_self_query/)

  * [Rockset](https://python.langchain.com/docs/integrations/vectorstores/rockset/)

  * [SAP HANA Cloud Vector Engine](https://python.langchain.com/docs/integrations/vectorstores/sap_hanavector/)

  * [SVM](https://python.langchain.com/docs/integrations/retrievers/svm/)

  * [SingleStoreDB](https://python.langchain.com/docs/integrations/vectorstores/singlestoredb/)

  * [StarRocks](https://python.langchain.com/docs/integrations/vectorstores/starrocks/)

  * [Supabase \(Postgres\)](https://python.langchain.com/docs/integrations/vectorstores/supabase/)

  * [Tencent Cloud VectorDB](https://python.langchain.com/docs/integrations/vectorstores/tencentvectordb/)

  * [Text embedding models](https://python.langchain.com/docs/how_to/embed_text/)

  * [TiDB Vector](https://python.langchain.com/docs/integrations/vectorstores/tidb_vector/)

  * [Tigris](https://python.langchain.com/docs/integrations/vectorstores/tigris/)

  * [Timescale Vector \(Postgres\)](https://python.langchain.com/docs/integrations/vectorstores/timescalevector/)

  * [Timescale Vector \(Postgres\) ](https://python.langchain.com/docs/integrations/retrievers/self_query/timescalevector_self_query/)

  * [Typesense](https://python.langchain.com/docs/integrations/vectorstores/typesense/)

  * [USearch](https://python.langchain.com/docs/integrations/vectorstores/usearch/)

  * [UpTrain](https://python.langchain.com/docs/integrations/callbacks/uptrain/)

  * [Upstash Vector](https://python.langchain.com/docs/integrations/vectorstores/upstash/)

  * [Vector stores and retrievers](https://python.langchain.com/docs/tutorials/retrievers/)

  * [Weaviate](https://python.langchain.com/docs/integrations/vectorstores/weaviate/)

  * [Xata](https://python.langchain.com/docs/integrations/vectorstores/xata/)

  * [Yellowbrick](https://python.langchain.com/docs/integrations/vectorstores/yellowbrick/)

  * [YouTube audio](https://python.langchain.com/docs/integrations/document_loaders/youtube_audio/)

  * [Zilliz](https://python.langchain.com/docs/integrations/vectorstores/zilliz/)

  * [kNN](https://python.langchain.com/docs/integrations/retrievers/knn/)

  * [scikit-learn](https://python.langchain.com/docs/integrations/vectorstores/sklearn/)

  * [viking DB](https://python.langchain.com/docs/integrations/vectorstores/vikingdb/)

__On this page