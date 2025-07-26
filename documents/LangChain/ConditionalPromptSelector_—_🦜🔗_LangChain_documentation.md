# ConditionalPromptSelector — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chains/langchain.chains.prompt_selector.ConditionalPromptSelector.html
**Word Count:** 85
**Links Count:** 204
**Scraped:** 2025-07-21 07:49:32
**Status:** completed

---

# ConditionalPromptSelector\#

_class _langchain.chains.prompt\_selector.ConditionalPromptSelector[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/prompt_selector.html#ConditionalPromptSelector)\#     

Bases: [`BasePromptSelector`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.prompt_selector.BasePromptSelector.html#langchain.chains.prompt_selector.BasePromptSelector "langchain.chains.prompt_selector.BasePromptSelector")

Prompt collection that goes through conditionals.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _conditionals _: list\[tuple\[Callable\[\[[BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\], bool\], [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")\]\]__\[Optional\]_\#     

List of conditionals and prompts to use if the conditionals match.

_param _default\_prompt _: [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")_ _\[Required\]_\#     

Default prompt to use if no conditionals match.

get\_prompt\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_, \) → [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/prompt_selector.html#ConditionalPromptSelector.get_prompt)\#     

Get default prompt for a language model.

Parameters:     

**llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – Language model to get prompt for.

Returns:     

Prompt to use for the language model.

Return type:     

[_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")

Examples using ConditionalPromptSelector

  * [Run models locally](https://python.langchain.com/docs/how_to/local_llms/)

__On this page