# InfinoCallbackHandler — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.infino_callback.InfinoCallbackHandler.html
**Word Count:** 497
**Links Count:** 267
**Scraped:** 2025-07-21 08:17:20
**Status:** completed

---

# InfinoCallbackHandler\#

_class _langchain\_community.callbacks.infino\_callback.InfinoCallbackHandler\(

    _model\_id : str | None = None_,     _model\_version : str | None = None_,     _verbose : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/infino_callback.html#InfinoCallbackHandler)\#     

Callback Handler that logs to Infino.

Attributes

`ignore_agent` | Whether to ignore agent callbacks.   ---|---   `ignore_chain` | Whether to ignore chain callbacks.   `ignore_chat_model` | Whether to ignore chat model callbacks.   `ignore_custom_event` | Ignore custom event.   `ignore_llm` | Whether to ignore LLM callbacks.   `ignore_retriever` | Whether to ignore retriever callbacks.   `ignore_retry` | Whether to ignore retry callbacks.   `raise_error` | Whether to raise an error if an exception occurs.   `run_inline` | Whether to run the callback inline.      Methods

`__init__`\(\[model\_id, model\_version, verbose\]\) |    ---|---   `on_agent_action`\(action, \*\*kwargs\) | Do nothing when agent takes a specific action.   `on_agent_finish`\(finish, \*\*kwargs\) | Do nothing.   `on_chain_end`\(outputs, \*\*kwargs\) | Do nothing when LLM chain ends.   `on_chain_error`\(error, \*\*kwargs\) | Need to log the error.   `on_chain_start`\(serialized, inputs, \*\*kwargs\) | Do nothing when LLM chain starts.   `on_chat_model_start`\(serialized, messages, ...\) | Run when LLM starts running.   `on_custom_event`\(name, data, \*, run\_id\[, ...\]\) | Override to define a handler for a custom event.   `on_llm_end`\(response, \*\*kwargs\) | Log the latency, error, token usage, and response to Infino.   `on_llm_error`\(error, \*\*kwargs\) | Set the error flag.   `on_llm_new_token`\(token, \*\*kwargs\) | Do nothing when a new token is generated.   `on_llm_start`\(serialized, prompts, \*\*kwargs\) | Log the prompts to Infino, and set start time and error flag.   `on_retriever_end`\(documents, \*, run\_id\[, ...\]\) | Run when Retriever ends running.   `on_retriever_error`\(error, \*, run\_id\[, ...\]\) | Run when Retriever errors.   `on_retriever_start`\(serialized, query, \*, run\_id\) | Run when the Retriever starts running.   `on_retry`\(retry\_state, \*, run\_id\[, parent\_run\_id\]\) | Run on a retry event.   `on_text`\(text, \*\*kwargs\) | Do nothing.   `on_tool_end`\(output\[, observation\_prefix, ...\]\) | Do nothing when tool ends.   `on_tool_error`\(error, \*\*kwargs\) | Do nothing when tool outputs an error.   `on_tool_start`\(serialized, input\_str, \*\*kwargs\) | Do nothing when tool starts.      Parameters:     

  * **model\_id** \(_str_ _|__None_\)

  * **model\_version** \(_str_ _|__None_\)

  * **verbose** \(_bool_\)

\_\_init\_\_\(

    _model\_id : str | None = None_,     _model\_version : str | None = None_,     _verbose : bool = False_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/infino_callback.html#InfinoCallbackHandler.__init__)\#     

Parameters:     

  * **model\_id** \(_str_ _|__None_\)

  * **model\_version** \(_str_ _|__None_\)

  * **verbose** \(_bool_\)

Return type:     

None

on\_agent\_action\(

    _action : [AgentAction](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction")_,     _\*\* kwargs: Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/infino_callback.html#InfinoCallbackHandler.on_agent_action)\#     

Do nothing when agent takes a specific action.

Parameters:     

  * **action** \([_AgentAction_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction")\)

  * **kwargs** \(_Any_\)

Return type:     

_Any_

on\_agent\_finish\(

    _finish : [AgentFinish](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentFinish.html#langchain_core.agents.AgentFinish "langchain_core.agents.AgentFinish")_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/infino_callback.html#InfinoCallbackHandler.on_agent_finish)\#     

Do nothing.

Parameters:     

  * **finish** \([_AgentFinish_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentFinish.html#langchain_core.agents.AgentFinish "langchain_core.agents.AgentFinish")\)

  * **kwargs** \(_Any_\)

Return type:     

None

on\_chain\_end\(

    _outputs : Dict\[str, Any\]_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/infino_callback.html#InfinoCallbackHandler.on_chain_end)\#     

Do nothing when LLM chain ends.

Parameters:     

  * **outputs** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

None

on\_chain\_error\(

    _error : BaseException_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/infino_callback.html#InfinoCallbackHandler.on_chain_error)\#     

Need to log the error.

Parameters:     

  * **error** \(_BaseException_\)

  * **kwargs** \(_Any_\)

Return type:     

None

on\_chain\_start\(

    _serialized : Dict\[str, Any\]_,     _inputs : Dict\[str, Any\]_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/infino_callback.html#InfinoCallbackHandler.on_chain_start)\#     

Do nothing when LLM chain starts.

Parameters:     

  * **serialized** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **inputs** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

None

on\_chat\_model\_start\(

    _serialized : Dict\[str, Any\]_,     _messages : List\[List\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]\]_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/infino_callback.html#InfinoCallbackHandler.on_chat_model_start)\#     

Run when LLM starts running.

Parameters:     

  * **serialized** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **messages** \(_List_ _\[__List_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]__\]_\)

  * **kwargs** \(_Any_\)

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

    _response : [LLMResult](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.llm_result.LLMResult.html#langchain_core.outputs.llm_result.LLMResult "langchain_core.outputs.llm_result.LLMResult")_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/infino_callback.html#InfinoCallbackHandler.on_llm_end)\#     

Log the latency, error, token usage, and response to Infino.

Parameters:     

  * **response** \([_LLMResult_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.llm_result.LLMResult.html#langchain_core.outputs.llm_result.LLMResult "langchain_core.outputs.llm_result.LLMResult")\)

  * **kwargs** \(_Any_\)

Return type:     

None

on\_llm\_error\(

    _error : BaseException_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/infino_callback.html#InfinoCallbackHandler.on_llm_error)\#     

Set the error flag.

Parameters:     

  * **error** \(_BaseException_\)

  * **kwargs** \(_Any_\)

Return type:     

None

on\_llm\_new\_token\(

    _token : str_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/infino_callback.html#InfinoCallbackHandler.on_llm_new_token)\#     

Do nothing when a new token is generated.

Parameters:     

  * **token** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

None

on\_llm\_start\(

    _serialized : Dict\[str, Any\]_,     _prompts : List\[str\]_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/infino_callback.html#InfinoCallbackHandler.on_llm_start)\#     

Log the prompts to Infino, and set start time and error flag.

Parameters:     

  * **serialized** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **prompts** \(_List_ _\[__str_ _\]_\)

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

    _text : str_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/infino_callback.html#InfinoCallbackHandler.on_text)\#     

Do nothing.

Parameters:     

  * **text** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

None

on\_tool\_end\(

    _output : str_,     _observation\_prefix : str | None = None_,     _llm\_prefix : str | None = None_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/infino_callback.html#InfinoCallbackHandler.on_tool_end)\#     

Do nothing when tool ends.

Parameters:     

  * **output** \(_str_\)

  * **observation\_prefix** \(_str_ _|__None_\)

  * **llm\_prefix** \(_str_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

None

on\_tool\_error\(

    _error : BaseException_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/infino_callback.html#InfinoCallbackHandler.on_tool_error)\#     

Do nothing when tool outputs an error.

Parameters:     

  * **error** \(_BaseException_\)

  * **kwargs** \(_Any_\)

Return type:     

None

on\_tool\_start\(

    _serialized : Dict\[str, Any\]_,     _input\_str : str_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/infino_callback.html#InfinoCallbackHandler.on_tool_start)\#     

Do nothing when tool starts.

Parameters:     

  * **serialized** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **input\_str** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

None

Examples using InfinoCallbackHandler

  * [Infino](https://python.langchain.com/docs/integrations/providers/infino/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)