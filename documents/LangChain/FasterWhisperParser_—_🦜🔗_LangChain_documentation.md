# FasterWhisperParser — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.audio.FasterWhisperParser.html
**Word Count:** 223
**Links Count:** 405
**Scraped:** 2025-07-21 08:11:12
**Status:** completed

---

# FasterWhisperParser\#

_class _langchain\_community.document\_loaders.parsers.audio.FasterWhisperParser\(

    _\*_ ,     _device : str | None = 'cuda'_,     _model\_size : str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/audio.html#FasterWhisperParser)\#     

Transcribe and parse audio files with faster-whisper.

faster-whisper is a reimplementation of OpenAI’s Whisper model using CTranslate2, which is up to 4 times faster than openai/whisper for the same accuracy while using less memory. The efficiency can be further improved with 8-bit quantization on both CPU and GPU.

It can automatically detect the following 14 languages and transcribe the text into their respective languages: en, zh, fr, de, ja, ko, ru, es, th, it, pt, vi, ar, tr.

The gitbub repository for faster-whisper is : [SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper)

Example: Load a YouTube video and transcribe the video speech into a document.                    from langchain.document_loaders.generic import GenericLoader     from langchain_community.document_loaders.parsers.audio         import FasterWhisperParser     from langchain.document_loaders.blob_loaders.youtube_audio         import YoutubeAudioLoader               url="https://www.youtube.com/watch?v=your_video"     save_dir="your_dir/"     loader = GenericLoader(         YoutubeAudioLoader([url],save_dir),         FasterWhisperParser()     )     docs = loader.load()     

Initialize the parser.

Parameters:     

  * **device** \(_str_ _|__None_\) – It can be “cuda” or “cpu” based on the available device.

  * **model\_size** \(_str_ _|__None_\) – There are four model sizes to choose from: “base”, “small”, “medium”, and “large-v3”, based on the available GPU memory.

Methods

`__init__`\(\*\[, device, model\_size\]\) | Initialize the parser.   ---|---   `lazy_parse`\(blob\) | Lazily parse the blob.   `parse`\(blob\) | Eagerly parse the blob into a document or documents.      \_\_init\_\_\(

    _\*_ ,     _device : str | None = 'cuda'_,     _model\_size : str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/audio.html#FasterWhisperParser.__init__)\#     

Initialize the parser.

Parameters:     

  * **device** \(_str_ _|__None_\) – It can be “cuda” or “cpu” based on the available device.

  * **model\_size** \(_str_ _|__None_\) – There are four model sizes to choose from: “base”, “small”, “medium”, and “large-v3”, based on the available GPU memory.

lazy\_parse\(

    _blob : [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")_, \) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/audio.html#FasterWhisperParser.lazy_parse)\#     

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