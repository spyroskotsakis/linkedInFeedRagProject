# trace_as_chain_group — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.trace_as_chain_group.html
**Word Count:** 141
**Links Count:** 142
**Scraped:** 2025-07-21 07:53:34
**Status:** completed

---

# trace\_as\_chain\_group\#

langchain\_core.callbacks.manager.trace\_as\_chain\_group\(

    _group\_name : str_,     _callback\_manager : [CallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManager.html#langchain_core.callbacks.manager.CallbackManager "langchain_core.callbacks.manager.CallbackManager") | None = None_,     _\*_ ,     _inputs : dict\[str, Any\] | None = None_,     _project\_name : str | None = None_,     _example\_id : str | UUID | None = None_,     _run\_id : UUID | None = None_,     _tags : list\[str\] | None = None_,     _metadata : dict\[str, Any\] | None = None_, \) → Generator\[[CallbackManagerForChainGroup](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForChainGroup.html#langchain_core.callbacks.manager.CallbackManagerForChainGroup "langchain_core.callbacks.manager.CallbackManagerForChainGroup"), None, None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/manager.html#trace_as_chain_group)\#     

Get a callback manager for a chain group in a context manager.

Useful for grouping different calls together as a single run even if they aren’t composed in a single chain.

Parameters:     

  * **group\_name** \(_str_\) – The name of the chain group.

  * **callback\_manager** \([_CallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManager.html#langchain_core.callbacks.manager.CallbackManager "langchain_core.callbacks.manager.CallbackManager") _,__optional_\) – The callback manager to use. Defaults to None.

  * **inputs** \(_dict_ _\[__str_ _,__Any_ _\]__,__optional_\) – The inputs to the chain group. Defaults to None.

  * **project\_name** \(_str_ _,__optional_\) – The name of the project. Defaults to None.

  * **example\_id** \(_str_ _or_ _UUID_ _,__optional_\) – The ID of the example. Defaults to None.

  * **run\_id** \(_UUID_ _,__optional_\) – The ID of the run.

  * **tags** \(_list_ _\[__str_ _\]__,__optional_\) – The inheritable tags to apply to all runs. Defaults to None.

  * **metadata** \(_dict_ _\[__str_ _,__Any_ _\]__,__optional_\) – The metadata to apply to all runs. Defaults to None.

Return type:     

Generator\[[CallbackManagerForChainGroup](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForChainGroup.html#langchain_core.callbacks.manager.CallbackManagerForChainGroup "langchain_core.callbacks.manager.CallbackManagerForChainGroup"), None, None\]

Note: must have LANGCHAIN\_TRACING\_V2 env var set to true to see the trace in LangSmith.

Returns:     

The callback manager for the chain group.

Return type:     

[CallbackManagerForChainGroup](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForChainGroup.html#langchain_core.callbacks.manager.CallbackManagerForChainGroup "langchain_core.callbacks.manager.CallbackManagerForChainGroup")

Parameters:     

  * **group\_name** \(_str_\)

  * **callback\_manager** \(_Optional_ _\[_[_CallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManager.html#langchain_core.callbacks.manager.CallbackManager "langchain_core.callbacks.manager.CallbackManager") _\]_\)

  * **inputs** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\)

  * **project\_name** \(_Optional_ _\[__str_ _\]_\)

  * **example\_id** \(_Optional_ _\[__Union_ _\[__str_ _,__UUID_ _\]__\]_\)

  * **run\_id** \(_Optional_ _\[__UUID_ _\]_\)

  * **tags** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\)

  * **metadata** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\)

Example               llm_input = "Foo"     with trace_as_chain_group("group_name", inputs={"input": llm_input}) as manager:         # Use the callback manager for the chain group         res = llm.invoke(llm_input, {"callbacks": manager})         manager.on_chain_end({"output": res})     

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)