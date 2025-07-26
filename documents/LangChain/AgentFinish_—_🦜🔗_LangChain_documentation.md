# AgentFinish — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentFinish.html
**Word Count:** 93
**Links Count:** 112
**Scraped:** 2025-07-21 07:51:39
**Status:** completed

---

# AgentFinish\#

_class _langchain\_core.agents.AgentFinish[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/agents.html#AgentFinish)\#     

Bases: [`Serializable`](https://python.langchain.com/api_reference/core/load/langchain_core.load.serializable.Serializable.html#langchain_core.load.serializable.Serializable "langchain_core.load.serializable.Serializable")

Final return value of an ActionAgent.

Agents return an AgentFinish when they have reached a stopping condition.

Override init to support instantiation by position for backward compat.

_param _log _: str_ _\[Required\]_\#     

Additional information to log about the return value. This is used to pass along the full LLM prediction, not just the parsed out return value. For example, if the full LLM prediction was Final Answer: 2 you may want to just return 2 as a return value, but pass along the full string as a log \(for debugging or observability purposes\).

_param _return\_values _: dict_ _\[Required\]_\#     

Dictionary of return values.

_param _type _: Literal\['AgentFinish'\]__ = 'AgentFinish'_\#     

_property _messages _: Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_\#     

Messages that correspond to this observation.

__On this page