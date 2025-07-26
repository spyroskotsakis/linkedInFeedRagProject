# create_extraction_chain_pydantic — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_tools.extraction.create_extraction_chain_pydantic.html
**Word Count:** 199
**Links Count:** 197
**Scraped:** 2025-07-21 07:49:32
**Status:** completed

---

# create\_extraction\_chain\_pydantic\#

langchain.chains.openai\_tools.extraction.create\_extraction\_chain\_pydantic\(

    _pydantic\_schemas : list\[type\[BaseModel\]\] | type\[BaseModel\]_,     _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _system\_message : str = 'Extract and save the relevant entities mentioned in the following passage together with their properties.\n\nIf a property is not present and is not required in the function parameters, do not include it in the output.'_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/openai_tools/extraction.html#create_extraction_chain_pydantic)\#     

Deprecated since version 0.1.14: LangChain has introduced a method called with\_structured\_output thatis available on ChatModels capable of tool calling.You can read more about the method here: <<https://python.langchain.com/docs/modules/model_io/chat/structured_output/>>. Please follow our extraction use case documentation for more guidelineson how to do information extraction with LLMs.<<https://python.langchain.com/docs/use_cases/extraction/>>. with\_structured\_output does not currently support a list of pydantic schemas. If this is a blocker or if you notice other issues, please provide feedback here:<[langchain-ai/langchain\#18154](https://github.com/langchain-ai/langchain/discussions/18154)> Use :meth:\`~ from pydantic import BaseModel, Field from langchain\_anthropic import ChatAnthropic

class Joke\(BaseModel\):     

setup: str = Field\(description=”The setup of the joke”\) punchline: str = Field\(description=”The punchline to the joke”\)

\# Or any other chat model that supports tools. \# Please reference to to the documentation of structured\_output \# to see an up to date list of which models support \# with\_structured\_output. model = ChatAnthropic\(model=”claude-3-opus-20240229”, temperature=0\) structured\_llm = model.with\_structured\_output\(Joke\) structured\_llm.invoke\(“Tell me a joke about cats.

> Make sure to call the Joke function.”\)

\` instead. It will not be removed until langchain==1.0.

Creates a chain that extracts information from a passage.

Parameters:     

  * **pydantic\_schemas** \(_list_ _\[__type_ _\[__BaseModel_ _\]__\]__|__type_ _\[__BaseModel_ _\]_\) – The schema of the entities to extract.

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – The language model to use.

  * **system\_message** \(_str_\) – The system message to use for extraction.

Returns:     

A runnable that extracts information from a passage.

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")

Examples using create\_extraction\_chain\_pydantic

  * [Generate Synthetic Data](https://python.langchain.com/docs/tutorials/data_generation/)

__On this page