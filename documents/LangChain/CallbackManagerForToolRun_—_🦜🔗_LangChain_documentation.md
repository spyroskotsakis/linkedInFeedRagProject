# CallbackManagerForToolRun — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForToolRun.html
**Word Count:** 354
**Links Count:** 175
**Scraped:** 2025-07-21 07:54:58
**Status:** completed

---

# CallbackManagerForToolRun\#

_class _langchain\_core.callbacks.manager.CallbackManagerForToolRun\(

    _\*_ ,     _run\_id : UUID_,     _handlers : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\]_,     _inheritable\_handlers : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\]_,     _parent\_run\_id : UUID | None = None_,     _tags : list\[str\] | None = None_,     _inheritable\_tags : list\[str\] | None = None_,     _metadata : dict\[str, Any\] | None = None_,     _inheritable\_metadata : dict\[str, Any\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/manager.html#CallbackManagerForToolRun)\#     

Callback manager for tool run.

Initialize the run manager.

Parameters:     

  * **run\_id** \(_UUID_\) – The ID of the run.

  * **handlers** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]_\) – The list of handlers.

  * **inheritable\_handlers** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]_\) – The list of inheritable handlers.

  * **parent\_run\_id** \(_UUID_ _,__optional_\) – The ID of the parent run. Defaults to None.

  * **tags** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\) – The list of tags. Defaults to None.

  * **inheritable\_tags** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\) – The list of inheritable tags. Defaults to None.

  * **metadata** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\) – The metadata. Defaults to None.

  * **inheritable\_metadata** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\) – The inheritable metadata. Defaults to None.

Methods

`__init__`\(\*, run\_id, handlers, ...\[, ...\]\) | Initialize the run manager.   ---|---   `get_child`\(\[tag\]\) | Get a child callback manager.   `get_noop_manager`\(\) | Return a manager that doesn't perform any operations.   `on_custom_event`\(name, data, \*, run\_id\[, ...\]\) | Override to define a handler for a custom event.   `on_retry`\(retry\_state, \*\*kwargs\) | Run when a retry is received.   `on_text`\(text, \*\*kwargs\) | Run when a text is received.   `on_tool_end`\(output, \*\*kwargs\) | Run when the tool ends running.   `on_tool_error`\(error, \*\*kwargs\) | Run when tool errors.      \_\_init\_\_\(

    _\*_ ,     _run\_id : UUID_,     _handlers : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\]_,     _inheritable\_handlers : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\]_,     _parent\_run\_id : UUID | None = None_,     _tags : list\[str\] | None = None_,     _inheritable\_tags : list\[str\] | None = None_,     _metadata : dict\[str, Any\] | None = None_,     _inheritable\_metadata : dict\[str, Any\] | None = None_, \) → None\#     

Initialize the run manager.

Parameters:     

  * **run\_id** \(_UUID_\) – The ID of the run.

  * **handlers** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]_\) – The list of handlers.

  * **inheritable\_handlers** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]_\) – The list of inheritable handlers.

  * **parent\_run\_id** \(_UUID_ _,__optional_\) – The ID of the parent run. Defaults to None.

  * **tags** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\) – The list of tags. Defaults to None.

  * **inheritable\_tags** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\) – The list of inheritable tags. Defaults to None.

  * **metadata** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\) – The metadata. Defaults to None.

  * **inheritable\_metadata** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\) – The inheritable metadata. Defaults to None.

Return type:     

None

get\_child\(

    _tag : str | None = None_, \) → [CallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManager.html#langchain_core.callbacks.manager.CallbackManager "langchain_core.callbacks.manager.CallbackManager")\#     

Get a child callback manager.

Parameters:     

**tag** \(_str_ _,__optional_\) – The tag for the child callback manager. Defaults to None.

Returns:     

The child callback manager.

Return type:     

[CallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManager.html#langchain_core.callbacks.manager.CallbackManager "langchain_core.callbacks.manager.CallbackManager")

_classmethod _get\_noop\_manager\(\) → Self\#     

Return a manager that doesn’t perform any operations.

Returns:     

The noop manager.

Return type:     

[BaseRunManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.BaseRunManager.html#langchain_core.callbacks.manager.BaseRunManager "langchain_core.callbacks.manager.BaseRunManager")

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

on\_retry\(

    _retry\_state : RetryCallState_,     _\*\* kwargs: Any_, \) → None\#     

Run when a retry is received.

Parameters:     

  * **retry\_state** \(_RetryCallState_\) – The retry state.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

None

on\_text\(

    _text : str_,     _\*\* kwargs: Any_, \) → Any\#     

Run when a text is received.

Parameters:     

  * **text** \(_str_\) – The received text.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Returns:     

The result of the callback.

Return type:     

Any

on\_tool\_end\(

    _output : Any_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/manager.html#CallbackManagerForToolRun.on_tool_end)\#     

Run when the tool ends running.

Parameters:     

  * **output** \(_Any_\) – The output of the tool.

  * **\*\*kwargs** \(_Any_\) – The keyword arguments to pass to the event handler

Return type:     

None

on\_tool\_error\(

    _error : BaseException_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/manager.html#CallbackManagerForToolRun.on_tool_error)\#     

Run when tool errors.

Parameters:     

  * **error** \(_Exception_ _or_ _KeyboardInterrupt_\) – The error.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

None

Examples using CallbackManagerForToolRun

  * [How to add a semantic layer over graph database](https://python.langchain.com/docs/how_to/graph_semantic/)

  * [How to create tools](https://python.langchain.com/docs/how_to/custom_tools/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)