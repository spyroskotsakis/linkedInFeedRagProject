# OpenAIWhisperParser — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.audio.OpenAIWhisperParser.html
**Word Count:** 114
**Links Count:** 406
**Scraped:** 2025-07-21 08:01:32
**Status:** completed

---

# OpenAIWhisperParser\#

_class _langchain\_community.document\_loaders.parsers.audio.OpenAIWhisperParser\(

    _api\_key : str | None = None_,     _\*_ ,     _chunk\_duration\_threshold : float = 0.1_,     _base\_url : str | None = None_,     _language : str | None = None_,     _prompt : str | None = None_,     _response\_format : Literal\['json', 'text', 'srt', 'verbose\_json', 'vtt'\] | None = None_,     _temperature : float | None = None_,     _model : str = 'whisper-1'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/audio.html#OpenAIWhisperParser)\#     

Transcribe and parse audio files.

Audio transcription is with OpenAI Whisper model.

Parameters:     

  * **api\_key** \(_str_ _|__None_\) – OpenAI API key

  * **chunk\_duration\_threshold** \(_float_\) – Minimum duration of a chunk in seconds NOTE: According to the OpenAI API, the chunk duration should be at least 0.1 seconds. If the chunk duration is less or equal than the threshold, it will be skipped.

  * **base\_url** \(_str_ _|__None_\)

  * **language** \(_str_ _|__None_\)

  * **prompt** \(_str_ _|__None_\)

  * **response\_format** \(_Literal_ _\[__'json'__,__'text'__,__'srt'__,__'verbose\_json'__,__'vtt'__\]__|__None_\)

  * **temperature** \(_float_ _|__None_\)

  * **model** \(_str_\)

Methods

`__init__`\(\[api\_key, ...\]\) |    ---|---   `lazy_parse`\(blob\) | Lazily parse the blob.   `parse`\(blob\) | Eagerly parse the blob into a document or documents.      \_\_init\_\_\(

    _api\_key : str | None = None_,     _\*_ ,     _chunk\_duration\_threshold : float = 0.1_,     _base\_url : str | None = None_,     _language : str | None = None_,     _prompt : str | None = None_,     _response\_format : Literal\['json', 'text', 'srt', 'verbose\_json', 'vtt'\] | None = None_,     _temperature : float | None = None_,     _model : str = 'whisper-1'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/audio.html#OpenAIWhisperParser.__init__)\#     

Parameters:     

  * **api\_key** \(_str_ _|__None_\)

  * **chunk\_duration\_threshold** \(_float_\)

  * **base\_url** \(_str_ _|__None_\)

  * **language** \(_str_ _|__None_\)

  * **prompt** \(_str_ _|__None_\)

  * **response\_format** \(_Literal_ _\[__'json'__,__'text'__,__'srt'__,__'verbose\_json'__,__'vtt'__\]__|__None_\)

  * **temperature** \(_float_ _|__None_\)

  * **model** \(_str_\)

lazy\_parse\(

    _blob : [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")_, \) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/audio.html#OpenAIWhisperParser.lazy_parse)\#     

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

Examples using OpenAIWhisperParser

  * [Google](https://python.langchain.com/docs/integrations/providers/google/)

  * [YouTube audio](https://python.langchain.com/docs/integrations/document_loaders/youtube_audio/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)