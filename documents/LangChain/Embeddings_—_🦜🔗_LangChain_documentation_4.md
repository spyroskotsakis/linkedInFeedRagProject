# Embeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html
**Word Count:** 228
**Links Count:** 119
**Scraped:** 2025-07-21 07:56:25
**Status:** completed

---

# Embeddings\#

_class _langchain\_core.embeddings.embeddings.Embeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/embeddings/embeddings.html#Embeddings)\#     

Interface for embedding models.

This is an interface meant for implementing text embedding models.

Text embedding models are used to map text to a vector \(a point in n-dimensional space\).

Texts that are similar will usually be mapped to points that are close to each other in this space. The exact details of what’s considered “similar” and how “distance” is measured in this space are dependent on the specific embedding model.

This abstraction contains a method for embedding a list of documents and a method for embedding a query text. The embedding of a query text is expected to be a single vector, while the embedding of a list of documents is expected to be a list of vectors.

Usually the query embedding is identical to the document embedding, but the abstraction allows treating them independently.

In addition to the synchronous methods, this interface also provides asynchronous versions of the methods.

By default, the asynchronous methods are implemented using the synchronous methods; however, implementations may choose to override the asynchronous methods with an async native implementation for performance reasons.

Methods

`aembed_documents`\(texts\) | Asynchronous Embed search docs.   ---|---   `aembed_query`\(text\) | Asynchronous Embed query text.   `embed_documents`\(texts\) | Embed search docs.   `embed_query`\(text\) | Embed query text.      _async _aembed\_documents\(

    _texts : list\[str\]_, \) → list\[list\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/embeddings/embeddings.html#Embeddings.aembed_documents)\#     

Asynchronous Embed search docs.

Parameters:     

**texts** \(_list_ _\[__str_ _\]_\) – List of text to embed.

Returns:     

List of embeddings.

Return type:     

list\[list\[float\]\]

_async _aembed\_query\(_text : str_\) → list\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/embeddings/embeddings.html#Embeddings.aembed_query)\#     

Asynchronous Embed query text.

Parameters:     

**text** \(_str_\) – Text to embed.

Returns:     

Embedding.

Return type:     

list\[float\]

_abstractmethod _embed\_documents\(

    _texts : list\[str\]_, \) → list\[list\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/embeddings/embeddings.html#Embeddings.embed_documents)\#     

Embed search docs.

Parameters:     

**texts** \(_list_ _\[__str_ _\]_\) – List of text to embed.

Returns:     

List of embeddings.

Return type:     

list\[list\[float\]\]

_abstractmethod _embed\_query\(_text : str_\) → list\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/embeddings/embeddings.html#Embeddings.embed_query)\#     

Embed query text.

Parameters:     

**text** \(_str_\) – Text to embed.

Returns:     

Embedding.

Return type:     

list\[float\]

Examples using Embeddings

  * [ElasticsearchRetriever](https://python.langchain.com/docs/integrations/retrievers/elasticsearch_retriever/)

  * [Infinispan](https://python.langchain.com/docs/integrations/vectorstores/infinispanvs/)

__On this page