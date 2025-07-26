# DeleteEventSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/google_community/calendar/langchain_google_community.calendar.delete_event.DeleteEventSchema.html
**Word Count:** 59
**Links Count:** 110
**Scraped:** 2025-07-21 07:59:27
**Status:** completed

---

# DeleteEventSchema\#

_class _langchain\_google\_community.calendar.delete\_event.DeleteEventSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/calendar/delete_event.html#DeleteEventSchema)\#     

Bases: `BaseModel`

Input for CalendarDeleteEvent.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _calendar\_id _: str | None_ _ = 'primary'_\#     

The origin calendar ID.

_param _event\_id _: str_ _\[Required\]_\#     

The event ID to delete.

_param _send\_updates _: str | None_ _ = None_\#     

Whether to send updates to attendees.Allowed values are ‘all’, ‘externalOnly’, or ‘none’.

__On this page