# AgentActionMessageLog — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentActionMessageLog.html
**Word Count:** 230
**Links Count:** 117
**Scraped:** 2025-07-21 07:53:06
**Status:** completed

---

# AgentActionMessageLog\#

_class _langchain\_core.agents.AgentActionMessageLog[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/agents.html#AgentActionMessageLog)\#     

Bases: [`AgentAction`](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction")

Representation of an action to be executed by an agent.

This is similar to AgentAction, but includes a message log consisting of chat messages. This is useful when working with ChatModels, and is used to reconstruct conversation history from the agent’s perspective.

Create an AgentAction.

Parameters:     

  * **tool** – The name of the tool to execute.

  * **tool\_input** – The input to pass in to the Tool.

  * **log** – Additional information to log about the action.

_param _log _: str_ _\[Required\]_\#     

Additional information to log about the action. This log can be used in a few ways. First, it can be used to audit what exactly the LLM predicted to lead to this \(tool, tool\_input\). Second, it can be used in future iterations to show the LLMs prior thoughts. This is useful when \(tool, tool\_input\) does not contain full information about the LLM prediction \(for example, any thought before the tool/tool\_input\).

_param _message\_log _: Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]__\[Required\]_\#     

Similar to log, this can be used to pass along extra information about what exact messages were predicted by the LLM before parsing out the \(tool, tool\_input\). This is again useful if \(tool, tool\_input\) cannot be used to fully recreate the LLM prediction, and you need that LLM prediction \(for future agent iteration\). Compared to log, this is useful when the underlying LLM is a ChatModel \(and therefore returns messages rather than a string\).

_param _tool _: str_ _\[Required\]_\#     

The name of the Tool to execute.

_param _tool\_input _: str | dict_ _\[Required\]_\#     

The input to pass in to the Tool.

_param _type _: Literal\['AgentActionMessageLog'\]__ = 'AgentActionMessageLog'_\#     

_property _messages _: Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_\#     

Return the messages that correspond to this action.

__On this page