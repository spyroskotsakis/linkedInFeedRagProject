# drop_table — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/db2/db2vs/langchain_db2.db2vs.drop_table.html
**Word Count:** 34
**Links Count:** 72
**Scraped:** 2025-07-21 07:59:00
**Status:** completed

---

# drop\_table\#

langchain\_db2.db2vs.drop\_table\(_client : Connection_, _table\_name : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_db2/db2vs.html#drop_table)\#     

Drop a table from the database.

Parameters:     

  * **client** \(_Connection_\) – The ibm\_db\_dbi connection object.

  * **table\_name** \(_str_\) – The name of the table to drop.

Raises:     

**RuntimeError** – If an error occurs while dropping the table.

Return type:     

None

__On this page