# GitLabToolkit — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.gitlab.toolkit.GitLabToolkit.html
**Word Count:** 115
**Links Count:** 177
**Scraped:** 2025-07-21 08:15:47
**Status:** completed

---

# GitLabToolkit\#

_class _langchain\_community.agent\_toolkits.gitlab.toolkit.GitLabToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/gitlab/toolkit.html#GitLabToolkit)\#     

Bases: [`BaseToolkit`](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseToolkit.html#langchain_core.tools.base.BaseToolkit "langchain_core.tools.base.BaseToolkit")

GitLab Toolkit.

_Security Note_ : This toolkit contains tools that can read and modify     

the state of a service; e.g., by creating, deleting, or updating, reading underlying data.

For example, this toolkit can be used to create issues, pull requests, and comments on GitLab.

See <https://python.langchain.com/docs/security> for more information.

Parameters:     

**tools** – List\[BaseTool\]. The tools in the toolkit. Default is an empty list.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _tools _: List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]__ = \[\]_\#     

_classmethod _from\_gitlab\_api\_wrapper\(

    _gitlab\_api\_wrapper : [GitLabAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.gitlab.GitLabAPIWrapper.html#langchain_community.utilities.gitlab.GitLabAPIWrapper "langchain_community.utilities.gitlab.GitLabAPIWrapper")_,     _\*_ ,     _included\_tools : List\[str\] | None = None_, \) → GitLabToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/gitlab/toolkit.html#GitLabToolkit.from_gitlab_api_wrapper)\#     

Create a GitLabToolkit from a GitLabAPIWrapper.

Parameters:     

  * **gitlab\_api\_wrapper** \([_GitLabAPIWrapper_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.gitlab.GitLabAPIWrapper.html#langchain_community.utilities.gitlab.GitLabAPIWrapper "langchain_community.utilities.gitlab.GitLabAPIWrapper")\) – GitLabAPIWrapper. The GitLab API wrapper.

  * **included\_tools** \(_List_ _\[__str_ _\]__|__None_\)

Returns:     

GitLabToolkit. The GitLab toolkit.

Return type:     

_GitLabToolkit_

get\_tools\(\) → List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/gitlab/toolkit.html#GitLabToolkit.get_tools)\#     

Get the tools in the toolkit.

Return type:     

_List_\[[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]

Examples using GitLabToolkit

  * [Gitlab Toolkit](https://python.langchain.com/docs/integrations/tools/gitlab/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)