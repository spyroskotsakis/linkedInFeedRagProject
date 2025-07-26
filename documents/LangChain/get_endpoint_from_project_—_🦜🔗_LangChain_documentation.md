# get_endpoint_from_project — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/azure_ai/utils/langchain_azure_ai.utils.utils.get_endpoint_from_project.html
**Word Count:** 68
**Links Count:** 78
**Scraped:** 2025-07-21 07:52:07
**Status:** completed

---

# get\_endpoint\_from\_project\#

langchain\_azure\_ai.utils.utils.get\_endpoint\_from\_project\(

    _project\_connection\_string : str_,     _credential : TokenCredential_, \) → Tuple\[str, AzureKeyCredential | TokenCredential\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/utils/utils.html#get_endpoint_from_project)\#     

Retrieves the default inference endpoint and credentials from a project.

It uses the Azure AI project’s connection string to retrieve the inference defaults. The default connection of type Azure AI Services is used to retrieve the endpoint and credentials.

Parameters:     

  * **project\_connection\_string** \(_str_\) – Connection string for the Azure AI project.

  * **credential** \(_TokenCredential_\) – Azure credential object. Credentials must be of type TokenCredential when using the project\_connection\_string parameter.

Returns:     

Endpoint URL and     

credentials.

Return type:     

Tuple\[str, Union\[AzureKeyCredential, TokenCredential\]\]

__On this page