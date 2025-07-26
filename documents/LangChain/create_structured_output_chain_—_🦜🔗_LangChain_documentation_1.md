# create_structured_output_chain — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.base.create_structured_output_chain.html
**Word Count:** 206
**Links Count:** 197
**Scraped:** 2025-07-21 07:48:33
**Status:** completed

---

# create\_structured\_output\_chain\#

langchain.chains.openai\_functions.base.create\_structured\_output\_chain\(

    _output\_schema : dict\[str, Any\] | type\[BaseModel\]_,     _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _prompt : [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")_,     _\*_ ,     _output\_key : str = 'function'_,     _output\_parser : [BaseLLMOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseLLMOutputParser.html#langchain_core.output_parsers.base.BaseLLMOutputParser "langchain_core.output_parsers.base.BaseLLMOutputParser") | None = None_,     _\*\* kwargs: Any_, \) → [LLMChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm.LLMChain.html#langchain.chains.llm.LLMChain "langchain.chains.llm.LLMChain")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/openai_functions/base.html#create_structured_output_chain)\#     

Deprecated since version 0.1.1: Use `with_structured_output()` instead. It will not be removed until langchain==1.0.

\[Legacy\] Create an LLMChain that uses an OpenAI function to get a structured output.

Parameters:     

  * **output\_schema** \(_dict_ _\[__str_ _,__Any_ _\]__|__type_ _\[__BaseModel_ _\]_\) – Either a dictionary or pydantic.BaseModel class. If a dictionary is passed in, it’s assumed to already be a valid JsonSchema. For best results, pydantic.BaseModels should have docstrings describing what the schema represents and descriptions for the parameters.

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – Language model to use, assumed to support the OpenAI function-calling API.

  * **prompt** \([_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")\) – BasePromptTemplate to pass to the model.

  * **output\_key** \(_str_\) – The key to use when returning the output in LLMChain.\_\_call\_\_.

  * **output\_parser** \([_BaseLLMOutputParser_](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseLLMOutputParser.html#langchain_core.output_parsers.base.BaseLLMOutputParser "langchain_core.output_parsers.base.BaseLLMOutputParser") _|__None_\) – BaseLLMOutputParser to use for parsing model outputs. By default will be inferred from the function types. If pydantic.BaseModels are passed in, then the OutputParser will try to parse outputs using those. Otherwise model outputs will simply be parsed as JSON.

  * **kwargs** \(_Any_\)

Returns:     

An LLMChain that will pass the given function to the model.

Return type:     

[_LLMChain_](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm.LLMChain.html#langchain.chains.llm.LLMChain "langchain.chains.llm.LLMChain")

Example               from typing import Optional          from langchain.chains.openai_functions import create_structured_output_chain     from langchain_community.chat_models import ChatOpenAI     from langchain_core.prompts import ChatPromptTemplate          from pydantic import BaseModel, Field          class Dog(BaseModel):         """Identifying information about a dog."""              name: str = Field(..., description="The dog's name")         color: str = Field(..., description="The dog's color")         fav_food: Optional[str] = Field(None, description="The dog's favorite food")          llm = ChatOpenAI(model="gpt-3.5-turbo-0613", temperature=0)     prompt = ChatPromptTemplate.from_messages(         [             ("system", "You are a world class algorithm for extracting information in structured formats."),             ("human", "Use the given format to extract information from the following input: {input}"),             ("human", "Tip: Make sure to answer in the correct format"),         ]     )     chain = create_structured_output_chain(Dog, llm, prompt)     chain.run("Harry was a chubby brown beagle who loved chicken")     # -> Dog(name="Harry", color="brown", fav_food="chicken")     

Examples using create\_structured\_output\_chain

  * [Activeloop Deep Memory](https://python.langchain.com/docs/integrations/retrievers/activeloop/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)