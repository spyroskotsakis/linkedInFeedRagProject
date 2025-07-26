# create_metadata_tagger — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_transformers/langchain_community.document_transformers.openai_functions.create_metadata_tagger.html
**Word Count:** 149
**Links Count:** 118
**Scraped:** 2025-07-21 08:03:51
**Status:** completed

---

# create\_metadata\_tagger\#

langchain\_community.document\_transformers.openai\_functions.create\_metadata\_tagger\(

    _metadata\_schema : Dict\[str, Any\] | Type\[BaseModel\]_,     _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _prompt : [ChatPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html#langchain_core.prompts.chat.ChatPromptTemplate "langchain_core.prompts.chat.ChatPromptTemplate") | None = None_,     _\*_ ,     _tagging\_chain\_kwargs : Dict | None = None_, \) → [OpenAIMetadataTagger](https://python.langchain.com/api_reference/community/document_transformers/langchain_community.document_transformers.openai_functions.OpenAIMetadataTagger.html#langchain_community.document_transformers.openai_functions.OpenAIMetadataTagger "langchain_community.document_transformers.openai_functions.OpenAIMetadataTagger")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/openai_functions.html#create_metadata_tagger)\#     

Create a DocumentTransformer that uses an OpenAI function chain to automatically     

> tag documents with metadata based on their content and an input schema.

Args:     

metadata\_schema: Either a dictionary or pydantic.BaseModel class. If a dictionary     

is passed in, it’s assumed to already be a valid JsonSchema. For best results, pydantic.BaseModels should have docstrings describing what the schema represents and descriptions for the parameters.

llm: Language model to use, assumed to support the OpenAI function-calling API.     

Defaults to use “gpt-3.5-turbo-0613”

prompt: BasePromptTemplate to pass to the model.

Returns:     

An LLMChain that will pass the given function to the model.

Example:                    from langchain_community.chat_models import ChatOpenAI     from langchain_community.document_transformers import create_metadata_tagger     from langchain_core.documents import Document          schema = {         "properties": {             "movie_title": { "type": "string" },             "critic": { "type": "string" },             "tone": {                 "type": "string",                 "enum": ["positive", "negative"]             },             "rating": {                 "type": "integer",                 "description": "The number of stars the critic rated the movie"             }         },         "required": ["movie_title", "critic", "tone"]     }          # Must be an OpenAI model that supports functions     llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")          document_transformer = create_metadata_tagger(schema, llm)     original_documents = [         Document(page_content="Review of The Bee Movie     

By Roger Ebert

This is the greatest movie ever made. 4 out of 5 stars.”\),     

Document\(page\_content=”Review of The Godfather

By Anonymous

This movie was super boring. 1 out of 5 stars.”, metadata=\{“reliable”: False\}\),     

\]

enhanced\_documents = document\_transformer.transform\_documents\(original\_documents\)

Parameters:     

  * **metadata\_schema** \(_Dict_ _\[__str_ _,__Any_ _\]__|__Type_ _\[__BaseModel_ _\]_\)

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\)

  * **prompt** \([_ChatPromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html#langchain_core.prompts.chat.ChatPromptTemplate "langchain_core.prompts.chat.ChatPromptTemplate") _|__None_\)

  * **tagging\_chain\_kwargs** \(_Dict_ _|__None_\)

Return type:     

[_OpenAIMetadataTagger_](https://python.langchain.com/api_reference/community/document_transformers/langchain_community.document_transformers.openai_functions.OpenAIMetadataTagger.html#langchain_community.document_transformers.openai_functions.OpenAIMetadataTagger "langchain_community.document_transformers.openai_functions.OpenAIMetadataTagger")

Examples using create\_metadata\_tagger

  * [OpenAI metadata tagger](https://python.langchain.com/docs/integrations/document_transformers/openai_metadata_tagger/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)