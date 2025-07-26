# ConnectionParams — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.baiduvectordb.ConnectionParams.html
**Word Count:** 68
**Links Count:** 323
**Scraped:** 2025-07-21 08:18:17
**Status:** completed

---

# ConnectionParams\#

_class _langchain\_community.vectorstores.baiduvectordb.ConnectionParams\(

    _endpoint : str_,     _api\_key : str_,     _account : str = 'root'_,     _connection\_timeout\_in\_mills : int = 50000_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/baiduvectordb.html#ConnectionParams)\#     

Baidu VectorDB Connection params.

See the following documentation for details: <https://cloud.baidu.com/doc/VDB/s/6lrsob0wy>

Attribute:     

endpoint \(str\)The access address of the vector database server     

that the client needs to connect to.

api\_key \(str\): API key for client to access the vector database server,     

which is used for authentication.

account \(str\) : Account for client to access the vector database server. connection\_timeout\_in\_mills \(int\) : Request Timeout.

Methods

`__init__`\(endpoint, api\_key\[, account, ...\]\) |    ---|---      Parameters:     

  * **endpoint** \(_str_\)

  * **api\_key** \(_str_\)

  * **account** \(_str_\)

  * **connection\_timeout\_in\_mills** \(_int_\)

\_\_init\_\_\(

    _endpoint : str_,     _api\_key : str_,     _account : str = 'root'_,     _connection\_timeout\_in\_mills : int = 50000_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/baiduvectordb.html#ConnectionParams.__init__)\#     

Parameters:     

  * **endpoint** \(_str_\)

  * **api\_key** \(_str_\)

  * **account** \(_str_\)

  * **connection\_timeout\_in\_mills** \(_int_\)

Examples using ConnectionParams

  * [Baidu VectorDB](https://python.langchain.com/docs/integrations/vectorstores/baiduvectordb/)

  * [Tencent Cloud VectorDB](https://python.langchain.com/docs/integrations/vectorstores/tencentvectordb/)

__On this page