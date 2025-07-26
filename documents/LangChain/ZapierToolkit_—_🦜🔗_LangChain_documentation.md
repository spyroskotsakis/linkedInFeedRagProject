# ZapierToolkit — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.zapier.toolkit.ZapierToolkit.html
**Word Count:** 93
**Links Count:** 183
**Scraped:** 2025-07-21 08:19:43
**Status:** completed

---

# ZapierToolkit\#

_class _langchain\_community.agent\_toolkits.zapier.toolkit.ZapierToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/zapier/toolkit.html#ZapierToolkit)\#     

Bases: [`BaseToolkit`](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseToolkit.html#langchain_core.tools.base.BaseToolkit "langchain_core.tools.base.BaseToolkit")

Zapier Toolkit.

Parameters:     

**tools** – List\[BaseTool\]. The tools in the toolkit. Default is an empty list.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _tools _: List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]__ = \[\]_\#     

_async classmethod _async\_from\_zapier\_nla\_wrapper\(

    _zapier\_nla\_wrapper : [ZapierNLAWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.zapier.ZapierNLAWrapper.html#langchain_community.utilities.zapier.ZapierNLAWrapper "langchain_community.utilities.zapier.ZapierNLAWrapper")_, \) → ZapierToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/zapier/toolkit.html#ZapierToolkit.async_from_zapier_nla_wrapper)\#     

Async create a toolkit from a ZapierNLAWrapper.

Parameters:     

**zapier\_nla\_wrapper** \([_ZapierNLAWrapper_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.zapier.ZapierNLAWrapper.html#langchain_community.utilities.zapier.ZapierNLAWrapper "langchain_community.utilities.zapier.ZapierNLAWrapper")\) – ZapierNLAWrapper. The Zapier NLA wrapper.

Returns:     

ZapierToolkit. The Zapier toolkit.

Return type:     

_ZapierToolkit_

_classmethod _from\_zapier\_nla\_wrapper\(

    _zapier\_nla\_wrapper : [ZapierNLAWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.zapier.ZapierNLAWrapper.html#langchain_community.utilities.zapier.ZapierNLAWrapper "langchain_community.utilities.zapier.ZapierNLAWrapper")_, \) → ZapierToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/zapier/toolkit.html#ZapierToolkit.from_zapier_nla_wrapper)\#     

Create a toolkit from a ZapierNLAWrapper.

Parameters:     

**zapier\_nla\_wrapper** \([_ZapierNLAWrapper_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.zapier.ZapierNLAWrapper.html#langchain_community.utilities.zapier.ZapierNLAWrapper "langchain_community.utilities.zapier.ZapierNLAWrapper")\) – ZapierNLAWrapper. The Zapier NLA wrapper.

Returns:     

ZapierToolkit. The Zapier toolkit.

Return type:     

_ZapierToolkit_

get\_tools\(\) → List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/zapier/toolkit.html#ZapierToolkit.get_tools)\#     

Get the tools in the toolkit.

Return type:     

_List_\[[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]

Examples using ZapierToolkit

  * [Zapier Natural Language Actions](https://python.langchain.com/docs/integrations/tools/zapier/)

__On this page