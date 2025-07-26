# create_prem_retry_decorator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.premai.create_prem_retry_decorator.html
**Word Count:** 26
**Links Count:** 209
**Scraped:** 2025-07-21 08:04:25
**Status:** completed

---

# create\_prem\_retry\_decorator\#

langchain\_community.embeddings.premai.create\_prem\_retry\_decorator\(

    _embedder : [PremAIEmbeddings](https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.premai.PremAIEmbeddings.html#langchain_community.embeddings.premai.PremAIEmbeddings "langchain_community.embeddings.premai.PremAIEmbeddings")_,     _\*_ ,     _max\_retries : int = 1_, \) → Callable\[\[Any\], Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/premai.html#create_prem_retry_decorator)\#     

Create a retry decorator for PremAIEmbeddings.

Parameters:     

  * **embedder** \([_PremAIEmbeddings_](https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.premai.PremAIEmbeddings.html#langchain_community.embeddings.premai.PremAIEmbeddings "langchain_community.embeddings.premai.PremAIEmbeddings")\) – The PremAIEmbeddings instance

  * **max\_retries** \(_int_\) – The maximum number of retries

Returns:     

The retry decorator

Return type:     

Callable\[\[Any\], Any\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)