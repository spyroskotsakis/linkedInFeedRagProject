# LogEntry — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/tracers/langchain_core.tracers.log_stream.LogEntry.html
**Word Count:** 98
**Links Count:** 157
**Scraped:** 2025-07-21 07:55:26
**Status:** completed

---

# LogEntry\#

_class _langchain\_core.tracers.log\_stream.LogEntry[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/tracers/log_stream.html#LogEntry)\#     

A single entry in the run log.

id _: str_\#     

ID of the sub-run.

name _: str_\#     

Name of the object being run.

type _: str_\#     

Type of the object being run, eg. prompt, chain, llm, etc.

tags _: list\[str\]_\#     

List of tags for the run.

metadata _: dict\[str, Any\]_\#     

Key-value pairs of metadata for the run.

start\_time _: str_\#     

ISO-8601 timestamp of when the run started.

streamed\_output\_str _: list\[str\]_\#     

List of LLM tokens streamed by this run, if applicable.

streamed\_output _: list\[Any\]_\#     

List of output chunks streamed by this run, if available.

inputs _: NotRequired\[Any | None\]_\#     

Inputs to this run. Not available currently via astream\_log.

final\_output _: Any | None_\#     

Final output of this run.

Only available after the run has finished successfully.

end\_time _: str | None_\#     

ISO-8601 timestamp of when the run ended. Only available after the run has finished.

__On this page