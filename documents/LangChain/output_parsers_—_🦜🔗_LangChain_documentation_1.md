# output_parsers — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/output_parsers.html
**Word Count:** 62
**Links Count:** 104
**Scraped:** 2025-07-21 08:09:49
**Status:** completed

---

# `output_parsers`\#

**OutputParser** classes parse the output of an LLM call.

**Class hierarchy:**               BaseLLMOutputParser --> BaseOutputParser --> <name>OutputParser  # GuardrailsOutputParser     

**Main helpers:**               Serializable, Generation, PromptValue     

**Classes**

[`output_parsers.ernie_functions.JsonKeyOutputFunctionsParser`](https://python.langchain.com/api_reference/community/output_parsers/langchain_community.output_parsers.ernie_functions.JsonKeyOutputFunctionsParser.html#langchain_community.output_parsers.ernie_functions.JsonKeyOutputFunctionsParser "langchain_community.output_parsers.ernie_functions.JsonKeyOutputFunctionsParser") | Parse an output as the element of the Json object.   ---|---   [`output_parsers.ernie_functions.JsonOutputFunctionsParser`](https://python.langchain.com/api_reference/community/output_parsers/langchain_community.output_parsers.ernie_functions.JsonOutputFunctionsParser.html#langchain_community.output_parsers.ernie_functions.JsonOutputFunctionsParser "langchain_community.output_parsers.ernie_functions.JsonOutputFunctionsParser") | Parse an output as the Json object.   [`output_parsers.ernie_functions.OutputFunctionsParser`](https://python.langchain.com/api_reference/community/output_parsers/langchain_community.output_parsers.ernie_functions.OutputFunctionsParser.html#langchain_community.output_parsers.ernie_functions.OutputFunctionsParser "langchain_community.output_parsers.ernie_functions.OutputFunctionsParser") | Parse an output that is one of sets of values.   [`output_parsers.ernie_functions.PydanticAttrOutputFunctionsParser`](https://python.langchain.com/api_reference/community/output_parsers/langchain_community.output_parsers.ernie_functions.PydanticAttrOutputFunctionsParser.html#langchain_community.output_parsers.ernie_functions.PydanticAttrOutputFunctionsParser "langchain_community.output_parsers.ernie_functions.PydanticAttrOutputFunctionsParser") | Parse an output as an attribute of a pydantic object.   [`output_parsers.ernie_functions.PydanticOutputFunctionsParser`](https://python.langchain.com/api_reference/community/output_parsers/langchain_community.output_parsers.ernie_functions.PydanticOutputFunctionsParser.html#langchain_community.output_parsers.ernie_functions.PydanticOutputFunctionsParser "langchain_community.output_parsers.ernie_functions.PydanticOutputFunctionsParser") | Parse an output as a pydantic object.   [`output_parsers.rail_parser.GuardrailsOutputParser`](https://python.langchain.com/api_reference/community/output_parsers/langchain_community.output_parsers.rail_parser.GuardrailsOutputParser.html#langchain_community.output_parsers.rail_parser.GuardrailsOutputParser "langchain_community.output_parsers.rail_parser.GuardrailsOutputParser") | Parse the output of an LLM call using Guardrails.