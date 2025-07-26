# MoveEventSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/google_community/calendar/langchain_google_community.calendar.move_event.MoveEventSchema.html
**Word Count:** 62
**Links Count:** 112
**Scraped:** 2025-07-21 07:59:27
**Status:** completed

---

# MoveEventSchema\#

_class _langchain\_google\_community.calendar.move\_event.MoveEventSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/calendar/move_event.html#MoveEventSchema)\#     

Bases: `BaseModel`

Input for CalendarMoveEvent.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _destination\_calendar\_id _: str_ _\[Required\]_\#     

The destination calendar ID.

_param _event\_id _: str_ _\[Required\]_\#     

The event ID to move.

_param _origin\_calenddar\_id _: str_ _\[Required\]_\#     

The origin calendar ID.

_param _send\_updates _: str | None_ _ = None_\#     

Whether to send updates to attendees.Allowed values are ‘all’, ‘externalOnly’, or ‘none’.

__On this page