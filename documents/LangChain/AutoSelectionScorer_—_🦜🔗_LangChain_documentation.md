# AutoSelectionScorer — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.base.AutoSelectionScorer.html
**Word Count:** 44
**Links Count:** 149
**Scraped:** 2025-07-21 08:23:33
**Status:** completed

---

# AutoSelectionScorer\#

_class _langchain\_experimental.rl\_chain.base.AutoSelectionScorer[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/base.html#AutoSelectionScorer)\#     

Bases: [`SelectionScorer`](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.base.SelectionScorer.html#langchain_experimental.rl_chain.base.SelectionScorer "langchain_experimental.rl_chain.base.SelectionScorer")\[[`Event`](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.base.Event.html#langchain_experimental.rl_chain.base.Event "langchain_experimental.rl_chain.base.Event")\], `BaseModel`

Auto selection scorer.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _llm\_chain _: [LLMChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm.LLMChain.html#langchain.chains.llm.LLMChain "langchain.chains.llm.LLMChain")_ _\[Required\]_\#     

_param _prompt _: [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") | None_ _ = None_\#     

_param _scoring\_criteria\_template\_str _: str | None_ _ = None_\#     

_static _get\_default\_prompt\(\) → [ChatPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html#langchain_core.prompts.chat.ChatPromptTemplate "langchain_core.prompts.chat.ChatPromptTemplate")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/base.html#AutoSelectionScorer.get_default_prompt)\#     

Return type:     

[_ChatPromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html#langchain_core.prompts.chat.ChatPromptTemplate "langchain_core.prompts.chat.ChatPromptTemplate")

_static _get\_default\_system\_prompt\(\) → [SystemMessagePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.SystemMessagePromptTemplate.html#langchain_core.prompts.chat.SystemMessagePromptTemplate "langchain_core.prompts.chat.SystemMessagePromptTemplate")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/base.html#AutoSelectionScorer.get_default_system_prompt)\#     

Return type:     

[_SystemMessagePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.SystemMessagePromptTemplate.html#langchain_core.prompts.chat.SystemMessagePromptTemplate "langchain_core.prompts.chat.SystemMessagePromptTemplate")

score\_response\(

    _inputs : Dict\[str, Any\]_,     _llm\_response : str_,     _event : [Event](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.base.Event.html#langchain_experimental.rl_chain.base.Event "langchain_experimental.rl_chain.base.Event")_, \) → float[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/base.html#AutoSelectionScorer.score_response)\#     

Parameters:     

  * **inputs** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **llm\_response** \(_str_\)

  * **event** \([_Event_](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.base.Event.html#langchain_experimental.rl_chain.base.Event "langchain_experimental.rl_chain.base.Event")\)

Return type:     

float

__On this page