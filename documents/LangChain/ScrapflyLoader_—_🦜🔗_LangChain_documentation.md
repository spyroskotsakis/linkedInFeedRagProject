# ScrapflyLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.scrapfly.ScrapflyLoader.html
**Word Count:** 194
**Links Count:** 419
**Scraped:** 2025-07-21 08:18:47
**Status:** completed

---

# ScrapflyLoader\#

_class _langchain\_community.document\_loaders.scrapfly.ScrapflyLoader\(

    _urls : List\[str\]_,     _\*_ ,     _api\_key : str | None = None_,     _scrape\_format : Literal\['markdown', 'text'\] = 'markdown'_,     _scrape\_config : dict | None = None_,     _continue\_on\_failure : bool = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/scrapfly.html#ScrapflyLoader)\#     

Turn a url to llm accessible markdown with Scrapfly.io.

For further details, visit: <https://scrapfly.io/docs/sdk/python>

Initialize client.

Parameters:     

  * **urls** \(_List_ _\[__str_ _\]_\) – List of urls to scrape.

  * **api\_key** \(_str_ _|__None_\) – The Scrapfly API key. If not specified must have env var SCRAPFLY\_API\_KEY set.

  * **scrape\_format** \(_Literal_ _\[__'markdown'__,__'text'__\]_\) – Scrape result format, one or “markdown” or “text”.

  * **scrape\_config** \(_dict_ _|__None_\) – Dictionary of ScrapFly scrape config object.

  * **continue\_on\_failure** \(_bool_\) – Whether to continue if scraping a url fails.

Methods

`__init__`\(urls, \*\[, api\_key, scrape\_format, ...\]\) | Initialize client.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _urls : List\[str\]_,     _\*_ ,     _api\_key : str | None = None_,     _scrape\_format : Literal\['markdown', 'text'\] = 'markdown'_,     _scrape\_config : dict | None = None_,     _continue\_on\_failure : bool = True_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/scrapfly.html#ScrapflyLoader.__init__)\#     

Initialize client.

Parameters:     

  * **urls** \(_List_ _\[__str_ _\]_\) – List of urls to scrape.

  * **api\_key** \(_str_ _|__None_\) – The Scrapfly API key. If not specified must have env var SCRAPFLY\_API\_KEY set.

  * **scrape\_format** \(_Literal_ _\[__'markdown'__,__'text'__\]_\) – Scrape result format, one or “markdown” or “text”.

  * **scrape\_config** \(_dict_ _|__None_\) – Dictionary of ScrapFly scrape config object.

  * **continue\_on\_failure** \(_bool_\) – Whether to continue if scraping a url fails.

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

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/scrapfly.html#ScrapflyLoader.lazy_load)\#     

A lazy loader for Documents.

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

Examples using ScrapflyLoader

  * [\# ScrapFly](https://python.langchain.com/docs/integrations/document_loaders/scrapfly/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)