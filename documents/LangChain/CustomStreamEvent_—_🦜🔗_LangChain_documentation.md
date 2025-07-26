# CustomStreamEvent — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.schema.CustomStreamEvent.html
**Word Count:** 34
**Links Count:** 204
**Scraped:** 2025-07-21 07:55:55
**Status:** completed

---

# CustomStreamEvent\#

_class _langchain\_core.runnables.schema.CustomStreamEvent[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/schema.html#CustomStreamEvent)\#     

Custom stream event created by the user.

Added in version 0.2.15.

event _: Literal\['on\_custom\_event'\]_\#     

The event type.

run\_id _: str_\#     

tags _: NotRequired\[list\[str\]\]_\#     

metadata _: NotRequired\[dict\[str, Any\]\]_\#     

parent\_ids _: Sequence\[str\]_\#     

name _: str_\#     

User defined name for the event.

data _: Any_\#     

The data associated with the event. Free form and can be anything.

__On this page