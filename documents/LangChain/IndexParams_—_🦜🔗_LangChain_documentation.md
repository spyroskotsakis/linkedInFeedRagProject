# IndexParams — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.tencentvectordb.IndexParams.html
**Word Count:** 19
**Links Count:** 321
**Scraped:** 2025-07-21 08:10:17
**Status:** completed

---

# IndexParams\#

_class _langchain\_community.vectorstores.tencentvectordb.IndexParams\(

    _dimension : int_,     _shard : int = 1_,     _replicas : int = 2_,     _index\_type : str = 'HNSW'_,     _metric\_type : str = 'L2'_,     _params : Dict | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/tencentvectordb.html#IndexParams)\#     

Tencent vector DB Index params.

See the following documentation for details: <https://cloud.tencent.com/document/product/1709/95826>

Methods

`__init__`\(dimension\[, shard, replicas, ...\]\) |    ---|---      Parameters:     

  * **dimension** \(_int_\)

  * **shard** \(_int_\)

  * **replicas** \(_int_\)

  * **index\_type** \(_str_\)

  * **metric\_type** \(_str_\)

  * **params** \(_Optional_ _\[__Dict_ _\]_\)

\_\_init\_\_\(

    _dimension : int_,     _shard : int = 1_,     _replicas : int = 2_,     _index\_type : str = 'HNSW'_,     _metric\_type : str = 'L2'_,     _params : Dict | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/tencentvectordb.html#IndexParams.__init__)\#     

Parameters:     

  * **dimension** \(_int_\)

  * **shard** \(_int_\)

  * **replicas** \(_int_\)

  * **index\_type** \(_str_\)

  * **metric\_type** \(_str_\)

  * **params** \(_Dict_ _|__None_\)

__On this page