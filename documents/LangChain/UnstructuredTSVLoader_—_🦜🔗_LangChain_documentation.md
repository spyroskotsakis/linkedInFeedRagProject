# UnstructuredTSVLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.tsv.UnstructuredTSVLoader.html
**Word Count:** 155
**Links Count:** 418
**Scraped:** 2025-07-21 08:17:20
**Status:** completed

---

# UnstructuredTSVLoader\#

_class _langchain\_community.document\_loaders.tsv.UnstructuredTSVLoader\(

    _file\_path : str | Path_,     _mode : str = 'single'_,     _\*\* unstructured\_kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/tsv.html#UnstructuredTSVLoader)\#     

Load TSV files using Unstructured.

Like other Unstructured loaders, UnstructuredTSVLoader can be used in both “single” and “elements” mode. If you use the loader in “elements” mode, the TSV file will be a single Unstructured Table element. If you use the loader in “elements” mode, an HTML representation of the table will be available in the “text\_as\_html” key in the document metadata.

Examples

from langchain\_community.document\_loaders.tsv import UnstructuredTSVLoader

loader = UnstructuredTSVLoader\(“stanley-cups.tsv”, mode=”elements”\) docs = loader.load\(\)

Initialize with file path.

Methods

`__init__`\(file\_path\[, mode\]\) | Initialize with file path.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Load file.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      Parameters:     

  * **file\_path** \(_str_ _|__Path_\)

  * **mode** \(_str_\)

  * **unstructured\_kwargs** \(_Any_\)

\_\_init\_\_\(

    _file\_path : str | Path_,     _mode : str = 'single'_,     _\*\* unstructured\_kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/tsv.html#UnstructuredTSVLoader.__init__)\#     

Initialize with file path.

Parameters:     

  * **file\_path** \(_str_ _|__Path_\)

  * **mode** \(_str_\)

  * **unstructured\_kwargs** \(_Any_\)

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load file.

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

Examples using UnstructuredTSVLoader

  * [TSV](https://python.langchain.com/docs/integrations/document_loaders/tsv/)

  * [Unstructured](https://python.langchain.com/docs/integrations/providers/unstructured/)

__On this page