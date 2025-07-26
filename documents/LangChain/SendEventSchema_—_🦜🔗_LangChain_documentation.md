# SendEventSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.office365.send_event.SendEventSchema.html
**Word Count:** 165
**Links Count:** 417
**Scraped:** 2025-07-21 08:05:36
**Status:** completed

---

# SendEventSchema\#

_class _langchain\_community.tools.office365.send\_event.SendEventSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/office365/send_event.html#SendEventSchema)\#     

Bases: `BaseModel`

Input for CreateEvent Tool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _attendees _: List\[str\]__\[Required\]_\#     

The list of attendees for the event.

_param _body _: str_ _\[Required\]_\#     

The message body to include in the event.

_param _end\_datetime _: str_ _\[Required\]_\#     

The end datetime for the event in the following format: YYYY-MM-DDTHH:MM:SS±hh:mm, where “T” separates the date and time components, and the time zone offset is specified as ±hh:mm. For example: “2023-06-09T10:30:00+03:00” represents June 9th, 2023, at 10:30 AM in a time zone with a positive offset of 3 hours from Coordinated Universal Time \(UTC\).

_param _start\_datetime _: str_ _\[Required\]_\#     

The start datetime for the event in the following format: YYYY-MM-DDTHH:MM:SS±hh:mm, where “T” separates the date and time components, and the time zone offset is specified as ±hh:mm. For example: “2023-06-09T10:30:00+03:00” represents June 9th, 2023, at 10:30 AM in a time zone with a positive offset of 3 hours from Coordinated Universal Time \(UTC\).

_param _subject _: str_ _\[Required\]_\#     

The subject of the event.

__On this page