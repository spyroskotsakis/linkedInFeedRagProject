# truncate_run_iterative — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.tracers.wandb.truncate_run_iterative.html
**Word Count:** 42
**Links Count:** 181
**Scraped:** 2025-07-21 08:01:32
**Status:** completed

---

# truncate\_run\_iterative\#

langchain\_community.callbacks.tracers.wandb.truncate\_run\_iterative\(

    _runs : List\[Dict\[str, Any\]\]_,     _keep\_keys : Tuple\[str, ...\] = \(\)_, \) → List\[Dict\[str, Any\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/tracers/wandb.html#truncate_run_iterative)\#     

Utility to truncate a list of runs dictionaries to only keep the specified     

keys in each run.

Parameters:     

  * **runs** \(_List_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]_\) – The list of runs to truncate.

  * **keep\_keys** \(_Tuple_ _\[__str_ _,__...__\]_\) – The keys to keep in each run.

Returns:     

The truncated list of runs.

Return type:     

_List_\[_Dict_\[str, _Any_\]\]

__On this page