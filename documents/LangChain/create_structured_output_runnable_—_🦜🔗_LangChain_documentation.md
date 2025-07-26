# create_structured_output_runnable — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chains/langchain_community.chains.ernie_functions.base.create_structured_output_runnable.html
**Word Count:** 172
**Links Count:** 169
**Scraped:** 2025-07-21 08:19:13
**Status:** completed

---

# create\_structured\_output\_runnable\#

langchain\_community.chains.ernie\_functions.base.create\_structured\_output\_runnable\(

    _output\_schema : Dict\[str, Any\] | Type\[BaseModel\]_,     _llm : [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")_,     _prompt : [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")_,     _\*_ ,     _output\_parser : [BaseOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseOutputParser.html#langchain_core.output_parsers.base.BaseOutputParser "langchain_core.output_parsers.base.BaseOutputParser") | [BaseGenerationOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseGenerationOutputParser.html#langchain_core.output_parsers.base.BaseGenerationOutputParser "langchain_core.output_parsers.base.BaseGenerationOutputParser") | None = None_,     _\*\* kwargs: Any_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chains/ernie_functions/base.html#create_structured_output_runnable)\#     

Create a runnable that uses an Ernie function to get a structured output.

Parameters:     

  * **output\_schema** \(_Dict_ _\[__str_ _,__Any_ _\]__|__Type_ _\[__BaseModel_ _\]_\) – Either a dictionary or pydantic.BaseModel class. If a dictionary is passed in, it’s assumed to already be a valid JsonSchema. For best results, pydantic.BaseModels should have docstrings describing what the schema represents and descriptions for the parameters.

  * **llm** \([_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\) – Language model to use, assumed to support the Ernie function-calling API.

  * **prompt** \([_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")\) – BasePromptTemplate to pass to the model.

  * **output\_parser** \([_BaseOutputParser_](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseOutputParser.html#langchain_core.output_parsers.base.BaseOutputParser "langchain_core.output_parsers.base.BaseOutputParser") _|_[_BaseGenerationOutputParser_](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseGenerationOutputParser.html#langchain_core.output_parsers.base.BaseGenerationOutputParser "langchain_core.output_parsers.base.BaseGenerationOutputParser") _|__None_\) – BaseLLMOutputParser to use for parsing model outputs. By default will be inferred from the function types. If pydantic.BaseModels are passed in, then the OutputParser will try to parse outputs using those. Otherwise model outputs will simply be parsed as JSON.

  * **kwargs** \(_Any_\)

Returns:     

A runnable sequence that will pass the given function to the model when run.

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")

Example               from typing import Optional          from langchain.chains.ernie_functions import create_structured_output_chain     from langchain_community.chat_models import ErnieBotChat     from langchain_core.prompts import ChatPromptTemplate     from pydantic import BaseModel, Field          class Dog(BaseModel):         """Identifying information about a dog."""              name: str = Field(..., description="The dog's name")         color: str = Field(..., description="The dog's color")         fav_food: Optional[str] = Field(None, description="The dog's favorite food")          llm = ErnieBotChat(model_name="ERNIE-Bot-4")     prompt = ChatPromptTemplate.from_messages(         [             ("user", "Use the given format to extract information from the following input: {input}"),             ("assistant", "OK!"),             ("user", "Tip: Make sure to answer in the correct format"),         ]     )     chain = create_structured_output_chain(Dog, llm, prompt)     chain.invoke({"input": "Harry was a chubby brown beagle who loved chicken"})     # -> Dog(name="Harry", color="brown", fav_food="chicken")     

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)