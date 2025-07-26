# BM25SparseEmbedding — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/milvus/utils/langchain_milvus.utils.sparse.BM25SparseEmbedding.html
**Word Count:** 138
**Links Count:** 95
**Scraped:** 2025-07-21 08:26:28
**Status:** completed

---

# BM25SparseEmbedding\#

_class _langchain\_milvus.utils.sparse.BM25SparseEmbedding\(

    _corpus : List\[str\]_,     _language : str = 'en'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_milvus/utils/sparse.html#BM25SparseEmbedding)\#     

Sparse embedding model based on BM25.

\*\*Note: We recommend using the Milvus built-in BM25 function to implement sparse embedding in your application. This class is more of a reference because it requires the user to manage the corpus,

> which is not practical. The Milvus built-in function solves this problem and makes the BM25 sparse process easier and less frustrating for users.

For more information, please refer to: <https://milvus.io/docs/full-text-search.md#Full-Text-Search> and [milvus-io/bootcamp](https://github.com/milvus-io/bootcamp/blob/master/bootcamp/tutorials/integration/langchain/full_text_search_with_langchain.ipynb) \*\*

This class uses the BM25 model in Milvus model to implement sparse vector embedding. This model requires pymilvus\[model\] to be installed. pip install pymilvus\[model\] For more information please refer to: <https://milvus.io/docs/embed-with-bm25.md>

Methods

`__init__`\(corpus\[, language\]\) |    ---|---   `aembed_documents`\(texts\) | Asynchronous Embed search docs.   `aembed_query`\(query\) | Asynchronous Embed query text.   `embed_documents`\(texts\) | Embed search docs.   `embed_query`\(text\) | Embed query text.      Parameters:     

  * **corpus** \(_List_ _\[__str_ _\]_\)

  * **language** \(_str_\)

\_\_init\_\_\(

    _corpus : List\[str\]_,     _language : str = 'en'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_milvus/utils/sparse.html#BM25SparseEmbedding.__init__)\#     

Parameters:     

  * **corpus** \(_List_ _\[__str_ _\]_\)

  * **language** \(_str_\)

_async _aembed\_documents\(

    _texts : list\[str\]_, \) → List\[Dict\[int, float\]\]\#     

Asynchronous Embed search docs.

Parameters:     

**texts** \(_list_ _\[__str_ _\]_\) – List of text to embed.

Returns:     

List of embeddings.

Return type:     

_List_\[_Dict_\[int, float\]\]

_async _aembed\_query\(

    _query : str_, \) → Dict\[int, float\]\#     

Asynchronous Embed query text.

Parameters:     

**query** \(_str_\) – Text to embed.

Returns:     

Embedding.

Return type:     

_Dict_\[int, float\]

embed\_documents\(

    _texts : List\[str\]_, \) → List\[Dict\[int, float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_milvus/utils/sparse.html#BM25SparseEmbedding.embed_documents)\#     

Embed search docs.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\)

Return type:     

_List_\[_Dict_\[int, float\]\]

embed\_query\(

    _text : str_, \) → Dict\[int, float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_milvus/utils/sparse.html#BM25SparseEmbedding.embed_query)\#     

Embed query text.

Parameters:     

**text** \(_str_\)

Return type:     

_Dict_\[int, float\]

__On this page