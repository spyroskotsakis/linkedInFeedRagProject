# IFixitLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.ifixit.IFixitLoader.html
**Word Count:** 250
**Links Count:** 442
**Scraped:** 2025-07-21 08:03:18
**Status:** completed

---

# IFixitLoader\#

_class _langchain\_community.document\_loaders.ifixit.IFixitLoader\(_web\_path : str_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/ifixit.html#IFixitLoader)\#     

Load iFixit repair guides, device wikis and answers.

iFixit is the largest, open repair community on the web. The site contains nearly 100k repair manuals, 200k Questions & Answers on 42k devices, and all the data is licensed under CC-BY.

This loader will allow you to download the text of a repair guide, text of Q&A’s and wikis from devices on iFixit using their open APIs and web scraping.

Initialize with a web path.

Methods

`__init__`\(web\_path\) | Initialize with a web path.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.   `load_device`\(\[url\_override, include\_guides\]\) | Loads a device   `load_guide`\(\[url\_override\]\) | Load a guide   `load_questions_and_answers`\(\[url\_override\]\) | Load a list of questions and answers.   `load_suggestions`\(\[query, doc\_type\]\) | Load suggestions.      Parameters:     

**web\_path** \(_str_\)

\_\_init\_\_\(_web\_path : str_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/ifixit.html#IFixitLoader.__init__)\#     

Initialize with a web path.

Parameters:     

**web\_path** \(_str_\)

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

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/ifixit.html#IFixitLoader.load)\#     

Load data into Document objects.

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

load\_device\(

    _url\_override : str | None = None_,     _include\_guides : bool = True_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/ifixit.html#IFixitLoader.load_device)\#     

Loads a device

Parameters:     

  * **url\_override** \(_str_ _|__None_\) – A URL to override the default URL.

  * **include\_guides** \(_bool_\) – Whether to include guides linked to from the device. Defaults to True.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Returns:

load\_guide\(

    _url\_override : str | None = None_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/ifixit.html#IFixitLoader.load_guide)\#     

Load a guide

Parameters:     

**url\_override** \(_str_ _|__None_\) – A URL to override the default URL.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Returns: List\[Document\]

load\_questions\_and\_answers\(

    _url\_override : str | None = None_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/ifixit.html#IFixitLoader.load_questions_and_answers)\#     

Load a list of questions and answers.

Parameters:     

**url\_override** \(_str_ _|__None_\) – A URL to override the default URL.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Returns: List\[Document\]

_static _load\_suggestions\(

    _query : str = ''_,     _doc\_type : str = 'all'_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/ifixit.html#IFixitLoader.load_suggestions)\#     

Load suggestions.

Parameters:     

  * **query** \(_str_\) – A query string

  * **doc\_type** \(_str_\) – The type of document to search for. Can be one of “all”, “device”, “guide”, “teardown”, “answer”, “wiki”.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Returns:

Examples using IFixitLoader

  * [iFixit](https://python.langchain.com/docs/integrations/document_loaders/ifixit/)

__On this page