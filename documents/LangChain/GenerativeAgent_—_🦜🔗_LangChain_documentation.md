# GenerativeAgent — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/generative_agents/langchain_experimental.generative_agents.generative_agent.GenerativeAgent.html
**Word Count:** 160
**Links Count:** 142
**Scraped:** 2025-07-21 08:24:27
**Status:** completed

---

# GenerativeAgent\#

_class _langchain\_experimental.generative\_agents.generative\_agent.GenerativeAgent[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/generative_agents/generative_agent.html#GenerativeAgent)\#     

Bases: `BaseModel`

Agent as a character with memory and innate characteristics.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _age _: int | None_ _ = None_\#     

The optional age of the character.

_param _daily\_summaries _: List\[str\]__\[Optional\]_\#     

Summary of the events in the plan that the agent took.

_param _last\_refreshed _: datetime_ _\[Optional\]_\#     

The last time the character’s summary was regenerated.

_param _llm _: [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_ _\[Required\]_\#     

The underlying language model.

_param _memory _: [GenerativeAgentMemory](https://python.langchain.com/api_reference/experimental/generative_agents/langchain_experimental.generative_agents.memory.GenerativeAgentMemory.html#langchain_experimental.generative_agents.memory.GenerativeAgentMemory "langchain_experimental.generative_agents.memory.GenerativeAgentMemory")_ _\[Required\]_\#     

The memory object that combines relevance, recency, and ‘importance’.

_param _name _: str_ _\[Required\]_\#     

The character’s name.

_param _status _: str_ _\[Required\]_\#     

The traits of the character you wish not to change.

_param _summary _: str_ _ = ''_\#     

Stateful self-summary generated via reflection on the character’s memory.

_param _summary\_refresh\_seconds _: int_ _ = 3600_\#     

How frequently to re-generate the summary.

_param _traits _: str_ _ = 'N/A'_\#     

Permanent traits to ascribe to the character.

_param _verbose _: bool_ _ = False_\#     

chain\(

    _prompt : [PromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.prompt.PromptTemplate.html#langchain_core.prompts.prompt.PromptTemplate "langchain_core.prompts.prompt.PromptTemplate")_, \) → [LLMChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm.LLMChain.html#langchain.chains.llm.LLMChain "langchain.chains.llm.LLMChain")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/generative_agents/generative_agent.html#GenerativeAgent.chain)\#     

Create a chain with the same settings as the agent.

Parameters:     

**prompt** \([_PromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.prompt.PromptTemplate.html#langchain_core.prompts.prompt.PromptTemplate "langchain_core.prompts.prompt.PromptTemplate")\)

Return type:     

[_LLMChain_](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm.LLMChain.html#langchain.chains.llm.LLMChain "langchain.chains.llm.LLMChain")

generate\_dialogue\_response\(

    _observation : str_,     _now : datetime | None = None_, \) → Tuple\[bool, str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/generative_agents/generative_agent.html#GenerativeAgent.generate_dialogue_response)\#     

React to a given observation.

Parameters:     

  * **observation** \(_str_\)

  * **now** \(_datetime_ _|__None_\)

Return type:     

_Tuple_\[bool, str\]

generate\_reaction\(

    _observation : str_,     _now : datetime | None = None_, \) → Tuple\[bool, str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/generative_agents/generative_agent.html#GenerativeAgent.generate_reaction)\#     

React to a given observation.

Parameters:     

  * **observation** \(_str_\)

  * **now** \(_datetime_ _|__None_\)

Return type:     

_Tuple_\[bool, str\]

get\_full\_header\(

    _force\_refresh : bool = False_,     _now : datetime | None = None_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/generative_agents/generative_agent.html#GenerativeAgent.get_full_header)\#     

Return a full header of the agent’s status, summary, and current time.

Parameters:     

  * **force\_refresh** \(_bool_\)

  * **now** \(_datetime_ _|__None_\)

Return type:     

str

get\_summary\(

    _force\_refresh : bool = False_,     _now : datetime | None = None_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/generative_agents/generative_agent.html#GenerativeAgent.get_summary)\#     

Return a descriptive summary of the agent.

Parameters:     

  * **force\_refresh** \(_bool_\)

  * **now** \(_datetime_ _|__None_\)

Return type:     

str

summarize\_related\_memories\(

    _observation : str_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/generative_agents/generative_agent.html#GenerativeAgent.summarize_related_memories)\#     

Summarize memories that are most relevant to an observation.

Parameters:     

**observation** \(_str_\)

Return type:     

str

__On this page