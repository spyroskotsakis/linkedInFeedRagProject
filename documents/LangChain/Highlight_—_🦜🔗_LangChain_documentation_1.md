# Highlight — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.kendra.Highlight.html
**Word Count:** 76
**Links Count:** 180
**Scraped:** 2025-07-21 08:11:13
**Status:** completed

---

# Highlight\#

_class _langchain\_community.retrievers.kendra.Highlight[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/retrievers/kendra.html#Highlight)\#     

Bases: `BaseModel`

Information that highlights the keywords in the excerpt.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _BeginOffset _: int_ _\[Required\]_\#     

The zero-based location in the excerpt where the highlight starts.

_param _EndOffset _: int_ _\[Required\]_\#     

The zero-based location in the excerpt where the highlight ends.

_param _TopAnswer _: bool | None_ _\[Required\]_\#     

Indicates whether the result is the best one.

_param _Type _: str | None_ _\[Required\]_\#     

The highlight type: STANDARD or THESAURUS\_SYNONYM.

__On this page