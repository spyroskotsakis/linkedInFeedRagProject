# PolygonAggregatesSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.polygon.aggregates.PolygonAggregatesSchema.html
**Word Count:** 138
**Links Count:** 417
**Scraped:** 2025-07-21 08:02:42
**Status:** completed

---

# PolygonAggregatesSchema\#

_class _langchain\_community.tools.polygon.aggregates.PolygonAggregatesSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/polygon/aggregates.html#PolygonAggregatesSchema)\#     

Bases: `BaseModel`

Input for PolygonAggregates.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _from\_date _: str_ _\[Required\]_\#     

The start of the aggregate time window. Either a date with the format YYYY-MM-DD or a millisecond timestamp.

_param _ticker _: str_ _\[Required\]_\#     

The ticker symbol to fetch aggregates for.

_param _timespan _: str_ _\[Required\]_\#     

The size of the time window. Possible values are: second, minute, hour, day, week, month, quarter, year. Default is ‘day’

_param _timespan\_multiplier _: int_ _\[Required\]_\#     

The number of timespans to aggregate. For example, if timespan is ‘day’ and timespan\_multiplier is 1, the result will be daily bars. If timespan is ‘day’ and timespan\_multiplier is 5, the result will be weekly bars. Default is 1.

_param _to\_date _: str_ _\[Required\]_\#     

The end of the aggregate time window. Either a date with the format YYYY-MM-DD or a millisecond timestamp.

__On this page