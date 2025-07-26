# wrapped_response_future — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra.wrapped_response_future.html
**Word Count:** 46
**Links Count:** 249
**Scraped:** 2025-07-21 08:16:18
**Status:** completed

---

# wrapped\_response\_future\#

_async _langchain\_community.utilities.cassandra.wrapped\_response\_future\(

    _func : Callable\[..., ResponseFuture\]_,     _\* args: Any_,     _\*\* kwargs: Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/cassandra.html#wrapped_response_future)\#     

Wrap a Cassandra response future in an asyncio future.

Parameters:     

  * **func** \(_Callable_ _\[__...__,__ResponseFuture_ _\]_\) – The Cassandra function to call.

  * **\*args** \(_Any_\) – The arguments to pass to the Cassandra function.

  * **\*\*kwargs** \(_Any_\) – The keyword arguments to pass to the Cassandra function.

Returns:     

The result of the Cassandra function.

Return type:     

Any

__On this page