# NumericFieldSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.schema.NumericFieldSchema.html
**Word Count:** 45
**Links Count:** 112
**Scraped:** 2025-07-21 08:28:38
**Status:** completed

---

# NumericFieldSchema\#

_class _langchain\_aws.vectorstores.inmemorydb.schema.NumericFieldSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/vectorstores/inmemorydb/schema.html#NumericFieldSchema)\#     

Bases: [`InMemoryDBField`](https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBField.html#langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBField "langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBField")

Schema for numeric fields in Redis.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _name _: str_ _\[Required\]_\#     

_param _no\_index _: bool_ _ = False_\#     

_param _sortable _: bool | None_ _ = False_\#     

as\_field\(\) → NumericField[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/vectorstores/inmemorydb/schema.html#NumericFieldSchema.as_field)\#     

Return type:     

NumericField

__On this page