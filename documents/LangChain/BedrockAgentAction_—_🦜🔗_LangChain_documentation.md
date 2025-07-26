# BedrockAgentAction — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/agents/langchain_aws.agents.types.BedrockAgentAction.html
**Word Count:** 133
**Links Count:** 107
**Scraped:** 2025-07-21 08:28:38
**Status:** completed

---

# BedrockAgentAction\#

_class _langchain\_aws.agents.types.BedrockAgentAction[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/agents/types.html#BedrockAgentAction)\#     

Bases: [`AgentAction`](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction")

AgentAction with session id information.

Parameters:     

  * **session\_id** – session id

  * **trace\_log** – trace log as string when enable\_trace flag is set

Create an AgentAction.

Parameters:     

  * **tool** – The name of the tool to execute.

  * **tool\_input** – The input to pass in to the Tool.

  * **log** – Additional information to log about the action.

_param _invocation\_id _: str | None_ _\[Required\]_\#     

_param _log _: str_ _\[Required\]_\#     

Additional information to log about the action. This log can be used in a few ways. First, it can be used to audit what exactly the LLM predicted to lead to this \(tool, tool\_input\). Second, it can be used in future iterations to show the LLMs prior thoughts. This is useful when \(tool, tool\_input\) does not contain full information about the LLM prediction \(for example, any thought before the tool/tool\_input\).

_param _session\_id _: str_ _\[Required\]_\#     

_param _tool _: str_ _\[Required\]_\#     

The name of the Tool to execute.

_param _tool\_input _: str | dict_ _\[Required\]_\#     

The input to pass in to the Tool.

_param _trace\_log _: str | None_ _\[Required\]_\#     

_param _type _: Literal\['AgentAction'\]__ = 'AgentAction'_\#     

_property _messages _: Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_\#     

Return the messages that correspond to this action.

__On this page