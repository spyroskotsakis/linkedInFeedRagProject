# TagFieldSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.schema.TagFieldSchema.html
**Word Count:** 45
**Links Count:** 116
**Scraped:** 2025-07-21 08:29:02
**Status:** completed

---

# TagFieldSchema\#

_class _langchain\_aws.vectorstores.inmemorydb.schema.TagFieldSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/vectorstores/inmemorydb/schema.html#TagFieldSchema)\#     

Bases: [`InMemoryDBField`](https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBField.html#langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBField "langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBField")

Schema for tag fields in Redis.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _case\_sensitive _: bool_ _ = False_\#     

_param _name _: str_ _\[Required\]_\#     

_param _no\_index _: bool_ _ = False_\#     

_param _separator _: str_ _ = ','_\#     

_param _sortable _: bool | None_ _ = False_\#     

as\_field\(\) → TagField[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/vectorstores/inmemorydb/schema.html#TagFieldSchema.as_field)\#     

Return type:     

TagField

__On this page