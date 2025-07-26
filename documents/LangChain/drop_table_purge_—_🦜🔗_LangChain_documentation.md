# drop_table_purge — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.oraclevs.drop_table_purge.html
**Word Count:** 37
**Links Count:** 316
**Scraped:** 2025-07-21 08:11:12
**Status:** completed

---

# drop\_table\_purge\#

langchain\_community.vectorstores.oraclevs.drop\_table\_purge\(

    _client : Any_,     _table\_name : str_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/oraclevs.html#drop_table_purge)\#     

Drop a table and purge it from the database.

Parameters:     

  * **client** \(_Any_\) – The OracleDB connection object.

  * **table\_name** \(_str_\) – The name of the table to drop.

Raises:     

**RuntimeError** – If an error occurs while dropping the table.

Return type:     

None

__On this page