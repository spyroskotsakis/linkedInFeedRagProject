# AzureOpenAIEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/openai/embeddings/langchain_openai.embeddings.azure.AzureOpenAIEmbeddings.html
**Word Count:** 791
**Links Count:** 154
**Scraped:** 2025-07-21 08:27:44
**Status:** completed

---

# AzureOpenAIEmbeddings\#

_class _langchain\_openai.embeddings.azure.AzureOpenAIEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_openai/embeddings/azure.html#AzureOpenAIEmbeddings)\#     

Bases: [`OpenAIEmbeddings`](https://python.langchain.com/api_reference/openai/embeddings/langchain_openai.embeddings.base.OpenAIEmbeddings.html#langchain_openai.embeddings.base.OpenAIEmbeddings "langchain_openai.embeddings.base.OpenAIEmbeddings")

AzureOpenAI embedding model integration.

Setup:     

To access AzureOpenAI embedding models you’ll need to create an Azure account, get an API key, and install the langchain-openai integration package.

You’ll need to have an Azure OpenAI instance deployed. You can deploy a version on Azure Portal following this \[guide\]\(<https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource?pivots=web-portal>\).

Once you have your instance running, make sure you have the name of your instance and key. You can find the key in the Azure Portal, under the “Keys and Endpoint” section of your instance.               pip install -U langchain_openai          # Set up your environment variables (or pass them directly to the model)     export AZURE_OPENAI_API_KEY="your-api-key"     export AZURE_OPENAI_ENDPOINT="https://<your-endpoint>.openai.azure.com/"     export AZURE_OPENAI_API_VERSION="2024-02-01"     

Key init args — completion params:     

model: str     

Name of AzureOpenAI model to use.

dimensions: Optional\[int\]     

Number of dimensions for the embeddings. Can be specified only if the underlying model supports it.

Key init args — client params:     

api\_key: Optional\[SecretStr\]

See full list of supported init args and their descriptions in the params section.

Instantiate:                    from langchain_openai import AzureOpenAIEmbeddings          embeddings = AzureOpenAIEmbeddings(         model="text-embedding-3-large"         # dimensions: Optional[int] = None, # Can specify dimensions with new text-embedding-3 models         # azure_endpoint="https://<your-endpoint>.openai.azure.com/", If not provided, will read env variable AZURE_OPENAI_ENDPOINT         # api_key=... # Can provide an API key directly. If missing read env variable AZURE_OPENAI_API_KEY         # openai_api_version=..., # If not provided, will read env variable AZURE_OPENAI_API_VERSION     )     

Embed single text:                    input_text = "The meaning of life is 42"     vector = embed.embed_query(input_text)     print(vector[:3])                    [-0.024603435769677162, -0.007543657906353474, 0.0039630369283258915]     

Embed multiple texts:                     input_texts = ["Document 1...", "Document 2..."]     vectors = embed.embed_documents(input_texts)     print(len(vectors))     # The first 3 coordinates for the first vector     print(vectors[0][:3])                    2     [-0.024603435769677162, -0.007543657906353474, 0.0039630369283258915]     

Async:                     vector = await embed.aembed_query(input_text)     print(vector[:3])           # multiple:      # await embed.aembed_documents(input_texts)                    [-0.009100092574954033, 0.005071679595857859, -0.0029193938244134188]     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _allowed\_special _: Literal\['all'\] | set\[str\] | None_ _ = None_\#     

_param _azure\_ad\_async\_token\_provider _: Callable\[\[\], Awaitable\[str\]\] | None_ _ = None_\#     

A function that returns an Azure Active Directory token.

Will be invoked on every async request.

_param _azure\_ad\_token _: SecretStr | None_ _\[Optional\]_\#     

Your Azure Active Directory token.

Automatically inferred from env var AZURE\_OPENAI\_AD\_TOKEN if not provided.

For more: <https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id>.

_param _azure\_ad\_token\_provider _: Callable\[\[\], str\] | None_ _ = None_\#     

A function that returns an Azure Active Directory token.

Will be invoked on every sync request. For async requests, will be invoked if azure\_ad\_async\_token\_provider is not provided.

_param _azure\_endpoint _: str | None_ _\[Optional\]_\#     

Your Azure endpoint, including the resource.

Automatically inferred from env var AZURE\_OPENAI\_ENDPOINT if not provided.

Example: https://example-resource.azure.openai.com/

_param _check\_embedding\_ctx\_length _: bool_ _ = True_\#     

Whether to check the token length of inputs and automatically split inputs longer than embedding\_ctx\_length.

_param _chunk\_size _: int_ _ = 2048_\#     

Maximum number of texts to embed in each batch

_param _default\_headers _: Mapping\[str, str\] | None_ _ = None_\#     

_param _default\_query _: Mapping\[str, object\] | None_ _ = None_\#     

_param _deployment _: str | None_ _ = None_ _\(alias 'azure\_deployment'\)_\#     

A model deployment.

If given sets the base client URL to include /deployments/\{azure\_deployment\}. Note: this means you won’t be able to use non-deployment endpoints.

_param _dimensions _: int | None_ _ = None_\#     

The number of dimensions the resulting output embeddings should have.

Only supported in text-embedding-3 and later models.

_param _disallowed\_special _: Literal\['all'\] | set\[str\] | Sequence\[str\] | None_ _ = None_\#     

_param _embedding\_ctx\_length _: int_ _ = 8191_\#     

The maximum number of tokens to embed at once.

_param _headers _: Any_ _ = None_\#     

_param _http\_async\_client _: Any | None_ _ = None_\#     

Optional `httpx.AsyncClient`. Only used for async invocations. Must specify `http_client` as well if you’d like a custom client for sync invocations.

_param _http\_client _: Any | None_ _ = None_\#     

Optional `httpx.Client`. Only used for sync invocations. Must specify `http_async_client` as well if you’d like a custom client for async invocations.

_param _max\_retries _: int_ _ = 2_\#     

Maximum number of retries to make when generating.

_param _model _: str_ _ = 'text-embedding-ada-002'_\#     

_param _model\_kwargs _: dict\[str, Any\]__\[Optional\]_\#     

Holds any model parameters valid for create call not explicitly specified.

_param _openai\_api\_base _: str | None_ _\[Optional\]__\(alias 'base\_url'\)_\#     

Base URL path for API requests, leave blank if not using a proxy or service emulator.

_param _openai\_api\_key _: SecretStr | None_ _\[Optional\]__\(alias 'api\_key'\)_\#     

Automatically inferred from env var AZURE\_OPENAI\_API\_KEY if not provided.

_param _openai\_api\_type _: str | None_ _\[Optional\]_\#     

_param _openai\_api\_version _: str | None_ _\[Optional\]__\(alias 'api\_version'\)_\#     

Automatically inferred from env var OPENAI\_API\_VERSION if not provided.

Set to “2023-05-15” by default if env variable OPENAI\_API\_VERSION is not set.

_param _openai\_organization _: str | None_ _\[Optional\]__\(alias 'organization'\)_\#     

Automatically inferred from env var `OPENAI_ORG_ID` if not provided.

_param _openai\_proxy _: str | None_ _\[Optional\]_\#     

_param _request\_timeout _: float | tuple\[float, float\] | Any | None_ _ = None_ _\(alias 'timeout'\)_\#     

Timeout for requests to OpenAI completion API. Can be float, `httpx.Timeout` or None.

_param _retry\_max\_seconds _: int_ _ = 20_\#     

Max number of seconds to wait between retries

_param _retry\_min\_seconds _: int_ _ = 4_\#     

Min number of seconds to wait between retries

_param _show\_progress\_bar _: bool_ _ = False_\#     

Whether to show a progress bar when embedding.

_param _skip\_empty _: bool_ _ = False_\#     

Whether to skip empty strings when embedding or raise an error. Defaults to not skipping.

_param _tiktoken\_enabled _: bool_ _ = True_\#     

Set this to False for non-OpenAI implementations of the embeddings API, e.g. the `--extensions openai` extension for `text-generation-webui`

_param _tiktoken\_model\_name _: str | None_ _ = None_\#     

The model name to pass to tiktoken when using this class. Tiktoken is used to count the number of tokens in documents to constrain them to be under a certain limit. By default, when set to None, this will be the same as the embedding model name. However, there are some cases where you may want to use this Embedding class with a model name not supported by tiktoken. This can include when using Azure embeddings or when using one of the many model providers that expose an OpenAI-like API but with different models. In those cases, in order to avoid erroring when tiktoken is called, you can specify a model name to use here.

_param _validate\_base\_url _: bool_ _ = True_\#     

_async _aembed\_documents\(

    _texts : list\[str\]_,     _chunk\_size : int | None = None_,     _\*\* kwargs: Any_, \) → list\[list\[float\]\]\#     

Call out to OpenAI’s embedding endpoint async for embedding search docs.

Parameters:     

  * **texts** \(_list_ _\[__str_ _\]_\) – The list of texts to embed.

  * **chunk\_size** \(_int_ _|__None_\) – The chunk size of embeddings. If None, will use the chunk size specified by the class.

  * **kwargs** \(_Any_\) – Additional keyword arguments to pass to the embedding API.

Returns:     

List of embeddings, one for each text.

Return type:     

list\[list\[float\]\]

_async _aembed\_query\(

    _text : str_,     _\*\* kwargs: Any_, \) → list\[float\]\#     

Call out to OpenAI’s embedding endpoint async for embedding query text.

Parameters:     

  * **text** \(_str_\) – The text to embed.

  * **kwargs** \(_Any_\) – Additional keyword arguments to pass to the embedding API.

Returns:     

Embedding for the text.

Return type:     

list\[float\]

embed\_documents\(

    _texts : list\[str\]_,     _chunk\_size : int | None = None_,     _\*\* kwargs: Any_, \) → list\[list\[float\]\]\#     

Call out to OpenAI’s embedding endpoint for embedding search docs.

Parameters:     

  * **texts** \(_list_ _\[__str_ _\]_\) – The list of texts to embed.

  * **chunk\_size** \(_int_ _|__None_\) – The chunk size of embeddings. If None, will use the chunk size specified by the class.

  * **kwargs** \(_Any_\) – Additional keyword arguments to pass to the embedding API.

Returns:     

List of embeddings, one for each text.

Return type:     

list\[list\[float\]\]

embed\_query\(

    _text : str_,     _\*\* kwargs: Any_, \) → list\[float\]\#     

Call out to OpenAI’s embedding endpoint for embedding query text.

Parameters:     

  * **text** \(_str_\) – The text to embed.

  * **kwargs** \(_Any_\) – Additional keyword arguments to pass to the embedding API.

Returns:     

Embedding for the text.

Return type:     

list\[float\]

Examples using AzureOpenAIEmbeddings

  * [Azure AI Search](https://python.langchain.com/docs/integrations/vectorstores/azuresearch/)

  * [Azure Cosmos DB No SQL](https://python.langchain.com/docs/integrations/vectorstores/azure_cosmos_db_no_sql/)

  * [AzureAISearchRetriever](https://python.langchain.com/docs/integrations/retrievers/azure_ai_search/)

  * [AzureOpenAIEmbeddings](https://python.langchain.com/docs/integrations/text_embedding/azureopenai/)

  * [Microsoft](https://python.langchain.com/docs/integrations/providers/microsoft/)

__On this page