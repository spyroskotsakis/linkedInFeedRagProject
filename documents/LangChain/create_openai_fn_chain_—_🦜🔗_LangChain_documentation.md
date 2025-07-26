# create_openai_fn_chain — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.base.create_openai_fn_chain.html
**Word Count:** 346
**Links Count:** 196
**Scraped:** 2025-07-21 07:48:06
**Status:** completed

---

# create\_openai\_fn\_chain\#

langchain.chains.openai\_functions.base.create\_openai\_fn\_chain\(

    _functions : Sequence\[dict\[str, Any\] | type\[BaseModel\] | Callable\]_,     _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _prompt : [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")_,     _\*_ ,     _enforce\_single\_function\_usage : bool = True_,     _output\_key : str = 'function'_,     _output\_parser : [BaseLLMOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseLLMOutputParser.html#langchain_core.output_parsers.base.BaseLLMOutputParser "langchain_core.output_parsers.base.BaseLLMOutputParser") | None = None_,     _\*\* kwargs: Any_, \) → [LLMChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm.LLMChain.html#langchain.chains.llm.LLMChain "langchain.chains.llm.LLMChain")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/openai_functions/base.html#create_openai_fn_chain)\#     

Deprecated since version 0.1.1: Use `create_openai_fn_runnable()` instead. It will not be removed until langchain==1.0.

\[Legacy\] Create an LLM chain that uses OpenAI functions.

Parameters:     

  * **functions** \(_Sequence_ _\[__dict_ _\[__str_ _,__Any_ _\]__|__type_ _\[__BaseModel_ _\]__|__Callable_ _\]_\) – A sequence of either dictionaries, pydantic.BaseModels classes, or Python functions. If dictionaries are passed in, they are assumed to already be a valid OpenAI functions. If only a single function is passed in, then it will be enforced that the model use that function. pydantic.BaseModels and Python functions should have docstrings describing what the function does. For best results, pydantic.BaseModels should have descriptions of the parameters and Python functions should have Google Python style args descriptions in the docstring. Additionally, Python functions should only use primitive types \(str, int, float, bool\) or pydantic.BaseModels for arguments.

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – Language model to use, assumed to support the OpenAI function-calling API.

  * **prompt** \([_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")\) – BasePromptTemplate to pass to the model.

  * **enforce\_single\_function\_usage** \(_bool_\) – only used if a single function is passed in. If True, then the model will be forced to use the given function. If False, then the model will be given the option to use the given function or not.

  * **output\_key** \(_str_\) – The key to use when returning the output in LLMChain.\_\_call\_\_.

  * **output\_parser** \([_BaseLLMOutputParser_](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseLLMOutputParser.html#langchain_core.output_parsers.base.BaseLLMOutputParser "langchain_core.output_parsers.base.BaseLLMOutputParser") _|__None_\) – BaseLLMOutputParser to use for parsing model outputs. By default will be inferred from the function types. If pydantic.BaseModels are passed in, then the OutputParser will try to parse outputs using those. Otherwise model outputs will simply be parsed as JSON. If multiple functions are passed in and they are not pydantic.BaseModels, the chain output will include both the name of the function that was returned and the arguments to pass to the function.

  * **kwargs** \(_Any_\)

Returns:     

An LLMChain that will pass in the given functions to the model when run.

Return type:     

[_LLMChain_](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm.LLMChain.html#langchain.chains.llm.LLMChain "langchain.chains.llm.LLMChain")

Example               from typing import Optional          from langchain.chains.openai_functions import create_openai_fn_chain     from langchain_community.chat_models import ChatOpenAI     from langchain_core.prompts import ChatPromptTemplate          from pydantic import BaseModel, Field               class RecordPerson(BaseModel):         """Record some identifying information about a person."""              name: str = Field(..., description="The person's name")         age: int = Field(..., description="The person's age")         fav_food: Optional[str] = Field(None, description="The person's favorite food")               class RecordDog(BaseModel):         """Record some identifying information about a dog."""              name: str = Field(..., description="The dog's name")         color: str = Field(..., description="The dog's color")         fav_food: Optional[str] = Field(None, description="The dog's favorite food")               llm = ChatOpenAI(model="gpt-4", temperature=0)     prompt = ChatPromptTemplate.from_messages(         [             ("system", "You are a world class algorithm for recording entities."),             ("human", "Make calls to the relevant function to record the entities in the following input: {input}"),             ("human", "Tip: Make sure to answer in the correct format"),         ]     )     chain = create_openai_fn_chain([RecordPerson, RecordDog], llm, prompt)     chain.run("Harry was a chubby brown beagle who loved chicken")     # -> RecordDog(name="Harry", color="brown", fav_food="chicken")     

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)