# SteamToolkit — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.steam.toolkit.SteamToolkit.html
**Word Count:** 78
**Links Count:** 176
**Scraped:** 2025-07-21 08:12:08
**Status:** completed

---

# SteamToolkit\#

_class _langchain\_community.agent\_toolkits.steam.toolkit.SteamToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/steam/toolkit.html#SteamToolkit)\#     

Bases: [`BaseToolkit`](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseToolkit.html#langchain_core.tools.base.BaseToolkit "langchain_core.tools.base.BaseToolkit")

Steam Toolkit.

Parameters:     

**tools** – List\[BaseTool\]. The tools in the toolkit. Default is an empty list.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _tools _: List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]__ = \[\]_\#     

_classmethod _from\_steam\_api\_wrapper\(

    _steam\_api\_wrapper : [SteamWebAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.steam.SteamWebAPIWrapper.html#langchain_community.utilities.steam.SteamWebAPIWrapper "langchain_community.utilities.steam.SteamWebAPIWrapper")_, \) → SteamToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/steam/toolkit.html#SteamToolkit.from_steam_api_wrapper)\#     

Create a Steam Toolkit from a Steam API Wrapper.

Parameters:     

**steam\_api\_wrapper** \([_SteamWebAPIWrapper_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.steam.SteamWebAPIWrapper.html#langchain_community.utilities.steam.SteamWebAPIWrapper "langchain_community.utilities.steam.SteamWebAPIWrapper")\) – SteamWebAPIWrapper. The Steam API Wrapper.

Returns:     

SteamToolkit. The Steam Toolkit.

Return type:     

_SteamToolkit_

get\_tools\(\) → List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/steam/toolkit.html#SteamToolkit.get_tools)\#     

Get the tools in the toolkit.

Return type:     

_List_\[[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]

Examples using SteamToolkit

  * [Steam Toolkit](https://python.langchain.com/docs/integrations/tools/steam/)

__On this page