# BiliBiliLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.bilibili.BiliBiliLoader.html
**Word Count:** 218
**Links Count:** 418
**Scraped:** 2025-07-21 08:09:49
**Status:** completed

---

# BiliBiliLoader\#

_class _langchain\_community.document\_loaders.bilibili.BiliBiliLoader\(

    _video\_urls : List\[str\]_,     _sessdata : str = ''_,     _bili\_jct : str = ''_,     _buvid3 : str = ''_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/bilibili.html#BiliBiliLoader)\#     

Load fetching transcripts from BiliBili videos.

Initialize the loader with BiliBili video URLs and authentication cookies. if no authentication cookies are provided, the loader can’t get transcripts and will only fetch videos info.

Parameters:     

  * **video\_urls** \(_List_ _\[__str_ _\]_\) – List of BiliBili video URLs.

  * **sessdata** \(_str_\) – SESSDATA cookie value for authentication.

  * **bili\_jct** \(_str_\) – BILI\_JCT cookie value for authentication.

  * **buvid3** \(_str_\) – BUVI3 cookie value for authentication.

Methods

`__init__`\(video\_urls\[, sessdata, bili\_jct, ...\]\) | Initialize the loader with BiliBili video URLs and authentication cookies.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load and return a list of documents containing video transcripts.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _video\_urls : List\[str\]_,     _sessdata : str = ''_,     _bili\_jct : str = ''_,     _buvid3 : str = ''_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/bilibili.html#BiliBiliLoader.__init__)\#     

Initialize the loader with BiliBili video URLs and authentication cookies. if no authentication cookies are provided, the loader can’t get transcripts and will only fetch videos info.

Parameters:     

  * **video\_urls** \(_List_ _\[__str_ _\]_\) – List of BiliBili video URLs.

  * **sessdata** \(_str_\) – SESSDATA cookie value for authentication.

  * **bili\_jct** \(_str_\) – BILI\_JCT cookie value for authentication.

  * **buvid3** \(_str_\) – BUVI3 cookie value for authentication.

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/bilibili.html#BiliBiliLoader.load)\#     

Load and return a list of documents containing video transcripts.

Returns:     

List of Document objects transcripts and metadata.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

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

Examples using BiliBiliLoader

  * [BiliBili](https://python.langchain.com/docs/integrations/document_loaders/bilibili/)

__On this page