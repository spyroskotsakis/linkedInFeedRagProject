# InlineAgentConfiguration — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/agents/langchain_aws.agents.types.InlineAgentConfiguration.html
**Word Count:** 11
**Links Count:** 116
**Scraped:** 2025-07-21 08:28:38
**Status:** completed

---

# InlineAgentConfiguration\#

_class _langchain\_aws.agents.types.InlineAgentConfiguration[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/agents/types.html#InlineAgentConfiguration)\#     

Configurations for an Inline Agent.

foundation\_model _: str_\#     

instruction _: str_\#     

enable\_trace _: bool | None_\#     

tools _: List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]_\#     

enable\_human\_input _: bool | None_\#     

enable\_code\_interpreter _: bool | None_\#     

customer\_encryption\_key\_arn _: str | None_\#     

idle\_session\_ttl\_in\_seconds _: int | None_\#     

guardrail\_configuration _: [GuardrailConfiguration](https://python.langchain.com/api_reference/aws/agents/langchain_aws.agents.types.GuardrailConfiguration.html#langchain_aws.agents.types.GuardrailConfiguration "langchain_aws.agents.types.GuardrailConfiguration") | None_\#     

knowledge\_bases _: [KnowledgebaseConfiguration](https://python.langchain.com/api_reference/aws/agents/langchain_aws.agents.types.KnowledgebaseConfiguration.html#langchain_aws.agents.types.KnowledgebaseConfiguration "langchain_aws.agents.types.KnowledgebaseConfiguration") | None_\#     

prompt\_override\_configuration _: Dict | None_\#     

inline\_session\_state _: Dict | None_\#     

__On this page