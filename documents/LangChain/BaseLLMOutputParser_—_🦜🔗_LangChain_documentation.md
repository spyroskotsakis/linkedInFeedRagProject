# BaseLLMOutputParser — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseLLMOutputParser.html
**Word Count:** 156
**Links Count:** 137
**Scraped:** 2025-07-21 07:52:36
**Status:** completed

---

# BaseLLMOutputParser\#

_class _langchain\_core.output\_parsers.base.BaseLLMOutputParser[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/output_parsers/base.html#BaseLLMOutputParser)\#     

Abstract base class for parsing the outputs of a model.

Methods

`aparse_result`\(result, \*\[, partial\]\) | Async parse a list of candidate model Generations into a specific format.   ---|---   `parse_result`\(result, \*\[, partial\]\) | Parse a list of candidate model Generations into a specific format.      _async _aparse\_result\(

    _result : list\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]_,     _\*_ ,     _partial : bool = False_, \) → T[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/output_parsers/base.html#BaseLLMOutputParser.aparse_result)\#     

Async parse a list of candidate model Generations into a specific format.

Parameters:     

  * **result** \(_list_ _\[_[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation") _\]_\) – A list of Generations to be parsed. The Generations are assumed to be different candidate outputs for a single model input.

  * **partial** \(_bool_\) – Whether to parse the output as a partial result. This is useful for parsers that can parse partial results. Default is False.

Returns:     

Structured output.

Return type:     

_T_

_abstractmethod _parse\_result\(

    _result : list\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]_,     _\*_ ,     _partial : bool = False_, \) → T[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/output_parsers/base.html#BaseLLMOutputParser.parse_result)\#     

Parse a list of candidate model Generations into a specific format.

Parameters:     

  * **result** \(_list_ _\[_[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation") _\]_\) – A list of Generations to be parsed. The Generations are assumed to be different candidate outputs for a single model input.

  * **partial** \(_bool_\) – Whether to parse the output as a partial result. This is useful for parsers that can parse partial results. Default is False.

Returns:     

Structured output.

Return type:     

_T_

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)