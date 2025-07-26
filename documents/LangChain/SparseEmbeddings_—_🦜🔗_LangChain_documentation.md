# SparseEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/qdrant/sparse_embeddings/langchain_qdrant.sparse_embeddings.SparseEmbeddings.html
**Word Count:** 40
**Links Count:** 97
**Scraped:** 2025-07-21 08:26:51
**Status:** completed

---

# SparseEmbeddings\#

_class _langchain\_qdrant.sparse\_embeddings.SparseEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_qdrant/sparse_embeddings.html#SparseEmbeddings)\#     

An interface for sparse embedding models to use with Qdrant.

Methods

`aembed_documents`\(texts\) | Asynchronous Embed search docs.   ---|---   `aembed_query`\(text\) | Asynchronous Embed query text.   `embed_documents`\(texts\) | Embed search docs.   `embed_query`\(text\) | Embed query text.      _async _aembed\_documents\(

    _texts : list\[str\]_, \) → list\[[SparseVector](https://python.langchain.com/api_reference/qdrant/sparse_embeddings/langchain_qdrant.sparse_embeddings.SparseVector.html#langchain_qdrant.sparse_embeddings.SparseVector "langchain_qdrant.sparse_embeddings.SparseVector")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_qdrant/sparse_embeddings.html#SparseEmbeddings.aembed_documents)\#     

Asynchronous Embed search docs.

Parameters:     

**texts** \(_list_ _\[__str_ _\]_\)

Return type:     

list\[[_SparseVector_](https://python.langchain.com/api_reference/qdrant/sparse_embeddings/langchain_qdrant.sparse_embeddings.SparseVector.html#langchain_qdrant.sparse_embeddings.SparseVector "langchain_qdrant.sparse_embeddings.SparseVector")\]

_async _aembed\_query\(

    _text : str_, \) → [SparseVector](https://python.langchain.com/api_reference/qdrant/sparse_embeddings/langchain_qdrant.sparse_embeddings.SparseVector.html#langchain_qdrant.sparse_embeddings.SparseVector "langchain_qdrant.sparse_embeddings.SparseVector")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_qdrant/sparse_embeddings.html#SparseEmbeddings.aembed_query)\#     

Asynchronous Embed query text.

Parameters:     

**text** \(_str_\)

Return type:     

[_SparseVector_](https://python.langchain.com/api_reference/qdrant/sparse_embeddings/langchain_qdrant.sparse_embeddings.SparseVector.html#langchain_qdrant.sparse_embeddings.SparseVector "langchain_qdrant.sparse_embeddings.SparseVector")

_abstractmethod _embed\_documents\(

    _texts : list\[str\]_, \) → list\[[SparseVector](https://python.langchain.com/api_reference/qdrant/sparse_embeddings/langchain_qdrant.sparse_embeddings.SparseVector.html#langchain_qdrant.sparse_embeddings.SparseVector "langchain_qdrant.sparse_embeddings.SparseVector")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_qdrant/sparse_embeddings.html#SparseEmbeddings.embed_documents)\#     

Embed search docs.

Parameters:     

**texts** \(_list_ _\[__str_ _\]_\)

Return type:     

list\[[_SparseVector_](https://python.langchain.com/api_reference/qdrant/sparse_embeddings/langchain_qdrant.sparse_embeddings.SparseVector.html#langchain_qdrant.sparse_embeddings.SparseVector "langchain_qdrant.sparse_embeddings.SparseVector")\]

_abstractmethod _embed\_query\(

    _text : str_, \) → [SparseVector](https://python.langchain.com/api_reference/qdrant/sparse_embeddings/langchain_qdrant.sparse_embeddings.SparseVector.html#langchain_qdrant.sparse_embeddings.SparseVector "langchain_qdrant.sparse_embeddings.SparseVector")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_qdrant/sparse_embeddings.html#SparseEmbeddings.embed_query)\#     

Embed query text.

Parameters:     

**text** \(_str_\)

Return type:     

[_SparseVector_](https://python.langchain.com/api_reference/qdrant/sparse_embeddings/langchain_qdrant.sparse_embeddings.SparseVector.html#langchain_qdrant.sparse_embeddings.SparseVector "langchain_qdrant.sparse_embeddings.SparseVector")

__On this page