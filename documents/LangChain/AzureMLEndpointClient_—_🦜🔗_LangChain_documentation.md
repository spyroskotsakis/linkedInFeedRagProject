# AzureMLEndpointClient — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/llms/langchain_community.llms.azureml_endpoint.AzureMLEndpointClient.html
**Word Count:** 21
**Links Count:** 292
**Scraped:** 2025-07-21 08:10:17
**Status:** completed

---

# AzureMLEndpointClient\#

_class _langchain\_community.llms.azureml\_endpoint.AzureMLEndpointClient\(

    _endpoint\_url : str_,     _endpoint\_api\_key : str_,     _deployment\_name : str = ''_,     _timeout : int = 50_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/azureml_endpoint.html#AzureMLEndpointClient)\#     

AzureML Managed Endpoint client.

Initialize the class.

Methods

`__init__`\(endpoint\_url, endpoint\_api\_key\[, ...\]\) | Initialize the class.   ---|---   `call`\(body\[, run\_manager\]\) | call.      Parameters:     

  * **endpoint\_url** \(_str_\)

  * **endpoint\_api\_key** \(_str_\)

  * **deployment\_name** \(_str_\)

  * **timeout** \(_int_\)

\_\_init\_\_\(

    _endpoint\_url : str_,     _endpoint\_api\_key : str_,     _deployment\_name : str = ''_,     _timeout : int = 50_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/azureml_endpoint.html#AzureMLEndpointClient.__init__)\#     

Initialize the class.

Parameters:     

  * **endpoint\_url** \(_str_\)

  * **endpoint\_api\_key** \(_str_\)

  * **deployment\_name** \(_str_\)

  * **timeout** \(_int_\)

Return type:     

None

call\(

    _body : bytes_,     _run\_manager : [CallbackManagerForLLMRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForLLMRun.html#langchain_core.callbacks.manager.CallbackManagerForLLMRun "langchain_core.callbacks.manager.CallbackManagerForLLMRun") | None = None_,     _\*\* kwargs: Any_, \) → bytes[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/azureml_endpoint.html#AzureMLEndpointClient.call)\#     

call.

Parameters:     

  * **body** \(_bytes_\)

  * **run\_manager** \([_CallbackManagerForLLMRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForLLMRun.html#langchain_core.callbacks.manager.CallbackManagerForLLMRun "langchain_core.callbacks.manager.CallbackManagerForLLMRun") _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

bytes

__On this page