# ObsidianLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.obsidian.ObsidianLoader.html
**Word Count:** 152
**Links Count:** 418
**Scraped:** 2025-07-21 08:07:22
**Status:** completed

---

# ObsidianLoader\#

_class _langchain\_community.document\_loaders.obsidian.ObsidianLoader\(

    _path : str | Path_,     _encoding : str = 'UTF-8'_,     _collect\_metadata : bool = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/obsidian.html#ObsidianLoader)\#     

Load Obsidian files from directory.

Initialize with a path.

Parameters:     

  * **path** \(_str_ _|__Path_\) – Path to the directory containing the Obsidian files.

  * **encoding** \(_str_\) – Charset encoding, defaults to “UTF-8”

  * **collect\_metadata** \(_bool_\) – Whether to collect metadata from the front matter. Defaults to True.

Attributes

`DATAVIEW_INLINE_BRACKET_REGEX` |    ---|---   `DATAVIEW_INLINE_PAREN_REGEX` |    `DATAVIEW_LINE_REGEX` |    `FRONT_MATTER_REGEX` |    `TAG_REGEX` |    `TEMPLATE_VARIABLE_REGEX` |       Methods

`__init__`\(path\[, encoding, collect\_metadata\]\) | Initialize with a path.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _path : str | Path_,     _encoding : str = 'UTF-8'_,     _collect\_metadata : bool = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/obsidian.html#ObsidianLoader.__init__)\#     

Initialize with a path.

Parameters:     

  * **path** \(_str_ _|__Path_\) – Path to the directory containing the Obsidian files.

  * **encoding** \(_str_\) – Charset encoding, defaults to “UTF-8”

  * **collect\_metadata** \(_bool_\) – Whether to collect metadata from the front matter. Defaults to True.

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/obsidian.html#ObsidianLoader.lazy_load)\#     

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

Examples using ObsidianLoader

  * [Obsidian](https://python.langchain.com/docs/integrations/document_loaders/obsidian/)

__On this page