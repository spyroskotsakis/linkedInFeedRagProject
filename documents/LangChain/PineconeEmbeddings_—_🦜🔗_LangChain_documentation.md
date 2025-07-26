# PineconeEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/pinecone/embeddings/langchain_pinecone.embeddings.PineconeEmbeddings.html
**Word Count:** 129
**Links Count:** 102
**Scraped:** 2025-07-21 08:00:23
**Status:** completed

---

# PineconeEmbeddings\#

_class _langchain\_pinecone.embeddings.PineconeEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_pinecone/embeddings.html#PineconeEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

PineconeEmbeddings embedding model.

Example               from langchain_pinecone import PineconeEmbeddings     from langchain_pinecone import PineconeVectorStore     from langchain_core.documents import Document          # Initialize embeddings with a specific model     embeddings = PineconeEmbeddings(model="multilingual-e5-large")          # Embed a single query     query_embedding = embeddings.embed_query("What is machine learning?")          # Embed multiple documents     docs = ["Document 1 content", "Document 2 content"]     doc_embeddings = embeddings.embed_documents(docs)          # Use with PineconeVectorStore     from pinecone import Pinecone          pc = Pinecone(api_key="your-api-key")     index = pc.Index("your-index-name")          vectorstore = PineconeVectorStore(         index=index,         embedding=embeddings     )          # Add documents to vector store     vectorstore.add_documents([         Document(page_content="Hello, world!"),         Document(page_content="This is a test.")     ])          # Search for similar documents     results = vectorstore.similarity_search("hello", k=2)     

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_pinecone/embeddings.html#PineconeEmbeddings.aembed_documents)\#     

Asynchronous Embed search docs.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – List of text to embed.

Returns:     

List of embeddings.

Return type:     

_List_\[_List_\[float\]\]

_async _aembed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_pinecone/embeddings.html#PineconeEmbeddings.aembed_query)\#     

Asynchronously embed query text.

Parameters:     

**text** \(_str_\)

Return type:     

_List_\[float\]

embed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_pinecone/embeddings.html#PineconeEmbeddings.embed_documents)\#     

Embed search docs.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\)

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_pinecone/embeddings.html#PineconeEmbeddings.embed_query)\#     

Embed query text.

Parameters:     

**text** \(_str_\)

Return type:     

_List_\[float\]

_property _async\_client _: PineconeAsyncio_\#     

Lazily initialize the async client.

__On this page