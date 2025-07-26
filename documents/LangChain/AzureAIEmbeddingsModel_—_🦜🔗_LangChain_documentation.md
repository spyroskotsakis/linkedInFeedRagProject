# AzureAIEmbeddingsModel — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/azure_ai/embeddings/langchain_azure_ai.embeddings.inference.AzureAIEmbeddingsModel.html
**Word Count:** 230
**Links Count:** 109
**Scraped:** 2025-07-21 07:52:07
**Status:** completed

---

# AzureAIEmbeddingsModel\#

_class _langchain\_azure\_ai.embeddings.inference.AzureAIEmbeddingsModel[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/embeddings/inference.html#AzureAIEmbeddingsModel)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Azure AI model inference for embeddings.

Examples

If your endpoint supports multiple models, indicate the parameter model\_name:

Troubleshooting:     

To diagnostic issues with the model, you can enable debug logging:

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _api\_version _: str | None_ _ = None_\#     

The API version to use for the Azure AI model inference API. If None, the default version is used.

_param _client\_kwargs _: Dict\[str, Any\]__ = \{\}_\#     

Additional kwargs for the Azure AI client used.

_param _credential _: str | AzureKeyCredential | TokenCredential_ _\[Required\]_\#     

The API key or credential to use for the Azure AI model inference.

_param _dimensions _: int | None_ _ = None_\#     

The number of dimensions in the embeddings to generate. If None, the model’s default is used.

_param _embed\_batch\_size _: int_ _ = 1024_\#     

The batch size for embedding requests. The default is 1024.

_param _endpoint _: str | None_ _ = None_\#     

The endpoint URI where the model is deployed. Either this or the project\_connection\_string parameter must be specified.

_param _model\_kwargs _: Dict\[str, Any\]__ = \{\}_\#     

Additional kwargs model parameters.

_param _model\_name _: str | None_ _ = None_ _\(alias 'model'\)_\#     

The name of the model to use for inference, if the endpoint is running more than one model. If not, this parameter is ignored.

_param _project\_connection\_string _: str | None_ _ = None_\#     

The connection string to use for the Azure AI project. If this is specified, then the endpoint parameter becomes optional and credential has to be of type TokenCredential.

_classmethod _validate\_environment\(

    _values : Dict_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/embeddings/inference.html#AzureAIEmbeddingsModel.validate_environment)\#     

Validate that api key exists in environment.

Parameters:     

**values** \(_Dict_\)

Return type:     

_Any_

_async _aembed\_documents\(

    _texts : list\[str\]_, \) → list\[list\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/embeddings/inference.html#AzureAIEmbeddingsModel.aembed_documents)\#     

Asynchronous Embed search docs.

Parameters:     

**texts** \(_list_ _\[__str_ _\]_\) – List of text to embed.

Returns:     

List of embeddings.

Return type:     

list\[list\[float\]\]

_async _aembed\_query\(

    _text : str_, \) → list\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/embeddings/inference.html#AzureAIEmbeddingsModel.aembed_query)\#     

Asynchronous Embed query text.

Parameters:     

**text** \(_str_\) – Text to embed.

Returns:     

Embedding.

Return type:     

list\[float\]

embed\_documents\(

    _texts : list\[str\]_, \) → list\[list\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/embeddings/inference.html#AzureAIEmbeddingsModel.embed_documents)\#     

Embed search docs.

Parameters:     

**texts** \(_list_ _\[__str_ _\]_\) – List of text to embed.

Returns:     

List of embeddings.

Return type:     

list\[list\[float\]\]

embed\_query\(_text : str_\) → list\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/embeddings/inference.html#AzureAIEmbeddingsModel.embed_query)\#     

Embed query text.

Parameters:     

**text** \(_str_\) – Text to embed.

Returns:     

Embedding.

Return type:     

list\[float\]

__On this page