# BaseModel — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.pgembedding.BaseModel.html
**Word Count:** 100
**Links Count:** 319
**Scraped:** 2025-07-21 08:00:23
**Status:** completed

---

# BaseModel\#

_class _langchain\_community.vectorstores.pgembedding.BaseModel\(_\*\* kwargs: Any_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/pgembedding.html#BaseModel)\#     

Base model for all SQL stores.

A simple constructor that allows initialization from kwargs.

Sets attributes on the constructed instance using the names and values in `kwargs`.

Only keys that are present as attributes of the instance’s class are allowed. These could be, for example, any mapped columns or relationships.

Attributes

`metadata` |    ---|---   `registry` |    `uuid` |       Methods

`__init__`\(\*\*kwargs\) | A simple constructor that allows initialization from kwargs.   ---|---      Parameters:     

**kwargs** \(_Any_\)

\_\_init\_\_\(_\*\* kwargs: Any_\) → None\#     

A simple constructor that allows initialization from kwargs.

Sets attributes on the constructed instance using the names and values in `kwargs`.

Only keys that are present as attributes of the instance’s class are allowed. These could be, for example, any mapped columns or relationships.

Parameters:     

  * **self** \(_Any_\)

  * **kwargs** \(_Any_\)

Return type:     

None

__On this page