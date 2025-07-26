# connect_sse — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.zhipuai.connect_sse.html
**Word Count:** 32
**Links Count:** 227
**Scraped:** 2025-07-21 08:16:51
**Status:** completed

---

# connect\_sse\#

langchain\_community.chat\_models.zhipuai.connect\_sse\(

    _client : Any_,     _method : str_,     _url : str_,     _\*\* kwargs: Any_, \) → Iterator[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/zhipuai.html#connect_sse)\#     

Context manager for connecting to an SSE stream.

Parameters:     

  * **client** \(_Any_\) – The HTTP client.

  * **method** \(_str_\) – The HTTP method.

  * **url** \(_str_\) – The URL.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

Yields:     

The event source.

Return type:     

_Iterator_

__On this page