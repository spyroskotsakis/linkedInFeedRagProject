# GoogleTranslateTransformer — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/google_community/translate/langchain_google_community.translate.GoogleTranslateTransformer.html
**Word Count:** 141
**Links Count:** 107
**Scraped:** 2025-07-21 07:59:27
**Status:** completed

---

# GoogleTranslateTransformer\#

_class _langchain\_google\_community.translate.GoogleTranslateTransformer\(

    _project\_id : str_,     _\*_ ,     _location : str = 'global'_,     _model\_id : str | None = None_,     _glossary\_id : str | None = None_,     _api\_endpoint : str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/translate.html#GoogleTranslateTransformer)\#     

Translate text documents using Google Cloud Translation.

Parameters:     

  * **project\_id** \(_str_\) – Google Cloud Project ID.

  * **location** \(_str_\) – \(Optional\) Translate model location.

  * **model\_id** \(_str_ _|__None_\) – \(Optional\) Translate model ID to use.

  * **glossary\_id** \(_str_ _|__None_\) – \(Optional\) Translate glossary ID to use.

  * **api\_endpoint** \(_str_ _|__None_\) – \(Optional\) Regional endpoint to use.

Methods

`__init__`\(project\_id, \*\[, location, ...\]\) |    ---|---   `atransform_documents`\(documents, \*\*kwargs\) | Asynchronously transform a list of documents.   `transform_documents`\(documents, \*\*kwargs\) | Translate text documents using Google Translate.      \_\_init\_\_\(

    _project\_id : str_,     _\*_ ,     _location : str = 'global'_,     _model\_id : str | None = None_,     _glossary\_id : str | None = None_,     _api\_endpoint : str | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/translate.html#GoogleTranslateTransformer.__init__)\#     

Parameters:     

  * **project\_id** \(_str_\) – Google Cloud Project ID.

  * **location** \(_str_\) – \(Optional\) Translate model location.

  * **model\_id** \(_str_ _|__None_\) – \(Optional\) Translate model ID to use.

  * **glossary\_id** \(_str_ _|__None_\) – \(Optional\) Translate glossary ID to use.

  * **api\_endpoint** \(_str_ _|__None_\) – \(Optional\) Regional endpoint to use.

Return type:     

None

_async _atransform\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Asynchronously transform a list of documents.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – A sequence of Documents to be transformed.

  * **kwargs** \(_Any_\)

Returns:     

A sequence of transformed Documents.

Return type:     

Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

transform\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/translate.html#GoogleTranslateTransformer.transform_documents)\#     

Translate text documents using Google Translate.

Parameters:     

  * **source\_language\_code** – ISO 639 language code of the input document.

  * **target\_language\_code** – ISO 639 language code of the output document. For supported languages, refer to: <https://cloud.google.com/translate/docs/languages>

  * **mime\_type** – \(Optional\) Media Type of input text. Options: text/plain, text/html

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

_Sequence_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)