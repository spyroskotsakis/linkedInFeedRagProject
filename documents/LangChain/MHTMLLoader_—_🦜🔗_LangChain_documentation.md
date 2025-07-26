# MHTMLLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.mhtml.MHTMLLoader.html
**Word Count:** 214
**Links Count:** 418
**Scraped:** 2025-07-21 08:02:07
**Status:** completed

---

# MHTMLLoader\#

_class _langchain\_community.document\_loaders.mhtml.MHTMLLoader\(

    _file\_path : str | Path_,     _open\_encoding : str | None = None_,     _bs\_kwargs : dict | None = None_,     _get\_text\_separator : str = ''_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/mhtml.html#MHTMLLoader)\#     

Parse MHTML files with BeautifulSoup.

initialize with path, and optionally, file encoding to use, and any kwargs to pass to the BeautifulSoup object.

Parameters:     

  * **file\_path** \(_str_ _|__Path_\) – Path to file to load.

  * **open\_encoding** \(_str_ _|__None_\) – The encoding to use when opening the file.

  * **bs\_kwargs** \(_dict_ _|__None_\) – Any kwargs to pass to the BeautifulSoup object.

  * **get\_text\_separator** \(_str_\) – The separator to use when getting the text from the soup.

Methods

`__init__`\(file\_path\[, open\_encoding, ...\]\) | initialize with path, and optionally, file encoding to use, and any kwargs to pass to the BeautifulSoup object.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Load MHTML document into document objects.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _file\_path : str | Path_,     _open\_encoding : str | None = None_,     _bs\_kwargs : dict | None = None_,     _get\_text\_separator : str = ''_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/mhtml.html#MHTMLLoader.__init__)\#     

initialize with path, and optionally, file encoding to use, and any kwargs to pass to the BeautifulSoup object.

Parameters:     

  * **file\_path** \(_str_ _|__Path_\) – Path to file to load.

  * **open\_encoding** \(_str_ _|__None_\) – The encoding to use when opening the file.

  * **bs\_kwargs** \(_dict_ _|__None_\) – Any kwargs to pass to the BeautifulSoup object.

  * **get\_text\_separator** \(_str_\) – The separator to use when getting the text from the soup.

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

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/mhtml.html#MHTMLLoader.lazy_load)\#     

Load MHTML document into document objects.

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

Examples using MHTMLLoader

  * [mhtml](https://python.langchain.com/docs/integrations/document_loaders/mhtml/)

__On this page