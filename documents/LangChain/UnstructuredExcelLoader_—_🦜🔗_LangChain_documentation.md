# UnstructuredExcelLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.excel.UnstructuredExcelLoader.html
**Word Count:** 220
**Links Count:** 419
**Scraped:** 2025-07-21 08:18:46
**Status:** completed

---

# UnstructuredExcelLoader\#

_class _langchain\_community.document\_loaders.excel.UnstructuredExcelLoader\(

    _file\_path : str | Path_,     _mode : str = 'single'_,     _\*\* unstructured\_kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/excel.html#UnstructuredExcelLoader)\#     

Load Microsoft Excel files using Unstructured.

Like other Unstructured loaders, UnstructuredExcelLoader can be used in both “single” and “elements” mode. If you use the loader in “elements” mode, each sheet in the Excel file will be an Unstructured Table element. If you use the loader in “single” mode, an HTML representation of the table will be available in the “text\_as\_html” key in the document metadata.

Examples

from langchain\_community.document\_loaders.excel import UnstructuredExcelLoader

loader = UnstructuredExcelLoader\(“stanley-cups.xlsx”, mode=”elements”\) docs = loader.load\(\)

Parameters:     

  * **file\_path** \(_str_ _|__Path_\) – The path to the Microsoft Excel file.

  * **mode** \(_str_\) – The mode to use when partitioning the file. See unstructured docs for more info. Optional. Defaults to “single”.

  * **\*\*unstructured\_kwargs** \(_Any_\) – Keyword arguments to pass to unstructured.

Methods

`__init__`\(file\_path\[, mode\]\) |    ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Load file.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _file\_path : str | Path_,     _mode : str = 'single'_,     _\*\* unstructured\_kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/excel.html#UnstructuredExcelLoader.__init__)\#     

Parameters:     

  * **file\_path** \(_str_ _|__Path_\) – The path to the Microsoft Excel file.

  * **mode** \(_str_\) – The mode to use when partitioning the file. See unstructured docs for more info. Optional. Defaults to “single”.

  * **\*\*unstructured\_kwargs** \(_Any_\) – Keyword arguments to pass to unstructured.

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

Examples using UnstructuredExcelLoader

  * [Microsoft](https://python.langchain.com/docs/integrations/providers/microsoft/)

  * [Microsoft Excel](https://python.langchain.com/docs/integrations/document_loaders/microsoft_excel/)

  * [Unstructured](https://python.langchain.com/docs/integrations/providers/unstructured/)

__On this page