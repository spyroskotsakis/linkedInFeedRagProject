# sync_call_fallback — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/qdrant/vectorstores/langchain_qdrant.vectorstores.sync_call_fallback.html
**Word Count:** 40
**Links Count:** 74
**Scraped:** 2025-07-21 08:26:51
**Status:** completed

---

# sync\_call\_fallback\#

langchain\_qdrant.vectorstores.sync\_call\_fallback\(

    _method : Callable_, \) → Callable[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_qdrant/vectorstores.html#sync_call_fallback)\#     

Decorator to call the synchronous method of the class if the async method is not implemented. This decorator might be only used for the methods that are defined as async in the class.

Parameters:     

**method** \(_Callable_\)

Return type:     

_Callable_

__On this page