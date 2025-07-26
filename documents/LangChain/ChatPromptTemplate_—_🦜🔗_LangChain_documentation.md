# ChatPromptTemplate — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html
**Word Count:** 3127
**Links Count:** 481
**Scraped:** 2025-07-21 07:56:25
**Status:** completed

---

# ChatPromptTemplate\#

_class _langchain\_core.prompts.chat.ChatPromptTemplate[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompts/chat.html#ChatPromptTemplate)\#     

Bases: [`BaseChatPromptTemplate`](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.BaseChatPromptTemplate.html#langchain_core.prompts.chat.BaseChatPromptTemplate "langchain_core.prompts.chat.BaseChatPromptTemplate")

Prompt template for chat models.

Use to create flexible templated prompts for chat models.

Examples

Changed in version 0.2.24: You can pass any Message-like formats supported by `ChatPromptTemplate.from_messages()` directly to `ChatPromptTemplate()` init.               from langchain_core.prompts import ChatPromptTemplate          template = ChatPromptTemplate([         ("system", "You are a helpful AI bot. Your name is {name}."),         ("human", "Hello, how are you doing?"),         ("ai", "I'm doing well, thanks!"),         ("human", "{user_input}"),     ])          prompt_value = template.invoke(         {             "name": "Bob",             "user_input": "What is your name?"         }     )     # Output:     # ChatPromptValue(     #    messages=[     #        SystemMessage(content='You are a helpful AI bot. Your name is Bob.'),     #        HumanMessage(content='Hello, how are you doing?'),     #        AIMessage(content="I'm doing well, thanks!"),     #        HumanMessage(content='What is your name?')     #    ]     #)     

Messages Placeholder:

>  >     # In addition to Human/AI/Tool/Function messages, >     # you can initialize the template with a MessagesPlaceholder >     # either using the class directly or with the shorthand tuple syntax: >      >     template = ChatPromptTemplate([ >         ("system", "You are a helpful AI bot."), >         # Means the template will receive an optional list of messages under >         # the "conversation" key >         ("placeholder", "{conversation}") >         # Equivalently: >         # MessagesPlaceholder(variable_name="conversation", optional=True) >     ]) >      >     prompt_value = template.invoke( >         { >             "conversation": [ >                 ("human", "Hi!"), >                 ("ai", "How can I assist you today?"), >                 ("human", "Can you make me an ice cream sundae?"), >                 ("ai", "No.") >             ] >         } >     ) >      >     # Output: >     # ChatPromptValue( >     #    messages=[ >     #        SystemMessage(content='You are a helpful AI bot.'), >     #        HumanMessage(content='Hi!'), >     #        AIMessage(content='How can I assist you today?'), >     #        HumanMessage(content='Can you make me an ice cream sundae?'), >     #        AIMessage(content='No.'), >     #    ] >     #) >     

Single-variable template:

> If your prompt has only a single input variable \(i.e., 1 instance of “\{variable\_nams\}”\), and you invoke the template with a non-dict object, the prompt template will inject the provided argument into that variable location. >      >      >     from langchain_core.prompts import ChatPromptTemplate >      >     template = ChatPromptTemplate([ >         ("system", "You are a helpful AI bot. Your name is Carl."), >         ("human", "{user_input}"), >     ]) >      >     prompt_value = template.invoke("Hello, there!") >     # Equivalent to >     # prompt_value = template.invoke({"user_input": "Hello, there!"}) >      >     # Output: >     #  ChatPromptValue( >     #     messages=[ >     #         SystemMessage(content='You are a helpful AI bot. Your name is Carl.'), >     #         HumanMessage(content='Hello, there!'), >     #     ] >     # ) >     

Create a chat prompt template from a variety of message formats.

Parameters:     

  * **messages** – sequence of message representations. A message can be represented using the following formats: \(1\) BaseMessagePromptTemplate, \(2\) BaseMessage, \(3\) 2-tuple of \(message type, template\); e.g., \(“human”, “\{user\_input\}”\), \(4\) 2-tuple of \(message class, template\), \(5\) a string which is shorthand for \(“human”, template\); e.g., “\{user\_input\}”.

  * **template\_format** – format of the template. Defaults to “f-string”.

  * **input\_variables** – A list of the names of the variables whose values are required as inputs to the prompt.

  * **optional\_variables** – A list of the names of the variables for placeholder or MessagePlaceholder that are optional. These variables are auto inferred from the prompt and user need not provide them.

  * **partial\_variables** – A dictionary of the partial variables the prompt template carries. Partial variables populate the template so that you don’t need to pass them in every time you call the prompt.

  * **validate\_template** – Whether to validate the template.

  * **input\_types** – A dictionary of the types of the variables the prompt template expects. If not provided, all variables are assumed to be strings.

Returns:     

A chat prompt template.

Examples

Instantiation from a list of message templates:               template = ChatPromptTemplate([         ("human", "Hello, how are you?"),         ("ai", "I'm doing well, thanks!"),         ("human", "That's good to hear."),     ])     

Instantiation from mixed message formats:               template = ChatPromptTemplate([         SystemMessage(content="hello"),         ("human", "Hello, how are you?"),     ])     

Note

ChatPromptTemplate implements the standard [`Runnable Interface`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable"). 🏃

The [`Runnable Interface`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") has additional methods that are available on runnables, such as [`with_config`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.with_config "langchain_core.runnables.base.Runnable.with_config"), [`with_types`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.with_types "langchain_core.runnables.base.Runnable.with_types"), [`with_retry`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.with_retry "langchain_core.runnables.base.Runnable.with_retry"), [`assign`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.assign "langchain_core.runnables.base.Runnable.assign"), [`bind`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.bind "langchain_core.runnables.base.Runnable.bind"), [`get_graph`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.get_graph "langchain_core.runnables.base.Runnable.get_graph"), and more.

_param _input\_types _: Dict\[str, Any\]__\[Optional\]_\#     

A dictionary of the types of the variables the prompt template expects. If not provided, all variables are assumed to be strings.

_param _input\_variables _: list\[str\]__\[Required\]_\#     

A list of the names of the variables whose values are required as inputs to the prompt.

_param _messages _: Annotated\[list\[MessageLike\], SkipValidation\(\)\]__\[Required\]_\#     

List of messages consisting of either message prompt templates or messages.

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

_param _validate\_template _: bool_ _ = False_\#     

Whether or not to try validating the template.

_classmethod _from\_messages\(

    _messages : Sequence\[MessageLikeRepresentation\]_,     _template\_format : PromptTemplateFormat = 'f-string'_, \) → ChatPromptTemplate[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompts/chat.html#ChatPromptTemplate.from_messages)\#     

Create a chat prompt template from a variety of message formats.

Examples

Instantiation from a list of message templates:               template = ChatPromptTemplate.from_messages([         ("human", "Hello, how are you?"),         ("ai", "I'm doing well, thanks!"),         ("human", "That's good to hear."),     ])     

Instantiation from mixed message formats:               template = ChatPromptTemplate.from_messages([         SystemMessage(content="hello"),         ("human", "Hello, how are you?"),     ])     

Parameters:     

  * **messages** \(_Sequence_ _\[__MessageLikeRepresentation_ _\]_\) – sequence of message representations. A message can be represented using the following formats: \(1\) BaseMessagePromptTemplate, \(2\) BaseMessage, \(3\) 2-tuple of \(message type, template\); e.g., \(“human”, “\{user\_input\}”\), \(4\) 2-tuple of \(message class, template\), \(5\) a string which is shorthand for \(“human”, template\); e.g., “\{user\_input\}”.

  * **template\_format** \(_PromptTemplateFormat_\) – format of the template. Defaults to “f-string”.

Returns:     

a chat prompt template.

Return type:     

ChatPromptTemplate

_classmethod _from\_role\_strings\(

    _string\_messages : list\[tuple\[str, str\]\]_, \) → ChatPromptTemplate[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompts/chat.html#ChatPromptTemplate.from_role_strings)\#     

Deprecated since version 0.0.1: Use `from_messages()` instead.

Create a chat prompt template from a list of \(role, template\) tuples.

Parameters:     

**string\_messages** \(_list_ _\[__tuple_ _\[__str_ _,__str_ _\]__\]_\) – list of \(role, template\) tuples.

Returns:     

a chat prompt template.

Return type:     

_ChatPromptTemplate_

_classmethod _from\_strings\(

    _string\_messages : list\[tuple\[type\[[BaseMessagePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.message.BaseMessagePromptTemplate.html#langchain_core.prompts.message.BaseMessagePromptTemplate "langchain_core.prompts.message.BaseMessagePromptTemplate")\], str\]\]_, \) → ChatPromptTemplate[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompts/chat.html#ChatPromptTemplate.from_strings)\#     

Deprecated since version 0.0.1: Use `from_messages()` instead.

Create a chat prompt template from a list of \(role class, template\) tuples.

Parameters:     

**string\_messages** \(_list_ _\[__tuple_ _\[__type_ _\[_[_BaseMessagePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.message.BaseMessagePromptTemplate.html#langchain_core.prompts.message.BaseMessagePromptTemplate "langchain_core.prompts.message.BaseMessagePromptTemplate") _\]__,__str_ _\]__\]_\) – list of \(role class, template\) tuples.

Returns:     

a chat prompt template.

Return type:     

_ChatPromptTemplate_

_classmethod _from\_template\(

    _template : str_,     _\*\* kwargs: Any_, \) → ChatPromptTemplate[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompts/chat.html#ChatPromptTemplate.from_template)\#     

Create a chat prompt template from a template string.

Creates a chat template consisting of a single message assumed to be from the human.

Parameters:     

  * **template** \(_str_\) – template string

  * **\*\*kwargs** \(_Any_\) – keyword arguments to pass to the constructor.

Returns:     

A new instance of this class.

Return type:     

_ChatPromptTemplate_

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

_async _aformat\(_\*\* kwargs: Any_\) → str\#     

Async format the chat template into a string.

Parameters:     

**\*\*kwargs** \(_Any_\) – keyword arguments to use for filling in template variables in all the template messages in this chat template.

Returns:     

formatted string.

Return type:     

str

_async _aformat\_messages\(

    _\*\* kwargs: Any_, \) → list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompts/chat.html#ChatPromptTemplate.aformat_messages)\#     

Async format the chat template into a list of finalized messages.

Parameters:     

**\*\*kwargs** \(_Any_\) – keyword arguments to use for filling in template variables in all the template messages in this chat template.

Returns:     

list of formatted messages.

Raises:     

**ValueError** – If unexpected input.

Return type:     

list\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

_async _aformat\_prompt\(

    _\*\* kwargs: Any_, \) → [ChatPromptValue](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.ChatPromptValue.html#langchain_core.prompt_values.ChatPromptValue "langchain_core.prompt_values.ChatPromptValue")\#     

Async format prompt. Should return a ChatPromptValue.

Parameters:     

**\*\*kwargs** \(_Any_\) – Keyword arguments to use for formatting.

Returns:     

PromptValue.

Return type:     

[_ChatPromptValue_](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.ChatPromptValue.html#langchain_core.prompt_values.ChatPromptValue "langchain_core.prompt_values.ChatPromptValue")

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

append\(

    _message : [BaseMessagePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.message.BaseMessagePromptTemplate.html#langchain_core.prompts.message.BaseMessagePromptTemplate "langchain_core.prompts.message.BaseMessagePromptTemplate") | [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") | [BaseChatPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.BaseChatPromptTemplate.html#langchain_core.prompts.chat.BaseChatPromptTemplate "langchain_core.prompts.chat.BaseChatPromptTemplate") | tuple\[str | type, str | list\[dict\] | list\[object\]\] | str | dict\[str, Any\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompts/chat.html#ChatPromptTemplate.append)\#     

Append a message to the end of the chat template.

Parameters:     

**message** \([_BaseMessagePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.message.BaseMessagePromptTemplate.html#langchain_core.prompts.message.BaseMessagePromptTemplate "langchain_core.prompts.message.BaseMessagePromptTemplate") _|_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _|_[_BaseChatPromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.BaseChatPromptTemplate.html#langchain_core.prompts.chat.BaseChatPromptTemplate "langchain_core.prompts.chat.BaseChatPromptTemplate") _|__tuple_ _\[__str_ _|__type_ _,__str_ _|__list_ _\[__dict_ _\]__|__list_ _\[__object_ _\]__\]__|__str_ _|__dict_ _\[__str_ _,__Any_ _\]_\) – representation of a message to append.

Return type:     

None

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

extend\(

    _messages : Sequence\[MessageLikeRepresentation\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompts/chat.html#ChatPromptTemplate.extend)\#     

Extend the chat template with a sequence of messages.

Parameters:     

**messages** \(_Sequence_ _\[__MessageLikeRepresentation_ _\]_\) – sequence of message representations to append.

Return type:     

None

format\(_\*\* kwargs: Any_\) → str\#     

Format the chat template into a string.

Parameters:     

**\*\*kwargs** \(_Any_\) – keyword arguments to use for filling in template variables in all the template messages in this chat template.

Returns:     

formatted string.

Return type:     

str

format\_messages\(

    _\*\* kwargs: Any_, \) → list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompts/chat.html#ChatPromptTemplate.format_messages)\#     

Format the chat template into a list of finalized messages.

Parameters:     

**\*\*kwargs** \(_Any_\) – keyword arguments to use for filling in template variables in all the template messages in this chat template.

Returns:     

list of formatted messages.

Return type:     

list\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

format\_prompt\(

    _\*\* kwargs: Any_, \) → [ChatPromptValue](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.ChatPromptValue.html#langchain_core.prompt_values.ChatPromptValue "langchain_core.prompt_values.ChatPromptValue")\#     

Format prompt. Should return a ChatPromptValue.

Parameters:     

**\*\*kwargs** \(_Any_\) – Keyword arguments to use for formatting.

Returns:     

ChatPromptValue.

Return type:     

[_ChatPromptValue_](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.ChatPromptValue.html#langchain_core.prompt_values.ChatPromptValue "langchain_core.prompt_values.ChatPromptValue")

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

    _\*\* kwargs: Any_, \) → ChatPromptTemplate[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompts/chat.html#ChatPromptTemplate.partial)\#     

Get a new ChatPromptTemplate with some input variables already filled in.

Parameters:     

**\*\*kwargs** \(_Any_\) – keyword arguments to use for filling in template variables. Ought to be a subset of the input variables.

Returns:     

A new ChatPromptTemplate.

Return type:     

_ChatPromptTemplate_

Example               from langchain_core.prompts import ChatPromptTemplate          template = ChatPromptTemplate.from_messages(         [             ("system", "You are an AI assistant named {name}."),             ("human", "Hi I'm {user}"),             ("ai", "Hi there, {user}, I'm {name}."),             ("human", "{input}"),         ]     )     template2 = template.partial(user="Lucy", name="R2D2")          template2.format_messages(input="hello")     

pretty\_print\(\) → None\#     

Print a human-readable representation.

Return type:     

None

pretty\_repr\(_html : bool = False_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompts/chat.html#ChatPromptTemplate.pretty_repr)\#     

Human-readable representation.

Parameters:     

**html** \(_bool_\) – Whether to format as HTML. Defaults to False.

Returns:     

Human-readable representation.

Return type:     

str

save\(

    _file\_path : Path | str_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompts/chat.html#ChatPromptTemplate.save)\#     

Save prompt to file.

Parameters:     

**file\_path** \(_Path_ _|__str_\) – path to file.

Return type:     

None

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

Examples using ChatPromptTemplate

  * [\# Basic example \(short documents\)](https://python.langchain.com/docs/versions/migrating_chains/map_reduce_chain/)

  * [\# Example](https://python.langchain.com/docs/versions/migrating_chains/map_rerank_docs_chain/)

  * [\# Legacy](https://python.langchain.com/docs/versions/migrating_chains/llm_router_chain/)

  * [AWS DynamoDB](https://python.langchain.com/docs/integrations/memory/aws_dynamodb/)

  * [Activeloop Deep Memory](https://python.langchain.com/docs/integrations/retrievers/activeloop/)

  * [Apache Cassandra](https://python.langchain.com/docs/integrations/vectorstores/cassandra/)

  * [ApertureDB](https://python.langchain.com/docs/integrations/vectorstores/aperturedb/)

  * [ArxivRetriever](https://python.langchain.com/docs/integrations/retrievers/arxiv/)

  * [AskNews](https://python.langchain.com/docs/integrations/retrievers/asknews/)

  * [AzureAISearchRetriever](https://python.langchain.com/docs/integrations/retrievers/azure_ai_search/)

  * [AzureChatOpenAI](https://python.langchain.com/docs/integrations/chat/azure_chat_openai/)

  * [Build a Chatbot](https://python.langchain.com/docs/tutorials/chatbot/)

  * [Build a Local RAG Application](https://python.langchain.com/docs/tutorials/local_rag/)

  * [Build a PDF ingestion and Question/Answering system](https://python.langchain.com/docs/tutorials/pdf_qa/)

  * [Build a Query Analysis System](https://python.langchain.com/docs/tutorials/query_analysis/)

  * [Build a Retrieval Augmented Generation \(RAG\) App](https://python.langchain.com/docs/tutorials/rag/)

  * [Build a Simple LLM Application with LCEL](https://python.langchain.com/docs/tutorials/llm_chain/)

  * [Build an Extraction Chain](https://python.langchain.com/docs/tutorials/extraction/)

  * [ChatAI21](https://python.langchain.com/docs/integrations/chat/ai21/)

  * [ChatAnthropic](https://python.langchain.com/docs/integrations/chat/anthropic/)

  * [ChatBedrock](https://python.langchain.com/docs/integrations/chat/bedrock/)

  * [ChatDatabricks](https://python.langchain.com/docs/integrations/chat/databricks/)

  * [ChatFireworks](https://python.langchain.com/docs/integrations/chat/fireworks/)

  * [ChatGoogleGenerativeAI](https://python.langchain.com/docs/integrations/chat/google_generative_ai/)

  * [ChatGroq](https://python.langchain.com/docs/integrations/chat/groq/)

  * [ChatMistralAI](https://python.langchain.com/docs/integrations/chat/mistralai/)

  * [ChatNVIDIA](https://python.langchain.com/docs/integrations/chat/nvidia_ai_endpoints/)

  * [ChatOCIGenAI](https://python.langchain.com/docs/integrations/chat/oci_generative_ai/)

  * [ChatOllama](https://python.langchain.com/docs/integrations/chat/ollama/)

  * [ChatOpenAI](https://python.langchain.com/docs/integrations/chat/openai/)

  * [ChatPerplexity](https://python.langchain.com/docs/integrations/chat/perplexity/)

  * [ChatTogether](https://python.langchain.com/docs/integrations/chat/together/)

  * [ChatUpstage](https://python.langchain.com/docs/integrations/chat/upstage/)

  * [ChatVertexAI](https://python.langchain.com/docs/integrations/chat/google_vertex_ai_palm/)

  * [ChatWatsonx](https://python.langchain.com/docs/integrations/chat/ibm_watsonx/)

  * [ChatYI](https://python.langchain.com/docs/integrations/chat/yi/)

  * [Classify Text into Labels](https://python.langchain.com/docs/tutorials/classification/)

  * [Cohere](https://python.langchain.com/docs/integrations/providers/cohere/)

  * [Conceptual guide](https://python.langchain.com/docs/concepts/)

  * [Context](https://python.langchain.com/docs/integrations/callbacks/context/)

  * [Conversational RAG](https://python.langchain.com/docs/tutorials/qa_chat_history/)

  * [Couchbase](https://python.langchain.com/docs/integrations/memory/couchbase_chat_message_history/)

  * [Databricks Unity Catalog \(UC\)](https://python.langchain.com/docs/integrations/tools/databricks/)

  * [Eden AI](https://python.langchain.com/docs/integrations/chat/edenai/)

  * [ElasticsearchRetriever](https://python.langchain.com/docs/integrations/retrievers/elasticsearch_retriever/)

  * [Facebook Messenger](https://python.langchain.com/docs/integrations/chat_loaders/facebook/)

  * [Fiddler](https://python.langchain.com/docs/integrations/callbacks/fiddler/)

  * [Figma](https://python.langchain.com/docs/integrations/document_loaders/figma/)

  * [FinancialDatasets Toolkit](https://python.langchain.com/docs/integrations/tools/financial_datasets/)

  * [Fleet AI Context](https://python.langchain.com/docs/integrations/retrievers/fleet_context/)

  * [Google AlloyDB for PostgreSQL](https://python.langchain.com/docs/integrations/memory/google_alloydb/)

  * [Google El Carro Oracle](https://python.langchain.com/docs/integrations/memory/google_el_carro/)

  * [Google SQL for MySQL](https://python.langchain.com/docs/integrations/memory/google_sql_mysql/)

  * [Google SQL for PostgreSQL](https://python.langchain.com/docs/integrations/memory/google_sql_pg/)

  * [Google SQL for SQL Server](https://python.langchain.com/docs/integrations/memory/google_sql_mssql/)

  * [Google Vertex AI Search](https://python.langchain.com/docs/integrations/retrievers/google_vertex_ai_search/)

  * [How deal with high cardinality categoricals when doing query analysis](https://python.langchain.com/docs/how_to/query_high_cardinality/)

  * [How to add a semantic layer over graph database](https://python.langchain.com/docs/how_to/graph_semantic/)

  * [How to add ad-hoc tool calling capability to LLMs and Chat Models](https://python.langchain.com/docs/how_to/tools_prompting/)

  * [How to add chat history](https://python.langchain.com/docs/how_to/qa_chat_history_how_to/)

  * [How to add default invocation args to a Runnable](https://python.langchain.com/docs/how_to/binding/)

  * [How to add examples to the prompt for query analysis](https://python.langchain.com/docs/how_to/query_few_shot/)

  * [How to add fallbacks to a runnable](https://python.langchain.com/docs/how_to/fallbacks/)

  * [How to add memory to chatbots](https://python.langchain.com/docs/how_to/chatbots_memory/)

  * [How to add message history](https://python.langchain.com/docs/how_to/message_history/)

  * [How to add retrieval to chatbots](https://python.langchain.com/docs/how_to/chatbots_retrieval/)

  * [How to add tools to chatbots](https://python.langchain.com/docs/how_to/chatbots_tools/)

  * [How to add values to a chain’s state](https://python.langchain.com/docs/how_to/assign/)

  * [How to attach callbacks to a runnable](https://python.langchain.com/docs/how_to/callbacks_attach/)

  * [How to chain runnables](https://python.langchain.com/docs/how_to/sequence/)

  * [How to convert Runnables as Tools](https://python.langchain.com/docs/how_to/convert_runnable_to_tool/)

  * [How to create a custom LLM class](https://python.langchain.com/docs/how_to/custom_llm/)

  * [How to create a dynamic \(self-constructing\) chain](https://python.langchain.com/docs/how_to/dynamic_chain/)

  * [How to create custom callback handlers](https://python.langchain.com/docs/how_to/custom_callbacks/)

  * [How to create tools](https://python.langchain.com/docs/how_to/custom_tools/)

  * [How to deal with large databases when doing SQL question-answering](https://python.langchain.com/docs/how_to/sql_large_db/)

  * [How to debug your LLM apps](https://python.langchain.com/docs/how_to/debugging/)

  * [How to do per-user retrieval](https://python.langchain.com/docs/how_to/qa_per_user/)

  * [How to do query validation as part of SQL question-answering](https://python.langchain.com/docs/how_to/sql_query_checking/)

  * [How to do question answering over CSVs](https://python.langchain.com/docs/how_to/sql_csv/)

  * [How to do tool/function calling](https://python.langchain.com/docs/how_to/function_calling/)

  * [How to get a RAG application to add citations](https://python.langchain.com/docs/how_to/qa_citations/)

  * [How to get your RAG application to return sources](https://python.langchain.com/docs/how_to/qa_sources/)

  * [How to handle cases where no queries are generated](https://python.langchain.com/docs/how_to/query_no_queries/)

  * [How to handle long text when doing extraction](https://python.langchain.com/docs/how_to/extraction_long_text/)

  * [How to handle multiple queries when doing query analysis](https://python.langchain.com/docs/how_to/query_multiple_queries/)

  * [How to handle multiple retrievers when doing query analysis](https://python.langchain.com/docs/how_to/query_multiple_retrievers/)

  * [How to handle tool errors](https://python.langchain.com/docs/how_to/tools_error/)

  * [How to inspect runnables](https://python.langchain.com/docs/how_to/inspect/)

  * [How to invoke runnables in parallel](https://python.langchain.com/docs/how_to/parallel/)

  * [How to map values to a graph database](https://python.langchain.com/docs/how_to/graph_mapping/)

  * [How to migrate from legacy LangChain agents to LangGraph](https://python.langchain.com/docs/how_to/migrate_agent/)

  * [How to pass callbacks in at runtime](https://python.langchain.com/docs/how_to/callbacks_runtime/)

  * [How to pass through arguments from one step to the next](https://python.langchain.com/docs/how_to/passthrough/)

  * [How to propagate callbacks constructor](https://python.langchain.com/docs/how_to/callbacks_constructor/)

  * [How to retrieve using multiple vectors per document](https://python.langchain.com/docs/how_to/multi_vector/)

  * [How to return structured data from a model](https://python.langchain.com/docs/how_to/structured_output/)

  * [How to run custom functions](https://python.langchain.com/docs/how_to/functions/)

  * [How to save and load LangChain objects](https://python.langchain.com/docs/how_to/serialization/)

  * [How to stream events from a tool](https://python.langchain.com/docs/how_to/tool_stream_events/)

  * [How to stream results from your RAG application](https://python.langchain.com/docs/how_to/qa_streaming/)

  * [How to stream runnables](https://python.langchain.com/docs/how_to/streaming/)

  * [How to summarize text in a single LLM call](https://python.langchain.com/docs/how_to/summarize_stuff/)

  * [How to summarize text through iterative refinement](https://python.langchain.com/docs/how_to/summarize_refine/)

  * [How to summarize text through parallelization](https://python.langchain.com/docs/how_to/summarize_map_reduce/)

  * [How to track token usage in ChatModels](https://python.langchain.com/docs/how_to/chat_token_usage_tracking/)

  * [How to use few shot examples in chat models](https://python.langchain.com/docs/how_to/few_shot_examples_chat/)

  * [How to use few-shot prompting with tool calling](https://python.langchain.com/docs/how_to/tools_few_shot/)

  * [How to use multimodal prompts](https://python.langchain.com/docs/how_to/multimodal_prompts/)

  * [How to use prompting alone \(no tool calling\) to do extraction](https://python.langchain.com/docs/how_to/extraction_parse/)

  * [How to use reference examples when doing extraction](https://python.langchain.com/docs/how_to/extraction_examples/)

  * [Hybrid Search](https://python.langchain.com/docs/how_to/hybrid/)

  * [Image captions](https://python.langchain.com/docs/integrations/document_loaders/image_captions/)

  * [Jaguar Vector Database](https://python.langchain.com/docs/integrations/vectorstores/jaguar/)

  * [JinaChat](https://python.langchain.com/docs/integrations/chat/jinachat/)

  * [Kinetica Language To SQL Chat Model](https://python.langchain.com/docs/integrations/chat/kinetica/)

  * [LangChain Expression Language Cheatsheet](https://python.langchain.com/docs/how_to/lcel_cheatsheet/)

  * [LangSmith LLM Runs](https://python.langchain.com/docs/integrations/chat_loaders/langsmith_llm_runs/)

  * [Llama.cpp](https://python.langchain.com/docs/integrations/chat/llamacpp/)

  * [Llama2Chat](https://python.langchain.com/docs/integrations/chat/llama2_chat/)

  * [Load docs](https://python.langchain.com/docs/versions/migrating_chains/conversation_retrieval_chain/)

  * [MLflow](https://python.langchain.com/docs/integrations/providers/mlflow_tracking/)

  * [Maritalk](https://python.langchain.com/docs/integrations/chat/maritalk/)

  * [MongoDB](https://python.langchain.com/docs/integrations/memory/mongodb_chat_message_history/)

  * [NVIDIA NIMs ](https://python.langchain.com/docs/integrations/text_embedding/nvidia_ai_endpoints/)

  * [OllamaFunctions](https://python.langchain.com/docs/integrations/chat/ollama_functions/)

  * [OllamaLLM](https://python.langchain.com/docs/integrations/llms/ollama/)

  * [OpenAI metadata tagger](https://python.langchain.com/docs/integrations/document_transformers/openai_metadata_tagger/)

  * [RAGatouille](https://python.langchain.com/docs/integrations/retrievers/ragatouille/)

  * [Redis](https://python.langchain.com/docs/integrations/memory/redis_chat_message_history/)

  * [Riza Code Interpreter](https://python.langchain.com/docs/integrations/tools/riza/)

  * [SQL \(SQLAlchemy\)](https://python.langchain.com/docs/integrations/memory/sql_chat_message_history/)

  * [SQLite](https://python.langchain.com/docs/integrations/memory/sqlite/)

  * [Streamlit](https://python.langchain.com/docs/integrations/memory/streamlit_chat_message_history/)

  * [Summarize Text](https://python.langchain.com/docs/tutorials/summarization/)

  * [Tavily Search](https://python.langchain.com/docs/integrations/tools/tavily_search/)

  * [TavilySearchAPIRetriever](https://python.langchain.com/docs/integrations/retrievers/tavily/)

  * [TiDB](https://python.langchain.com/docs/integrations/memory/tidb_chat_message_history/)

  * [UpTrain](https://python.langchain.com/docs/integrations/callbacks/uptrain/)

  * [Vector stores and retrievers](https://python.langchain.com/docs/tutorials/retrievers/)

  * [Weaviate](https://python.langchain.com/docs/integrations/vectorstores/weaviate/)

  * [WikipediaRetriever](https://python.langchain.com/docs/integrations/retrievers/wikipedia/)

  * [Yellowbrick](https://python.langchain.com/docs/integrations/vectorstores/yellowbrick/)

  * [You.com](https://python.langchain.com/docs/integrations/retrievers/you-retriever/)

  * [Yuan2.0](https://python.langchain.com/docs/integrations/chat/yuan2/)

  * [ZepCloudChatMessageHistory](https://python.langchain.com/docs/integrations/memory/zep_cloud_chat_message_history/)

  * [iMessage](https://python.langchain.com/docs/integrations/chat_loaders/imessage/)

  * [vLLM Chat](https://python.langchain.com/docs/integrations/chat/vllm/)

  * [🦜️🏓 LangServe](https://python.langchain.com/docs/langserve/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)