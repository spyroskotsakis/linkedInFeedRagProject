# CreateEventSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/google_community/calendar/langchain_google_community.calendar.create_event.CreateEventSchema.html
**Word Count:** 239
**Links Count:** 130
**Scraped:** 2025-07-21 07:59:27
**Status:** completed

---

# CreateEventSchema\#

_class _langchain\_google\_community.calendar.create\_event.CreateEventSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/calendar/create_event.html#CreateEventSchema)\#     

Bases: `BaseModel`

Input for CalendarCreateEvent.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _attendees _: List\[str\] | None_ _ = None_\#     

A list of attendees’ email addresses for the event.

_param _calendar\_id _: str_ _ = 'primary'_\#     

The calendar ID to create the event in.

_param _color\_id _: str | None_ _ = None_\#     

The color ID of the event. None for default. ‘1’: Lavender, ‘2’: Sage, ‘3’: Grape, ‘4’: Flamingo, ‘5’: Banana, ‘6’: Tangerine, ‘7’: Peacock, ‘8’: Graphite, ‘9’: Blueberry, ‘10’: Basil, ‘11’: Tomato.

_param _conference\_data _: bool | None_ _ = None_\#     

Whether to include conference data.

_param _description _: str | None_ _ = None_\#     

The description of the event.

_param _end\_datetime _: str_ _\[Required\]_\#     

The end datetime for the event in ‘YYYY-MM-DD HH:MM:SS’ format. If the event is an all-day event, set the time to ‘YYYY-MM-DD’ format.

_param _location _: str | None_ _ = None_\#     

The location of the event.

_param _recurrence _: Dict\[str, Any\] | None_ _ = None_\#     

The recurrence of the event. Format: \{‘FREQ’: <’DAILY’ or ‘WEEKLY’>, ‘INTERVAL’: <number>, ‘COUNT’: <number or None>, ‘UNTIL’: <’YYYYMMDD’ or None>, ‘BYDAY’: <’MO’, ‘TU’, ‘WE’, ‘TH’, ‘FR’, ‘SA’, ‘SU’ or None>\}. Use either COUNT or UNTIL, but not both; set the other to None.

_param _reminders _: None | bool | List\[Dict\[str, Any\]\]__ = None_\#     

Reminders for the event. Set to True for default reminders, or provide a list like \[\{‘method’: ‘email’, ‘minutes’: <minutes>\}, …\]. Valid methods are ‘email’ and ‘popup’.

_param _start\_datetime _: str_ _\[Required\]_\#     

The start datetime for the event in ‘YYYY-MM-DD HH:MM:SS’ format.If the event is an all-day event, set the time to ‘YYYY-MM-DD’ format.If you do not know the current datetime, use the tool to get it.

_param _summary _: str_ _\[Required\]_\#     

The title of the event.

_param _timezone _: str_ _\[Required\]_\#     

The timezone of the event.

_param _transparency _: str | None_ _ = None_\#     

User availability for the event.transparent for available and opaque for busy.

__On this page