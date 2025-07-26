# IndexableBaseModel — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/adapters/langchain_community.adapters.openai.IndexableBaseModel.html
**Word Count:** 49
**Links Count:** 109
**Scraped:** 2025-07-21 08:18:17
**Status:** completed

---

# IndexableBaseModel\#

_class _langchain\_community.adapters.openai.IndexableBaseModel[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/adapters/openai.html#IndexableBaseModel)\#     

Bases: `BaseModel`

Allows a BaseModel to return its fields by string variable indexing.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

__On this page