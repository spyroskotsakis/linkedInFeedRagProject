# AnyscaleEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.anyscale.AnyscaleEmbeddings.html
**Word Count:** 417
**Links Count:** 274
**Scraped:** 2025-07-21 08:22:37
**Status:** completed

---

# AnyscaleEmbeddings\#

_class _langchain\_community.embeddings.anyscale.AnyscaleEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/anyscale.html#AnyscaleEmbeddings)\#     

Bases: [`OpenAIEmbeddings`](https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.openai.OpenAIEmbeddings.html#langchain_community.embeddings.openai.OpenAIEmbeddings "langchain_community.embeddings.openai.OpenAIEmbeddings")

Anyscale Embeddings API.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _allowed\_special _: Literal\['all'\] | Set\[str\]__ = \{\}_\#     

_param _anyscale\_api\_base _: str_ _ = 'https://api.endpoints.anyscale.com/v1'_\#     

Base URL path for API requests.

_param _anyscale\_api\_key _: SecretStr | None_ _ = None_\#     

AnyScale Endpoints API keys.

_param _chunk\_size _: int_ _ = 1000_\#     

Maximum number of texts to embed in each batch

_param _default\_headers _: Mapping\[str, str\] | None_ _ = None_\#     

_param _default\_query _: Mapping\[str, object\] | None_ _ = None_\#     

_param _deployment _: str | None_ _ = 'text-embedding-ada-002'_\#     

_param _disallowed\_special _: Literal\['all'\] | Set\[str\] | Sequence\[str\]__ = 'all'_\#     

_param _embedding\_ctx\_length _: int_ _ = 500_\#     

The maximum number of tokens to embed at once.

_param _headers _: Any_ _ = None_\#     

_param _http\_client _: Any | None_ _ = None_\#     

Optional httpx.Client.

_param _max\_retries _: int_ _ = 2_\#     

Maximum number of retries to make when generating.

_param _model _: str_ _ = 'thenlper/gte-large'_\#     

Model name to use.

_param _model\_kwargs _: Dict\[str, Any\]__\[Optional\]_\#     

Holds any model parameters valid for create call not explicitly specified.

_param _openai\_api\_base _: str | None_ _ = None_ _\(alias 'base\_url'\)_\#     

Base URL path for API requests, leave blank if not using a proxy or service emulator.

_param _openai\_api\_key _: str | None_ _ = None_ _\(alias 'api\_key'\)_\#     

Automatically inferred from env var OPENAI\_API\_KEY if not provided.

_param _openai\_api\_type _: str | None_ _ = None_\#     

_param _openai\_api\_version _: str | None_ _ = None_ _\(alias 'api\_version'\)_\#     

Automatically inferred from env var OPENAI\_API\_VERSION if not provided.

_param _openai\_organization _: str | None_ _ = None_ _\(alias 'organization'\)_\#     

Automatically inferred from env var OPENAI\_ORG\_ID if not provided.

_param _openai\_proxy _: str | None_ _ = None_\#     

_param _request\_timeout _: float | Tuple\[float, float\] | Any | None_ _ = None_ _\(alias 'timeout'\)_\#     

Timeout for requests to OpenAI completion API. Can be float, httpx.Timeout or None.

_param _retry\_max\_seconds _: int_ _ = 20_\#     

Max number of seconds to wait between retries

_param _retry\_min\_seconds _: int_ _ = 4_\#     

Min number of seconds to wait between retries

_param _show\_progress\_bar _: bool_ _ = False_\#     

Whether to show a progress bar when embedding.

_param _skip\_empty _: bool_ _ = False_\#     

Whether to skip empty strings when embedding or raise an error. Defaults to not skipping.

_param _tiktoken\_enabled _: bool_ _ = False_\#     

Set this to False for non-OpenAI implementations of the embeddings API

_param _tiktoken\_model\_name _: str | None_ _ = None_\#     

The model name to pass to tiktoken when using this class. Tiktoken is used to count the number of tokens in documents to constrain them to be under a certain limit. By default, when set to None, this will be the same as the embedding model name. However, there are some cases where you may want to use this Embedding class with a model name not supported by tiktoken. This can include when using Azure embeddings or when using one of the many model providers that expose an OpenAI-like API but with different models. In those cases, in order to avoid erroring when tiktoken is called, you can specify a model name to use here.

_classmethod _validate\_environment\(

    _values : dict_, \) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/anyscale.html#AnyscaleEmbeddings.validate_environment)\#     

Validate that api key and python package exists in environment.

Parameters:     

**values** \(_dict_\)

Return type:     

dict

_async _aembed\_documents\(

    _texts : List\[str\]_,     _chunk\_size : int | None = 0_, \) → List\[List\[float\]\]\#     

Call out to OpenAI’s embedding endpoint async for embedding search docs.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

  * **chunk\_size** \(_int_ _|__None_\) – The chunk size of embeddings. If None, will use the chunk size specified by the class.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

_async _aembed\_query\(

    _text : str_, \) → List\[float\]\#     

Call out to OpenAI’s embedding endpoint async for embedding query text.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embedding for the text.

Return type:     

_List_\[float\]

embed\_documents\(

    _texts : List\[str\]_,     _chunk\_size : int | None = 0_, \) → List\[List\[float\]\]\#     

Call out to OpenAI’s embedding endpoint for embedding search docs.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

  * **chunk\_size** \(_int_ _|__None_\) – The chunk size of embeddings. If None, will use the chunk size specified by the class.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\]\#     

Call out to OpenAI’s embedding endpoint for embedding query text.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embedding for the text.

Return type:     

_List_\[float\]

Examples using AnyscaleEmbeddings

  * [Anyscale](https://python.langchain.com/docs/integrations/providers/anyscale/)

__On this page