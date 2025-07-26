# UnstructuredEPubLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.epub.UnstructuredEPubLoader.html
**Word Count:** 226
**Links Count:** 419
**Scraped:** 2025-07-21 08:10:17
**Status:** completed

---

# UnstructuredEPubLoader\#

_class _langchain\_community.document\_loaders.epub.UnstructuredEPubLoader\(

    _file\_path : str | Path_,     _mode : str = 'single'_,     _\*\* unstructured\_kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/epub.html#UnstructuredEPubLoader)\#     

Load EPub files using Unstructured.

You can run the loader in one of two modes: “single” and “elements”. If you use “single” mode, the document will be returned as a single langchain Document object. If you use “elements” mode, the unstructured library will split the document into elements such as Title and NarrativeText. You can pass in additional unstructured kwargs after mode to apply different unstructured settings.

Examples

from langchain\_community.document\_loaders import UnstructuredEPubLoader

loader = UnstructuredEPubLoader\(     

“example.epub”, mode=”elements”, strategy=”fast”,

\) docs = loader.load\(\)

References

<https://unstructured-io.github.io/unstructured/bricks.html#partition-epub>

Parameters:     

  * **file\_path** \(_str_ _|__Path_\) – The path to the EPub file to load.

  * **mode** \(_str_\) – The mode to use when loading the file. Can be one of “single”, “multi”, or “all”. Default is “single”.

  * **\*\*unstructured\_kwargs** \(_Any_\) – Any kwargs to pass to the unstructured.

Methods

`__init__`\(file\_path\[, mode\]\) |    ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Load file.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _file\_path : str | Path_,     _mode : str = 'single'_,     _\*\* unstructured\_kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/epub.html#UnstructuredEPubLoader.__init__)\#     

Parameters:     

  * **file\_path** \(_str_ _|__Path_\) – The path to the EPub file to load.

  * **mode** \(_str_\) – The mode to use when loading the file. Can be one of “single”, “multi”, or “all”. Default is “single”.

  * **\*\*unstructured\_kwargs** \(_Any_\) – Any kwargs to pass to the unstructured.

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

Examples using UnstructuredEPubLoader

  * [EPub ](https://python.langchain.com/docs/integrations/document_loaders/epub/)

  * [Unstructured](https://python.langchain.com/docs/integrations/providers/unstructured/)

__On this page