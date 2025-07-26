# handle_event — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.handle_event.html
**Word Count:** 80
**Links Count:** 138
**Scraped:** 2025-07-21 07:55:55
**Status:** completed

---

# handle\_event\#

langchain\_core.callbacks.manager.handle\_event\(

    _handlers : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\]_,     _event\_name : str_,     _ignore\_condition\_name : str | None_,     _\* args: Any_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/manager.html#handle_event)\#     

Generic event handler for CallbackManager.

Note: This function is used by LangServe to handle events.

Parameters:     

  * **handlers** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]_\) – The list of handlers that will handle the event.

  * **event\_name** \(_str_\) – The name of the event \(e.g., “on\_llm\_start”\).

  * **ignore\_condition\_name** \(_str_ _|__None_\) – Name of the attribute defined on handler that if True will cause the handler to be skipped for the given event.

  * **\*args** \(_Any_\) – The arguments to pass to the event handler.

  * **\*\*kwargs** \(_Any_\) – The keyword arguments to pass to the event handler

Return type:     

None

__On this page