# NasaToolkit — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.nasa.toolkit.NasaToolkit.html
**Word Count:** 61
**Links Count:** 176
**Scraped:** 2025-07-21 08:03:18
**Status:** completed

---

# NasaToolkit\#

_class _langchain\_community.agent\_toolkits.nasa.toolkit.NasaToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/nasa/toolkit.html#NasaToolkit)\#     

Bases: [`BaseToolkit`](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseToolkit.html#langchain_core.tools.base.BaseToolkit "langchain_core.tools.base.BaseToolkit")

Nasa Toolkit.

Parameters:     

**tools** – List\[BaseTool\]. The tools in the toolkit. Default is an empty list.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _tools _: List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]__ = \[\]_\#     

_classmethod _from\_nasa\_api\_wrapper\(

    _nasa\_api\_wrapper : [NasaAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.nasa.NasaAPIWrapper.html#langchain_community.utilities.nasa.NasaAPIWrapper "langchain_community.utilities.nasa.NasaAPIWrapper")_, \) → NasaToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/nasa/toolkit.html#NasaToolkit.from_nasa_api_wrapper)\#     

Parameters:     

**nasa\_api\_wrapper** \([_NasaAPIWrapper_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.nasa.NasaAPIWrapper.html#langchain_community.utilities.nasa.NasaAPIWrapper "langchain_community.utilities.nasa.NasaAPIWrapper")\)

Return type:     

_NasaToolkit_

get\_tools\(\) → List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/nasa/toolkit.html#NasaToolkit.get_tools)\#     

Get the tools in the toolkit.

Return type:     

_List_\[[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]

Examples using NasaToolkit

  * [NASA Toolkit](https://python.langchain.com/docs/integrations/tools/nasa/)

__On this page