# create_openai_fn_runnable — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chains/langchain.chains.structured_output.base.create_openai_fn_runnable.html
**Word Count:** 445
**Links Count:** 202
**Scraped:** 2025-07-21 07:49:32
**Status:** completed

---

# create\_openai\_fn\_runnable\#

langchain.chains.structured\_output.base.create\_openai\_fn\_runnable\(

    _functions : Sequence\[dict\[str, Any\] | type\[BaseModel\] | Callable\]_,     _llm : [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")_,     _prompt : [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") | None = None_,     _\*_ ,     _enforce\_single\_function\_usage : bool = True_,     _output\_parser : [BaseOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseOutputParser.html#langchain_core.output_parsers.base.BaseOutputParser "langchain_core.output_parsers.base.BaseOutputParser") | [BaseGenerationOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseGenerationOutputParser.html#langchain_core.output_parsers.base.BaseGenerationOutputParser "langchain_core.output_parsers.base.BaseGenerationOutputParser") | None = None_,     _\*\* llm\_kwargs: Any_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/structured_output/base.html#create_openai_fn_runnable)\#     

Deprecated since version 0.1.14: LangChain has introduced a method called with\_structured\_output that is available on ChatModels capable of tool calling. You can read more about the method here: <<https://python.langchain.com/docs/modules/model_io/chat/structured_output/>>. Please follow our extraction use case documentation for more guidelines on how to do information extraction with LLMs. <<https://python.langchain.com/docs/use_cases/extraction/>>. If you notice other issues, please provide feedback here: <[langchain-ai/langchain\#18154](https://github.com/langchain-ai/langchain/discussions/18154)> Use :meth:\`~ from pydantic import BaseModel, Field from langchain\_anthropic import ChatAnthropic

class Joke\(BaseModel\):     

setup: str = Field\(description=”The setup of the joke”\) punchline: str = Field\(description=”The punchline to the joke”\)

\# Or any other chat model that supports tools. \# Please reference to to the documentation of structured\_output \# to see an up to date list of which models support \# with\_structured\_output. model = ChatAnthropic\(model=”claude-3-opus-20240229”, temperature=0\) structured\_llm = model.with\_structured\_output\(Joke\) structured\_llm.invoke\(“Tell me a joke about cats.

> Make sure to call the Joke function.”\)

\` instead. It will not be removed until langchain==1.0.

Create a runnable sequence that uses OpenAI functions.

Parameters:     

  * **functions** \(_Sequence_ _\[__dict_ _\[__str_ _,__Any_ _\]__|__type_ _\[__BaseModel_ _\]__|__Callable_ _\]_\) – A sequence of either dictionaries, pydantic.BaseModels classes, or Python functions. If dictionaries are passed in, they are assumed to already be a valid OpenAI functions. If only a single function is passed in, then it will be enforced that the model use that function. pydantic.BaseModels and Python functions should have docstrings describing what the function does. For best results, pydantic.BaseModels should have descriptions of the parameters and Python functions should have Google Python style args descriptions in the docstring. Additionally, Python functions should only use primitive types \(str, int, float, bool\) or pydantic.BaseModels for arguments.

  * **llm** \([_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\) – Language model to use, assumed to support the OpenAI function-calling API.

  * **prompt** \([_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") _|__None_\) – BasePromptTemplate to pass to the model.

  * **enforce\_single\_function\_usage** \(_bool_\) – only used if a single function is passed in. If True, then the model will be forced to use the given function. If False, then the model will be given the option to use the given function or not.

  * **output\_parser** \([_BaseOutputParser_](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseOutputParser.html#langchain_core.output_parsers.base.BaseOutputParser "langchain_core.output_parsers.base.BaseOutputParser") _|_[_BaseGenerationOutputParser_](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseGenerationOutputParser.html#langchain_core.output_parsers.base.BaseGenerationOutputParser "langchain_core.output_parsers.base.BaseGenerationOutputParser") _|__None_\) – BaseLLMOutputParser to use for parsing model outputs. By default will be inferred from the function types. If pydantic.BaseModels are passed in, then the OutputParser will try to parse outputs using those. Otherwise model outputs will simply be parsed as JSON. If multiple functions are passed in and they are not pydantic.BaseModels, the chain output will include both the name of the function that was returned and the arguments to pass to the function.

  * **\*\*llm\_kwargs** \(_Any_\) – Additional named arguments to pass to the language model.

Returns:     

A runnable sequence that will pass in the given functions to the model when run.

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")

Example               from typing import Optional          from langchain.chains.structured_output import create_openai_fn_runnable     from langchain_openai import ChatOpenAI     from pydantic import BaseModel, Field               class RecordPerson(BaseModel):         '''Record some identifying information about a person.'''              name: str = Field(..., description="The person's name")         age: int = Field(..., description="The person's age")         fav_food: Optional[str] = Field(None, description="The person's favorite food")               class RecordDog(BaseModel):         '''Record some identifying information about a dog.'''              name: str = Field(..., description="The dog's name")         color: str = Field(..., description="The dog's color")         fav_food: Optional[str] = Field(None, description="The dog's favorite food")               llm = ChatOpenAI(model="gpt-4", temperature=0)     structured_llm = create_openai_fn_runnable([RecordPerson, RecordDog], llm)     structured_llm.invoke("Harry was a chubby brown beagle who loved chicken)     # -> RecordDog(name="Harry", color="brown", fav_food="chicken")     

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)