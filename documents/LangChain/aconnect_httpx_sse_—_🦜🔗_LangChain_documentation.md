# aconnect_httpx_sse — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.baichuan.aconnect_httpx_sse.html
**Word Count:** 41
**Links Count:** 227
**Scraped:** 2025-07-21 08:15:47
**Status:** completed

---

# aconnect\_httpx\_sse\#

langchain\_community.chat\_models.baichuan.aconnect\_httpx\_sse\(

    _client : Any_,     _method : str_,     _url : str_,     _\*\* kwargs: Any_, \) → AsyncIterator[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/baichuan.html#aconnect_httpx_sse)\#     

Async context manager for connecting to an SSE stream.

Parameters:     

  * **client** \(_Any_\) – The httpx client.

  * **method** \(_str_\) – The HTTP method.

  * **url** \(_str_\) – The URL to connect to.

  * **kwargs** \(_Any_\) – Additional keyword arguments to pass to the client.

Yields:     

An EventSource object.

Return type:     

_AsyncIterator_

__On this page