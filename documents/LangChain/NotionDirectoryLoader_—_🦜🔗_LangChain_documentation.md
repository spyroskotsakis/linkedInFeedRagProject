# NotionDirectoryLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.notion.NotionDirectoryLoader.html
**Word Count:** 98
**Links Count:** 419
**Scraped:** 2025-07-21 08:17:49
**Status:** completed

---

# NotionDirectoryLoader\#

_class _langchain\_community.document\_loaders.notion.NotionDirectoryLoader\(

    _path : str | Path_,     _\*_ ,     _encoding : str = 'utf-8'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/notion.html#NotionDirectoryLoader)\#     

Load Notion directory dump.

Initialize with a file path.

Methods

`__init__`\(path, \*\[, encoding\]\) | Initialize with a file path.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load documents.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      Parameters:     

  * **path** \(_str_ _|__Path_\)

  * **encoding** \(_str_\)

\_\_init\_\_\(

    _path : str | Path_,     _\*_ ,     _encoding : str = 'utf-8'_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/notion.html#NotionDirectoryLoader.__init__)\#     

Initialize with a file path.

Parameters:     

  * **path** \(_str_ _|__Path_\)

  * **encoding** \(_str_\)

Return type:     

None

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

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/notion.html#NotionDirectoryLoader.load)\#     

Load documents.

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

Examples using NotionDirectoryLoader

  * [Notion DB](https://python.langchain.com/docs/integrations/providers/notion/)

  * [Notion DB 2/2](https://python.langchain.com/docs/integrations/document_loaders/notion/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)