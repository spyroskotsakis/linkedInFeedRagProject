# create_qa_with_structure_chain — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.qa_with_structure.create_qa_with_structure_chain.html
**Word Count:** 79
**Links Count:** 197
**Scraped:** 2025-07-21 07:50:02
**Status:** completed

---

# create\_qa\_with\_structure\_chain\#

langchain.chains.openai\_functions.qa\_with\_structure.create\_qa\_with\_structure\_chain\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _schema : dict | type\[BaseModel\]_,     _output\_parser : str = 'base'_,     _prompt : [PromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.prompt.PromptTemplate.html#langchain_core.prompts.prompt.PromptTemplate "langchain_core.prompts.prompt.PromptTemplate") | [ChatPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html#langchain_core.prompts.chat.ChatPromptTemplate "langchain_core.prompts.chat.ChatPromptTemplate") | None = None_,     _verbose : bool = False_, \) → [LLMChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm.LLMChain.html#langchain.chains.llm.LLMChain "langchain.chains.llm.LLMChain")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/openai_functions/qa_with_structure.html#create_qa_with_structure_chain)\#     

Deprecated since version 0.2.13: This function is deprecated. Refer to this guide on retrieval and question answering with structured responses: <https://python.langchain.com/docs/how_to/qa_sources/#structure-sources-in-model-response> It will not be removed until langchain==1.0.

Create a question answering chain that returns an answer with sources     

based on schema.

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – Language model to use for the chain.

  * **schema** \(_dict_ _|__type_ _\[__BaseModel_ _\]_\) – Pydantic schema to use for the output.

  * **output\_parser** \(_str_\) – Output parser to use. Should be one of pydantic or base. Default to base.

  * **prompt** \([_PromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.prompt.PromptTemplate.html#langchain_core.prompts.prompt.PromptTemplate "langchain_core.prompts.prompt.PromptTemplate") _|_[_ChatPromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html#langchain_core.prompts.chat.ChatPromptTemplate "langchain_core.prompts.chat.ChatPromptTemplate") _|__None_\) – Optional prompt to use for the chain.

  * **verbose** \(_bool_\)

Return type:     

[_LLMChain_](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm.LLMChain.html#langchain.chains.llm.LLMChain "langchain.chains.llm.LLMChain")

Returns:

__On this page