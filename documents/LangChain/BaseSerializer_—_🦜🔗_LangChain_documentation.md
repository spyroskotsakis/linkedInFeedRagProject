# BaseSerializer — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.sklearn.BaseSerializer.html
**Word Count:** 51
**Links Count:** 332
**Scraped:** 2025-07-21 08:04:25
**Status:** completed

---

# BaseSerializer\#

_class _langchain\_community.vectorstores.sklearn.BaseSerializer\(_persist\_path : str_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/sklearn.html#BaseSerializer)\#     

Base class for serializing data.

Methods

`__init__`\(persist\_path\) |    ---|---   `extension`\(\) | The file extension suggested by this serializer \(without dot\).   `load`\(\) | Loads the data from the persist\_path   `save`\(data\) | Saves the data to the persist\_path      Parameters:     

**persist\_path** \(_str_\)

\_\_init\_\_\(_persist\_path : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/sklearn.html#BaseSerializer.__init__)\#     

Parameters:     

**persist\_path** \(_str_\)

Return type:     

None

_abstractmethod classmethod _extension\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/sklearn.html#BaseSerializer.extension)\#     

The file extension suggested by this serializer \(without dot\).

Return type:     

str

_abstractmethod _load\(\) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/sklearn.html#BaseSerializer.load)\#     

Loads the data from the persist\_path

Return type:     

_Any_

_abstractmethod _save\(_data : Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/sklearn.html#BaseSerializer.save)\#     

Saves the data to the persist\_path

Parameters:     

**data** \(_Any_\)

Return type:     

None

__On this page