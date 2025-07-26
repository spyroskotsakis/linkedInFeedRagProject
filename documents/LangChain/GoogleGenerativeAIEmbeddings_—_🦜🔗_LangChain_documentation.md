# GoogleGenerativeAIEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/google_genai/embeddings/langchain_google_genai.embeddings.GoogleGenerativeAIEmbeddings.html
**Word Count:** 350
**Links Count:** 112
**Scraped:** 2025-07-21 07:59:00
**Status:** completed

---

# GoogleGenerativeAIEmbeddings\#

_class _langchain\_google\_genai.embeddings.GoogleGenerativeAIEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_genai/embeddings.html#GoogleGenerativeAIEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Google Generative AI Embeddings.

To use, you must have either:

>   1. The `GOOGLE_API_KEY` environment variable set with your API key, or >  > 

>  > 2\. Pass your API key using the google\_api\_key kwarg to the GoogleGenerativeAIEmbeddings constructor.

Example               from langchain_google_genai import GoogleGenerativeAIEmbeddings          embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")     embeddings.embed_query("What's our Q1 revenue?")     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _client\_options _: Dict | None_ _ = None_\#     

A dictionary of client options to pass to the Google API client, such as api\_endpoint.

_param _credentials _: Any_ _ = None_\#     

The default custom credentials \(google.auth.credentials.Credentials\) to use when making API calls. If not provided, credentials will be ascertained from the GOOGLE\_API\_KEY envvar

_param _google\_api\_key _: SecretStr | None_ _\[Optional\]_\#     

The Google API key to use. If not provided, the GOOGLE\_API\_KEY environment variable will be used.

_param _model _: str_ _\[Required\]_\#     

The name of the embedding model to use. Example: `'models/embedding-001'`

_param _request\_options _: Dict | None_ _ = None_\#     

A dictionary of request options to pass to the Google API client.Example: \{‘timeout’: 10\}

_param _task\_type _: str | None_ _ = None_\#     

The task type. Valid options include: `'task_type_unspecified'`, `'retrieval_query'`, `'retrieval_document'`, `'semantic_similarity'`, `'classification'`, and `'clustering'`

_param _transport _: str | None_ _ = None_\#     

A string, one of: \[`'rest'`, `'grpc'`, `'grpc_asyncio'`\].

_async _aembed\_documents\(

    _texts : List\[str\]_,     _\*_ ,     _batch\_size : int = 100_,     _task\_type : str | None = None_,     _titles : List\[str\] | None = None_,     _output\_dimensionality : int | None = None_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_genai/embeddings.html#GoogleGenerativeAIEmbeddings.aembed_documents)\#     

Embed a list of strings using the [batch endpoint](https://ai.google.dev/api/embeddings#method:-models.batchembedcontents).

Google Generative AI currently sets a max batch size of 100 strings.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\) – List\[str\] The list of strings to embed.

  * **batch\_size** \(_int_\) – \[int\] The batch size of embeddings to send to the model

  * **task\_type** \(_str_ _|__None_\) – [task\_type](https://ai.google.dev/api/embeddings#tasktype)

  * **titles** \(_List_ _\[__str_ _\]__|__None_\) – An optional list of titles for texts provided. Only applicable when TaskType is `'RETRIEVAL_DOCUMENT'`.

  * **output\_dimensionality** \(_int_ _|__None_\) – Optional [reduced dimension for the output embedding](https://ai.google.dev/api/embeddings#EmbedContentRequest).

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

_async _aembed\_query\(

    _text : str_,     _\*_ ,     _task\_type : str | None = None_,     _title : str | None = None_,     _output\_dimensionality : int | None = None_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_genai/embeddings.html#GoogleGenerativeAIEmbeddings.aembed_query)\#     

Embed a text, using the [non-batch endpoint](https://ai.google.dev/api/embeddings#method:-models.embedcontent).

Parameters:     

  * **text** \(_str_\) – The text to embed.

  * **task\_type** \(_str_ _|__None_\) – [task\_type](https://ai.google.dev/api/embeddings#tasktype)

  * **title** \(_str_ _|__None_\) – An optional title for the text. Only applicable when TaskType is `'RETRIEVAL_DOCUMENT'`.

  * **output\_dimensionality** \(_int_ _|__None_\) – Optional [reduced dimension for the output embedding](https://ai.google.dev/api/embeddings#EmbedContentRequest).

Returns:     

Embedding for the text.

Return type:     

_List_\[float\]

embed\_documents\(

    _texts : List\[str\]_,     _\*_ ,     _batch\_size : int = 100_,     _task\_type : str | None = None_,     _titles : List\[str\] | None = None_,     _output\_dimensionality : int | None = None_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_genai/embeddings.html#GoogleGenerativeAIEmbeddings.embed_documents)\#     

Embed a list of strings using the [batch endpoint](https://ai.google.dev/api/embeddings#method:-models.batchembedcontents).

Google Generative AI currently sets a max batch size of 100 strings.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\) – List\[str\] The list of strings to embed.

  * **batch\_size** \(_int_\) – \[int\] The batch size of embeddings to send to the model

  * **task\_type** \(_str_ _|__None_\) – [task\_type](https://ai.google.dev/api/embeddings#tasktype)

  * **titles** \(_List_ _\[__str_ _\]__|__None_\) – An optional list of titles for texts provided. Only applicable when TaskType is `'RETRIEVAL_DOCUMENT'`.

  * **output\_dimensionality** \(_int_ _|__None_\) – Optional [reduced dimension for the output embedding](https://ai.google.dev/api/embeddings#EmbedContentRequest).

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_,     _\*_ ,     _task\_type : str | None = None_,     _title : str | None = None_,     _output\_dimensionality : int | None = None_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_genai/embeddings.html#GoogleGenerativeAIEmbeddings.embed_query)\#     

Embed a text, using the [non-batch endpoint](https://ai.google.dev/api/embeddings#method:-models.embedcontent).

Parameters:     

  * **text** \(_str_\) – The text to embed.

  * **task\_type** \(_str_ _|__None_\) – [task\_type](https://ai.google.dev/api/embeddings#tasktype)

  * **title** \(_str_ _|__None_\) – An optional title for the text. Only applicable when TaskType is `'RETRIEVAL_DOCUMENT'`.

  * **output\_dimensionality** \(_int_ _|__None_\) – Optional [reduced dimension for the output embedding](https://ai.google.dev/api/embeddings#EmbedContentRequest).

Returns:     

Embedding for the text.

Return type:     

_List_\[float\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)