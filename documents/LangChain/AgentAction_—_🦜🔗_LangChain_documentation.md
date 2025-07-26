# AgentAction — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html
**Word Count:** 157
**Links Count:** 114
**Scraped:** 2025-07-21 07:51:39
**Status:** completed

---

# AgentAction\#

_class _langchain\_core.agents.AgentAction[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/agents.html#AgentAction)\#     

Bases: [`Serializable`](https://python.langchain.com/api_reference/core/load/langchain_core.load.serializable.Serializable.html#langchain_core.load.serializable.Serializable "langchain_core.load.serializable.Serializable")

Represents a request to execute an action by an agent.

The action consists of the name of the tool to execute and the input to pass to the tool. The log is used to pass along extra information about the action.

Create an AgentAction.

Parameters:     

  * **tool** – The name of the tool to execute.

  * **tool\_input** – The input to pass in to the Tool.

  * **log** – Additional information to log about the action.

_param _log _: str_ _\[Required\]_\#     

Additional information to log about the action. This log can be used in a few ways. First, it can be used to audit what exactly the LLM predicted to lead to this \(tool, tool\_input\). Second, it can be used in future iterations to show the LLMs prior thoughts. This is useful when \(tool, tool\_input\) does not contain full information about the LLM prediction \(for example, any thought before the tool/tool\_input\).

_param _tool _: str_ _\[Required\]_\#     

The name of the Tool to execute.

_param _tool\_input _: str | dict_ _\[Required\]_\#     

The input to pass in to the Tool.

_param _type _: Literal\['AgentAction'\]__ = 'AgentAction'_\#     

_property _messages _: Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_\#     

Return the messages that correspond to this action.

__On this page