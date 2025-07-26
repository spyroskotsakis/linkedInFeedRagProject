# convert_pydantic_to_openai_function — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.convert_pydantic_to_openai_function.html
**Word Count:** 86
**Links Count:** 169
**Scraped:** 2025-07-21 07:53:06
**Status:** completed

---

# convert\_pydantic\_to\_openai\_function\#

langchain\_core.utils.function\_calling.convert\_pydantic\_to\_openai\_function\(

    _model : type_,     _\*_ ,     _name : str | None = None_,     _description : str | None = None_,     _rm\_titles : bool = True_, \) → [FunctionDescription](https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.FunctionDescription.html#langchain_core.utils.function_calling.FunctionDescription "langchain_core.utils.function_calling.FunctionDescription")\#     

Deprecated since version 0.1.16: Use [`convert_to_openai_function()`](https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.convert_to_openai_function.html#langchain_core.utils.function_calling.convert_to_openai_function "langchain_core.utils.function_calling.convert_to_openai_function") instead. It will not be removed until langchain-core==1.0.

Converts a Pydantic model to a function description for the OpenAI API.

Parameters:     

  * **model** \(_type_\) – The Pydantic model to convert.

  * **name** \(_str_ _|__None_\) – The name of the function. If not provided, the title of the schema will be used.

  * **description** \(_str_ _|__None_\) – The description of the function. If not provided, the description of the schema will be used.

  * **rm\_titles** \(_bool_\) – Whether to remove titles from the schema. Defaults to True.

Returns:     

The function description.

Return type:     

[_FunctionDescription_](https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.FunctionDescription.html#langchain_core.utils.function_calling.FunctionDescription "langchain_core.utils.function_calling.FunctionDescription")

Examples using convert\_pydantic\_to\_openai\_function

  * [LangSmith LLM Runs](https://python.langchain.com/docs/integrations/chat_loaders/langsmith_llm_runs/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)