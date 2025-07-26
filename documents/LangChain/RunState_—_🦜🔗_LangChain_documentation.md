# RunState — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/tracers/langchain_core.tracers.log_stream.RunState.html
**Word Count:** 74
**Links Count:** 148
**Scraped:** 2025-07-21 07:56:25
**Status:** completed

---

# RunState\#

_class _langchain\_core.tracers.log\_stream.RunState[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/tracers/log_stream.html#RunState)\#     

State of the run.

id _: str_\#     

ID of the run.

streamed\_output _: list\[Any\]_\#     

List of output chunks streamed by Runnable.stream\(\)

final\_output _: Any | None_\#     

Final output of the run, usually the result of aggregating \(+\) streamed\_output. Updated throughout the run when supported by the Runnable.

name _: str_\#     

Name of the object being run.

type _: str_\#     

Type of the object being run, eg. prompt, chain, llm, etc.

logs _: dict\[str, [LogEntry](https://python.langchain.com/api_reference/core/tracers/langchain_core.tracers.log_stream.LogEntry.html#langchain_core.tracers.log_stream.LogEntry "langchain_core.tracers.log_stream.LogEntry")\]_\#     

Map of run names to sub-runs. If filters were supplied, this list will contain only the runs that matched the filters.

__On this page