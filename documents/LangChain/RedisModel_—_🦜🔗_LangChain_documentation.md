# RedisModel — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.schema.RedisModel.html
**Word Count:** 46
**Links Count:** 360
**Scraped:** 2025-07-21 08:12:36
**Status:** completed

---

# RedisModel\#

_class _langchain\_community.vectorstores.redis.schema.RedisModel[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/redis/schema.html#RedisModel)\#     

Bases: `BaseModel`

Schema for Redis index.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _content\_key _: str_ _ = 'content'_\#     

_param _content\_vector\_key _: str_ _ = 'content\_vector'_\#     

_param _extra _: List\[[RedisField](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.schema.RedisField.html#langchain_community.vectorstores.redis.schema.RedisField "langchain_community.vectorstores.redis.schema.RedisField")\] | None_ _ = None_\#     

_param _numeric _: List\[[NumericFieldSchema](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.schema.NumericFieldSchema.html#langchain_community.vectorstores.redis.schema.NumericFieldSchema "langchain_community.vectorstores.redis.schema.NumericFieldSchema")\] | None_ _ = None_\#     

_param _tag _: List\[[TagFieldSchema](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.schema.TagFieldSchema.html#langchain_community.vectorstores.redis.schema.TagFieldSchema "langchain_community.vectorstores.redis.schema.TagFieldSchema")\] | None_ _ = None_\#     

_param _text _: List\[[TextFieldSchema](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.schema.TextFieldSchema.html#langchain_community.vectorstores.redis.schema.TextFieldSchema "langchain_community.vectorstores.redis.schema.TextFieldSchema")\]__ = \[TextFieldSchema\(name='content', weight=1, no\_stem=False, phonetic\_matcher=None, withsuffixtrie=False, no\_index=False, sortable=False\)\]_\#     

_param _vector _: List\[[FlatVectorField](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.schema.FlatVectorField.html#langchain_community.vectorstores.redis.schema.FlatVectorField "langchain_community.vectorstores.redis.schema.FlatVectorField") | [HNSWVectorField](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.schema.HNSWVectorField.html#langchain_community.vectorstores.redis.schema.HNSWVectorField "langchain_community.vectorstores.redis.schema.HNSWVectorField")\] | None_ _ = None_\#     

add\_content\_field\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/redis/schema.html#RedisModel.add_content_field)\#     

Return type:     

None

add\_vector\_field\(

    _vector\_field : Dict\[str, Any\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/redis/schema.html#RedisModel.add_vector_field)\#     

Parameters:     

**vector\_field** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

Return type:     

None

as\_dict\(\) → Dict\[str, List\[Any\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/redis/schema.html#RedisModel.as_dict)\#     

Return type:     

_Dict_\[str, _List_\[_Any_\]\]

get\_fields\(\) → List\[[RedisField](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.schema.RedisField.html#langchain_community.vectorstores.redis.schema.RedisField "langchain_community.vectorstores.redis.schema.RedisField")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/redis/schema.html#RedisModel.get_fields)\#     

Return type:     

_List_\[[_RedisField_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.schema.RedisField.html#langchain_community.vectorstores.redis.schema.RedisField "langchain_community.vectorstores.redis.schema.RedisField")\]

_property _content\_vector _: [FlatVectorField](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.schema.FlatVectorField.html#langchain_community.vectorstores.redis.schema.FlatVectorField "langchain_community.vectorstores.redis.schema.FlatVectorField") | [HNSWVectorField](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.schema.HNSWVectorField.html#langchain_community.vectorstores.redis.schema.HNSWVectorField "langchain_community.vectorstores.redis.schema.HNSWVectorField")_\#     

_property _is\_empty _: bool_\#     

_property _metadata\_keys _: List\[str\]_\#     

_property _vector\_dtype _: dtype_\#     

__On this page