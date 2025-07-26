# collect_runs — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/tracers/langchain_core.tracers.context.collect_runs.html
**Word Count:** 22
**Links Count:** 137
**Scraped:** 2025-07-21 07:54:29
**Status:** completed

---

# collect\_runs\#

langchain\_core.tracers.context.collect\_runs\(\) → Generator\[[RunCollectorCallbackHandler](https://python.langchain.com/api_reference/core/tracers/langchain_core.tracers.run_collector.RunCollectorCallbackHandler.html#langchain_core.tracers.run_collector.RunCollectorCallbackHandler "langchain_core.tracers.run_collector.RunCollectorCallbackHandler"), None, None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/tracers/context.html#collect_runs)\#     

Collect all run traces in context.

Yields:     

_run\_collector.RunCollectorCallbackHandler_ – The run collector callback handler.

Return type:     

Generator\[[RunCollectorCallbackHandler](https://python.langchain.com/api_reference/core/tracers/langchain_core.tracers.run_collector.RunCollectorCallbackHandler.html#langchain_core.tracers.run_collector.RunCollectorCallbackHandler "langchain_core.tracers.run_collector.RunCollectorCallbackHandler"), None, None\]

Example               >>> with collect_runs() as runs_cb:             chain.invoke("foo")             run_id = runs_cb.traced_runs[0].id     

__On this page