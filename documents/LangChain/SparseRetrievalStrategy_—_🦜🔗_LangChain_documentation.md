# SparseRetrievalStrategy — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.elasticsearch.SparseRetrievalStrategy.html
**Word Count:** 282
**Links Count:** 340
**Scraped:** 2025-07-21 08:20:13
**Status:** completed

---

# SparseRetrievalStrategy\#

_class _langchain\_community.vectorstores.elasticsearch.SparseRetrievalStrategy\(_model\_id : str | None = None_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/elasticsearch.html#SparseRetrievalStrategy)\#     

Deprecated since version 0.0.27: Use `Use class in langchain-elasticsearch package` instead.

Sparse retrieval strategy using the text\_expansion processor.

Methods

`__init__`\(\[model\_id\]\) |    ---|---   `before_index_setup`\(client, text\_field, ...\) | Executes before the index is created.   `index`\(dims\_length, vector\_query\_field, ...\) | Executes when the index is created.   `query`\(query\_vector, query, k, fetch\_k, ...\) | Executes when a search is performed on the store.   `require_inference`\(\) | Returns whether or not the strategy requires inference to be performed on the text before it is added to the index.      Parameters:     

**model\_id** \(_str_ _|__None_\)

\_\_init\_\_\(

    _model\_id : str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/elasticsearch.html#SparseRetrievalStrategy.__init__)\#     

Parameters:     

**model\_id** \(_str_ _|__None_\)

before\_index\_setup\(

    _client : Elasticsearch_,     _text\_field : str_,     _vector\_query\_field : str_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/elasticsearch.html#SparseRetrievalStrategy.before_index_setup)\#     

Executes before the index is created. Used for setting up any required Elasticsearch resources like a pipeline.

Parameters:     

  * **client** \(_Elasticsearch_\) – The Elasticsearch client.

  * **text\_field** \(_str_\) – The field containing the text data in the index.

  * **vector\_query\_field** \(_str_\) – The field containing the vector representations in the index.

Return type:     

None

index\(

    _dims\_length : int | None_,     _vector\_query\_field : str_,     _similarity : [DistanceStrategy](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.utils.DistanceStrategy.html#langchain_community.vectorstores.utils.DistanceStrategy "langchain_community.vectorstores.utils.DistanceStrategy") | None_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/elasticsearch.html#SparseRetrievalStrategy.index)\#     

Executes when the index is created.

Parameters:     

  * **dims\_length** \(_int_ _|__None_\) – Numeric length of the embedding vectors, or None if not using vector-based query.

  * **vector\_query\_field** \(_str_\) – The field containing the vector representations in the index.

  * **similarity** \([_DistanceStrategy_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.utils.DistanceStrategy.html#langchain_community.vectorstores.utils.DistanceStrategy "langchain_community.vectorstores.utils.DistanceStrategy") _|__None_\) – The similarity strategy to use, or None if not using one.

Returns:     

The Elasticsearch settings and mappings for the strategy.

Return type:     

Dict

query\(

    _query\_vector : List\[float\] | None_,     _query : str | None_,     _k : int_,     _fetch\_k : int_,     _vector\_query\_field : str_,     _text\_field : str_,     _filter : List\[dict\]_,     _similarity : [DistanceStrategy](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.utils.DistanceStrategy.html#langchain_community.vectorstores.utils.DistanceStrategy "langchain_community.vectorstores.utils.DistanceStrategy") | None_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/elasticsearch.html#SparseRetrievalStrategy.query)\#     

Executes when a search is performed on the store.

Parameters:     

  * **query\_vector** \(_List_ _\[__float_ _\]__|__None_\) – The query vector, or None if not using vector-based query.

  * **query** \(_str_ _|__None_\) – The text query, or None if not using text-based query.

  * **k** \(_int_\) – The total number of results to retrieve.

  * **fetch\_k** \(_int_\) – The number of results to fetch initially.

  * **vector\_query\_field** \(_str_\) – The field containing the vector representations in the index.

  * **text\_field** \(_str_\) – The field containing the text data in the index.

  * **filter** \(_List_ _\[__dict_ _\]_\) – List of filter clauses to apply to the query.

  * **similarity** \([_DistanceStrategy_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.utils.DistanceStrategy.html#langchain_community.vectorstores.utils.DistanceStrategy "langchain_community.vectorstores.utils.DistanceStrategy") _|__None_\) – The similarity strategy to use, or None if not using one.

Returns:     

The Elasticsearch query body.

Return type:     

Dict

require\_inference\(\) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/elasticsearch.html#SparseRetrievalStrategy.require_inference)\#     

Returns whether or not the strategy requires inference to be performed on the text before it is added to the index.

Returns:     

Whether or not the strategy requires inference to be performed on the text before it is added to the index.

Return type:     

bool

__On this page