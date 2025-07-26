# PineconeSparseEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/pinecone/embeddings/langchain_pinecone.embeddings.PineconeSparseEmbeddings.html
**Word Count:** 184
**Links Count:** 102
**Scraped:** 2025-07-21 08:00:23
**Status:** completed

---

# PineconeSparseEmbeddings\#

_class _langchain\_pinecone.embeddings.PineconeSparseEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_pinecone/embeddings.html#PineconeSparseEmbeddings)\#     

Bases: [`PineconeEmbeddings`](https://python.langchain.com/api_reference/pinecone/embeddings/langchain_pinecone.embeddings.PineconeEmbeddings.html#langchain_pinecone.embeddings.PineconeEmbeddings "langchain_pinecone.embeddings.PineconeEmbeddings")

PineconeSparseEmbeddings embedding model.

Example               from langchain_pinecone import PineconeSparseEmbeddings     from langchain_pinecone import PineconeVectorStore     from langchain_core.documents import Document          # Initialize sparse embeddings     sparse_embeddings = PineconeSparseEmbeddings(model="pinecone-sparse-english-v0")          # Embed a single query (returns SparseValues)     query_embedding = sparse_embeddings.embed_query("What is machine learning?")     # query_embedding contains SparseValues with indices and values          # Embed multiple documents     docs = ["Document 1 content", "Document 2 content"]     doc_embeddings = sparse_embeddings.embed_documents(docs)          # Use with an index configured for sparse vectors     from pinecone import Pinecone          pc = Pinecone(api_key="your-api-key")          # Create index with sparse embeddings support     if not pc.has_index("sparse-index"):         pc.create_index_for_model(             name="sparse-index",             cloud="aws",             region="us-east-1",             embed={                 "model": "pinecone-sparse-english-v0",                 "field_map": {"text": "chunk_text"},                 "metric": "dotproduct",                 "read_parameters": {},                 "write_parameters": {}             }         )          index = pc.Index("sparse-index")          # IMPORTANT: Use PineconeSparseVectorStore for sparse vectors     # The regular PineconeVectorStore won't work with sparse embeddings     from langchain_pinecone.vectorstores_sparse import PineconeSparseVectorStore          # Initialize sparse vector store with sparse embeddings     vector_store = PineconeSparseVectorStore(         index=index,         embedding=sparse_embeddings     )          # Add documents     from uuid import uuid4          documents = [         Document(page_content="Machine learning is awesome", metadata={"source": "article"}),         Document(page_content="Neural networks power modern AI", metadata={"source": "book"})     ]          # Generate unique IDs for each document     uuids = [str(uuid4()) for _ in range(len(documents))]          # Add documents to the vector store     vector_store.add_documents(documents=documents, ids=uuids)          # Search for similar documents     results = vector_store.similarity_search("machine learning", k=2)     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _batch\_size _: int | None_ _ = None_\#     

Batch size for embedding documents.

_param _dimension _: int | None_ _ = None_\#     

_param _document\_params _: Dict_ _\[Optional\]_\#     

Parameters for embedding document

_param _model _: str_ _\[Required\]_\#     

Model to use for example ‘multilingual-e5-large’.

_param _pinecone\_api\_key _: SecretStr_ _\[Optional\]__\(alias 'api\_key'\)_\#     

Pinecone API key.

If not provided, will look for the PINECONE\_API\_KEY environment variable.

_param _query\_params _: Dict_ _\[Optional\]_\#     

Parameters for embedding query.

_param _show\_progress\_bar _: bool_ _ = False_\#     

_async _aembed\_documents\(

    _texts : List\[str\]_, \) → List\[SparseValues\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_pinecone/embeddings.html#PineconeSparseEmbeddings.aembed_documents)\#     

Asynchronously embed search docs with sparse embeddings.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\)

Return type:     

_List_\[_SparseValues_\]

_async _aembed\_query\(

    _text : str_, \) → SparseValues[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_pinecone/embeddings.html#PineconeSparseEmbeddings.aembed_query)\#     

Asynchronously embed query text with sparse embeddings.

Parameters:     

**text** \(_str_\)

Return type:     

_SparseValues_

embed\_documents\(

    _texts : List\[str\]_, \) → List\[SparseValues\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_pinecone/embeddings.html#PineconeSparseEmbeddings.embed_documents)\#     

Embed search docs with sparse embeddings.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\)

Return type:     

_List_\[_SparseValues_\]

embed\_query\(

    _text : str_, \) → SparseValues[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_pinecone/embeddings.html#PineconeSparseEmbeddings.embed_query)\#     

Embed query text with sparse embeddings.

Parameters:     

**text** \(_str_\)

Return type:     

_SparseValues_

_property _async\_client _: PineconeAsyncio_\#     

Lazily initialize the async client.

__On this page