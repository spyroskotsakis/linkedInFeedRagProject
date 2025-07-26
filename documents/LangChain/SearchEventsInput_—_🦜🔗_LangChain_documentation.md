# SearchEventsInput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.office365.events_search.SearchEventsInput.html
**Word Count:** 180
**Links Count:** 416
**Scraped:** 2025-07-21 08:01:32
**Status:** completed

---

# SearchEventsInput\#

_class _langchain\_community.tools.office365.events\_search.SearchEventsInput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/office365/events_search.html#SearchEventsInput)\#     

Bases: `BaseModel`

Input for SearchEmails Tool.

From <https://learn.microsoft.com/en-us/graph/search-query-parameter>

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _end\_datetime _: str_ _\[Required\]_\#     

The end datetime for the search query in the following format: YYYY-MM-DDTHH:MM:SS±hh:mm, where “T” separates the date and time components, and the time zone offset is specified as ±hh:mm. For example: “2023-06-09T10:30:00+03:00” represents June 9th, 2023, at 10:30 AM in a time zone with a positive offset of 3 hours from Coordinated Universal Time \(UTC\).

_param _max\_results _: int_ _ = 10_\#     

The maximum number of results to return.

_param _start\_datetime _: str_ _\[Required\]_\#     

The start datetime for the search query in the following format: YYYY-MM-DDTHH:MM:SS±hh:mm, where “T” separates the date and time components, and the time zone offset is specified as ±hh:mm. For example: “2023-06-09T10:30:00+03:00” represents June 9th, 2023, at 10:30 AM in a time zone with a positive offset of 3 hours from Coordinated Universal Time \(UTC\).

_param _truncate _: bool_ _ = True_\#     

Whether the event’s body is truncated to meet token number limits. Set to False for searches that will retrieve small events, otherwise, set to True.

__On this page