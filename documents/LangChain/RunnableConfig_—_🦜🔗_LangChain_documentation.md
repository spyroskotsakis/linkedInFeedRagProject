# RunnableConfig — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html
**Word Count:** 215
**Links Count:** 218
**Scraped:** 2025-07-21 07:51:39
**Status:** completed

---

# RunnableConfig\#

_class _langchain\_core.runnables.config.RunnableConfig[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/config.html#RunnableConfig)\#     

Configuration for a Runnable.

tags _: list\[str\]_\#     

Tags for this call and any sub-calls \(eg. a Chain calling an LLM\). You can use these to filter calls.

metadata _: dict\[str, Any\]_\#     

Metadata for this call and any sub-calls \(eg. a Chain calling an LLM\). Keys should be strings, values should be JSON-serializable.

callbacks _: list | Any | None_\#     

Callbacks for this call and any sub-calls \(eg. a Chain calling an LLM\). Tags are passed to all callbacks, metadata is passed to handle\*Start callbacks.

run\_name _: str_\#     

Name for the tracer run for this call. Defaults to the name of the class.

max\_concurrency _: int | None_\#     

Maximum number of parallel calls to make. If not provided, defaults to ThreadPoolExecutor’s default.

recursion\_limit _: int_\#     

Maximum number of times a call can recurse. If not provided, defaults to 25.

configurable _: dict\[str, Any\]_\#     

Runtime values for attributes previously made configurable on this Runnable, or sub-Runnables, through .configurable\_fields\(\) or .configurable\_alternatives\(\). Check .output\_schema\(\) for a description of the attributes that have been made configurable.

run\_id _: UUID | None_\#     

Unique identifier for the tracer run for this call. If not provided, a new UUID will be generated.

Examples using RunnableConfig

  * [\# Example](https://python.langchain.com/docs/versions/migrating_chains/refine_docs_chain/)

  * [\# Legacy](https://python.langchain.com/docs/versions/migrating_chains/multi_prompt_chain/)

  * [How to access the RunnableConfig from a tool](https://python.langchain.com/docs/how_to/tool_configure/)

  * [How to add ad-hoc tool calling capability to LLMs and Chat Models](https://python.langchain.com/docs/how_to/tools_prompting/)

  * [How to dispatch custom callback events](https://python.langchain.com/docs/how_to/callbacks_custom_events/)

  * [How to handle tool errors](https://python.langchain.com/docs/how_to/tools_error/)

  * [How to pass runtime secrets to runnables](https://python.langchain.com/docs/how_to/runnable_runtime_secrets/)

  * [How to run custom functions](https://python.langchain.com/docs/how_to/functions/)

  * [How to stream events from a tool](https://python.langchain.com/docs/how_to/tool_stream_events/)

  * [How to summarize text through iterative refinement](https://python.langchain.com/docs/how_to/summarize_refine/)

  * [LangChain Expression Language Cheatsheet](https://python.langchain.com/docs/how_to/lcel_cheatsheet/)

  * [Tavily Search](https://python.langchain.com/docs/integrations/tools/tavily_search/)

__On this page