# aexecute_cql — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra.aexecute_cql.html
**Word Count:** 39
**Links Count:** 249
**Scraped:** 2025-07-21 08:18:47
**Status:** completed

---

# aexecute\_cql\#

_async _langchain\_community.utilities.cassandra.aexecute\_cql\(

    _session : Session_,     _query : str_,     _\*\* kwargs: Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/cassandra.html#aexecute_cql)\#     

Execute a CQL query asynchronously.

Parameters:     

  * **session** \(_Session_\) – The Cassandra session to use.

  * **query** \(_str_\) – The CQL query to execute.

  * **kwargs** \(_Any_\) – Additional keyword arguments to pass to the session execute method.

Returns:     

The result of the query.

Return type:     

Any

__On this page