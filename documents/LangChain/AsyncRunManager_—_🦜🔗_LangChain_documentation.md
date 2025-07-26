# AsyncRunManager — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncRunManager.html
**Word Count:** 286
**Links Count:** 168
**Scraped:** 2025-07-21 07:53:06
**Status:** completed

---

# AsyncRunManager\#

_class _langchain\_core.callbacks.manager.AsyncRunManager\(

    _\*_ ,     _run\_id : UUID_,     _handlers : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\]_,     _inheritable\_handlers : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\]_,     _parent\_run\_id : UUID | None = None_,     _tags : list\[str\] | None = None_,     _inheritable\_tags : list\[str\] | None = None_,     _metadata : dict\[str, Any\] | None = None_,     _inheritable\_metadata : dict\[str, Any\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/manager.html#AsyncRunManager)\#     

Async Run Manager.

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

`__init__`\(\*, run\_id, handlers, ...\[, ...\]\) | Initialize the run manager.   ---|---   `get_noop_manager`\(\) | Return a manager that doesn't perform any operations.   `get_sync`\(\) | Get the equivalent sync RunManager.   `on_custom_event`\(name, data, \*, run\_id\[, ...\]\) | Override to define a handler for a custom event.   `on_retry`\(retry\_state, \*\*kwargs\) | Async run when a retry is received.   `on_text`\(text, \*\*kwargs\) | Run when a text is received.      \_\_init\_\_\(

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

_classmethod _get\_noop\_manager\(\) → Self\#     

Return a manager that doesn’t perform any operations.

Returns:     

The noop manager.

Return type:     

[BaseRunManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.BaseRunManager.html#langchain_core.callbacks.manager.BaseRunManager "langchain_core.callbacks.manager.BaseRunManager")

_abstractmethod _get\_sync\(\) → [RunManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.RunManager.html#langchain_core.callbacks.manager.RunManager "langchain_core.callbacks.manager.RunManager")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/manager.html#AsyncRunManager.get_sync)\#     

Get the equivalent sync RunManager.

Returns:     

The sync RunManager.

Return type:     

[RunManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.RunManager.html#langchain_core.callbacks.manager.RunManager "langchain_core.callbacks.manager.RunManager")

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

_async _on\_retry\(

    _retry\_state : RetryCallState_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/manager.html#AsyncRunManager.on_retry)\#     

Async run when a retry is received.

Parameters:     

  * **retry\_state** \(_RetryCallState_\) – The retry state.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

None

_async _on\_text\(

    _text : str_,     _\*\* kwargs: Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/manager.html#AsyncRunManager.on_text)\#     

Run when a text is received.

Parameters:     

  * **text** \(_str_\) – The received text.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Returns:     

The result of the callback.

Return type:     

Any

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)