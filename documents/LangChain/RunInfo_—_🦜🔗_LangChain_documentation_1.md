# RunInfo — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/tracers/langchain_core.tracers.event_stream.RunInfo.html
**Word Count:** 55
**Links Count:** 147
**Scraped:** 2025-07-21 07:55:55
**Status:** completed

---

# RunInfo\#

_class _langchain\_core.tracers.event\_stream.RunInfo[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/tracers/event_stream.html#RunInfo)\#     

Information about a run.

This is used to keep track of the metadata associated with a run.

Parameters:     

  * **name** – The name of the run.

  * **tags** – The tags associated with the run.

  * **metadata** – The metadata associated with the run.

  * **run\_type** – The type of the run.

  * **inputs** – The inputs to the run.

  * **parent\_run\_id** – The ID of the parent run.

name _: str_\#     

tags _: list\[str\]_\#     

metadata _: dict\[str, Any\]_\#     

run\_type _: str_\#     

inputs _: NotRequired\[Any\]_\#     

parent\_run\_id _: UUID | None_\#     

__On this page