# NarrativeModel — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/cpal/langchain_experimental.cpal.models.NarrativeModel.html
**Word Count:** 44
**Links Count:** 115
**Scraped:** 2025-07-21 08:25:17
**Status:** completed

---

# NarrativeModel\#

_class _langchain\_experimental.cpal.models.NarrativeModel[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/cpal/models.html#NarrativeModel)\#     

Bases: `BaseModel`

Narrative input as three story elements.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _story\_hypothetical _: str_ _\[Required\]_\#     

_param _story\_outcome\_question _: str_ _\[Required\]_\#     

_param _story\_plot _: str_ _\[Required\]_\#     

__On this page