# PolygonToolkit — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.polygon.toolkit.PolygonToolkit.html
**Word Count:** 78
**Links Count:** 177
**Scraped:** 2025-07-21 08:18:17
**Status:** completed

---

# PolygonToolkit\#

_class _langchain\_community.agent\_toolkits.polygon.toolkit.PolygonToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/polygon/toolkit.html#PolygonToolkit)\#     

Bases: [`BaseToolkit`](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseToolkit.html#langchain_core.tools.base.BaseToolkit "langchain_core.tools.base.BaseToolkit")

Polygon Toolkit.

Parameters:     

**tools** – List\[BaseTool\]. The tools in the toolkit.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _tools _: List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]__ = \[\]_\#     

_classmethod _from\_polygon\_api\_wrapper\(

    _polygon\_api\_wrapper : [PolygonAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.polygon.PolygonAPIWrapper.html#langchain_community.utilities.polygon.PolygonAPIWrapper "langchain_community.utilities.polygon.PolygonAPIWrapper")_, \) → PolygonToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/polygon/toolkit.html#PolygonToolkit.from_polygon_api_wrapper)\#     

Create a Polygon Toolkit from a Polygon API Wrapper.

Parameters:     

**polygon\_api\_wrapper** \([_PolygonAPIWrapper_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.polygon.PolygonAPIWrapper.html#langchain_community.utilities.polygon.PolygonAPIWrapper "langchain_community.utilities.polygon.PolygonAPIWrapper")\) – PolygonAPIWrapper. The Polygon API Wrapper.

Returns:     

PolygonToolkit. The Polygon Toolkit.

Return type:     

_PolygonToolkit_

get\_tools\(\) → List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/polygon/toolkit.html#PolygonToolkit.get_tools)\#     

Get the tools in the toolkit.

Return type:     

_List_\[[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]

Examples using PolygonToolkit

  * [Polygon IO Toolkit](https://python.langchain.com/docs/integrations/tools/polygon_toolkit/)

  * [Polygon IO Toolkit and Tools](https://python.langchain.com/docs/integrations/tools/polygon/)

__On this page