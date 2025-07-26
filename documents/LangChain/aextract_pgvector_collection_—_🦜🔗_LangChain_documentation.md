# aextract_pgvector_collection — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/postgres/utils/langchain_postgres.utils.pgvector_migrator.aextract_pgvector_collection.html
**Word Count:** 49
**Links Count:** 80
**Scraped:** 2025-07-21 08:25:40
**Status:** completed

---

# aextract\_pgvector\_collection\#

_async _langchain\_postgres.utils.pgvector\_migrator.aextract\_pgvector\_collection\(

    _engine : [PGEngine](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.PGEngine.html#langchain_postgres.v2.engine.PGEngine "langchain_postgres.v2.engine.PGEngine")_,     _collection\_name : str_,     _batch\_size : int = 1000_, \) → AsyncIterator\[Sequence\[RowMapping\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/utils/pgvector_migrator.html#aextract_pgvector_collection)\#     

Extract all data belonging to a PGVector collection.

Parameters:     

  * **engine** \([_PGEngine_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.PGEngine.html#langchain_postgres.v2.engine.PGEngine "langchain_postgres.v2.engine.PGEngine")\) – The PG engine corresponding to the Database.

  * **collection\_name** \(_str_\) – The name of the collection to get the data for.

  * **batch\_size** \(_int_\) – The batch size for collection extraction. Default: 1000. Optional.

Yields:     

The data present in the collection.

Return type:     

_AsyncIterator_\[_Sequence_\[_RowMapping_\]\]

__On this page