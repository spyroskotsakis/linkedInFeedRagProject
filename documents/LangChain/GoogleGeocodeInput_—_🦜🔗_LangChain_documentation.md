# GoogleGeocodeInput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/google_community/geocoding/langchain_google_community.geocoding.GoogleGeocodeInput.html
**Word Count:** 45
**Links Count:** 91
**Scraped:** 2025-07-21 07:59:00
**Status:** completed

---

# GoogleGeocodeInput\#

_class _langchain\_google\_community.geocoding.GoogleGeocodeInput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/geocoding.html#GoogleGeocodeInput)\#     

Bases: `BaseModel`

Input for the Geocoding tool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _query _: str_ _\[Required\]_\#     

Locations for query.

__On this page