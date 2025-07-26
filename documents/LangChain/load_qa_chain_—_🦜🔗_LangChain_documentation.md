# load_qa_chain — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chains/langchain.chains.question_answering.chain.load_qa_chain.html
**Word Count:** 105
**Links Count:** 202
**Scraped:** 2025-07-21 07:50:02
**Status:** completed

---

# load\_qa\_chain\#

langchain.chains.question\_answering.chain.load\_qa\_chain\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _chain\_type : str = 'stuff'_,     _verbose : bool | None = None_,     _callback\_manager : [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _\*\* kwargs: Any_, \) → [BaseCombineDocumentsChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.base.BaseCombineDocumentsChain.html#langchain.chains.combine_documents.base.BaseCombineDocumentsChain "langchain.chains.combine_documents.base.BaseCombineDocumentsChain")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/question_answering/chain.html#load_qa_chain)\#     

Deprecated since version 0.2.13: This class is deprecated. See the following migration guides for replacements based on chain\_type:

stuff: <https://python.langchain.com/docs/versions/migrating_chains/stuff_docs_chain> map\_reduce: <https://python.langchain.com/docs/versions/migrating_chains/map_reduce_chain> refine: <https://python.langchain.com/docs/versions/migrating_chains/refine_chain> map\_rerank: <https://python.langchain.com/docs/versions/migrating_chains/map_rerank_docs_chain>

See also guides on retrieval and question-answering here: <https://python.langchain.com/docs/how_to/#qa-with-rag> It will not be removed until langchain==1.0.

Load question answering chain.

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – Language Model to use in the chain.

  * **chain\_type** \(_str_\) – Type of document combining chain to use. Should be one of “stuff”, “map\_reduce”, “map\_rerank”, and “refine”.

  * **verbose** \(_bool_ _|__None_\) – Whether chains should be run in verbose mode or not. Note that this applies to all chains that make up the final chain.

  * **callback\_manager** \([_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\) – Callback manager to use for the chain.

  * **kwargs** \(_Any_\)

Returns:     

A chain to use for question answering.

Return type:     

[_BaseCombineDocumentsChain_](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.combine_documents.base.BaseCombineDocumentsChain.html#langchain.chains.combine_documents.base.BaseCombineDocumentsChain "langchain.chains.combine_documents.base.BaseCombineDocumentsChain")

Examples using load\_qa\_chain

  * [Amazon Textract ](https://python.langchain.com/docs/integrations/document_loaders/amazon_textract/)

  * [Maritalk](https://python.langchain.com/docs/integrations/chat/maritalk/)

  * [SageMakerEndpoint](https://python.langchain.com/docs/integrations/llms/sagemaker/)

__On this page