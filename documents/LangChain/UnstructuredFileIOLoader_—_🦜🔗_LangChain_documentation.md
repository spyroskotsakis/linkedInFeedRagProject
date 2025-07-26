# UnstructuredFileIOLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.unstructured.UnstructuredFileIOLoader.html
**Word Count:** 233
**Links Count:** 420
**Scraped:** 2025-07-21 08:03:18
**Status:** completed

---

# UnstructuredFileIOLoader\#

_class _langchain\_community.document\_loaders.unstructured.UnstructuredFileIOLoader\(

    _file : IO\[bytes\]_,     _\*_ ,     _mode : str = 'single'_,     _\*\* unstructured\_kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/unstructured.html#UnstructuredFileIOLoader)\#     

Deprecated since version 0.2.8: Use `:class:`~langchain_unstructured.UnstructuredLoader`` instead. It will not be removed until langchain-community==1.0.

Load file-like objects opened in read mode using Unstructured.

The file loader uses the unstructured partition function and will automatically detect the file type. You can run the loader in different modes: “single”, “elements”, and “paged”. The default “single” mode will return a single langchain Document object. If you use “elements” mode, the unstructured library will split the document into elements such as Title and NarrativeText and return those as individual langchain Document objects. In addition to these post-processing modes \(which are specific to the LangChain Loaders\), Unstructured has its own “chunking” parameters for post-processing elements into more useful chunks for uses cases such as Retrieval Augmented Generation \(RAG\). You can pass in additional unstructured kwargs to configure different unstructured settings.

Examples

from langchain\_community.document\_loaders import UnstructuredFileIOLoader

with open\(“example.pdf”, “rb”\) as f:     

loader = UnstructuredFileIOLoader\(     

f, mode=”elements”, strategy=”fast”,

\) docs = loader.load\(\)

References

<https://docs.unstructured.io/open-source/core-functionality/partitioning> <https://docs.unstructured.io/open-source/core-functionality/chunking>

Initialize with file path.

Methods

`__init__`\(file, \*\[, mode\]\) | Initialize with file path.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Load file.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      Parameters:     

  * **file** \(_IO_ _\[__bytes_ _\]_\)

  * **mode** \(_str_\)

  * **unstructured\_kwargs** \(_Any_\)

\_\_init\_\_\(

    _file : IO\[bytes\]_,     _\*_ ,     _mode : str = 'single'_,     _\*\* unstructured\_kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/unstructured.html#UnstructuredFileIOLoader.__init__)\#     

Initialize with file path.

Parameters:     

  * **file** \(_IO_ _\[__bytes_ _\]_\)

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

Examples using UnstructuredFileIOLoader

  * [Google Drive](https://python.langchain.com/docs/integrations/document_loaders/google_drive/)

  * [Unstructured](https://python.langchain.com/docs/integrations/providers/unstructured/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)