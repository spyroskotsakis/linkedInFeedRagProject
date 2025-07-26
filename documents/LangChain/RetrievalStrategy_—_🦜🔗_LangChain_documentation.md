# RetrievalStrategy — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/elasticsearch/vectorstores/langchain_elasticsearch.vectorstores.RetrievalStrategy.html
**Word Count:** 298
**Links Count:** 101
**Scraped:** 2025-07-21 08:25:40
**Status:** completed

---

# RetrievalStrategy\#

_class _langchain\_elasticsearch.vectorstores.RetrievalStrategy[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/vectorstores.html#RetrievalStrategy)\#     

Methods

`before_index_creation`\(\*, client, text\_field, ...\) | Executes before the index is created.   ---|---   `es_mappings_settings`\(\*, text\_field, ...\) | Create the required index and do necessary preliminary work, like creating inference pipelines or checking if a required model was deployed.   `es_query`\(\*, query, query\_vector, text\_field, ...\) | Returns the Elasticsearch query body for the given parameters.   `needs_inference`\(\) | Some retrieval strategies index embedding vectors and allow search by embedding vector, for example the DenseVectorStrategy strategy.      before\_index\_creation\(

    _\*_ ,     _client : Elasticsearch_,     _text\_field : str_,     _vector\_field : str_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/elasticsearch/helpers/vectorstore/_sync/strategies.html#RetrievalStrategy.before_index_creation)\#     

Executes before the index is created. Used for setting up any required Elasticsearch resources like a pipeline. Defaults to a no-op.

Parameters:     

  * **client** \(_Elasticsearch_\) – The Elasticsearch client.

  * **text\_field** \(_str_\) – The field containing the text data in the index.

  * **vector\_field** \(_str_\) – The field containing the vector representations in the index.

Return type:     

None

_abstractmethod _es\_mappings\_settings\(

    _\*_ ,     _text\_field : str_,     _vector\_field : str_,     _num\_dimensions : int | None_, \) → Tuple\[Dict\[str, Any\], Dict\[str, Any\]\][\[source\]](https://python.langchain.com/api_reference/_modules/elasticsearch/helpers/vectorstore/_sync/strategies.html#RetrievalStrategy.es_mappings_settings)\#     

Create the required index and do necessary preliminary work, like creating inference pipelines or checking if a required model was deployed.

Parameters:     

  * **client** – Elasticsearch client connection.

  * **text\_field** \(_str_\) – The field containing the text data in the index.

  * **vector\_field** \(_str_\) – The field containing the vector representations in the index.

  * **num\_dimensions** \(_int_ _|__None_\) – If vectors are indexed, how many dimensions do they have.

Returns:     

Dictionary with field and field type pairs that describe the schema.

Return type:     

_Tuple_\[_Dict_\[str, _Any_\], _Dict_\[str, _Any_\]\]

_abstractmethod _es\_query\(

    _\*_ ,     _query : str | None_,     _query\_vector : List\[float\] | None_,     _text\_field : str_,     _vector\_field : str_,     _k : int_,     _num\_candidates : int_,     _filter : List\[Dict\[str, Any\]\] = \[\]_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/elasticsearch/helpers/vectorstore/_sync/strategies.html#RetrievalStrategy.es_query)\#     

Returns the Elasticsearch query body for the given parameters. The store will execute the query.

Parameters:     

  * **query** \(_str_ _|__None_\) – The text query. Can be None if query\_vector is given.

  * **k** \(_int_\) – The total number of results to retrieve.

  * **num\_candidates** \(_int_\) – The number of results to fetch initially in knn search.

  * **filter** \(_List_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]_\) – List of filter clauses to apply to the query.

  * **query\_vector** \(_List_ _\[__float_ _\]__|__None_\) – The query vector. Can be None if a query string is given.

  * **text\_field** \(_str_\)

  * **vector\_field** \(_str_\)

Returns:     

The Elasticsearch query body.

Return type:     

_Dict_\[str, _Any_\]

needs\_inference\(\) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/elasticsearch/helpers/vectorstore/_sync/strategies.html#RetrievalStrategy.needs_inference)\#     

Some retrieval strategies index embedding vectors and allow search by embedding vector, for example the DenseVectorStrategy strategy. Mapping a user input query string to an embedding vector is called inference. Inference can be applied in Elasticsearch \(using a model\_id\) or outside of Elasticsearch \(using an EmbeddingService defined on the VectorStore\). In the latter case, this method has to return True.

Return type:     

bool

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)