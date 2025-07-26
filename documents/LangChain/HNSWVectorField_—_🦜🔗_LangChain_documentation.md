# HNSWVectorField — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.schema.HNSWVectorField.html
**Word Count:** 46
**Links Count:** 127
**Scraped:** 2025-07-21 08:28:38
**Status:** completed

---

# HNSWVectorField\#

_class _langchain\_aws.vectorstores.inmemorydb.schema.HNSWVectorField[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/vectorstores/inmemorydb/schema.html#HNSWVectorField)\#     

Bases: [`InMemoryDBVectorField`](https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBVectorField.html#langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBVectorField "langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBVectorField")

Schema for HNSW vector fields in Redis.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _algorithm _: Literal\['HNSW'\]__ = 'HNSW'_\#     

_param _datatype _: str_ _ = 'FLOAT32'_\#     

_param _dims _: int_ _\[Required\]_\#     

_param _distance\_metric _: [InMemoryDBDistanceMetric](https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBDistanceMetric.html#langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBDistanceMetric "langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBDistanceMetric")_ _ = 'COSINE'_\#     

_param _ef\_construction _: int_ _ = 200_\#     

_param _ef\_runtime _: int_ _ = 10_\#     

_param _epsilon _: float_ _ = 0.01_\#     

_param _initial\_cap _: int | None_ _ = None_\#     

_param _m _: int_ _ = 16_\#     

_param _name _: str_ _\[Required\]_\#     

as\_field\(\) → VectorField[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/vectorstores/inmemorydb/schema.html#HNSWVectorField.as_field)\#     

Return type:     

VectorField

__On this page