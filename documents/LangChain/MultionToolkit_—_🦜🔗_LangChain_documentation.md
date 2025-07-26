# MultionToolkit — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.multion.toolkit.MultionToolkit.html
**Word Count:** 95
**Links Count:** 167
**Scraped:** 2025-07-21 08:08:35
**Status:** completed

---

# MultionToolkit\#

_class _langchain\_community.agent\_toolkits.multion.toolkit.MultionToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/multion/toolkit.html#MultionToolkit)\#     

Bases: [`BaseToolkit`](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseToolkit.html#langchain_core.tools.base.BaseToolkit "langchain_core.tools.base.BaseToolkit")

Toolkit for interacting with the Browser Agent.

**Security Note** : This toolkit contains tools that interact with the     

user’s browser via the multion API which grants an agent access to the user’s browser.

Please review the documentation for the multion API to understand the security implications of using this toolkit.

See <https://python.langchain.com/docs/security> for more information.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

get\_tools\(\) → List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/multion/toolkit.html#MultionToolkit.get_tools)\#     

Get the tools in the toolkit.

Return type:     

_List_\[[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]

Examples using MultionToolkit

  * [MultiOn Toolkit](https://python.langchain.com/docs/integrations/tools/multion/)

__On this page