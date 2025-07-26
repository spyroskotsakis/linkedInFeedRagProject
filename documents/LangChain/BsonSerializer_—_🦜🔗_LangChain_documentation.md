# BsonSerializer — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.sklearn.BsonSerializer.html
**Word Count:** 54
**Links Count:** 332
**Scraped:** 2025-07-21 08:05:36
**Status:** completed

---

# BsonSerializer\#

_class _langchain\_community.vectorstores.sklearn.BsonSerializer\(_persist\_path : str_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/sklearn.html#BsonSerializer)\#     

Serialize data in Binary JSON using the bson python package.

Methods

`__init__`\(persist\_path\) |    ---|---   `extension`\(\) | The file extension suggested by this serializer \(without dot\).   `load`\(\) | Loads the data from the persist\_path   `save`\(data\) | Saves the data to the persist\_path      Parameters:     

**persist\_path** \(_str_\)

\_\_init\_\_\(_persist\_path : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/sklearn.html#BsonSerializer.__init__)\#     

Parameters:     

**persist\_path** \(_str_\)

Return type:     

None

_classmethod _extension\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/sklearn.html#BsonSerializer.extension)\#     

The file extension suggested by this serializer \(without dot\).

Return type:     

str

load\(\) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/sklearn.html#BsonSerializer.load)\#     

Loads the data from the persist\_path

Return type:     

_Any_

save\(_data : Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/sklearn.html#BsonSerializer.save)\#     

Saves the data to the persist\_path

Parameters:     

**data** \(_Any_\)

Return type:     

None

__On this page