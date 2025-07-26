# EventData — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.schema.EventData.html
**Word Count:** 135
**Links Count:** 196
**Scraped:** 2025-07-21 07:54:29
**Status:** completed

---

# EventData\#

_class _langchain\_core.runnables.schema.EventData[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/schema.html#EventData)\#     

Data associated with a streaming event.

input _: Any_\#     

The input passed to the Runnable that generated the event.

Inputs will sometimes be available at the _START_ of the Runnable, and sometimes at the _END_ of the Runnable.

If a Runnable is able to stream its inputs, then its input by definition won’t be known until the _END_ of the Runnable when it has finished streaming its inputs.

output _: Any_\#     

The output of the Runnable that generated the event.

Outputs will only be available at the _END_ of the Runnable.

For most Runnables, this field can be inferred from the chunk field, though there might be some exceptions for special cased Runnables \(e.g., like chat models\), which may return more information.

chunk _: Any_\#     

A streaming chunk from the output that generated the event.

chunks support addition in general, and adding them up should result in the output of the Runnable that generated the event.

__On this page