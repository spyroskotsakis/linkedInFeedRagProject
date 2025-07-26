# UnstructuredLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/unstructured/document_loaders/langchain_unstructured.document_loaders.UnstructuredLoader.html
**Word Count:** 151
**Links Count:** 105
**Scraped:** 2025-07-21 07:58:09
**Status:** completed

---

# UnstructuredLoader\#

_class _langchain\_unstructured.document\_loaders.UnstructuredLoader\(

    _file\_path : str | Path | list\[str\] | list\[Path\] | None = None_,     _\*_ ,     _file : IO\[bytes\] | list\[IO\[bytes\]\] | None = None_,     _partition\_via\_api : bool = False_,     _post\_processors : list\[Callable\[\[str\], str\]\] | None = None_,     _api\_key : str | None = None_,     _client : UnstructuredClient | None = None_,     _url : str | None = None_,     _web\_url : str | None = None_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_unstructured/document_loaders.html#UnstructuredLoader)\#     

Unstructured document loader interface.

Setup:     

Install `langchain-unstructured` and set environment variable `UNSTRUCTURED_API_KEY`.

Instantiate:      Lazy load:                    docs = []     docs_lazy = loader.lazy_load()          # async variant:     # docs_lazy = await loader.alazy_load()          for doc in docs_lazy:         docs.append(doc)     print(docs[0].page_content[:100])     print(docs[0].metadata)                    1 2 0 2     {'source': './example_data/layout-parser-paper.pdf', 'coordinates': {'points': ((16.34, 213.36), (16.34, 253.36), (36.34, 253.36), (36.34, 213.36)), 'system': 'PixelSpace', 'layout_width': 612, 'layout_height': 792}, 'file_directory': './example_data', 'filename': 'layout-parser-paper.pdf', 'languages': ['eng'], 'last_modified': '2024-07-25T21:28:58', 'page_number': 1, 'filetype': 'application/pdf', 'category': 'UncategorizedText', 'element_id': 'd3ce55f220dfb75891b4394a18bcb973'}     

Async load:                    docs = await loader.aload()     print(docs[0].page_content[:100])     print(docs[0].metadata)                    1 2 0 2     {'source': './example_data/layout-parser-paper.pdf', 'coordinates': {'points': ((16.34, 213.36), (16.34, 253.36), (36.34, 253.36), (36.34, 213.36)), 'system': 'PixelSpace', 'layout_width': 612, 'layout_height': 792}, 'file_directory': './example_data', 'filename': 'layout-parser-paper.pdf', 'languages': ['eng'], 'last_modified': '2024-07-25T21:28:58', 'page_number': 1, 'filetype': 'application/pdf', 'category': 'UncategorizedText', 'element_id': 'd3ce55f220dfb75891b4394a18bcb973'}     

Load URL:                    loader = UnstructuredLoader(web_url="https://www.example.com/")     print(docs[0])                    page_content='Example Domain' metadata={'category_depth': 0, 'languages': ['eng'], 'filetype': 'text/html', 'url': 'https://www.example.com/', 'category': 'Title', 'element_id': 'fdaa78d856f9d143aeeed85bf23f58f8'}                    print(docs[1])                    page_content='This domain is for use in illustrative examples in documents. You may use this domain in literature without prior coordination or asking for permission.' metadata={'languages': ['eng'], 'parent_id': 'fdaa78d856f9d143aeeed85bf23f58f8', 'filetype': 'text/html', 'url': 'https://www.example.com/', 'category': 'NarrativeText', 'element_id': '3652b8458b0688639f973fe36253c992'}     

References

<https://docs.unstructured.io/api-reference/api-services/sdk> <https://docs.unstructured.io/api-reference/api-services/overview> <https://docs.unstructured.io/open-source/core-functionality/partitioning> <https://docs.unstructured.io/open-source/core-functionality/chunking>

Initialize loader.

Methods

`__init__`\(\[file\_path, file, ...\]\) | Initialize loader.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Load file\(s\) to the \_UnstructuredBaseLoader.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      Parameters:     

  * **file\_path** \(_Optional_ _\[__str_ _|__Path_ _|__list_ _\[__str_ _\]__|__list_ _\[__Path_ _\]__\]_\)

  * **file** \(_Optional_ _\[__IO_ _\[__bytes_ _\]__|__list_ _\[__IO_ _\[__bytes_ _\]__\]__\]_\)

  * **partition\_via\_api** \(_bool_\)

  * **post\_processors** \(_Optional_ _\[__list_ _\[__Callable_ _\[__\[__str_ _\]__,__str_ _\]__\]__\]_\)

  * **api\_key** \(_Optional_ _\[__str_ _\]_\)

  * **client** \(_Optional_ _\[__UnstructuredClient_ _\]_\)

  * **url** \(_Optional_ _\[__str_ _\]_\)

  * **web\_url** \(_Optional_ _\[__str_ _\]_\)

  * **kwargs** \(_Any_\)

\_\_init\_\_\(

    _file\_path : str | Path | list\[str\] | list\[Path\] | None = None_,     _\*_ ,     _file : IO\[bytes\] | list\[IO\[bytes\]\] | None = None_,     _partition\_via\_api : bool = False_,     _post\_processors : list\[Callable\[\[str\], str\]\] | None = None_,     _api\_key : str | None = None_,     _client : UnstructuredClient | None = None_,     _url : str | None = None_,     _web\_url : str | None = None_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_unstructured/document_loaders.html#UnstructuredLoader.__init__)\#     

Initialize loader.

Parameters:     

  * **file\_path** \(_str_ _|__Path_ _|__list_ _\[__str_ _\]__|__list_ _\[__Path_ _\]__|__None_\)

  * **file** \(_IO_ _\[__bytes_ _\]__|__list_ _\[__IO_ _\[__bytes_ _\]__\]__|__None_\)

  * **partition\_via\_api** \(_bool_\)

  * **post\_processors** \(_list_ _\[__Callable_ _\[__\[__str_ _\]__,__str_ _\]__\]__|__None_\)

  * **api\_key** \(_str_ _|__None_\)

  * **client** \(_UnstructuredClient_ _|__None_\)

  * **url** \(_str_ _|__None_\)

  * **web\_url** \(_str_ _|__None_\)

  * **kwargs** \(_Any_\)

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_unstructured/document_loaders.html#UnstructuredLoader.lazy_load)\#     

Load file\(s\) to the \_UnstructuredBaseLoader.

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

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)