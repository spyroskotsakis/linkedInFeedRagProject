# aconnect_sse — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.zhipuai.aconnect_sse.html
**Word Count:** 33
**Links Count:** 227
**Scraped:** 2025-07-21 08:03:18
**Status:** completed

---

# aconnect\_sse\#

langchain\_community.chat\_models.zhipuai.aconnect\_sse\(

    _client : Any_,     _method : str_,     _url : str_,     _\*\* kwargs: Any_, \) → AsyncIterator[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/zhipuai.html#aconnect_sse)\#     

Async context manager for connecting to an SSE stream.

Parameters:     

  * **client** \(_Any_\) – The HTTP client.

  * **method** \(_str_\) – The HTTP method.

  * **url** \(_str_\) – The URL.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

Yields:     

The event source.

Return type:     

_AsyncIterator_

__On this page