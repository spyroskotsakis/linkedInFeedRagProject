# get_output_parser — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/google_vertexai/chains/langchain_google_vertexai.chains.get_output_parser.html
**Word Count:** 46
**Links Count:** 86
**Scraped:** 2025-07-21 08:27:19
**Status:** completed

---

# get\_output\_parser\#

langchain\_google\_vertexai.chains.get\_output\_parser\(

    _functions : Sequence\[Type\[BaseModel\]\]_, \) → [BaseOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseOutputParser.html#langchain_core.output_parsers.base.BaseOutputParser "langchain_core.output_parsers.base.BaseOutputParser") | [BaseGenerationOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseGenerationOutputParser.html#langchain_core.output_parsers.base.BaseGenerationOutputParser "langchain_core.output_parsers.base.BaseGenerationOutputParser")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_vertexai/chains.html#get_output_parser)\#     

Get the appropriate function output parser given the user functions.

Parameters:     

**functions** \(_Sequence_ _\[__Type_ _\[__BaseModel_ _\]__\]_\) – Sequence where element is a dictionary, a `pydantic.BaseModel` class, or a Python function. If a dictionary is passed in, it is assumed to already be a valid OpenAI function.

Returns:     

A PydanticFunctionsOutputParser

Return type:     

[_BaseOutputParser_](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseOutputParser.html#langchain_core.output_parsers.base.BaseOutputParser "langchain_core.output_parsers.base.BaseOutputParser") | [_BaseGenerationOutputParser_](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseGenerationOutputParser.html#langchain_core.output_parsers.base.BaseGenerationOutputParser "langchain_core.output_parsers.base.BaseGenerationOutputParser")

__On this page