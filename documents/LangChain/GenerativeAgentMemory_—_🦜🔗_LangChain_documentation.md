# GenerativeAgentMemory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/generative_agents/langchain_experimental.generative_agents.memory.GenerativeAgentMemory.html
**Word Count:** 158
**Links Count:** 178
**Scraped:** 2025-07-21 08:25:17
**Status:** completed

---

# GenerativeAgentMemory\#

_class _langchain\_experimental.generative\_agents.memory.GenerativeAgentMemory[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/generative_agents/memory.html#GenerativeAgentMemory)\#     

Bases: `BaseMemory`

Memory for the generative agent.

_param _add\_memory\_key _: str_ _ = 'add\_memory'_\#     

_param _aggregate\_importance _: float_ _ = 0.0_\#     

Track the sum of the ‘importance’ of recent memories.

Triggers reflection when it reaches reflection\_threshold.

_param _current\_plan _: List\[str\]__ = \[\]_\#     

The current plan of the agent.

_param _importance\_weight _: float_ _ = 0.15_\#     

How much weight to assign the memory importance.

_param _llm _: [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_ _\[Required\]_\#     

The core language model.

_param _max\_tokens\_limit _: int_ _ = 1200_\#     

_param _memory\_retriever _: [TimeWeightedVectorStoreRetriever](https://python.langchain.com/api_reference/langchain/retrievers/langchain.retrievers.time_weighted_retriever.TimeWeightedVectorStoreRetriever.html#langchain.retrievers.time_weighted_retriever.TimeWeightedVectorStoreRetriever "langchain.retrievers.time_weighted_retriever.TimeWeightedVectorStoreRetriever")_ _\[Required\]_\#     

The retriever to fetch related memories.

_param _most\_recent\_memories\_key _: str_ _ = 'most\_recent\_memories'_\#     

_param _most\_recent\_memories\_token\_key _: str_ _ = 'recent\_memories\_token'_\#     

_param _now\_key _: str_ _ = 'now'_\#     

_param _queries\_key _: str_ _ = 'queries'_\#     

_param _reflecting _: bool_ _ = False_\#     

_param _reflection\_threshold _: float | None_ _ = None_\#     

When aggregate\_importance exceeds reflection\_threshold, stop to reflect.

_param _relevant\_memories\_key _: str_ _ = 'relevant\_memories'_\#     

_param _relevant\_memories\_simple\_key _: str_ _ = 'relevant\_memories\_simple'_\#     

_param _verbose _: bool_ _ = False_\#     

_async _aclear\(\) → None\#     

Async clear memory contents.

Return type:     

None

add\_memories\(

    _memory\_content : str_,     _now : datetime | None = None_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/generative_agents/memory.html#GenerativeAgentMemory.add_memories)\#     

Add an observations or memories to the agent’s memory.

Parameters:     

  * **memory\_content** \(_str_\)

  * **now** \(_datetime_ _|__None_\)

Return type:     

_List_\[str\]

add\_memory\(

    _memory\_content : str_,     _now : datetime | None = None_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/generative_agents/memory.html#GenerativeAgentMemory.add_memory)\#     

Add an observation or memory to the agent’s memory.

Parameters:     

  * **memory\_content** \(_str_\)

  * **now** \(_datetime_ _|__None_\)

Return type:     

_List_\[str\]

_async _aload\_memory\_variables\(

    _inputs : dict\[str, Any\]_, \) → dict\[str, Any\]\#     

Async return key-value pairs given the text input to the chain.

Parameters:     

**inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The inputs to the chain.

Returns:     

A dictionary of key-value pairs.

Return type:     

dict\[str, _Any_\]

_async _asave\_context\(

    _inputs : dict\[str, Any\]_,     _outputs : dict\[str, str\]_, \) → None\#     

Async save the context of this chain run to memory.

Parameters:     

  * **inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The inputs to the chain.

  * **outputs** \(_dict_ _\[__str_ _,__str_ _\]_\) – The outputs of the chain.

Return type:     

None

chain\(

    _prompt : [PromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.prompt.PromptTemplate.html#langchain_core.prompts.prompt.PromptTemplate "langchain_core.prompts.prompt.PromptTemplate")_, \) → [LLMChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm.LLMChain.html#langchain.chains.llm.LLMChain "langchain.chains.llm.LLMChain")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/generative_agents/memory.html#GenerativeAgentMemory.chain)\#     

Parameters:     

**prompt** \([_PromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.prompt.PromptTemplate.html#langchain_core.prompts.prompt.PromptTemplate "langchain_core.prompts.prompt.PromptTemplate")\)

Return type:     

[_LLMChain_](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm.LLMChain.html#langchain.chains.llm.LLMChain "langchain.chains.llm.LLMChain")

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/generative_agents/memory.html#GenerativeAgentMemory.clear)\#     

Clear memory contents.

Return type:     

None

fetch\_memories\(

    _observation : str_,     _now : datetime | None = None_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/generative_agents/memory.html#GenerativeAgentMemory.fetch_memories)\#     

Fetch related memories.

Parameters:     

  * **observation** \(_str_\)

  * **now** \(_datetime_ _|__None_\)

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

format\_memories\_detail\(

    _relevant\_memories : List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/generative_agents/memory.html#GenerativeAgentMemory.format_memories_detail)\#     

Parameters:     

**relevant\_memories** \(_List_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

Return type:     

str

format\_memories\_simple\(

    _relevant\_memories : List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/generative_agents/memory.html#GenerativeAgentMemory.format_memories_simple)\#     

Parameters:     

**relevant\_memories** \(_List_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

Return type:     

str

load\_memory\_variables\(

    _inputs : Dict\[str, Any\]_, \) → Dict\[str, str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/generative_agents/memory.html#GenerativeAgentMemory.load_memory_variables)\#     

Return key-value pairs given the text input to the chain.

Parameters:     

**inputs** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

Return type:     

_Dict_\[str, str\]

pause\_to\_reflect\(

    _now : datetime | None = None_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/generative_agents/memory.html#GenerativeAgentMemory.pause_to_reflect)\#     

Reflect on recent observations and generate ‘insights’.

Parameters:     

**now** \(_datetime_ _|__None_\)

Return type:     

_List_\[str\]

save\_context\(

    _inputs : Dict\[str, Any\]_,     _outputs : Dict\[str, Any\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/generative_agents/memory.html#GenerativeAgentMemory.save_context)\#     

Save the context of this model run to memory.

Parameters:     

  * **inputs** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **outputs** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

Return type:     

None

_property _memory\_variables _: List\[str\]_\#     

Input keys this memory class will load dynamically.

__On this page