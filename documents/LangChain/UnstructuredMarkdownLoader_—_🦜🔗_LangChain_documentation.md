# UnstructuredMarkdownLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.markdown.UnstructuredMarkdownLoader.html
**Word Count:** 228
**Links Count:** 423
**Scraped:** 2025-07-21 08:16:51
**Status:** completed

---

# UnstructuredMarkdownLoader\#

_class _langchain\_community.document\_loaders.markdown.UnstructuredMarkdownLoader\(

    _file\_path : str | Path_,     _mode : str = 'single'_,     _\*\* unstructured\_kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/markdown.html#UnstructuredMarkdownLoader)\#     

Load Markdown files using Unstructured.

You can run the loader in one of two modes: “single” and “elements”. If you use “single” mode, the document will be returned as a single langchain Document object. If you use “elements” mode, the unstructured library will split the document into elements such as Title and NarrativeText. You can pass in additional unstructured kwargs after mode to apply different unstructured settings.

Setup:     

Install `langchain-community`.               pip install -U langchain-community     

Instantiate:                    from langchain_community.document_loaders import UnstructuredMarkdownLoader          loader = UnstructuredMarkdownLoader(         "./example_data/example.md",         mode="elements",         strategy="fast",     )     

Lazy load:                    docs = []     docs_lazy = loader.lazy_load()          # async variant:     # docs_lazy = await loader.alazy_load()          for doc in docs_lazy:         docs.append(doc)     print(docs[0].page_content[:100])     print(docs[0].metadata)                    Sample Markdown Document     {'source': './example_data/example.md', 'category_depth': 0, 'last_modified': '2024-08-14T15:04:18', 'languages': ['eng'], 'filetype': 'text/markdown', 'file_directory': './example_data', 'filename': 'example.md', 'category': 'Title', 'element_id': '3d0b313864598e704aa26c728ecb61e5'}     

Async load:                    docs = await loader.aload()     print(docs[0].page_content[:100])     print(docs[0].metadata)                    Sample Markdown Document     {'source': './example_data/example.md', 'category_depth': 0, 'last_modified': '2024-08-14T15:04:18', 'languages': ['eng'], 'filetype': 'text/markdown', 'file_directory': './example_data', 'filename': 'example.md', 'category': 'Title', 'element_id': '3d0b313864598e704aa26c728ecb61e5'}     

References

<https://unstructured-io.github.io/unstructured/core/partition.html#partition-md>

Parameters:     

  * **file\_path** \(_str_ _|__Path_\) – The path to the Markdown file to load.

  * **mode** \(_str_\) – The mode to use when loading the file. Can be one of “single”, “multi”, or “all”. Default is “single”.

  * **\*\*unstructured\_kwargs** \(_Any_\) – Any kwargs to pass to the unstructured.

Methods

`__init__`\(file\_path\[, mode\]\) |    ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Load file.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _file\_path : str | Path_,     _mode : str = 'single'_,     _\*\* unstructured\_kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/markdown.html#UnstructuredMarkdownLoader.__init__)\#     

Parameters:     

  * **file\_path** \(_str_ _|__Path_\) – The path to the Markdown file to load.

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

Examples using UnstructuredMarkdownLoader

  * [Apache Doris](https://python.langchain.com/docs/integrations/vectorstores/apache_doris/)

  * [How to load Markdown](https://python.langchain.com/docs/how_to/document_loader_markdown/)

  * [StarRocks](https://python.langchain.com/docs/integrations/vectorstores/starrocks/)

  * [Unstructured](https://python.langchain.com/docs/integrations/providers/unstructured/)

  * [UnstructuredMarkdownLoader](https://python.langchain.com/docs/integrations/document_loaders/unstructured_markdown/)

  * [langchain](https://python.langchain.com/docs/changes/changelog/langchain/)

__On this page