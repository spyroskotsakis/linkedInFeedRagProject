# HNSWVectorField — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.schema.HNSWVectorField.html
**Word Count:** 47
**Links Count:** 343
**Scraped:** 2025-07-21 08:09:13
**Status:** completed

---

# HNSWVectorField\#

_class _langchain\_community.vectorstores.redis.schema.HNSWVectorField[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/redis/schema.html#HNSWVectorField)\#     

Bases: [`RedisVectorField`](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.schema.RedisVectorField.html#langchain_community.vectorstores.redis.schema.RedisVectorField "langchain_community.vectorstores.redis.schema.RedisVectorField")

Schema for HNSW vector fields in Redis.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _algorithm _: Literal\['HNSW'\]__ = 'HNSW'_\#     

_param _datatype _: str_ _ = 'FLOAT32'_\#     

_param _dims _: int_ _\[Required\]_\#     

_param _distance\_metric _: [RedisDistanceMetric](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.schema.RedisDistanceMetric.html#langchain_community.vectorstores.redis.schema.RedisDistanceMetric "langchain_community.vectorstores.redis.schema.RedisDistanceMetric")_ _ = 'COSINE'_\#     

_param _ef\_construction _: int_ _ = 200_\#     

_param _ef\_runtime _: int_ _ = 10_\#     

_param _epsilon _: float_ _ = 0.01_\#     

_param _initial\_cap _: int | None_ _ = None_\#     

_param _m _: int_ _ = 16_\#     

_param _name _: str_ _\[Required\]_\#     

_classmethod _uppercase\_and\_check\_dtype\(_v : str_\) → str\#     

Parameters:     

**v** \(_str_\)

Return type:     

str

as\_field\(\) → VectorField[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/redis/schema.html#HNSWVectorField.as_field)\#     

Return type:     

VectorField

__On this page