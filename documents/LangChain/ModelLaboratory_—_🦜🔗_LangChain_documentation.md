# ModelLaboratory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/model_laboratory/langchain.model_laboratory.ModelLaboratory.html
**Word Count:** 288
**Links Count:** 109
**Scraped:** 2025-07-21 07:48:06
**Status:** completed

---

# ModelLaboratory\#

_class _langchain.model\_laboratory.ModelLaboratory\(

    _chains : Sequence\[[Chain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.base.Chain.html#langchain.chains.base.Chain "langchain.chains.base.Chain")\]_,     _names : list\[str\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/model_laboratory.html#ModelLaboratory)\#     

A utility to experiment with and compare the performance of different models.

Initialize the ModelLaboratory with chains to experiment with.

Parameters:     

  * **chains** \(_Sequence_ _\[_[_Chain_](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.base.Chain.html#langchain.chains.base.Chain "langchain.chains.base.Chain") _\]_\) – A sequence of chains to experiment with.

  * **variable.** \(_Each chain must have exactly one input and one output_\)

  * **names** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\)

names \(Optional\[List\[str\]\]\): Optional list of names corresponding to each chain.     

If provided, its length must match the number of chains.

Raises:     

  * **ValueError** – If any chain is not an instance of Chain.

  * **ValueError** – If a chain does not have exactly one input variable.

  * **ValueError** – If a chain does not have exactly one output variable.

  * **ValueError** – If the length of names does not match the number of chains.

Parameters:     

  * **chains** \(_Sequence_ _\[_[_Chain_](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.base.Chain.html#langchain.chains.base.Chain "langchain.chains.base.Chain") _\]_\)

  * **names** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\)

Methods

`__init__`\(chains\[, names\]\) | Initialize the ModelLaboratory with chains to experiment with.   ---|---   `compare`\(text\) | Compare model outputs on an input text.   `from_llms`\(llms\[, prompt\]\) | Initialize the ModelLaboratory with LLMs and an optional prompt.      \_\_init\_\_\(

    _chains : Sequence\[[Chain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.base.Chain.html#langchain.chains.base.Chain "langchain.chains.base.Chain")\]_,     _names : list\[str\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/model_laboratory.html#ModelLaboratory.__init__)\#     

Initialize the ModelLaboratory with chains to experiment with.

Parameters:     

  * **chains** \(_Sequence_ _\[_[_Chain_](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.base.Chain.html#langchain.chains.base.Chain "langchain.chains.base.Chain") _\]_\) – A sequence of chains to experiment with.

  * **variable.** \(_Each chain must have exactly one input and one output_\)

  * **names** \(_list_ _\[__str_ _\]__|__None_\)

names \(Optional\[List\[str\]\]\): Optional list of names corresponding to each chain.     

If provided, its length must match the number of chains.

Raises:     

  * **ValueError** – If any chain is not an instance of Chain.

  * **ValueError** – If a chain does not have exactly one input variable.

  * **ValueError** – If a chain does not have exactly one output variable.

  * **ValueError** – If the length of names does not match the number of chains.

Parameters:     

  * **chains** \(_Sequence_ _\[_[_Chain_](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.base.Chain.html#langchain.chains.base.Chain "langchain.chains.base.Chain") _\]_\)

  * **names** \(_list_ _\[__str_ _\]__|__None_\)

compare\(_text : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/model_laboratory.html#ModelLaboratory.compare)\#     

Compare model outputs on an input text.

If a prompt was provided with starting the laboratory, then this text will be fed into the prompt. If no prompt was provided, then the input text is the entire prompt.

Parameters:     

**text** \(_str_\) – input text to run all models on.

Return type:     

None

_classmethod _from\_llms\(

    _llms : list\[[BaseLLM](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.llms.BaseLLM.html#langchain_core.language_models.llms.BaseLLM "langchain_core.language_models.llms.BaseLLM")\]_,     _prompt : [PromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.prompt.PromptTemplate.html#langchain_core.prompts.prompt.PromptTemplate "langchain_core.prompts.prompt.PromptTemplate") | None = None_, \) → ModelLaboratory[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/model_laboratory.html#ModelLaboratory.from_llms)\#     

Initialize the ModelLaboratory with LLMs and an optional prompt.

Parameters:     

  * **llms** \(_List_ _\[_[_BaseLLM_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.llms.BaseLLM.html#langchain_core.language_models.llms.BaseLLM "langchain_core.language_models.llms.BaseLLM") _\]_\) – A list of LLMs to experiment with.

  * **prompt** \(_Optional_ _\[_[_PromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.prompt.PromptTemplate.html#langchain_core.prompts.prompt.PromptTemplate "langchain_core.prompts.prompt.PromptTemplate") _\]_\) – An optional prompt to use with the LLMs. If provided, the prompt must contain exactly one input variable.

Returns:     

An instance of ModelLaboratory initialized with LLMs.

Return type:     

ModelLaboratory

Examples using ModelLaboratory

  * [Manifest](https://python.langchain.com/docs/integrations/llms/manifest/)

__On this page