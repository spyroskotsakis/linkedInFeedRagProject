# GmailToolkit — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/google_community/gmail/langchain_google_community.gmail.toolkit.GmailToolkit.html
**Word Count:** 91
**Links Count:** 114
**Scraped:** 2025-07-21 07:59:27
**Status:** completed

---

# GmailToolkit\#

_class _langchain\_google\_community.gmail.toolkit.GmailToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/gmail/toolkit.html#GmailToolkit)\#     

Bases: [`BaseToolkit`](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseToolkit.html#langchain_core.tools.base.BaseToolkit "langchain_core.tools.base.BaseToolkit")

Toolkit for interacting with Gmail.

_Security Note_ : This toolkit contains tools that can read and modify     

the state of a service; e.g., by reading, creating, updating, deleting data associated with this service.

For example, this toolkit can be used to send emails on behalf of the associated account.

See <https://python.langchain.com/docs/security> for more information.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _api\_resource _: [Resource](https://python.langchain.com/api_reference/google_community/gmail/langchain_google_community.gmail.search.Resource.html#langchain_google_community.gmail.search.Resource "langchain_google_community.gmail.search.Resource")_ _\[Optional\]_\#     

get\_tools\(\) → List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/gmail/toolkit.html#GmailToolkit.get_tools)\#     

Get the tools in the toolkit.

Return type:     

_List_\[[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]

__On this page