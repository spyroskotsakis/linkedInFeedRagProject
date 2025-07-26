# load_summarize_chain — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chains/langchain.chains.summarize.chain.load_summarize_chain.html
**Word Count:** 67
**Links Count:** 195
**Scraped:** 2025-07-21 07:49:01
**Status:** completed

---

# load\_summarize\_chain\#

langchain.chains.summarize.chain.load\_summarize\_chain\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _chain\_type : str = 'stuff'_,     _verbose : bool | None = None_,     _\*\* kwargs: Any_, \) → [BaseCombineDocumentsChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.base.BaseCombineDocumentsChain.html#langchain.chains.combine_documents.base.BaseCombineDocumentsChain "langchain.chains.combine_documents.base.BaseCombineDocumentsChain")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/summarize/chain.html#load_summarize_chain)\#     

Load summarizing chain.

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – Language Model to use in the chain.

  * **chain\_type** \(_str_\) – Type of document combining chain to use. Should be one of “stuff”, “map\_reduce”, and “refine”.

  * **verbose** \(_bool_ _|__None_\) – Whether chains should be run in verbose mode or not. Note that this applies to all chains that make up the final chain.

  * **kwargs** \(_Any_\)

Returns:     

A chain to use for summarizing.

Return type:     

[_BaseCombineDocumentsChain_](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.base.BaseCombineDocumentsChain.html#langchain.chains.combine_documents.base.BaseCombineDocumentsChain "langchain.chains.combine_documents.base.BaseCombineDocumentsChain")

Examples using load\_summarize\_chain

  * [Infino](https://python.langchain.com/docs/integrations/callbacks/infino/)

  * [LarkSuite \(FeiShu\)](https://python.langchain.com/docs/integrations/document_loaders/larksuite/)

  * [Model caches](https://python.langchain.com/docs/integrations/llm_caching/)

__On this page