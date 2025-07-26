# YandexSTTParser — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.audio.YandexSTTParser.html
**Word Count:** 159
**Links Count:** 404
**Scraped:** 2025-07-21 08:01:32
**Status:** completed

---

# YandexSTTParser\#

_class _langchain\_community.document\_loaders.parsers.audio.YandexSTTParser\(

    _\*_ ,     _api\_key : str | None = None_,     _iam\_token : str | None = None_,     _model : str = 'general'_,     _language : str = 'auto'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/audio.html#YandexSTTParser)\#     

Transcribe and parse audio files. Audio transcription is with OpenAI Whisper model.

Initialize the parser.

Parameters:     

  * **api\_key** \(_str_ _|__None_\) – API key for a service account

  * **role.** \(_with the ai.speechkit-stt.user_\)

  * **iam\_token** \(_str_ _|__None_\) – IAM token for a service account

  * **role.**

  * **model** \(_str_\) – Recognition model name. Defaults to general.

  * **language** \(_str_\) – The language in ISO 639-1 format. Defaults to automatic language recognition.

Either api\_key or iam\_token must be provided, but not both.

Methods

`__init__`\(\*\[, api\_key, iam\_token, model, ...\]\) | Initialize the parser.   ---|---   `lazy_parse`\(blob\) | Lazily parse the blob.   `parse`\(blob\) | Eagerly parse the blob into a document or documents.      \_\_init\_\_\(

    _\*_ ,     _api\_key : str | None = None_,     _iam\_token : str | None = None_,     _model : str = 'general'_,     _language : str = 'auto'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/audio.html#YandexSTTParser.__init__)\#     

Initialize the parser.

Parameters:     

  * **api\_key** \(_str_ _|__None_\) – API key for a service account

  * **role.** \(_with the ai.speechkit-stt.user_\)

  * **iam\_token** \(_str_ _|__None_\) – IAM token for a service account

  * **role.**

  * **model** \(_str_\) – Recognition model name. Defaults to general.

  * **language** \(_str_\) – The language in ISO 639-1 format. Defaults to automatic language recognition.

Either api\_key or iam\_token must be provided, but not both.

lazy\_parse\(

    _blob : [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")_, \) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/audio.html#YandexSTTParser.lazy_parse)\#     

Lazily parse the blob.

Parameters:     

**blob** \([_Blob_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")\)

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