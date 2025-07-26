# EmbeddingService — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/elasticsearch/embeddings/langchain_elasticsearch.embeddings.EmbeddingService.html
**Word Count:** 69
**Links Count:** 87
**Scraped:** 2025-07-21 08:25:40
**Status:** completed

---

# EmbeddingService\#

_class _langchain\_elasticsearch.embeddings.EmbeddingService[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/embeddings.html#EmbeddingService)\#     

Methods

`embed_documents`\(texts\) | Generate embeddings for a list of documents.   ---|---   `embed_query`\(query\) | Generate an embedding for a single query text.      _abstractmethod _embed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/elasticsearch/helpers/vectorstore/_sync/embedding_service.html#EmbeddingService.embed_documents)\#     

Generate embeddings for a list of documents.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – A list of document strings to generate embeddings for.

Returns:     

A list of embeddings, one for each document in the input.

Return type:     

_List_\[_List_\[float\]\]

_abstractmethod _embed\_query\(

    _query : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/elasticsearch/helpers/vectorstore/_sync/embedding_service.html#EmbeddingService.embed_query)\#     

Generate an embedding for a single query text.

Parameters:     

  * **text** – The query text to generate an embedding for.

  * **query** \(_str_\)

Returns:     

The embedding for the input query text.

Return type:     

_List_\[float\]

__On this page