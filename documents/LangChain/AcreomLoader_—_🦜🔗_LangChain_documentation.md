# AcreomLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.acreom.AcreomLoader.html
**Word Count:** 104
**Links Count:** 419
**Scraped:** 2025-07-21 08:21:12
**Status:** completed

---

# AcreomLoader\#

_class _langchain\_community.document\_loaders.acreom.AcreomLoader\(

    _path : str | Path_,     _encoding : str = 'UTF-8'_,     _collect\_metadata : bool = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/acreom.html#AcreomLoader)\#     

Load acreom vault from a directory.

Initialize the loader.

Attributes

`FRONT_MATTER_REGEX` | Regex to match front matter metadata in markdown files.   ---|---      Methods

`__init__`\(path\[, encoding, collect\_metadata\]\) | Initialize the loader.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      Parameters:     

  * **path** \(_str_ _|__Path_\)

  * **encoding** \(_str_\)

  * **collect\_metadata** \(_bool_\)

\_\_init\_\_\(

    _path : str | Path_,     _encoding : str = 'UTF-8'_,     _collect\_metadata : bool = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/acreom.html#AcreomLoader.__init__)\#     

Initialize the loader.

Parameters:     

  * **path** \(_str_ _|__Path_\)

  * **encoding** \(_str_\)

  * **collect\_metadata** \(_bool_\)

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/acreom.html#AcreomLoader.lazy_load)\#     

A lazy loader for Documents.

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

Examples using AcreomLoader

  * [Acreom](https://python.langchain.com/docs/integrations/providers/acreom/)

  * [acreom](https://python.langchain.com/docs/integrations/document_loaders/acreom/)

__On this page