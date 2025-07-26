# RedisTag — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.filters.RedisTag.html
**Word Count:** 54
**Links Count:** 326
**Scraped:** 2025-07-21 08:06:11
**Status:** completed

---

# RedisTag\#

_class _langchain\_community.vectorstores.redis.filters.RedisTag\(_field : str_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/redis/filters.html#RedisTag)\#     

RedisFilterField representing a tag in a Redis index.

Create a RedisTag FilterField.

Parameters:     

**field** \(_str_\) – The name of the RedisTag field in the index to be queried against.

Attributes

`OPERATORS` |    ---|---   `OPERATOR_MAP` |    `SUPPORTED_VAL_TYPES` |    `escaper` |       Methods

`__init__`\(field\) | Create a RedisTag FilterField.   ---|---   `equals`\(other\) |       \_\_init\_\_\(_field : str_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/redis/filters.html#RedisTag.__init__)\#     

Create a RedisTag FilterField.

Parameters:     

**field** \(_str_\) – The name of the RedisTag field in the index to be queried against.

equals\(

    _other : [RedisFilterField](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.filters.RedisFilterField.html#langchain_community.vectorstores.redis.filters.RedisFilterField "langchain_community.vectorstores.redis.filters.RedisFilterField")_, \) → bool\#     

Parameters:     

**other** \([_RedisFilterField_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.filters.RedisFilterField.html#langchain_community.vectorstores.redis.filters.RedisFilterField "langchain_community.vectorstores.redis.filters.RedisFilterField")\)

Return type:     

bool

Examples using RedisTag

  * [Redis](https://python.langchain.com/docs/integrations/vectorstores/redis/)

__On this page