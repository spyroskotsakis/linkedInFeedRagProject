# AgentStep — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentStep.html
**Word Count:** 24
**Links Count:** 111
**Scraped:** 2025-07-21 07:55:55
**Status:** completed

---

# AgentStep\#

_class _langchain\_core.agents.AgentStep[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/agents.html#AgentStep)\#     

Bases: [`Serializable`](https://python.langchain.com/api_reference/core/load/langchain_core.load.serializable.Serializable.html#langchain_core.load.serializable.Serializable "langchain_core.load.serializable.Serializable")

Result of running an AgentAction.

_param _action _: [AgentAction](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction")_ _\[Required\]_\#     

The AgentAction that was executed.

_param _observation _: Any_ _\[Required\]_\#     

The result of the AgentAction.

_property _messages _: Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_\#     

Messages that correspond to this observation.

__On this page