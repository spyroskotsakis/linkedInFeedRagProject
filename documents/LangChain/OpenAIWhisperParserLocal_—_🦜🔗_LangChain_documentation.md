# OpenAIWhisperParserLocal — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.audio.OpenAIWhisperParserLocal.html
**Word Count:** 227
**Links Count:** 404
**Scraped:** 2025-07-21 08:20:13
**Status:** completed

---

# OpenAIWhisperParserLocal\#

_class _langchain\_community.document\_loaders.parsers.audio.OpenAIWhisperParserLocal\(

    _device : str = '0'_,     _lang\_model : str | None = None_,     _batch\_size : int = 8_,     _chunk\_length : int = 30_,     _forced\_decoder\_ids : Tuple\[Dict\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/audio.html#OpenAIWhisperParserLocal)\#     

Transcribe and parse audio files with OpenAI Whisper model.

Audio transcription with OpenAI Whisper model locally from transformers.

Parameters: device - device to use

> NOTE: By default uses the gpu if available, if you want to use cpu, please set device = “cpu”

lang\_model - whisper model to use, for example “openai/whisper-medium” forced\_decoder\_ids - id states for decoder in multilanguage model,

> usage example: from transformers import WhisperProcessor processor = WhisperProcessor.from\_pretrained\(“openai/whisper-medium”\) forced\_decoder\_ids = WhisperProcessor.get\_decoder\_prompt\_ids\(language=”french”, >
>> task=”transcribe”\) >  > forced\_decoder\_ids = WhisperProcessor.get\_decoder\_prompt\_ids\(language=”french”, task=”translate”\)

Initialize the parser.

Parameters:     

  * **device** \(_str_\) – device to use.

  * **lang\_model** \(_str_ _|__None_\) – whisper model to use, for example “openai/whisper-medium”. Defaults to None.

  * **forced\_decoder\_ids** \(_Tuple_ _\[__Dict_ _\]__|__None_\) – id states for decoder in a multilanguage model. Defaults to None.

  * **batch\_size** \(_int_\) – batch size used for decoding Defaults to 8.

  * **chunk\_length** \(_int_\) – chunk length used during inference. Defaults to 30s.

Methods

`__init__`\(\[device, lang\_model, batch\_size, ...\]\) | Initialize the parser.   ---|---   `lazy_parse`\(blob\) | Lazily parse the blob.   `parse`\(blob\) | Eagerly parse the blob into a document or documents.      \_\_init\_\_\(

    _device : str = '0'_,     _lang\_model : str | None = None_,     _batch\_size : int = 8_,     _chunk\_length : int = 30_,     _forced\_decoder\_ids : Tuple\[Dict\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/audio.html#OpenAIWhisperParserLocal.__init__)\#     

Initialize the parser.

Parameters:     

  * **device** \(_str_\) – device to use.

  * **lang\_model** \(_str_ _|__None_\) – whisper model to use, for example “openai/whisper-medium”. Defaults to None.

  * **forced\_decoder\_ids** \(_Tuple_ _\[__Dict_ _\]__|__None_\) – id states for decoder in a multilanguage model. Defaults to None.

  * **batch\_size** \(_int_\) – batch size used for decoding Defaults to 8.

  * **chunk\_length** \(_int_\) – chunk length used during inference. Defaults to 30s.

lazy\_parse\(

    _blob : [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")_, \) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/audio.html#OpenAIWhisperParserLocal.lazy_parse)\#     

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

__On this page