# ConneryToolkit — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.connery.toolkit.ConneryToolkit.html
**Word Count:** 86
**Links Count:** 178
**Scraped:** 2025-07-21 08:09:13
**Status:** completed

---

# ConneryToolkit\#

_class _langchain\_community.agent\_toolkits.connery.toolkit.ConneryToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/connery/toolkit.html#ConneryToolkit)\#     

Bases: [`BaseToolkit`](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseToolkit.html#langchain_core.tools.base.BaseToolkit "langchain_core.tools.base.BaseToolkit")

Toolkit with a list of Connery Actions as tools.

Parameters:     

**tools** \(_List_ _\[_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]_\) – The list of Connery Actions.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _tools _: List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]__\[Required\]_\#     

_classmethod _create\_instance\(

    _connery\_service : [ConneryService](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.connery.service.ConneryService.html#langchain_community.tools.connery.service.ConneryService "langchain_community.tools.connery.service.ConneryService")_, \) → ConneryToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/connery/toolkit.html#ConneryToolkit.create_instance)\#     

Creates a Connery Toolkit using a Connery Service.

Parameters:     

**connery\_service** \([_ConneryService_](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.connery.service.ConneryService.html#langchain_community.tools.connery.service.ConneryService "langchain_community.tools.connery.service.ConneryService")\) – The Connery Service to get the list of Connery Actions.

Returns:     

The Connery Toolkit.

Return type:     

ConneryToolkit

get\_tools\(\) → List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/connery/toolkit.html#ConneryToolkit.get_tools)\#     

Returns the list of Connery Actions.

Return type:     

_List_\[[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]

Examples using ConneryToolkit

  * [Connery Toolkit](https://python.langchain.com/docs/integrations/tools/connery_toolkit/)

  * [Connery Toolkit and Tools](https://python.langchain.com/docs/integrations/tools/connery/)

__On this page