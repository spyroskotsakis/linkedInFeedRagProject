# OpenAPIToolkit — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.openapi.toolkit.OpenAPIToolkit.html
**Word Count:** 109
**Links Count:** 184
**Scraped:** 2025-07-21 08:20:44
**Status:** completed

---

# OpenAPIToolkit\#

_class _langchain\_community.agent\_toolkits.openapi.toolkit.OpenAPIToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/openapi/toolkit.html#OpenAPIToolkit)\#     

Bases: [`BaseToolkit`](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseToolkit.html#langchain_core.tools.base.BaseToolkit "langchain_core.tools.base.BaseToolkit")

Toolkit for interacting with an OpenAPI API.

_Security Note_ : This toolkit contains tools that can read and modify     

the state of a service; e.g., by creating, deleting, or updating, reading underlying data.

For example, this toolkit can be used to delete data exposed via an OpenAPI compliant API.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _allow\_dangerous\_requests _: bool_ _ = False_\#     

Allow dangerous requests. See documentation for details.

_param _json\_agent _: Any_ _\[Required\]_\#     

The JSON agent.

_param _requests\_wrapper _: [TextRequestsWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.requests.TextRequestsWrapper.html#langchain_community.utilities.requests.TextRequestsWrapper "langchain_community.utilities.requests.TextRequestsWrapper")_ _\[Required\]_\#     

The requests wrapper.

_classmethod _from\_llm\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _json\_spec : [JsonSpec](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.json.tool.JsonSpec.html#langchain_community.tools.json.tool.JsonSpec "langchain_community.tools.json.tool.JsonSpec")_,     _requests\_wrapper : [TextRequestsWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.requests.TextRequestsWrapper.html#langchain_community.utilities.requests.TextRequestsWrapper "langchain_community.utilities.requests.TextRequestsWrapper")_,     _allow\_dangerous\_requests : bool = False_,     _\*\* kwargs: Any_, \) → OpenAPIToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/openapi/toolkit.html#OpenAPIToolkit.from_llm)\#     

Create json agent from llm, then initialize.

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\)

  * **json\_spec** \([_JsonSpec_](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.json.tool.JsonSpec.html#langchain_community.tools.json.tool.JsonSpec "langchain_community.tools.json.tool.JsonSpec")\)

  * **requests\_wrapper** \([_TextRequestsWrapper_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.requests.TextRequestsWrapper.html#langchain_community.utilities.requests.TextRequestsWrapper "langchain_community.utilities.requests.TextRequestsWrapper")\)

  * **allow\_dangerous\_requests** \(_bool_\)

  * **kwargs** \(_Any_\)

Return type:     

_OpenAPIToolkit_

get\_tools\(\) → List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/openapi/toolkit.html#OpenAPIToolkit.get_tools)\#     

Get the tools in the toolkit.

Return type:     

_List_\[[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]

Examples using OpenAPIToolkit

  * [OpenAPI Toolkit](https://python.langchain.com/docs/integrations/tools/openapi/)

__On this page