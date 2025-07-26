# ExactRetrievalStrategy — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.elasticsearch.ExactRetrievalStrategy.html
**Word Count:** 243
**Links Count:** 337
**Scraped:** 2025-07-21 08:10:45
**Status:** completed

---

# ExactRetrievalStrategy\#

_class _langchain\_community.vectorstores.elasticsearch.ExactRetrievalStrategy\(

    _\* args: Any_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/elasticsearch.html#ExactRetrievalStrategy)\#     

Deprecated since version 0.0.27: Use `Use class in langchain-elasticsearch package` instead.

Exact retrieval strategy using the script\_score query.

Methods

`__init__`\(\*args, \*\*kwargs\) |    ---|---   `before_index_setup`\(client, text\_field, ...\) | Executes before the index is created.   `index`\(dims\_length, vector\_query\_field, ...\) | Create the mapping for the Elasticsearch index.   `query`\(query\_vector, query, k, fetch\_k, ...\) | Executes when a search is performed on the store.   `require_inference`\(\) | Returns whether or not the strategy requires inference to be performed on the text before it is added to the index.      \_\_init\_\_\(

    _\* args: Any_,     _\*\* kwargs: Any_, \) → Any\#     

Parameters:     

  * **self** \(_Any_\)

  * **args** \(_Any_\)

  * **kwargs** \(_Any_\)

Return type:     

_Any_

before\_index\_setup\(

    _client : Elasticsearch_,     _text\_field : str_,     _vector\_query\_field : str_, \) → None\#     

Executes before the index is created. Used for setting up any required Elasticsearch resources like a pipeline.

Parameters:     

  * **client** \(_Elasticsearch_\) – The Elasticsearch client.

  * **text\_field** \(_str_\) – The field containing the text data in the index.

  * **vector\_query\_field** \(_str_\) – The field containing the vector representations in the index.

Return type:     

None

index\(

    _dims\_length : int | None_,     _vector\_query\_field : str_,     _similarity : [DistanceStrategy](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.utils.DistanceStrategy.html#langchain_community.vectorstores.utils.DistanceStrategy "langchain_community.vectorstores.utils.DistanceStrategy") | None_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/elasticsearch.html#ExactRetrievalStrategy.index)\#     

Create the mapping for the Elasticsearch index.

Parameters:     

  * **dims\_length** \(_int_ _|__None_\)

  * **vector\_query\_field** \(_str_\)

  * **similarity** \([_DistanceStrategy_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.utils.DistanceStrategy.html#langchain_community.vectorstores.utils.DistanceStrategy "langchain_community.vectorstores.utils.DistanceStrategy") _|__None_\)

Return type:     

_Dict_

query\(

    _query\_vector : List\[float\] | None_,     _query : str | None_,     _k : int_,     _fetch\_k : int_,     _vector\_query\_field : str_,     _text\_field : str_,     _filter : List\[dict\] | None_,     _similarity : [DistanceStrategy](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.utils.DistanceStrategy.html#langchain_community.vectorstores.utils.DistanceStrategy "langchain_community.vectorstores.utils.DistanceStrategy") | None_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/elasticsearch.html#ExactRetrievalStrategy.query)\#     

Executes when a search is performed on the store.

Parameters:     

  * **query\_vector** \(_List_ _\[__float_ _\]__|__None_\) – The query vector, or None if not using vector-based query.

  * **query** \(_str_ _|__None_\) – The text query, or None if not using text-based query.

  * **k** \(_int_\) – The total number of results to retrieve.

  * **fetch\_k** \(_int_\) – The number of results to fetch initially.

  * **vector\_query\_field** \(_str_\) – The field containing the vector representations in the index.

  * **text\_field** \(_str_\) – The field containing the text data in the index.

  * **filter** \(_List_ _\[__dict_ _\]__|__None_\) – List of filter clauses to apply to the query.

  * **similarity** \([_DistanceStrategy_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.utils.DistanceStrategy.html#langchain_community.vectorstores.utils.DistanceStrategy "langchain_community.vectorstores.utils.DistanceStrategy") _|__None_\) – The similarity strategy to use, or None if not using one.

Returns:     

The Elasticsearch query body.

Return type:     

Dict

require\_inference\(\) → bool\#     

Returns whether or not the strategy requires inference to be performed on the text before it is added to the index.

Returns:     

Whether or not the strategy requires inference to be performed on the text before it is added to the index.

Return type:     

bool

__On this page