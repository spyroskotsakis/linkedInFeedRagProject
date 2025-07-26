# RedisField — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.schema.RedisField.html
**Word Count:** 43
**Links Count:** 318
**Scraped:** 2025-07-21 08:09:13
**Status:** completed

---

# RedisField\#

_class _langchain\_community.vectorstores.redis.schema.RedisField[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/redis/schema.html#RedisField)\#     

Bases: `BaseModel`

Base class for Redis fields.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _name _: str_ _\[Required\]_\#     

__On this page