# AsyncCallbackManagerForRetrieverRun — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForRetrieverRun.html
**Word Count:** 347
**Links Count:** 181
**Scraped:** 2025-07-21 07:54:29
**Status:** completed

---

# AsyncCallbackManagerForRetrieverRun\#

_class _langchain\_core.callbacks.manager.AsyncCallbackManagerForRetrieverRun\(

    _\*_ ,     _run\_id : UUID_,     _handlers : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\]_,     _inheritable\_handlers : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\]_,     _parent\_run\_id : UUID | None = None_,     _tags : list\[str\] | None = None_,     _inheritable\_tags : list\[str\] | None = None_,     _metadata : dict\[str, Any\] | None = None_,     _inheritable\_metadata : dict\[str, Any\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/manager.html#AsyncCallbackManagerForRetrieverRun)\#     

Async callback manager for retriever run.

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

`__init__`\(\*, run\_id, handlers, ...\[, ...\]\) | Initialize the run manager.   ---|---   `get_child`\(\[tag\]\) | Get a child callback manager.   `get_noop_manager`\(\) | Return a manager that doesn't perform any operations.   `get_sync`\(\) | Get the equivalent sync RunManager.   `on_custom_event`\(name, data, \*, run\_id\[, ...\]\) | Override to define a handler for a custom event.   `on_retriever_end`\(documents, \*\*kwargs\) | Run when the retriever ends running.   `on_retriever_error`\(error, \*\*kwargs\) | Run when retriever errors.   `on_retry`\(retry\_state, \*\*kwargs\) | Async run when a retry is received.   `on_text`\(text, \*\*kwargs\) | Run when a text is received.      \_\_init\_\_\(

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

    _tag : str | None = None_, \) → [AsyncCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManager.html#langchain_core.callbacks.manager.AsyncCallbackManager "langchain_core.callbacks.manager.AsyncCallbackManager")\#     

Get a child callback manager.

Parameters:     

**tag** \(_str_ _,__optional_\) – The tag for the child callback manager. Defaults to None.

Returns:     

The child callback manager.

Return type:     

[AsyncCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManager.html#langchain_core.callbacks.manager.AsyncCallbackManager "langchain_core.callbacks.manager.AsyncCallbackManager")

_classmethod _get\_noop\_manager\(\) → Self\#     

Return a manager that doesn’t perform any operations.

Returns:     

The noop manager.

Return type:     

[BaseRunManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.BaseRunManager.html#langchain_core.callbacks.manager.BaseRunManager "langchain_core.callbacks.manager.BaseRunManager")

get\_sync\(\) → [CallbackManagerForRetrieverRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForRetrieverRun.html#langchain_core.callbacks.manager.CallbackManagerForRetrieverRun "langchain_core.callbacks.manager.CallbackManagerForRetrieverRun")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/manager.html#AsyncCallbackManagerForRetrieverRun.get_sync)\#     

Get the equivalent sync RunManager.

Returns:     

The sync RunManager.

Return type:     

[CallbackManagerForRetrieverRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForRetrieverRun.html#langchain_core.callbacks.manager.CallbackManagerForRetrieverRun "langchain_core.callbacks.manager.CallbackManagerForRetrieverRun")

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

_async _on\_retriever\_end\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/manager.html#AsyncCallbackManagerForRetrieverRun.on_retriever_end)\#     

Run when the retriever ends running.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – The retrieved documents.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

None

_async _on\_retriever\_error\(

    _error : BaseException_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/manager.html#AsyncCallbackManagerForRetrieverRun.on_retriever_error)\#     

Run when retriever errors.

Parameters:     

  * **error** \(_BaseException_\) – The error.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

None

_async _on\_retry\(

    _retry\_state : RetryCallState_,     _\*\* kwargs: Any_, \) → None\#     

Async run when a retry is received.

Parameters:     

  * **retry\_state** \(_RetryCallState_\) – The retry state.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

None

_async _on\_text\(

    _text : str_,     _\*\* kwargs: Any_, \) → Any\#     

Run when a text is received.

Parameters:     

  * **text** \(_str_\) – The received text.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Returns:     

The result of the callback.

Return type:     

Any

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)