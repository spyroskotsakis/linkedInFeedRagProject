# create_tagging_chain_pydantic — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.tagging.create_tagging_chain_pydantic.html
**Word Count:** 162
**Links Count:** 198
**Scraped:** 2025-07-21 07:51:08
**Status:** completed

---

# create\_tagging\_chain\_pydantic\#

langchain.chains.openai\_functions.tagging.create\_tagging\_chain\_pydantic\(

    _pydantic\_schema : Any_,     _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _prompt : [ChatPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html#langchain_core.prompts.chat.ChatPromptTemplate "langchain_core.prompts.chat.ChatPromptTemplate") | None = None_,     _\*\* kwargs: Any_, \) → [Chain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.base.Chain.html#langchain.chains.base.Chain "langchain.chains.base.Chain")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/openai_functions/tagging.html#create_tagging_chain_pydantic)\#     

Deprecated since version 0.2.13: LangChain has introduced a method called with\_structured\_output that is available on ChatModels capable of tool calling. See API reference for this function for replacement: <<https://api.python.langchain.com/en/latest/chains/langchain.chains.openai_functions.tagging.create_tagging_chain_pydantic.html>> You can read more about with\_structured\_output here: <<https://python.langchain.com/docs/how_to/structured_output/>>. If you notice other issues, please provide feedback here: <[langchain-ai/langchain\#18154](https://github.com/langchain-ai/langchain/discussions/18154)> It will not be removed until langchain==1.0.

Create a chain that extracts information from a passage     

based on a pydantic schema.

This function is deprecated. Please use with\_structured\_output instead. See example usage below:               from pydantic import BaseModel, Field     from langchain_anthropic import ChatAnthropic          class Joke(BaseModel):         setup: str = Field(description="The setup of the joke")         punchline: str = Field(description="The punchline to the joke")          # Or any other chat model that supports tools.     # Please reference to to the documentation of structured_output     # to see an up to date list of which models support     # with_structured_output.     model = ChatAnthropic(model="claude-3-opus-20240229", temperature=0)     structured_llm = model.with_structured_output(Joke)     structured_llm.invoke(         "Why did the cat cross the road? To get to the other "         "side... and then lay down in the middle of it!"     )     

Read more here: <https://python.langchain.com/docs/how_to/structured_output/>

Parameters:     

  * **pydantic\_schema** \(_Any_\) – The pydantic schema of the entities to extract.

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – The language model to use.

  * **prompt** \([_ChatPromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html#langchain_core.prompts.chat.ChatPromptTemplate "langchain_core.prompts.chat.ChatPromptTemplate") _|__None_\)

  * **kwargs** \(_Any_\)

Returns:     

Chain \(LLMChain\) that can be used to extract information from a passage.

Return type:     

[_Chain_](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.base.Chain.html#langchain.chains.base.Chain "langchain.chains.base.Chain")

__On this page