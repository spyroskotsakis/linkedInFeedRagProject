# AsyncElasticsearchEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/elasticsearch/embeddings/langchain_elasticsearch.embeddings.AsyncElasticsearchEmbeddings.html
**Word Count:** 422
**Links Count:** 107
**Scraped:** 2025-07-21 08:25:40
**Status:** completed

---

# AsyncElasticsearchEmbeddings\#

_class _langchain\_elasticsearch.embeddings.AsyncElasticsearchEmbeddings\(

    _client : MlClient_,     _model\_id : str_,     _\*_ ,     _input\_field : str = 'text\_field'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/embeddings.html#AsyncElasticsearchEmbeddings)\#     

Initialize the ElasticsearchEmbeddings instance.

Parameters:     

  * **client** \(_MlClient_\) – An Elasticsearch ML client object.

  * **model\_id** \(_str_\) – The model\_id of the model deployed in the Elasticsearch cluster.

  * **input\_field** \(_str_\) – The name of the key for the input text field in the document. Defaults to ‘text\_field’.

Methods

`__init__`\(client, model\_id, \*\[, input\_field\]\) | Initialize the ElasticsearchEmbeddings instance.   ---|---   `aembed_documents`\(texts\) | Generate embeddings for a list of documents.   `aembed_query`\(text\) | Generate an embedding for a single query text.   `embed_documents`\(texts\) | Embed search docs.   `embed_query`\(text\) | Embed query text.   `from_credentials`\(model\_id, \*\[, es\_cloud\_id, ...\]\) | Instantiate embeddings from Elasticsearch credentials.   `from_es_connection`\(model\_id, es\_connection\) | Instantiate embeddings from an existing Elasticsearch connection.      \_\_init\_\_\(

    _client : MlClient_,     _model\_id : str_,     _\*_ ,     _input\_field : str = 'text\_field'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_async/embeddings.html#AsyncElasticsearchEmbeddings.__init__)\#     

Initialize the ElasticsearchEmbeddings instance.

Parameters:     

  * **client** \(_MlClient_\) – An Elasticsearch ML client object.

  * **model\_id** \(_str_\) – The model\_id of the model deployed in the Elasticsearch cluster.

  * **input\_field** \(_str_\) – The name of the key for the input text field in the document. Defaults to ‘text\_field’.

_async _aembed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_async/embeddings.html#AsyncElasticsearchEmbeddings.aembed_documents)\#     

Generate embeddings for a list of documents.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – A list of document text strings to generate embeddings for.

Returns:     

A list of embeddings, one for each document in the input     

list.

Return type:     

List\[List\[float\]\]

_async _aembed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_async/embeddings.html#AsyncElasticsearchEmbeddings.aembed_query)\#     

Generate an embedding for a single query text.

Parameters:     

**text** \(_str_\) – The query text to generate an embedding for.

Returns:     

The embedding for the input query text.

Return type:     

List\[float\]

embed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/embeddings.html#AsyncElasticsearchEmbeddings.embed_documents)\#     

Embed search docs.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – List of text to embed.

Returns:     

List of embeddings.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/embeddings.html#AsyncElasticsearchEmbeddings.embed_query)\#     

Embed query text.

Parameters:     

**text** \(_str_\) – Text to embed.

Returns:     

Embedding.

Return type:     

_List_\[float\]

_classmethod _from\_credentials\(

    _model\_id : str_,     _\*_ ,     _es\_cloud\_id : str | None = None_,     _es\_api\_key : str | None = None_,     _input\_field : str = 'text\_field'_, \) → AsyncElasticsearchEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_async/embeddings.html#AsyncElasticsearchEmbeddings.from_credentials)\#     

Instantiate embeddings from Elasticsearch credentials.

Parameters:     

  * **model\_id** \(_str_\) – The model\_id of the model deployed in the Elasticsearch cluster.

  * **input\_field** \(_str_\) – The name of the key for the input text field in the document. Defaults to ‘text\_field’.

  * **es\_cloud\_id** \(_str_ _|__None_\) – \(str, optional\): The Elasticsearch cloud ID to connect to.

  * **es\_user** – \(str, optional\): Elasticsearch username.

  * **es\_password** – \(str, optional\): Elasticsearch password.

  * **es\_api\_key** \(_str_ _|__None_\)

Return type:     

_AsyncElasticsearchEmbeddings_

Example               from langchain_elasticserach.embeddings import ElasticsearchEmbeddings          # Define the model ID and input field name (if different from default)     model_id = "your_model_id"     # Optional, only if different from 'text_field'     input_field = "your_input_field"          # Credentials can be passed in two ways. Either set the env vars     # ES_CLOUD_ID, ES_USER, ES_PASSWORD and they will be automatically     # pulled in, or pass them in directly as kwargs.     embeddings = ElasticsearchEmbeddings.from_credentials(         model_id,         input_field=input_field,         # es_cloud_id="foo",         # es_user="bar",         # es_password="baz",     )          documents = [         "This is an example document.",         "Another example document to generate embeddings for.",     ]     embeddings_generator.embed_documents(documents)     

_classmethod _from\_es\_connection\(

    _model\_id : str_,     _es\_connection : AsyncElasticsearch_,     _input\_field : str = 'text\_field'_, \) → AsyncElasticsearchEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_async/embeddings.html#AsyncElasticsearchEmbeddings.from_es_connection)\#     

Instantiate embeddings from an existing Elasticsearch connection.

This method provides a way to create an instance of the ElasticsearchEmbeddings class using an existing Elasticsearch connection. The connection object is used to create an MlClient, which is then used to initialize the ElasticsearchEmbeddings instance.

Args: model\_id \(str\): The model\_id of the model deployed in the Elasticsearch cluster. es\_connection \(elasticsearch.Elasticsearch\): An existing Elasticsearch connection object. input\_field \(str, optional\): The name of the key for the input text field in the document. Defaults to ‘text\_field’.

Returns: ElasticsearchEmbeddings: An instance of the ElasticsearchEmbeddings class.

Example               from elasticsearch import Elasticsearch          from langchain_elasticsearch.embeddings import ElasticsearchEmbeddings          # Define the model ID and input field name (if different from default)     model_id = "your_model_id"     # Optional, only if different from 'text_field'     input_field = "your_input_field"          # Create Elasticsearch connection     es_connection = Elasticsearch(         hosts=["localhost:9200"], http_auth=("user", "password")     )          # Instantiate ElasticsearchEmbeddings using the existing connection     embeddings = ElasticsearchEmbeddings.from_es_connection(         model_id,         es_connection,         input_field=input_field,     )          documents = [         "This is an example document.",         "Another example document to generate embeddings for.",     ]     embeddings_generator.embed_documents(documents)     

Parameters:     

  * **model\_id** \(_str_\)

  * **es\_connection** \(_AsyncElasticsearch_\)

  * **input\_field** \(_str_\)

Return type:     

_AsyncElasticsearchEmbeddings_

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)