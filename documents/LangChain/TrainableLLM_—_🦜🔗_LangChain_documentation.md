# TrainableLLM — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.memorize.tool.TrainableLLM.html
**Word Count:** 16
**Links Count:** 422
**Scraped:** 2025-07-21 08:22:37
**Status:** completed

---

# TrainableLLM\#

_class _langchain\_community.tools.memorize.tool.TrainableLLM\(_\* args_, _\*\* kwargs_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/memorize/tool.html#TrainableLLM)\#     

Protocol for trainable language models.

Methods

`__init__`\(\*args, \*\*kwargs\) |    ---|---   `atrain_unsupervised`\(inputs, \*\*kwargs\) |    `train_unsupervised`\(inputs, \*\*kwargs\) |       \_\_init\_\_\(_\* args_, _\*\* kwargs_\)\#     

_abstractmethod async _atrain\_unsupervised\(

    _inputs : Sequence\[str\]_,     _\*\* kwargs: Any_, \) → [TrainResult](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.gradient_ai.TrainResult.html#langchain_community.llms.gradient_ai.TrainResult "langchain_community.llms.gradient_ai.TrainResult")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/memorize/tool.html#TrainableLLM.atrain_unsupervised)\#     

Parameters:     

  * **inputs** \(_Sequence_ _\[__str_ _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

[_TrainResult_](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.gradient_ai.TrainResult.html#langchain_community.llms.gradient_ai.TrainResult "langchain_community.llms.gradient_ai.TrainResult")

_abstractmethod _train\_unsupervised\(

    _inputs : Sequence\[str\]_,     _\*\* kwargs: Any_, \) → [TrainResult](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.gradient_ai.TrainResult.html#langchain_community.llms.gradient_ai.TrainResult "langchain_community.llms.gradient_ai.TrainResult")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/memorize/tool.html#TrainableLLM.train_unsupervised)\#     

Parameters:     

  * **inputs** \(_Sequence_ _\[__str_ _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

[_TrainResult_](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.gradient_ai.TrainResult.html#langchain_community.llms.gradient_ai.TrainResult "langchain_community.llms.gradient_ai.TrainResult")

__On this page