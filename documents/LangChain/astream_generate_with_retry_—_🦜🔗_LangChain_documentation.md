# astream_generate_with_retry — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/llms/langchain_community.llms.tongyi.astream_generate_with_retry.html
**Word Count:** 23
**Links Count:** 284
**Scraped:** 2025-07-21 08:02:42
**Status:** completed

---

# astream\_generate\_with\_retry\#

_async _langchain\_community.llms.tongyi.astream\_generate\_with\_retry\(

    _llm : [Tongyi](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.tongyi.Tongyi.html#langchain_community.llms.tongyi.Tongyi "langchain_community.llms.tongyi.Tongyi")_,     _\*\* kwargs: Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/tongyi.html#astream_generate_with_retry)\#     

Async version of stream\_generate\_with\_retry.

Because the dashscope SDK doesn’t provide an async API, we wrap stream\_generate\_with\_retry with an async generator.

Parameters:     

  * **llm** \([_Tongyi_](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.tongyi.Tongyi.html#langchain_community.llms.tongyi.Tongyi "langchain_community.llms.tongyi.Tongyi")\)

  * **kwargs** \(_Any_\)

Return type:     

_Any_

__On this page