# ConnectionParams — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.tencentvectordb.ConnectionParams.html
**Word Count:** 69
**Links Count:** 323
**Scraped:** 2025-07-21 08:02:42
**Status:** completed

---

# ConnectionParams\#

_class _langchain\_community.vectorstores.tencentvectordb.ConnectionParams\(

    _url : str_,     _key : str_,     _username : str = 'root'_,     _timeout : int = 10_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/tencentvectordb.html#ConnectionParams)\#     

Tencent vector DB Connection params.

See the following documentation for details: <https://cloud.tencent.com/document/product/1709/95820>

Attribute:     

url \(str\)The access address of the vector database server     

that the client needs to connect to.

key \(str\): API key for client to access the vector database server,     

which is used for authentication.

username \(str\) : Account for client to access the vector database server. timeout \(int\) : Request Timeout.

Methods

`__init__`\(url, key\[, username, timeout\]\) |    ---|---      Parameters:     

  * **url** \(_str_\)

  * **key** \(_str_\)

  * **username** \(_str_\)

  * **timeout** \(_int_\)

\_\_init\_\_\(

    _url : str_,     _key : str_,     _username : str = 'root'_,     _timeout : int = 10_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/tencentvectordb.html#ConnectionParams.__init__)\#     

Parameters:     

  * **url** \(_str_\)

  * **key** \(_str_\)

  * **username** \(_str_\)

  * **timeout** \(_int_\)

Examples using ConnectionParams

  * [Baidu VectorDB](https://python.langchain.com/docs/integrations/vectorstores/baiduvectordb/)

  * [Tencent Cloud VectorDB](https://python.langchain.com/docs/integrations/vectorstores/tencentvectordb/)

__On this page