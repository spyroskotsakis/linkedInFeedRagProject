# AsyncEmbeddingServiceAdapter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/elasticsearch/embeddings/langchain_elasticsearch.embeddings.AsyncEmbeddingServiceAdapter.html
**Word Count:** 71
**Links Count:** 95
**Scraped:** 2025-07-21 08:25:40
**Status:** completed

---

# AsyncEmbeddingServiceAdapter\#

_class _langchain\_elasticsearch.embeddings.AsyncEmbeddingServiceAdapter\(

    _langchain\_embeddings : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/embeddings.html#AsyncEmbeddingServiceAdapter)\#     

Methods

`__init__`\(langchain\_embeddings\) |    ---|---   `embed_documents`\(texts\) | Generate embeddings for a list of documents.   `embed_query`\(text\) | Generate an embedding for a single query text.      Parameters:     

**langchain\_embeddings** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

\_\_init\_\_\(

    _langchain\_embeddings : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_async/embeddings.html#AsyncEmbeddingServiceAdapter.__init__)\#     

Parameters:     

**langchain\_embeddings** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

_async _embed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_async/embeddings.html#AsyncEmbeddingServiceAdapter.embed_documents)\#     

Generate embeddings for a list of documents.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – A list of document text strings to generate embeddings for.

Returns:     

A list of embeddings, one for each document in the input     

list.

Return type:     

List\[List\[float\]\]

_async _embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_async/embeddings.html#AsyncEmbeddingServiceAdapter.embed_query)\#     

Generate an embedding for a single query text.

Parameters:     

**text** \(_str_\) – The query text to generate an embedding for.

Returns:     

The embedding for the input query text.

Return type:     

List\[float\]

__On this page