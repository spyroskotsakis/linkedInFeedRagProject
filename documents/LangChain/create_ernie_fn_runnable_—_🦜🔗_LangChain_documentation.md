# create_ernie_fn_runnable — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chains/langchain_community.chains.ernie_functions.base.create_ernie_fn_runnable.html
**Word Count:** 277
**Links Count:** 169
**Scraped:** 2025-07-21 08:22:10
**Status:** completed

---

# create\_ernie\_fn\_runnable\#

langchain\_community.chains.ernie\_functions.base.create\_ernie\_fn\_runnable\(

    _functions : Sequence\[Dict\[str, Any\] | Type\[BaseModel\] | Callable\]_,     _llm : [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")_,     _prompt : [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")_,     _\*_ ,     _output\_parser : [BaseOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseOutputParser.html#langchain_core.output_parsers.base.BaseOutputParser "langchain_core.output_parsers.base.BaseOutputParser") | [BaseGenerationOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseGenerationOutputParser.html#langchain_core.output_parsers.base.BaseGenerationOutputParser "langchain_core.output_parsers.base.BaseGenerationOutputParser") | None = None_,     _\*\* kwargs: Any_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chains/ernie_functions/base.html#create_ernie_fn_runnable)\#     

Create a runnable sequence that uses Ernie functions.

Parameters:     

  * **functions** \(_Sequence_ _\[__Dict_ _\[__str_ _,__Any_ _\]__|__Type_ _\[__BaseModel_ _\]__|__Callable_ _\]_\) – A sequence of either dictionaries, pydantic.BaseModels classes, or Python functions. If dictionaries are passed in, they are assumed to already be a valid Ernie functions. If only a single function is passed in, then it will be enforced that the model use that function. pydantic.BaseModels and Python functions should have docstrings describing what the function does. For best results, pydantic.BaseModels should have descriptions of the parameters and Python functions should have Google Python style args descriptions in the docstring. Additionally, Python functions should only use primitive types \(str, int, float, bool\) or pydantic.BaseModels for arguments.

  * **llm** \([_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\) – Language model to use, assumed to support the Ernie function-calling API.

  * **prompt** \([_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")\) – BasePromptTemplate to pass to the model.

  * **output\_parser** \([_BaseOutputParser_](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseOutputParser.html#langchain_core.output_parsers.base.BaseOutputParser "langchain_core.output_parsers.base.BaseOutputParser") _|_[_BaseGenerationOutputParser_](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseGenerationOutputParser.html#langchain_core.output_parsers.base.BaseGenerationOutputParser "langchain_core.output_parsers.base.BaseGenerationOutputParser") _|__None_\) – BaseLLMOutputParser to use for parsing model outputs. By default will be inferred from the function types. If pydantic.BaseModels are passed in, then the OutputParser will try to parse outputs using those. Otherwise model outputs will simply be parsed as JSON. If multiple functions are passed in and they are not pydantic.BaseModels, the chain output will include both the name of the function that was returned and the arguments to pass to the function.

  * **kwargs** \(_Any_\)

Returns:     

A runnable sequence that will pass in the given functions to the model when run.

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")

Example               from typing import Optional          from langchain.chains.ernie_functions import create_ernie_fn_chain     from langchain_community.chat_models import ErnieBotChat     from langchain_core.prompts import ChatPromptTemplate     from pydantic import BaseModel, Field               class RecordPerson(BaseModel):         """Record some identifying information about a person."""              name: str = Field(..., description="The person's name")         age: int = Field(..., description="The person's age")         fav_food: Optional[str] = Field(None, description="The person's favorite food")               class RecordDog(BaseModel):         """Record some identifying information about a dog."""              name: str = Field(..., description="The dog's name")         color: str = Field(..., description="The dog's color")         fav_food: Optional[str] = Field(None, description="The dog's favorite food")               llm = ErnieBotChat(model_name="ERNIE-Bot-4")     prompt = ChatPromptTemplate.from_messages(         [             ("user", "Make calls to the relevant function to record the entities in the following input: {input}"),             ("assistant", "OK!"),             ("user", "Tip: Make sure to answer in the correct format"),         ]     )     chain = create_ernie_fn_runnable([RecordPerson, RecordDog], llm, prompt)     chain.invoke({"input": "Harry was a chubby brown beagle who loved chicken"})     # -> RecordDog(name="Harry", color="brown", fav_food="chicken")     

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)