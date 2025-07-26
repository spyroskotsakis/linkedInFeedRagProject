# InMemoryDBVectorField — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBVectorField.html
**Word Count:** 44
**Links Count:** 116
**Scraped:** 2025-07-21 08:29:02
**Status:** completed

---

# InMemoryDBVectorField\#

_class _langchain\_aws.vectorstores.inmemorydb.schema.InMemoryDBVectorField[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/vectorstores/inmemorydb/schema.html#InMemoryDBVectorField)\#     

Bases: [`InMemoryDBField`](https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBField.html#langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBField "langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBField")

Base class for Redis vector fields.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _algorithm _: object_ _\[Required\]_\#     

_param _datatype _: str_ _ = 'FLOAT32'_\#     

_param _dims _: int_ _\[Required\]_\#     

_param _distance\_metric _: [InMemoryDBDistanceMetric](https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBDistanceMetric.html#langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBDistanceMetric "langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBDistanceMetric")_ _ = 'COSINE'_\#     

_param _initial\_cap _: int | None_ _ = None_\#     

_param _name _: str_ _\[Required\]_\#     

__On this page