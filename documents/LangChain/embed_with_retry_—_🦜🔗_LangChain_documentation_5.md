# embed_with_retry — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.premai.embed_with_retry.html
**Word Count:** 14
**Links Count:** 209
**Scraped:** 2025-07-21 08:18:17
**Status:** completed

---

# embed\_with\_retry\#

langchain\_community.embeddings.premai.embed\_with\_retry\(

    _embedder : [PremAIEmbeddings](https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.premai.PremAIEmbeddings.html#langchain_community.embeddings.premai.PremAIEmbeddings "langchain_community.embeddings.premai.PremAIEmbeddings")_,     _model : str_,     _project\_id : int_,     _input : str | List\[str\]_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/premai.html#embed_with_retry)\#     

Using tenacity for retry in embedding calls

Parameters:     

  * **embedder** \([_PremAIEmbeddings_](https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.premai.PremAIEmbeddings.html#langchain_community.embeddings.premai.PremAIEmbeddings "langchain_community.embeddings.premai.PremAIEmbeddings")\)

  * **model** \(_str_\)

  * **project\_id** \(_int_\)

  * **input** \(_str_ _|__List_ _\[__str_ _\]_\)

Return type:     

_Any_

__On this page