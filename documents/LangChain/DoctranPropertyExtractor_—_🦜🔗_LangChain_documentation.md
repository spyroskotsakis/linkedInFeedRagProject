# DoctranPropertyExtractor — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_transformers/langchain_community.document_transformers.doctran_text_extract.DoctranPropertyExtractor.html
**Word Count:** 103
**Links Count:** 132
**Scraped:** 2025-07-21 08:17:20
**Status:** completed

---

# DoctranPropertyExtractor\#

_class _langchain\_community.document\_transformers.doctran\_text\_extract.DoctranPropertyExtractor\(

    _properties : List\[dict\]_,     _openai\_api\_key : str | None = None_,     _openai\_api\_model : str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/doctran_text_extract.html#DoctranPropertyExtractor)\#     

Extract properties from text documents using doctran.

Parameters:     

  * **properties** \(_List_ _\[__dict_ _\]_\) – A list of the properties to extract.

  * **openai\_api\_key** \(_str_ _|__None_\) – OpenAI API key. Can also be specified via environment variable `OPENAI_API_KEY`.

  * **openai\_api\_model** \(_str_ _|__None_\)

Example               from langchain_community.document_transformers import DoctranPropertyExtractor          properties = [         {             "name": "category",             "description": "What type of email this is.",             "type": "string",             "enum": ["update", "action_item", "customer_feedback", "announcement", "other"],             "required": True,         },         {             "name": "mentions",             "description": "A list of all people mentioned in this email.",             "type": "array",             "items": {                 "name": "full_name",                 "description": "The full name of the person mentioned.",                 "type": "string",             },             "required": True,         },         {             "name": "eli5",             "description": "Explain this email to me like I'm 5 years old.",             "type": "string",             "required": True,         },     ]          # Pass in openai_api_key or set env var OPENAI_API_KEY     property_extractor = DoctranPropertyExtractor(properties)     transformed_document = await qa_transformer.atransform_documents(documents)     

Methods

`__init__`\(properties\[, openai\_api\_key, ...\]\) |    ---|---   `atransform_documents`\(documents, \*\*kwargs\) | Extracts properties from text documents using doctran.   `transform_documents`\(documents, \*\*kwargs\) | Extracts properties from text documents using doctran.      \_\_init\_\_\(

    _properties : List\[dict\]_,     _openai\_api\_key : str | None = None_,     _openai\_api\_model : str | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/doctran_text_extract.html#DoctranPropertyExtractor.__init__)\#     

Parameters:     

  * **properties** \(_List_ _\[__dict_ _\]_\)

  * **openai\_api\_key** \(_str_ _|__None_\)

  * **openai\_api\_model** \(_str_ _|__None_\)

Return type:     

None

_async _atransform\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/doctran_text_extract.html#DoctranPropertyExtractor.atransform_documents)\#     

Extracts properties from text documents using doctran.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

_Sequence_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

transform\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/doctran_text_extract.html#DoctranPropertyExtractor.transform_documents)\#     

Extracts properties from text documents using doctran.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

_Sequence_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Examples using DoctranPropertyExtractor

  * [Doctran: extract properties](https://python.langchain.com/docs/integrations/document_transformers/doctran_extract_properties/)

__On this page