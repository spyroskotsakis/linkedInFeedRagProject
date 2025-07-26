# AzureOpenAIEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.azure_openai.AzureOpenAIEmbeddings.html
**Word Count:** 497
**Links Count:** 282
**Scraped:** 2025-07-21 08:06:11
**Status:** completed

---

# AzureOpenAIEmbeddings\#

_class _langchain\_community.embeddings.azure\_openai.AzureOpenAIEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/azure_openai.html#AzureOpenAIEmbeddings)\#     

Bases: [`OpenAIEmbeddings`](https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.openai.OpenAIEmbeddings.html#langchain_community.embeddings.openai.OpenAIEmbeddings "langchain_community.embeddings.openai.OpenAIEmbeddings")

Deprecated since version 0.0.9: Use `:class:`~langchain_openai.AzureOpenAIEmbeddings`` instead. It will not be removed until langchain-community==1.0.

Azure OpenAI Embeddings API.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _allowed\_special _: Literal\['all'\] | Set\[str\]__ = \{\}_\#     

_param _azure\_ad\_async\_token\_provider _: Callable\[\[\], Awaitable\[str\]\] | None_ _ = None_\#     

A function that returns an Azure Active Directory token.

Will be invoked on every async request.

_param _azure\_ad\_token _: str | None_ _ = None_\#     

Your Azure Active Directory token.

Automatically inferred from env var AZURE\_OPENAI\_AD\_TOKEN if not provided.

For more: <https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id>.

_param _azure\_ad\_token\_provider _: Callable\[\[\], str\] | None_ _ = None_\#     

A function that returns an Azure Active Directory token.

Will be invoked on every sync request. For async requests, will be invoked if azure\_ad\_async\_token\_provider is not provided.

_param _azure\_endpoint _: str | None_ _ = None_\#     

Your Azure endpoint, including the resource.

Automatically inferred from env var AZURE\_OPENAI\_ENDPOINT if not provided.

Example: https://example-resource.azure.openai.com/

_param _chunk\_size _: int_ _ = 1000_\#     

Maximum number of texts to embed in each batch

_param _default\_headers _: Mapping\[str, str\] | None_ _ = None_\#     

_param _default\_query _: Mapping\[str, object\] | None_ _ = None_\#     

_param _deployment _: str | None_ _ = None_ _\(alias 'azure\_deployment'\)_\#     

A model deployment.

If given sets the base client URL to include /deployments/\{azure\_deployment\}. Note: this means you won’t be able to use non-deployment endpoints.

_param _disallowed\_special _: Literal\['all'\] | Set\[str\] | Sequence\[str\]__ = 'all'_\#     

_param _embedding\_ctx\_length _: int_ _ = 8191_\#     

The maximum number of tokens to embed at once.

_param _headers _: Any_ _ = None_\#     

_param _http\_client _: Any | None_ _ = None_\#     

Optional httpx.Client.

_param _max\_retries _: int_ _ = 2_\#     

Maximum number of retries to make when generating.

_param _model _: str_ _ = 'text-embedding-ada-002'_\#     

_param _model\_kwargs _: Dict\[str, Any\]__\[Optional\]_\#     

Holds any model parameters valid for create call not explicitly specified.

_param _openai\_api\_base _: str | None_ _ = None_ _\(alias 'base\_url'\)_\#     

Base URL path for API requests, leave blank if not using a proxy or service emulator.

_param _openai\_api\_key _: str | None_ _ = None_ _\(alias 'api\_key'\)_\#     

Automatically inferred from env var AZURE\_OPENAI\_API\_KEY if not provided.

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

_param _tiktoken\_enabled _: bool_ _ = True_\#     

Set this to False for non-OpenAI implementations of the embeddings API, e.g. the –extensions openai extension for text-generation-webui

_param _tiktoken\_model\_name _: str | None_ _ = None_\#     

The model name to pass to tiktoken when using this class. Tiktoken is used to count the number of tokens in documents to constrain them to be under a certain limit. By default, when set to None, this will be the same as the embedding model name. However, there are some cases where you may want to use this Embedding class with a model name not supported by tiktoken. This can include when using Azure embeddings or when using one of the many model providers that expose an OpenAI-like API but with different models. In those cases, in order to avoid erroring when tiktoken is called, you can specify a model name to use here.

_param _validate\_base\_url _: bool_ _ = True_\#     

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

Examples using AzureOpenAIEmbeddings

  * [Azure AI Search](https://python.langchain.com/docs/integrations/vectorstores/azuresearch/)

  * [Azure Cosmos DB No SQL](https://python.langchain.com/docs/integrations/vectorstores/azure_cosmos_db_no_sql/)

  * [AzureAISearchRetriever](https://python.langchain.com/docs/integrations/retrievers/azure_ai_search/)

  * [AzureOpenAIEmbeddings](https://python.langchain.com/docs/integrations/text_embedding/azureopenai/)

  * [Microsoft](https://python.langchain.com/docs/integrations/providers/microsoft/)

__On this page