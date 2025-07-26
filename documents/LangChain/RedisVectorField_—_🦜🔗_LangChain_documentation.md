# RedisVectorField — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.schema.RedisVectorField.html
**Word Count:** 45
**Links Count:** 333
**Scraped:** 2025-07-21 08:15:47
**Status:** completed

---

# RedisVectorField\#

_class _langchain\_community.vectorstores.redis.schema.RedisVectorField[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/redis/schema.html#RedisVectorField)\#     

Bases: [`RedisField`](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.schema.RedisField.html#langchain_community.vectorstores.redis.schema.RedisField "langchain_community.vectorstores.redis.schema.RedisField")

Base class for Redis vector fields.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _algorithm _: object_ _\[Required\]_\#     

_param _datatype _: str_ _ = 'FLOAT32'_\#     

_param _dims _: int_ _\[Required\]_\#     

_param _distance\_metric _: [RedisDistanceMetric](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.schema.RedisDistanceMetric.html#langchain_community.vectorstores.redis.schema.RedisDistanceMetric "langchain_community.vectorstores.redis.schema.RedisDistanceMetric")_ _ = 'COSINE'_\#     

_param _initial\_cap _: int | None_ _ = None_\#     

_param _name _: str_ _\[Required\]_\#     

_classmethod _uppercase\_and\_check\_dtype\(_v : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/redis/schema.html#RedisVectorField.uppercase_and_check_dtype)\#     

Parameters:     

**v** \(_str_\)

Return type:     

str

__On this page