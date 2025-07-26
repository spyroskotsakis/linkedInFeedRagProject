# aformat_document — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.aformat_document.html
**Word Count:** 93
**Links Count:** 132
**Scraped:** 2025-07-21 07:54:02
**Status:** completed

---

# aformat\_document\#

_async _langchain\_core.prompts.base.aformat\_document\(

    _doc : [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")_,     _prompt : [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")\[str\]_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompts/base.html#aformat_document)\#     

Async format a document into a string based on a prompt template.

First, this pulls information from the document from two sources:

  1. page\_content:     

This takes the information from the document.page\_content and assigns it to a variable named page\_content.

  2. metadata:     

This takes information from document.metadata and assigns it to variables of the same name.

Those variables are then passed into the prompt to produce a formatted string.

Parameters:     

  * **doc** \([_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\) – Document, the page\_content and metadata will be used to create the final string.

  * **prompt** \([_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") _\[__str_ _\]_\) – BasePromptTemplate, will be used to format the page\_content and metadata into the final string.

Returns:     

string of the document formatted.

Return type:     

str

__On this page