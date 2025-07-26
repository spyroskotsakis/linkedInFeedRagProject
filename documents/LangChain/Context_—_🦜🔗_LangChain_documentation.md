# Context — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.Context.html
**Word Count:** 39
**Links Count:** 167
**Scraped:** 2025-07-21 08:03:51
**Status:** completed

---

# Context\#

_class _langchain\_community.chains.pebblo\_retrieval.models.Context[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chains/pebblo_retrieval/models.html#Context)\#     

Bases: `BaseModel`

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _doc _: str | None_ _\[Required\]_\#     

_param _pb\_checksum _: str | None_ _\[Required\]_\#     

_param _retrieved\_from _: str | None_ _\[Required\]_\#     

_param _vector\_db _: str_ _\[Required\]_\#     

__On this page