# JsonToolkit — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.json.toolkit.JsonToolkit.html
**Word Count:** 57
**Links Count:** 169
**Scraped:** 2025-07-21 08:05:36
**Status:** completed

---

# JsonToolkit\#

_class _langchain\_community.agent\_toolkits.json.toolkit.JsonToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/json/toolkit.html#JsonToolkit)\#     

Bases: [`BaseToolkit`](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseToolkit.html#langchain_core.tools.base.BaseToolkit "langchain_core.tools.base.BaseToolkit")

Toolkit for interacting with a JSON spec.

Parameters:     

**spec** – The JSON spec.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _spec _: [JsonSpec](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.json.tool.JsonSpec.html#langchain_community.tools.json.tool.JsonSpec "langchain_community.tools.json.tool.JsonSpec")_ _\[Required\]_\#     

get\_tools\(\) → List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/json/toolkit.html#JsonToolkit.get_tools)\#     

Get the tools in the toolkit.

Return type:     

_List_\[[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]

Examples using JsonToolkit

  * [JSON Toolkit](https://python.langchain.com/docs/integrations/tools/json/)

__On this page