# CallbackManagerForChainGroup — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForChainGroup.html
**Word Count:** 828
**Links Count:** 246
**Scraped:** 2025-07-21 07:53:34
**Status:** completed

---

# CallbackManagerForChainGroup\#

_class _langchain\_core.callbacks.manager.CallbackManagerForChainGroup\(

    _handlers : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\]_,     _inheritable\_handlers : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | None = None_,     _parent\_run\_id : UUID | None = None_,     _\*_ ,     _parent\_run\_manager : [CallbackManagerForChainRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForChainRun.html#langchain_core.callbacks.manager.CallbackManagerForChainRun "langchain_core.callbacks.manager.CallbackManagerForChainRun")_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/manager.html#CallbackManagerForChainGroup)\#     

Callback manager for the chain group.

Initialize the callback manager.

Parameters:     

  * **handlers** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]_\) – The list of handlers.

  * **inheritable\_handlers** \(_Optional_ _\[__list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__\]_\) – The list of inheritable handlers. Defaults to None.

  * **parent\_run\_id** \(_Optional_ _\[__UUID_ _\]_\) – The ID of the parent run. Defaults to None.

  * **parent\_run\_manager** \([_CallbackManagerForChainRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForChainRun.html#langchain_core.callbacks.manager.CallbackManagerForChainRun "langchain_core.callbacks.manager.CallbackManagerForChainRun")\) – The parent run manager.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Attributes

`is_async` | Whether the callback manager is async.   ---|---      Methods

`__init__`\(handlers\[, inheritable\_handlers, ...\]\) | Initialize the callback manager.   ---|---   `add_handler`\(handler\[, inherit\]\) | Add a handler to the callback manager.   `add_metadata`\(metadata\[, inherit\]\) | Add metadata to the callback manager.   `add_tags`\(tags\[, inherit\]\) | Add tags to the callback manager.   `configure`\(\[inheritable\_callbacks, ...\]\) | Configure the callback manager.   `copy`\(\) | Copy the callback manager.   `merge`\(other\) | Merge the group callback manager with another callback manager.   `on_chain_end`\(outputs, \*\*kwargs\) | Run when traced chain group ends.   `on_chain_error`\(error, \*\*kwargs\) | Run when chain errors.   `on_chain_start`\(serialized, inputs\[, run\_id\]\) | Run when chain starts running.   `on_chat_model_start`\(serialized, messages\[, ...\]\) | Run when chat model starts running.   `on_custom_event`\(name, data\[, run\_id\]\) | Dispatch an adhoc event to the handlers \(async version\).   `on_llm_start`\(serialized, prompts\[, run\_id\]\) | Run when LLM starts running.   `on_retriever_start`\(serialized, query\[, ...\]\) | Run when the retriever starts running.   `on_tool_start`\(serialized, input\_str\[, ...\]\) | Run when tool starts running.   `remove_handler`\(handler\) | Remove a handler from the callback manager.   `remove_metadata`\(keys\) | Remove metadata from the callback manager.   `remove_tags`\(tags\) | Remove tags from the callback manager.   `set_handler`\(handler\[, inherit\]\) | Set handler as the only handler on the callback manager.   `set_handlers`\(handlers\[, inherit\]\) | Set handlers as the only handlers on the callback manager.      \_\_init\_\_\(

    _handlers : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\]_,     _inheritable\_handlers : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | None = None_,     _parent\_run\_id : UUID | None = None_,     _\*_ ,     _parent\_run\_manager : [CallbackManagerForChainRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForChainRun.html#langchain_core.callbacks.manager.CallbackManagerForChainRun "langchain_core.callbacks.manager.CallbackManagerForChainRun")_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/manager.html#CallbackManagerForChainGroup.__init__)\#     

Initialize the callback manager.

Parameters:     

  * **handlers** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]_\) – The list of handlers.

  * **inheritable\_handlers** \(_Optional_ _\[__list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__\]_\) – The list of inheritable handlers. Defaults to None.

  * **parent\_run\_id** \(_Optional_ _\[__UUID_ _\]_\) – The ID of the parent run. Defaults to None.

  * **parent\_run\_manager** \([_CallbackManagerForChainRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForChainRun.html#langchain_core.callbacks.manager.CallbackManagerForChainRun "langchain_core.callbacks.manager.CallbackManagerForChainRun")\) – The parent run manager.

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

    _inheritable\_callbacks : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _local\_callbacks : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _verbose : bool = False_,     _inheritable\_tags : list\[str\] | None = None_,     _local\_tags : list\[str\] | None = None_,     _inheritable\_metadata : dict\[str, Any\] | None = None_,     _local\_metadata : dict\[str, Any\] | None = None_, \) → [CallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManager.html#langchain_core.callbacks.manager.CallbackManager "langchain_core.callbacks.manager.CallbackManager")\#     

Configure the callback manager.

Parameters:     

  * **inheritable\_callbacks** \(_Optional_ _\[__Callbacks_ _\]__,__optional_\) – The inheritable callbacks. Defaults to None.

  * **local\_callbacks** \(_Optional_ _\[__Callbacks_ _\]__,__optional_\) – The local callbacks. Defaults to None.

  * **verbose** \(_bool_ _,__optional_\) – Whether to enable verbose mode. Defaults to False.

  * **inheritable\_tags** \(_Optional_ _\[__list_ _\[__str_ _\]__\]__,__optional_\) – The inheritable tags. Defaults to None.

  * **local\_tags** \(_Optional_ _\[__list_ _\[__str_ _\]__\]__,__optional_\) – The local tags. Defaults to None.

  * **inheritable\_metadata** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]__,__optional_\) – The inheritable metadata. Defaults to None.

  * **local\_metadata** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]__,__optional_\) – The local metadata. Defaults to None.

Returns:     

The configured callback manager.

Return type:     

[CallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManager.html#langchain_core.callbacks.manager.CallbackManager "langchain_core.callbacks.manager.CallbackManager")

copy\(\) → CallbackManagerForChainGroup[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/manager.html#CallbackManagerForChainGroup.copy)\#     

Copy the callback manager.

Return type:     

_CallbackManagerForChainGroup_

merge\(

    _other : [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager")_, \) → CallbackManagerForChainGroup[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/manager.html#CallbackManagerForChainGroup.merge)\#     

Merge the group callback manager with another callback manager.

Overwrites the merge method in the base class to ensure that the parent run manager is preserved. Keeps the parent\_run\_manager from the current object.

Returns:     

A copy of the current object with the     

handlers, tags, and other attributes merged from the other object.

Return type:     

CallbackManagerForChainGroup

Parameters:     

  * **self** \(_CallbackManagerForChainGroup_\)

  * **other** \([_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager")\)

Example: Merging two callback managers.

>  >     from langchain_core.callbacks.manager import CallbackManager, trace_as_chain_group >     from langchain_core.callbacks.stdout import StdOutCallbackHandler >      >     manager = CallbackManager(handlers=[StdOutCallbackHandler()], tags=["tag2"]) >     with trace_as_chain_group("My Group Name", tags=["tag1"]) as group_manager: >         merged_manager = group_manager.merge(manager) >         print(type(merged_manager)) >         # <class 'langchain_core.callbacks.manager.CallbackManagerForChainGroup'> >      >         print(merged_manager.handlers) >         # [ >         #    <langchain_core.callbacks.stdout.LangChainTracer object at ...>, >         #    <langchain_core.callbacks.streaming_stdout.StdOutCallbackHandler object at ...>, >         # ] >      >         print(merged_manager.tags) >         #    ['tag2', 'tag1'] >     

on\_chain\_end\(

    _outputs : dict\[str, Any\] | Any_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/manager.html#CallbackManagerForChainGroup.on_chain_end)\#     

Run when traced chain group ends.

Parameters:     

  * **outputs** \(_Union_ _\[__dict_ _\[__str_ _,__Any_ _\]__,__Any_ _\]_\) – The outputs of the chain.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

None

on\_chain\_error\(

    _error : BaseException_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/manager.html#CallbackManagerForChainGroup.on_chain_error)\#     

Run when chain errors.

Parameters:     

  * **error** \(_Exception_ _or_ _KeyboardInterrupt_\) – The error.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

None

on\_chain\_start\(

    _serialized : dict\[str, Any\] | None_,     _inputs : dict\[str, Any\] | Any_,     _run\_id : UUID | None = None_,     _\*\* kwargs: Any_, \) → [CallbackManagerForChainRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForChainRun.html#langchain_core.callbacks.manager.CallbackManagerForChainRun "langchain_core.callbacks.manager.CallbackManagerForChainRun")\#     

Run when chain starts running.

Parameters:     

  * **serialized** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\) – The serialized chain.

  * **inputs** \(_Union_ _\[__dict_ _\[__str_ _,__Any_ _\]__,__Any_ _\]_\) – The inputs to the chain.

  * **run\_id** \(_UUID_ _,__optional_\) – The ID of the run. Defaults to None.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Returns:     

The callback manager for the chain run.

Return type:     

[CallbackManagerForChainRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForChainRun.html#langchain_core.callbacks.manager.CallbackManagerForChainRun "langchain_core.callbacks.manager.CallbackManagerForChainRun")

on\_chat\_model\_start\(

    _serialized : dict\[str, Any\]_,     _messages : list\[list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]\]_,     _run\_id : UUID | None = None_,     _\*\* kwargs: Any_, \) → list\[[CallbackManagerForLLMRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForLLMRun.html#langchain_core.callbacks.manager.CallbackManagerForLLMRun "langchain_core.callbacks.manager.CallbackManagerForLLMRun")\]\#     

Run when chat model starts running.

Parameters:     

  * **serialized** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The serialized LLM.

  * **messages** \(_list_ _\[__list_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]__\]_\) – The list of messages.

  * **run\_id** \(_UUID_ _,__optional_\) – The ID of the run. Defaults to None.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Returns:     

A callback manager for each     

list of messages as an LLM run.

Return type:     

list\[[CallbackManagerForLLMRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForLLMRun.html#langchain_core.callbacks.manager.CallbackManagerForLLMRun "langchain_core.callbacks.manager.CallbackManagerForLLMRun")\]

on\_custom\_event\(

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

on\_llm\_start\(

    _serialized : dict\[str, Any\]_,     _prompts : list\[str\]_,     _run\_id : UUID | None = None_,     _\*\* kwargs: Any_, \) → list\[[CallbackManagerForLLMRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForLLMRun.html#langchain_core.callbacks.manager.CallbackManagerForLLMRun "langchain_core.callbacks.manager.CallbackManagerForLLMRun")\]\#     

Run when LLM starts running.

Parameters:     

  * **serialized** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The serialized LLM.

  * **prompts** \(_list_ _\[__str_ _\]_\) – The list of prompts.

  * **run\_id** \(_UUID_ _,__optional_\) – The ID of the run. Defaults to None.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Returns:     

A callback manager for each     

prompt as an LLM run.

Return type:     

list\[[CallbackManagerForLLMRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForLLMRun.html#langchain_core.callbacks.manager.CallbackManagerForLLMRun "langchain_core.callbacks.manager.CallbackManagerForLLMRun")\]

on\_retriever\_start\(

    _serialized : dict\[str, Any\] | None_,     _query : str_,     _run\_id : UUID | None = None_,     _parent\_run\_id : UUID | None = None_,     _\*\* kwargs: Any_, \) → [CallbackManagerForRetrieverRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForRetrieverRun.html#langchain_core.callbacks.manager.CallbackManagerForRetrieverRun "langchain_core.callbacks.manager.CallbackManagerForRetrieverRun")\#     

Run when the retriever starts running.

Parameters:     

  * **serialized** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\) – The serialized retriever.

  * **query** \(_str_\) – The query.

  * **run\_id** \(_UUID_ _,__optional_\) – The ID of the run. Defaults to None.

  * **parent\_run\_id** \(_UUID_ _,__optional_\) – The ID of the parent run. Defaults to None.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

[_CallbackManagerForRetrieverRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForRetrieverRun.html#langchain_core.callbacks.manager.CallbackManagerForRetrieverRun "langchain_core.callbacks.manager.CallbackManagerForRetrieverRun")

on\_tool\_start\(

    _serialized : dict\[str, Any\] | None_,     _input\_str : str_,     _run\_id : UUID | None = None_,     _parent\_run\_id : UUID | None = None_,     _inputs : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → [CallbackManagerForToolRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForToolRun.html#langchain_core.callbacks.manager.CallbackManagerForToolRun "langchain_core.callbacks.manager.CallbackManagerForToolRun")\#     

Run when tool starts running.

Parameters:     

  * **serialized** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Serialized representation of the tool.

  * **input\_str** \(_str_\) – The input to the tool as a string. Non-string inputs are cast to strings.

  * **run\_id** \(_UUID_ _|__None_\) – ID for the run. Defaults to None.

  * **parent\_run\_id** \(_UUID_ _|__None_\) – The ID of the parent run. Defaults to None.

  * **inputs** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – The original input to the tool if provided. Recommended for usage instead of input\_str when the original input is needed. If provided, the inputs are expected to be formatted as a dict. The keys will correspond to the named-arguments in the tool.

  * **\*\*kwargs** \(_Any_\) – The keyword arguments to pass to the event handler

Returns:     

The callback manager for the tool run.

Return type:     

[CallbackManagerForToolRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForToolRun.html#langchain_core.callbacks.manager.CallbackManagerForToolRun "langchain_core.callbacks.manager.CallbackManagerForToolRun")

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