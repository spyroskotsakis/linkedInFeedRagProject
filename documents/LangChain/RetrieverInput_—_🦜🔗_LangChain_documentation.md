# RetrieverInput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/tools/langchain_core.tools.retriever.RetrieverInput.html
**Word Count:** 47
**Links Count:** 116
**Scraped:** 2025-07-21 07:55:26
**Status:** completed

---

# RetrieverInput\#

_class _langchain\_core.tools.retriever.RetrieverInput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/tools/retriever.html#RetrieverInput)\#     

Bases: `BaseModel`

Input to the retriever.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _query _: str_ _\[Required\]_\#     

query to look up in retriever

__On this page