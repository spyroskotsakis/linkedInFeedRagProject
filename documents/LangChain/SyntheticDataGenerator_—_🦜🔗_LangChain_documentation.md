# SyntheticDataGenerator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/tabular_synthetic_data/langchain_experimental.tabular_synthetic_data.base.SyntheticDataGenerator.html
**Word Count:** 194
**Links Count:** 126
**Scraped:** 2025-07-21 08:24:51
**Status:** completed

---

# SyntheticDataGenerator\#

_class _langchain\_experimental.tabular\_synthetic\_data.base.SyntheticDataGenerator[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/tabular_synthetic_data/base.html#SyntheticDataGenerator)\#     

Bases: `BaseModel`

Generate synthetic data using the given LLM and few-shot template.

Utilizes the provided LLM to produce synthetic data based on the few-shot prompt template.

template\#     

Template for few-shot prompting.

Type:     

[FewShotPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.few_shot.FewShotPromptTemplate.html#langchain_core.prompts.few_shot.FewShotPromptTemplate "langchain_core.prompts.few_shot.FewShotPromptTemplate")

llm\#     

Large Language Model to use for generation.

Type:     

Optional\[[BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\]

llm\_chain\#     

LLM chain with the LLM and few-shot template.

Type:     

Optional\[[Chain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.base.Chain.html#langchain.chains.base.Chain "langchain.chains.base.Chain")\]

example\_input\_key\#     

Key to use for storing example inputs.

Type:     

str

Usage Example:                    >>> template = FewShotPromptTemplate(...)     >>> llm = BaseLanguageModel(...)     >>> generator = SyntheticDataGenerator(template=template, llm=llm)     >>> results = generator.generate(subject="climate change", runs=5)     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _example\_input\_key _: str_ _ = 'example'_\#     

_param _llm _: [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") | None_ _ = None_\#     

_param _llm\_chain _: [Chain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.base.Chain.html#langchain.chains.base.Chain "langchain.chains.base.Chain") | None_ _ = None_\#     

_param _results _: list_ _ = \[\]_\#     

_param _template _: [FewShotPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.few_shot.FewShotPromptTemplate.html#langchain_core.prompts.few_shot.FewShotPromptTemplate "langchain_core.prompts.few_shot.FewShotPromptTemplate")_ _\[Required\]_\#     

_async _agenerate\(

    _subject : str_,     _runs : int_,     _extra : str = ''_,     _\* args: Any_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/tabular_synthetic_data/base.html#SyntheticDataGenerator.agenerate)\#     

Generate synthetic data using the given subject asynchronously.

Note: Since the LLM calls run concurrently, you may have fewer duplicates by adding specific instructions to the “extra” keyword argument.

Parameters:     

  * **subject** \(_str_\) – The subject the synthetic data will be about.

  * **runs** \(_int_\) – Number of times to generate the data asynchronously.

  * **extra** \(_str_\) – Extra instructions for steerability in data generation.

  * **args** \(_Any_\)

  * **kwargs** \(_Any_\)

Returns:     

List of generated synthetic data for the given subject.

Return type:     

List\[str\]

Usage Example:                    >>> results = await generator.agenerate(subject="climate change", runs=5,     extra="Focus on env impacts.")     

generate\(

    _subject : str_,     _runs : int_,     _\* args: Any_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/tabular_synthetic_data/base.html#SyntheticDataGenerator.generate)\#     

Generate synthetic data using the given subject string.

Parameters:     

  * **subject** \(_str_\) – The subject the synthetic data will be about.

  * **runs** \(_int_\) – Number of times to generate the data.

  * **extra** \(_str_\) – Extra instructions for steerability in data generation.

  * **args** \(_Any_\)

  * **kwargs** \(_Any_\)

Returns:     

List of generated synthetic data.

Return type:     

List\[str\]

Usage Example:                    >>> results = generator.generate(subject="climate change", runs=5,     extra="Focus on environmental impacts.")     

__On this page