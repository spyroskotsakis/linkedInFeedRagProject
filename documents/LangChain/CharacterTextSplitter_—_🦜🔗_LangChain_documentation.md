# CharacterTextSplitter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/text_splitters/character/langchain_text_splitters.character.CharacterTextSplitter.html
**Word Count:** 241
**Links Count:** 208
**Scraped:** 2025-07-21 07:58:09
**Status:** completed

---

# CharacterTextSplitter\#

_class _langchain\_text\_splitters.character.CharacterTextSplitter\(

    _separator : str = '\n\n'_,     _is\_separator\_regex : bool = False_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/character.html#CharacterTextSplitter)\#     

Splitting text that looks at characters.

Create a new TextSplitter.

Methods

`__init__`\(\[separator, is\_separator\_regex\]\) | Create a new TextSplitter.   ---|---   `atransform_documents`\(documents, \*\*kwargs\) | Asynchronously transform a list of documents.   `create_documents`\(texts\[, metadatas\]\) | Create documents from a list of texts.   `from_huggingface_tokenizer`\(tokenizer, \*\*kwargs\) | Text splitter that uses HuggingFace tokenizer to count length.   `from_tiktoken_encoder`\(\[encoding\_name, ...\]\) | Text splitter that uses tiktoken encoder to count length.   `split_documents`\(documents\) | Split documents.   `split_text`\(text\) | Split into chunks without re-inserting lookaround separators.   `transform_documents`\(documents, \*\*kwargs\) | Transform sequence of documents by splitting them.      Parameters:     

  * **separator** \(_str_\)

  * **is\_separator\_regex** \(_bool_\)

  * **kwargs** \(_Any_\)

\_\_init\_\_\(

    _separator : str = '\n\n'_,     _is\_separator\_regex : bool = False_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/character.html#CharacterTextSplitter.__init__)\#     

Create a new TextSplitter.

Parameters:     

  * **separator** \(_str_\)

  * **is\_separator\_regex** \(_bool_\)

  * **kwargs** \(_Any_\)

Return type:     

None

_async _atransform\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Asynchronously transform a list of documents.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – A sequence of Documents to be transformed.

  * **kwargs** \(_Any_\)

Returns:     

A sequence of transformed Documents.

Return type:     

Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

create\_documents\(

    _texts : list\[str\]_,     _metadatas : list\[dict\[Any, Any\]\] | None = None_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Create documents from a list of texts.

Parameters:     

  * **texts** \(_list_ _\[__str_ _\]_\)

  * **metadatas** \(_list_ _\[__dict_ _\[__Any_ _,__Any_ _\]__\]__|__None_\)

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_classmethod _from\_huggingface\_tokenizer\(

    _tokenizer : Any_,     _\*\* kwargs: Any_, \) → [TextSplitter](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html#langchain_text_splitters.base.TextSplitter "langchain_text_splitters.base.TextSplitter")\#     

Text splitter that uses HuggingFace tokenizer to count length.

Parameters:     

  * **tokenizer** \(_Any_\)

  * **kwargs** \(_Any_\)

Return type:     

[_TextSplitter_](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html#langchain_text_splitters.base.TextSplitter "langchain_text_splitters.base.TextSplitter")

_classmethod _from\_tiktoken\_encoder\(

    _encoding\_name : str = 'gpt2'_,     _model\_name : str | None = None_,     _allowed\_special : Literal\['all'\] | Set\[str\] = \{\}_,     _disallowed\_special : Literal\['all'\] | Collection\[str\] = 'all'_,     _\*\* kwargs: Any_, \) → TS\#     

Text splitter that uses tiktoken encoder to count length.

Parameters:     

  * **encoding\_name** \(_str_\)

  * **model\_name** \(_str_ _|__None_\)

  * **allowed\_special** \(_Literal_ _\[__'all'__\]__|__~collections.abc.Set_ _\[__str_ _\]_\)

  * **disallowed\_special** \(_Literal_ _\[__'all'__\]__|__~collections.abc.Collection_ _\[__str_ _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

_TS_

split\_documents\(

    _documents : Iterable\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Split documents.

Parameters:     

**documents** \(_Iterable_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

split\_text\(_text : str_\) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/character.html#CharacterTextSplitter.split_text)\#     

Split into chunks without re-inserting lookaround separators.

Parameters:     

**text** \(_str_\)

Return type:     

list\[str\]

transform\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Transform sequence of documents by splitting them.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

_Sequence_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Examples using CharacterTextSplitter

  * [\# Basic example \(short documents\)](https://python.langchain.com/docs/versions/migrating_chains/map_reduce_chain/)

  * [Activeloop Deep Lake](https://python.langchain.com/docs/integrations/vectorstores/activeloop_deeplake/)

  * [Alibaba Cloud OpenSearch](https://python.langchain.com/docs/integrations/vectorstores/alibabacloud_opensearch/)

  * [Amazon Document DB](https://python.langchain.com/docs/integrations/vectorstores/documentdb/)

  * [AnalyticDB](https://python.langchain.com/docs/integrations/vectorstores/analyticdb/)

  * [Annoy](https://python.langchain.com/docs/integrations/vectorstores/annoy/)

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

  * [Confident](https://python.langchain.com/docs/integrations/callbacks/confident/)

  * [Couchbase ](https://python.langchain.com/docs/integrations/vectorstores/couchbase/)

  * [DashVector](https://python.langchain.com/docs/integrations/vectorstores/dashvector/)

  * [Databricks Vector Search](https://python.langchain.com/docs/integrations/vectorstores/databricks_vector_search/)

  * [DingoDB](https://python.langchain.com/docs/integrations/vectorstores/dingo/)

  * [DocArray HnswSearch](https://python.langchain.com/docs/integrations/vectorstores/docarray_hnsw/)

  * [DocArray InMemorySearch](https://python.langchain.com/docs/integrations/vectorstores/docarray_in_memory/)

  * [DuckDB](https://python.langchain.com/docs/integrations/vectorstores/duckdb/)

  * [Epsilla](https://python.langchain.com/docs/integrations/vectorstores/epsilla/)

  * [Faiss \(Async\)](https://python.langchain.com/docs/integrations/vectorstores/faiss_async/)

  * [Google Memorystore for Redis](https://python.langchain.com/docs/integrations/vectorstores/google_memorystore_redis/)

  * [Hippo](https://python.langchain.com/docs/integrations/vectorstores/hippo/)

  * [Hologres](https://python.langchain.com/docs/integrations/vectorstores/hologres/)

  * [How to create and query vector stores](https://python.langchain.com/docs/how_to/vectorstores/)

  * [How to do retrieval with contextual compression](https://python.langchain.com/docs/how_to/contextual_compression/)

  * [How to handle long text when doing extraction](https://python.langchain.com/docs/how_to/extraction_long_text/)

  * [How to split by character](https://python.langchain.com/docs/how_to/character_text_splitter/)

  * [How to split text by tokens ](https://python.langchain.com/docs/how_to/split_by_token/)

  * [How to summarize text through parallelization](https://python.langchain.com/docs/how_to/summarize_map_reduce/)

  * [How to use a vectorstore as a retriever](https://python.langchain.com/docs/how_to/vectorstore_retriever/)

  * [How to use the LangChain indexing API](https://python.langchain.com/docs/how_to/indexing/)

  * [Intel’s Visual Data Management System \(VDMS\)](https://python.langchain.com/docs/integrations/vectorstores/vdms/)

  * [Jaguar Vector Database](https://python.langchain.com/docs/integrations/vectorstores/jaguar/)

  * [JaguarDB Vector Database](https://python.langchain.com/docs/integrations/retrievers/jaguar/)

  * [Kinetica Vectorstore API](https://python.langchain.com/docs/integrations/vectorstores/kinetica/)

  * [Kinetica Vectorstore based Retriever](https://python.langchain.com/docs/integrations/retrievers/kinetica/)

  * [LanceDB](https://python.langchain.com/docs/integrations/vectorstores/lancedb/)

  * [Lantern](https://python.langchain.com/docs/integrations/vectorstores/lantern/)

  * [Manifest](https://python.langchain.com/docs/integrations/llms/manifest/)

  * [ManticoreSearch VectorStore](https://python.langchain.com/docs/integrations/vectorstores/manticore_search/)

  * [Marqo](https://python.langchain.com/docs/integrations/vectorstores/marqo/)

  * [Meilisearch](https://python.langchain.com/docs/integrations/vectorstores/meilisearch/)

  * [Model caches](https://python.langchain.com/docs/integrations/llm_caching/)

  * [Momento Vector Index \(MVI\)](https://python.langchain.com/docs/integrations/vectorstores/momento_vector_index/)

  * [MyScale](https://python.langchain.com/docs/integrations/vectorstores/myscale/)

  * [Neo4j Vector Index](https://python.langchain.com/docs/integrations/vectorstores/neo4jvector/)

  * [OpenAI](https://python.langchain.com/docs/integrations/providers/openai/)

  * [OpenSearch](https://python.langchain.com/docs/integrations/vectorstores/opensearch/)

  * [PGVecto.rs](https://python.langchain.com/docs/integrations/vectorstores/pgvecto_rs/)

  * [Postgres Embedding](https://python.langchain.com/docs/integrations/vectorstores/pgembedding/)

  * [Psychic](https://python.langchain.com/docs/integrations/document_loaders/psychic/)

  * [Relyt](https://python.langchain.com/docs/integrations/vectorstores/relyt/)

  * [Rockset](https://python.langchain.com/docs/integrations/vectorstores/rockset/)

  * [SAP HANA Cloud Vector Engine](https://python.langchain.com/docs/integrations/vectorstores/sap_hanavector/)

  * [SQLite-VSS](https://python.langchain.com/docs/integrations/vectorstores/sqlitevss/)

  * [ScaNN](https://python.langchain.com/docs/integrations/vectorstores/scann/)

  * [SemaDB](https://python.langchain.com/docs/integrations/vectorstores/semadb/)

  * [SingleStoreDB](https://python.langchain.com/docs/integrations/retrievers/singlestoredb/)

  * [Summarize Text](https://python.langchain.com/docs/tutorials/summarization/)

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

  * [Upstash Vector](https://python.langchain.com/docs/integrations/vectorstores/upstash/)

  * [VDMS](https://python.langchain.com/docs/integrations/providers/vdms/)

  * [Vald](https://python.langchain.com/docs/integrations/vectorstores/vald/)

  * [Vespa](https://python.langchain.com/docs/integrations/vectorstores/vespa/)

  * [Weaviate](https://python.langchain.com/docs/integrations/vectorstores/weaviate/)

  * [Xata](https://python.langchain.com/docs/integrations/vectorstores/xata/)

  * [Zilliz](https://python.langchain.com/docs/integrations/vectorstores/zilliz/)

  * [scikit-learn](https://python.langchain.com/docs/integrations/vectorstores/sklearn/)

  * [vlite](https://python.langchain.com/docs/integrations/vectorstores/vlite/)

__On this page