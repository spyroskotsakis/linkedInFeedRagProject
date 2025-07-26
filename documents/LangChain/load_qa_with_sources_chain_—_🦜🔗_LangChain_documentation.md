# load_qa_with_sources_chain — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chains/langchain.chains.qa_with_sources.loading.load_qa_with_sources_chain.html
**Word Count:** 104
**Links Count:** 197
**Scraped:** 2025-07-21 07:50:36
**Status:** completed

---

# load\_qa\_with\_sources\_chain\#

langchain.chains.qa\_with\_sources.loading.load\_qa\_with\_sources\_chain\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _chain\_type : str = 'stuff'_,     _verbose : bool | None = None_,     _\*\* kwargs: Any_, \) → [BaseCombineDocumentsChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.base.BaseCombineDocumentsChain.html#langchain.chains.combine_documents.base.BaseCombineDocumentsChain "langchain.chains.combine_documents.base.BaseCombineDocumentsChain")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/qa_with_sources/loading.html#load_qa_with_sources_chain)\#     

Deprecated since version 0.2.13: This function is deprecated. Refer to this guide on retrieval and question answering with sources: <https://python.langchain.com/docs/how_to/qa_sources/>

See also the following migration guides for replacements based on chain\_type: stuff: <https://python.langchain.com/docs/versions/migrating_chains/stuff_docs_chain> map\_reduce: <https://python.langchain.com/docs/versions/migrating_chains/map_reduce_chain> refine: <https://python.langchain.com/docs/versions/migrating_chains/refine_chain> map\_rerank: <https://python.langchain.com/docs/versions/migrating_chains/map_rerank_docs_chain> It will not be removed until langchain==1.0.

Load a question answering with sources chain.

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – Language Model to use in the chain.

  * **chain\_type** \(_str_\) – Type of document combining chain to use. Should be one of “stuff”, “map\_reduce”, “refine” and “map\_rerank”.

  * **verbose** \(_bool_ _|__None_\) – Whether chains should be run in verbose mode or not. Note that this applies to all chains that make up the final chain.

  * **kwargs** \(_Any_\)

Returns:     

A chain to use for question answering with sources.

Return type:     

[_BaseCombineDocumentsChain_](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.base.BaseCombineDocumentsChain.html#langchain.chains.combine_documents.base.BaseCombineDocumentsChain "langchain.chains.combine_documents.base.BaseCombineDocumentsChain")

__On this page