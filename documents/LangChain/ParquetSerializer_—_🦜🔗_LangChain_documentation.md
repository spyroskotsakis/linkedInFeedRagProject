# ParquetSerializer — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.sklearn.ParquetSerializer.html
**Word Count:** 52
**Links Count:** 332
**Scraped:** 2025-07-21 08:16:51
**Status:** completed

---

# ParquetSerializer\#

_class _langchain\_community.vectorstores.sklearn.ParquetSerializer\(_persist\_path : str_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/sklearn.html#ParquetSerializer)\#     

Serialize data in Apache Parquet format using the pyarrow package.

Methods

`__init__`\(persist\_path\) |    ---|---   `extension`\(\) | The file extension suggested by this serializer \(without dot\).   `load`\(\) | Loads the data from the persist\_path   `save`\(data\) | Saves the data to the persist\_path      Parameters:     

**persist\_path** \(_str_\)

\_\_init\_\_\(_persist\_path : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/sklearn.html#ParquetSerializer.__init__)\#     

Parameters:     

**persist\_path** \(_str_\)

Return type:     

None

_classmethod _extension\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/sklearn.html#ParquetSerializer.extension)\#     

The file extension suggested by this serializer \(without dot\).

Return type:     

str

load\(\) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/sklearn.html#ParquetSerializer.load)\#     

Loads the data from the persist\_path

Return type:     

_Any_

save\(_data : Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/sklearn.html#ParquetSerializer.save)\#     

Saves the data to the persist\_path

Parameters:     

**data** \(_Any_\)

Return type:     

None

__On this page