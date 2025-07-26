# DoctranTextTranslator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_transformers/langchain_community.document_transformers.doctran_text_translate.DoctranTextTranslator.html
**Word Count:** 72
**Links Count:** 132
**Scraped:** 2025-07-21 08:20:44
**Status:** completed

---

# DoctranTextTranslator\#

_class _langchain\_community.document\_transformers.doctran\_text\_translate.DoctranTextTranslator\(

    _openai\_api\_key : str | None = None_,     _language : str = 'english'_,     _openai\_api\_model : str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/doctran_text_translate.html#DoctranTextTranslator)\#     

Translate text documents using doctran.

Parameters:     

  * **openai\_api\_key** \(_Optional_ _\[__str_ _\]_\) – OpenAI API key. Can also be specified via environment variable

  * **OPENAI\_API\_KEY.**

  * **language** \(_str_\) – The language to translate _to_.

  * **openai\_api\_model** \(_Optional_ _\[__str_ _\]_\)

Example               

from langchain\_community.document\_transformers import DoctranTextTranslator

\# Pass in openai\_api\_key or set env var OPENAI\_API\_KEY qa\_translator = DoctranTextTranslator\(language=”spanish”\) translated\_document = await qa\_translator.atransform\_documents\(documents\)

Methods

`__init__`\(\[openai\_api\_key, language, ...\]\) |    ---|---   `atransform_documents`\(documents, \*\*kwargs\) | Translates text documents using doctran.   `transform_documents`\(documents, \*\*kwargs\) | Translates text documents using doctran.      \_\_init\_\_\(

    _openai\_api\_key : str | None = None_,     _language : str = 'english'_,     _openai\_api\_model : str | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/doctran_text_translate.html#DoctranTextTranslator.__init__)\#     

Parameters:     

  * **openai\_api\_key** \(_str_ _|__None_\)

  * **language** \(_str_\)

  * **openai\_api\_model** \(_str_ _|__None_\)

Return type:     

None

_async _atransform\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/doctran_text_translate.html#DoctranTextTranslator.atransform_documents)\#     

Translates text documents using doctran.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

_Sequence_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

transform\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/doctran_text_translate.html#DoctranTextTranslator.transform_documents)\#     

Translates text documents using doctran.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

_Sequence_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Examples using DoctranTextTranslator

  * [Doctran: language translation](https://python.langchain.com/docs/integrations/document_transformers/doctran_translate_document/)

__On this page