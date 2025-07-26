# LoggingCallbackHandler — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/callbacks/langchain.callbacks.tracers.logging.LoggingCallbackHandler.html
**Word Count:** 968
**Links Count:** 169
**Scraped:** 2025-07-21 07:51:39
**Status:** completed

---

# LoggingCallbackHandler\#

_class _langchain.callbacks.tracers.logging.LoggingCallbackHandler\(

    _logger : Logger_,     _log\_level : int = 20_,     _extra : dict | None = None_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/callbacks/tracers/logging.html#LoggingCallbackHandler)\#     

Tracer that logs via the input Logger.

Create a FunctionCallbackHandler.

Parameters:     

  * **function** – The callback function to call.

  * **logger** \(_Logger_\)

  * **log\_level** \(_int_\)

  * **extra** \(_dict_ _|__None_\)

  * **kwargs** \(_Any_\)

Attributes

`ignore_agent` | Whether to ignore agent callbacks.   ---|---   `ignore_chain` | Whether to ignore chain callbacks.   `ignore_chat_model` | Whether to ignore chat model callbacks.   `ignore_custom_event` | Ignore custom event.   `ignore_llm` | Whether to ignore LLM callbacks.   `ignore_retriever` | Whether to ignore retriever callbacks.   `ignore_retry` | Whether to ignore retry callbacks.   `log_missing_parent` |    `name` | The name of the tracer.   `raise_error` | Whether to raise an error if an exception occurs.   `run_inline` | Whether to run the callback inline.      Methods

`__init__`\(logger\[, log\_level, extra\]\) | Create a FunctionCallbackHandler.   ---|---   `get_breadcrumbs`\(run\) | Get the breadcrumbs of a run.   `get_parents`\(run\) | Get the parents of a run.   `on_agent_action`\(action, \*, run\_id\[, ...\]\) | Run on agent action.   `on_agent_finish`\(finish, \*, run\_id\[, ...\]\) | Run on the agent end.   `on_chain_end`\(outputs, \*, run\_id\[, inputs\]\) | End a trace for a chain run.   `on_chain_error`\(error, \*\[, inputs\]\) | Handle an error for a chain run.   `on_chain_start`\(serialized, inputs, \*, run\_id\) | Start a trace for a chain run.   `on_chat_model_start`\(serialized, messages, \*, ...\) | Start a trace for an LLM run.   `on_custom_event`\(name, data, \*, run\_id\[, ...\]\) | Override to define a handler for a custom event.   `on_llm_end`\(response, \*, run\_id, \*\*kwargs\) | End a trace for an LLM run.   `on_llm_error`\(error, \*, run\_id, \*\*kwargs\) | Handle an error for an LLM run.   `on_llm_new_token`\(token, \*\[, chunk, ...\]\) | Run on new LLM token.   `on_llm_start`\(serialized, prompts, \*, run\_id\) | Start a trace for an LLM run.   `on_retriever_end`\(documents, \*, run\_id, \*\*kwargs\) | Run when the Retriever ends running.   `on_retriever_error`\(error, \*, run\_id, \*\*kwargs\) | Run when Retriever errors.   `on_retriever_start`\(serialized, query, \*, run\_id\) | Run when the Retriever starts running.   `on_retry`\(retry\_state, \*, run\_id, \*\*kwargs\) | Run on retry.   `on_text`\(text, \*, run\_id\[, parent\_run\_id\]\) | Run on an arbitrary text.   `on_tool_end`\(output, \*, run\_id, \*\*kwargs\) | End a trace for a tool run.   `on_tool_error`\(error, \*, run\_id, \*\*kwargs\) | Handle an error for a tool run.   `on_tool_start`\(serialized, input\_str, \*, run\_id\) | Start a trace for a tool run.      \_\_init\_\_\(

    _logger : Logger_,     _log\_level : int = 20_,     _extra : dict | None = None_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/callbacks/tracers/logging.html#LoggingCallbackHandler.__init__)\#     

Create a FunctionCallbackHandler.

Parameters:     

  * **function** – The callback function to call.

  * **logger** \(_Logger_\)

  * **log\_level** \(_int_\)

  * **extra** \(_dict_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

None

get\_breadcrumbs\(

    _run : RunTree_, \) → str\#     

Get the breadcrumbs of a run.

Parameters:     

**run** \(_RunTree_\) – The run to get the breadcrumbs of.

Returns:     

A string with the breadcrumbs of the run.

Return type:     

str

get\_parents\(

    _run : RunTree_, \) → list\[RunTree\]\#     

Get the parents of a run.

Parameters:     

**run** \(_RunTree_\) – The run to get the parents of.

Returns:     

A list of parent runs.

Return type:     

list\[_RunTree_\]

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

    _text : str_,     _\*_ ,     _run\_id : UUID_,     _parent\_run\_id : UUID | None = None_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/callbacks/tracers/logging.html#LoggingCallbackHandler.on_text)\#     

Run on an arbitrary text.

Parameters:     

  * **text** \(_str_\) – The text.

  * **run\_id** \(_UUID_\) – The run ID. This is the ID of the current run.

  * **parent\_run\_id** \(_UUID_\) – The parent run ID. This is the ID of the parent run.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

None

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

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)