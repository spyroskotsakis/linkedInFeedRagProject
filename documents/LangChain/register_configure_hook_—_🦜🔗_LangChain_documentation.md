# register_configure_hook — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/tracers/langchain_core.tracers.context.register_configure_hook.html
**Word Count:** 50
**Links Count:** 137
**Scraped:** 2025-07-21 07:55:55
**Status:** completed

---

# register\_configure\_hook\#

langchain\_core.tracers.context.register\_configure\_hook\(

    _context\_var : ContextVar\[Any | None\]_,     _inheritable : bool_,     _handle\_class : type\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | None = None_,     _env\_var : str | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/tracers/context.html#register_configure_hook)\#     

Register a configure hook.

Parameters:     

  * **context\_var** \(_ContextVar_ _\[__Optional_ _\[__Any_ _\]__\]_\) – The context variable.

  * **inheritable** \(_bool_\) – Whether the context variable is inheritable.

  * **handle\_class** \(_Optional_ _\[__Type_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__\]__,__optional_\) – The callback handler class. Defaults to None.

  * **env\_var** \(_Optional_ _\[__str_ _\]__,__optional_\) – The environment variable. Defaults to None.

Raises:     

**ValueError** – If env\_var is set, handle\_class must also be set to a non-None value.

Return type:     

None

__On this page