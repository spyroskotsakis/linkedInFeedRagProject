# Runnable — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html
**Word Count:** 3203
**Links Count:** 421
**Scraped:** 2025-07-21 07:51:39
**Status:** completed

---

# Runnable\#

_class _langchain\_core.runnables.base.Runnable[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#Runnable)\#     

A unit of work that can be invoked, batched, streamed, transformed and composed.

## Key Methods\#

  * **invoke/ainvoke** : Transforms a single input into an output.

  * **batch/abatch** : Efficiently transforms multiple inputs into outputs.

  * **stream/astream** : Streams output from a single input as it’s produced.

  * **astream\_log** : Streams output and selected intermediate results from an input.

Built-in optimizations:

  * **Batch** : By default, batch runs invoke\(\) in parallel using a thread pool executor. Override to optimize batching.

  * **Async** : Methods with “a” suffix are asynchronous. By default, they execute the sync counterpart using asyncio’s thread pool. Override for native async.

All methods accept an optional config argument, which can be used to configure execution, add tags and metadata for tracing and debugging etc.

Runnables expose schematic information about their input, output and config via the input\_schema property, the output\_schema property and config\_schema method.

## LCEL and Composition\#

The LangChain Expression Language \(LCEL\) is a declarative way to compose Runnables into chains. Any chain constructed this way will automatically have sync, async, batch, and streaming support.

The main composition primitives are RunnableSequence and RunnableParallel.

**RunnableSequence** invokes a series of runnables sequentially, with one Runnable’s output serving as the next’s input. Construct using the | operator or by passing a list of runnables to RunnableSequence.

**RunnableParallel** invokes runnables concurrently, providing the same input to each. Construct it using a dict literal within a sequence or by passing a dict to RunnableParallel.

For example,               from langchain_core.runnables import RunnableLambda          # A RunnableSequence constructed using the `|` operator     sequence = RunnableLambda(lambda x: x + 1) | RunnableLambda(lambda x: x * 2)     sequence.invoke(1) # 4     sequence.batch([1, 2, 3]) # [4, 6, 8]               # A sequence that contains a RunnableParallel constructed using a dict literal     sequence = RunnableLambda(lambda x: x + 1) | {         'mul_2': RunnableLambda(lambda x: x * 2),         'mul_5': RunnableLambda(lambda x: x * 5)     }     sequence.invoke(1) # {'mul_2': 4, 'mul_5': 10}     

## Standard Methods\#

All Runnables expose additional methods that can be used to modify their behavior \(e.g., add a retry policy, add lifecycle listeners, make them configurable, etc.\).

These methods will work on any Runnable, including Runnable chains constructed by composing other Runnables. See the individual methods for details.

For example,               from langchain_core.runnables import RunnableLambda          import random          def add_one(x: int) -> int:         return x + 1               def buggy_double(y: int) -> int:         """Buggy code that will fail 70% of the time"""         if random.random() > 0.3:             print('This code failed, and will probably be retried!')  # noqa: T201             raise ValueError('Triggered buggy code')         return y * 2          sequence = (         RunnableLambda(add_one) |         RunnableLambda(buggy_double).with_retry( # Retry on failure             stop_after_attempt=10,             wait_exponential_jitter=False         )     )          print(sequence.input_schema.model_json_schema()) # Show inferred input schema     print(sequence.output_schema.model_json_schema()) # Show inferred output schema     print(sequence.invoke(2)) # invoke the sequence (note the retry above!!)     

## Debugging and tracing\#

As the chains get longer, it can be useful to be able to see intermediate results to debug and trace the chain.

You can set the global debug flag to True to enable debug output for all chains:

>  >     from langchain_core.globals import set_debug >     set_debug(True) >     

Alternatively, you can pass existing or custom callbacks to any given chain:

>  >     from langchain_core.tracers import ConsoleCallbackHandler >      >     chain.invoke( >         ..., >         config={'callbacks': [ConsoleCallbackHandler()]} >     ) >     

For a UI \(and much more\) checkout LangSmith: <https://docs.smith.langchain.com/>

Attributes

`InputType` | The type of input this Runnable accepts specified as a type annotation.   ---|---   `OutputType` | The type of output this Runnable produces specified as a type annotation.   `config_specs` | List configurable fields for this Runnable.   `input_schema` | The type of input this Runnable accepts specified as a pydantic model.   `output_schema` | The type of output this Runnable produces specified as a pydantic model.      Methods

`abatch`\(inputs\[, config, return\_exceptions\]\) | Default implementation runs ainvoke in parallel using asyncio.gather.   ---|---   `abatch_as_completed`\(\) | Run ainvoke in parallel on a list of inputs.   `ainvoke`\(input\[, config\]\) | Default implementation of ainvoke, calls invoke from a thread.   `as_tool`\(\[args\_schema, name, description, ...\]\) |    `assign`\(\*\*kwargs\) | Assigns new fields to the dict output of this Runnable.   `astream`\(input\[, config\]\) | Default implementation of astream, which calls ainvoke.   `astream_events`\(input\[, config, version, ...\]\) | Generate a stream of events.   `astream_log`\(\) | Stream all output from a Runnable, as reported to the callback system.   `atransform`\(input\[, config\]\) | Default implementation of atransform, which buffers input and calls astream.   `batch`\(inputs\[, config, return\_exceptions\]\) | Default implementation runs invoke in parallel using a thread pool executor.   `batch_as_completed`\(\) | Run invoke in parallel on a list of inputs.   `bind`\(\*\*kwargs\) | Bind arguments to a Runnable, returning a new Runnable.   `config_schema`\(\*\[, include\]\) | The type of config this Runnable accepts specified as a pydantic model.   `get_config_jsonschema`\(\*\[, include\]\) | Get a JSON schema that represents the config of the Runnable.   `get_graph`\(\[config\]\) | Return a graph representation of this Runnable.   `get_input_jsonschema`\(\[config\]\) | Get a JSON schema that represents the input to the Runnable.   `get_input_schema`\(\[config\]\) | Get a pydantic model that can be used to validate input to the Runnable.   `get_name`\(\[suffix, name\]\) | Get the name of the Runnable.   `get_output_jsonschema`\(\[config\]\) | Get a JSON schema that represents the output of the Runnable.   `get_output_schema`\(\[config\]\) | Get a pydantic model that can be used to validate output to the Runnable.   `get_prompts`\(\[config\]\) | Return a list of prompts used by this Runnable.   `invoke`\(input\[, config\]\) | Transform a single input into an output.   `map`\(\) | Return a new Runnable that maps a list of inputs to a list of outputs.   `pick`\(keys\) | Pick keys from the output dict of this Runnable.   `pipe`\(\*others\[, name\]\) | Compose this Runnable with Runnable-like objects to make a RunnableSequence.   `stream`\(input\[, config\]\) | Default implementation of stream, which calls invoke.   `transform`\(input\[, config\]\) | Default implementation of transform, which buffers input and calls astream.   `with_alisteners`\(\*\[, on\_start, on\_end, on\_error\]\) | Bind async lifecycle listeners to a Runnable, returning a new Runnable.   `with_config`\(\[config\]\) | Bind config to a Runnable, returning a new Runnable.   `with_fallbacks`\(fallbacks, \*\[, ...\]\) | Add fallbacks to a Runnable, returning a new Runnable.   `with_listeners`\(\*\[, on\_start, on\_end, on\_error\]\) | Bind lifecycle listeners to a Runnable, returning a new Runnable.   `with_retry`\(\*\[, retry\_if\_exception\_type, ...\]\) | Create a new Runnable that retries the original Runnable on exceptions.   `with_types`\(\*\[, input\_type, output\_type\]\) | Bind input and output types to a Runnable, returning a new Runnable.      _async _abatch\(

    _inputs : list\[Input\]_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | list\[[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")\] | None = None_,     _\*_ ,     _return\_exceptions : bool = False_,     _\*\* kwargs: Any | None_, \) → list\[Output\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#Runnable.abatch)\#     

Default implementation runs ainvoke in parallel using asyncio.gather.

The default implementation of batch works well for IO bound runnables.

Subclasses should override this method if they can batch more efficiently; e.g., if the underlying Runnable uses an API which supports a batch mode.

Parameters:     

  * **inputs** \(_list_ _\[__Input_ _\]_\) – A list of inputs to the Runnable.

  * **config** \([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__list_ _\[_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _\]__|__None_\) – A config to use when invoking the Runnable. The config supports standard keys like ‘tags’, ‘metadata’ for tracing purposes, ‘max\_concurrency’ for controlling how much work to do in parallel, and other keys. Please refer to the RunnableConfig for more details. Defaults to None.

  * **return\_exceptions** \(_bool_\) – Whether to return exceptions instead of raising them. Defaults to False.

  * **kwargs** \(_Any_ _|__None_\) – Additional keyword arguments to pass to the Runnable.

Returns:     

A list of outputs from the Runnable.

Return type:     

list\[_Output_\]

_async _abatch\_as\_completed\(

    _inputs : Sequence\[Input\]_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | Sequence\[[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")\] | None = None_,     _\*_ ,     _return\_exceptions : Literal\[False\] = False_,     _\*\* kwargs: Any | None_, \) → AsyncIterator\[tuple\[int, Output\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#Runnable.abatch_as_completed)\# _async _abatch\_as\_completed\(

    _inputs : Sequence\[Input\]_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | Sequence\[[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")\] | None = None_,     _\*_ ,     _return\_exceptions : Literal\[True\]_,     _\*\* kwargs: Any | None_, \) → AsyncIterator\[tuple\[int, Output | Exception\]\]     

Run ainvoke in parallel on a list of inputs.

Yields results as they complete.

Parameters:     

  * **inputs** – A list of inputs to the Runnable.

  * **config** – A config to use when invoking the Runnable. The config supports standard keys like ‘tags’, ‘metadata’ for tracing purposes, ‘max\_concurrency’ for controlling how much work to do in parallel, and other keys. Please refer to the RunnableConfig for more details. Defaults to None. Defaults to None.

  * **return\_exceptions** – Whether to return exceptions instead of raising them. Defaults to False.

  * **kwargs** – Additional keyword arguments to pass to the Runnable.

Yields:     

A tuple of the index of the input and the output from the Runnable.

_async _ainvoke\(

    _input : Input_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_,     _\*\* kwargs: Any_, \) → Output[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#Runnable.ainvoke)\#     

Default implementation of ainvoke, calls invoke from a thread.

The default implementation allows usage of async code even if the Runnable did not implement a native async version of invoke.

Subclasses should override this method if they can run asynchronously.

Parameters:     

  * **input** \(_Input_\)

  * **config** \([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_Output_

as\_tool\(

    _args\_schema : type\[[BaseModel](https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.models.BaseModel.html#langchain_experimental.video_captioning.models.BaseModel "langchain_experimental.video_captioning.models.BaseModel")\] | None = None_,     _\*_ ,     _name : str | None = None_,     _description : str | None = None_,     _arg\_types : dict\[str, type\] | None = None_, \) → [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#Runnable.as_tool)\#     

Beta

This API is in beta and may change in the future.

Create a BaseTool from a Runnable.

`as_tool` will instantiate a BaseTool with a name, description, and `args_schema` from a Runnable. Where possible, schemas are inferred from `runnable.get_input_schema`. Alternatively \(e.g., if the Runnable takes a dict as input and the specific dict keys are not typed\), the schema can be specified directly with `args_schema`. You can also pass `arg_types` to just specify the required arguments and their types.

Parameters:     

  * **args\_schema** \(_Optional_ _\[__type_ _\[_[_BaseModel_](https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.models.BaseModel.html#langchain_experimental.video_captioning.models.BaseModel "langchain_experimental.video_captioning.models.BaseModel") _\]__\]_\) – The schema for the tool. Defaults to None.

  * **name** \(_Optional_ _\[__str_ _\]_\) – The name of the tool. Defaults to None.

  * **description** \(_Optional_ _\[__str_ _\]_\) – The description of the tool. Defaults to None.

  * **arg\_types** \(_Optional_ _\[__dict_ _\[__str_ _,__type_ _\]__\]_\) – A dictionary of argument names to types. Defaults to None.

Returns:     

A BaseTool instance.

Return type:     

[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")

Typed dict input:               from typing_extensions import TypedDict     from langchain_core.runnables import RunnableLambda          class Args(TypedDict):         a: int         b: list[int]          def f(x: Args) -> str:         return str(x["a"] * max(x["b"]))          runnable = RunnableLambda(f)     as_tool = runnable.as_tool()     as_tool.invoke({"a": 3, "b": [1, 2]})     

`dict` input, specifying schema via `args_schema`:               from typing import Any     from pydantic import BaseModel, Field     from langchain_core.runnables import RunnableLambda          def f(x: dict[str, Any]) -> str:         return str(x["a"] * max(x["b"]))          class FSchema(BaseModel):         """Apply a function to an integer and list of integers."""              a: int = Field(..., description="Integer")         b: list[int] = Field(..., description="List of ints")          runnable = RunnableLambda(f)     as_tool = runnable.as_tool(FSchema)     as_tool.invoke({"a": 3, "b": [1, 2]})     

`dict` input, specifying schema via `arg_types`:               from typing import Any     from langchain_core.runnables import RunnableLambda          def f(x: dict[str, Any]) -> str:         return str(x["a"] * max(x["b"]))          runnable = RunnableLambda(f)     as_tool = runnable.as_tool(arg_types={"a": int, "b": list[int]})     as_tool.invoke({"a": 3, "b": [1, 2]})     

String input:               from langchain_core.runnables import RunnableLambda          def f(x: str) -> str:         return x + "a"          def g(x: str) -> str:         return x + "z"          runnable = RunnableLambda(f) | g     as_tool = runnable.as_tool()     as_tool.invoke("b")     

Added in version 0.2.14.

assign\(

    _\*\* kwargs: Runnable\[dict\[str, Any\], Any\] | Callable\[\[dict\[str, Any\]\], Any\] | Mapping\[str, Runnable\[dict\[str, Any\], Any\] | Callable\[\[dict\[str, Any\]\], Any\]\]_, \) → [RunnableSerializable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableSerializable.html#langchain_core.runnables.base.RunnableSerializable "langchain_core.runnables.base.RunnableSerializable")\[Any, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#Runnable.assign)\#     

Assigns new fields to the dict output of this Runnable.

Returns a new Runnable.               from langchain_community.llms.fake import FakeStreamingListLLM     from langchain_core.output_parsers import StrOutputParser     from langchain_core.prompts import SystemMessagePromptTemplate     from langchain_core.runnables import Runnable     from operator import itemgetter          prompt = (         SystemMessagePromptTemplate.from_template("You are a nice assistant.")         + "{question}"     )     llm = FakeStreamingListLLM(responses=["foo-lish"])          chain: Runnable = prompt | llm | {"str": StrOutputParser()}          chain_with_assign = chain.assign(hello=itemgetter("str") | llm)          print(chain_with_assign.input_schema.model_json_schema())     # {'title': 'PromptInput', 'type': 'object', 'properties':     {'question': {'title': 'Question', 'type': 'string'}}}     print(chain_with_assign.output_schema.model_json_schema())     # {'title': 'RunnableSequenceOutput', 'type': 'object', 'properties':     {'str': {'title': 'Str',     'type': 'string'}, 'hello': {'title': 'Hello', 'type': 'string'}}}     

Parameters:     

**kwargs** \(_Runnable_ _\[__dict_ _\[__str_ _,__Any_ _\]__,__Any_ _\]__|__Callable_ _\[__\[__dict_ _\[__str_ _,__Any_ _\]__\]__,__Any_ _\]__|__Mapping_ _\[__str_ _,__Runnable_ _\[__dict_ _\[__str_ _,__Any_ _\]__,__Any_ _\]__|__Callable_ _\[__\[__dict_ _\[__str_ _,__Any_ _\]__\]__,__Any_ _\]__\]_\)

Return type:     

[_RunnableSerializable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableSerializable.html#langchain_core.runnables.base.RunnableSerializable "langchain_core.runnables.base.RunnableSerializable")\[Any, Any\]

_async _astream\(

    _input : Input_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_,     _\*\* kwargs: Any | None_, \) → AsyncIterator\[Output\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#Runnable.astream)\#     

Default implementation of astream, which calls ainvoke.

Subclasses should override this method if they support streaming output.

Parameters:     

  * **input** \(_Input_\) – The input to the Runnable.

  * **config** \([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__None_\) – The config to use for the Runnable. Defaults to None.

  * **kwargs** \(_Any_ _|__None_\) – Additional keyword arguments to pass to the Runnable.

Yields:     

The output of the Runnable.

Return type:     

_AsyncIterator_\[_Output_\]

_async _astream\_events\(

    _input : Any_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_,     _\*_ ,     _version : Literal\['v1', 'v2'\] = 'v2'_,     _include\_names : Sequence\[str\] | None = None_,     _include\_types : Sequence\[str\] | None = None_,     _include\_tags : Sequence\[str\] | None = None_,     _exclude\_names : Sequence\[str\] | None = None_,     _exclude\_types : Sequence\[str\] | None = None_,     _exclude\_tags : Sequence\[str\] | None = None_,     _\*\* kwargs: Any_, \) → AsyncIterator\[StreamEvent\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#Runnable.astream_events)\#     

Generate a stream of events.

Use to create an iterator over StreamEvents that provide real-time information about the progress of the Runnable, including StreamEvents from intermediate results.

A StreamEvent is a dictionary with the following schema:

  * `event`: **str** \- Event names are of the format: on\_\[runnable\_type\]\_\(start|stream|end\).

  * `name`: **str** \- The name of the Runnable that generated the event.

  * `run_id`: **str** \- randomly generated ID associated with the given execution of the Runnable that emitted the event. A child Runnable that gets invoked as part of the execution of a parent Runnable is assigned its own unique ID.

  * `parent_ids`: **list\[str\]** \- The IDs of the parent runnables that generated the event. The root Runnable will have an empty list. The order of the parent IDs is from the root to the immediate parent. Only available for v2 version of the API. The v1 version of the API will return an empty list.

  * `tags`: **Optional\[list\[str\]\]** \- The tags of the Runnable that generated the event.

  * `metadata`: **Optional\[dict\[str, Any\]\]** \- The metadata of the Runnable that generated the event.

  * `data`: **dict\[str, Any\]**

Below is a table that illustrates some events that might be emitted by various chains. Metadata fields have been omitted from the table for brevity. Chain definitions have been included after the table.

Note

This reference table is for the V2 version of the schema.

event | name | chunk | input | output   ---|---|---|---|---   on\_chat\_model\_start | \[model name\] |  | \{“messages”: \[\[SystemMessage, HumanMessage\]\]\} |    on\_chat\_model\_stream | \[model name\] | AIMessageChunk\(content=”hello”\) |  |    on\_chat\_model\_end | \[model name\] |  | \{“messages”: \[\[SystemMessage, HumanMessage\]\]\} | AIMessageChunk\(content=”hello world”\)   on\_llm\_start | \[model name\] |  | \{‘input’: ‘hello’\} |    on\_llm\_stream | \[model name\] | ‘Hello’ |  |    on\_llm\_end | \[model name\] |  | ‘Hello human\!’ |    on\_chain\_start | format\_docs |  |  |    on\_chain\_stream | format\_docs | “hello world\!, goodbye world\!” |  |    on\_chain\_end | format\_docs |  | \[Document\(…\)\] | “hello world\!, goodbye world\!”   on\_tool\_start | some\_tool |  | \{“x”: 1, “y”: “2”\} |    on\_tool\_end | some\_tool |  |  | \{“x”: 1, “y”: “2”\}   on\_retriever\_start | \[retriever name\] |  | \{“query”: “hello”\} |    on\_retriever\_end | \[retriever name\] |  | \{“query”: “hello”\} | \[Document\(…\), ..\]   on\_prompt\_start | \[template\_name\] |  | \{“question”: “hello”\} |    on\_prompt\_end | \[template\_name\] |  | \{“question”: “hello”\} | ChatPromptValue\(messages: \[SystemMessage, …\]\)      In addition to the standard events, users can also dispatch custom events \(see example below\).

Custom events will be only be surfaced with in the v2 version of the API\!

A custom event has following format:

Attribute | Type | Description   ---|---|---   name | str | A user defined name for the event.   data | Any | The data associated with the event. This can be anything, though we suggest making it JSON serializable.      Here are declarations associated with the standard events shown above:

format\_docs:               def format_docs(docs: list[Document]) -> str:         '''Format the docs.'''         return ", ".join([doc.page_content for doc in docs])          format_docs = RunnableLambda(format_docs)     

some\_tool:               @tool     def some_tool(x: int, y: str) -> dict:         '''Some_tool.'''         return {"x": x, "y": y}     

prompt:               template = ChatPromptTemplate.from_messages(         [("system", "You are Cat Agent 007"), ("human", "{question}")]     ).with_config({"run_name": "my_template", "tags": ["my_template"]})     

Example:               from langchain_core.runnables import RunnableLambda          async def reverse(s: str) -> str:         return s[::-1]          chain = RunnableLambda(func=reverse)          events = [         event async for event in chain.astream_events("hello", version="v2")     ]          # will produce the following events (run_id, and parent_ids     # has been omitted for brevity):     [         {             "data": {"input": "hello"},             "event": "on_chain_start",             "metadata": {},             "name": "reverse",             "tags": [],         },         {             "data": {"chunk": "olleh"},             "event": "on_chain_stream",             "metadata": {},             "name": "reverse",             "tags": [],         },         {             "data": {"output": "olleh"},             "event": "on_chain_end",             "metadata": {},             "name": "reverse",             "tags": [],         },     ]     

Example: Dispatch Custom Event               from langchain_core.callbacks.manager import (         adispatch_custom_event,     )     from langchain_core.runnables import RunnableLambda, RunnableConfig     import asyncio               async def slow_thing(some_input: str, config: RunnableConfig) -> str:         """Do something that takes a long time."""         await asyncio.sleep(1) # Placeholder for some slow operation         await adispatch_custom_event(             "progress_event",             {"message": "Finished step 1 of 3"},             config=config # Must be included for python < 3.10         )         await asyncio.sleep(1) # Placeholder for some slow operation         await adispatch_custom_event(             "progress_event",             {"message": "Finished step 2 of 3"},             config=config # Must be included for python < 3.10         )         await asyncio.sleep(1) # Placeholder for some slow operation         return "Done"          slow_thing = RunnableLambda(slow_thing)          async for event in slow_thing.astream_events("some_input", version="v2"):         print(event)     

Parameters:     

  * **input** \(_Any_\) – The input to the Runnable.

  * **config** \(_Optional_ _\[_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _\]_\) – The config to use for the Runnable.

  * **version** \(_Literal_ _\[__'v1'__,__'v2'__\]_\) – The version of the schema to use either v2 or v1. Users should use v2. v1 is for backwards compatibility and will be deprecated in 0.4.0. No default will be assigned until the API is stabilized. custom events will only be surfaced in v2.

  * **include\_names** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – Only include events from runnables with matching names.

  * **include\_types** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – Only include events from runnables with matching types.

  * **include\_tags** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – Only include events from runnables with matching tags.

  * **exclude\_names** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – Exclude events from runnables with matching names.

  * **exclude\_types** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – Exclude events from runnables with matching types.

  * **exclude\_tags** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – Exclude events from runnables with matching tags.

  * **kwargs** \(_Any_\) – Additional keyword arguments to pass to the Runnable. These will be passed to astream\_log as this implementation of astream\_events is built on top of astream\_log.

Yields:     

An async stream of StreamEvents.

Raises:     

**NotImplementedError** – If the version is not v1 or v2.

Return type:     

AsyncIterator\[StreamEvent\]

_async _astream\_log\(

    _input : Any_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_,     _\*_ ,     _diff : Literal\[True\] = True_,     _with\_streamed\_output\_list : bool = True_,     _include\_names : Sequence\[str\] | None = None_,     _include\_types : Sequence\[str\] | None = None_,     _include\_tags : Sequence\[str\] | None = None_,     _exclude\_names : Sequence\[str\] | None = None_,     _exclude\_types : Sequence\[str\] | None = None_,     _exclude\_tags : Sequence\[str\] | None = None_,     _\*\* kwargs: Any_, \) → AsyncIterator\[[RunLogPatch](https://python.langchain.com/api_reference/core/tracers/langchain_core.tracers.log_stream.RunLogPatch.html#langchain_core.tracers.log_stream.RunLogPatch "langchain_core.tracers.log_stream.RunLogPatch")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#Runnable.astream_log)\# _async _astream\_log\(

    _input : Any_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_,     _\*_ ,     _diff : Literal\[False\]_,     _with\_streamed\_output\_list : bool = True_,     _include\_names : Sequence\[str\] | None = None_,     _include\_types : Sequence\[str\] | None = None_,     _include\_tags : Sequence\[str\] | None = None_,     _exclude\_names : Sequence\[str\] | None = None_,     _exclude\_types : Sequence\[str\] | None = None_,     _exclude\_tags : Sequence\[str\] | None = None_,     _\*\* kwargs: Any_, \) → AsyncIterator\[[RunLog](https://python.langchain.com/api_reference/core/tracers/langchain_core.tracers.log_stream.RunLog.html#langchain_core.tracers.log_stream.RunLog "langchain_core.tracers.log_stream.RunLog")\]     

Stream all output from a Runnable, as reported to the callback system.

This includes all inner runs of LLMs, Retrievers, Tools, etc.

Output is streamed as Log objects, which include a list of Jsonpatch ops that describe how the state of the run has changed in each step, and the final state of the run.

The Jsonpatch ops can be applied in order to construct state.

Parameters:     

  * **input** – The input to the Runnable.

  * **config** – The config to use for the Runnable.

  * **diff** – Whether to yield diffs between each step or the current state.

  * **with\_streamed\_output\_list** – Whether to yield the streamed\_output list.

  * **include\_names** – Only include logs with these names.

  * **include\_types** – Only include logs with these types.

  * **include\_tags** – Only include logs with these tags.

  * **exclude\_names** – Exclude logs with these names.

  * **exclude\_types** – Exclude logs with these types.

  * **exclude\_tags** – Exclude logs with these tags.

  * **kwargs** – Additional keyword arguments to pass to the Runnable.

Yields:     

A RunLogPatch or RunLog object.

_async _atransform\(

    _input : AsyncIterator\[Input\]_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_,     _\*\* kwargs: Any | None_, \) → AsyncIterator\[Output\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#Runnable.atransform)\#     

Default implementation of atransform, which buffers input and calls astream.

Subclasses should override this method if they can start producing output while input is still being generated.

Parameters:     

  * **input** \(_AsyncIterator_ _\[__Input_ _\]_\) – An async iterator of inputs to the Runnable.

  * **config** \([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__None_\) – The config to use for the Runnable. Defaults to None.

  * **kwargs** \(_Any_ _|__None_\) – Additional keyword arguments to pass to the Runnable.

Yields:     

The output of the Runnable.

Return type:     

_AsyncIterator_\[_Output_\]

batch\(

    _inputs : list\[Input\]_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | list\[[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")\] | None = None_,     _\*_ ,     _return\_exceptions : bool = False_,     _\*\* kwargs: Any | None_, \) → list\[Output\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#Runnable.batch)\#     

Default implementation runs invoke in parallel using a thread pool executor.

The default implementation of batch works well for IO bound runnables.

Subclasses should override this method if they can batch more efficiently; e.g., if the underlying Runnable uses an API which supports a batch mode.

Parameters:     

  * **inputs** \(_list_ _\[__Input_ _\]_\)

  * **config** \([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__list_ _\[_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _\]__|__None_\)

  * **return\_exceptions** \(_bool_\)

  * **kwargs** \(_Any_ _|__None_\)

Return type:     

list\[_Output_\]

batch\_as\_completed\(

    _inputs : Sequence\[Input\]_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | Sequence\[[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")\] | None = None_,     _\*_ ,     _return\_exceptions : Literal\[False\] = False_,     _\*\* kwargs: Any_, \) → Iterator\[tuple\[int, Output\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#Runnable.batch_as_completed)\# batch\_as\_completed\(

    _inputs : Sequence\[Input\]_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | Sequence\[[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")\] | None = None_,     _\*_ ,     _return\_exceptions : Literal\[True\]_,     _\*\* kwargs: Any_, \) → Iterator\[tuple\[int, Output | Exception\]\]     

Run invoke in parallel on a list of inputs.

Yields results as they complete.

bind\(

    _\*\* kwargs: Any_, \) → Runnable\[Input, Output\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#Runnable.bind)\#     

Bind arguments to a Runnable, returning a new Runnable.

Useful when a Runnable in a chain requires an argument that is not in the output of the previous Runnable or included in the user input.

Parameters:     

**kwargs** \(_Any_\) – The arguments to bind to the Runnable.

Returns:     

A new Runnable with the arguments bound.

Return type:     

_Runnable_\[_Input_ , _Output_\]

Example:               from langchain_ollama import ChatOllama     from langchain_core.output_parsers import StrOutputParser          llm = ChatOllama(model='llama2')          # Without bind.     chain = (         llm         | StrOutputParser()     )          chain.invoke("Repeat quoted words exactly: 'One two three four five.'")     # Output is 'One two three four five.'          # With bind.     chain = (         llm.bind(stop=["three"])         | StrOutputParser()     )          chain.invoke("Repeat quoted words exactly: 'One two three four five.'")     # Output is 'One two'     

config\_schema\(

    _\*_ ,     _include : Sequence\[str\] | None = None_, \) → type\[BaseModel\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#Runnable.config_schema)\#     

The type of config this Runnable accepts specified as a pydantic model.

To mark a field as configurable, see the configurable\_fields and configurable\_alternatives methods.

Parameters:     

**include** \(_Sequence_ _\[__str_ _\]__|__None_\) – A list of fields to include in the config schema.

Returns:     

A pydantic model that can be used to validate config.

Return type:     

type\[_BaseModel_\]

get\_config\_jsonschema\(

    _\*_ ,     _include : Sequence\[str\] | None = None_, \) → dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#Runnable.get_config_jsonschema)\#     

Get a JSON schema that represents the config of the Runnable.

Parameters:     

**include** \(_Sequence_ _\[__str_ _\]__|__None_\) – A list of fields to include in the config schema.

Returns:     

A JSON schema that represents the config of the Runnable.

Return type:     

dict\[str, _Any_\]

Added in version 0.3.0.

get\_graph\(

    _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_, \) → [Graph](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Graph.html#langchain_core.runnables.graph.Graph "langchain_core.runnables.graph.Graph")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#Runnable.get_graph)\#     

Return a graph representation of this Runnable.

Parameters:     

**config** \([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__None_\)

Return type:     

[_Graph_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Graph.html#langchain_core.runnables.graph.Graph "langchain_core.runnables.graph.Graph")

get\_input\_jsonschema\(

    _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_, \) → dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#Runnable.get_input_jsonschema)\#     

Get a JSON schema that represents the input to the Runnable.

Parameters:     

**config** \([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__None_\) – A config to use when generating the schema.

Returns:     

A JSON schema that represents the input to the Runnable.

Return type:     

dict\[str, _Any_\]

Example               from langchain_core.runnables import RunnableLambda          def add_one(x: int) -> int:         return x + 1          runnable = RunnableLambda(add_one)          print(runnable.get_input_jsonschema())     

Added in version 0.3.0.

get\_input\_schema\(

    _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_, \) → type\[BaseModel\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#Runnable.get_input_schema)\#     

Get a pydantic model that can be used to validate input to the Runnable.

Runnables that leverage the configurable\_fields and configurable\_alternatives methods will have a dynamic input schema that depends on which configuration the Runnable is invoked with.

This method allows to get an input schema for a specific configuration.

Parameters:     

**config** \([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__None_\) – A config to use when generating the schema.

Returns:     

A pydantic model that can be used to validate input.

Return type:     

type\[_BaseModel_\]

get\_name\(

    _suffix : str | None = None_,     _\*_ ,     _name : str | None = None_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#Runnable.get_name)\#     

Get the name of the Runnable.

Parameters:     

  * **suffix** \(_str_ _|__None_\)

  * **name** \(_str_ _|__None_\)

Return type:     

str

get\_output\_jsonschema\(

    _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_, \) → dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#Runnable.get_output_jsonschema)\#     

Get a JSON schema that represents the output of the Runnable.

Parameters:     

**config** \([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__None_\) – A config to use when generating the schema.

Returns:     

A JSON schema that represents the output of the Runnable.

Return type:     

dict\[str, _Any_\]

Example               from langchain_core.runnables import RunnableLambda          def add_one(x: int) -> int:         return x + 1          runnable = RunnableLambda(add_one)          print(runnable.get_output_jsonschema())     

Added in version 0.3.0.

get\_output\_schema\(

    _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_, \) → type\[BaseModel\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#Runnable.get_output_schema)\#     

Get a pydantic model that can be used to validate output to the Runnable.

Runnables that leverage the configurable\_fields and configurable\_alternatives methods will have a dynamic output schema that depends on which configuration the Runnable is invoked with.

This method allows to get an output schema for a specific configuration.

Parameters:     

**config** \([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__None_\) – A config to use when generating the schema.

Returns:     

A pydantic model that can be used to validate output.

Return type:     

type\[_BaseModel_\]

get\_prompts\(

    _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_, \) → list\[[BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#Runnable.get_prompts)\#     

Return a list of prompts used by this Runnable.

Parameters:     

**config** \(_Optional_ _\[_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _\]_\)

Return type:     

list\[[BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")\]

_abstractmethod _invoke\(

    _input : Input_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_,     _\*\* kwargs: Any_, \) → Output[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#Runnable.invoke)\#     

Transform a single input into an output.

Parameters:     

  * **input** \(_Input_\) – The input to the Runnable.

  * **config** \([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__None_\) – A config to use when invoking the Runnable. The config supports standard keys like ‘tags’, ‘metadata’ for tracing purposes, ‘max\_concurrency’ for controlling how much work to do in parallel, and other keys. Please refer to the RunnableConfig for more details.

  * **kwargs** \(_Any_\)

Returns:     

The output of the Runnable.

Return type:     

_Output_

map\(\) → Runnable\[list\[Input\], list\[Output\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#Runnable.map)\#     

Return a new Runnable that maps a list of inputs to a list of outputs.

Calls invoke\(\) with each input.

Returns:     

A new Runnable that maps a list of inputs to a list of outputs.

Return type:     

_Runnable_\[list\[_Input_\], list\[_Output_\]\]

Example               from langchain_core.runnables import RunnableLambda          def _lambda(x: int) -> int:         return x + 1          runnable = RunnableLambda(_lambda)     print(runnable.map().invoke([1, 2, 3])) # [2, 3, 4]     

pick\(

    _keys : str | list\[str\]_, \) → [RunnableSerializable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableSerializable.html#langchain_core.runnables.base.RunnableSerializable "langchain_core.runnables.base.RunnableSerializable")\[Any, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#Runnable.pick)\#     

Pick keys from the output dict of this Runnable.

Pick single key:                    import json          from langchain_core.runnables import RunnableLambda, RunnableMap          as_str = RunnableLambda(str)     as_json = RunnableLambda(json.loads)     chain = RunnableMap(str=as_str, json=as_json)          chain.invoke("[1, 2, 3]")     # -> {"str": "[1, 2, 3]", "json": [1, 2, 3]}          json_only_chain = chain.pick("json")     json_only_chain.invoke("[1, 2, 3]")     # -> [1, 2, 3]     

Pick list of keys:                    from typing import Any          import json          from langchain_core.runnables import RunnableLambda, RunnableMap          as_str = RunnableLambda(str)     as_json = RunnableLambda(json.loads)     def as_bytes(x: Any) -> bytes:         return bytes(x, "utf-8")          chain = RunnableMap(         str=as_str,         json=as_json,         bytes=RunnableLambda(as_bytes)     )          chain.invoke("[1, 2, 3]")     # -> {"str": "[1, 2, 3]", "json": [1, 2, 3], "bytes": b"[1, 2, 3]"}          json_and_bytes_chain = chain.pick(["json", "bytes"])     json_and_bytes_chain.invoke("[1, 2, 3]")     # -> {"json": [1, 2, 3], "bytes": b"[1, 2, 3]"}     

Parameters:     

**keys** \(_str_ _|__list_ _\[__str_ _\]_\)

Return type:     

[_RunnableSerializable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableSerializable.html#langchain_core.runnables.base.RunnableSerializable "langchain_core.runnables.base.RunnableSerializable")\[Any, Any\]

pipe\(

    _\* others: Runnable\[Any, Other\] | Callable\[\[Any\], Other\]_,     _name : str | None = None_, \) → [RunnableSerializable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableSerializable.html#langchain_core.runnables.base.RunnableSerializable "langchain_core.runnables.base.RunnableSerializable")\[-Input, Other\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#Runnable.pipe)\#     

Compose this Runnable with Runnable-like objects to make a RunnableSequence.

Equivalent to RunnableSequence\(self, \*others\) or self | others\[0\] | …

Example               from langchain_core.runnables import RunnableLambda          def add_one(x: int) -> int:         return x + 1          def mul_two(x: int) -> int:         return x * 2          runnable_1 = RunnableLambda(add_one)     runnable_2 = RunnableLambda(mul_two)     sequence = runnable_1.pipe(runnable_2)     # Or equivalently:     # sequence = runnable_1 | runnable_2     # sequence = RunnableSequence(first=runnable_1, last=runnable_2)     sequence.invoke(1)     await sequence.ainvoke(1)     # -> 4          sequence.batch([1, 2, 3])     await sequence.abatch([1, 2, 3])     # -> [4, 6, 8]     

Parameters:     

  * **others** \(_Runnable_ _\[__Any_ _,__Other_ _\]__|__Callable_ _\[__\[__Any_ _\]__,__Other_ _\]_\)

  * **name** \(_str_ _|__None_\)

Return type:     

[_RunnableSerializable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableSerializable.html#langchain_core.runnables.base.RunnableSerializable "langchain_core.runnables.base.RunnableSerializable")\[-Input, ~Other\]

stream\(

    _input : Input_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_,     _\*\* kwargs: Any | None_, \) → Iterator\[Output\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#Runnable.stream)\#     

Default implementation of stream, which calls invoke.

Subclasses should override this method if they support streaming output.

Parameters:     

  * **input** \(_Input_\) – The input to the Runnable.

  * **config** \([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__None_\) – The config to use for the Runnable. Defaults to None.

  * **kwargs** \(_Any_ _|__None_\) – Additional keyword arguments to pass to the Runnable.

Yields:     

The output of the Runnable.

Return type:     

_Iterator_\[_Output_\]

transform\(

    _input : Iterator\[Input\]_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_,     _\*\* kwargs: Any | None_, \) → Iterator\[Output\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#Runnable.transform)\#     

Default implementation of transform, which buffers input and calls astream.

Subclasses should override this method if they can start producing output while input is still being generated.

Parameters:     

  * **input** \(_Iterator_ _\[__Input_ _\]_\) – An iterator of inputs to the Runnable.

  * **config** \([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__None_\) – The config to use for the Runnable. Defaults to None.

  * **kwargs** \(_Any_ _|__None_\) – Additional keyword arguments to pass to the Runnable.

Yields:     

The output of the Runnable.

Return type:     

_Iterator_\[_Output_\]

with\_alisteners\(

    _\*_ ,     _on\_start : AsyncListener | None = None_,     _on\_end : AsyncListener | None = None_,     _on\_error : AsyncListener | None = None_, \) → Runnable\[Input, Output\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#Runnable.with_alisteners)\#     

Bind async lifecycle listeners to a Runnable, returning a new Runnable.

on\_start: Asynchronously called before the Runnable starts running. on\_end: Asynchronously called after the Runnable finishes running. on\_error: Asynchronously called if the Runnable throws an error.

The Run object contains information about the run, including its id, type, input, output, error, start\_time, end\_time, and any tags or metadata added to the run.

Parameters:     

  * **on\_start** \(_Optional_ _\[__AsyncListener_ _\]_\) – Asynchronously called before the Runnable starts running. Defaults to None.

  * **on\_end** \(_Optional_ _\[__AsyncListener_ _\]_\) – Asynchronously called after the Runnable finishes running. Defaults to None.

  * **on\_error** \(_Optional_ _\[__AsyncListener_ _\]_\) – Asynchronously called if the Runnable throws an error. Defaults to None.

Returns:     

A new Runnable with the listeners bound.

Return type:     

Runnable\[Input, Output\]

Example:               from langchain_core.runnables import RunnableLambda, Runnable     from datetime import datetime, timezone     import time     import asyncio          def format_t(timestamp: float) -> str:         return datetime.fromtimestamp(timestamp, tz=timezone.utc).isoformat()          async def test_runnable(time_to_sleep : int):         print(f"Runnable[{time_to_sleep}s]: starts at {format_t(time.time())}")         await asyncio.sleep(time_to_sleep)         print(f"Runnable[{time_to_sleep}s]: ends at {format_t(time.time())}")          async def fn_start(run_obj : Runnable):         print(f"on start callback starts at {format_t(time.time())}")         await asyncio.sleep(3)         print(f"on start callback ends at {format_t(time.time())}")          async def fn_end(run_obj : Runnable):         print(f"on end callback starts at {format_t(time.time())}")         await asyncio.sleep(2)         print(f"on end callback ends at {format_t(time.time())}")          runnable = RunnableLambda(test_runnable).with_alisteners(         on_start=fn_start,         on_end=fn_end     )     async def concurrent_runs():         await asyncio.gather(runnable.ainvoke(2), runnable.ainvoke(3))          asyncio.run(concurrent_runs())     Result:     on start callback starts at 2025-03-01T07:05:22.875378+00:00     on start callback starts at 2025-03-01T07:05:22.875495+00:00     on start callback ends at 2025-03-01T07:05:25.878862+00:00     on start callback ends at 2025-03-01T07:05:25.878947+00:00     Runnable[2s]: starts at 2025-03-01T07:05:25.879392+00:00     Runnable[3s]: starts at 2025-03-01T07:05:25.879804+00:00     Runnable[2s]: ends at 2025-03-01T07:05:27.881998+00:00     on end callback starts at 2025-03-01T07:05:27.882360+00:00     Runnable[3s]: ends at 2025-03-01T07:05:28.881737+00:00     on end callback starts at 2025-03-01T07:05:28.882428+00:00     on end callback ends at 2025-03-01T07:05:29.883893+00:00     on end callback ends at 2025-03-01T07:05:30.884831+00:00     

with\_config\(

    _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_,     _\*\* kwargs: Any_, \) → Runnable\[Input, Output\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#Runnable.with_config)\#     

Bind config to a Runnable, returning a new Runnable.

Parameters:     

  * **config** \([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__None_\) – The config to bind to the Runnable.

  * **kwargs** \(_Any_\) – Additional keyword arguments to pass to the Runnable.

Returns:     

A new Runnable with the config bound.

Return type:     

_Runnable_\[_Input_ , _Output_\]

with\_fallbacks\(_fallbacks: Sequence\[Runnable\[Input, Output\]\], \*, exceptions\_to\_handle: tuple\[type\[BaseException\], ...\] = \(<class 'Exception'>,\), exception\_key: Optional\[str\] = None_\) → RunnableWithFallbacksT\[Input, Output\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#Runnable.with_fallbacks)\#     

Add fallbacks to a Runnable, returning a new Runnable.

The new Runnable will try the original Runnable, and then each fallback in order, upon failures.

Parameters:     

  * **fallbacks** \(_Sequence_ _\[__Runnable_ _\[__Input_ _,__Output_ _\]__\]_\) – A sequence of runnables to try if the original Runnable fails.

  * **exceptions\_to\_handle** \(_tuple_ _\[__type_ _\[__BaseException_ _\]__,__...__\]_\) – A tuple of exception types to handle. Defaults to \(Exception,\).

  * **exception\_key** \(_Optional_ _\[__str_ _\]_\) – If string is specified then handled exceptions will be passed to fallbacks as part of the input under the specified key. If None, exceptions will not be passed to fallbacks. If used, the base Runnable and its fallbacks must accept a dictionary as input. Defaults to None.

Returns:     

A new Runnable that will try the original Runnable, and then each fallback in order, upon failures.

Return type:     

RunnableWithFallbacksT\[Input, Output\]

Example               from typing import Iterator          from langchain_core.runnables import RunnableGenerator               def _generate_immediate_error(input: Iterator) -> Iterator[str]:         raise ValueError()         yield ""               def _generate(input: Iterator) -> Iterator[str]:         yield from "foo bar"               runnable = RunnableGenerator(_generate_immediate_error).with_fallbacks(         [RunnableGenerator(_generate)]         )     print(''.join(runnable.stream({}))) #foo bar     

Parameters:     

  * **fallbacks** \(_Sequence_ _\[__Runnable_ _\[__Input_ _,__Output_ _\]__\]_\) – A sequence of runnables to try if the original Runnable fails.

  * **exceptions\_to\_handle** \(_tuple_ _\[__type_ _\[__BaseException_ _\]__,__...__\]_\) – A tuple of exception types to handle.

  * **exception\_key** \(_Optional_ _\[__str_ _\]_\) – If string is specified then handled exceptions will be passed to fallbacks as part of the input under the specified key. If None, exceptions will not be passed to fallbacks. If used, the base Runnable and its fallbacks must accept a dictionary as input.

Returns:     

A new Runnable that will try the original Runnable, and then each fallback in order, upon failures.

Return type:     

RunnableWithFallbacksT\[Input, Output\]

with\_listeners\(

    _\*_ ,     _on\_start : Callable\[\[Run\], None\] | Callable\[\[Run, [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")\], None\] | None = None_,     _on\_end : Callable\[\[Run\], None\] | Callable\[\[Run, [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")\], None\] | None = None_,     _on\_error : Callable\[\[Run\], None\] | Callable\[\[Run, [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")\], None\] | None = None_, \) → Runnable\[Input, Output\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#Runnable.with_listeners)\#     

Bind lifecycle listeners to a Runnable, returning a new Runnable.

on\_start: Called before the Runnable starts running, with the Run object. on\_end: Called after the Runnable finishes running, with the Run object. on\_error: Called if the Runnable throws an error, with the Run object.

The Run object contains information about the run, including its id, type, input, output, error, start\_time, end\_time, and any tags or metadata added to the run.

Parameters:     

  * **on\_start** \(_Optional_ _\[__Union_ _\[__Callable_ _\[__\[__Run_ _\]__,__None_ _\]__,__Callable_ _\[__\[__Run_ _,_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _\]__,__None_ _\]__\]__\]_\) – Called before the Runnable starts running. Defaults to None.

  * **on\_end** \(_Optional_ _\[__Union_ _\[__Callable_ _\[__\[__Run_ _\]__,__None_ _\]__,__Callable_ _\[__\[__Run_ _,_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _\]__,__None_ _\]__\]__\]_\) – Called after the Runnable finishes running. Defaults to None.

  * **on\_error** \(_Optional_ _\[__Union_ _\[__Callable_ _\[__\[__Run_ _\]__,__None_ _\]__,__Callable_ _\[__\[__Run_ _,_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _\]__,__None_ _\]__\]__\]_\) – Called if the Runnable throws an error. Defaults to None.

Returns:     

A new Runnable with the listeners bound.

Return type:     

Runnable\[Input, Output\]

Example:               from langchain_core.runnables import RunnableLambda     from langchain_core.tracers.schemas import Run          import time          def test_runnable(time_to_sleep : int):         time.sleep(time_to_sleep)          def fn_start(run_obj: Run):         print("start_time:", run_obj.start_time)          def fn_end(run_obj: Run):         print("end_time:", run_obj.end_time)          chain = RunnableLambda(test_runnable).with_listeners(         on_start=fn_start,         on_end=fn_end     )     chain.invoke(2)     

with\_retry\(_\*, retry\_if\_exception\_type: tuple\[type\[BaseException\], ...\] = \(<class 'Exception'>,\), wait\_exponential\_jitter: bool = True, exponential\_jitter\_params: Optional\[ExponentialJitterParams\] = None, stop\_after\_attempt: int = 3_\) → Runnable\[Input, Output\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#Runnable.with_retry)\#     

Create a new Runnable that retries the original Runnable on exceptions.

Parameters:     

  * **retry\_if\_exception\_type** \(_tuple_ _\[__type_ _\[__BaseException_ _\]__,__...__\]_\) – A tuple of exception types to retry on. Defaults to \(Exception,\).

  * **wait\_exponential\_jitter** \(_bool_\) – Whether to add jitter to the wait time between retries. Defaults to True.

  * **stop\_after\_attempt** \(_int_\) – The maximum number of attempts to make before giving up. Defaults to 3.

  * **exponential\_jitter\_params** \(_Optional_ _\[_[_ExponentialJitterParams_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.retry.ExponentialJitterParams.html#langchain_core.runnables.retry.ExponentialJitterParams "langchain_core.runnables.retry.ExponentialJitterParams") _\]_\) – Parameters for `tenacity.wait_exponential_jitter`. Namely: `initial`, `max`, `exp_base`, and `jitter` \(all float values\).

Returns:     

A new Runnable that retries the original Runnable on exceptions.

Return type:     

Runnable\[Input, Output\]

Example:               from langchain_core.runnables import RunnableLambda          count = 0               def _lambda(x: int) -> None:         global count         count = count + 1         if x == 1:             raise ValueError("x is 1")         else:              pass               runnable = RunnableLambda(_lambda)     try:         runnable.with_retry(             stop_after_attempt=2,             retry_if_exception_type=(ValueError,),         ).invoke(1)     except ValueError:         pass          assert (count == 2)     

with\_types\(

    _\*_ ,     _input\_type : type\[Input\] | None = None_,     _output\_type : type\[Output\] | None = None_, \) → Runnable\[Input, Output\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#Runnable.with_types)\#     

Bind input and output types to a Runnable, returning a new Runnable.

Parameters:     

  * **input\_type** \(_type_ _\[__Input_ _\]__|__None_\) – The input type to bind to the Runnable. Defaults to None.

  * **output\_type** \(_type_ _\[__Output_ _\]__|__None_\) – The output type to bind to the Runnable. Defaults to None.

Returns:     

A new Runnable with the types bound.

Return type:     

_Runnable_\[_Input_ , _Output_\]

Examples using Runnable

  * [How to add a human-in-the-loop for tools](https://python.langchain.com/docs/how_to/tools_human/)

  * [How to create a dynamic \(self-constructing\) chain](https://python.langchain.com/docs/how_to/dynamic_chain/)

  * [How to handle tool errors](https://python.langchain.com/docs/how_to/tools_error/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)