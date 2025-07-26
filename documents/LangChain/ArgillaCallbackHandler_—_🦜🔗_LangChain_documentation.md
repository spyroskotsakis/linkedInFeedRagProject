# ArgillaCallbackHandler — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.argilla_callback.ArgillaCallbackHandler.html
**Word Count:** 989
**Links Count:** 269
**Scraped:** 2025-07-21 08:15:47
**Status:** completed

---

# ArgillaCallbackHandler\#

_class _langchain\_community.callbacks.argilla\_callback.ArgillaCallbackHandler\(

    _dataset\_name : str_,     _workspace\_name : str | None = None_,     _api\_url : str | None = None_,     _api\_key : str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/argilla_callback.html#ArgillaCallbackHandler)\#     

Callback Handler that logs into Argilla.

Parameters:     

  * **dataset\_name** \(_str_\) – name of the FeedbackDataset in Argilla. Note that it must exist in advance. If you need help on how to create a FeedbackDataset in Argilla, please visit <https://docs.argilla.io/en/latest/tutorials_and_integrations/integrations/use_argilla_callback_in_langchain.html>.

  * **workspace\_name** \(_str_ _|__None_\) – name of the workspace in Argilla where the specified FeedbackDataset lives in. Defaults to None, which means that the default workspace will be used.

  * **api\_url** \(_str_ _|__None_\) – URL of the Argilla Server that we want to use, and where the FeedbackDataset lives in. Defaults to None, which means that either ARGILLA\_API\_URL environment variable or the default will be used.

  * **api\_key** \(_str_ _|__None_\) – API Key to connect to the Argilla Server. Defaults to None, which means that either ARGILLA\_API\_KEY environment variable or the default will be used.

Raises:     

  * **ImportError** – if the argilla package is not installed.

  * **ConnectionError** – if the connection to Argilla fails.

  * **FileNotFoundError** – if the FeedbackDataset retrieval from Argilla fails.

Examples               >>> from langchain_community.llms import OpenAI     >>> from langchain_community.callbacks import ArgillaCallbackHandler     >>> argilla_callback = ArgillaCallbackHandler(     ...     dataset_name="my-dataset",     ...     workspace_name="my-workspace",     ...     api_url="http://localhost:6900",     ...     api_key="argilla.apikey",     ... )     >>> llm = OpenAI(     ...     temperature=0,     ...     callbacks=[argilla_callback],     ...     verbose=True,     ...     openai_api_key="API_KEY_HERE",     ... )     >>> llm.generate([     ...     "What is the best NLP-annotation tool out there? (no bias at all)",     ... ])     "Argilla, no doubt about it."     

Initializes the ArgillaCallbackHandler.

Parameters:     

  * **dataset\_name** \(_str_\) – name of the FeedbackDataset in Argilla. Note that it must exist in advance. If you need help on how to create a FeedbackDataset in Argilla, please visit <https://docs.argilla.io/en/latest/tutorials_and_integrations/integrations/use_argilla_callback_in_langchain.html>.

  * **workspace\_name** \(_str_ _|__None_\) – name of the workspace in Argilla where the specified FeedbackDataset lives in. Defaults to None, which means that the default workspace will be used.

  * **api\_url** \(_str_ _|__None_\) – URL of the Argilla Server that we want to use, and where the FeedbackDataset lives in. Defaults to None, which means that either ARGILLA\_API\_URL environment variable or the default will be used.

  * **api\_key** \(_str_ _|__None_\) – API Key to connect to the Argilla Server. Defaults to None, which means that either ARGILLA\_API\_KEY environment variable or the default will be used.

Raises:     

  * **ImportError** – if the argilla package is not installed.

  * **ConnectionError** – if the connection to Argilla fails.

  * **FileNotFoundError** – if the FeedbackDataset retrieval from Argilla fails.

Attributes

`BLOG_URL` |    ---|---   `DEFAULT_API_URL` |    `ISSUES_URL` |    `REPO_URL` |    `ignore_agent` | Whether to ignore agent callbacks.   `ignore_chain` | Whether to ignore chain callbacks.   `ignore_chat_model` | Whether to ignore chat model callbacks.   `ignore_custom_event` | Ignore custom event.   `ignore_llm` | Whether to ignore LLM callbacks.   `ignore_retriever` | Whether to ignore retriever callbacks.   `ignore_retry` | Whether to ignore retry callbacks.   `raise_error` | Whether to raise an error if an exception occurs.   `run_inline` | Whether to run the callback inline.      Methods

`__init__`\(dataset\_name\[, workspace\_name, ...\]\) | Initializes the ArgillaCallbackHandler.   ---|---   `on_agent_action`\(action, \*\*kwargs\) | Do nothing when agent takes a specific action.   `on_agent_finish`\(finish, \*\*kwargs\) | Do nothing   `on_chain_end`\(outputs, \*\*kwargs\) | If either the parent\_run\_id or the run\_id is in self.prompts, then log the outputs to Argilla, and pop the run from self.prompts.   `on_chain_error`\(error, \*\*kwargs\) | Do nothing when LLM chain outputs an error.   `on_chain_start`\(serialized, inputs, \*\*kwargs\) | If the key input is in inputs, then save it in self.prompts using either the parent\_run\_id or the run\_id as the key.   `on_chat_model_start`\(serialized, messages, \*, ...\) | Run when a chat model starts running.   `on_custom_event`\(name, data, \*, run\_id\[, ...\]\) | Override to define a handler for a custom event.   `on_llm_end`\(response, \*\*kwargs\) | Log records to Argilla when an LLM ends.   `on_llm_error`\(error, \*\*kwargs\) | Do nothing when LLM outputs an error.   `on_llm_new_token`\(token, \*\*kwargs\) | Do nothing when a new token is generated.   `on_llm_start`\(serialized, prompts, \*\*kwargs\) | Save the prompts in memory when an LLM starts.   `on_retriever_end`\(documents, \*, run\_id\[, ...\]\) | Run when Retriever ends running.   `on_retriever_error`\(error, \*, run\_id\[, ...\]\) | Run when Retriever errors.   `on_retriever_start`\(serialized, query, \*, run\_id\) | Run when the Retriever starts running.   `on_retry`\(retry\_state, \*, run\_id\[, parent\_run\_id\]\) | Run on a retry event.   `on_text`\(text, \*\*kwargs\) | Do nothing   `on_tool_end`\(output\[, observation\_prefix, ...\]\) | Do nothing when tool ends.   `on_tool_error`\(error, \*\*kwargs\) | Do nothing when tool outputs an error.   `on_tool_start`\(serialized, input\_str, \*\*kwargs\) | Do nothing when tool starts.      \_\_init\_\_\(

    _dataset\_name : str_,     _workspace\_name : str | None = None_,     _api\_url : str | None = None_,     _api\_key : str | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/argilla_callback.html#ArgillaCallbackHandler.__init__)\#     

Initializes the ArgillaCallbackHandler.

Parameters:     

  * **dataset\_name** \(_str_\) – name of the FeedbackDataset in Argilla. Note that it must exist in advance. If you need help on how to create a FeedbackDataset in Argilla, please visit <https://docs.argilla.io/en/latest/tutorials_and_integrations/integrations/use_argilla_callback_in_langchain.html>.

  * **workspace\_name** \(_str_ _|__None_\) – name of the workspace in Argilla where the specified FeedbackDataset lives in. Defaults to None, which means that the default workspace will be used.

  * **api\_url** \(_str_ _|__None_\) – URL of the Argilla Server that we want to use, and where the FeedbackDataset lives in. Defaults to None, which means that either ARGILLA\_API\_URL environment variable or the default will be used.

  * **api\_key** \(_str_ _|__None_\) – API Key to connect to the Argilla Server. Defaults to None, which means that either ARGILLA\_API\_KEY environment variable or the default will be used.

Raises:     

  * **ImportError** – if the argilla package is not installed.

  * **ConnectionError** – if the connection to Argilla fails.

  * **FileNotFoundError** – if the FeedbackDataset retrieval from Argilla fails.

Return type:     

None

on\_agent\_action\(

    _action : [AgentAction](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction")_,     _\*\* kwargs: Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/argilla_callback.html#ArgillaCallbackHandler.on_agent_action)\#     

Do nothing when agent takes a specific action.

Parameters:     

  * **action** \([_AgentAction_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction")\)

  * **kwargs** \(_Any_\)

Return type:     

_Any_

on\_agent\_finish\(

    _finish : [AgentFinish](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentFinish.html#langchain_core.agents.AgentFinish "langchain_core.agents.AgentFinish")_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/argilla_callback.html#ArgillaCallbackHandler.on_agent_finish)\#     

Do nothing

Parameters:     

  * **finish** \([_AgentFinish_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentFinish.html#langchain_core.agents.AgentFinish "langchain_core.agents.AgentFinish")\)

  * **kwargs** \(_Any_\)

Return type:     

None

on\_chain\_end\(

    _outputs : Dict\[str, Any\]_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/argilla_callback.html#ArgillaCallbackHandler.on_chain_end)\#     

If either the parent\_run\_id or the run\_id is in self.prompts, then log the outputs to Argilla, and pop the run from self.prompts. The behavior differs if the output is a list or not.

Parameters:     

  * **outputs** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

None

on\_chain\_error\(

    _error : BaseException_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/argilla_callback.html#ArgillaCallbackHandler.on_chain_error)\#     

Do nothing when LLM chain outputs an error.

Parameters:     

  * **error** \(_BaseException_\)

  * **kwargs** \(_Any_\)

Return type:     

None

on\_chain\_start\(

    _serialized : Dict\[str, Any\]_,     _inputs : Dict\[str, Any\]_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/argilla_callback.html#ArgillaCallbackHandler.on_chain_start)\#     

If the key input is in inputs, then save it in self.prompts using either the parent\_run\_id or the run\_id as the key. This is done so that we don’t log the same input prompt twice, once when the LLM starts and once when the chain starts.

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

    _response : [LLMResult](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.llm_result.LLMResult.html#langchain_core.outputs.llm_result.LLMResult "langchain_core.outputs.llm_result.LLMResult")_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/argilla_callback.html#ArgillaCallbackHandler.on_llm_end)\#     

Log records to Argilla when an LLM ends.

Parameters:     

  * **response** \([_LLMResult_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.llm_result.LLMResult.html#langchain_core.outputs.llm_result.LLMResult "langchain_core.outputs.llm_result.LLMResult")\)

  * **kwargs** \(_Any_\)

Return type:     

None

on\_llm\_error\(

    _error : BaseException_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/argilla_callback.html#ArgillaCallbackHandler.on_llm_error)\#     

Do nothing when LLM outputs an error.

Parameters:     

  * **error** \(_BaseException_\)

  * **kwargs** \(_Any_\)

Return type:     

None

on\_llm\_new\_token\(

    _token : str_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/argilla_callback.html#ArgillaCallbackHandler.on_llm_new_token)\#     

Do nothing when a new token is generated.

Parameters:     

  * **token** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

None

on\_llm\_start\(

    _serialized : Dict\[str, Any\]_,     _prompts : List\[str\]_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/argilla_callback.html#ArgillaCallbackHandler.on_llm_start)\#     

Save the prompts in memory when an LLM starts.

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

    _text : str_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/argilla_callback.html#ArgillaCallbackHandler.on_text)\#     

Do nothing

Parameters:     

  * **text** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

None

on\_tool\_end\(

    _output : Any_,     _observation\_prefix : str | None = None_,     _llm\_prefix : str | None = None_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/argilla_callback.html#ArgillaCallbackHandler.on_tool_end)\#     

Do nothing when tool ends.

Parameters:     

  * **output** \(_Any_\)

  * **observation\_prefix** \(_str_ _|__None_\)

  * **llm\_prefix** \(_str_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

None

on\_tool\_error\(

    _error : BaseException_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/argilla_callback.html#ArgillaCallbackHandler.on_tool_error)\#     

Do nothing when tool outputs an error.

Parameters:     

  * **error** \(_BaseException_\)

  * **kwargs** \(_Any_\)

Return type:     

None

on\_tool\_start\(

    _serialized : Dict\[str, Any\]_,     _input\_str : str_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/argilla_callback.html#ArgillaCallbackHandler.on_tool_start)\#     

Do nothing when tool starts.

Parameters:     

  * **serialized** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **input\_str** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

None

Examples using ArgillaCallbackHandler

  * [Argilla](https://python.langchain.com/docs/integrations/providers/argilla/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)