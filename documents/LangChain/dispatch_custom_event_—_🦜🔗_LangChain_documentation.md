# dispatch_custom_event — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.dispatch_custom_event.html
**Word Count:** 68
**Links Count:** 139
**Scraped:** 2025-07-21 07:53:34
**Status:** completed

---

# dispatch\_custom\_event\#

langchain\_core.callbacks.manager.dispatch\_custom\_event\(

    _name : str_,     _data : Any_,     _\*_ ,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/manager.html#dispatch_custom_event)\#     

Dispatch an adhoc event.

Parameters:     

  * **name** \(_str_\) – The name of the adhoc event.

  * **data** \(_Any_\) – The data for the adhoc event. Free form data. Ideally should be JSON serializable to avoid serialization issues downstream, but this is not enforced.

  * **config** \(_Optional_ _\[_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _\]_\) – Optional config object. Mirrors the async API but not strictly needed.

Return type:     

None

Example               from langchain_core.callbacks import BaseCallbackHandler     from langchain_core.callbacks import dispatch_custom_event     from langchain_core.runnable import RunnableLambda          class CustomCallbackManager(BaseCallbackHandler):         def on_custom_event(             self,             name: str,             data: Any,             *,             run_id: UUID,             tags: Optional[list[str]] = None,             metadata: Optional[dict[str, Any]] = None,             **kwargs: Any,         ) -> None:             print(f"Received custom event: {name} with data: {data}")          def foo(inputs):         dispatch_custom_event("my_event", {"bar": "buzz})         return inputs          foo_ = RunnableLambda(foo)     foo_.invoke({"a": "1"}, {"callbacks": [CustomCallbackManager()]})     

Added in version 0.2.15.

Examples using dispatch\_custom\_event

  * [How to dispatch custom callback events](https://python.langchain.com/docs/how_to/callbacks_custom_events/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)