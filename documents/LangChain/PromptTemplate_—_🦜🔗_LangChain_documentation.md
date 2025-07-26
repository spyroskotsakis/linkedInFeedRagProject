# PromptTemplate — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.prompt.PromptTemplate.html
**Word Count:** 2648
**Links Count:** 425
**Scraped:** 2025-07-21 07:52:36
**Status:** completed

---

# PromptTemplate\#

_class _langchain\_core.prompts.prompt.PromptTemplate[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompts/prompt.html#PromptTemplate)\#     

Bases: [`StringPromptTemplate`](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.string.StringPromptTemplate.html#langchain_core.prompts.string.StringPromptTemplate "langchain_core.prompts.string.StringPromptTemplate")

Prompt template for a language model.

A prompt template consists of a string template. It accepts a set of parameters from the user that can be used to generate a prompt for a language model.

The template can be formatted using either f-strings \(default\), jinja2, or mustache syntax.

_Security warning_ :     

Prefer using template\_format=”f-string” instead of template\_format=”jinja2”, or make sure to NEVER accept jinja2 templates from untrusted sources as they may lead to arbitrary Python code execution.

As of LangChain 0.0.329, Jinja2 templates will be rendered using Jinja2’s SandboxedEnvironment by default. This sand-boxing should be treated as a best-effort approach rather than a guarantee of security, as it is an opt-out rather than opt-in approach.

Despite the sand-boxing, we recommend to never use jinja2 templates from untrusted sources.

Example               from langchain_core.prompts import PromptTemplate          # Instantiation using from_template (recommended)     prompt = PromptTemplate.from_template("Say {foo}")     prompt.format(foo="bar")          # Instantiation using initializer     prompt = PromptTemplate(template="Say {foo}")     

Note

PromptTemplate implements the standard [`Runnable Interface`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable"). 🏃

The [`Runnable Interface`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") has additional methods that are available on runnables, such as [`with_config`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.with_config "langchain_core.runnables.base.Runnable.with_config"), [`with_types`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.with_types "langchain_core.runnables.base.Runnable.with_types"), [`with_retry`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.with_retry "langchain_core.runnables.base.Runnable.with_retry"), [`assign`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.assign "langchain_core.runnables.base.Runnable.assign"), [`bind`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.bind "langchain_core.runnables.base.Runnable.bind"), [`get_graph`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.get_graph "langchain_core.runnables.base.Runnable.get_graph"), and more.

_param _input\_types _: Dict\[str, Any\]__\[Optional\]_\#     

A dictionary of the types of the variables the prompt template expects. If not provided, all variables are assumed to be strings.

_param _input\_variables _: list\[str\]__\[Required\]_\#     

A list of the names of the variables whose values are required as inputs to the prompt.

_param _metadata _: Dict\[str, Any\] | None_ _ = None_\#     

Metadata to be used for tracing.

_param _optional\_variables _: list\[str\]__ = \[\]_\#     

optional\_variables: A list of the names of the variables for placeholder or MessagePlaceholder that are optional. These variables are auto inferred from the prompt and user need not provide them.

_param _output\_parser _: [BaseOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseOutputParser.html#langchain_core.output_parsers.base.BaseOutputParser "langchain_core.output_parsers.base.BaseOutputParser") | None_ _ = None_\#     

How to parse the output of calling an LLM on this formatted prompt.

_param _partial\_variables _: Mapping\[str, Any\]__\[Optional\]_\#     

A dictionary of the partial variables the prompt template carries.

Partial variables populate the template so that you don’t need to pass them in every time you call the prompt.

_param _tags _: list\[str\] | None_ _ = None_\#     

Tags to be used for tracing.

_param _template _: str_ _\[Required\]_\#     

The prompt template.

_param _template\_format _: PromptTemplateFormat_ _ = 'f-string'_\#     

The format of the prompt template. Options are: ‘f-string’, ‘mustache’, ‘jinja2’.

_param _validate\_template _: bool_ _ = False_\#     

Whether or not to try validating the template.

_classmethod _from\_examples\(

    _examples : list\[str\]_,     _suffix : str_,     _input\_variables : list\[str\]_,     _example\_separator : str = '\n\n'_,     _prefix : str = ''_,     _\*\* kwargs: Any_, \) → PromptTemplate[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompts/prompt.html#PromptTemplate.from_examples)\#     

Take examples in list format with prefix and suffix to create a prompt.

Intended to be used as a way to dynamically create a prompt from examples.

Parameters:     

  * **examples** \(_list_ _\[__str_ _\]_\) – List of examples to use in the prompt.

  * **suffix** \(_str_\) – String to go after the list of examples. Should generally set up the user’s input.

  * **input\_variables** \(_list_ _\[__str_ _\]_\) – A list of variable names the final prompt template will expect.

  * **example\_separator** \(_str_\) – The separator to use in between examples. Defaults to two new line characters.

  * **prefix** \(_str_\) – String that should go before any examples. Generally includes examples. Default to an empty string.

  * **kwargs** \(_Any_\)

Returns:     

The final prompt generated.

Return type:     

_PromptTemplate_

_classmethod _from\_file\(

    _template\_file : str | Path_,     _input\_variables : list\[str\] | None = None_,     _encoding : str | None = None_,     _\*\* kwargs: Any_, \) → PromptTemplate[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompts/prompt.html#PromptTemplate.from_file)\#     

Load a prompt from a file.

Parameters:     

  * **template\_file** \(_str_ _|__Path_\) – The path to the file containing the prompt template.

  * **input\_variables** \(_list_ _\[__str_ _\]__|__None_\) – \[DEPRECATED\] A list of variable names the final prompt template will expect. Defaults to None.

  * **encoding** \(_str_ _|__None_\) – The encoding system for opening the template file. If not provided, will use the OS default.

  * **kwargs** \(_Any_\)

Return type:     

_PromptTemplate_

input\_variables is ignored as from\_file now delegates to from\_template\(\).

Returns:     

The prompt loaded from the file.

Parameters:     

  * **template\_file** \(_str_ _|__Path_\)

  * **input\_variables** \(_list_ _\[__str_ _\]__|__None_\)

  * **encoding** \(_str_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_PromptTemplate_

_classmethod _from\_template\(

    _template : str_,     _\*_ ,     _template\_format : Literal\['f-string', 'mustache', 'jinja2'\] = 'f-string'_,     _partial\_variables : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → PromptTemplate[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompts/prompt.html#PromptTemplate.from_template)\#     

Load a prompt template from a template.

_Security warning_ :     

Prefer using template\_format=”f-string” instead of template\_format=”jinja2”, or make sure to NEVER accept jinja2 templates from untrusted sources as they may lead to arbitrary Python code execution.

As of LangChain 0.0.329, Jinja2 templates will be rendered using Jinja2’s SandboxedEnvironment by default. This sand-boxing should be treated as a best-effort approach rather than a guarantee of security, as it is an opt-out rather than opt-in approach.

Despite the sand-boxing, we recommend never using jinja2 templates from untrusted sources.

Parameters:     

  * **template** \(_str_\) – The template to load.

  * **template\_format** \(_Literal_ _\[__'f-string'__,__'mustache'__,__'jinja2'__\]_\) – The format of the template. Use jinja2 for jinja2, mustache for mustache, and f-string for f-strings. Defaults to f-string.

  * **partial\_variables** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – 

A dictionary of variables that can be used to partially     

fill in the template. For example, if the template is

”\{variable1\} \{variable2\}”, and partial\_variables is \{“variable1”: “foo”\}, then the final prompt will be “foo \{variable2\}”. Defaults to None.

  * **kwargs** \(_Any_\) – Any other arguments to pass to the prompt template.

Returns:     

The prompt template loaded from the template.

Return type:     

_PromptTemplate_

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

_async _aformat\(

    _\*\* kwargs: Any_, \) → FormatOutputType\#     

Async format the prompt with the inputs.

Parameters:     

**kwargs** \(_Any_\) – Any arguments to be passed to the prompt template.

Returns:     

A formatted string.

Return type:     

_FormatOutputType_

Example:               await prompt.aformat(variable1="foo")     

_async _aformat\_prompt\(

    _\*\* kwargs: Any_, \) → [PromptValue](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue")\#     

Async format the prompt with the inputs.

Parameters:     

**kwargs** \(_Any_\) – Any arguments to be passed to the prompt template.

Returns:     

A formatted string.

Return type:     

[_PromptValue_](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue")

_async _ainvoke\(

    _input : dict_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_,     _\*\* kwargs: Any_, \) → [PromptValue](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue")\#     

Async invoke the prompt.

Parameters:     

  * **input** \(_dict_\) – Dict, input to the prompt.

  * **config** \([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__None_\) – RunnableConfig, configuration for the prompt.

  * **kwargs** \(_Any_\)

Returns:     

The output of the prompt.

Return type:     

[PromptValue](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue")

_async _astream\(

    _input : Input_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_,     _\*\* kwargs: Any | None_, \) → AsyncIterator\[Output\]\#     

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

format\(_\*\* kwargs: Any_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompts/prompt.html#PromptTemplate.format)\#     

Format the prompt with the inputs.

Parameters:     

**kwargs** \(_Any_\) – Any arguments to be passed to the prompt template.

Returns:     

A formatted string.

Return type:     

str

format\_prompt\(

    _\*\* kwargs: Any_, \) → [PromptValue](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue")\#     

Format the prompt with the inputs.

Parameters:     

**kwargs** \(_Any_\) – Any arguments to be passed to the prompt template.

Returns:     

A formatted string.

Return type:     

[_PromptValue_](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue")

invoke\(

    _input : dict_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_,     _\*\* kwargs: Any_, \) → [PromptValue](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue")\#     

Invoke the prompt.

Parameters:     

  * **input** \(_dict_\) – Dict, input to the prompt.

  * **config** \([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__None_\) – RunnableConfig, configuration for the prompt.

  * **kwargs** \(_Any_\)

Returns:     

The output of the prompt.

Return type:     

[PromptValue](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue")

partial\(

    _\*\* kwargs: str | Callable\[\[\], str\]_, \) → [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")\#     

Return a partial of the prompt template.

Parameters:     

**kwargs** \(_str_ _|__Callable_ _\[__\[__\]__,__str_ _\]_\) – Union\[str, Callable\[\[\], str\]\], partial variables to set.

Returns:     

A partial of the prompt template.

Return type:     

[BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")

pretty\_print\(\) → None\#     

Print a pretty representation of the prompt.

Return type:     

None

pretty\_repr\(_html : bool = False_\) → str\#     

Get a pretty representation of the prompt.

Parameters:     

**html** \(_bool_\) – Whether to return an HTML-formatted string.

Returns:     

A pretty representation of the prompt.

Return type:     

str

save\(_file\_path : Path | str_\) → None\#     

Save the prompt.

Parameters:     

**file\_path** \(_Path_ _|__str_\) – Path to directory to save prompt to.

Raises:     

  * **ValueError** – If the prompt has partial variables.

  * **ValueError** – If the file path is not json or yaml.

  * **NotImplementedError** – If the prompt type is not implemented.

Return type:     

None

Example: .. code-block:: python

> prompt.save\(file\_path=”path/prompt.yaml”\)

stream\(

    _input : Input_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_,     _\*\* kwargs: Any | None_, \) → Iterator\[Output\]\#     

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

Examples using PromptTemplate

  * [\# Example](https://python.langchain.com/docs/versions/migrating_chains/map_rerank_docs_chain/)

  * [\# Legacy](https://python.langchain.com/docs/versions/migrating_chains/llm_router_chain/)

  * [\# Oracle Cloud Infrastructure Generative AI](https://python.langchain.com/docs/integrations/llms/oci_generative_ai/)

  * [AI21LLM](https://python.langchain.com/docs/integrations/llms/ai21/)

  * [Aim](https://python.langchain.com/docs/integrations/providers/aim_tracking/)

  * [AirbyteLoader](https://python.langchain.com/docs/integrations/document_loaders/airbyte/)

  * [Aleph Alpha](https://python.langchain.com/docs/integrations/llms/aleph_alpha/)

  * [Alibaba Cloud PAI EAS](https://python.langchain.com/docs/integrations/llms/alibabacloud_pai_eas_endpoint/)

  * [Amazon Document DB](https://python.langchain.com/docs/integrations/vectorstores/documentdb/)

  * [AnthropicLLM](https://python.langchain.com/docs/integrations/llms/anthropic/)

  * [Anyscale](https://python.langchain.com/docs/integrations/llms/anyscale/)

  * [Apache AGE](https://python.langchain.com/docs/integrations/graphs/apache_age/)

  * [Aphrodite Engine](https://python.langchain.com/docs/integrations/llms/aphrodite/)

  * [Argilla](https://python.langchain.com/docs/integrations/callbacks/argilla/)

  * [Azure ML](https://python.langchain.com/docs/integrations/llms/azure_ml/)

  * [Banana](https://python.langchain.com/docs/integrations/llms/banana/)

  * [Baseten](https://python.langchain.com/docs/integrations/llms/baseten/)

  * [Bittensor](https://python.langchain.com/docs/integrations/llms/bittensor/)

  * [Build a Question/Answering system over SQL data](https://python.langchain.com/docs/tutorials/sql_qa/)

  * [Build a Retrieval Augmented Generation \(RAG\) App](https://python.langchain.com/docs/tutorials/rag/)

  * [C Transformers](https://python.langchain.com/docs/integrations/llms/ctransformers/)

  * [CTranslate2](https://python.langchain.com/docs/integrations/llms/ctranslate2/)

  * [CerebriumAI](https://python.langchain.com/docs/integrations/llms/cerebriumai/)

  * [ChatGLM](https://python.langchain.com/docs/integrations/llms/chatglm/)

  * [Clarifai](https://python.langchain.com/docs/integrations/llms/clarifai/)

  * [Cloudflare Workers AI](https://python.langchain.com/docs/integrations/llms/cloudflare_workersai/)

  * [Cohere](https://python.langchain.com/docs/integrations/llms/cohere/)

  * [Comet](https://python.langchain.com/docs/integrations/providers/comet_tracking/)

  * [Conceptual guide](https://python.langchain.com/docs/concepts/)

  * [Context](https://python.langchain.com/docs/integrations/callbacks/context/)

  * [DSPy](https://python.langchain.com/docs/integrations/providers/dspy/)

  * [Dall-E Image Generator](https://python.langchain.com/docs/integrations/tools/dalle_image_generator/)

  * [DeepInfra](https://python.langchain.com/docs/integrations/llms/deepinfra/)

  * [Eden AI](https://python.langchain.com/docs/integrations/llms/edenai/)

  * [ExLlamaV2](https://python.langchain.com/docs/integrations/llms/exllamav2/)

  * [Fireworks](https://python.langchain.com/docs/integrations/llms/fireworks/)

  * [Flyte](https://python.langchain.com/docs/integrations/providers/flyte/)

  * [ForefrontAI](https://python.langchain.com/docs/integrations/llms/forefrontai/)

  * [GPT4All](https://python.langchain.com/docs/integrations/llms/gpt4all/)

  * [Generate Synthetic Data](https://python.langchain.com/docs/tutorials/data_generation/)

  * [GigaChat](https://python.langchain.com/docs/integrations/llms/gigachat/)

  * [Google AI](https://python.langchain.com/docs/integrations/llms/google_ai/)

  * [Google Cloud Vertex AI](https://python.langchain.com/docs/integrations/llms/google_vertex_ai_palm/)

  * [Google Cloud Vertex AI Reranker](https://python.langchain.com/docs/integrations/document_transformers/google_cloud_vertexai_rerank/)

  * [Google Drive](https://python.langchain.com/docs/integrations/document_loaders/google_drive/)

  * [GooseAI](https://python.langchain.com/docs/integrations/llms/gooseai/)

  * [Gradient](https://python.langchain.com/docs/integrations/llms/gradient/)

  * [How to add fallbacks to a runnable](https://python.langchain.com/docs/how_to/fallbacks/)

  * [How to best prompt for Graph-RAG](https://python.langchain.com/docs/how_to/graph_prompting/)

  * [How to better prompt when doing SQL question-answering](https://python.langchain.com/docs/how_to/sql_prompting/)

  * [How to compose prompts together](https://python.langchain.com/docs/how_to/prompts_composition/)

  * [How to configure runtime chain internals](https://python.langchain.com/docs/how_to/configure/)

  * [How to parse JSON output](https://python.langchain.com/docs/how_to/output_parser_json/)

  * [How to parse XML output](https://python.langchain.com/docs/how_to/output_parser_xml/)

  * [How to parse YAML output](https://python.langchain.com/docs/how_to/output_parser_yaml/)

  * [How to partially format prompt templates](https://python.langchain.com/docs/how_to/prompts_partial/)

  * [How to reorder retrieved results to mitigate the “lost in the middle” effect](https://python.langchain.com/docs/how_to/long_context_reorder/)

  * [How to retry when a parsing error occurs](https://python.langchain.com/docs/how_to/output_parser_retry/)

  * [How to route between sub-chains](https://python.langchain.com/docs/how_to/routing/)

  * [How to select examples by length](https://python.langchain.com/docs/how_to/example_selectors_length_based/)

  * [How to select examples by maximal marginal relevance \(MMR\)](https://python.langchain.com/docs/how_to/example_selectors_mmr/)

  * [How to select examples by n-gram overlap](https://python.langchain.com/docs/how_to/example_selectors_ngram/)

  * [How to select examples by similarity](https://python.langchain.com/docs/how_to/example_selectors_similarity/)

  * [How to track token usage for LLMs](https://python.langchain.com/docs/how_to/llm_token_usage_tracking/)

  * [How to use example selectors](https://python.langchain.com/docs/how_to/example_selectors/)

  * [How to use few shot examples](https://python.langchain.com/docs/how_to/few_shot_examples/)

  * [How to use output parsers to parse an LLM response into structured format](https://python.langchain.com/docs/how_to/output_parser_structured/)

  * [How to use the MultiQueryRetriever](https://python.langchain.com/docs/how_to/MultiQueryRetriever/)

  * [Hugging Face Local Pipelines](https://python.langchain.com/docs/integrations/llms/huggingface_pipelines/)

  * [Huggingface Endpoints](https://python.langchain.com/docs/integrations/llms/huggingface_endpoint/)

  * [IBM watsonx.ai](https://python.langchain.com/docs/integrations/llms/ibm_watsonx/)

  * [IPEX-LLM](https://python.langchain.com/docs/integrations/llms/ipex_llm/)

  * [Identity-enabled RAG using PebbloRetrievalQA](https://python.langchain.com/docs/integrations/providers/pebblo/pebblo_retrieval_qa/)

  * [Intel Weight-Only Quantization](https://python.langchain.com/docs/integrations/llms/weight_only_quantization/)

  * [Javelin AI Gateway](https://python.langchain.com/docs/integrations/providers/javelin_ai_gateway/)

  * [Javelin AI Gateway Tutorial](https://python.langchain.com/docs/integrations/llms/javelin/)

  * [Llama.cpp](https://python.langchain.com/docs/integrations/llms/llamacpp/)

  * [MLX Local Pipelines](https://python.langchain.com/docs/integrations/llms/mlx_pipelines/)

  * [MLflow AI Gateway](https://python.langchain.com/docs/integrations/providers/mlflow_ai_gateway/)

  * [Manifest](https://python.langchain.com/docs/integrations/llms/manifest/)

  * [Memgraph](https://python.langchain.com/docs/integrations/graphs/memgraph/)

  * [Milvus Hybrid Search Retriever](https://python.langchain.com/docs/integrations/retrievers/milvus_hybrid_search/)

  * [Minimax](https://python.langchain.com/docs/integrations/llms/minimax/)

  * [Modal](https://python.langchain.com/docs/integrations/llms/modal/)

  * [MosaicML](https://python.langchain.com/docs/integrations/llms/mosaicml/)

  * [Motörhead](https://python.langchain.com/docs/integrations/memory/motorhead_memory/)

  * [NLP Cloud](https://python.langchain.com/docs/integrations/llms/nlpcloud/)

  * [NVIDIA Riva: ASR and TTS](https://python.langchain.com/docs/integrations/tools/nvidia_riva/)

  * [Nebula \(Symbl.ai\)](https://python.langchain.com/docs/integrations/llms/symblai_nebula/)

  * [Neo4j](https://python.langchain.com/docs/integrations/graphs/neo4j_cypher/)

  * [OctoAI](https://python.langchain.com/docs/integrations/llms/octoai/)

  * [OpaquePrompts](https://python.langchain.com/docs/integrations/llms/opaqueprompts/)

  * [OpenAI](https://python.langchain.com/docs/integrations/llms/openai/)

  * [OpenLLM](https://python.langchain.com/docs/integrations/llms/openllm/)

  * [OpenLM](https://python.langchain.com/docs/integrations/llms/openlm/)

  * [OpenVINO](https://python.langchain.com/docs/integrations/llms/openvino/)

  * [Petals](https://python.langchain.com/docs/integrations/llms/petals/)

  * [PipelineAI](https://python.langchain.com/docs/integrations/llms/pipelineai/)

  * [Predibase](https://python.langchain.com/docs/integrations/llms/predibase/)

  * [Prediction Guard](https://python.langchain.com/docs/integrations/llms/predictionguard/)

  * [Ray Serve](https://python.langchain.com/docs/integrations/providers/ray_serve/)

  * [RePhraseQuery](https://python.langchain.com/docs/integrations/retrievers/re_phrase/)

  * [Rebuff](https://python.langchain.com/docs/integrations/providers/rebuff/)

  * [Reddit Search ](https://python.langchain.com/docs/integrations/tools/reddit_search/)

  * [Replicate](https://python.langchain.com/docs/integrations/llms/replicate/)

  * [Run models locally](https://python.langchain.com/docs/how_to/local_llms/)

  * [Runhouse](https://python.langchain.com/docs/integrations/llms/runhouse/)

  * [SAP HANA Cloud Vector Engine](https://python.langchain.com/docs/integrations/vectorstores/sap_hanavector/)

  * [SageMaker Tracking](https://python.langchain.com/docs/integrations/callbacks/sagemaker_tracking/)

  * [SageMakerEndpoint](https://python.langchain.com/docs/integrations/llms/sagemaker/)

  * [Shale Protocol](https://python.langchain.com/docs/integrations/providers/shaleprotocol/)

  * [Solar](https://python.langchain.com/docs/integrations/llms/solar/)

  * [StochasticAI](https://python.langchain.com/docs/integrations/llms/stochasticai/)

  * [TextGen](https://python.langchain.com/docs/integrations/llms/textgen/)

  * [Titan Takeoff](https://python.langchain.com/docs/integrations/llms/titan_takeoff/)

  * [Tongyi Qwen](https://python.langchain.com/docs/integrations/llms/tongyi/)

  * [Volc Engine Maas](https://python.langchain.com/docs/integrations/llms/volcengine_maas/)

  * [Weights & Biases](https://python.langchain.com/docs/integrations/providers/wandb_tracking/)

  * [Writer](https://python.langchain.com/docs/integrations/llms/writer/)

  * [Xorbits Inference \(Xinference\)](https://python.langchain.com/docs/integrations/llms/xinference/)

  * [YandexGPT](https://python.langchain.com/docs/integrations/llms/yandex/)

  * [Zapier Natural Language Actions](https://python.langchain.com/docs/integrations/tools/zapier/)

  * [vLLM](https://python.langchain.com/docs/integrations/llms/vllm/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)