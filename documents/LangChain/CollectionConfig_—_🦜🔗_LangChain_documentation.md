# CollectionConfig — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.zep.CollectionConfig.html
**Word Count:** 69
**Links Count:** 330
**Scraped:** 2025-07-21 08:15:47
**Status:** completed

---

# CollectionConfig\#

_class _langchain\_community.vectorstores.zep.CollectionConfig\(

    _name : str_,     _description : str | None_,     _metadata : Dict\[str, Any\] | None_,     _embedding\_dimensions : int_,     _is\_auto\_embedded : bool_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/zep.html#CollectionConfig)\#     

Configuration for a Zep Collection.

If the collection does not exist, it will be created.

Parameters:     

  * **name** \(_str_\)

  * **description** \(_str_ _|__None_\)

  * **metadata** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\)

  * **embedding\_dimensions** \(_int_\)

  * **is\_auto\_embedded** \(_bool_\)

name\#     

The name of the collection.

Type:     

str

description\#     

An optional description of the collection.

Type:     

Optional\[str\]

metadata\#     

Optional metadata for the collection.

Type:     

Optional\[Dict\[str, Any\]\]

embedding\_dimensions\#     

The number of dimensions for the embeddings in the collection. This should match the Zep server configuration if auto-embed is true.

Type:     

int

is\_auto\_embedded\#     

A flag indicating whether the collection is automatically embedded by Zep.

Type:     

bool

Attributes

Methods

`__init__`\(name, description, metadata, ...\) |    ---|---      \_\_init\_\_\(

    _name : str_,     _description : str | None_,     _metadata : Dict\[str, Any\] | None_,     _embedding\_dimensions : int_,     _is\_auto\_embedded : bool_, \) → None\#     

Parameters:     

  * **name** \(_str_\)

  * **description** \(_str_ _|__None_\)

  * **metadata** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\)

  * **embedding\_dimensions** \(_int_\)

  * **is\_auto\_embedded** \(_bool_\)

Return type:     

None

Examples using CollectionConfig

  * [Zep](https://python.langchain.com/docs/integrations/vectorstores/zep/)

__On this page