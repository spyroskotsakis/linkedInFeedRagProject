# create_citation_fuzzy_match_runnable — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.citation_fuzzy_match.create_citation_fuzzy_match_runnable.html
**Word Count:** 49
**Links Count:** 192
**Scraped:** 2025-07-21 07:50:36
**Status:** completed

---

# create\_citation\_fuzzy\_match\_runnable\#

langchain.chains.openai\_functions.citation\_fuzzy\_match.create\_citation\_fuzzy\_match\_runnable\(

    _llm : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/openai_functions/citation_fuzzy_match.html#create_citation_fuzzy_match_runnable)\#     

Create a citation fuzzy match Runnable.

Example usage:

>  >     from langchain.chains import create_citation_fuzzy_match_runnable >     from langchain_openai import ChatOpenAI >      >     llm = ChatOpenAI(model="gpt-4o-mini") >      >     context = "Alice has blue eyes. Bob has brown eyes. Charlie has green eyes." >     question = "What color are Bob's eyes?" >      >     chain = create_citation_fuzzy_match_runnable(llm) >     chain.invoke({"question": question, "context": context}) >     

Parameters:     

**llm** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\) – Language model to use for the chain. Must implement bind\_tools.

Returns:     

Runnable that can be used to answer questions with citations.

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")

__On this page