# TagFieldSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.schema.TagFieldSchema.html
**Word Count:** 45
**Links Count:** 330
**Scraped:** 2025-07-21 08:00:56
**Status:** completed

---

# TagFieldSchema\#

_class _langchain\_community.vectorstores.redis.schema.TagFieldSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/redis/schema.html#TagFieldSchema)\#     

Bases: [`RedisField`](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.schema.RedisField.html#langchain_community.vectorstores.redis.schema.RedisField "langchain_community.vectorstores.redis.schema.RedisField")

Schema for tag fields in Redis.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _case\_sensitive _: bool_ _ = False_\#     

_param _name _: str_ _\[Required\]_\#     

_param _no\_index _: bool_ _ = False_\#     

_param _separator _: str_ _ = ','_\#     

_param _sortable _: bool | None_ _ = False_\#     

as\_field\(\) → TagField[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/redis/schema.html#TagFieldSchema.as_field)\#     

Return type:     

TagField

__On this page