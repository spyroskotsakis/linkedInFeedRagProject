# InMemoryDBField — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBField.html
**Word Count:** 43
**Links Count:** 104
**Scraped:** 2025-07-21 08:28:38
**Status:** completed

---

# InMemoryDBField\#

_class _langchain\_aws.vectorstores.inmemorydb.schema.InMemoryDBField[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/vectorstores/inmemorydb/schema.html#InMemoryDBField)\#     

Bases: `BaseModel`

Base class for Redis fields.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _name _: str_ _\[Required\]_\#     

__On this page