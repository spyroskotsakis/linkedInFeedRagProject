# GooglePlacesSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.google_places.tool.GooglePlacesSchema.html
**Word Count:** 44
**Links Count:** 409
**Scraped:** 2025-07-21 08:21:41
**Status:** completed

---

# GooglePlacesSchema\#

_class _langchain\_community.tools.google\_places.tool.GooglePlacesSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/google_places/tool.html#GooglePlacesSchema)\#     

Bases: `BaseModel`

Input for GooglePlacesTool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _query _: str_ _\[Required\]_\#     

Query for google maps

__On this page