# CohereEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.cohere.CohereEmbeddings.html
**Word Count:** 199
**Links Count:** 249
**Scraped:** 2025-07-21 08:05:36
**Status:** completed

---

# CohereEmbeddings\#

_class _langchain\_community.embeddings.cohere.CohereEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/cohere.html#CohereEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Deprecated since version 0.0.30: Use `:class:`~langchain_cohere.CohereEmbeddings`` instead. It will not be removed until langchain-community==1.0.

Cohere embedding models.

To use, you should have the `cohere` python package installed, and the environment variable `COHERE_API_KEY` set with your API key or pass it as a named parameter to the constructor.

Example               from langchain_community.embeddings import CohereEmbeddings     cohere = CohereEmbeddings(         model="embed-english-light-v3.0",         cohere_api_key="my-api-key"     )     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _async\_client _: Any_ _ = None_\#     

Cohere async client.

_param _client _: Any_ _ = None_\#     

Cohere client.

_param _cohere\_api\_key _: str | None_ _ = None_\#     

_param _max\_retries _: int_ _ = 3_\#     

Maximum number of retries to make when generating.

_param _model _: str_ _ = 'embed-english-v2.0'_\#     

Model name to use.

_param _request\_timeout _: float | None_ _ = None_\#     

Timeout in seconds for the Cohere API request.

_param _truncate _: str | None_ _ = None_\#     

Truncate embeddings that are too long from start or end \(“NONE”|”START”|”END”\)

_param _user\_agent _: str_ _ = 'langchain'_\#     

Identifier for the application making the request.

_async _aembed\(

    _texts : List\[str\]_,     _\*_ ,     _input\_type : str | None = None_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/cohere.html#CohereEmbeddings.aembed)\#     

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\)

  * **input\_type** \(_str_ _|__None_\)

Return type:     

_List_\[_List_\[float\]\]

_async _aembed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/cohere.html#CohereEmbeddings.aembed_documents)\#     

Async call out to Cohere’s embedding endpoint.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

_async _aembed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/cohere.html#CohereEmbeddings.aembed_query)\#     

Async call out to Cohere’s embedding endpoint.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

aembed\_with\_retry\(

    _\*\* kwargs: Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/cohere.html#CohereEmbeddings.aembed_with_retry)\#     

Use tenacity to retry the embed call.

Parameters:     

**kwargs** \(_Any_\)

Return type:     

_Any_

embed\(

    _texts : List\[str\]_,     _\*_ ,     _input\_type : str | None = None_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/cohere.html#CohereEmbeddings.embed)\#     

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\)

  * **input\_type** \(_str_ _|__None_\)

Return type:     

_List_\[_List_\[float\]\]

embed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/cohere.html#CohereEmbeddings.embed_documents)\#     

Embed a list of document texts.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/cohere.html#CohereEmbeddings.embed_query)\#     

Call out to Cohere’s embedding endpoint.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

embed\_with\_retry\(

    _\*\* kwargs: Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/cohere.html#CohereEmbeddings.embed_with_retry)\#     

Use tenacity to retry the embed call.

Parameters:     

**kwargs** \(_Any_\)

Return type:     

_Any_

Examples using CohereEmbeddings

  * [Cohere reranker](https://python.langchain.com/docs/integrations/retrievers/cohere-reranker/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)