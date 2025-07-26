# SimpleModel — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/prompty/core/langchain_prompty.core.SimpleModel.html
**Word Count:** 44
**Links Count:** 84
**Scraped:** 2025-07-21 08:26:51
**Status:** completed

---

# SimpleModel\#

_class _langchain\_prompty.core.SimpleModel[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_prompty/core.html#SimpleModel)\#     

Bases: `BaseModel`, `Generic`\[`T`\]

Simple model for a single item.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _item _: T_ _\[Required\]_\#     

__On this page