# ScheduleMessageSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.slack.schedule_message.ScheduleMessageSchema.html
**Word Count:** 111
**Links Count:** 413
**Scraped:** 2025-07-21 08:10:45
**Status:** completed

---

# ScheduleMessageSchema\#

_class _langchain\_community.tools.slack.schedule\_message.ScheduleMessageSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/slack/schedule_message.html#ScheduleMessageSchema)\#     

Bases: `BaseModel`

Input for ScheduleMessageTool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _channel _: str_ _\[Required\]_\#     

The channel, private group, or IM channel to send message to.

_param _message _: str_ _\[Required\]_\#     

The message to be sent.

_param _timestamp _: str_ _\[Required\]_\#     

The datetime for when the message should be sent in the following format: YYYY-MM-DDTHH:MM:SS±hh:mm, where “T” separates the date and time components, and the time zone offset is specified as ±hh:mm. For example: “2023-06-09T10:30:00+03:00” represents June 9th, 2023, at 10:30 AM in a time zone with a positive offset of 3 hours from Coordinated Universal Time \(UTC\).

__On this page