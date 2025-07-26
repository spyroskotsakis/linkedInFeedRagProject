# AzureAiServicesToolkit — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.azure_ai_services.AzureAiServicesToolkit.html
**Word Count:** 54
**Links Count:** 166
**Scraped:** 2025-07-21 08:11:12
**Status:** completed

---

# AzureAiServicesToolkit\#

_class _langchain\_community.agent\_toolkits.azure\_ai\_services.AzureAiServicesToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/azure_ai_services.html#AzureAiServicesToolkit)\#     

Bases: [`BaseToolkit`](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseToolkit.html#langchain_core.tools.base.BaseToolkit "langchain_core.tools.base.BaseToolkit")

Toolkit for Azure AI Services.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

get\_tools\(\) → List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/azure_ai_services.html#AzureAiServicesToolkit.get_tools)\#     

Get the tools in the toolkit.

Return type:     

_List_\[[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]

Examples using AzureAiServicesToolkit

  * [Azure AI Services Toolkit](https://python.langchain.com/docs/integrations/tools/azure_ai_services/)

__On this page