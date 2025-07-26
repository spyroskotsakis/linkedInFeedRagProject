# GooglePlacesSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/google_community/places_api/langchain_google_community.places_api.GooglePlacesSchema.html
**Word Count:** 44
**Links Count:** 91
**Scraped:** 2025-07-21 07:59:27
**Status:** completed

---

# GooglePlacesSchema\#

_class _langchain\_google\_community.places\_api.GooglePlacesSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/places_api.html#GooglePlacesSchema)\#     

Bases: `BaseModel`

Input for GooglePlacesTool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _query _: str_ _\[Required\]_\#     

Query for google maps

__On this page