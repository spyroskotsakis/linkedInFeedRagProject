# ChatNVIDIA — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/nvidia_ai_endpoints/chat_models/langchain_nvidia_ai_endpoints.chat_models.ChatNVIDIA.html
**Word Count:** 3144
**Links Count:** 323
**Scraped:** 2025-07-21 07:57:45
**Status:** completed

---

# ChatNVIDIA\#

_class _langchain\_nvidia\_ai\_endpoints.chat\_models.ChatNVIDIA[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_nvidia_ai_endpoints/chat_models.html#ChatNVIDIA)\#     

Bases: [`BaseChatModel`](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")

NVIDIA chat model.

Example               from langchain_nvidia_ai_endpoints import ChatNVIDIA               model = ChatNVIDIA(model="meta/llama2-70b")     response = model.invoke("Hello")     

Create a new NVIDIAChat chat model.

This class provides access to a NVIDIA NIM for chat. By default, it connects to a hosted NIM, but can be configured to connect to a local NIM using the base\_url parameter. An API key is required to connect to the hosted NIM.

Parameters:     

  * **model** \(_str_\) – The model to use for chat.

  * **nvidia\_api\_key** \(_str_\) – The API key to use for connecting to the hosted NIM.

  * **api\_key** \(_str_\) – Alternative to nvidia\_api\_key.

  * **base\_url** \(_str_\) – The base URL of the NIM to connect to. Format for base URL is <http://host:port>

  * **temperature** \(_float_\) – Sampling temperature in \[0, 1\].

  * **max\_tokens** \(_int_\) – Maximum number of tokens to generate. Deprecated, use max\_completion\_tokens instead max\_tokens and max\_completion\_tokens are aliases. If both max\_tokens and max\_completion\_tokens are supplied, max\_completion\_tokens takes precedence.

  * **max\_completion\_tokens** \(_int_\) – Maximum number of tokens to generate.

  * **top\_p** \(_float_\) – Top-p for distribution sampling.

  * **seed** \(_int_\) – A seed for deterministic results.

  * **stop** \(_list_ _\[__str_ _\]_\) – A list of cased stop words.

API Key: \- The recommended way to provide the API key is through the NVIDIA\_API\_KEY

> environment variable.

Base URL: \- Connect to a self-hosted model with NVIDIA NIM using the base\_url arg to

> link to the local host at localhost:8000: llm = ChatNVIDIA\( >
>> base\_url=”<http://localhost:8000/v1>”, model=”meta-llama3-8b-instruct” >  > \)

Note

ChatNVIDIA implements the standard [`Runnable Interface`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable"). 🏃

The [`Runnable Interface`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") has additional methods that are available on runnables, such as [`with_config`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.with_config "langchain_core.runnables.base.Runnable.with_config"), [`with_types`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.with_types "langchain_core.runnables.base.Runnable.with_types"), [`with_retry`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.with_retry "langchain_core.runnables.base.Runnable.with_retry"), [`assign`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.assign "langchain_core.runnables.base.Runnable.assign"), [`bind`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.bind "langchain_core.runnables.base.Runnable.bind"), [`get_graph`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.get_graph "langchain_core.runnables.base.Runnable.get_graph"), and more.

_param _base\_url _: str | None_ _ = None_\#     

Base url for model listing an invocation

_param _cache _: [BaseCache](https://python.langchain.com/api_reference/core/caches/langchain_core.caches.BaseCache.html#langchain_core.caches.BaseCache "langchain_core.caches.BaseCache") | bool | None_ _ = None_\#     

Whether to cache the response.

  * If true, will use the global cache.

  * If false, will not use a cache

  * If None, will use the global cache if it’s set, otherwise no cache.

  * If instance of BaseCache, will use the provided cache.

Caching is not currently supported for streaming methods of models.

_param _callback\_manager _: [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None_ _ = None_\#     

Deprecated since version 0.1.7: Use `callbacks()` instead. It will be removed in pydantic==1.0.

Callback manager to add to the run trace.

_param _callbacks _: Callbacks_ _ = None_\#     

Callbacks to add to the run trace.

_param _custom\_get\_token\_ids _: Callable\[\[str\], list\[int\]\] | None_ _ = None_\#     

Optional encoder to use for counting tokens.

_param _disable\_streaming _: bool | Literal\['tool\_calling'\]__ = False_\#     

Whether to disable streaming for this model.

If streaming is bypassed, then `stream()`/`astream()`/`astream_events()` will defer to `invoke()`/`ainvoke()`.

  * If True, will always bypass streaming case.

  * If `'tool_calling'`, will bypass streaming case only when the model is called with a `tools` keyword argument. In other words, LangChain will automatically switch to non-streaming behavior \(`invoke()`\) only when the tools argument is provided. This offers the best of both worlds.

  * If False \(default\), will always use streaming case if available.

The main reason for this flag is that code might be written using `.stream()` and a user may want to swap out a given model for another model whose the implementation does not properly support streaming.

_param _max\_tokens _: int | None_ _ = 1024_ _\(alias 'max\_completion\_tokens'\)_\#     

Maximum \# of tokens to generate

_param _metadata _: dict\[str, Any\] | None_ _ = None_\#     

Metadata to add to the run trace.

_param _model _: str | None_ _ = None_\#     

Name of the model to invoke

_param _rate\_limiter _: [BaseRateLimiter](https://python.langchain.com/api_reference/core/rate_limiters/langchain_core.rate_limiters.BaseRateLimiter.html#langchain_core.rate_limiters.BaseRateLimiter "langchain_core.rate_limiters.BaseRateLimiter") | None_ _ = None_\#     

An optional rate limiter to use for limiting the number of requests.

_param _seed _: int | None_ _ = None_\#     

The seed for deterministic results

_param _stop _: Sequence\[str\] | None_ _ = None_\#     

Stop words \(cased\)

_param _stream\_options _: Dict\[str, Any\] | None_ _ = \{'include\_usage': True\}_\#     

Stream options for the model. Set to None to disable

_param _tags _: list\[str\] | None_ _ = None_\#     

Tags to add to the run trace.

_param _temperature _: float | None_ _ = None_\#     

Sampling temperature in \[0, 1\]

_param _top\_p _: float | None_ _ = None_\#     

Top-p for distribution sampling

_param _verbose _: bool_ _\[Optional\]_\#     

Whether to print out response text.

_classmethod _get\_available\_models\(

    _\*\* kwargs: Any_, \) → List\[Model\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_nvidia_ai_endpoints/chat_models.html#ChatNVIDIA.get_available_models)\#     

Get a list of available models that work with ChatNVIDIA.

Parameters:     

**kwargs** \(_Any_\)

Return type:     

_List_\[_Model_\]

\_\_call\_\_\(

    _messages : list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_,     _stop : list\[str\] | None = None_,     _callbacks : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _\*\* kwargs: Any_, \) → [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\#     

Deprecated since version 0.1.7: Use `invoke()` instead. It will not be removed until langchain-core==1.0.

Call the model.

Parameters:     

  * **messages** \(_list_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]_\) – List of messages.

  * **stop** \(_list_ _\[__str_ _\]__|__None_\) – Stop words to use when generating. Model output is cut off at the first occurrence of any of these substrings.

  * **callbacks** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__|_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\) – Callbacks to pass through. Used for executing additional functionality, such as logging or streaming, throughout generation.

  * **\*\*kwargs** \(_Any_\) – Arbitrary additional keyword arguments. These are usually passed to the model provider API call.

Returns:     

The model output message.

Return type:     

[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")

_async _abatch\(

    _inputs : list\[Input\]_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | list\[[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")\] | None = None_,     _\*_ ,     _return\_exceptions : bool = False_,     _\*\* kwargs: Any | None_, \) → list\[Output\]\#     

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

    _inputs : Sequence\[Input\]_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | Sequence\[[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")\] | None = None_,     _\*_ ,     _return\_exceptions : bool = False_,     _\*\* kwargs: Any | None_, \) → AsyncIterator\[tuple\[int, Output | Exception\]\]\#     

Run ainvoke in parallel on a list of inputs.

Yields results as they complete.

Parameters:     

  * **inputs** \(_Sequence_ _\[__Input_ _\]_\) – A list of inputs to the Runnable.

  * **config** \([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__Sequence_ _\[_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _\]__|__None_\) – A config to use when invoking the Runnable. The config supports standard keys like ‘tags’, ‘metadata’ for tracing purposes, ‘max\_concurrency’ for controlling how much work to do in parallel, and other keys. Please refer to the RunnableConfig for more details. Defaults to None. Defaults to None.

  * **return\_exceptions** \(_bool_\) – Whether to return exceptions instead of raising them. Defaults to False.

  * **kwargs** \(_Any_ _|__None_\) – Additional keyword arguments to pass to the Runnable.

Yields:     

A tuple of the index of the input and the output from the Runnable.

Return type:     

_AsyncIterator_\[tuple\[int, _Output_ | Exception\]\]

_async _ainvoke\(

    _input : LanguageModelInput_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_,     _\*_ ,     _stop : list\[str\] | None = None_,     _\*\* kwargs: Any_, \) → [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\#     

Default implementation of ainvoke, calls invoke from a thread.

The default implementation allows usage of async code even if the Runnable did not implement a native async version of invoke.

Subclasses should override this method if they can run asynchronously.

Parameters:     

  * **input** \(_LanguageModelInput_\)

  * **config** \(_Optional_ _\[_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _\]_\)

  * **stop** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\)

  * **kwargs** \(_Any_\)

Return type:     

[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")

_async _astream\(

    _input : LanguageModelInput_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_,     _\*_ ,     _stop : list\[str\] | None = None_,     _\*\* kwargs: Any_, \) → AsyncIterator\[[BaseMessageChunk](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessageChunk.html#langchain_core.messages.base.BaseMessageChunk "langchain_core.messages.base.BaseMessageChunk")\]\#     

Default implementation of astream, which calls ainvoke.

Subclasses should override this method if they support streaming output.

Parameters:     

  * **input** \(_LanguageModelInput_\) – The input to the Runnable.

  * **config** \(_Optional_ _\[_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _\]_\) – The config to use for the Runnable. Defaults to None.

  * **kwargs** \(_Any_\) – Additional keyword arguments to pass to the Runnable.

  * **stop** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\)

Yields:     

The output of the Runnable.

Return type:     

AsyncIterator\[[BaseMessageChunk](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessageChunk.html#langchain_core.messages.base.BaseMessageChunk "langchain_core.messages.base.BaseMessageChunk")\]

_async _astream\_events\(

    _input : Any_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_,     _\*_ ,     _version : Literal\['v1', 'v2'\] = 'v2'_,     _include\_names : Sequence\[str\] | None = None_,     _include\_types : Sequence\[str\] | None = None_,     _include\_tags : Sequence\[str\] | None = None_,     _exclude\_names : Sequence\[str\] | None = None_,     _exclude\_types : Sequence\[str\] | None = None_,     _exclude\_tags : Sequence\[str\] | None = None_,     _\*\* kwargs: Any_, \) → AsyncIterator\[StreamEvent\]\#     

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

batch\(

    _inputs : list\[Input\]_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | list\[[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")\] | None = None_,     _\*_ ,     _return\_exceptions : bool = False_,     _\*\* kwargs: Any | None_, \) → list\[Output\]\#     

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

    _inputs : Sequence\[Input\]_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | Sequence\[[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")\] | None = None_,     _\*_ ,     _return\_exceptions : bool = False_,     _\*\* kwargs: Any | None_, \) → Iterator\[tuple\[int, Output | Exception\]\]\#     

Run invoke in parallel on a list of inputs.

Yields results as they complete.

Parameters:     

  * **inputs** \(_Sequence_ _\[__Input_ _\]_\)

  * **config** \([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__Sequence_ _\[_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _\]__|__None_\)

  * **return\_exceptions** \(_bool_\)

  * **kwargs** \(_Any_ _|__None_\)

Return type:     

_Iterator_\[tuple\[int, _Output_ | Exception\]\]

bind\(

    _\*\* kwargs: Any_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Input, Output\]\#     

Bind arguments to a Runnable, returning a new Runnable.

Useful when a Runnable in a chain requires an argument that is not in the output of the previous Runnable or included in the user input.

Parameters:     

**kwargs** \(_Any_\) – The arguments to bind to the Runnable.

Returns:     

A new Runnable with the arguments bound.

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[_Input_ , _Output_\]

Example:               from langchain_ollama import ChatOllama     from langchain_core.output_parsers import StrOutputParser          llm = ChatOllama(model='llama2')          # Without bind.     chain = (         llm         | StrOutputParser()     )          chain.invoke("Repeat quoted words exactly: 'One two three four five.'")     # Output is 'One two three four five.'          # With bind.     chain = (         llm.bind(stop=["three"])         | StrOutputParser()     )          chain.invoke("Repeat quoted words exactly: 'One two three four five.'")     # Output is 'One two'     

bind\_functions\(

    _functions : Sequence\[Dict\[str, Any\] | Type\[BaseModel\] | Callable\]_,     _function\_call : str | None = None_,     _\*\* kwargs: Any_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[[PromptValue](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue") | str | Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") | list\[str\] | tuple\[str, str\] | str | dict\[str, Any\]\], [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_nvidia_ai_endpoints/chat_models.html#ChatNVIDIA.bind_functions)\#     

Parameters:     

  * **functions** \(_Sequence_ _\[__Dict_ _\[__str_ _,__Any_ _\]__|__Type_ _\[__BaseModel_ _\]__|__Callable_ _\]_\)

  * **function\_call** \(_str_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[[_PromptValue_](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue") | str | _Sequence_\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") | list\[str\] | tuple\[str, str\] | str | dict\[str, _Any_\]\], [_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

bind\_tools\(

    _tools : Sequence\[Dict\[str, Any\] | Type | Callable | [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]_,     _\*_ ,     _tool\_choice : dict | str | Literal\['auto', 'none', 'any', 'required'\] | bool | None = None_,     _\*\* kwargs: Any_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[[PromptValue](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue") | str | Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") | list\[str\] | tuple\[str, str\] | str | dict\[str, Any\]\], [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_nvidia_ai_endpoints/chat_models.html#ChatNVIDIA.bind_tools)\#     

Bind tools to the model.

Notes

  * The strict mode is always in effect, if you need it disabled,     

please file an issue.

Parameters:     

  * **tools** \(_list_\) – A list of tools to bind to the model.

  * **\(****Optional****\[****Union****\[****dict** \(_tool\_choice_\) – 

str,     

Literal\[“auto”, “none”, “any”, “required”\], bool\]\]\):

Control tool choice.     

”any” and “required” - force a tool call. “auto” - let the model decide. “none” - force no tool call. string or dict - force a specific tool call. bool - if True, force a tool call; if False, force no tool call.

Defaults to passing no value.

  * **tool\_choice** \(_dict_ _|__str_ _|__Literal_ _\[__'auto'__,__'none'__,__'any'__,__'required'__\]__|__bool_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[[_PromptValue_](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue") | str | _Sequence_\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") | list\[str\] | tuple\[str, str\] | str | dict\[str, _Any_\]\], [_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

:paramstr,     

> Literal\[“auto”, “none”, “any”, “required”\], bool\]\]\):

Control tool choice.     

“any” and “required” - force a tool call. “auto” - let the model decide. “none” - force no tool call. string or dict - force a specific tool call. bool - if True, force a tool call; if False, force no tool call.

Defaults to passing no value.

Parameters:     

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

  * **tools** \(_Sequence_ _\[__Dict_ _\[__str_ _,__Any_ _\]__|__Type_ _|__Callable_ _|_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]_\)

  * **tool\_choice** \(_dict_ _|__str_ _|__Literal_ _\[__'auto'__,__'none'__,__'any'__,__'required'__\]__|__bool_ _|__None_\)

  * **\*\*kwargs**

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[[_PromptValue_](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue") | str | _Sequence_\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") | list\[str\] | tuple\[str, str\] | str | dict\[str, _Any_\]\], [_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

see <https://python.langchain.com/v0.1/docs/modules/model_io/chat/function_calling/#request-forcing-a-tool-call>

configurable\_alternatives\(

    _which : [ConfigurableField](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableField.html#langchain_core.runnables.utils.ConfigurableField "langchain_core.runnables.utils.ConfigurableField")_,     _\*_ ,     _default\_key : str = 'default'_,     _prefix\_keys : bool = False_,     _\*\* kwargs: [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Input, Output\] | Callable\[\[\], [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Input, Output\]\]_, \) → [RunnableSerializable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableSerializable.html#langchain_core.runnables.base.RunnableSerializable "langchain_core.runnables.base.RunnableSerializable")\#     

Configure alternatives for Runnables that can be set at runtime.

Parameters:     

  * **which** \([_ConfigurableField_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableField.html#langchain_core.runnables.utils.ConfigurableField "langchain_core.runnables.utils.ConfigurableField")\) – The ConfigurableField instance that will be used to select the alternative.

  * **default\_key** \(_str_\) – The default key to use if no alternative is selected. Defaults to “default”.

  * **prefix\_keys** \(_bool_\) – Whether to prefix the keys with the ConfigurableField id. Defaults to False.

  * **\*\*kwargs** \([_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") _\[__Input_ _,__Output_ _\]__|__Callable_ _\[__\[__\]__,_[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") _\[__Input_ _,__Output_ _\]__\]_\) – A dictionary of keys to Runnable instances or callables that return Runnable instances.

Returns:     

A new Runnable with the alternatives configured.

Return type:     

[_RunnableSerializable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableSerializable.html#langchain_core.runnables.base.RunnableSerializable "langchain_core.runnables.base.RunnableSerializable")               from langchain_anthropic import ChatAnthropic     from langchain_core.runnables.utils import ConfigurableField     from langchain_openai import ChatOpenAI          model = ChatAnthropic(         model_name="claude-3-sonnet-20240229"     ).configurable_alternatives(         ConfigurableField(id="llm"),         default_key="anthropic",         openai=ChatOpenAI()     )          # uses the default model ChatAnthropic     print(model.invoke("which organization created you?").content)          # uses ChatOpenAI     print(         model.with_config(             configurable={"llm": "openai"}         ).invoke("which organization created you?").content     )     

configurable\_fields\(

    _\*\* kwargs: [ConfigurableField](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableField.html#langchain_core.runnables.utils.ConfigurableField "langchain_core.runnables.utils.ConfigurableField") | [ConfigurableFieldSingleOption](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableFieldSingleOption.html#langchain_core.runnables.utils.ConfigurableFieldSingleOption "langchain_core.runnables.utils.ConfigurableFieldSingleOption") | [ConfigurableFieldMultiOption](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableFieldMultiOption.html#langchain_core.runnables.utils.ConfigurableFieldMultiOption "langchain_core.runnables.utils.ConfigurableFieldMultiOption")_, \) → [RunnableSerializable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableSerializable.html#langchain_core.runnables.base.RunnableSerializable "langchain_core.runnables.base.RunnableSerializable")\#     

Configure particular Runnable fields at runtime.

Parameters:     

**\*\*kwargs** \([_ConfigurableField_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableField.html#langchain_core.runnables.utils.ConfigurableField "langchain_core.runnables.utils.ConfigurableField") _|_[_ConfigurableFieldSingleOption_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableFieldSingleOption.html#langchain_core.runnables.utils.ConfigurableFieldSingleOption "langchain_core.runnables.utils.ConfigurableFieldSingleOption") _|_[_ConfigurableFieldMultiOption_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableFieldMultiOption.html#langchain_core.runnables.utils.ConfigurableFieldMultiOption "langchain_core.runnables.utils.ConfigurableFieldMultiOption")\) – A dictionary of ConfigurableField instances to configure.

Returns:     

A new Runnable with the fields configured.

Return type:     

[_RunnableSerializable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableSerializable.html#langchain_core.runnables.base.RunnableSerializable "langchain_core.runnables.base.RunnableSerializable")               from langchain_core.runnables import ConfigurableField     from langchain_openai import ChatOpenAI          model = ChatOpenAI(max_tokens=20).configurable_fields(         max_tokens=ConfigurableField(             id="output_token_number",             name="Max tokens in the output",             description="The maximum number of tokens in the output",         )     )          # max_tokens = 20     print(         "max_tokens_20: ",         model.invoke("tell me something about chess").content     )          # max_tokens = 200     print("max_tokens_200: ", model.with_config(         configurable={"output_token_number": 200}         ).invoke("tell me something about chess").content     )     

get\_num\_tokens\(_text : str_\) → int\#     

Get the number of tokens present in the text.

Useful for checking if an input fits in a model’s context window.

Parameters:     

**text** \(_str_\) – The string input to tokenize.

Returns:     

The integer number of tokens in the text.

Return type:     

int

get\_num\_tokens\_from\_messages\(

    _messages : list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_,     _tools : Sequence | None = None_, \) → int\#     

Get the number of tokens in the messages.

Useful for checking if an input fits in a model’s context window.

**Note** : the base implementation of get\_num\_tokens\_from\_messages ignores tool schemas.

Parameters:     

  * **messages** \(_list_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]_\) – The message inputs to tokenize.

  * **tools** \(_Sequence_ _|__None_\) – If provided, sequence of dict, BaseModel, function, or BaseTools to be converted to tool schemas.

Returns:     

The sum of the number of tokens across the messages.

Return type:     

int

get\_token\_ids\(_text : str_\) → list\[int\]\#     

Return the ordered ids of the tokens in a text.

Parameters:     

**text** \(_str_\) – The string input to tokenize.

Returns:     

A list of ids corresponding to the tokens in the text, in order they occur     

in the text.

Return type:     

list\[int\]

invoke\(

    _input : LanguageModelInput_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_,     _\*_ ,     _stop : list\[str\] | None = None_,     _\*\* kwargs: Any_, \) → [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\#     

Transform a single input into an output.

Parameters:     

  * **input** \(_LanguageModelInput_\) – The input to the Runnable.

  * **config** \(_Optional_ _\[_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _\]_\) – A config to use when invoking the Runnable. The config supports standard keys like ‘tags’, ‘metadata’ for tracing purposes, ‘max\_concurrency’ for controlling how much work to do in parallel, and other keys. Please refer to the RunnableConfig for more details.

  * **stop** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\)

  * **kwargs** \(_Any_\)

Returns:     

The output of the Runnable.

Return type:     

[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")

stream\(

    _input : LanguageModelInput_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_,     _\*_ ,     _stop : list\[str\] | None = None_,     _\*\* kwargs: Any_, \) → Iterator\[[BaseMessageChunk](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessageChunk.html#langchain_core.messages.base.BaseMessageChunk "langchain_core.messages.base.BaseMessageChunk")\]\#     

Default implementation of stream, which calls invoke.

Subclasses should override this method if they support streaming output.

Parameters:     

  * **input** \(_LanguageModelInput_\) – The input to the Runnable.

  * **config** \(_Optional_ _\[_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _\]_\) – The config to use for the Runnable. Defaults to None.

  * **kwargs** \(_Any_\) – Additional keyword arguments to pass to the Runnable.

  * **stop** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\)

Yields:     

The output of the Runnable.

Return type:     

Iterator\[[BaseMessageChunk](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessageChunk.html#langchain_core.messages.base.BaseMessageChunk "langchain_core.messages.base.BaseMessageChunk")\]

with\_alisteners\(

    _\*_ ,     _on\_start : AsyncListener | None = None_,     _on\_end : AsyncListener | None = None_,     _on\_error : AsyncListener | None = None_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Input, Output\]\#     

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

[Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Input, Output\]

Example:               from langchain_core.runnables import RunnableLambda, Runnable     from datetime import datetime, timezone     import time     import asyncio          def format_t(timestamp: float) -> str:         return datetime.fromtimestamp(timestamp, tz=timezone.utc).isoformat()          async def test_runnable(time_to_sleep : int):         print(f"Runnable[{time_to_sleep}s]: starts at {format_t(time.time())}")         await asyncio.sleep(time_to_sleep)         print(f"Runnable[{time_to_sleep}s]: ends at {format_t(time.time())}")          async def fn_start(run_obj : Runnable):         print(f"on start callback starts at {format_t(time.time())}")         await asyncio.sleep(3)         print(f"on start callback ends at {format_t(time.time())}")          async def fn_end(run_obj : Runnable):         print(f"on end callback starts at {format_t(time.time())}")         await asyncio.sleep(2)         print(f"on end callback ends at {format_t(time.time())}")          runnable = RunnableLambda(test_runnable).with_alisteners(         on_start=fn_start,         on_end=fn_end     )     async def concurrent_runs():         await asyncio.gather(runnable.ainvoke(2), runnable.ainvoke(3))          asyncio.run(concurrent_runs())     Result:     on start callback starts at 2025-03-01T07:05:22.875378+00:00     on start callback starts at 2025-03-01T07:05:22.875495+00:00     on start callback ends at 2025-03-01T07:05:25.878862+00:00     on start callback ends at 2025-03-01T07:05:25.878947+00:00     Runnable[2s]: starts at 2025-03-01T07:05:25.879392+00:00     Runnable[3s]: starts at 2025-03-01T07:05:25.879804+00:00     Runnable[2s]: ends at 2025-03-01T07:05:27.881998+00:00     on end callback starts at 2025-03-01T07:05:27.882360+00:00     Runnable[3s]: ends at 2025-03-01T07:05:28.881737+00:00     on end callback starts at 2025-03-01T07:05:28.882428+00:00     on end callback ends at 2025-03-01T07:05:29.883893+00:00     on end callback ends at 2025-03-01T07:05:30.884831+00:00     

with\_config\(

    _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_,     _\*\* kwargs: Any_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Input, Output\]\#     

Bind config to a Runnable, returning a new Runnable.

Parameters:     

  * **config** \([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__None_\) – The config to bind to the Runnable.

  * **kwargs** \(_Any_\) – Additional keyword arguments to pass to the Runnable.

Returns:     

A new Runnable with the config bound.

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[_Input_ , _Output_\]

with\_fallbacks\(_fallbacks: Sequence\[Runnable\[Input, Output\]\], \*, exceptions\_to\_handle: tuple\[type\[BaseException\], ...\] = \(<class 'Exception'>,\), exception\_key: Optional\[str\] = None_\) → RunnableWithFallbacksT\[Input, Output\]\#     

Add fallbacks to a Runnable, returning a new Runnable.

The new Runnable will try the original Runnable, and then each fallback in order, upon failures.

Parameters:     

  * **fallbacks** \(_Sequence_ _\[_[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") _\[__Input_ _,__Output_ _\]__\]_\) – A sequence of runnables to try if the original Runnable fails.

  * **exceptions\_to\_handle** \(_tuple_ _\[__type_ _\[__BaseException_ _\]__,__...__\]_\) – A tuple of exception types to handle. Defaults to \(Exception,\).

  * **exception\_key** \(_Optional_ _\[__str_ _\]_\) – If string is specified then handled exceptions will be passed to fallbacks as part of the input under the specified key. If None, exceptions will not be passed to fallbacks. If used, the base Runnable and its fallbacks must accept a dictionary as input. Defaults to None.

Returns:     

A new Runnable that will try the original Runnable, and then each fallback in order, upon failures.

Return type:     

RunnableWithFallbacksT\[Input, Output\]

Example               from typing import Iterator          from langchain_core.runnables import RunnableGenerator               def _generate_immediate_error(input: Iterator) -> Iterator[str]:         raise ValueError()         yield ""               def _generate(input: Iterator) -> Iterator[str]:         yield from "foo bar"               runnable = RunnableGenerator(_generate_immediate_error).with_fallbacks(         [RunnableGenerator(_generate)]         )     print(''.join(runnable.stream({}))) #foo bar     

Parameters:     

  * **fallbacks** \(_Sequence_ _\[_[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") _\[__Input_ _,__Output_ _\]__\]_\) – A sequence of runnables to try if the original Runnable fails.

  * **exceptions\_to\_handle** \(_tuple_ _\[__type_ _\[__BaseException_ _\]__,__...__\]_\) – A tuple of exception types to handle.

  * **exception\_key** \(_Optional_ _\[__str_ _\]_\) – If string is specified then handled exceptions will be passed to fallbacks as part of the input under the specified key. If None, exceptions will not be passed to fallbacks. If used, the base Runnable and its fallbacks must accept a dictionary as input.

Returns:     

A new Runnable that will try the original Runnable, and then each fallback in order, upon failures.

Return type:     

RunnableWithFallbacksT\[Input, Output\]

with\_listeners\(

    _\*_ ,     _on\_start : Callable\[\[Run\], None\] | Callable\[\[Run, [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")\], None\] | None = None_,     _on\_end : Callable\[\[Run\], None\] | Callable\[\[Run, [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")\], None\] | None = None_,     _on\_error : Callable\[\[Run\], None\] | Callable\[\[Run, [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")\], None\] | None = None_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Input, Output\]\#     

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

[Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Input, Output\]

Example:               from langchain_core.runnables import RunnableLambda     from langchain_core.tracers.schemas import Run          import time          def test_runnable(time_to_sleep : int):         time.sleep(time_to_sleep)          def fn_start(run_obj: Run):         print("start_time:", run_obj.start_time)          def fn_end(run_obj: Run):         print("end_time:", run_obj.end_time)          chain = RunnableLambda(test_runnable).with_listeners(         on_start=fn_start,         on_end=fn_end     )     chain.invoke(2)     

with\_retry\(_\*, retry\_if\_exception\_type: tuple\[type\[BaseException\], ...\] = \(<class 'Exception'>,\), wait\_exponential\_jitter: bool = True, exponential\_jitter\_params: Optional\[ExponentialJitterParams\] = None, stop\_after\_attempt: int = 3_\) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Input, Output\]\#     

Create a new Runnable that retries the original Runnable on exceptions.

Parameters:     

  * **retry\_if\_exception\_type** \(_tuple_ _\[__type_ _\[__BaseException_ _\]__,__...__\]_\) – A tuple of exception types to retry on. Defaults to \(Exception,\).

  * **wait\_exponential\_jitter** \(_bool_\) – Whether to add jitter to the wait time between retries. Defaults to True.

  * **stop\_after\_attempt** \(_int_\) – The maximum number of attempts to make before giving up. Defaults to 3.

  * **exponential\_jitter\_params** \(_Optional_ _\[_[_ExponentialJitterParams_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.retry.ExponentialJitterParams.html#langchain_core.runnables.retry.ExponentialJitterParams "langchain_core.runnables.retry.ExponentialJitterParams") _\]_\) – Parameters for `tenacity.wait_exponential_jitter`. Namely: `initial`, `max`, `exp_base`, and `jitter` \(all float values\).

Returns:     

A new Runnable that retries the original Runnable on exceptions.

Return type:     

[Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Input, Output\]

Example:               from langchain_core.runnables import RunnableLambda          count = 0               def _lambda(x: int) -> None:         global count         count = count + 1         if x == 1:             raise ValueError("x is 1")         else:              pass               runnable = RunnableLambda(_lambda)     try:         runnable.with_retry(             stop_after_attempt=2,             retry_if_exception_type=(ValueError,),         ).invoke(1)     except ValueError:         pass          assert (count == 2)     

with\_structured\_output\(

    _schema : Dict | Type_,     _\*_ ,     _include\_raw : bool = False_,     _\*\* kwargs: Any_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[[PromptValue](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue") | str | Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") | list\[str\] | tuple\[str, str\] | str | dict\[str, Any\]\], Dict | BaseModel\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_nvidia_ai_endpoints/chat_models.html#ChatNVIDIA.with_structured_output)\#     

Bind a structured output schema to the model.

Parameters:     

  * **schema** \(_Union_ _\[__Dict_ _,__Type_ _\]_\) – The schema to bind to the model.

  * **include\_raw** \(_bool_\) – Always False. Passing True raises an error.

  * **\*\*kwargs** – Additional keyword arguments.

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[[_PromptValue_](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue") | str | _Sequence_\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") | list\[str\] | tuple\[str, str\] | str | dict\[str, _Any_\]\], _Dict_ | _BaseModel_\]

Notes

  * strict mode is always in effect, if you need it disabled, please file an issue.

  * if you need include\_raw=True consider using an unstructured model and     

output formatter, or file an issue.

The schema can be -     

  0. a dictionary representing a JSON schema

  1. a Pydantic object

  2. an Enum

0\. If a dictionary is provided, the model will return a dictionary. Example: \`\`\` json\_schema = \{

> “title”: “joke”, “description”: “Joke to tell user.”, “type”: “object”, “properties”: \{ >
>> “setup”: \{ >>      >>  >> “type”: “string”, “description”: “The setup of the joke”, >>  >> \}, “punchline”: \{ >> >>> “type”: “string”, “description”: “The punchline to the joke”, >>  >> \}, >  > \}, “required”: \[“setup”, “punchline”\],

\}

structured\_llm = llm.with\_structured\_output\(json\_schema\) structured\_llm.invoke\(“Tell me a joke about NVIDIA”\) \# Output: \{‘setup’: ‘Why did NVIDIA go broke? The hardware ate all the software.’, \# ‘punchline’: ‘It took a big bite out of their main board.’\} \`\`\`

  1. If a Pydantic schema is provided, the model will return a Pydantic object. Example:

\`\`\` from pydantic import BaseModel, Field class Joke\(BaseModel\):

> setup: str = Field\(description=”The setup of the joke”\) punchline: str = Field\(description=”The punchline to the joke”\)

structured\_llm = llm.with\_structured\_output\(Joke\) structured\_llm.invoke\(“Tell me a joke about NVIDIA”\) \# Output: Joke\(setup=’Why did NVIDIA go broke? The hardware ate all the software.’, \# punchline=’It took a big bite out of their main board.’\) \`\`\`

  2. If an Enum is provided, all values must be strings, and the model will return an Enum object. Example:

\`\`\` import enum class Choices\(enum.Enum\):

> A = “A” B = “B” C = “C”

structured\_llm = llm.with\_structured\_output\(Choices\) structured\_llm.invoke\(“What is the first letter in this list? \[X, Y, Z, C\]”\) \# Output: <Choices.C: ‘C’> \`\`\`

Note about streaming: Unlike other streaming responses, the streamed chunks will be increasingly complete. They will not be deltas. The last chunk will contain the complete response.

For instance with a dictionary schema, the chunks will be: \`\`\` structured\_llm = llm.with\_structured\_output\(json\_schema\) for chunk in structured\_llm.stream\(“Tell me a joke about NVIDIA”\):

> print\(chunk\)

\# Output: \# \{\} \# \{‘setup’: ‘’\} \# \{‘setup’: ‘Why’\} \# \{‘setup’: ‘Why did’\} \# \{‘setup’: ‘Why did N’\} \# \{‘setup’: ‘Why did NVID’\} \# … \# \{‘setup’: ‘Why did NVIDIA go broke? The hardware ate all the software.’, ‘punchline’: ‘It took a big bite out of their main board’\} \# \{‘setup’: ‘Why did NVIDIA go broke? The hardware ate all the software.’, ‘punchline’: ‘It took a big bite out of their main board.’\} \`\`\`

For instnace with a Pydantic schema, the chunks will be: \`\`\` structured\_llm = llm.with\_structured\_output\(Joke\) for chunk in structured\_llm.stream\(“Tell me a joke about NVIDIA”\):

> print\(chunk\)

\# Output: \# setup=’Why did NVIDIA go broke? The hardware ate all the software.’ punchline=’’ \# setup=’Why did NVIDIA go broke? The hardware ate all the software.’ punchline=’It’ \# setup=’Why did NVIDIA go broke? The hardware ate all the software.’ punchline=’It took’ \# … \# setup=’Why did NVIDIA go broke? The hardware ate all the software.’ punchline=’It took a big bite out of their main board’ \# setup=’Why did NVIDIA go broke? The hardware ate all the software.’ punchline=’It took a big bite out of their main board.’ \`\`\`

For Pydantic schema and Enum, the output will be None if the response is insufficient to construct the object or otherwise invalid. For instance, \`\`\` llm = ChatNVIDIA\(max\_completion\_tokens=1\) structured\_llm = llm.with\_structured\_output\(Joke\) print\(structured\_llm.invoke\(“Tell me a joke about NVIDIA”\)\)

\# Output: None \`\`\`

For more, see <https://python.langchain.com/docs/how_to/structured_output/>

with\_thinking\_mode\(

    _enabled : bool = True_,     _\*\* kwargs: Any_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[[PromptValue](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue") | str | Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") | list\[str\] | tuple\[str, str\] | str | dict\[str, Any\]\], [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_nvidia_ai_endpoints/chat_models.html#ChatNVIDIA.with_thinking_mode)\#     

Configure the model to use thinking mode.

Parameters:     

  * **enabled** \(_bool_\) – Whether to enable thinking mode. Defaults to True.

  * **\*\*kwargs** – Additional keyword arguments.

Returns:     

A runnable that will use thinking mode when enabled.

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[[_PromptValue_](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue") | str | _Sequence_\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") | list\[str\] | tuple\[str, str\] | str | dict\[str, _Any_\]\], [_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

Example               from langchain_nvidia_ai_endpoints import ChatNVIDIA          model = ChatNVIDIA(model="nvidia/llama-3.1-nemotron-nano-8b-v1")          # Enable thinking mode     thinking_model = model.with_thinking_mode(enabled=True)     response = thinking_model.invoke("Hello")          # Disable thinking mode     no_thinking_model = model.with_thinking_mode(enabled=False)     response = no_thinking_model.invoke("Hello")     

with\_types\(

    _\*_ ,     _input\_type : type\[Input\] | None = None_,     _output\_type : type\[Output\] | None = None_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Input, Output\]\#     

Bind input and output types to a Runnable, returning a new Runnable.

Parameters:     

  * **input\_type** \(_type_ _\[__Input_ _\]__|__None_\) – The input type to bind to the Runnable. Defaults to None.

  * **output\_type** \(_type_ _\[__Output_ _\]__|__None_\) – The output type to bind to the Runnable. Defaults to None.

Returns:     

A new Runnable with the types bound.

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[_Input_ , _Output_\]

_property _available\_models _: List\[Model\]_\#     

Get a list of available models that work with ChatNVIDIA.

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)