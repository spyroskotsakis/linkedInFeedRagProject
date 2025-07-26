# YoutubeLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.youtube.YoutubeLoader.html
**Word Count:** 137
**Links Count:** 435
**Scraped:** 2025-07-21 08:22:37
**Status:** completed

---

# YoutubeLoader\#

_class _langchain\_community.document\_loaders.youtube.YoutubeLoader\(

    _video\_id : str_,     _add\_video\_info : bool = False_,     _language : str | Sequence\[str\] = 'en'_,     _translation : str | None = None_,     _transcript\_format : [TranscriptFormat](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.youtube.TranscriptFormat.html#langchain_community.document_loaders.youtube.TranscriptFormat "langchain_community.document_loaders.youtube.TranscriptFormat") = TranscriptFormat.TEXT_,     _continue\_on\_failure : bool = False_,     _chunk\_size\_seconds : int = 120_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/youtube.html#YoutubeLoader)\#     

Load YouTube video transcripts.

Initialize with YouTube video ID.

Methods

`__init__`\(video\_id\[, add\_video\_info, ...\]\) | Initialize with YouTube video ID.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `extract_video_id`\(youtube\_url\) | Extract video ID from common YouTube URLs.   `from_youtube_url`\(youtube\_url, \*\*kwargs\) | Given a YouTube URL, construct a loader.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load YouTube transcripts into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      Parameters:     

  * **video\_id** \(_str_\)

  * **add\_video\_info** \(_bool_\)

  * **language** \(_Union_ _\[__str_ _,__Sequence_ _\[__str_ _\]__\]_\)

  * **translation** \(_Optional_ _\[__str_ _\]_\)

  * **transcript\_format** \([_TranscriptFormat_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.youtube.TranscriptFormat.html#langchain_community.document_loaders.youtube.TranscriptFormat "langchain_community.document_loaders.youtube.TranscriptFormat")\)

  * **continue\_on\_failure** \(_bool_\)

  * **chunk\_size\_seconds** \(_int_\)

\_\_init\_\_\(

    _video\_id : str_,     _add\_video\_info : bool = False_,     _language : str | Sequence\[str\] = 'en'_,     _translation : str | None = None_,     _transcript\_format : [TranscriptFormat](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.youtube.TranscriptFormat.html#langchain_community.document_loaders.youtube.TranscriptFormat "langchain_community.document_loaders.youtube.TranscriptFormat") = TranscriptFormat.TEXT_,     _continue\_on\_failure : bool = False_,     _chunk\_size\_seconds : int = 120_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/youtube.html#YoutubeLoader.__init__)\#     

Initialize with YouTube video ID.

Parameters:     

  * **video\_id** \(_str_\)

  * **add\_video\_info** \(_bool_\)

  * **language** \(_str_ _|__Sequence_ _\[__str_ _\]_\)

  * **translation** \(_str_ _|__None_\)

  * **transcript\_format** \([_TranscriptFormat_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.youtube.TranscriptFormat.html#langchain_community.document_loaders.youtube.TranscriptFormat "langchain_community.document_loaders.youtube.TranscriptFormat")\)

  * **continue\_on\_failure** \(_bool_\)

  * **chunk\_size\_seconds** \(_int_\)

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_static _extract\_video\_id\(_youtube\_url : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/youtube.html#YoutubeLoader.extract_video_id)\#     

Extract video ID from common YouTube URLs.

Parameters:     

**youtube\_url** \(_str_\)

Return type:     

str

_classmethod _from\_youtube\_url\(

    _youtube\_url : str_,     _\*\* kwargs: Any_, \) → YoutubeLoader[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/youtube.html#YoutubeLoader.from_youtube_url)\#     

Given a YouTube URL, construct a loader. See YoutubeLoader\(\) constructor for a list of keyword arguments.

Parameters:     

  * **youtube\_url** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

_YoutubeLoader_

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/youtube.html#YoutubeLoader.load)\#     

Load YouTube transcripts into Document objects.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

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

Examples using YoutubeLoader

  * [Build a Query Analysis System](https://python.langchain.com/docs/tutorials/query_analysis/)

  * [Google](https://python.langchain.com/docs/integrations/providers/google/)

  * [YouTube](https://python.langchain.com/docs/integrations/providers/youtube/)

  * [YouTube transcripts](https://python.langchain.com/docs/integrations/document_loaders/youtube_transcript/)

__On this page