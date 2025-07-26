# FlightSearchSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.amadeus.flight_search.FlightSearchSchema.html
**Word Count:** 147
**Links Count:** 417
**Scraped:** 2025-07-21 08:00:56
**Status:** completed

---

# FlightSearchSchema\#

_class _langchain\_community.tools.amadeus.flight\_search.FlightSearchSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/amadeus/flight_search.html#FlightSearchSchema)\#     

Bases: `BaseModel`

Schema for the AmadeusFlightSearch tool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _departureDateTimeEarliest _: str_ _\[Required\]_\#     

The earliest departure datetime from the origin airport for the flight search in the following format: “YYYY-MM-DDTHH:MM:SS”, where “T” separates the date and time components. For example: “2023-06-09T10:30:00” represents June 9th, 2023, at 10:30 AM.

_param _departureDateTimeLatest _: str_ _\[Required\]_\#     

The latest departure datetime from the origin airport for the flight search in the following format: “YYYY-MM-DDTHH:MM:SS”, where “T” separates the date and time components. For example: “2023-06-09T10:30:00” represents June 9th, 2023, at 10:30 AM.

_param _destinationLocationCode _: str_ _\[Required\]_\#     

The three letter International Air Transport Association \(IATA\) Location Identifier for the search’s destination airport.

_param _originLocationCode _: str_ _\[Required\]_\#     

The three letter International Air Transport Association \(IATA\) Location Identifier for the search’s origin airport.

_param _page\_number _: int_ _ = 1_\#     

The specific page number of flight results to retrieve

__On this page