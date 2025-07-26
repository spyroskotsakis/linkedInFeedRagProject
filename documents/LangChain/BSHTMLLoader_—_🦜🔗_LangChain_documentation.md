# BSHTMLLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.html_bs.BSHTMLLoader.html
**Word Count:** 238
**Links Count:** 420
**Scraped:** 2025-07-21 08:21:41
**Status:** completed

---

# BSHTMLLoader\#

_class _langchain\_community.document\_loaders.html\_bs.BSHTMLLoader\(

    _file\_path : str | Path_,     _open\_encoding : str | None = None_,     _bs\_kwargs : dict | None = None_,     _get\_text\_separator : str = ''_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/html_bs.html#BSHTMLLoader)\#     

\_\_ModuleName\_\_ document loader integration

Setup:     

Install `langchain-community` and `bs4`.               pip install -U langchain-community bs4     

Instantiate:                    from langchain_community.document_loaders import BSHTMLLoader          loader = BSHTMLLoader(         file_path="./example_data/fake-content.html",     )     

Lazy load:                    docs = []     docs_lazy = loader.lazy_load()          # async variant:     # docs_lazy = await loader.alazy_load()          for doc in docs_lazy:         docs.append(doc)     print(docs[0].page_content[:100])     print(docs[0].metadata)                    Test Title               My First Heading     My first paragraph.                    {'source': './example_data/fake-content.html', 'title': 'Test Title'}     

Async load:                    docs = await loader.aload()     print(docs[0].page_content[:100])     print(docs[0].metadata)                    Test Title               My First Heading     My first paragraph.                    {'source': './example_data/fake-content.html', 'title': 'Test Title'}     

initialize with path, and optionally, file encoding to use, and any kwargs to pass to the BeautifulSoup object.

Parameters:     

  * **file\_path** \(_str_ _|__Path_\) – The path to the file to load.

  * **open\_encoding** \(_str_ _|__None_\) – The encoding to use when opening the file.

  * **bs\_kwargs** \(_dict_ _|__None_\) – Any kwargs to pass to the BeautifulSoup object.

  * **get\_text\_separator** \(_str_\) – The separator to use when calling get\_text on the soup.

Methods

`__init__`\(file\_path\[, open\_encoding, ...\]\) | initialize with path, and optionally, file encoding to use, and any kwargs to pass to the BeautifulSoup object.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Load HTML document into document objects.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _file\_path : str | Path_,     _open\_encoding : str | None = None_,     _bs\_kwargs : dict | None = None_,     _get\_text\_separator : str = ''_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/html_bs.html#BSHTMLLoader.__init__)\#     

initialize with path, and optionally, file encoding to use, and any kwargs to pass to the BeautifulSoup object.

Parameters:     

  * **file\_path** \(_str_ _|__Path_\) – The path to the file to load.

  * **open\_encoding** \(_str_ _|__None_\) – The encoding to use when opening the file.

  * **bs\_kwargs** \(_dict_ _|__None_\) – Any kwargs to pass to the BeautifulSoup object.

  * **get\_text\_separator** \(_str_\) – The separator to use when calling get\_text on the soup.

Return type:     

None

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/html_bs.html#BSHTMLLoader.lazy_load)\#     

Load HTML document into document objects.

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

Examples using BSHTMLLoader

  * [BSHTMLLoader](https://python.langchain.com/docs/integrations/document_loaders/bshtml/)

  * [How to handle long text when doing extraction](https://python.langchain.com/docs/how_to/extraction_long_text/)

  * [How to load HTML](https://python.langchain.com/docs/how_to/document_loader_html/)

__On this page