# WatsonxToolkit — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/ibm/toolkit/langchain_ibm.toolkit.WatsonxToolkit.html
**Word Count:** 144
**Links Count:** 100
**Scraped:** 2025-07-21 08:44:55
**Status:** completed

---

# WatsonxToolkit\#

_class _langchain\_ibm.toolkit.WatsonxToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_ibm/toolkit.html#WatsonxToolkit)\#     

Bases: [`BaseToolkit`](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseToolkit.html#langchain_core.tools.base.BaseToolkit "langchain_core.tools.base.BaseToolkit")

IBM watsonx.ai Toolkit.

Setup

To use, you should have `langchain_ibm` python package installed, and the environment variable `WATSONX_APIKEY` set with your API key, or pass it as a named parameter to the constructor.               pip install -U langchain-ibm     export WATSONX_APIKEY="your-api-key"     

Example               from langchain_ibm import WatsonxToolkit          watsonx_toolkit = WatsonxToolkit(         url="https://us-south.ml.cloud.ibm.com",         apikey="*****",     )     tools = watsonx_toolkit.get_tools()          google_search = watsonx_toolkit.get_tool(tool_name="GoogleSearch")          tool_config = {         "maxResults": 3,     }     google_search.set_tool_config(tool_config)     input = {         "input": "Search IBM",     }     search_result = google_search.invoke(input)     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _apikey _: SecretStr | None_ _\[Optional\]_\#     

API key to the watsonx.ai Runtime.

_param _project\_id _: str | None_ _ = None_\#     

ID of the watsonx.ai Studio project.

_param _space\_id _: str | None_ _ = None_\#     

ID of the watsonx.ai Studio space.

_param _token _: SecretStr | None_ _\[Optional\]_\#     

Token to the watsonx.ai Runtime.

_param _url _: SecretStr_ _\[Optional\]_\#     

URL to the watsonx.ai Runtime.

_param _verify _: str | bool | None_ _ = None_\#     

You can pass one of following as verify: \* the path to a CA\_BUNDLE file \* the path of directory with certificates of trusted CAs \* True - default path to truststore will be taken \* False - no verification will be made

_param _watsonx\_client _: APIClient | None_ _ = None_\#     

get\_tool\(

    _tool\_name : str_, \) → [WatsonxTool](https://python.langchain.com/api_reference/ibm/toolkit/langchain_ibm.toolkit.WatsonxTool.html#langchain_ibm.toolkit.WatsonxTool "langchain_ibm.toolkit.WatsonxTool")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_ibm/toolkit.html#WatsonxToolkit.get_tool)\#     

Get the tool with a given name.

Parameters:     

**tool\_name** \(_str_\)

Return type:     

[_WatsonxTool_](https://python.langchain.com/api_reference/ibm/toolkit/langchain_ibm.toolkit.WatsonxTool.html#langchain_ibm.toolkit.WatsonxTool "langchain_ibm.toolkit.WatsonxTool")

get\_tools\(\) → list\[[WatsonxTool](https://python.langchain.com/api_reference/ibm/toolkit/langchain_ibm.toolkit.WatsonxTool.html#langchain_ibm.toolkit.WatsonxTool "langchain_ibm.toolkit.WatsonxTool")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_ibm/toolkit.html#WatsonxToolkit.get_tools)\#     

Get the tools in the toolkit.

Return type:     

list\[[_WatsonxTool_](https://python.langchain.com/api_reference/ibm/toolkit/langchain_ibm.toolkit.WatsonxTool.html#langchain_ibm.toolkit.WatsonxTool "langchain_ibm.toolkit.WatsonxTool")\]

__On this page