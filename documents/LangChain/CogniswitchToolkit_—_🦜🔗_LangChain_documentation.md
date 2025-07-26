# CogniswitchToolkit — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.cogniswitch.toolkit.CogniswitchToolkit.html
**Word Count:** 83
**Links Count:** 172
**Scraped:** 2025-07-21 08:10:17
**Status:** completed

---

# CogniswitchToolkit\#

_class _langchain\_community.agent\_toolkits.cogniswitch.toolkit.CogniswitchToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/cogniswitch/toolkit.html#CogniswitchToolkit)\#     

Bases: [`BaseToolkit`](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseToolkit.html#langchain_core.tools.base.BaseToolkit "langchain_core.tools.base.BaseToolkit")

Toolkit for CogniSwitch.

Use the toolkit to get all the tools present in the Cogniswitch and use them to interact with your knowledge.

Parameters:     

  * **cs\_token** – str. The Cogniswitch token.

  * **OAI\_token** – str. The OpenAI API token.

  * **apiKey** – str. The Cogniswitch OAuth token.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _OAI\_token _: str_ _\[Required\]_\#     

_param _apiKey _: str_ _\[Required\]_\#     

_param _cs\_token _: str_ _\[Required\]_\#     

get\_tools\(\) → List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/cogniswitch/toolkit.html#CogniswitchToolkit.get_tools)\#     

Get the tools in the toolkit.

Return type:     

_List_\[[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]

Examples using CogniswitchToolkit

  * [Cogniswitch Toolkit](https://python.langchain.com/docs/integrations/tools/cogniswitch/)

__On this page