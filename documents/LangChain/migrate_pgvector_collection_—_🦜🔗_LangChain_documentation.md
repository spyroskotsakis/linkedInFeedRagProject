# migrate_pgvector_collection — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/postgres/utils/langchain_postgres.utils.pgvector_migrator.migrate_pgvector_collection.html
**Word Count:** 81
**Links Count:** 82
**Scraped:** 2025-07-21 08:26:03
**Status:** completed

---

# migrate\_pgvector\_collection\#

langchain\_postgres.utils.pgvector\_migrator.migrate\_pgvector\_collection\(

    _engine : [PGEngine](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.PGEngine.html#langchain_postgres.v2.engine.PGEngine "langchain_postgres.v2.engine.PGEngine")_,     _collection\_name : str_,     _vector\_store : [PGVectorStore](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.vectorstores.PGVectorStore.html#langchain_postgres.v2.vectorstores.PGVectorStore "langchain_postgres.v2.vectorstores.PGVectorStore")_,     _delete\_pg\_collection : bool | None = False_,     _insert\_batch\_size : int = 1000_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/utils/pgvector_migrator.html#migrate_pgvector_collection)\#     

Migrate all data present in a PGVector collection to use separate tables for each collection. The new data format is compatible with the PGVectorStore interface.

Parameters:     

  * **engine** \([_PGEngine_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.PGEngine.html#langchain_postgres.v2.engine.PGEngine "langchain_postgres.v2.engine.PGEngine")\) – The PG engine corresponding to the Database.

  * **collection\_name** \(_str_\) – The collection to migrate.

  * **vector\_store** \([_PGVectorStore_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.vectorstores.PGVectorStore.html#langchain_postgres.v2.vectorstores.PGVectorStore "langchain_postgres.v2.vectorstores.PGVectorStore")\) – The PGVectorStore object corresponding to the new collection table.

  * **delete\_pg\_collection** \(_bool_\) – An option to delete the original data upon migration. Default: False. Optional.

  * **insert\_batch\_size** \(_int_\) – Number of rows to insert at once in the table. Default: 1000.

Return type:     

None

__On this page