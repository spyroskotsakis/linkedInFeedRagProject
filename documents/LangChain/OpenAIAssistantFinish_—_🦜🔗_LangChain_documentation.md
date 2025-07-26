# OpenAIAssistantFinish — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/agents/langchain.agents.openai_assistant.base.OpenAIAssistantFinish.html
**Word Count:** 87
**Links Count:** 173
**Scraped:** 2025-07-21 07:50:02
**Status:** completed

---

# OpenAIAssistantFinish\#

_class _langchain.agents.openai\_assistant.base.OpenAIAssistantFinish[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/openai_assistant/base.html#OpenAIAssistantFinish)\#     

Bases: [`AgentFinish`](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentFinish.html#langchain_core.agents.AgentFinish "langchain_core.agents.AgentFinish")

AgentFinish with run and thread metadata.

Parameters:     

  * **run\_id** – Run id.

  * **thread\_id** – Thread id.

Override init to support instantiation by position for backward compat.

_param _log _: str_ _\[Required\]_\#     

Additional information to log about the return value. This is used to pass along the full LLM prediction, not just the parsed out return value. For example, if the full LLM prediction was Final Answer: 2 you may want to just return 2 as a return value, but pass along the full string as a log \(for debugging or observability purposes\).

_param _return\_values _: dict_ _\[Required\]_\#     

Dictionary of return values.

_param _run\_id _: str_ _\[Required\]_\#     

_param _thread\_id _: str_ _\[Required\]_\#     

_param _type _: Literal\['AgentFinish'\]__ = 'AgentFinish'_\#     

_property _messages _: Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_\#     

Messages that correspond to this observation.

__On this page