# WatsonxEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/ibm/embeddings/langchain_ibm.embeddings.WatsonxEmbeddings.html
**Word Count:** 221
**Links Count:** 114
**Scraped:** 2025-07-21 08:44:55
**Status:** completed

---

# WatsonxEmbeddings\#

_class _langchain\_ibm.embeddings.WatsonxEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_ibm/embeddings.html#WatsonxEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

IBM watsonx.ai embedding models.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _apikey _: SecretStr | None_ _\[Optional\]_\#     

API key to the Watson Machine Learning or CPD instance.

_param _instance\_id _: SecretStr | None_ _\[Optional\]_\#     

Instance\_id of the CPD instance.

_param _model _: str | None_ _ = None_\#     

Name or alias of the foundation model to use. When using IBM’s watsonx.ai Model Gateway \(public preview\), you can specify any supported third-party model—OpenAI, Anthropic, NVIDIA, Cerebras, or IBM’s own Granite series—via a single, OpenAI-compatible interface. Models must be explicitly provisioned \(opt-in\) through the Gateway to ensure secure, vendor-agnostic access and easy switch-over without reconfiguration.

For more details on configuration and usage, see IBM watsonx Model Gateway docs: [https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/fm-model-gateway.html?context=wx&audience=wdp](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/fm-model-gateway.html?context=wx&audience=wdp)

_param _model\_id _: str | None_ _ = None_\#     

Type of model to use.

_param _params _: Dict | None_ _ = None_\#     

Model parameters to use during request generation.

_param _password _: SecretStr | None_ _\[Optional\]_\#     

Password to the CPD instance.

_param _project\_id _: str | None_ _ = None_\#     

ID of the Watson Studio project.

_param _space\_id _: str | None_ _ = None_\#     

ID of the Watson Studio space.

_param _token _: SecretStr | None_ _\[Optional\]_\#     

Token to the CPD instance.

_param _url _: SecretStr_ _\[Optional\]_\#     

URL to the Watson Machine Learning or CPD instance.

_param _username _: SecretStr | None_ _\[Optional\]_\#     

Username to the CPD instance.

_param _verify _: str | bool | None_ _ = None_\#     

You can pass one of following as verify: \* the path to a CA\_BUNDLE file \* the path of directory with certificates of trusted CAs \* True - default path to truststore will be taken \* False - no verification will be made

_param _version _: SecretStr | None_ _ = None_\#     

Version of the CPD instance.

_async _aembed\_documents\(

    _texts : List\[str\]_,     _\*\* kwargs: Any_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_ibm/embeddings.html#WatsonxEmbeddings.aembed_documents)\#     

Asynchronous Embed search docs.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

_List_\[_List_\[float\]\]

_async _aembed\_query\(

    _text : str_,     _\*\* kwargs: Any_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_ibm/embeddings.html#WatsonxEmbeddings.aembed_query)\#     

Asynchronous Embed query text.

Parameters:     

  * **text** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

_List_\[float\]

embed\_documents\(

    _texts : List\[str\]_,     _\*\* kwargs: Any_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_ibm/embeddings.html#WatsonxEmbeddings.embed_documents)\#     

Embed search docs.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_,     _\*\* kwargs: Any_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_ibm/embeddings.html#WatsonxEmbeddings.embed_query)\#     

Embed query text.

Parameters:     

  * **text** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

_List_\[float\]

__On this page