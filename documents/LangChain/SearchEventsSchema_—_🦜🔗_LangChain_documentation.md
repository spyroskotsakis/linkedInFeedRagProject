# SearchEventsSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/google_community/calendar/langchain_google_community.calendar.search_events.SearchEventsSchema.html
**Word Count:** 144
**Links Count:** 118
**Scraped:** 2025-07-21 07:59:27
**Status:** completed

---

# SearchEventsSchema\#

_class _langchain\_google\_community.calendar.search\_events.SearchEventsSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/calendar/search_events.html#SearchEventsSchema)\#     

Bases: `BaseModel`

Input for CalendarSearchEvents.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _calendars\_info _: str_ _\[Required\]_\#     

A list with the information about all Calendars in Google CalendarUse the tool ‘get\_calendars\_info’ to get it.

_param _max\_datetime _: str_ _\[Required\]_\#     

The end datetime for the events search.

_param _max\_results _: int_ _ = 10_\#     

The maximum number of results to return.

_param _min\_datetime _: str_ _\[Required\]_\#     

The start datetime for the events in ‘YYYY-MM-DD HH:MM:SS’ format. If you do not know the current datetime, use the tool to get it.

_param _order\_by _: str_ _ = 'startTime'_\#     

The order of the events, either ‘startTime’ or ‘updated’.

_param _query _: str | None_ _ = None_\#     

Free text search terms to find events, that match these terms in the following fields: summary, description, location, attendee’s displayName, attendee’s email, organizer’s displayName, organizer’s email.

_param _single\_events _: bool_ _ = True_\#     

Whether to expand recurring events into instances and only return single one-off events and instances of recurring events.’startTime’ or ‘updated’.

__On this page