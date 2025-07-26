# JiraToolkit — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.jira.toolkit.JiraToolkit.html
**Word Count:** 100
**Links Count:** 177
**Scraped:** 2025-07-21 08:03:18
**Status:** completed

---

# JiraToolkit\#

_class _langchain\_community.agent\_toolkits.jira.toolkit.JiraToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/jira/toolkit.html#JiraToolkit)\#     

Bases: [`BaseToolkit`](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseToolkit.html#langchain_core.tools.base.BaseToolkit "langchain_core.tools.base.BaseToolkit")

Jira Toolkit.

_Security Note_ : This toolkit contains tools that can read and modify     

the state of a service; e.g., by creating, deleting, or updating, reading underlying data.

See <https://python.langchain.com/docs/security> for more information.

Parameters:     

**tools** – List\[BaseTool\]. The tools in the toolkit. Default is an empty list.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _tools _: List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]__ = \[\]_\#     

_classmethod _from\_jira\_api\_wrapper\(

    _jira\_api\_wrapper : [JiraAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.jira.JiraAPIWrapper.html#langchain_community.utilities.jira.JiraAPIWrapper "langchain_community.utilities.jira.JiraAPIWrapper")_, \) → JiraToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/jira/toolkit.html#JiraToolkit.from_jira_api_wrapper)\#     

Create a JiraToolkit from a JiraAPIWrapper.

Parameters:     

**jira\_api\_wrapper** \([_JiraAPIWrapper_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.jira.JiraAPIWrapper.html#langchain_community.utilities.jira.JiraAPIWrapper "langchain_community.utilities.jira.JiraAPIWrapper")\) – JiraAPIWrapper. The Jira API wrapper.

Returns:     

JiraToolkit. The Jira toolkit.

Return type:     

_JiraToolkit_

get\_tools\(\) → List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/jira/toolkit.html#JiraToolkit.get_tools)\#     

Get the tools in the toolkit.

Return type:     

_List_\[[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]

Examples using JiraToolkit

  * [Jira Toolkit](https://python.langchain.com/docs/integrations/tools/jira/)

__On this page