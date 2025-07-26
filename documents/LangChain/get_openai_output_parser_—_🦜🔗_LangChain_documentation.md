# get_openai_output_parser — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chains/langchain.chains.structured_output.base.get_openai_output_parser.html
**Word Count:** 83
**Links Count:** 192
**Scraped:** 2025-07-21 07:51:08
**Status:** completed

---

# get\_openai\_output\_parser\#

langchain.chains.structured\_output.base.get\_openai\_output\_parser\(

    _functions : Sequence\[dict\[str, Any\] | type\[BaseModel\] | Callable\]_, \) → [BaseOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseOutputParser.html#langchain_core.output_parsers.base.BaseOutputParser "langchain_core.output_parsers.base.BaseOutputParser") | [BaseGenerationOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseGenerationOutputParser.html#langchain_core.output_parsers.base.BaseGenerationOutputParser "langchain_core.output_parsers.base.BaseGenerationOutputParser")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/structured_output/base.html#get_openai_output_parser)\#     

Get the appropriate function output parser given the user functions.

Parameters:     

**functions** \(_Sequence_ _\[__dict_ _\[__str_ _,__Any_ _\]__|__type_ _\[__BaseModel_ _\]__|__Callable_ _\]_\) – Sequence where element is a dictionary, a pydantic.BaseModel class, or a Python function. If a dictionary is passed in, it is assumed to already be a valid OpenAI function.

Returns:     

A PydanticOutputFunctionsParser if functions are Pydantic classes, otherwise     

a JsonOutputFunctionsParser. If there’s only one function and it is not a Pydantic class, then the output parser will automatically extract only the function arguments and not the function name.

Return type:     

[_BaseOutputParser_](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseOutputParser.html#langchain_core.output_parsers.base.BaseOutputParser "langchain_core.output_parsers.base.BaseOutputParser") | [_BaseGenerationOutputParser_](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseGenerationOutputParser.html#langchain_core.output_parsers.base.BaseGenerationOutputParser "langchain_core.output_parsers.base.BaseGenerationOutputParser")

__On this page