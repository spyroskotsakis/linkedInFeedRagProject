# TextFieldSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.schema.TextFieldSchema.html
**Word Count:** 45
**Links Count:** 120
**Scraped:** 2025-07-21 08:29:02
**Status:** completed

---

# TextFieldSchema\#

_class _langchain\_aws.vectorstores.inmemorydb.schema.TextFieldSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/vectorstores/inmemorydb/schema.html#TextFieldSchema)\#     

Bases: [`InMemoryDBField`](https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBField.html#langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBField "langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBField")

Schema for text fields in Redis.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _name _: str_ _\[Required\]_\#     

_param _no\_index _: bool_ _ = False_\#     

_param _no\_stem _: bool_ _ = False_\#     

_param _phonetic\_matcher _: str | None_ _ = None_\#     

_param _sortable _: bool | None_ _ = False_\#     

_param _weight _: float_ _ = 1_\#     

_param _withsuffixtrie _: bool_ _ = False_\#     

as\_field\(\) → TextField[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/vectorstores/inmemorydb/schema.html#TextFieldSchema.as_field)\#     

Return type:     

TextField

__On this page