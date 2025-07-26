# SpiderLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.spider.SpiderLoader.html
**Word Count:** 224
**Links Count:** 419
**Scraped:** 2025-07-21 08:10:45
**Status:** completed

---

# SpiderLoader\#

_class _langchain\_community.document\_loaders.spider.SpiderLoader\(

    _url : str_,     _\*_ ,     _api\_key : str | None = None_,     _mode : Literal\['scrape', 'crawl'\] = 'scrape'_,     _params : dict | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/spider.html#SpiderLoader)\#     

Load web pages as Documents using Spider AI.

Must have the Python package spider-client installed and a Spider API key. See <https://spider.cloud> for more.

Initialize with API key and URL.

Parameters:     

  * **url** \(_str_\) – The URL to be processed.

  * **api\_key** \(_str_ _|__None_\) – The Spider API key. If not specified, will be read from env

  * **SPIDER\_API\_KEY.** \(_var_\)

  * **mode** \(_Literal_ _\[__'scrape'__,__'crawl'__\]_\) – The mode to run the loader in. Default is “scrape”. Options include “scrape” \(single page\) and “crawl” \(with deeper crawling following subpages\).

  * **params** \(_dict_ _|__None_\) – Additional parameters for the Spider API.

Methods

`__init__`\(url, \*\[, api\_key, mode, params\]\) | Initialize with API key and URL.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Load documents based on the specified mode.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _url : str_,     _\*_ ,     _api\_key : str | None = None_,     _mode : Literal\['scrape', 'crawl'\] = 'scrape'_,     _params : dict | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/spider.html#SpiderLoader.__init__)\#     

Initialize with API key and URL.

Parameters:     

  * **url** \(_str_\) – The URL to be processed.

  * **api\_key** \(_str_ _|__None_\) – The Spider API key. If not specified, will be read from env

  * **SPIDER\_API\_KEY.** \(_var_\)

  * **mode** \(_Literal_ _\[__'scrape'__,__'crawl'__\]_\) – The mode to run the loader in. Default is “scrape”. Options include “scrape” \(single page\) and “crawl” \(with deeper crawling following subpages\).

  * **params** \(_dict_ _|__None_\) – Additional parameters for the Spider API.

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/spider.html#SpiderLoader.lazy_load)\#     

Load documents based on the specified mode.

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

Examples using SpiderLoader

  * [Spider](https://python.langchain.com/docs/integrations/document_loaders/spider/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)