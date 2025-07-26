# BedrockAgentFinish — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/agents/langchain_aws.agents.types.BedrockAgentFinish.html
**Word Count:** 93
**Links Count:** 103
**Scraped:** 2025-07-21 08:44:55
**Status:** completed

---

# BedrockAgentFinish\#

_class _langchain\_aws.agents.types.BedrockAgentFinish[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/agents/types.html#BedrockAgentFinish)\#     

Bases: [`AgentFinish`](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentFinish.html#langchain_core.agents.AgentFinish "langchain_core.agents.AgentFinish")

AgentFinish with session id information.

Parameters:     

  * **session\_id** – Session id

  * **trace\_log** – trace log as string when enable\_trace flag is set

Override init to support instantiation by position for backward compat.

_param _log _: str_ _\[Required\]_\#     

Additional information to log about the return value. This is used to pass along the full LLM prediction, not just the parsed out return value. For example, if the full LLM prediction was Final Answer: 2 you may want to just return 2 as a return value, but pass along the full string as a log \(for debugging or observability purposes\).

_param _return\_values _: dict_ _\[Required\]_\#     

Dictionary of return values.

_param _session\_id _: str_ _\[Required\]_\#     

_param _trace\_log _: str | None_ _\[Required\]_\#     

_param _type _: Literal\['AgentFinish'\]__ = 'AgentFinish'_\#     

_property _messages _: Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_\#     

Messages that correspond to this observation.

__On this page