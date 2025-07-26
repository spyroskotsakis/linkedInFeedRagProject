# BaseCallbackManager — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html
**Word Count:** 694
**Links Count:** 216
**Scraped:** 2025-07-21 07:54:58
**Status:** completed

---

# BaseCallbackManager\#

_class _langchain\_core.callbacks.base.BaseCallbackManager\(

    _handlers : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\]_,     _inheritable\_handlers : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | None = None_,     _parent\_run\_id : UUID | None = None_,     _\*_ ,     _tags : list\[str\] | None = None_,     _inheritable\_tags : list\[str\] | None = None_,     _metadata : dict\[str, Any\] | None = None_,     _inheritable\_metadata : dict\[str, Any\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/base.html#BaseCallbackManager)\#     

Base callback manager for LangChain.

Initialize callback manager.

Parameters:     

  * **handlers** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]_\) – The handlers.

  * **inheritable\_handlers** \(_Optional_ _\[__list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__\]_\) – The inheritable handlers. Default is None.

  * **parent\_run\_id** \(_Optional_ _\[__UUID_ _\]_\) – The parent run ID. Default is None.

  * **tags** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\) – The tags. Default is None.

  * **inheritable\_tags** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\) – The inheritable tags. Default is None.

  * **metadata** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\) – The metadata. Default is None.

  * **inheritable\_metadata** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\) – The inheritable metadata. Default is None.

Attributes

`is_async` | Whether the callback manager is async.   ---|---      Methods

`__init__`\(handlers\[, inheritable\_handlers, ...\]\) | Initialize callback manager.   ---|---   `add_handler`\(handler\[, inherit\]\) | Add a handler to the callback manager.   `add_metadata`\(metadata\[, inherit\]\) | Add metadata to the callback manager.   `add_tags`\(tags\[, inherit\]\) | Add tags to the callback manager.   `copy`\(\) | Copy the callback manager.   `merge`\(other\) | Merge the callback manager with another callback manager.   `on_chain_start`\(serialized, inputs, \*, run\_id\) | Run when a chain starts running.   `on_chat_model_start`\(serialized, messages, \*, ...\) | Run when a chat model starts running.   `on_llm_start`\(serialized, prompts, \*, run\_id\) | Run when LLM starts running.   `on_retriever_start`\(serialized, query, \*, run\_id\) | Run when the Retriever starts running.   `on_tool_start`\(serialized, input\_str, \*, run\_id\) | Run when the tool starts running.   `remove_handler`\(handler\) | Remove a handler from the callback manager.   `remove_metadata`\(keys\) | Remove metadata from the callback manager.   `remove_tags`\(tags\) | Remove tags from the callback manager.   `set_handler`\(handler\[, inherit\]\) | Set handler as the only handler on the callback manager.   `set_handlers`\(handlers\[, inherit\]\) | Set handlers as the only handlers on the callback manager.      \_\_init\_\_\(

    _handlers : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\]_,     _inheritable\_handlers : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | None = None_,     _parent\_run\_id : UUID | None = None_,     _\*_ ,     _tags : list\[str\] | None = None_,     _inheritable\_tags : list\[str\] | None = None_,     _metadata : dict\[str, Any\] | None = None_,     _inheritable\_metadata : dict\[str, Any\] | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/base.html#BaseCallbackManager.__init__)\#     

Initialize callback manager.

Parameters:     

  * **handlers** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]_\) – The handlers.

  * **inheritable\_handlers** \(_Optional_ _\[__list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__\]_\) – The inheritable handlers. Default is None.

  * **parent\_run\_id** \(_Optional_ _\[__UUID_ _\]_\) – The parent run ID. Default is None.

  * **tags** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\) – The tags. Default is None.

  * **inheritable\_tags** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\) – The inheritable tags. Default is None.

  * **metadata** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\) – The metadata. Default is None.

  * **inheritable\_metadata** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\) – The inheritable metadata. Default is None.

Return type:     

None

add\_handler\(

    _handler : [BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")_,     _inherit : bool = True_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/base.html#BaseCallbackManager.add_handler)\#     

Add a handler to the callback manager.

Parameters:     

  * **handler** \([_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\) – The handler to add.

  * **inherit** \(_bool_\) – Whether to inherit the handler. Default is True.

Return type:     

None

add\_metadata\(

    _metadata : dict\[str, Any\]_,     _inherit : bool = True_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/base.html#BaseCallbackManager.add_metadata)\#     

Add metadata to the callback manager.

Parameters:     

  * **metadata** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The metadata to add.

  * **inherit** \(_bool_\) – Whether to inherit the metadata. Default is True.

Return type:     

None

add\_tags\(

    _tags : list\[str\]_,     _inherit : bool = True_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/base.html#BaseCallbackManager.add_tags)\#     

Add tags to the callback manager.

Parameters:     

  * **tags** \(_list_ _\[__str_ _\]_\) – The tags to add.

  * **inherit** \(_bool_\) – Whether to inherit the tags. Default is True.

Return type:     

None

copy\(\) → Self[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/base.html#BaseCallbackManager.copy)\#     

Copy the callback manager.

Return type:     

_Self_

merge\(

    _other : BaseCallbackManager_, \) → Self[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/base.html#BaseCallbackManager.merge)\#     

Merge the callback manager with another callback manager.

May be overwritten in subclasses. Primarily used internally within merge\_configs.

Returns:     

The merged callback manager of the same type     

as the current object.

Return type:     

BaseCallbackManager

Parameters:     

**other** \(_BaseCallbackManager_\)

Example: Merging two callback managers.

>  >     from langchain_core.callbacks.manager import CallbackManager, trace_as_chain_group >     from langchain_core.callbacks.stdout import StdOutCallbackHandler >      >     manager = CallbackManager(handlers=[StdOutCallbackHandler()], tags=["tag2"]) >     with trace_as_chain_group("My Group Name", tags=["tag1"]) as group_manager: >         merged_manager = group_manager.merge(manager) >         print(merged_manager.handlers) >         # [ >         #    <langchain_core.callbacks.stdout.StdOutCallbackHandler object at ...>, >         #    <langchain_core.callbacks.streaming_stdout.StreamingStdOutCallbackHandler object at ...>, >         # ] >      >         print(merged_manager.tags) >         #    ['tag2', 'tag1'] >     

on\_chain\_start\(

    _serialized : dict\[str, Any\]_,     _inputs : dict\[str, Any\]_,     _\*_ ,     _run\_id : UUID_,     _parent\_run\_id : UUID | None = None_,     _tags : list\[str\] | None = None_,     _metadata : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → Any\#     

Run when a chain starts running.

Parameters:     

  * **serialized** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The serialized chain.

  * **inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The inputs.

  * **run\_id** \(_UUID_\) – The run ID. This is the ID of the current run.

  * **parent\_run\_id** \(_UUID_\) – The parent run ID. This is the ID of the parent run.

  * **tags** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\) – The tags.

  * **metadata** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\) – The metadata.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

Any

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

on\_llm\_start\(

    _serialized : dict\[str, Any\]_,     _prompts : list\[str\]_,     _\*_ ,     _run\_id : UUID_,     _parent\_run\_id : UUID | None = None_,     _tags : list\[str\] | None = None_,     _metadata : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → Any\#     

Run when LLM starts running.

Attention

This method is called for non-chat models \(regular LLMs\). If you’re implementing a handler for a chat model, you should use `on_chat_model_start` instead.

Parameters:     

  * **serialized** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The serialized LLM.

  * **prompts** \(_list_ _\[__str_ _\]_\) – The prompts.

  * **run\_id** \(_UUID_\) – The run ID. This is the ID of the current run.

  * **parent\_run\_id** \(_UUID_\) – The parent run ID. This is the ID of the parent run.

  * **tags** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\) – The tags.

  * **metadata** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\) – The metadata.

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

remove\_handler\(

    _handler : [BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/base.html#BaseCallbackManager.remove_handler)\#     

Remove a handler from the callback manager.

Parameters:     

**handler** \([_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\) – The handler to remove.

Return type:     

None

remove\_metadata\(_keys : list\[str\]_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/base.html#BaseCallbackManager.remove_metadata)\#     

Remove metadata from the callback manager.

Parameters:     

**keys** \(_list_ _\[__str_ _\]_\) – The keys to remove.

Return type:     

None

remove\_tags\(_tags : list\[str\]_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/base.html#BaseCallbackManager.remove_tags)\#     

Remove tags from the callback manager.

Parameters:     

**tags** \(_list_ _\[__str_ _\]_\) – The tags to remove.

Return type:     

None

set\_handler\(

    _handler : [BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")_,     _inherit : bool = True_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/base.html#BaseCallbackManager.set_handler)\#     

Set handler as the only handler on the callback manager.

Parameters:     

  * **handler** \([_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\) – The handler to set.

  * **inherit** \(_bool_\) – Whether to inherit the handler. Default is True.

Return type:     

None

set\_handlers\(

    _handlers : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\]_,     _inherit : bool = True_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/base.html#BaseCallbackManager.set_handlers)\#     

Set handlers as the only handlers on the callback manager.

Parameters:     

  * **handlers** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]_\) – The handlers to set.

  * **inherit** \(_bool_\) – Whether to inherit the handlers. Default is True.

Return type:     

None

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)