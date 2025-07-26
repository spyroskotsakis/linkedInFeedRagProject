# identify — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.llmonitor_callback.identify.html
**Word Count:** 28
**Links Count:** 184
**Scraped:** 2025-07-21 08:20:13
**Status:** completed

---

# identify\#

langchain\_community.callbacks.llmonitor\_callback.identify\(

    _user\_id : str_,     _user\_props : Any = None_, \) → [UserContextManager](https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.llmonitor_callback.UserContextManager.html#langchain_community.callbacks.llmonitor_callback.UserContextManager "langchain_community.callbacks.llmonitor_callback.UserContextManager")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/llmonitor_callback.html#identify)\#     

Builds an LLMonitor UserContextManager

Parameters:     

  * **user\_id** \(_-_\) – The user id.

  * **user\_props** \(_-_\) – The user properties.

Returns:     

A context manager that sets the user context.

Return type:     

[_UserContextManager_](https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.llmonitor_callback.UserContextManager.html#langchain_community.callbacks.llmonitor_callback.UserContextManager "langchain_community.callbacks.llmonitor_callback.UserContextManager")

Examples using identify

  * [LLMonitor](https://python.langchain.com/docs/integrations/callbacks/llmonitor/)

__On this page