# O365Toolkit — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.office365.toolkit.O365Toolkit.html
**Word Count:** 123
**Links Count:** 170
**Scraped:** 2025-07-21 08:17:20
**Status:** completed

---

# O365Toolkit\#

_class _langchain\_community.agent\_toolkits.office365.toolkit.O365Toolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/office365/toolkit.html#O365Toolkit)\#     

Bases: [`BaseToolkit`](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseToolkit.html#langchain_core.tools.base.BaseToolkit "langchain_core.tools.base.BaseToolkit")

Toolkit for interacting with Office 365.

_Security Note_ : This toolkit contains tools that can read and modify     

the state of a service; e.g., by reading, creating, updating, deleting data associated with this service.

For example, this toolkit can be used search through emails and events, send messages and event invites, and create draft messages.

Please make sure that the permissions given by this toolkit are appropriate for your use case.

See <https://python.langchain.com/docs/security> for more information.

Parameters:     

**account** – Optional. The Office 365 account. Default is None.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _account _: Account_ _\[Optional\]_\#     

get\_tools\(\) → List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/office365/toolkit.html#O365Toolkit.get_tools)\#     

Get the tools in the toolkit.

Return type:     

_List_\[[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]

Examples using O365Toolkit

  * [Microsoft](https://python.langchain.com/docs/integrations/providers/microsoft/)

  * [Office365 Toolkit](https://python.langchain.com/docs/integrations/tools/office365/)

__On this page