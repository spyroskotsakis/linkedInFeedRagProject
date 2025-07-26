# UnstructuredURLLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.url.UnstructuredURLLoader.html
**Word Count:** 185
**Links Count:** 420
**Scraped:** 2025-07-21 08:22:10
**Status:** completed

---

# UnstructuredURLLoader\#

_class _langchain\_community.document\_loaders.url.UnstructuredURLLoader\(

    _urls : List\[str\]_,     _continue\_on\_failure : bool = True_,     _mode : str = 'single'_,     _show\_progress\_bar : bool = False_,     _\*\* unstructured\_kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/url.html#UnstructuredURLLoader)\#     

Load files from remote URLs using Unstructured.

Use the unstructured partition function to detect the MIME type and route the file to the appropriate partitioner.

You can run the loader in one of two modes: “single” and “elements”. If you use “single” mode, the document will be returned as a single langchain Document object. If you use “elements” mode, the unstructured library will split the document into elements such as Title and NarrativeText. You can pass in additional unstructured kwargs after mode to apply different unstructured settings.

Examples

from langchain\_community.document\_loaders import UnstructuredURLLoader

loader = UnstructuredURLLoader\(     

urls=\[“<url-1>”, “<url-2>”\], mode=”elements”, strategy=”fast”,

\) docs = loader.load\(\)

References

<https://unstructured-io.github.io/unstructured/bricks.html#partition>

Initialize with file path.

Methods

`__init__`\(urls\[, continue\_on\_failure, mode, ...\]\) | Initialize with file path.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load file.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      Parameters:     

  * **urls** \(_List_ _\[__str_ _\]_\)

  * **continue\_on\_failure** \(_bool_\)

  * **mode** \(_str_\)

  * **show\_progress\_bar** \(_bool_\)

  * **unstructured\_kwargs** \(_Any_\)

\_\_init\_\_\(

    _urls : List\[str\]_,     _continue\_on\_failure : bool = True_,     _mode : str = 'single'_,     _show\_progress\_bar : bool = False_,     _\*\* unstructured\_kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/url.html#UnstructuredURLLoader.__init__)\#     

Initialize with file path.

Parameters:     

  * **urls** \(_List_ _\[__str_ _\]_\)

  * **continue\_on\_failure** \(_bool_\)

  * **mode** \(_str_\)

  * **show\_progress\_bar** \(_bool_\)

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

A lazy loader for Documents.

Return type:     

Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/url.html#UnstructuredURLLoader.load)\#     

Load file.

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

Examples using UnstructuredURLLoader

  * [URL](https://python.langchain.com/docs/integrations/document_loaders/url/)

  * [Unstructured](https://python.langchain.com/docs/integrations/providers/unstructured/)

__On this page