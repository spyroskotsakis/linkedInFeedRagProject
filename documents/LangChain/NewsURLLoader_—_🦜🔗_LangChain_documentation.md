# NewsURLLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.news.NewsURLLoader.html
**Word Count:** 188
**Links Count:** 420
**Scraped:** 2025-07-21 08:15:47
**Status:** completed

---

# NewsURLLoader\#

_class _langchain\_community.document\_loaders.news.NewsURLLoader\(

    _urls : List\[str\]_,     _text\_mode : bool = True_,     _nlp : bool = False_,     _continue\_on\_failure : bool = True_,     _show\_progress\_bar : bool = False_,     _\*\* newspaper\_kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/news.html#NewsURLLoader)\#     

Load news articles from URLs using Unstructured.

Parameters:     

  * **urls** \(_List_ _\[__str_ _\]_\) – URLs to load. Each is loaded into its own document.

  * **text\_mode** \(_bool_\) – If True, extract text from URL and use that for page content. Otherwise, extract raw HTML.

  * **nlp** \(_bool_\) – If True, perform NLP on the extracted contents, like providing a summary and extracting keywords.

  * **continue\_on\_failure** \(_bool_\) – If True, continue loading documents even if loading fails for a particular URL.

  * **show\_progress\_bar** \(_bool_\) – If True, use tqdm to show a loading progress bar. Requires tqdm to be installed, `pip install tqdm`.

  * **\*\*newspaper\_kwargs** \(_Any_\) – Any additional named arguments to pass to newspaper.Article\(\).

Example               from langchain_community.document_loaders import NewsURLLoader          loader = NewsURLLoader(         urls=["<url-1>", "<url-2>"],     )     docs = loader.load()     

Newspaper reference:     

<https://newspaper.readthedocs.io/en/latest/>

Initialize with file path.

Methods

`__init__`\(urls\[, text\_mode, nlp, ...\]\) | Initialize with file path.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _urls : List\[str\]_,     _text\_mode : bool = True_,     _nlp : bool = False_,     _continue\_on\_failure : bool = True_,     _show\_progress\_bar : bool = False_,     _\*\* newspaper\_kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/news.html#NewsURLLoader.__init__)\#     

Initialize with file path.

Parameters:     

  * **urls** \(_List_ _\[__str_ _\]_\)

  * **text\_mode** \(_bool_\)

  * **nlp** \(_bool_\)

  * **continue\_on\_failure** \(_bool_\)

  * **show\_progress\_bar** \(_bool_\)

  * **newspaper\_kwargs** \(_Any_\)

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

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/news.html#NewsURLLoader.lazy_load)\#     

A lazy loader for Documents.

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/news.html#NewsURLLoader.load)\#     

Load data into Document objects.

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

Examples using NewsURLLoader

  * [News URL](https://python.langchain.com/docs/integrations/document_loaders/news/)

__On this page