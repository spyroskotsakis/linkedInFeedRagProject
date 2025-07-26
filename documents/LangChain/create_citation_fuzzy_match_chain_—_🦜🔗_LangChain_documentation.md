# create_citation_fuzzy_match_chain — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.citation_fuzzy_match.create_citation_fuzzy_match_chain.html
**Word Count:** 41
**Links Count:** 193
**Scraped:** 2025-07-21 07:48:33
**Status:** completed

---

# create\_citation\_fuzzy\_match\_chain\#

langchain.chains.openai\_functions.citation\_fuzzy\_match.create\_citation\_fuzzy\_match\_chain\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_, \) → [LLMChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm.LLMChain.html#langchain.chains.llm.LLMChain "langchain.chains.llm.LLMChain")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/openai_functions/citation_fuzzy_match.html#create_citation_fuzzy_match_chain)\#     

Deprecated since version 0.2.13: Use [`create_citation_fuzzy_match_runnable()`](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.citation_fuzzy_match.create_citation_fuzzy_match_runnable.html#langchain.chains.openai_functions.citation_fuzzy_match.create_citation_fuzzy_match_runnable "langchain.chains.openai_functions.citation_fuzzy_match.create_citation_fuzzy_match_runnable") instead. It will not be removed until langchain==1.0.

Create a citation fuzzy match chain.

Parameters:     

**llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – Language model to use for the chain.

Returns:     

Chain \(LLMChain\) that can be used to answer questions with citations.

Return type:     

[_LLMChain_](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm.LLMChain.html#langchain.chains.llm.LLMChain "langchain.chains.llm.LLMChain")

__On this page