# ClosestAirportSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.amadeus.closest_airport.ClosestAirportSchema.html
**Word Count:** 101
**Links Count:** 409
**Scraped:** 2025-07-21 08:03:18
**Status:** completed

---

# ClosestAirportSchema\#

_class _langchain\_community.tools.amadeus.closest\_airport.ClosestAirportSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/amadeus/closest_airport.html#ClosestAirportSchema)\#     

Bases: `BaseModel`

Schema for the AmadeusClosestAirport tool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _location _: str_ _\[Required\]_\#     

The location for which you would like to find the nearest airport along with optional details such as country, state, region, or province, allowing for easy processing and identification of the closest airport. Examples of the format are the following: Cali, Colombia

> Lincoln, Nebraska, United States

New York, United States Sydney, New South Wales, Australia Rome, Lazio, Italy Toronto, Ontario, Canada

__On this page