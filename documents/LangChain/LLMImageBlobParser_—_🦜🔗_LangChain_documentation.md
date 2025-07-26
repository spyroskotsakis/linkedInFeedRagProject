# LLMImageBlobParser — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.images.LLMImageBlobParser.html
**Word Count:** 149
**Links Count:** 412
**Scraped:** 2025-07-21 08:16:18
**Status:** completed

---

# LLMImageBlobParser\#

_class _langchain\_community.document\_loaders.parsers.images.LLMImageBlobParser\(

    _\*_ ,     _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_,     _prompt : str = 'You are an assistant tasked with summarizing images for retrieval. 1. These summaries will be embedded and used to retrieve the raw image. Give a concise summary of the image that is well optimized for retrieval\n2. extract all the text from the image. Do not exclude any content from the page.\nFormat answer in markdown without explanatory text and without markdown delimiter \`\`\` at the beginning. '_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/images.html#LLMImageBlobParser)\#     

Parser for analyzing images using a language model \(LLM\).

model\#     

The language model to use for analysis.

Type:     

[BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")

prompt\#     

The prompt to provide to the language model.

Type:     

str

Initializes the LLMImageBlobParser.

Parameters:     

  * **model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\) – The language model to use for analysis.

  * **prompt** \(_str_\) – The prompt to provide to the language model.

Methods

`__init__`\(\*, model\[, prompt\]\) | Initializes the LLMImageBlobParser.   ---|---   `lazy_parse`\(blob\) | Lazily parse a blob and yields Documents containing the parsed content.   `parse`\(blob\) | Eagerly parse the blob into a document or documents.      \_\_init\_\_\(

    _\*_ ,     _model : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_,     _prompt : str = 'You are an assistant tasked with summarizing images for retrieval. 1. These summaries will be embedded and used to retrieve the raw image. Give a concise summary of the image that is well optimized for retrieval\n2. extract all the text from the image. Do not exclude any content from the page.\nFormat answer in markdown without explanatory text and without markdown delimiter \`\`\` at the beginning. '_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/images.html#LLMImageBlobParser.__init__)\#     

Initializes the LLMImageBlobParser.

Parameters:     

  * **model** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\) – The language model to use for analysis.

  * **prompt** \(_str_\) – The prompt to provide to the language model.

lazy\_parse\(

    _blob : [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")_, \) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Lazily parse a blob and yields Documents containing the parsed content.

Parameters:     

**blob** \([_Blob_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")\) – The blob to be parsed.

Yields:     

_Document_ – A document containing the parsed content and metadata.

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

parse\(_blob : [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")_\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Eagerly parse the blob into a document or documents.

This is a convenience method for interactive development environment.

Production applications should favor the lazy\_parse method instead.

Subclasses should generally not over-ride this parse method.

Parameters:     

**blob** \([_Blob_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")\) – Blob instance

Returns:     

List of documents

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)