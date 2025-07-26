# StandardStreamEvent — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.schema.StandardStreamEvent.html
**Word Count:** 36
**Links Count:** 205
**Scraped:** 2025-07-21 07:56:25
**Status:** completed

---

# StandardStreamEvent\#

_class _langchain\_core.runnables.schema.StandardStreamEvent[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/schema.html#StandardStreamEvent)\#     

A standard stream event that follows LangChain convention for event data.

event _: str_\#     

run\_id _: str_\#     

tags _: NotRequired\[list\[str\]\]_\#     

metadata _: NotRequired\[dict\[str, Any\]\]_\#     

parent\_ids _: Sequence\[str\]_\#     

data _: [EventData](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.schema.EventData.html#langchain_core.runnables.schema.EventData "langchain_core.runnables.schema.EventData")_\#     

Event data.

The contents of the event data depend on the event type.

name _: str_\#     

The name of the Runnable that generated the event.

__On this page