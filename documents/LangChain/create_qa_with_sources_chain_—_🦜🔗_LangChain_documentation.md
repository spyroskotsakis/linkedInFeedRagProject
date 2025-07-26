# create_qa_with_sources_chain — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.qa_with_structure.create_qa_with_sources_chain.html
**Word Count:** 74
**Links Count:** 193
**Scraped:** 2025-07-21 07:51:08
**Status:** completed

---

# create\_qa\_with\_sources\_chain\#

langchain.chains.openai\_functions.qa\_with\_structure.create\_qa\_with\_sources\_chain\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _verbose : bool = False_,     _\*\* kwargs: Any_, \) → [LLMChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm.LLMChain.html#langchain.chains.llm.LLMChain "langchain.chains.llm.LLMChain")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/openai_functions/qa_with_structure.html#create_qa_with_sources_chain)\#     

Deprecated since version 0.2.13: This function is deprecated. Refer to this guide on retrieval and question answering with sources: <https://python.langchain.com/docs/how_to/qa_sources/#structure-sources-in-model-response> It will not be removed until langchain==1.0.

Create a question answering chain that returns an answer with sources.

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – Language model to use for the chain.

  * **verbose** \(_bool_\) – Whether to print the details of the chain

  * **\*\*kwargs** \(_Any_\) – Keyword arguments to pass to create\_qa\_with\_structure\_chain.

Returns:     

Chain \(LLMChain\) that can be used to answer questions with citations.

Return type:     

[_LLMChain_](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm.LLMChain.html#langchain.chains.llm.LLMChain "langchain.chains.llm.LLMChain")

__On this page