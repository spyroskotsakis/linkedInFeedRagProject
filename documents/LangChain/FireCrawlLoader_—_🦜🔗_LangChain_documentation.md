# FireCrawlLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.firecrawl.FireCrawlLoader.html
**Word Count:** 364
**Links Count:** 430
**Scraped:** 2025-07-21 08:05:36
**Status:** completed

---

# FireCrawlLoader\#

_class _langchain\_community.document\_loaders.firecrawl.FireCrawlLoader\(

    _url : str_,     _\*_ ,     _api\_key : str | None = None_,     _api\_url : str | None = None_,     _mode : Literal\['crawl', 'scrape', 'map', 'extract', 'search'\] = 'crawl'_,     _params : dict | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/firecrawl.html#FireCrawlLoader)\#     

FireCrawlLoader document loader integration

Setup:     

Install `firecrawl-py`,\`\`langchain\_community\`\` and set environment variable `FIRECRAWL_API_KEY`.               pip install -U firecrawl-py langchain_community     export FIRECRAWL_API_KEY="your-api-key"     

Instantiate:                    from langchain_community.document_loaders import FireCrawlLoader          loader = FireCrawlLoader(         url = "https://firecrawl.dev",         mode = "crawl"         # other params = ...     )     

Lazy load:                    docs = []     docs_lazy = loader.lazy_load()          # async variant:     # docs_lazy = await loader.alazy_load()          for doc in docs_lazy:         docs.append(doc)     print(docs[0].page_content[:100])     print(docs[0].metadata)                    Introducing [Smart Crawl!](https://www.firecrawl.dev/smart-crawl)      Join the waitlist to turn any web     {'ogUrl': 'https://www.firecrawl.dev/', 'title': 'Home - Firecrawl', 'robots': 'follow, index', 'ogImage': 'https://www.firecrawl.dev/og.png?123', 'ogTitle': 'Firecrawl', 'sitemap': {'lastmod': '2024-08-12T00:28:16.681Z', 'changefreq': 'weekly'}, 'keywords': 'Firecrawl,Markdown,Data,Mendable,Langchain', 'sourceURL': 'https://www.firecrawl.dev/', 'ogSiteName': 'Firecrawl', 'description': 'Firecrawl crawls and converts any website into clean markdown.', 'ogDescription': 'Turn any website into LLM-ready data.', 'pageStatusCode': 200, 'ogLocaleAlternate': []}     

Async load:                    docs = await loader.aload()     print(docs[0].page_content[:100])     print(docs[0].metadata)                    Introducing [Smart Crawl!](https://www.firecrawl.dev/smart-crawl)      Join the waitlist to turn any web     {'ogUrl': 'https://www.firecrawl.dev/', 'title': 'Home - Firecrawl', 'robots': 'follow, index', 'ogImage': 'https://www.firecrawl.dev/og.png?123', 'ogTitle': 'Firecrawl', 'sitemap': {'lastmod': '2024-08-12T00:28:16.681Z', 'changefreq': 'weekly'}, 'keywords': 'Firecrawl,Markdown,Data,Mendable,Langchain', 'sourceURL': 'https://www.firecrawl.dev/', 'ogSiteName': 'Firecrawl', 'description': 'Firecrawl crawls and converts any website into clean markdown.', 'ogDescription': 'Turn any website into LLM-ready data.', 'pageStatusCode': 200, 'ogLocaleAlternate': []}     

Initialize with API key and url.

Parameters:     

  * **url** \(_str_\) – The url to be crawled.

  * **api\_key** \(_str_ _|__None_\) – The Firecrawl API key. If not specified will be read from env var FIRECRAWL\_API\_KEY. Get an API key

  * **api\_url** \(_str_ _|__None_\) – The Firecrawl API URL. If not specified will be read from env var FIRECRAWL\_API\_URL or defaults to <https://api.firecrawl.dev>.

  * **mode** \(_Literal_ _\[__'crawl'__,__'scrape'__,__'map'__,__'extract'__,__'search'__\]_\) – The mode to run the loader in. Default is “crawl”. Options include “scrape” \(single url\), “crawl” \(all accessible sub pages\), “map” \(returns list of links that are semantically related\). “extract” \(extracts structured data from a page\). “search” \(search for data across the web\).

  * **params** \(_dict_ _|__None_\) – The parameters to pass to the Firecrawl API. Examples include crawlerOptions. For more details, visit: [mendableai/firecrawl-py](https://github.com/mendableai/firecrawl-py)

Methods

`__init__`\(url, \*\[, api\_key, api\_url, mode, ...\]\) | Initialize with API key and url.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `legacy_crawler_options_adapter`\(params\) |    `legacy_scrape_options_adapter`\(params\) |    `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _url : str_,     _\*_ ,     _api\_key : str | None = None_,     _api\_url : str | None = None_,     _mode : Literal\['crawl', 'scrape', 'map', 'extract', 'search'\] = 'crawl'_,     _params : dict | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/firecrawl.html#FireCrawlLoader.__init__)\#     

Initialize with API key and url.

Parameters:     

  * **url** \(_str_\) – The url to be crawled.

  * **api\_key** \(_str_ _|__None_\) – The Firecrawl API key. If not specified will be read from env var FIRECRAWL\_API\_KEY. Get an API key

  * **api\_url** \(_str_ _|__None_\) – The Firecrawl API URL. If not specified will be read from env var FIRECRAWL\_API\_URL or defaults to <https://api.firecrawl.dev>.

  * **mode** \(_Literal_ _\[__'crawl'__,__'scrape'__,__'map'__,__'extract'__,__'search'__\]_\) – The mode to run the loader in. Default is “crawl”. Options include “scrape” \(single url\), “crawl” \(all accessible sub pages\), “map” \(returns list of links that are semantically related\). “extract” \(extracts structured data from a page\). “search” \(search for data across the web\).

  * **params** \(_dict_ _|__None_\) – The parameters to pass to the Firecrawl API. Examples include crawlerOptions. For more details, visit: [mendableai/firecrawl-py](https://github.com/mendableai/firecrawl-py)

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/firecrawl.html#FireCrawlLoader.lazy_load)\#     

A lazy loader for Documents.

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

legacy\_crawler\_options\_adapter\(

    _params : dict_, \) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/firecrawl.html#FireCrawlLoader.legacy_crawler_options_adapter)\#     

Parameters:     

**params** \(_dict_\)

Return type:     

dict

legacy\_scrape\_options\_adapter\(

    _params : dict_, \) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/firecrawl.html#FireCrawlLoader.legacy_scrape_options_adapter)\#     

Parameters:     

**params** \(_dict_\)

Return type:     

dict

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

Examples using FireCrawlLoader

  * [FireCrawl](https://python.langchain.com/docs/integrations/document_loaders/firecrawl/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)