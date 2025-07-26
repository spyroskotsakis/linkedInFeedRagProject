# LogStreamCallbackHandler — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/tracers/langchain_core.tracers.log_stream.LogStreamCallbackHandler.html
**Word Count:** 1350
**Links Count:** 226
**Scraped:** 2025-07-21 07:52:36
**Status:** completed

---

# LogStreamCallbackHandler\#

_class _langchain\_core.tracers.log\_stream.LogStreamCallbackHandler\(

    _\*_ ,     _auto\_close : bool = True_,     _include\_names : Sequence\[str\] | None = None_,     _include\_types : Sequence\[str\] | None = None_,     _include\_tags : Sequence\[str\] | None = None_,     _exclude\_names : Sequence\[str\] | None = None_,     _exclude\_types : Sequence\[str\] | None = None_,     _exclude\_tags : Sequence\[str\] | None = None_,     _\_schema\_format : Literal\['original', 'streaming\_events'\] = 'streaming\_events'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/tracers/log_stream.html#LogStreamCallbackHandler)\#     

Tracer that streams run logs to a stream.

A tracer that streams run logs to a stream.

Parameters:     

  * **auto\_close** \(_bool_\) – Whether to close the stream when the root run finishes.

  * **include\_names** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – Only include runs from Runnables with matching names.

  * **include\_types** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – Only include runs from Runnables with matching types.

  * **include\_tags** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – Only include runs from Runnables with matching tags.

  * **exclude\_names** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – Exclude runs from Runnables with matching names.

  * **exclude\_types** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – Exclude runs from Runnables with matching types.

  * **exclude\_tags** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – Exclude runs from Runnables with matching tags.

  * **\_schema\_format** \(_Literal_ _\[__'original'__,__'streaming\_events'__\]_\) – 

Primarily changes how the inputs and outputs are handled. **For internal use only. This API will change.** \- ‘original’ is the format used by all current tracers.

> This format is slightly inconsistent with respect to inputs and outputs.

    * ’streaming\_events’ is used for supporting streaming events, for internal usage. It will likely change in the future, or be deprecated entirely in favor of a dedicated async tracer for streaming events.

Raises:     

**ValueError** – If an invalid schema format is provided \(internal use only\).

Attributes

`ignore_agent` | Whether to ignore agent callbacks.   ---|---   `ignore_chain` | Whether to ignore chain callbacks.   `ignore_chat_model` | Whether to ignore chat model callbacks.   `ignore_custom_event` | Ignore custom event.   `ignore_llm` | Whether to ignore LLM callbacks.   `ignore_retriever` | Whether to ignore retriever callbacks.   `ignore_retry` | Whether to ignore retry callbacks.   `log_missing_parent` |    `raise_error` | Whether to raise an error if an exception occurs.   `run_inline` | Whether to run the callback inline.      Methods

`__init__`\(\*\[, auto\_close, include\_names, ...\]\) | A tracer that streams run logs to a stream.   ---|---   `include_run`\(run\) | Check if a Run should be included in the log.   `on_agent_action`\(action, \*, run\_id\[, ...\]\) | Run on agent action.   `on_agent_finish`\(finish, \*, run\_id\[, ...\]\) | Run on the agent end.   `on_chain_end`\(outputs, \*, run\_id\[, inputs\]\) | End a trace for a chain run.   `on_chain_error`\(error, \*\[, inputs\]\) | Handle an error for a chain run.   `on_chain_start`\(serialized, inputs, \*, run\_id\) | Start a trace for a chain run.   `on_chat_model_start`\(serialized, messages, \*, ...\) | Start a trace for an LLM run.   `on_custom_event`\(name, data, \*, run\_id\[, ...\]\) | Override to define a handler for a custom event.   `on_llm_end`\(response, \*, run\_id, \*\*kwargs\) | End a trace for an LLM run.   `on_llm_error`\(error, \*, run\_id, \*\*kwargs\) | Handle an error for an LLM run.   `on_llm_new_token`\(token, \*\[, chunk, ...\]\) | Run on new LLM token.   `on_llm_start`\(serialized, prompts, \*, run\_id\) | Start a trace for an LLM run.   `on_retriever_end`\(documents, \*, run\_id, \*\*kwargs\) | Run when the Retriever ends running.   `on_retriever_error`\(error, \*, run\_id, \*\*kwargs\) | Run when Retriever errors.   `on_retriever_start`\(serialized, query, \*, run\_id\) | Run when the Retriever starts running.   `on_retry`\(retry\_state, \*, run\_id, \*\*kwargs\) | Run on retry.   `on_text`\(text, \*, run\_id\[, parent\_run\_id\]\) | Run on an arbitrary text.   `on_tool_end`\(output, \*, run\_id, \*\*kwargs\) | End a trace for a tool run.   `on_tool_error`\(error, \*, run\_id, \*\*kwargs\) | Handle an error for a tool run.   `on_tool_start`\(serialized, input\_str, \*, run\_id\) | Start a trace for a tool run.   `send`\(\*ops\) | Send a patch to the stream, return False if the stream is closed.   `tap_output_aiter`\(run\_id, output\) | Tap an output async iterator to stream its values to the log.   `tap_output_iter`\(run\_id, output\) | Tap an output async iterator to stream its values to the log.      \_\_init\_\_\(

    _\*_ ,     _auto\_close : bool = True_,     _include\_names : Sequence\[str\] | None = None_,     _include\_types : Sequence\[str\] | None = None_,     _include\_tags : Sequence\[str\] | None = None_,     _exclude\_names : Sequence\[str\] | None = None_,     _exclude\_types : Sequence\[str\] | None = None_,     _exclude\_tags : Sequence\[str\] | None = None_,     _\_schema\_format : Literal\['original', 'streaming\_events'\] = 'streaming\_events'_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/tracers/log_stream.html#LogStreamCallbackHandler.__init__)\#     

A tracer that streams run logs to a stream.

Parameters:     

  * **auto\_close** \(_bool_\) – Whether to close the stream when the root run finishes.

  * **include\_names** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – Only include runs from Runnables with matching names.

  * **include\_types** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – Only include runs from Runnables with matching types.

  * **include\_tags** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – Only include runs from Runnables with matching tags.

  * **exclude\_names** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – Exclude runs from Runnables with matching names.

  * **exclude\_types** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – Exclude runs from Runnables with matching types.

  * **exclude\_tags** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – Exclude runs from Runnables with matching tags.

  * **\_schema\_format** \(_Literal_ _\[__'original'__,__'streaming\_events'__\]_\) – 

Primarily changes how the inputs and outputs are handled. **For internal use only. This API will change.** \- ‘original’ is the format used by all current tracers.

> This format is slightly inconsistent with respect to inputs and outputs.

    * ’streaming\_events’ is used for supporting streaming events, for internal usage. It will likely change in the future, or be deprecated entirely in favor of a dedicated async tracer for streaming events.

Raises:     

**ValueError** – If an invalid schema format is provided \(internal use only\).

Return type:     

None

include\_run\(_run : Run_\) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/tracers/log_stream.html#LogStreamCallbackHandler.include_run)\#     

Check if a Run should be included in the log.

Parameters:     

**run** \(_Run_\) – The Run to check.

Returns:     

True if the run should be included, False otherwise.

Return type:     

bool

on\_agent\_action\(

    _action : [AgentAction](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction")_,     _\*_ ,     _run\_id : UUID_,     _parent\_run\_id : UUID | None = None_,     _\*\* kwargs: Any_, \) → Any\#     

Run on agent action.

Parameters:     

  * **action** \([_AgentAction_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction")\) – The agent action.

  * **run\_id** \(_UUID_\) – The run ID. This is the ID of the current run.

  * **parent\_run\_id** \(_UUID_\) – The parent run ID. This is the ID of the parent run.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

Any

on\_agent\_finish\(

    _finish : [AgentFinish](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentFinish.html#langchain_core.agents.AgentFinish "langchain_core.agents.AgentFinish")_,     _\*_ ,     _run\_id : UUID_,     _parent\_run\_id : UUID | None = None_,     _\*\* kwargs: Any_, \) → Any\#     

Run on the agent end.

Parameters:     

  * **finish** \([_AgentFinish_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentFinish.html#langchain_core.agents.AgentFinish "langchain_core.agents.AgentFinish")\) – The agent finish.

  * **run\_id** \(_UUID_\) – The run ID. This is the ID of the current run.

  * **parent\_run\_id** \(_UUID_\) – The parent run ID. This is the ID of the parent run.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

Any

on\_chain\_end\(

    _outputs : dict\[str, Any\]_,     _\*_ ,     _run\_id : UUID_,     _inputs : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → Run\#     

End a trace for a chain run.

Parameters:     

  * **outputs** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The outputs for the chain.

  * **run\_id** \(_UUID_\) – The run ID.

  * **inputs** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\) – The inputs for the chain. Defaults to None.

  * **kwargs** \(_Any_\) – Additional arguments.

Returns:     

The run.

Return type:     

Run

on\_chain\_error\(

    _error : BaseException_,     _\*_ ,     _inputs : dict\[str, Any\] | None = None_,     _run\_id : UUID_,     _\*\* kwargs: Any_, \) → Run\#     

Handle an error for a chain run.

Parameters:     

  * **error** \(_BaseException_\) – The error.

  * **inputs** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\) – The inputs for the chain. Defaults to None.

  * **run\_id** \(_UUID_\) – The run ID.

  * **kwargs** \(_Any_\) – Additional arguments.

Returns:     

The run.

Return type:     

Run

on\_chain\_start\(

    _serialized : dict\[str, Any\]_,     _inputs : dict\[str, Any\]_,     _\*_ ,     _run\_id : UUID_,     _tags : list\[str\] | None = None_,     _parent\_run\_id : UUID | None = None_,     _metadata : dict\[str, Any\] | None = None_,     _run\_type : str | None = None_,     _name : str | None = None_,     _\*\* kwargs: Any_, \) → Run\#     

Start a trace for a chain run.

Parameters:     

  * **serialized** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The serialized chain.

  * **inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The inputs for the chain.

  * **run\_id** \(_UUID_\) – The run ID.

  * **tags** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\) – The tags for the run. Defaults to None.

  * **parent\_run\_id** \(_Optional_ _\[__UUID_ _\]_\) – The parent run ID. Defaults to None.

  * **metadata** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\) – The metadata for the run. Defaults to None.

  * **run\_type** \(_Optional_ _\[__str_ _\]_\) – The type of the run. Defaults to None.

  * **name** \(_Optional_ _\[__str_ _\]_\) – The name of the run.

  * **kwargs** \(_Any_\) – Additional arguments.

Returns:     

The run.

Return type:     

Run

on\_chat\_model\_start\(

    _serialized : dict\[str, Any\]_,     _messages : list\[list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]\]_,     _\*_ ,     _run\_id : UUID_,     _tags : list\[str\] | None = None_,     _parent\_run\_id : UUID | None = None_,     _metadata : dict\[str, Any\] | None = None_,     _name : str | None = None_,     _\*\* kwargs: Any_, \) → Run\#     

Start a trace for an LLM run.

Parameters:     

  * **serialized** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The serialized model.

  * **messages** \(_list_ _\[__list_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]__\]_\) – The messages to start the chat with.

  * **run\_id** \(_UUID_\) – The run ID.

  * **tags** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\) – The tags for the run. Defaults to None.

  * **parent\_run\_id** \(_Optional_ _\[__UUID_ _\]_\) – The parent run ID. Defaults to None.

  * **metadata** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\) – The metadata for the run. Defaults to None.

  * **name** \(_Optional_ _\[__str_ _\]_\) – The name of the run.

  * **kwargs** \(_Any_\) – Additional arguments.

Returns:     

The run.

Return type:     

Run

on\_custom\_event\(

    _name : str_,     _data : Any_,     _\*_ ,     _run\_id : UUID_,     _tags : list\[str\] | None = None_,     _metadata : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → Any\#     

Override to define a handler for a custom event.

Parameters:     

  * **name** \(_str_\) – The name of the custom event.

  * **data** \(_Any_\) – The data for the custom event. Format will match the format specified by the user.

  * **run\_id** \(_UUID_\) – The ID of the run.

  * **tags** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\) – The tags associated with the custom event \(includes inherited tags\).

  * **metadata** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\) – The metadata associated with the custom event \(includes inherited metadata\).

  * **kwargs** \(_Any_\)

Return type:     

Any

Added in version 0.2.15.

on\_llm\_end\(

    _response : [LLMResult](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.llm_result.LLMResult.html#langchain_core.outputs.llm_result.LLMResult "langchain_core.outputs.llm_result.LLMResult")_,     _\*_ ,     _run\_id : UUID_,     _\*\* kwargs: Any_, \) → Run\#     

End a trace for an LLM run.

Parameters:     

  * **response** \([_LLMResult_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.llm_result.LLMResult.html#langchain_core.outputs.llm_result.LLMResult "langchain_core.outputs.llm_result.LLMResult")\) – The response.

  * **run\_id** \(_UUID_\) – The run ID.

  * **kwargs** \(_Any_\) – Additional arguments.

Returns:     

The run.

Return type:     

Run

on\_llm\_error\(

    _error : BaseException_,     _\*_ ,     _run\_id : UUID_,     _\*\* kwargs: Any_, \) → Run\#     

Handle an error for an LLM run.

Parameters:     

  * **error** \(_BaseException_\) – The error.

  * **run\_id** \(_UUID_\) – The run ID.

  * **kwargs** \(_Any_\) – Additional arguments.

Returns:     

The run.

Return type:     

Run

on\_llm\_new\_token\(

    _token : str_,     _\*_ ,     _chunk : [GenerationChunk](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.GenerationChunk.html#langchain_core.outputs.generation.GenerationChunk "langchain_core.outputs.generation.GenerationChunk") | [ChatGenerationChunk](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.chat_generation.ChatGenerationChunk.html#langchain_core.outputs.chat_generation.ChatGenerationChunk "langchain_core.outputs.chat_generation.ChatGenerationChunk") | None = None_,     _run\_id : UUID_,     _parent\_run\_id : UUID | None = None_,     _\*\* kwargs: Any_, \) → Run\#     

Run on new LLM token. Only available when streaming is enabled.

Parameters:     

  * **token** \(_str_\) – The token.

  * **chunk** \(_Optional_ _\[__Union_ _\[_[_GenerationChunk_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.GenerationChunk.html#langchain_core.outputs.generation.GenerationChunk "langchain_core.outputs.generation.GenerationChunk") _,_[_ChatGenerationChunk_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.chat_generation.ChatGenerationChunk.html#langchain_core.outputs.chat_generation.ChatGenerationChunk "langchain_core.outputs.chat_generation.ChatGenerationChunk") _\]__\]_\) – The chunk. Defaults to None.

  * **run\_id** \(_UUID_\) – The run ID.

  * **parent\_run\_id** \(_Optional_ _\[__UUID_ _\]_\) – The parent run ID. Defaults to None.

  * **kwargs** \(_Any_\) – Additional arguments.

Returns:     

The run.

Return type:     

Run

on\_llm\_start\(

    _serialized : dict\[str, Any\]_,     _prompts : list\[str\]_,     _\*_ ,     _run\_id : UUID_,     _tags : list\[str\] | None = None_,     _parent\_run\_id : UUID | None = None_,     _metadata : dict\[str, Any\] | None = None_,     _name : str | None = None_,     _\*\* kwargs: Any_, \) → Run\#     

Start a trace for an LLM run.

Parameters:     

  * **serialized** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The serialized model.

  * **prompts** \(_list_ _\[__str_ _\]_\) – The prompts to start the LLM with.

  * **run\_id** \(_UUID_\) – The run ID.

  * **tags** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\) – The tags for the run. Defaults to None.

  * **parent\_run\_id** \(_Optional_ _\[__UUID_ _\]_\) – The parent run ID. Defaults to None.

  * **metadata** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\) – The metadata for the run. Defaults to None.

  * **name** \(_Optional_ _\[__str_ _\]_\) – The name of the run.

  * **kwargs** \(_Any_\) – Additional arguments.

Returns:     

The run.

Return type:     

Run

on\_retriever\_end\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*_ ,     _run\_id : UUID_,     _\*\* kwargs: Any_, \) → Run\#     

Run when the Retriever ends running.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – The documents.

  * **run\_id** \(_UUID_\) – The run ID.

  * **kwargs** \(_Any_\) – Additional arguments.

Returns:     

The run.

Return type:     

Run

on\_retriever\_error\(

    _error : BaseException_,     _\*_ ,     _run\_id : UUID_,     _\*\* kwargs: Any_, \) → Run\#     

Run when Retriever errors.

Parameters:     

  * **error** \(_BaseException_\) – The error.

  * **run\_id** \(_UUID_\) – The run ID.

  * **kwargs** \(_Any_\) – Additional arguments.

Returns:     

The run.

Return type:     

Run

on\_retriever\_start\(

    _serialized : dict\[str, Any\]_,     _query : str_,     _\*_ ,     _run\_id : UUID_,     _parent\_run\_id : UUID | None = None_,     _tags : list\[str\] | None = None_,     _metadata : dict\[str, Any\] | None = None_,     _name : str | None = None_,     _\*\* kwargs: Any_, \) → Run\#     

Run when the Retriever starts running.

Parameters:     

  * **serialized** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The serialized retriever.

  * **query** \(_str_\) – The query.

  * **run\_id** \(_UUID_\) – The run ID.

  * **parent\_run\_id** \(_Optional_ _\[__UUID_ _\]_\) – The parent run ID. Defaults to None.

  * **tags** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\) – The tags for the run. Defaults to None.

  * **metadata** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\) – The metadata for the run. Defaults to None.

  * **name** \(_Optional_ _\[__str_ _\]_\) – The name of the run.

  * **kwargs** \(_Any_\) – Additional arguments.

Returns:     

The run.

Return type:     

Run

on\_retry\(

    _retry\_state : RetryCallState_,     _\*_ ,     _run\_id : UUID_,     _\*\* kwargs: Any_, \) → Run\#     

Run on retry.

Parameters:     

  * **retry\_state** \(_RetryCallState_\) – The retry state.

  * **run\_id** \(_UUID_\) – The run ID.

  * **kwargs** \(_Any_\) – Additional arguments.

Returns:     

The run.

Return type:     

Run

on\_text\(

    _text : str_,     _\*_ ,     _run\_id : UUID_,     _parent\_run\_id : UUID | None = None_,     _\*\* kwargs: Any_, \) → Any\#     

Run on an arbitrary text.

Parameters:     

  * **text** \(_str_\) – The text.

  * **run\_id** \(_UUID_\) – The run ID. This is the ID of the current run.

  * **parent\_run\_id** \(_UUID_\) – The parent run ID. This is the ID of the parent run.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

Any

on\_tool\_end\(

    _output : Any_,     _\*_ ,     _run\_id : UUID_,     _\*\* kwargs: Any_, \) → Run\#     

End a trace for a tool run.

Parameters:     

  * **output** \(_Any_\) – The output for the tool.

  * **run\_id** \(_UUID_\) – The run ID.

  * **kwargs** \(_Any_\) – Additional arguments.

Returns:     

The run.

Return type:     

Run

on\_tool\_error\(

    _error : BaseException_,     _\*_ ,     _run\_id : UUID_,     _\*\* kwargs: Any_, \) → Run\#     

Handle an error for a tool run.

Parameters:     

  * **error** \(_BaseException_\) – The error.

  * **run\_id** \(_UUID_\) – The run ID.

  * **kwargs** \(_Any_\) – Additional arguments.

Returns:     

The run.

Return type:     

Run

on\_tool\_start\(

    _serialized : dict\[str, Any\]_,     _input\_str : str_,     _\*_ ,     _run\_id : UUID_,     _tags : list\[str\] | None = None_,     _parent\_run\_id : UUID | None = None_,     _metadata : dict\[str, Any\] | None = None_,     _name : str | None = None_,     _inputs : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → Run\#     

Start a trace for a tool run.

Parameters:     

  * **serialized** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The serialized tool.

  * **input\_str** \(_str_\) – The input string.

  * **run\_id** \(_UUID_\) – The run ID.

  * **tags** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\) – The tags for the run. Defaults to None.

  * **parent\_run\_id** \(_Optional_ _\[__UUID_ _\]_\) – The parent run ID. Defaults to None.

  * **metadata** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\) – The metadata for the run. Defaults to None.

  * **name** \(_Optional_ _\[__str_ _\]_\) – The name of the run.

  * **inputs** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\) – The inputs for the tool.

  * **kwargs** \(_Any_\) – Additional arguments.

Returns:     

The run.

Return type:     

Run

send\(

    _\* ops: dict\[str, Any\]_, \) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/tracers/log_stream.html#LogStreamCallbackHandler.send)\#     

Send a patch to the stream, return False if the stream is closed.

Parameters:     

**\*ops** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The operations to send to the stream.

Returns:     

True if the patch was sent successfully, False if the stream     

is closed.

Return type:     

bool

_async _tap\_output\_aiter\(

    _run\_id : UUID_,     _output : AsyncIterator\[T\]_, \) → AsyncIterator\[T\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/tracers/log_stream.html#LogStreamCallbackHandler.tap_output_aiter)\#     

Tap an output async iterator to stream its values to the log.

Parameters:     

  * **run\_id** \(_UUID_\) – The ID of the run.

  * **output** \(_AsyncIterator_ _\[__T_ _\]_\) – The output async iterator.

Yields:     

_T_ – The output value.

Return type:     

AsyncIterator\[T\]

tap\_output\_iter\(

    _run\_id : UUID_,     _output : Iterator\[T\]_, \) → Iterator\[T\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/tracers/log_stream.html#LogStreamCallbackHandler.tap_output_iter)\#     

Tap an output async iterator to stream its values to the log.

Parameters:     

  * **run\_id** \(_UUID_\) – The ID of the run.

  * **output** \(_Iterator_ _\[__T_ _\]_\) – The output iterator.

Yields:     

_T_ – The output value.

Return type:     

Iterator\[T\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)