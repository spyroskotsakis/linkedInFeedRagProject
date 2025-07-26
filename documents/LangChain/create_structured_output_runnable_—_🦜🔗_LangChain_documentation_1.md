# create_structured_output_runnable — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chains/langchain.chains.structured_output.base.create_structured_output_runnable.html
**Word Count:** 632
**Links Count:** 202
**Scraped:** 2025-07-21 07:51:08
**Status:** completed

---

# create\_structured\_output\_runnable\#

langchain.chains.structured\_output.base.create\_structured\_output\_runnable\(

    _output\_schema : dict\[str, Any\] | type\[BaseModel\]_,     _llm : [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")_,     _prompt : [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") | None = None_,     _\*_ ,     _output\_parser : [BaseOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseOutputParser.html#langchain_core.output_parsers.base.BaseOutputParser "langchain_core.output_parsers.base.BaseOutputParser") | [BaseGenerationOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseGenerationOutputParser.html#langchain_core.output_parsers.base.BaseGenerationOutputParser "langchain_core.output_parsers.base.BaseGenerationOutputParser") | None = None_,     _enforce\_function\_usage : bool = True_,     _return\_single : bool = True_,     _mode : Literal\['openai-functions', 'openai-tools', 'openai-json'\] = 'openai-functions'_,     _\*\* kwargs: Any_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/structured_output/base.html#create_structured_output_runnable)\#     

Deprecated since version 0.1.17: LangChain has introduced a method called with\_structured\_output that is available on ChatModels capable of tool calling. You can read more about the method here: <<https://python.langchain.com/docs/modules/model_io/chat/structured_output/>>.Please follow our extraction use case documentation for more guidelines on how to do information extraction with LLMs. <<https://python.langchain.com/docs/use_cases/extraction/>>. If you notice other issues, please provide feedback here: <[langchain-ai/langchain\#18154](https://github.com/langchain-ai/langchain/discussions/18154)> Use :meth:\`~ from pydantic import BaseModel, Field from langchain\_anthropic import ChatAnthropic

class Joke\(BaseModel\):     

setup: str = Field\(description=”The setup of the joke”\) punchline: str = Field\(description=”The punchline to the joke”\)

\# Or any other chat model that supports tools. \# Please reference to to the documentation of structured\_output \# to see an up to date list of which models support \# with\_structured\_output. model = ChatAnthropic\(model=”claude-3-opus-20240229”, temperature=0\) structured\_llm = model.with\_structured\_output\(Joke\) structured\_llm.invoke\(“Tell me a joke about cats.

> Make sure to call the Joke function.”\)

\` instead. It will not be removed until langchain==1.0.

Create a runnable for extracting structured outputs.

Parameters:     

  * **output\_schema** \(_dict_ _\[__str_ _,__Any_ _\]__|__type_ _\[__BaseModel_ _\]_\) – Either a dictionary or pydantic.BaseModel class. If a dictionary is passed in, it’s assumed to already be a valid JsonSchema. For best results, pydantic.BaseModels should have docstrings describing what the schema represents and descriptions for the parameters.

  * **llm** \([_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\) – Language model to use. Assumed to support the OpenAI function-calling API if mode is ‘openai-function’. Assumed to support OpenAI response\_format parameter if mode is ‘openai-json’.

  * **prompt** \([_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") _|__None_\) – BasePromptTemplate to pass to the model. If mode is ‘openai-json’ and prompt has input variable ‘output\_schema’ then the given output\_schema will be converted to a JsonSchema and inserted in the prompt.

  * **output\_parser** \([_BaseOutputParser_](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseOutputParser.html#langchain_core.output_parsers.base.BaseOutputParser "langchain_core.output_parsers.base.BaseOutputParser") _|_[_BaseGenerationOutputParser_](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseGenerationOutputParser.html#langchain_core.output_parsers.base.BaseGenerationOutputParser "langchain_core.output_parsers.base.BaseGenerationOutputParser") _|__None_\) – Output parser to use for parsing model outputs. By default will be inferred from the function types. If pydantic.BaseModel is passed in, then the OutputParser will try to parse outputs using the pydantic class. Otherwise model outputs will be parsed as JSON.

  * **mode** \(_Literal_ _\[__'openai-functions'__,__'openai-tools'__,__'openai-json'__\]_\) – How structured outputs are extracted from the model. If ‘openai-functions’ then OpenAI function calling is used with the deprecated ‘functions’, ‘function\_call’ schema. If ‘openai-tools’ then OpenAI function calling with the latest ‘tools’, ‘tool\_choice’ schema is used. This is recommended over ‘openai-functions’. If ‘openai-json’ then OpenAI model with response\_format set to JSON is used.

  * **enforce\_function\_usage** \(_bool_\) – Only applies when mode is ‘openai-tools’ or ‘openai-functions’. If True, then the model will be forced to use the given output schema. If False, then the model can elect whether to use the output schema.

  * **return\_single** \(_bool_\) – Only applies when mode is ‘openai-tools’. Whether to a list of structured outputs or a single one. If True and model does not return any structured outputs then chain output is None. If False and model does not return any structured outputs then chain output is an empty list.

  * **kwargs** \(_Any_\) – Additional named arguments.

Returns:     

A runnable sequence that will return a structured output\(s\) matching the given     

output\_schema.

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")

OpenAI tools example with Pydantic schema \(mode=’openai-tools’\):                    from typing import Optional          from langchain.chains import create_structured_output_runnable     from langchain_openai import ChatOpenAI     from pydantic import BaseModel, Field               class RecordDog(BaseModel):         '''Record some identifying information about a dog.'''              name: str = Field(..., description="The dog's name")         color: str = Field(..., description="The dog's color")         fav_food: Optional[str] = Field(None, description="The dog's favorite food")          llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)     prompt = ChatPromptTemplate.from_messages(         [             ("system", "You are an extraction algorithm. Please extract every possible instance"),             ('human', '{input}')         ]     )     structured_llm = create_structured_output_runnable(         RecordDog,         llm,         mode="openai-tools",         enforce_function_usage=True,         return_single=True     )     structured_llm.invoke({"input": "Harry was a chubby brown beagle who loved chicken"})     # -> RecordDog(name="Harry", color="brown", fav_food="chicken")     

OpenAI tools example with dict schema \(mode=”openai-tools”\):                    from typing import Optional          from langchain.chains import create_structured_output_runnable     from langchain_openai import ChatOpenAI               dog_schema = {         "type": "function",         "function": {             "name": "record_dog",             "description": "Record some identifying information about a dog.",             "parameters": {                 "type": "object",                 "properties": {                     "name": {                         "description": "The dog's name",                         "type": "string"                     },                     "color": {                         "description": "The dog's color",                         "type": "string"                     },                     "fav_food": {                         "description": "The dog's favorite food",                         "type": "string"                     }                 },                 "required": ["name", "color"]             }         }     }               llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)     structured_llm = create_structured_output_runnable(         dog_schema,         llm,         mode="openai-tools",         enforce_function_usage=True,         return_single=True     )     structured_llm.invoke("Harry was a chubby brown beagle who loved chicken")     # -> {'name': 'Harry', 'color': 'brown', 'fav_food': 'chicken'}     

OpenAI functions example \(mode=”openai-functions”\):                    from typing import Optional          from langchain.chains import create_structured_output_runnable     from langchain_openai import ChatOpenAI     from pydantic import BaseModel, Field          class Dog(BaseModel):         '''Identifying information about a dog.'''              name: str = Field(..., description="The dog's name")         color: str = Field(..., description="The dog's color")         fav_food: Optional[str] = Field(None, description="The dog's favorite food")          llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)     structured_llm = create_structured_output_runnable(Dog, llm, mode="openai-functions")     structured_llm.invoke("Harry was a chubby brown beagle who loved chicken")     # -> Dog(name="Harry", color="brown", fav_food="chicken")     

OpenAI functions with prompt example:                    from typing import Optional          from langchain.chains import create_structured_output_runnable     from langchain_openai import ChatOpenAI     from langchain_core.prompts import ChatPromptTemplate     from pydantic import BaseModel, Field          class Dog(BaseModel):         '''Identifying information about a dog.'''              name: str = Field(..., description="The dog's name")         color: str = Field(..., description="The dog's color")         fav_food: Optional[str] = Field(None, description="The dog's favorite food")          llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)     structured_llm = create_structured_output_runnable(Dog, llm, mode="openai-functions")     system = '''Extract information about any dogs mentioned in the user input.'''     prompt = ChatPromptTemplate.from_messages(         [("system", system), ("human", "{input}"),]     )     chain = prompt | structured_llm     chain.invoke({"input": "Harry was a chubby brown beagle who loved chicken"})     # -> Dog(name="Harry", color="brown", fav_food="chicken")     

OpenAI json response format example \(mode=”openai-json”\):                    from typing import Optional          from langchain.chains import create_structured_output_runnable     from langchain_openai import ChatOpenAI     from langchain_core.prompts import ChatPromptTemplate     from pydantic import BaseModel, Field          class Dog(BaseModel):         '''Identifying information about a dog.'''              name: str = Field(..., description="The dog's name")         color: str = Field(..., description="The dog's color")         fav_food: Optional[str] = Field(None, description="The dog's favorite food")          llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)     structured_llm = create_structured_output_runnable(Dog, llm, mode="openai-json")     system = '''You are a world class assistant for extracting information in structured JSON formats.     Extract a valid JSON blob from the user input that matches the following JSON Schema:          {output_schema}'''     prompt = ChatPromptTemplate.from_messages(         [("system", system), ("human", "{input}"),]     )     chain = prompt | structured_llm     chain.invoke({"input": "Harry was a chubby brown beagle who loved chicken"})     

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)