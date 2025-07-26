# JsonSerializer — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.sklearn.JsonSerializer.html
**Word Count:** 58
**Links Count:** 331
**Scraped:** 2025-07-21 08:08:35
**Status:** completed

---

# JsonSerializer\#

_class _langchain\_community.vectorstores.sklearn.JsonSerializer\(_persist\_path : str_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/sklearn.html#JsonSerializer)\#     

Serialize data in JSON using the json package from python standard library.

Methods

`__init__`\(persist\_path\) |    ---|---   `extension`\(\) | The file extension suggested by this serializer \(without dot\).   `load`\(\) | Loads the data from the persist\_path   `save`\(data\) | Saves the data to the persist\_path      Parameters:     

**persist\_path** \(_str_\)

\_\_init\_\_\(_persist\_path : str_\) → None\#     

Parameters:     

**persist\_path** \(_str_\)

Return type:     

None

_classmethod _extension\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/sklearn.html#JsonSerializer.extension)\#     

The file extension suggested by this serializer \(without dot\).

Return type:     

str

load\(\) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/sklearn.html#JsonSerializer.load)\#     

Loads the data from the persist\_path

Return type:     

_Any_

save\(_data : Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/sklearn.html#JsonSerializer.save)\#     

Saves the data to the persist\_path

Parameters:     

**data** \(_Any_\)

Return type:     

None

__On this page