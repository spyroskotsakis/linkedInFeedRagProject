# AssemblyAIAudioLoaderById — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.assemblyai.AssemblyAIAudioLoaderById.html
**Word Count:** 159
**Links Count:** 421
**Scraped:** 2025-07-21 08:05:36
**Status:** completed

---

# AssemblyAIAudioLoaderById\#

_class _langchain\_community.document\_loaders.assemblyai.AssemblyAIAudioLoaderById\(

    _transcript\_id : str_,     _api\_key : str_,     _transcript\_format : [TranscriptFormat](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.assemblyai.TranscriptFormat.html#langchain_community.document_loaders.assemblyai.TranscriptFormat "langchain_community.document_loaders.assemblyai.TranscriptFormat")_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/assemblyai.html#AssemblyAIAudioLoaderById)\#     

Load AssemblyAI audio transcripts.

It uses the AssemblyAI API to get an existing transcription and loads the transcribed text into one or more Documents, depending on the specified format.

Initializes the AssemblyAI AssemblyAIAudioLoaderById.

Parameters:     

  * **transcript\_id** \(_str_\) – Id of an existing transcription.

  * **transcript\_format** \([_TranscriptFormat_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.assemblyai.TranscriptFormat.html#langchain_community.document_loaders.assemblyai.TranscriptFormat "langchain_community.document_loaders.assemblyai.TranscriptFormat")\) – Transcript format to use. See class `TranscriptFormat` for more info.

  * **api\_key** \(_str_\) – AssemblyAI API key.

Methods

`__init__`\(transcript\_id, api\_key, ...\) | Initializes the AssemblyAI AssemblyAIAudioLoaderById.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Load data into Document objects.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _transcript\_id : str_,     _api\_key : str_,     _transcript\_format : [TranscriptFormat](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.assemblyai.TranscriptFormat.html#langchain_community.document_loaders.assemblyai.TranscriptFormat "langchain_community.document_loaders.assemblyai.TranscriptFormat")_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/assemblyai.html#AssemblyAIAudioLoaderById.__init__)\#     

Initializes the AssemblyAI AssemblyAIAudioLoaderById.

Parameters:     

  * **transcript\_id** \(_str_\) – Id of an existing transcription.

  * **transcript\_format** \([_TranscriptFormat_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.assemblyai.TranscriptFormat.html#langchain_community.document_loaders.assemblyai.TranscriptFormat "langchain_community.document_loaders.assemblyai.TranscriptFormat")\) – Transcript format to use. See class `TranscriptFormat` for more info.

  * **api\_key** \(_str_\) – AssemblyAI API key.

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/assemblyai.html#AssemblyAIAudioLoaderById.lazy_load)\#     

Load data into Document objects.

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

__On this page