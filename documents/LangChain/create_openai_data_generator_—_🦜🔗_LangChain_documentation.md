# create_openai_data_generator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/tabular_synthetic_data/langchain_experimental.tabular_synthetic_data.openai.create_openai_data_generator.html
**Word Count:** 152
**Links Count:** 106
**Scraped:** 2025-07-21 08:24:51
**Status:** completed

---

# create\_openai\_data\_generator\#

langchain\_experimental.tabular\_synthetic\_data.openai.create\_openai\_data\_generator\(

    _output\_schema : Dict\[str, Any\] | Type\[BaseModel\]_,     _llm : [ChatOpenAI](https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.openai.ChatOpenAI.html#langchain_community.chat_models.openai.ChatOpenAI "langchain_community.chat_models.openai.ChatOpenAI")_,     _prompt : [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")_,     _output\_parser : [BaseLLMOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseLLMOutputParser.html#langchain_core.output_parsers.base.BaseLLMOutputParser "langchain_core.output_parsers.base.BaseLLMOutputParser") | None = None_,     _\*\* kwargs: Any_, \) → [SyntheticDataGenerator](https://python.langchain.com/api_reference/experimental/tabular_synthetic_data/langchain_experimental.tabular_synthetic_data.base.SyntheticDataGenerator.html#langchain_experimental.tabular_synthetic_data.base.SyntheticDataGenerator "langchain_experimental.tabular_synthetic_data.base.SyntheticDataGenerator")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/tabular_synthetic_data/openai.html#create_openai_data_generator)\#     

Create an instance of SyntheticDataGenerator tailored for OpenAI models.

This function creates an LLM chain designed for structured output based on the provided schema, language model, and prompt template. The resulting chain is then used to instantiate and return a SyntheticDataGenerator.

Parameters:     

  * **output\_schema** \(_Union_ _\[__Dict_ _\[__str_ _,__Any_ _\]__,__Type_ _\[_[_BaseModel_](https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.models.BaseModel.html#langchain_experimental.video_captioning.models.BaseModel "langchain_experimental.video_captioning.models.BaseModel") _\]__\]_\) – Schema for expected

  * **a** \(_output. This can be either a dictionary representing a valid JsonSchema or_\)

  * **class.** \(_Pydantic BaseModel_\)

  * **llm** \([_ChatOpenAI_](https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html#langchain_openai.chat_models.base.ChatOpenAI "langchain_openai.chat_models.base.ChatOpenAI")\) – OpenAI language model to use.

  * **prompt** \([_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")\) – Template to be used for generating prompts.

  * **output\_parser** \(_Optional_ _\[_[_BaseLLMOutputParser_](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseLLMOutputParser.html#langchain_core.output_parsers.base.BaseLLMOutputParser "langchain_core.output_parsers.base.BaseLLMOutputParser") _\]__,__optional_\) – Parser for

  * **provided** \(_processing model outputs. If none is_\)

  * **inferred** \(_a default will be_\)

  * **types.** \(_from the function_\)

  * **kwargs** \(_Any_\) – Additional keyword arguments to be passed to

  * **create\_structured\_output\_chain.**

Return type:     

[_SyntheticDataGenerator_](https://python.langchain.com/api_reference/experimental/tabular_synthetic_data/langchain_experimental.tabular_synthetic_data.base.SyntheticDataGenerator.html#langchain_experimental.tabular_synthetic_data.base.SyntheticDataGenerator "langchain_experimental.tabular_synthetic_data.base.SyntheticDataGenerator")

Returns: SyntheticDataGenerator: An instance of the data generator set up with the constructed chain.

Usage:     

To generate synthetic data with a structured output, first define your desired output schema. Then, use this function to create a SyntheticDataGenerator instance. After obtaining the generator, you can utilize its methods to produce the desired synthetic data.

Examples using create\_openai\_data\_generator

  * [Generate Synthetic Data](https://python.langchain.com/docs/tutorials/data_generation/)

__On this page