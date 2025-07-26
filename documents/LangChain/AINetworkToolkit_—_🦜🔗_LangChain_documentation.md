# AINetworkToolkit — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.ainetwork.toolkit.AINetworkToolkit.html
**Word Count:** 112
**Links Count:** 172
**Scraped:** 2025-07-21 08:00:56
**Status:** completed

---

# AINetworkToolkit\#

_class _langchain\_community.agent\_toolkits.ainetwork.toolkit.AINetworkToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/ainetwork/toolkit.html#AINetworkToolkit)\#     

Bases: [`BaseToolkit`](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseToolkit.html#langchain_core.tools.base.BaseToolkit "langchain_core.tools.base.BaseToolkit")

Toolkit for interacting with AINetwork Blockchain.

_Security Note_ : This toolkit contains tools that can read and modify     

the state of a service; e.g., by reading, creating, updating, deleting data associated with this service.

See <https://python.langchain.com/docs/security> for more information.

Parameters:     

  * **network** – Optional. The network to connect to. Default is “testnet”. Options are “mainnet” or “testnet”.

  * **interface** – Optional. The interface to use. If not provided, will attempt to authenticate with the network. Default is None.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _interface _: Ain | None_ _ = None_\#     

_param _network _: Literal\['mainnet', 'testnet'\] | None_ _ = 'testnet'_\#     

get\_tools\(\) → List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/ainetwork/toolkit.html#AINetworkToolkit.get_tools)\#     

Get the tools in the toolkit.

Return type:     

_List_\[[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]

Examples using AINetworkToolkit

  * [AINetwork](https://python.langchain.com/docs/integrations/providers/ainetwork/)

  * [AINetwork Toolkit](https://python.langchain.com/docs/integrations/tools/ainetwork/)

__On this page