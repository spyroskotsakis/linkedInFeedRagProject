# BaseSparseEmbedding — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/milvus/utils/langchain_milvus.utils.sparse.BaseSparseEmbedding.html
**Word Count:** 89
**Links Count:** 89
**Scraped:** 2025-07-21 08:26:28
**Status:** completed

---

# BaseSparseEmbedding\#

_class _langchain\_milvus.utils.sparse.BaseSparseEmbedding[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_milvus/utils/sparse.html#BaseSparseEmbedding)\#     

Interface for Sparse embedding models.

You can inherit from it and implement your custom sparse embedding model.

By default, the asynchronous methods are implemented using the synchronous methods; however, implementations may choose to override the asynchronous methods with an async native implementation for performance reasons.

Methods

`aembed_documents`\(texts\) | Asynchronous Embed search docs.   ---|---   `aembed_query`\(query\) | Asynchronous Embed query text.   `embed_documents`\(texts\) | Embed search docs.   `embed_query`\(query\) | Embed query text.      _async _aembed\_documents\(

    _texts : list\[str\]_, \) → List\[Dict\[int, float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_milvus/utils/sparse.html#BaseSparseEmbedding.aembed_documents)\#     

Asynchronous Embed search docs.

Parameters:     

**texts** \(_list_ _\[__str_ _\]_\) – List of text to embed.

Returns:     

List of embeddings.

Return type:     

_List_\[_Dict_\[int, float\]\]

_async _aembed\_query\(

    _query : str_, \) → Dict\[int, float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_milvus/utils/sparse.html#BaseSparseEmbedding.aembed_query)\#     

Asynchronous Embed query text.

Parameters:     

**query** \(_str_\) – Text to embed.

Returns:     

Embedding.

Return type:     

_Dict_\[int, float\]

_abstractmethod _embed\_documents\(

    _texts : List\[str\]_, \) → List\[Dict\[int, float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_milvus/utils/sparse.html#BaseSparseEmbedding.embed_documents)\#     

Embed search docs.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\)

Return type:     

_List_\[_Dict_\[int, float\]\]

_abstractmethod _embed\_query\(

    _query : str_, \) → Dict\[int, float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_milvus/utils/sparse.html#BaseSparseEmbedding.embed_query)\#     

Embed query text.

Parameters:     

**query** \(_str_\)

Return type:     

_Dict_\[int, float\]

__On this page