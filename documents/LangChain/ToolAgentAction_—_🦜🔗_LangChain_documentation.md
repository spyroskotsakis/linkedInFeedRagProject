# ToolAgentAction — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/agents/langchain.agents.output_parsers.tools.ToolAgentAction.html
**Word Count:** 197
**Links Count:** 176
**Scraped:** 2025-07-21 07:51:08
**Status:** completed

---

# ToolAgentAction\#

_class _langchain.agents.output\_parsers.tools.ToolAgentAction[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/output_parsers/tools.html#ToolAgentAction)\#     

Bases: [`AgentActionMessageLog`](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentActionMessageLog.html#langchain_core.agents.AgentActionMessageLog "langchain_core.agents.AgentActionMessageLog")

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

_param _tool\_call\_id _: str_ _\[Required\]_\#     

Tool call that this message is responding to.

_param _tool\_input _: str | dict_ _\[Required\]_\#     

The input to pass in to the Tool.

_param _type _: Literal\['AgentActionMessageLog'\]__ = 'AgentActionMessageLog'_\#     

_property _messages _: Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_\#     

Return the messages that correspond to this action.

__On this page