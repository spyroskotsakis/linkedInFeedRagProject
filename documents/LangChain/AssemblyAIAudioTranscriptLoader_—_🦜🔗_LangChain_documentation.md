# AssemblyAIAudioTranscriptLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.assemblyai.AssemblyAIAudioTranscriptLoader.html
**Word Count:** 259
**Links Count:** 423
**Scraped:** 2025-07-21 08:05:00
**Status:** completed

---

# AssemblyAIAudioTranscriptLoader\#

_class _langchain\_community.document\_loaders.assemblyai.AssemblyAIAudioTranscriptLoader\(

    _file\_path : str | Path_,     _\*_ ,     _transcript\_format : [TranscriptFormat](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.assemblyai.TranscriptFormat.html#langchain_community.document_loaders.assemblyai.TranscriptFormat "langchain_community.document_loaders.assemblyai.TranscriptFormat") = TranscriptFormat.TEXT_,     _config : assemblyai.TranscriptionConfig | None = None_,     _api\_key : str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/assemblyai.html#AssemblyAIAudioTranscriptLoader)\#     

Load AssemblyAI audio transcripts.

It uses the AssemblyAI API to transcribe audio files and loads the transcribed text into one or more Documents, depending on the specified format.

To use, you should have the `assemblyai` python package installed, and the environment variable `ASSEMBLYAI_API_KEY` set with your API key. Alternatively, the API key can also be passed as an argument.

Audio files can be specified via an URL or a local file path.

Initializes the AssemblyAI AudioTranscriptLoader.

Parameters:     

  * **file\_path** \(_Union_ _\[__str_ _,__Path_ _\]_\) – An URL or a local file path.

  * **transcript\_format** \([_TranscriptFormat_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.assemblyai.TranscriptFormat.html#langchain_community.document_loaders.assemblyai.TranscriptFormat "langchain_community.document_loaders.assemblyai.TranscriptFormat")\) – Transcript format to use. See class `TranscriptFormat` for more info.

  * **config** \(_Optional_ _\[__assemblyai.TranscriptionConfig_ _\]_\) – Transcription options and features. If `None` is given, the Transcriber’s default configuration will be used.

  * **api\_key** \(_Optional_ _\[__str_ _\]_\) – AssemblyAI API key.

Methods

`__init__`\(file\_path, \*\[, transcript\_format, ...\]\) | Initializes the AssemblyAI AudioTranscriptLoader.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Transcribes the audio file and loads the transcript into documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _file\_path : str | Path_,     _\*_ ,     _transcript\_format : [TranscriptFormat](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.assemblyai.TranscriptFormat.html#langchain_community.document_loaders.assemblyai.TranscriptFormat "langchain_community.document_loaders.assemblyai.TranscriptFormat") = TranscriptFormat.TEXT_,     _config : assemblyai.TranscriptionConfig | None = None_,     _api\_key : str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/assemblyai.html#AssemblyAIAudioTranscriptLoader.__init__)\#     

Initializes the AssemblyAI AudioTranscriptLoader.

Parameters:     

  * **file\_path** \(_Union_ _\[__str_ _,__Path_ _\]_\) – An URL or a local file path.

  * **transcript\_format** \([_TranscriptFormat_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.assemblyai.TranscriptFormat.html#langchain_community.document_loaders.assemblyai.TranscriptFormat "langchain_community.document_loaders.assemblyai.TranscriptFormat")\) – Transcript format to use. See class `TranscriptFormat` for more info.

  * **config** \(_Optional_ _\[__assemblyai.TranscriptionConfig_ _\]_\) – Transcription options and features. If `None` is given, the Transcriber’s default configuration will be used.

  * **api\_key** \(_Optional_ _\[__str_ _\]_\) – AssemblyAI API key.

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/assemblyai.html#AssemblyAIAudioTranscriptLoader.lazy_load)\#     

Transcribes the audio file and loads the transcript into documents.

It uses the AssemblyAI API to transcribe the audio file and blocks until the transcription is finished.

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\_and\_split\(

    _text\_splitter : [TextSplitter](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html#langchain_text_splitters.base.TextSplitter "langchain_text_splitters.base.TextSplitter") | None = None_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load Documents and split into chunks. Chunks are returned as Documents.

Do not override this method. It should be considered to be deprecated\!

Parameters:     

**text\_splitter** \(_Optional_ _\[_[_TextSplitter_](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html#langchain_text_splitters.base.TextSplitter "langchain_text_splitters.base.TextSplitter") _\]_\) – TextSplitter instance to use for splitting documents. Defaults to RecursiveCharacterTextSplitter.

Returns:     

List of Documents.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Examples using AssemblyAIAudioTranscriptLoader

  * [AssemblyAI](https://python.langchain.com/docs/integrations/providers/assemblyai/)

  * [AssemblyAI Audio Transcripts](https://python.langchain.com/docs/integrations/document_loaders/assemblyai/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)