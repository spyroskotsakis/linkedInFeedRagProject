# WikipediaLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.wikipedia.WikipediaLoader.html
**Word Count:** 263
**Links Count:** 419
**Scraped:** 2025-07-21 08:20:13
**Status:** completed

---

# WikipediaLoader\#

_class _langchain\_community.document\_loaders.wikipedia.WikipediaLoader\(

    _query : str_,     _lang : str = 'en'_,     _load\_max\_docs : int | None = 25_,     _load\_all\_available\_meta : bool | None = False_,     _doc\_content\_chars\_max : int | None = 4000_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/wikipedia.html#WikipediaLoader)\#     

Load from Wikipedia.

The hard limit on the length of the query is 300 for now.

Each wiki page represents one Document.

Initializes a new instance of the WikipediaLoader class.

Parameters:     

  * **query** \(_str_\) – The query string to search on Wikipedia.

  * **lang** \(_str_ _,__optional_\) – The language code for the Wikipedia language edition. Defaults to “en”.

  * **load\_max\_docs** \(_int_ _,__optional_\) – The maximum number of documents to load. Defaults to 100.

  * **load\_all\_available\_meta** \(_bool_ _,__optional_\) – Indicates whether to load all available metadata for each document. Defaults to False.

  * **doc\_content\_chars\_max** \(_int_ _,__optional_\) – The maximum number of characters for the document content. Defaults to 4000.

Methods

`__init__`\(query\[, lang, load\_max\_docs, ...\]\) | Initializes a new instance of the WikipediaLoader class.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Loads the query result from Wikipedia into a list of Documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _query : str_,     _lang : str = 'en'_,     _load\_max\_docs : int | None = 25_,     _load\_all\_available\_meta : bool | None = False_,     _doc\_content\_chars\_max : int | None = 4000_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/wikipedia.html#WikipediaLoader.__init__)\#     

Initializes a new instance of the WikipediaLoader class.

Parameters:     

  * **query** \(_str_\) – The query string to search on Wikipedia.

  * **lang** \(_str_ _,__optional_\) – The language code for the Wikipedia language edition. Defaults to “en”.

  * **load\_max\_docs** \(_int_ _,__optional_\) – The maximum number of documents to load. Defaults to 100.

  * **load\_all\_available\_meta** \(_bool_ _,__optional_\) – Indicates whether to load all available metadata for each document. Defaults to False.

  * **doc\_content\_chars\_max** \(_int_ _,__optional_\) – The maximum number of characters for the document content. Defaults to 4000.

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/wikipedia.html#WikipediaLoader.lazy_load)\#     

Loads the query result from Wikipedia into a list of Documents.

Returns:     

A list of Document objects representing the loaded     

Wikipedia pages.

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

Examples using WikipediaLoader

  * [Diffbot](https://python.langchain.com/docs/integrations/graphs/diffbot/)

  * [Wikipedia](https://python.langchain.com/docs/integrations/document_loaders/wikipedia/)

__On this page