# EverNoteLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.evernote.EverNoteLoader.html
**Word Count:** 285
**Links Count:** 419
**Scraped:** 2025-07-21 08:19:13
**Status:** completed

---

# EverNoteLoader\#

_class _langchain\_community.document\_loaders.evernote.EverNoteLoader\(

    _file\_path : str | Path_,     _load\_single\_document : bool = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/evernote.html#EverNoteLoader)\#     

Document loader for EverNote ENEX export files.

Loads EverNote notebook export files \(`.enex` format\) into LangChain Documents. Extracts plain text content from HTML and preserves note metadata including titles, timestamps, and attachments. Uses secure XML parsing to prevent vulnerabilities.

The loader supports two modes: \- Single document: Concatenates all notes into one Document \(default\) \- Multiple documents: Creates separate Documents for each note

[Instructions for creating ENEX files](https://help.evernote.com/hc/en-us/articles/209005557-Export-notes-and-notebooks-as-ENEX-or-HTML)

Example:               from langchain_community.document_loaders import EverNoteLoader          # Load all notes as a single document     loader = EverNoteLoader("my_notebook.enex")     documents = loader.load()          # Load each note as a separate document:     # documents = [ document1, document2, ... ]     loader = EverNoteLoader("my_notebook.enex", load_single_document=False)     documents = loader.load()          # Lazy loading for large files     for doc in loader.lazy_load():         print(f"Title: {doc.metadata.get('title', 'Untitled')}")         print(f"Content: {doc.page_content[:100]}...")     

Note

Requires the `lxml` and `html2text` packages to be installed. Install with: `pip install lxml html2text`

Initialize the EverNote loader.

Parameters:     

  * **file\_path** \(_str_ _|__Path_\) – Path to the EverNote export file \(`.enex` extension\).

  * **load\_single\_document** \(_bool_\) – Whether to concatenate all notes into a single Document. If `True`, only the `source` metadata is preserved. If `False`, each note becomes a separate Document with its own metadata.

Methods

`__init__`\(file\_path\[, load\_single\_document\]\) | Initialize the EverNote loader.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Load documents from EverNote export file.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _file\_path : str | Path_,     _load\_single\_document : bool = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/evernote.html#EverNoteLoader.__init__)\#     

Initialize the EverNote loader.

Parameters:     

  * **file\_path** \(_str_ _|__Path_\) – Path to the EverNote export file \(`.enex` extension\).

  * **load\_single\_document** \(_bool_\) – Whether to concatenate all notes into a single Document. If `True`, only the `source` metadata is preserved. If `False`, each note becomes a separate Document with its own metadata.

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/evernote.html#EverNoteLoader.lazy_load)\#     

Load documents from EverNote export file.

Depending on the `load_single_document` setting, either yields individual Documents for each note or a single Document containing all notes.

Yields:     

_Document_ – Either individual note Documents or a single combined Document.

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

Examples using EverNoteLoader

  * [EverNote](https://python.langchain.com/docs/integrations/document_loaders/evernote/)

__On this page