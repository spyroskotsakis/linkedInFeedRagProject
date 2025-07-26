# create_extraction_chain — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.extraction.create_extraction_chain.html
**Word Count:** 206
**Links Count:** 198
**Scraped:** 2025-07-21 07:48:33
**Status:** completed

---

# create\_extraction\_chain\#

langchain.chains.openai\_functions.extraction.create\_extraction\_chain\(

    _schema : dict_,     _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _prompt : [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") | None = None_,     _tags : list\[str\] | None = None_,     _verbose : bool = False_, \) → [Chain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.base.Chain.html#langchain.chains.base.Chain "langchain.chains.base.Chain")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/openai_functions/extraction.html#create_extraction_chain)\#     

Deprecated since version 0.1.14: LangChain has introduced a method called with\_structured\_output thatis available on ChatModels capable of tool calling.You can read more about the method here: <<https://python.langchain.com/docs/modules/model_io/chat/structured_output/>>. Please follow our extraction use case documentation for more guidelineson how to do information extraction with LLMs.<<https://python.langchain.com/docs/use_cases/extraction/>>. If you notice other issues, please provide feedback here:<[langchain-ai/langchain\#18154](https://github.com/langchain-ai/langchain/discussions/18154)> Use :meth:\`~ from pydantic import BaseModel, Field from langchain\_anthropic import ChatAnthropic

class Joke\(BaseModel\):     

setup: str = Field\(description=”The setup of the joke”\) punchline: str = Field\(description=”The punchline to the joke”\)

\# Or any other chat model that supports tools. \# Please reference to to the documentation of structured\_output \# to see an up to date list of which models support \# with\_structured\_output. model = ChatAnthropic\(model=”claude-3-opus-20240229”, temperature=0\) structured\_llm = model.with\_structured\_output\(Joke\) structured\_llm.invoke\(“Tell me a joke about cats.

> Make sure to call the Joke function.”\)

\` instead. It will not be removed until langchain==1.0.

Creates a chain that extracts information from a passage.

Parameters:     

  * **schema** \(_dict_\) – The schema of the entities to extract.

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – The language model to use.

  * **prompt** \([_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") _|__None_\) – The prompt to use for extraction.

  * **verbose** \(_bool_\) – Whether to run in verbose mode. In verbose mode, some intermediate logs will be printed to the console. Defaults to the global verbose value, accessible via langchain.globals.get\_verbose\(\).

  * **tags** \(_list_ _\[__str_ _\]__|__None_\)

Returns:     

Chain that can be used to extract information from a passage.

Return type:     

[_Chain_](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.base.Chain.html#langchain.chains.base.Chain "langchain.chains.base.Chain")

__On this page