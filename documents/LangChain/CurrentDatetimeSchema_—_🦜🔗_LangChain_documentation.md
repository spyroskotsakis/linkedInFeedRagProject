# CurrentDatetimeSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/google_community/calendar/langchain_google_community.calendar.current_datetime.CurrentDatetimeSchema.html
**Word Count:** 46
**Links Count:** 106
**Scraped:** 2025-07-21 07:59:27
**Status:** completed

---

# CurrentDatetimeSchema\#

_class _langchain\_google\_community.calendar.current\_datetime.CurrentDatetimeSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/calendar/current_datetime.html#CurrentDatetimeSchema)\#     

Bases: `BaseModel`

Input for GetCurrentDatetime.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _calendar\_id _: str | None_ _ = 'primary'_\#     

The calendar ID. Defaults to ‘primary’.

__On this page