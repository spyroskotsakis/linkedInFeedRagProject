# atrace_as_chain_group — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.atrace_as_chain_group.html
**Word Count:** 150
**Links Count:** 140
**Scraped:** 2025-07-21 07:53:06
**Status:** completed

---

# atrace\_as\_chain\_group\#

langchain\_core.callbacks.manager.atrace\_as\_chain\_group\(

    _group\_name : str_,     _callback\_manager : [AsyncCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManager.html#langchain_core.callbacks.manager.AsyncCallbackManager "langchain_core.callbacks.manager.AsyncCallbackManager") | None = None_,     _\*_ ,     _inputs : dict\[str, Any\] | None = None_,     _project\_name : str | None = None_,     _example\_id : str | UUID | None = None_,     _run\_id : UUID | None = None_,     _tags : list\[str\] | None = None_,     _metadata : dict\[str, Any\] | None = None_, \) → AsyncGenerator\[[AsyncCallbackManagerForChainGroup](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForChainGroup.html#langchain_core.callbacks.manager.AsyncCallbackManagerForChainGroup "langchain_core.callbacks.manager.AsyncCallbackManagerForChainGroup"), None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/manager.html#atrace_as_chain_group)\#     

Get an async callback manager for a chain group in a context manager.

Useful for grouping different async calls together as a single run even if they aren’t composed in a single chain.

Parameters:     

  * **group\_name** \(_str_\) – The name of the chain group.

  * **callback\_manager** \([_AsyncCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManager.html#langchain_core.callbacks.manager.AsyncCallbackManager "langchain_core.callbacks.manager.AsyncCallbackManager") _,__optional_\) – The async callback manager to use, which manages tracing and other callback behavior. Defaults to None.

  * **inputs** \(_dict_ _\[__str_ _,__Any_ _\]__,__optional_\) – The inputs to the chain group. Defaults to None.

  * **project\_name** \(_str_ _,__optional_\) – The name of the project. Defaults to None.

  * **example\_id** \(_str_ _or_ _UUID_ _,__optional_\) – The ID of the example. Defaults to None.

  * **run\_id** \(_UUID_ _,__optional_\) – The ID of the run.

  * **tags** \(_list_ _\[__str_ _\]__,__optional_\) – The inheritable tags to apply to all runs. Defaults to None.

  * **metadata** \(_dict_ _\[__str_ _,__Any_ _\]__,__optional_\) – The metadata to apply to all runs. Defaults to None.

Returns:     

The async callback manager for the chain group.

Return type:     

[AsyncCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManager.html#langchain_core.callbacks.manager.AsyncCallbackManager "langchain_core.callbacks.manager.AsyncCallbackManager")

Note: must have LANGCHAIN\_TRACING\_V2 env var set to true to see the trace in LangSmith.

Example               llm_input = "Foo"     async with atrace_as_chain_group("group_name", inputs={"input": llm_input}) as manager:         # Use the async callback manager for the chain group         res = await llm.ainvoke(llm_input, {"callbacks": manager})         await manager.on_chain_end({"output": res})     

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)