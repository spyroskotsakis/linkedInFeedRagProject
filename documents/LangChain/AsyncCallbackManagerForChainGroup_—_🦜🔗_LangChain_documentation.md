# AsyncCallbackManagerForChainGroup — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForChainGroup.html
**Word Count:** 798
**Links Count:** 246
**Scraped:** 2025-07-21 07:54:58
**Status:** completed

---

# AsyncCallbackManagerForChainGroup\#

_class _langchain\_core.callbacks.manager.AsyncCallbackManagerForChainGroup\(

    _handlers : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\]_,     _inheritable\_handlers : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | None = None_,     _parent\_run\_id : UUID | None = None_,     _\*_ ,     _parent\_run\_manager : [AsyncCallbackManagerForChainRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun "langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun")_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/manager.html#AsyncCallbackManagerForChainGroup)\#     

Async callback manager for the chain group.

Initialize the async callback manager.

Parameters:     

  * **handlers** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]_\) – The list of handlers.

  * **inheritable\_handlers** \(_Optional_ _\[__list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__\]_\) – The list of inheritable handlers. Defaults to None.

  * **parent\_run\_id** \(_Optional_ _\[__UUID_ _\]_\) – The ID of the parent run. Defaults to None.

  * **parent\_run\_manager** \([_AsyncCallbackManagerForChainRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun "langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun")\) – The parent run manager.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Attributes

`is_async` | Return whether the handler is async.   ---|---      Methods

`__init__`\(handlers\[, inheritable\_handlers, ...\]\) | Initialize the async callback manager.   ---|---   `add_handler`\(handler\[, inherit\]\) | Add a handler to the callback manager.   `add_metadata`\(metadata\[, inherit\]\) | Add metadata to the callback manager.   `add_tags`\(tags\[, inherit\]\) | Add tags to the callback manager.   `configure`\(\[inheritable\_callbacks, ...\]\) | Configure the async callback manager.   `copy`\(\) | Copy the async callback manager.   `merge`\(other\) | Merge the group callback manager with another callback manager.   `on_chain_end`\(outputs, \*\*kwargs\) | Run when traced chain group ends.   `on_chain_error`\(error, \*\*kwargs\) | Run when chain errors.   `on_chain_start`\(serialized, inputs\[, run\_id\]\) | Async run when chain starts running.   `on_chat_model_start`\(serialized, messages\[, ...\]\) | Async run when LLM starts running.   `on_custom_event`\(name, data\[, run\_id\]\) | Dispatch an adhoc event to the handlers \(async version\).   `on_llm_start`\(serialized, prompts\[, run\_id\]\) | Run when LLM starts running.   `on_retriever_start`\(serialized, query\[, ...\]\) | Run when the retriever starts running.   `on_tool_start`\(serialized, input\_str\[, ...\]\) | Run when the tool starts running.   `remove_handler`\(handler\) | Remove a handler from the callback manager.   `remove_metadata`\(keys\) | Remove metadata from the callback manager.   `remove_tags`\(tags\) | Remove tags from the callback manager.   `set_handler`\(handler\[, inherit\]\) | Set handler as the only handler on the callback manager.   `set_handlers`\(handlers\[, inherit\]\) | Set handlers as the only handlers on the callback manager.      \_\_init\_\_\(

    _handlers : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\]_,     _inheritable\_handlers : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | None = None_,     _parent\_run\_id : UUID | None = None_,     _\*_ ,     _parent\_run\_manager : [AsyncCallbackManagerForChainRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun "langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun")_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/manager.html#AsyncCallbackManagerForChainGroup.__init__)\#     

Initialize the async callback manager.

Parameters:     

  * **handlers** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]_\) – The list of handlers.

  * **inheritable\_handlers** \(_Optional_ _\[__list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__\]_\) – The list of inheritable handlers. Defaults to None.

  * **parent\_run\_id** \(_Optional_ _\[__UUID_ _\]_\) – The ID of the parent run. Defaults to None.

  * **parent\_run\_manager** \([_AsyncCallbackManagerForChainRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun "langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun")\) – The parent run manager.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

None

add\_handler\(

    _handler : [BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")_,     _inherit : bool = True_, \) → None\#     

Add a handler to the callback manager.

Parameters:     

  * **handler** \([_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\) – The handler to add.

  * **inherit** \(_bool_\) – Whether to inherit the handler. Default is True.

Return type:     

None

add\_metadata\(

    _metadata : dict\[str, Any\]_,     _inherit : bool = True_, \) → None\#     

Add metadata to the callback manager.

Parameters:     

  * **metadata** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The metadata to add.

  * **inherit** \(_bool_\) – Whether to inherit the metadata. Default is True.

Return type:     

None

add\_tags\(

    _tags : list\[str\]_,     _inherit : bool = True_, \) → None\#     

Add tags to the callback manager.

Parameters:     

  * **tags** \(_list_ _\[__str_ _\]_\) – The tags to add.

  * **inherit** \(_bool_\) – Whether to inherit the tags. Default is True.

Return type:     

None

_classmethod _configure\(

    _inheritable\_callbacks : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _local\_callbacks : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _verbose : bool = False_,     _inheritable\_tags : list\[str\] | None = None_,     _local\_tags : list\[str\] | None = None_,     _inheritable\_metadata : dict\[str, Any\] | None = None_,     _local\_metadata : dict\[str, Any\] | None = None_, \) → [AsyncCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManager.html#langchain_core.callbacks.manager.AsyncCallbackManager "langchain_core.callbacks.manager.AsyncCallbackManager")\#     

Configure the async callback manager.

Parameters:     

  * **inheritable\_callbacks** \(_Optional_ _\[__Callbacks_ _\]__,__optional_\) – The inheritable callbacks. Defaults to None.

  * **local\_callbacks** \(_Optional_ _\[__Callbacks_ _\]__,__optional_\) – The local callbacks. Defaults to None.

  * **verbose** \(_bool_ _,__optional_\) – Whether to enable verbose mode. Defaults to False.

  * **inheritable\_tags** \(_Optional_ _\[__list_ _\[__str_ _\]__\]__,__optional_\) – The inheritable tags. Defaults to None.

  * **local\_tags** \(_Optional_ _\[__list_ _\[__str_ _\]__\]__,__optional_\) – The local tags. Defaults to None.

  * **inheritable\_metadata** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]__,__optional_\) – The inheritable metadata. Defaults to None.

  * **local\_metadata** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]__,__optional_\) – The local metadata. Defaults to None.

Returns:     

The configured async callback manager.

Return type:     

[AsyncCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManager.html#langchain_core.callbacks.manager.AsyncCallbackManager "langchain_core.callbacks.manager.AsyncCallbackManager")

copy\(\) → AsyncCallbackManagerForChainGroup[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/manager.html#AsyncCallbackManagerForChainGroup.copy)\#     

Copy the async callback manager.

Return type:     

_AsyncCallbackManagerForChainGroup_

merge\(

    _other : [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager")_, \) → AsyncCallbackManagerForChainGroup[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/manager.html#AsyncCallbackManagerForChainGroup.merge)\#     

Merge the group callback manager with another callback manager.

Overwrites the merge method in the base class to ensure that the parent run manager is preserved. Keeps the parent\_run\_manager from the current object.

Returns:     

A copy of the current AsyncCallbackManagerForChainGroup     

with the handlers, tags, etc. of the other callback manager merged in.

Return type:     

AsyncCallbackManagerForChainGroup

Parameters:     

  * **self** \(_AsyncCallbackManagerForChainGroup_\)

  * **other** \([_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager")\)

Example: Merging two callback managers.

>  >     from langchain_core.callbacks.manager import CallbackManager, atrace_as_chain_group >     from langchain_core.callbacks.stdout import StdOutCallbackHandler >      >     manager = CallbackManager(handlers=[StdOutCallbackHandler()], tags=["tag2"]) >     async with atrace_as_chain_group("My Group Name", tags=["tag1"]) as group_manager: >         merged_manager = group_manager.merge(manager) >         print(type(merged_manager)) >         # <class 'langchain_core.callbacks.manager.AsyncCallbackManagerForChainGroup'> >      >         print(merged_manager.handlers) >         # [ >         #    <langchain_core.callbacks.stdout.LangChainTracer object at ...>, >         #    <langchain_core.callbacks.streaming_stdout.StdOutCallbackHandler object at ...>, >         # ] >      >         print(merged_manager.tags) >         #    ['tag2', 'tag1'] >     

_async _on\_chain\_end\(

    _outputs : dict\[str, Any\] | Any_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/manager.html#AsyncCallbackManagerForChainGroup.on_chain_end)\#     

Run when traced chain group ends.

Parameters:     

  * **outputs** \(_Union_ _\[__dict_ _\[__str_ _,__Any_ _\]__,__Any_ _\]_\) – The outputs of the chain.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

None

_async _on\_chain\_error\(

    _error : BaseException_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/manager.html#AsyncCallbackManagerForChainGroup.on_chain_error)\#     

Run when chain errors.

Parameters:     

  * **error** \(_Exception_ _or_ _KeyboardInterrupt_\) – The error.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

None

_async _on\_chain\_start\(

    _serialized : dict\[str, Any\] | None_,     _inputs : dict\[str, Any\] | Any_,     _run\_id : UUID | None = None_,     _\*\* kwargs: Any_, \) → [AsyncCallbackManagerForChainRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun "langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun")\#     

Async run when chain starts running.

Parameters:     

  * **serialized** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\) – The serialized chain.

  * **inputs** \(_Union_ _\[__dict_ _\[__str_ _,__Any_ _\]__,__Any_ _\]_\) – The inputs to the chain.

  * **run\_id** \(_UUID_ _,__optional_\) – The ID of the run. Defaults to None.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Returns:     

The async callback manager     

for the chain run.

Return type:     

[AsyncCallbackManagerForChainRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun "langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun")

_async _on\_chat\_model\_start\(

    _serialized : dict\[str, Any\]_,     _messages : list\[list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]\]_,     _run\_id : UUID | None = None_,     _\*\* kwargs: Any_, \) → list\[[AsyncCallbackManagerForLLMRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun "langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun")\]\#     

Async run when LLM starts running.

Parameters:     

  * **serialized** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The serialized LLM.

  * **messages** \(_list_ _\[__list_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]__\]_\) – The list of messages.

  * **run\_id** \(_UUID_ _,__optional_\) – The ID of the run. Defaults to None.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Returns:     

The list of     

async callback managers, one for each LLM Run corresponding to each inner message list.

Return type:     

list\[[AsyncCallbackManagerForLLMRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun "langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun")\]

_async _on\_custom\_event\(

    _name : str_,     _data : Any_,     _run\_id : UUID | None = None_,     _\*\* kwargs: Any_, \) → None\#     

Dispatch an adhoc event to the handlers \(async version\).

This event should NOT be used in any internal LangChain code. The event is meant specifically for users of the library to dispatch custom events that are tailored to their application.

Parameters:     

  * **name** \(_str_\) – The name of the adhoc event.

  * **data** \(_Any_\) – The data for the adhoc event.

  * **run\_id** \(_UUID_ _|__None_\) – The ID of the run. Defaults to None.

  * **kwargs** \(_Any_\)

Return type:     

None

Added in version 0.2.14.

_async _on\_llm\_start\(

    _serialized : dict\[str, Any\]_,     _prompts : list\[str\]_,     _run\_id : UUID | None = None_,     _\*\* kwargs: Any_, \) → list\[[AsyncCallbackManagerForLLMRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun "langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun")\]\#     

Run when LLM starts running.

Parameters:     

  * **serialized** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The serialized LLM.

  * **prompts** \(_list_ _\[__str_ _\]_\) – The list of prompts.

  * **run\_id** \(_UUID_ _,__optional_\) – The ID of the run. Defaults to None.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Returns:     

The list of async     

callback managers, one for each LLM Run corresponding to each prompt.

Return type:     

list\[[AsyncCallbackManagerForLLMRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun "langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun")\]

_async _on\_retriever\_start\(

    _serialized : dict\[str, Any\] | None_,     _query : str_,     _run\_id : UUID | None = None_,     _parent\_run\_id : UUID | None = None_,     _\*\* kwargs: Any_, \) → [AsyncCallbackManagerForRetrieverRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForRetrieverRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForRetrieverRun "langchain_core.callbacks.manager.AsyncCallbackManagerForRetrieverRun")\#     

Run when the retriever starts running.

Parameters:     

  * **serialized** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\) – The serialized retriever.

  * **query** \(_str_\) – The query.

  * **run\_id** \(_UUID_ _,__optional_\) – The ID of the run. Defaults to None.

  * **parent\_run\_id** \(_UUID_ _,__optional_\) – The ID of the parent run. Defaults to None.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Returns:     

The async callback manager     

for the retriever run.

Return type:     

[AsyncCallbackManagerForRetrieverRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForRetrieverRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForRetrieverRun "langchain_core.callbacks.manager.AsyncCallbackManagerForRetrieverRun")

_async _on\_tool\_start\(

    _serialized : dict\[str, Any\] | None_,     _input\_str : str_,     _run\_id : UUID | None = None_,     _parent\_run\_id : UUID | None = None_,     _\*\* kwargs: Any_, \) → [AsyncCallbackManagerForToolRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForToolRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForToolRun "langchain_core.callbacks.manager.AsyncCallbackManagerForToolRun")\#     

Run when the tool starts running.

Parameters:     

  * **serialized** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\) – The serialized tool.

  * **input\_str** \(_str_\) – The input to the tool.

  * **run\_id** \(_UUID_ _,__optional_\) – The ID of the run. Defaults to None.

  * **parent\_run\_id** \(_UUID_ _,__optional_\) – The ID of the parent run. Defaults to None.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Returns:     

The async callback manager     

for the tool run.

Return type:     

[AsyncCallbackManagerForToolRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForToolRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForToolRun "langchain_core.callbacks.manager.AsyncCallbackManagerForToolRun")

remove\_handler\(

    _handler : [BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")_, \) → None\#     

Remove a handler from the callback manager.

Parameters:     

**handler** \([_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\) – The handler to remove.

Return type:     

None

remove\_metadata\(

    _keys : list\[str\]_, \) → None\#     

Remove metadata from the callback manager.

Parameters:     

**keys** \(_list_ _\[__str_ _\]_\) – The keys to remove.

Return type:     

None

remove\_tags\(

    _tags : list\[str\]_, \) → None\#     

Remove tags from the callback manager.

Parameters:     

**tags** \(_list_ _\[__str_ _\]_\) – The tags to remove.

Return type:     

None

set\_handler\(

    _handler : [BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")_,     _inherit : bool = True_, \) → None\#     

Set handler as the only handler on the callback manager.

Parameters:     

  * **handler** \([_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\) – The handler to set.

  * **inherit** \(_bool_\) – Whether to inherit the handler. Default is True.

Return type:     

None

set\_handlers\(

    _handlers : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\]_,     _inherit : bool = True_, \) → None\#     

Set handlers as the only handlers on the callback manager.

Parameters:     

  * **handlers** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]_\) – The handlers to set.

  * **inherit** \(_bool_\) – Whether to inherit the handlers. Default is True.

Return type:     

None

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)