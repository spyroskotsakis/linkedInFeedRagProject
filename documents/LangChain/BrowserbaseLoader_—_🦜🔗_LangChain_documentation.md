# BrowserbaseLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.browserbase.BrowserbaseLoader.html
**Word Count:** 102
**Links Count:** 419
**Scraped:** 2025-07-21 08:16:18
**Status:** completed

---

# BrowserbaseLoader\#

_class _langchain\_community.document\_loaders.browserbase.BrowserbaseLoader\(

    _urls : Sequence\[str\]_,     _text\_content : bool = False_,     _api\_key : str | None = None_,     _project\_id : str | None = None_,     _session\_id : str | None = None_,     _proxy : bool | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/browserbase.html#BrowserbaseLoader)\#     

Load pre-rendered web pages using a headless browser hosted on Browserbase.

Depends on browserbase and playwright packages. Get your API key from <https://browserbase.com>

Methods

`__init__`\(urls\[, text\_content, api\_key, ...\]\) |    ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Load pages from URLs   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      Parameters:     

  * **urls** \(_Sequence_ _\[__str_ _\]_\)

  * **text\_content** \(_bool_\)

  * **api\_key** \(_str_ _|__None_\)

  * **project\_id** \(_str_ _|__None_\)

  * **session\_id** \(_str_ _|__None_\)

  * **proxy** \(_bool_ _|__None_\)

\_\_init\_\_\(

    _urls : Sequence\[str\]_,     _text\_content : bool = False_,     _api\_key : str | None = None_,     _project\_id : str | None = None_,     _session\_id : str | None = None_,     _proxy : bool | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/browserbase.html#BrowserbaseLoader.__init__)\#     

Parameters:     

  * **urls** \(_Sequence_ _\[__str_ _\]_\)

  * **text\_content** \(_bool_\)

  * **api\_key** \(_str_ _|__None_\)

  * **project\_id** \(_str_ _|__None_\)

  * **session\_id** \(_str_ _|__None_\)

  * **proxy** \(_bool_ _|__None_\)

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/browserbase.html#BrowserbaseLoader.lazy_load)\#     

Load pages from URLs

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

Examples using BrowserbaseLoader

  * [Browserbase](https://python.langchain.com/docs/integrations/document_loaders/browserbase/)

__On this page