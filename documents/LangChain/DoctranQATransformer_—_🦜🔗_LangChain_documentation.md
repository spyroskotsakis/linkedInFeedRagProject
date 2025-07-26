# DoctranQATransformer — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_transformers/langchain_community.document_transformers.doctran_text_qa.DoctranQATransformer.html
**Word Count:** 76
**Links Count:** 132
**Scraped:** 2025-07-21 08:11:39
**Status:** completed

---

# DoctranQATransformer\#

_class _langchain\_community.document\_transformers.doctran\_text\_qa.DoctranQATransformer\(

    _openai\_api\_key : str | None = None_,     _openai\_api\_model : str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/doctran_text_qa.html#DoctranQATransformer)\#     

Extract QA from text documents using doctran.

Parameters:     

  * **openai\_api\_key** \(_str_ _|__None_\) – OpenAI API key. Can also be specified via environment variable `OPENAI_API_KEY`.

  * **openai\_api\_model** \(_str_ _|__None_\)

Example               from langchain_community.document_transformers import DoctranQATransformer          # Pass in openai_api_key or set env var OPENAI_API_KEY     qa_transformer = DoctranQATransformer()     transformed_document = await qa_transformer.atransform_documents(documents)     

Methods

`__init__`\(\[openai\_api\_key, openai\_api\_model\]\) |    ---|---   `atransform_documents`\(documents, \*\*kwargs\) | Asynchronously transform a list of documents.   `transform_documents`\(documents, \*\*kwargs\) | Extracts QA from text documents using doctran.      \_\_init\_\_\(

    _openai\_api\_key : str | None = None_,     _openai\_api\_model : str | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/doctran_text_qa.html#DoctranQATransformer.__init__)\#     

Parameters:     

  * **openai\_api\_key** \(_str_ _|__None_\)

  * **openai\_api\_model** \(_str_ _|__None_\)

Return type:     

None

_async _atransform\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/doctran_text_qa.html#DoctranQATransformer.atransform_documents)\#     

Asynchronously transform a list of documents.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – A sequence of Documents to be transformed.

  * **kwargs** \(_Any_\)

Returns:     

A sequence of transformed Documents.

Return type:     

_Sequence_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

transform\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/doctran_text_qa.html#DoctranQATransformer.transform_documents)\#     

Extracts QA from text documents using doctran.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

_Sequence_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Examples using DoctranQATransformer

  * [Doctran: interrogate documents](https://python.langchain.com/docs/integrations/document_transformers/doctran_interrogate_document/)

__On this page