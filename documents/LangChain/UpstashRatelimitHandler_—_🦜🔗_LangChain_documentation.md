# UpstashRatelimitHandler — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.upstash_ratelimit_callback.UpstashRatelimitHandler.html
**Word Count:** 1283
**Links Count:** 266
**Scraped:** 2025-07-21 08:07:56
**Status:** completed

---

# UpstashRatelimitHandler\#

_class _langchain\_community.callbacks.upstash\_ratelimit\_callback.UpstashRatelimitHandler\(

    _identifier : str_,     _\*_ ,     _token\_ratelimit : None = None_,     _request\_ratelimit : None = None_,     _include\_output\_tokens : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/upstash_ratelimit_callback.html#UpstashRatelimitHandler)\#     

Callback to handle rate limiting based on the number of requests or the number of tokens in the input.

It uses Upstash Ratelimit to track the ratelimit which utilizes Upstash Redis to track the state.

Should not be passed to the chain when initialising the chain. This is because the handler has a state which should be fresh every time invoke is called. Instead, initialise and pass a handler every time you invoke.

Creates UpstashRatelimitHandler. Must be passed an identifier to ratelimit like a user id or an ip address.

Additionally, it must be passed at least one of token\_ratelimit or request\_ratelimit parameters.

Parameters:     

  * **Union****\[****int** \(_identifier_\) – the identifier

  * **str****\]** – the identifier

  * **Optional****\[****Ratelimit****\]** \(_request\_ratelimit_\) – Ratelimit to limit the number of tokens. Only works with OpenAI models since only these models provide the number of tokens as information in their output.

  * **Optional****\[****Ratelimit****\]** – Ratelimit to limit the number of requests

  * **bool** \(_include\_output\_tokens_\) – Whether to count output tokens when rate limiting based on number of tokens. Only used when token\_ratelimit is passed. False by default.

  * **identifier** \(_str_\)

  * **token\_ratelimit** \(_None_\)

  * **request\_ratelimit** \(_None_\)

  * **include\_output\_tokens** \(_bool_\)

Example               from upstash_redis import Redis     from upstash_ratelimit import Ratelimit, FixedWindow          redis = Redis.from_env()     ratelimit = Ratelimit(         redis=redis,         # fixed window to allow 10 requests every 10 seconds:         limiter=FixedWindow(max_requests=10, window=10),     )          user_id = "foo"     handler = UpstashRatelimitHandler(         identifier=user_id,         request_ratelimit=ratelimit     )          # Initialize a simple runnable to test     chain = RunnableLambda(str)          # pass handler as callback:     output = chain.invoke(         "input",         config={             "callbacks": [handler]         }     )     

Attributes

`ignore_agent` | Whether to ignore agent callbacks.   ---|---   `ignore_chain` | Whether to ignore chain callbacks.   `ignore_chat_model` | Whether to ignore chat model callbacks.   `ignore_custom_event` | Ignore custom event.   `ignore_llm` | Whether to ignore LLM callbacks.   `ignore_retriever` | Whether to ignore retriever callbacks.   `ignore_retry` | Whether to ignore retry callbacks.   `raise_error` | Whether to raise an error if an exception occurs.   `run_inline` | Whether to run the callback inline.      Methods

`__init__`\(identifier, \*\[, token\_ratelimit, ...\]\) | Creates UpstashRatelimitHandler.   ---|---   `on_agent_action`\(action, \*, run\_id\[, ...\]\) | Run on agent action.   `on_agent_finish`\(finish, \*, run\_id\[, ...\]\) | Run on the agent end.   `on_chain_end`\(outputs, \*, run\_id\[, parent\_run\_id\]\) | Run when chain ends running.   `on_chain_error`\(error, \*, run\_id\[, parent\_run\_id\]\) | Run when chain errors.   `on_chain_start`\(serialized, inputs, \*\*kwargs\) | Run when chain starts running.   `on_chat_model_start`\(serialized, messages, \*, ...\) | Run when a chat model starts running.   `on_custom_event`\(name, data, \*, run\_id\[, ...\]\) | Override to define a handler for a custom event.   `on_llm_end`\(response, \*\*kwargs\) | Run when LLM ends running   `on_llm_error`\(error, \*, run\_id\[, parent\_run\_id\]\) | Run when LLM errors.   `on_llm_new_token`\(token, \*\[, chunk, ...\]\) | Run on new LLM token.   `on_llm_start`\(serialized, prompts, \*\*kwargs\) | Run when LLM starts running   `on_retriever_end`\(documents, \*, run\_id\[, ...\]\) | Run when Retriever ends running.   `on_retriever_error`\(error, \*, run\_id\[, ...\]\) | Run when Retriever errors.   `on_retriever_start`\(serialized, query, \*, run\_id\) | Run when the Retriever starts running.   `on_retry`\(retry\_state, \*, run\_id\[, parent\_run\_id\]\) | Run on a retry event.   `on_text`\(text, \*, run\_id\[, parent\_run\_id\]\) | Run on an arbitrary text.   `on_tool_end`\(output, \*, run\_id\[, parent\_run\_id\]\) | Run when the tool ends running.   `on_tool_error`\(error, \*, run\_id\[, parent\_run\_id\]\) | Run when tool errors.   `on_tool_start`\(serialized, input\_str, \*, run\_id\) | Run when the tool starts running.   `reset`\(\[identifier\]\) | Creates a new UpstashRatelimitHandler object with the same ratelimit configurations but with a new identifier if it's provided.      \_\_init\_\_\(

    _identifier : str_,     _\*_ ,     _token\_ratelimit : None = None_,     _request\_ratelimit : None = None_,     _include\_output\_tokens : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/upstash_ratelimit_callback.html#UpstashRatelimitHandler.__init__)\#     

Creates UpstashRatelimitHandler. Must be passed an identifier to ratelimit like a user id or an ip address.

Additionally, it must be passed at least one of token\_ratelimit or request\_ratelimit parameters.

Parameters:     

  * **Union****\[****int** \(_identifier_\) – the identifier

  * **str****\]** – the identifier

  * **Optional****\[****Ratelimit****\]** \(_request\_ratelimit_\) – Ratelimit to limit the number of tokens. Only works with OpenAI models since only these models provide the number of tokens as information in their output.

  * **Optional****\[****Ratelimit****\]** – Ratelimit to limit the number of requests

  * **bool** \(_include\_output\_tokens_\) – Whether to count output tokens when rate limiting based on number of tokens. Only used when token\_ratelimit is passed. False by default.

  * **identifier** \(_str_\)

  * **token\_ratelimit** \(_None_\)

  * **request\_ratelimit** \(_None_\)

  * **include\_output\_tokens** \(_bool_\)

Example               from upstash_redis import Redis     from upstash_ratelimit import Ratelimit, FixedWindow          redis = Redis.from_env()     ratelimit = Ratelimit(         redis=redis,         # fixed window to allow 10 requests every 10 seconds:         limiter=FixedWindow(max_requests=10, window=10),     )          user_id = "foo"     handler = UpstashRatelimitHandler(         identifier=user_id,         request_ratelimit=ratelimit     )          # Initialize a simple runnable to test     chain = RunnableLambda(str)          # pass handler as callback:     output = chain.invoke(         "input",         config={             "callbacks": [handler]         }     )     

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

    _outputs : dict\[str, Any\]_,     _\*_ ,     _run\_id : UUID_,     _parent\_run\_id : UUID | None = None_,     _\*\* kwargs: Any_, \) → Any\#     

Run when chain ends running.

Parameters:     

  * **outputs** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The outputs of the chain.

  * **run\_id** \(_UUID_\) – The run ID. This is the ID of the current run.

  * **parent\_run\_id** \(_UUID_\) – The parent run ID. This is the ID of the parent run.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

Any

on\_chain\_error\(

    _error : BaseException_,     _\*_ ,     _run\_id : UUID_,     _parent\_run\_id : UUID | None = None_,     _\*\* kwargs: Any_, \) → Any\#     

Run when chain errors.

Parameters:     

  * **error** \(_BaseException_\) – The error that occurred.

  * **run\_id** \(_UUID_\) – The run ID. This is the ID of the current run.

  * **parent\_run\_id** \(_UUID_\) – The parent run ID. This is the ID of the parent run.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

Any

on\_chain\_start\(

    _serialized : Dict\[str, Any\]_,     _inputs : Dict\[str, Any\]_,     _\*\* kwargs: Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/upstash_ratelimit_callback.html#UpstashRatelimitHandler.on_chain_start)\#     

Run when chain starts running.

on\_chain\_start runs multiple times during a chain execution. To make sure that it’s only called once, we keep a bool state \_checked. If not self.\_checked, we call limit with request\_ratelimit and raise UpstashRatelimitError if the identifier is rate limited.

Parameters:     

  * **serialized** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **inputs** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

_Any_

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

    _response : [LLMResult](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.llm_result.LLMResult.html#langchain_core.outputs.llm_result.LLMResult "langchain_core.outputs.llm_result.LLMResult")_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/upstash_ratelimit_callback.html#UpstashRatelimitHandler.on_llm_end)\#     

Run when LLM ends running

If the include\_output\_tokens is set to True, number of tokens in LLM completion are counted for rate limiting

Parameters:     

  * **response** \([_LLMResult_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.llm_result.LLMResult.html#langchain_core.outputs.llm_result.LLMResult "langchain_core.outputs.llm_result.LLMResult")\)

  * **kwargs** \(_Any_\)

Return type:     

None

on\_llm\_error\(

    _error : BaseException_,     _\*_ ,     _run\_id : UUID_,     _parent\_run\_id : UUID | None = None_,     _\*\* kwargs: Any_, \) → Any\#     

Run when LLM errors.

Parameters:     

  * **error** \(_BaseException_\) – The error that occurred.

  * **run\_id** \(_UUID_\) – The run ID. This is the ID of the current run.

  * **parent\_run\_id** \(_UUID_\) – The parent run ID. This is the ID of the parent run.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

Any

on\_llm\_new\_token\(

    _token : str_,     _\*_ ,     _chunk : [GenerationChunk](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.GenerationChunk.html#langchain_core.outputs.generation.GenerationChunk "langchain_core.outputs.generation.GenerationChunk") | [ChatGenerationChunk](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.chat_generation.ChatGenerationChunk.html#langchain_core.outputs.chat_generation.ChatGenerationChunk "langchain_core.outputs.chat_generation.ChatGenerationChunk") | None = None_,     _run\_id : UUID_,     _parent\_run\_id : UUID | None = None_,     _\*\* kwargs: Any_, \) → Any\#     

Run on new LLM token. Only available when streaming is enabled.

Parameters:     

  * **token** \(_str_\) – The new token.

  * **chunk** \([_GenerationChunk_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.GenerationChunk.html#langchain_core.outputs.generation.GenerationChunk "langchain_core.outputs.generation.GenerationChunk") _|_[_ChatGenerationChunk_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.chat_generation.ChatGenerationChunk.html#langchain_core.outputs.chat_generation.ChatGenerationChunk "langchain_core.outputs.chat_generation.ChatGenerationChunk")\) – The new generated chunk, containing content and other information.

  * **run\_id** \(_UUID_\) – The run ID. This is the ID of the current run.

  * **parent\_run\_id** \(_UUID_\) – The parent run ID. This is the ID of the parent run.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

Any

on\_llm\_start\(

    _serialized : Dict\[str, Any\]_,     _prompts : List\[str\]_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/upstash_ratelimit_callback.html#UpstashRatelimitHandler.on_llm_start)\#     

Run when LLM starts running

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

    _output : Any_,     _\*_ ,     _run\_id : UUID_,     _parent\_run\_id : UUID | None = None_,     _\*\* kwargs: Any_, \) → Any\#     

Run when the tool ends running.

Parameters:     

  * **output** \(_Any_\) – The output of the tool.

  * **run\_id** \(_UUID_\) – The run ID. This is the ID of the current run.

  * **parent\_run\_id** \(_UUID_\) – The parent run ID. This is the ID of the parent run.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

Any

on\_tool\_error\(

    _error : BaseException_,     _\*_ ,     _run\_id : UUID_,     _parent\_run\_id : UUID | None = None_,     _\*\* kwargs: Any_, \) → Any\#     

Run when tool errors.

Parameters:     

  * **error** \(_BaseException_\) – The error that occurred.

  * **run\_id** \(_UUID_\) – The run ID. This is the ID of the current run.

  * **parent\_run\_id** \(_UUID_\) – The parent run ID. This is the ID of the parent run.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

Any

on\_tool\_start\(

    _serialized : dict\[str, Any\]_,     _input\_str : str_,     _\*_ ,     _run\_id : UUID_,     _parent\_run\_id : UUID | None = None_,     _tags : list\[str\] | None = None_,     _metadata : dict\[str, Any\] | None = None_,     _inputs : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → Any\#     

Run when the tool starts running.

Parameters:     

  * **serialized** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The serialized tool.

  * **input\_str** \(_str_\) – The input string.

  * **run\_id** \(_UUID_\) – The run ID. This is the ID of the current run.

  * **parent\_run\_id** \(_UUID_\) – The parent run ID. This is the ID of the parent run.

  * **tags** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\) – The tags.

  * **metadata** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\) – The metadata.

  * **inputs** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\) – The inputs.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

Any

reset\(

    _identifier : str | None = None_, \) → UpstashRatelimitHandler[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/upstash_ratelimit_callback.html#UpstashRatelimitHandler.reset)\#     

Creates a new UpstashRatelimitHandler object with the same ratelimit configurations but with a new identifier if it’s provided.

Also resets the state of the handler.

Parameters:     

**identifier** \(_str_ _|__None_\)

Return type:     

_UpstashRatelimitHandler_

Examples using UpstashRatelimitHandler

  * [Upstash Ratelimit Callback](https://python.langchain.com/docs/integrations/callbacks/upstash_ratelimit/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)