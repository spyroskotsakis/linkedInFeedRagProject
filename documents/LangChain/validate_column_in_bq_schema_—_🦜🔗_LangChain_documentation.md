# validate_column_in_bq_schema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/google_community/bq_storage_vectorstores/langchain_google_community.bq_storage_vectorstores.utils.validate_column_in_bq_schema.html
**Word Count:** 63
**Links Count:** 92
**Scraped:** 2025-07-21 07:59:55
**Status:** completed

---

# validate\_column\_in\_bq\_schema\#

langchain\_google\_community.bq\_storage\_vectorstores.utils.validate\_column\_in\_bq\_schema\(

    _columns : dict_,     _column\_name : str_,     _expected\_types : list_,     _expected\_modes : list_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/bq_storage_vectorstores/utils.html#validate_column_in_bq_schema)\#     

Validates a column within a BigQuery schema.

Parameters:     

  * **columns** \(_dict_\) – A dictionary of BigQuery SchemaField objects representing

  * **schema.** \(_the table_\)

  * **column\_name** \(_str_\) – The name of the column to validate.

  * **expected\_types** \(_list_\) – A list of acceptable data types for the column.

  * **expected\_modes** \(_list_\) – A list of acceptable modes for the column.

Raises:     

  * **ValueError** – If the column doesn’t exist, has an unacceptable type,

  * **or has an unacceptable mode.** – 

Return type:     

None

__On this page