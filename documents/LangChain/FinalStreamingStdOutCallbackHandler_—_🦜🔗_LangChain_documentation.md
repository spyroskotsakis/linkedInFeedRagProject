# FinalStreamingStdOutCallbackHandler — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/callbacks/langchain.callbacks.streaming_stdout_final_only.FinalStreamingStdOutCallbackHandler.html
**Word Count:** 692
**Links Count:** 168
**Scraped:** 2025-07-21 07:50:02
**Status:** completed

---

# FinalStreamingStdOutCallbackHandler\#

_class _langchain.callbacks.streaming\_stdout\_final\_only.FinalStreamingStdOutCallbackHandler\(

    _\*_ ,     _answer\_prefix\_tokens : list\[str\] | None = None_,     _strip\_tokens : bool = True_,     _stream\_prefix : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/callbacks/streaming_stdout_final_only.html#FinalStreamingStdOutCallbackHandler)\#     

Callback handler for streaming in agents. Only works with agents using LLMs that support streaming.

Only the final output of the agent will be streamed.

Instantiate FinalStreamingStdOutCallbackHandler.

Parameters:     

  * **answer\_prefix\_tokens** \(_list_ _\[__str_ _\]__|__None_\) – Token sequence that prefixes the answer. Default is \[“Final”, “Answer”, “:”\]

  * **strip\_tokens** \(_bool_\) – Ignore white spaces and new lines when comparing answer\_prefix\_tokens to last tokens? \(to determine if answer has been reached\)

  * **stream\_prefix** \(_bool_\) – Should answer prefix itself also be streamed?

Attributes

`ignore_agent` | Whether to ignore agent callbacks.   ---|---   `ignore_chain` | Whether to ignore chain callbacks.   `ignore_chat_model` | Whether to ignore chat model callbacks.   `ignore_custom_event` | Ignore custom event.   `ignore_llm` | Whether to ignore LLM callbacks.   `ignore_retriever` | Whether to ignore retriever callbacks.   `ignore_retry` | Whether to ignore retry callbacks.   `raise_error` | Whether to raise an error if an exception occurs.   `run_inline` | Whether to run the callback inline.      Methods

`__init__`\(\*\[, answer\_prefix\_tokens, ...\]\) | Instantiate FinalStreamingStdOutCallbackHandler.   ---|---   `append_to_last_tokens`\(token\) |    `check_if_answer_reached`\(\) |    `on_agent_action`\(action, \*\*kwargs\) | Run on agent action.   `on_agent_finish`\(finish, \*\*kwargs\) | Run on the agent end.   `on_chain_end`\(outputs, \*\*kwargs\) | Run when a chain ends running.   `on_chain_error`\(error, \*\*kwargs\) | Run when chain errors.   `on_chain_start`\(serialized, inputs, \*\*kwargs\) | Run when a chain starts running.   `on_chat_model_start`\(serialized, messages, ...\) | Run when LLM starts running.   `on_custom_event`\(name, data, \*, run\_id\[, ...\]\) | Override to define a handler for a custom event.   `on_llm_end`\(response, \*\*kwargs\) | Run when LLM ends running.   `on_llm_error`\(error, \*\*kwargs\) | Run when LLM errors.   `on_llm_new_token`\(token, \*\*kwargs\) | Run on new LLM token.   `on_llm_start`\(serialized, prompts, \*\*kwargs\) | Run when LLM starts running.   `on_retriever_end`\(documents, \*, run\_id\[, ...\]\) | Run when Retriever ends running.   `on_retriever_error`\(error, \*, run\_id\[, ...\]\) | Run when Retriever errors.   `on_retriever_start`\(serialized, query, \*, run\_id\) | Run when the Retriever starts running.   `on_retry`\(retry\_state, \*, run\_id\[, parent\_run\_id\]\) | Run on a retry event.   `on_text`\(text, \*\*kwargs\) | Run on an arbitrary text.   `on_tool_end`\(output, \*\*kwargs\) | Run when tool ends running.   `on_tool_error`\(error, \*\*kwargs\) | Run when tool errors.   `on_tool_start`\(serialized, input\_str, \*\*kwargs\) | Run when the tool starts running.      \_\_init\_\_\(

    _\*_ ,     _answer\_prefix\_tokens : list\[str\] | None = None_,     _strip\_tokens : bool = True_,     _stream\_prefix : bool = False_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/callbacks/streaming_stdout_final_only.html#FinalStreamingStdOutCallbackHandler.__init__)\#     

Instantiate FinalStreamingStdOutCallbackHandler.

Parameters:     

  * **answer\_prefix\_tokens** \(_list_ _\[__str_ _\]__|__None_\) – Token sequence that prefixes the answer. Default is \[“Final”, “Answer”, “:”\]

  * **strip\_tokens** \(_bool_\) – Ignore white spaces and new lines when comparing answer\_prefix\_tokens to last tokens? \(to determine if answer has been reached\)

  * **stream\_prefix** \(_bool_\) – Should answer prefix itself also be streamed?

Return type:     

None

append\_to\_last\_tokens\(

    _token : str_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/callbacks/streaming_stdout_final_only.html#FinalStreamingStdOutCallbackHandler.append_to_last_tokens)\#     

Parameters:     

**token** \(_str_\)

Return type:     

None

check\_if\_answer\_reached\(\) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/callbacks/streaming_stdout_final_only.html#FinalStreamingStdOutCallbackHandler.check_if_answer_reached)\#     

Return type:     

bool

on\_agent\_action\(

    _action : [AgentAction](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction")_,     _\*\* kwargs: Any_, \) → Any\#     

Run on agent action.

Parameters:     

  * **action** \([_AgentAction_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction")\) – The agent action.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

Any

on\_agent\_finish\(

    _finish : [AgentFinish](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentFinish.html#langchain_core.agents.AgentFinish "langchain_core.agents.AgentFinish")_,     _\*\* kwargs: Any_, \) → None\#     

Run on the agent end.

Parameters:     

  * **finish** \([_AgentFinish_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentFinish.html#langchain_core.agents.AgentFinish "langchain_core.agents.AgentFinish")\) – The agent finish.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

None

on\_chain\_end\(

    _outputs : dict\[str, Any\]_,     _\*\* kwargs: Any_, \) → None\#     

Run when a chain ends running.

Parameters:     

  * **outputs** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The outputs of the chain.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

None

on\_chain\_error\(

    _error : BaseException_,     _\*\* kwargs: Any_, \) → None\#     

Run when chain errors.

Parameters:     

  * **error** \(_BaseException_\) – The error that occurred.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

None

on\_chain\_start\(

    _serialized : dict\[str, Any\]_,     _inputs : dict\[str, Any\]_,     _\*\* kwargs: Any_, \) → None\#     

Run when a chain starts running.

Parameters:     

  * **serialized** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The serialized chain.

  * **inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The inputs to the chain.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

None

on\_chat\_model\_start\(

    _serialized : dict\[str, Any\]_,     _messages : list\[list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]\]_,     _\*\* kwargs: Any_, \) → None\#     

Run when LLM starts running.

Parameters:     

  * **serialized** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The serialized LLM.

  * **messages** \(_list_ _\[__list_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]__\]_\) – The messages to run.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

None

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

    _response : [LLMResult](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.llm_result.LLMResult.html#langchain_core.outputs.llm_result.LLMResult "langchain_core.outputs.llm_result.LLMResult")_,     _\*\* kwargs: Any_, \) → None\#     

Run when LLM ends running.

Parameters:     

  * **response** \([_LLMResult_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.llm_result.LLMResult.html#langchain_core.outputs.llm_result.LLMResult "langchain_core.outputs.llm_result.LLMResult")\) – The response from the LLM.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

None

on\_llm\_error\(

    _error : BaseException_,     _\*\* kwargs: Any_, \) → None\#     

Run when LLM errors.

Parameters:     

  * **error** \(_BaseException_\) – The error that occurred.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

None

on\_llm\_new\_token\(

    _token : str_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/callbacks/streaming_stdout_final_only.html#FinalStreamingStdOutCallbackHandler.on_llm_new_token)\#     

Run on new LLM token. Only available when streaming is enabled.

Parameters:     

  * **token** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

None

on\_llm\_start\(

    _serialized : dict\[str, Any\]_,     _prompts : list\[str\]_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/callbacks/streaming_stdout_final_only.html#FinalStreamingStdOutCallbackHandler.on_llm_start)\#     

Run when LLM starts running.

Parameters:     

  * **serialized** \(_dict_ _\[__str_ _,__Any_ _\]_\)

  * **prompts** \(_list_ _\[__str_ _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

None

on\_retriever\_end\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*_ ,     _run\_id : UUID_,     _parent\_run\_id : UUID | None = None_,     _\*\* kwargs: Any_, \) → Any\#     

Run when Retriever ends running.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – The documents retrieved.

  * **run\_id** \(_UUID_\) – The run ID. This is the ID of the current run.

  * **parent\_run\_id** \(_UUID_\) – The parent run ID. This is the ID of the parent run.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

Any

on\_retriever\_error\(

    _error : BaseException_,     _\*_ ,     _run\_id : UUID_,     _parent\_run\_id : UUID | None = None_,     _\*\* kwargs: Any_, \) → Any\#     

Run when Retriever errors.

Parameters:     

  * **error** \(_BaseException_\) – The error that occurred.

  * **run\_id** \(_UUID_\) – The run ID. This is the ID of the current run.

  * **parent\_run\_id** \(_UUID_\) – The parent run ID. This is the ID of the parent run.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

Any

on\_retriever\_start\(

    _serialized : dict\[str, Any\]_,     _query : str_,     _\*_ ,     _run\_id : UUID_,     _parent\_run\_id : UUID | None = None_,     _tags : list\[str\] | None = None_,     _metadata : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → Any\#     

Run when the Retriever starts running.

Parameters:     

  * **serialized** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The serialized Retriever.

  * **query** \(_str_\) – The query.

  * **run\_id** \(_UUID_\) – The run ID. This is the ID of the current run.

  * **parent\_run\_id** \(_UUID_\) – The parent run ID. This is the ID of the parent run.

  * **tags** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\) – The tags.

  * **metadata** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\) – The metadata.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

Any

on\_retry\(

    _retry\_state : RetryCallState_,     _\*_ ,     _run\_id : UUID_,     _parent\_run\_id : UUID | None = None_,     _\*\* kwargs: Any_, \) → Any\#     

Run on a retry event.

Parameters:     

  * **retry\_state** \(_RetryCallState_\) – The retry state.

  * **run\_id** \(_UUID_\) – The run ID. This is the ID of the current run.

  * **parent\_run\_id** \(_UUID_\) – The parent run ID. This is the ID of the parent run.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

Any

on\_text\(

    _text : str_,     _\*\* kwargs: Any_, \) → None\#     

Run on an arbitrary text.

Parameters:     

  * **text** \(_str_\) – The text to print.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

None

on\_tool\_end\(

    _output : Any_,     _\*\* kwargs: Any_, \) → None\#     

Run when tool ends running.

Parameters:     

  * **output** \(_Any_\) – The output of the tool.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

None

on\_tool\_error\(

    _error : BaseException_,     _\*\* kwargs: Any_, \) → None\#     

Run when tool errors.

Parameters:     

  * **error** \(_BaseException_\) – The error that occurred.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

None

on\_tool\_start\(

    _serialized : dict\[str, Any\]_,     _input\_str : str_,     _\*\* kwargs: Any_, \) → None\#     

Run when the tool starts running.

Parameters:     

  * **serialized** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The serialized tool.

  * **input\_str** \(_str_\) – The input string.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

None

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)