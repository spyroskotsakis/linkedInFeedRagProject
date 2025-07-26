# drop_index_if_exists — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.oraclevs.drop_index_if_exists.html
**Word Count:** 34
**Links Count:** 316
**Scraped:** 2025-07-21 08:03:18
**Status:** completed

---

# drop\_index\_if\_exists\#

langchain\_community.vectorstores.oraclevs.drop\_index\_if\_exists\(

    _client : Any_,     _index\_name : str_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/oraclevs.html#drop_index_if_exists)\#     

Drop an index if it exists.

Parameters:     

  * **client** \(_Any_\) – The OracleDB connection object.

  * **index\_name** \(_str_\) – The name of the index to drop.

Raises:     

**RuntimeError** – If an error occurs while dropping the index.

Return type:     

None

__On this page