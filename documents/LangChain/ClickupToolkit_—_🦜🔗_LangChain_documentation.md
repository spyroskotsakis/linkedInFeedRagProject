# ClickupToolkit — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.clickup.toolkit.ClickupToolkit.html
**Word Count:** 102
**Links Count:** 177
**Scraped:** 2025-07-21 08:00:56
**Status:** completed

---

# ClickupToolkit\#

_class _langchain\_community.agent\_toolkits.clickup.toolkit.ClickupToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/clickup/toolkit.html#ClickupToolkit)\#     

Bases: [`BaseToolkit`](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseToolkit.html#langchain_core.tools.base.BaseToolkit "langchain_core.tools.base.BaseToolkit")

Clickup Toolkit.

_Security Note_ : This toolkit contains tools that can read and modify     

the state of a service; e.g., by reading, creating, updating, deleting data associated with this service.

See <https://python.langchain.com/docs/security> for more information.

Parameters:     

**tools** – List\[BaseTool\]. The tools in the toolkit. Default is an empty list.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _tools _: List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]__ = \[\]_\#     

_classmethod _from\_clickup\_api\_wrapper\(

    _clickup\_api\_wrapper : [ClickupAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.clickup.ClickupAPIWrapper.html#langchain_community.utilities.clickup.ClickupAPIWrapper "langchain_community.utilities.clickup.ClickupAPIWrapper")_, \) → ClickupToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/clickup/toolkit.html#ClickupToolkit.from_clickup_api_wrapper)\#     

Create a ClickupToolkit from a ClickupAPIWrapper.

Parameters:     

**clickup\_api\_wrapper** \([_ClickupAPIWrapper_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.clickup.ClickupAPIWrapper.html#langchain_community.utilities.clickup.ClickupAPIWrapper "langchain_community.utilities.clickup.ClickupAPIWrapper")\) – ClickupAPIWrapper. The Clickup API wrapper.

Returns:     

ClickupToolkit. The Clickup toolkit.

Return type:     

_ClickupToolkit_

get\_tools\(\) → List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/clickup/toolkit.html#ClickupToolkit.get_tools)\#     

Get the tools in the toolkit.

Return type:     

_List_\[[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]

Examples using ClickupToolkit

  * [ClickUp Toolkit](https://python.langchain.com/docs/integrations/tools/clickup/)

__On this page