# YoutubeAudioLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.blob_loaders.youtube_audio.YoutubeAudioLoader.html
**Word Count:** 27
**Links Count:** 397
**Scraped:** 2025-07-21 08:02:07
**Status:** completed

---

# YoutubeAudioLoader\#

_class _langchain\_community.document\_loaders.blob\_loaders.youtube\_audio.YoutubeAudioLoader\(_urls : List\[str\]_, _save\_dir : str_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/blob_loaders/youtube_audio.html#YoutubeAudioLoader)\#     

Load YouTube urls as audio file\(s\).

Methods

`__init__`\(urls, save\_dir\) |    ---|---   `yield_blobs`\(\) | Yield audio blobs for each url.      Parameters:     

  * **urls** \(_List_ _\[__str_ _\]_\)

  * **save\_dir** \(_str_\)

\_\_init\_\_\(

    _urls : List\[str\]_,     _save\_dir : str_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/blob_loaders/youtube_audio.html#YoutubeAudioLoader.__init__)\#     

Parameters:     

  * **urls** \(_List_ _\[__str_ _\]_\)

  * **save\_dir** \(_str_\)

yield\_blobs\(\) → Iterable\[[Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/blob_loaders/youtube_audio.html#YoutubeAudioLoader.yield_blobs)\#     

Yield audio blobs for each url.

Return type:     

_Iterable_\[[_Blob_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")\]

Examples using YoutubeAudioLoader

  * [Google](https://python.langchain.com/docs/integrations/providers/google/)

  * [YouTube audio](https://python.langchain.com/docs/integrations/document_loaders/youtube_audio/)

__On this page