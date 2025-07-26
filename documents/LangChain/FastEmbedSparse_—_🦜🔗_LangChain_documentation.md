# FastEmbedSparse — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/qdrant/fastembed_sparse/langchain_qdrant.fastembed_sparse.FastEmbedSparse.html
**Word Count:** 270
**Links Count:** 104
**Scraped:** 2025-07-21 08:26:51
**Status:** completed

---

# FastEmbedSparse\#

_class _langchain\_qdrant.fastembed\_sparse.FastEmbedSparse\(

    _model\_name : str = 'Qdrant/bm25'_,     _batch\_size : int = 256_,     _cache\_dir : str | None = None_,     _threads : int | None = None_,     _providers : Sequence\[Any\] | None = None_,     _parallel : int | None = None_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_qdrant/fastembed_sparse.html#FastEmbedSparse)\#     

An interface for sparse embedding models to use with Qdrant.

Sparse encoder implementation using FastEmbed - <https://qdrant.github.io/fastembed/> For a list of available models, see <https://qdrant.github.io/fastembed/examples/Supported_Models/>

Parameters:     

  * **model\_name** \(_str_\) – The name of the model to use. Defaults to “Qdrant/bm25”.

  * **batch\_size** \(_int_\) – Batch size for encoding. Defaults to 256.

  * **cache\_dir** \(_str_ _,__optional_\) – The path to the model cache directory. Can also be set using the FASTEMBED\_CACHE\_PATH env variable.

  * **threads** \(_int_ _,__optional_\) – The number of threads onnxruntime session can use.

  * **providers** \(_Sequence_ _\[__Any_ _\]__,__optional_\) – List of ONNX execution providers. parallel \(int, optional\): If >1, data-parallel encoding will be used, r Recommended for encoding of large datasets. If 0, use all available cores. If None, don’t use data-parallel processing, use default onnxruntime threading instead. Defaults to None.

  * **kwargs** \(_Any_\) – Additional options to pass to fastembed.SparseTextEmbedding

  * **parallel** \(_int_ _|__None_\)

Raises:     

**ValueError** – If the model\_name is not supported in SparseTextEmbedding.

Methods

`__init__`\(\[model\_name, batch\_size, ...\]\) | Sparse encoder implementation using FastEmbed - <https://qdrant.github.io/fastembed/> For a list of available models, see <https://qdrant.github.io/fastembed/examples/Supported_Models/>   ---|---   `aembed_documents`\(texts\) | Asynchronous Embed search docs.   `aembed_query`\(text\) | Asynchronous Embed query text.   `embed_documents`\(texts\) | Embed search docs.   `embed_query`\(text\) | Embed query text.      \_\_init\_\_\(

    _model\_name : str = 'Qdrant/bm25'_,     _batch\_size : int = 256_,     _cache\_dir : str | None = None_,     _threads : int | None = None_,     _providers : Sequence\[Any\] | None = None_,     _parallel : int | None = None_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_qdrant/fastembed_sparse.html#FastEmbedSparse.__init__)\#     

Sparse encoder implementation using FastEmbed - <https://qdrant.github.io/fastembed/> For a list of available models, see <https://qdrant.github.io/fastembed/examples/Supported_Models/>

Parameters:     

  * **model\_name** \(_str_\) – The name of the model to use. Defaults to “Qdrant/bm25”.

  * **batch\_size** \(_int_\) – Batch size for encoding. Defaults to 256.

  * **cache\_dir** \(_str_ _,__optional_\) – The path to the model cache directory. Can also be set using the FASTEMBED\_CACHE\_PATH env variable.

  * **threads** \(_int_ _,__optional_\) – The number of threads onnxruntime session can use.

  * **providers** \(_Sequence_ _\[__Any_ _\]__,__optional_\) – List of ONNX execution providers. parallel \(int, optional\): If >1, data-parallel encoding will be used, r Recommended for encoding of large datasets. If 0, use all available cores. If None, don’t use data-parallel processing, use default onnxruntime threading instead. Defaults to None.

  * **kwargs** \(_Any_\) – Additional options to pass to fastembed.SparseTextEmbedding

  * **parallel** \(_int_ _|__None_\)

Raises:     

**ValueError** – If the model\_name is not supported in SparseTextEmbedding.

Return type:     

None

_async _aembed\_documents\(

    _texts : list\[str\]_, \) → list\[[SparseVector](https://python.langchain.com/api_reference/qdrant/sparse_embeddings/langchain_qdrant.sparse_embeddings.SparseVector.html#langchain_qdrant.sparse_embeddings.SparseVector "langchain_qdrant.sparse_embeddings.SparseVector")\]\#     

Asynchronous Embed search docs.

Parameters:     

**texts** \(_list_ _\[__str_ _\]_\)

Return type:     

list\[[_SparseVector_](https://python.langchain.com/api_reference/qdrant/sparse_embeddings/langchain_qdrant.sparse_embeddings.SparseVector.html#langchain_qdrant.sparse_embeddings.SparseVector "langchain_qdrant.sparse_embeddings.SparseVector")\]

_async _aembed\_query\(

    _text : str_, \) → [SparseVector](https://python.langchain.com/api_reference/qdrant/sparse_embeddings/langchain_qdrant.sparse_embeddings.SparseVector.html#langchain_qdrant.sparse_embeddings.SparseVector "langchain_qdrant.sparse_embeddings.SparseVector")\#     

Asynchronous Embed query text.

Parameters:     

**text** \(_str_\)

Return type:     

[_SparseVector_](https://python.langchain.com/api_reference/qdrant/sparse_embeddings/langchain_qdrant.sparse_embeddings.SparseVector.html#langchain_qdrant.sparse_embeddings.SparseVector "langchain_qdrant.sparse_embeddings.SparseVector")

embed\_documents\(

    _texts : list\[str\]_, \) → list\[[SparseVector](https://python.langchain.com/api_reference/qdrant/sparse_embeddings/langchain_qdrant.sparse_embeddings.SparseVector.html#langchain_qdrant.sparse_embeddings.SparseVector "langchain_qdrant.sparse_embeddings.SparseVector")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_qdrant/fastembed_sparse.html#FastEmbedSparse.embed_documents)\#     

Embed search docs.

Parameters:     

**texts** \(_list_ _\[__str_ _\]_\)

Return type:     

list\[[_SparseVector_](https://python.langchain.com/api_reference/qdrant/sparse_embeddings/langchain_qdrant.sparse_embeddings.SparseVector.html#langchain_qdrant.sparse_embeddings.SparseVector "langchain_qdrant.sparse_embeddings.SparseVector")\]

embed\_query\(

    _text : str_, \) → [SparseVector](https://python.langchain.com/api_reference/qdrant/sparse_embeddings/langchain_qdrant.sparse_embeddings.SparseVector.html#langchain_qdrant.sparse_embeddings.SparseVector "langchain_qdrant.sparse_embeddings.SparseVector")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_qdrant/fastembed_sparse.html#FastEmbedSparse.embed_query)\#     

Embed query text.

Parameters:     

**text** \(_str_\)

Return type:     

[_SparseVector_](https://python.langchain.com/api_reference/qdrant/sparse_embeddings/langchain_qdrant.sparse_embeddings.SparseVector.html#langchain_qdrant.sparse_embeddings.SparseVector "langchain_qdrant.sparse_embeddings.SparseVector")

__On this page