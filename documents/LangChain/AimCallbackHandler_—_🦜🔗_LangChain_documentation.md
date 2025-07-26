# AimCallbackHandler — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.aim_callback.AimCallbackHandler.html
**Word Count:** 758
**Links Count:** 280
**Scraped:** 2025-07-21 08:01:32
**Status:** completed

---

# AimCallbackHandler\#

_class _langchain\_community.callbacks.aim\_callback.AimCallbackHandler\(

    _repo : str | None = None_,     _experiment\_name : str | None = None_,     _system\_tracking\_interval : int | None = 10_,     _log\_system\_params : bool = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/aim_callback.html#AimCallbackHandler)\#     

Callback Handler that logs to Aim.

Parameters:     

  * **repo** \(`str`, optional\) – Aim repository path or Repo object to which Run object is bound. If skipped, default Repo is used.

  * **experiment\_name** \(`str`, optional\) – Sets Run’s experiment property. ‘default’ if not specified. Can be used later to query runs/sequences.

  * **system\_tracking\_interval** \(`int`, optional\) – 

Sets the tracking interval in seconds for system usage metrics \(CPU, Memory, etc.\). Set to None

> to disable system metrics tracking.

  * **log\_system\_params** \(`bool`, optional\) – Enable/Disable logging of system params such as installed packages, git info, environment variables, etc.

This handler will utilize the associated callback method called and formats the input of each callback function with metadata regarding the state of LLM run and then logs the response to Aim.

Initialize callback handler.

Attributes

`always_verbose` | Whether to call verbose callbacks even if verbose is False.   ---|---   `ignore_agent` | Whether to ignore agent callbacks.   `ignore_chain` | Whether to ignore chain callbacks.   `ignore_chat_model` | Whether to ignore chat model callbacks.   `ignore_custom_event` | Ignore custom event.   `ignore_llm` | Whether to ignore LLM callbacks.   `ignore_retriever` | Whether to ignore retriever callbacks.   `ignore_retry` | Whether to ignore retry callbacks.   `raise_error` | Whether to raise an error if an exception occurs.   `run_inline` | Whether to run the callback inline.      Methods

`__init__`\(\[repo, experiment\_name, ...\]\) | Initialize callback handler.   ---|---   `flush_tracker`\(\[repo, experiment\_name, ...\]\) | Flush the tracker and reset the session.   `get_custom_callback_meta`\(\) |    `on_agent_action`\(action, \*\*kwargs\) | Run on agent action.   `on_agent_finish`\(finish, \*\*kwargs\) | Run when agent ends running.   `on_chain_end`\(outputs, \*\*kwargs\) | Run when chain ends running.   `on_chain_error`\(error, \*\*kwargs\) | Run when chain errors.   `on_chain_start`\(serialized, inputs, \*\*kwargs\) | Run when chain starts running.   `on_chat_model_start`\(serialized, messages, \*, ...\) | Run when a chat model starts running.   `on_custom_event`\(name, data, \*, run\_id\[, ...\]\) | Override to define a handler for a custom event.   `on_llm_end`\(response, \*\*kwargs\) | Run when LLM ends running.   `on_llm_error`\(error, \*\*kwargs\) | Run when LLM errors.   `on_llm_new_token`\(token, \*\*kwargs\) | Run when LLM generates a new token.   `on_llm_start`\(serialized, prompts, \*\*kwargs\) | Run when LLM starts.   `on_retriever_end`\(documents, \*, run\_id\[, ...\]\) | Run when Retriever ends running.   `on_retriever_error`\(error, \*, run\_id\[, ...\]\) | Run when Retriever errors.   `on_retriever_start`\(serialized, query, \*, run\_id\) | Run when the Retriever starts running.   `on_retry`\(retry\_state, \*, run\_id\[, parent\_run\_id\]\) | Run on a retry event.   `on_text`\(text, \*\*kwargs\) | Run when agent is ending.   `on_tool_end`\(output, \*\*kwargs\) | Run when tool ends running.   `on_tool_error`\(error, \*\*kwargs\) | Run when tool errors.   `on_tool_start`\(serialized, input\_str, \*\*kwargs\) | Run when tool starts running.   `reset_callback_meta`\(\) | Reset the callback metadata.   `setup`\(\*\*kwargs\) |       \_\_init\_\_\(

    _repo : str | None = None_,     _experiment\_name : str | None = None_,     _system\_tracking\_interval : int | None = 10_,     _log\_system\_params : bool = True_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/aim_callback.html#AimCallbackHandler.__init__)\#     

Initialize callback handler.

Parameters:     

  * **repo** \(_str_ _|__None_\)

  * **experiment\_name** \(_str_ _|__None_\)

  * **system\_tracking\_interval** \(_int_ _|__None_\)

  * **log\_system\_params** \(_bool_\)

Return type:     

None

flush\_tracker\(

    _repo : str | None = None_,     _experiment\_name : str | None = None_,     _system\_tracking\_interval : int | None = 10_,     _log\_system\_params : bool = True_,     _langchain\_asset : Any = None_,     _reset : bool = True_,     _finish : bool = False_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/aim_callback.html#AimCallbackHandler.flush_tracker)\#     

Flush the tracker and reset the session.

Parameters:     

  * **repo** \(`str`, optional\) – Aim repository path or Repo object to which Run object is bound. If skipped, default Repo is used.

  * **experiment\_name** \(`str`, optional\) – Sets Run’s experiment property. ‘default’ if not specified. Can be used later to query runs/sequences.

  * **system\_tracking\_interval** \(`int`, optional\) – 

Sets the tracking interval in seconds for system usage metrics \(CPU, Memory, etc.\). Set to None

> to disable system metrics tracking.

  * **log\_system\_params** \(`bool`, optional\) – Enable/Disable logging of system params such as installed packages, git info, environment variables, etc.

  * **langchain\_asset** \(_Any_\) – The langchain asset to save.

  * **reset** \(_bool_\) – Whether to reset the session.

  * **finish** \(_bool_\) – Whether to finish the run.

  * **Returns** – None

Return type:     

None

get\_custom\_callback\_meta\(\) → Dict\[str, Any\]\#     

Return type:     

_Dict_\[str, _Any_\]

on\_agent\_action\(

    _action : [AgentAction](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction")_,     _\*\* kwargs: Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/aim_callback.html#AimCallbackHandler.on_agent_action)\#     

Run on agent action.

Parameters:     

  * **action** \([_AgentAction_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction")\)

  * **kwargs** \(_Any_\)

Return type:     

_Any_

on\_agent\_finish\(

    _finish : [AgentFinish](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentFinish.html#langchain_core.agents.AgentFinish "langchain_core.agents.AgentFinish")_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/aim_callback.html#AimCallbackHandler.on_agent_finish)\#     

Run when agent ends running.

Parameters:     

  * **finish** \([_AgentFinish_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentFinish.html#langchain_core.agents.AgentFinish "langchain_core.agents.AgentFinish")\)

  * **kwargs** \(_Any_\)

Return type:     

None

on\_chain\_end\(

    _outputs : Dict\[str, Any\]_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/aim_callback.html#AimCallbackHandler.on_chain_end)\#     

Run when chain ends running.

Parameters:     

  * **outputs** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

None

on\_chain\_error\(

    _error : BaseException_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/aim_callback.html#AimCallbackHandler.on_chain_error)\#     

Run when chain errors.

Parameters:     

  * **error** \(_BaseException_\)

  * **kwargs** \(_Any_\)

Return type:     

None

on\_chain\_start\(

    _serialized : Dict\[str, Any\]_,     _inputs : Dict\[str, Any\]_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/aim_callback.html#AimCallbackHandler.on_chain_start)\#     

Run when chain starts running.

Parameters:     

  * **serialized** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **inputs** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

None

on\_chat\_model\_start\(

    _serialized : dict\[str, Any\]_,     _messages : list\[list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]\]_,     _\*_ ,     _run\_id : UUID_,     _parent\_run\_id : UUID | None = None_,     _tags : list\[str\] | None = None_,     _metadata : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → Any\#     

Run when a chat model starts running.

**ATTENTION** : This method is called for chat models. If you’re implementing a handler for a non-chat model, you should use `on_llm_start` instead.

Parameters:     

  * **serialized** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The serialized chat model.

  * **messages** \(_list_ _\[__list_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]__\]_\) – The messages.

  * **run\_id** \(_UUID_\) – The run ID. This is the ID of the current run.

  * **parent\_run\_id** \(_UUID_\) – The parent run ID. This is the ID of the parent run.

  * **tags** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\) – The tags.

  * **metadata** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\) – The metadata.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

Any

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

    _response : [LLMResult](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.llm_result.LLMResult.html#langchain_core.outputs.llm_result.LLMResult "langchain_core.outputs.llm_result.LLMResult")_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/aim_callback.html#AimCallbackHandler.on_llm_end)\#     

Run when LLM ends running.

Parameters:     

  * **response** \([_LLMResult_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.llm_result.LLMResult.html#langchain_core.outputs.llm_result.LLMResult "langchain_core.outputs.llm_result.LLMResult")\)

  * **kwargs** \(_Any_\)

Return type:     

None

on\_llm\_error\(

    _error : BaseException_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/aim_callback.html#AimCallbackHandler.on_llm_error)\#     

Run when LLM errors.

Parameters:     

  * **error** \(_BaseException_\)

  * **kwargs** \(_Any_\)

Return type:     

None

on\_llm\_new\_token\(

    _token : str_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/aim_callback.html#AimCallbackHandler.on_llm_new_token)\#     

Run when LLM generates a new token.

Parameters:     

  * **token** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

None

on\_llm\_start\(

    _serialized : Dict\[str, Any\]_,     _prompts : List\[str\]_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/aim_callback.html#AimCallbackHandler.on_llm_start)\#     

Run when LLM starts.

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

    _text : str_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/aim_callback.html#AimCallbackHandler.on_text)\#     

Run when agent is ending.

Parameters:     

  * **text** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

None

on\_tool\_end\(

    _output : Any_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/aim_callback.html#AimCallbackHandler.on_tool_end)\#     

Run when tool ends running.

Parameters:     

  * **output** \(_Any_\)

  * **kwargs** \(_Any_\)

Return type:     

None

on\_tool\_error\(

    _error : BaseException_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/aim_callback.html#AimCallbackHandler.on_tool_error)\#     

Run when tool errors.

Parameters:     

  * **error** \(_BaseException_\)

  * **kwargs** \(_Any_\)

Return type:     

None

on\_tool\_start\(

    _serialized : Dict\[str, Any\]_,     _input\_str : str_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/aim_callback.html#AimCallbackHandler.on_tool_start)\#     

Run when tool starts running.

Parameters:     

  * **serialized** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **input\_str** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

None

reset\_callback\_meta\(\) → None\#     

Reset the callback metadata.

Return type:     

None

setup\(_\*\* kwargs: Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/aim_callback.html#AimCallbackHandler.setup)\#     

Parameters:     

**kwargs** \(_Any_\)

Return type:     

None

Examples using AimCallbackHandler

  * [Aim](https://python.langchain.com/docs/integrations/providers/aim_tracking/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)