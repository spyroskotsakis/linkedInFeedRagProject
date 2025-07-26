# connect_httpx_sse — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.minimax.connect_httpx_sse.html
**Word Count:** 40
**Links Count:** 227
**Scraped:** 2025-07-21 08:17:20
**Status:** completed

---

# connect\_httpx\_sse\#

langchain\_community.chat\_models.minimax.connect\_httpx\_sse\(

    _client : Any_,     _method : str_,     _url : str_,     _\*\* kwargs: Any_, \) → Iterator[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/minimax.html#connect_httpx_sse)\#     

Context manager for connecting to an SSE stream.

Parameters:     

  * **client** \(_Any_\) – The httpx client.

  * **method** \(_str_\) – The HTTP method.

  * **url** \(_str_\) – The URL to connect to.

  * **kwargs** \(_Any_\) – Additional keyword arguments to pass to the client.

Yields:     

An EventSource object.

Return type:     

_Iterator_

__On this page