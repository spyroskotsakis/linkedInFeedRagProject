# AsyncChromiumLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.chromium.AsyncChromiumLoader.html
**Word Count:** 320
**Links Count:** 424
**Scraped:** 2025-07-21 08:03:51
**Status:** completed

---

# AsyncChromiumLoader\#

_class _langchain\_community.document\_loaders.chromium.AsyncChromiumLoader\(

    _urls : List\[str\]_,     _\*_ ,     _headless : bool = True_,     _user\_agent : str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/chromium.html#AsyncChromiumLoader)\#     

Scrape HTML pages from URLs using a headless instance of the Chromium.

Initialize the loader with a list of URL paths.

Parameters:     

  * **urls** \(_List_ _\[__str_ _\]_\) – A list of URLs to scrape content from.

  * **headless** \(_bool_\) – Whether to run browser in headless mode.

  * **user\_agent** \(_str_ _|__None_\) – The user agent to use for the browser

Raises:     

**ImportError** – If the required ‘playwright’ package is not installed.

Methods

`__init__`\(urls, \*\[, headless, user\_agent\]\) | Initialize the loader with a list of URL paths.   ---|---   `alazy_load`\(\) | Asynchronously load text content from the provided URLs.   `aload`\(\) | Load data into Document objects.   `ascrape_playwright`\(url\) | Asynchronously scrape the content of a given URL using Playwright's async API.   `lazy_load`\(\) | Lazily load text content from the provided URLs.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _urls : List\[str\]_,     _\*_ ,     _headless : bool = True_,     _user\_agent : str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/chromium.html#AsyncChromiumLoader.__init__)\#     

Initialize the loader with a list of URL paths.

Parameters:     

  * **urls** \(_List_ _\[__str_ _\]_\) – A list of URLs to scrape content from.

  * **headless** \(_bool_\) – Whether to run browser in headless mode.

  * **user\_agent** \(_str_ _|__None_\) – The user agent to use for the browser

Raises:     

**ImportError** – If the required ‘playwright’ package is not installed.

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/chromium.html#AsyncChromiumLoader.alazy_load)\#     

Asynchronously load text content from the provided URLs.

This method leverages asyncio to initiate the scraping of all provided URLs simultaneously. It improves performance by utilizing concurrent asynchronous requests. Each Document is yielded as soon as its content is available, encapsulating the scraped content.

Yields:     

_Document_ – A Document object containing the scraped content, along with its source URL as metadata.

Return type:     

_AsyncIterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _ascrape\_playwright\(_url : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/chromium.html#AsyncChromiumLoader.ascrape_playwright)\#     

Asynchronously scrape the content of a given URL using Playwright’s async API.

Parameters:     

**url** \(_str_\) – The URL to scrape.

Returns:     

The scraped HTML content or an error message if an exception occurs.

Return type:     

str

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/chromium.html#AsyncChromiumLoader.lazy_load)\#     

Lazily load text content from the provided URLs.

This method yields Documents one at a time as they’re scraped, instead of waiting to scrape all URLs before returning.

Yields:     

_Document_ – The scraped content encapsulated within a Document object.

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

Examples using AsyncChromiumLoader

  * [Async Chromium](https://python.langchain.com/docs/integrations/document_loaders/async_chromium/)

  * [Beautiful Soup](https://python.langchain.com/docs/integrations/document_transformers/beautiful_soup/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)