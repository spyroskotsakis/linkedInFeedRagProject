# NumericFieldSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.schema.NumericFieldSchema.html
**Word Count:** 45
**Links Count:** 326
**Scraped:** 2025-07-21 08:11:12
**Status:** completed

---

# NumericFieldSchema\#

_class _langchain\_community.vectorstores.redis.schema.NumericFieldSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/redis/schema.html#NumericFieldSchema)\#     

Bases: [`RedisField`](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.schema.RedisField.html#langchain_community.vectorstores.redis.schema.RedisField "langchain_community.vectorstores.redis.schema.RedisField")

Schema for numeric fields in Redis.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _name _: str_ _\[Required\]_\#     

_param _no\_index _: bool_ _ = False_\#     

_param _sortable _: bool | None_ _ = False_\#     

as\_field\(\) → NumericField[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/redis/schema.html#NumericFieldSchema.as_field)\#     

Return type:     

NumericField

__On this page