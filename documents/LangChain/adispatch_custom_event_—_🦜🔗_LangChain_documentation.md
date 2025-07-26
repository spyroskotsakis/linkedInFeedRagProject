# adispatch_custom_event — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.adispatch_custom_event.html
**Word Count:** 120
**Links Count:** 139
**Scraped:** 2025-07-21 07:54:29
**Status:** completed

---

# adispatch\_custom\_event\#

_async _langchain\_core.callbacks.manager.adispatch\_custom\_event\(

    _name : str_,     _data : Any_,     _\*_ ,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/manager.html#adispatch_custom_event)\#     

Dispatch an adhoc event to the handlers.

Parameters:     

  * **name** \(_str_\) – The name of the adhoc event.

  * **data** \(_Any_\) – The data for the adhoc event. Free form data. Ideally should be JSON serializable to avoid serialization issues downstream, but this is not enforced.

  * **config** \(_Optional_ _\[_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _\]_\) – Optional config object. Mirrors the async API but not strictly needed.

Return type:     

None

Example               from langchain_core.callbacks import (         AsyncCallbackHandler,         adispatch_custom_event     )     from langchain_core.runnable import RunnableLambda          class CustomCallbackManager(AsyncCallbackHandler):         async def on_custom_event(             self,             name: str,             data: Any,             *,             run_id: UUID,             tags: Optional[list[str]] = None,             metadata: Optional[dict[str, Any]] = None,             **kwargs: Any,         ) -> None:             print(f"Received custom event: {name} with data: {data}")          callback = CustomCallbackManager()          async def foo(inputs):         await adispatch_custom_event("my_event", {"bar": "buzz})         return inputs          foo_ = RunnableLambda(foo)     await foo_.ainvoke({"a": "1"}, {"callbacks": [CustomCallbackManager()]})     

Example: Use with astream events

>  >     from langchain_core.callbacks import ( >         AsyncCallbackHandler, >         adispatch_custom_event >     ) >     from langchain_core.runnable import RunnableLambda >      >     class CustomCallbackManager(AsyncCallbackHandler): >         async def on_custom_event( >             self, >             name: str, >             data: Any, >             *, >             run_id: UUID, >             tags: Optional[list[str]] = None, >             metadata: Optional[dict[str, Any]] = None, >             **kwargs: Any, >         ) -> None: >             print(f"Received custom event: {name} with data: {data}") >      >     callback = CustomCallbackManager() >      >     async def foo(inputs): >         await adispatch_custom_event("event_type_1", {"bar": "buzz}) >         await adispatch_custom_event("event_type_2", 5) >         return inputs >      >     foo_ = RunnableLambda(foo) >      >     async for event in foo_.ainvoke_stream( >         {"a": "1"}, >         version="v2", >         config={"callbacks": [CustomCallbackManager()]} >     ): >         print(event) >     

Warning

If using python <= 3.10 and async, you MUST specify the config parameter or the function will raise an error. This is due to a limitation in asyncio for python <= 3.10 that prevents LangChain from automatically propagating the config object on the user’s behalf.

Added in version 0.2.15.

Examples using adispatch\_custom\_event

  * [How to dispatch custom callback events](https://python.langchain.com/docs/how_to/callbacks_custom_events/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)