# FlatVectorField — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.schema.FlatVectorField.html
**Word Count:** 46
**Links Count:** 121
**Scraped:** 2025-07-21 08:44:55
**Status:** completed

---

# FlatVectorField\#

_class _langchain\_aws.vectorstores.inmemorydb.schema.FlatVectorField[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/vectorstores/inmemorydb/schema.html#FlatVectorField)\#     

Bases: [`InMemoryDBVectorField`](https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBVectorField.html#langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBVectorField "langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBVectorField")

Schema for flat vector fields in Redis.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _algorithm _: Literal\['FLAT'\]__ = 'FLAT'_\#     

_param _block\_size _: int | None_ _ = None_\#     

_param _datatype _: str_ _ = 'FLOAT32'_\#     

_param _dims _: int_ _\[Required\]_\#     

_param _distance\_metric _: [InMemoryDBDistanceMetric](https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBDistanceMetric.html#langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBDistanceMetric "langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBDistanceMetric")_ _ = 'COSINE'_\#     

_param _initial\_cap _: int | None_ _ = None_\#     

_param _name _: str_ _\[Required\]_\#     

as\_field\(\) → VectorField[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/vectorstores/inmemorydb/schema.html#FlatVectorField.as_field)\#     

Return type:     

VectorField

__On this page