# DocusaurusLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.docusaurus.DocusaurusLoader.html
**Word Count:** 341
**Links Count:** 433
**Scraped:** 2025-07-21 08:20:13
**Status:** completed

---

# DocusaurusLoader\#

_class _langchain\_community.document\_loaders.docusaurus.DocusaurusLoader\(

    _url : str_,     _custom\_html\_tags : List\[str\] | None = None_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/docusaurus.html#DocusaurusLoader)\#     

Load from Docusaurus Documentation.

It leverages the SitemapLoader to loop through the generated pages of a Docusaurus Documentation website and extracts the content by looking for specific HTML tags. By default, the parser searches for the main content of the Docusaurus page, which is normally the <article>. You can also define your own custom HTML tags by providing them as a list, for example: \[“div”, “.main”, “a”\].

Initialize DocusaurusLoader

Parameters:     

  * **url** \(_str_\) – The base URL of the Docusaurus website.

  * **custom\_html\_tags** \(_List_ _\[__str_ _\]__|__None_\) – Optional custom html tags to extract content from pages.

  * **kwargs** \(_Any_\) – Additional args to extend the underlying SitemapLoader, for example: filter\_urls, blocksize, meta\_function, is\_local, continue\_on\_failure

Attributes

`web_path` |    ---|---      Methods

`__init__`\(url\[, custom\_html\_tags\]\) | Initialize DocusaurusLoader   ---|---   `alazy_load`\(\) | Async lazy load text from the url\(s\) in web\_path.   `aload`\(\) |    `ascrape_all`\(urls\[, parser\]\) | Async fetch all urls, then return soups for all results.   `fetch_all`\(urls\) | Fetch all urls concurrently with rate limiting.   `lazy_load`\(\) | Load sitemap.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.   `parse_sitemap`\(soup, \*\[, depth\]\) | Parse sitemap xml and load into a list of dicts.   `scrape`\(\[parser\]\) | Scrape data from webpage and return it in BeautifulSoup format.   `scrape_all`\(urls\[, parser\]\) | Fetch all urls, then return soups for all results.      \_\_init\_\_\(

    _url : str_,     _custom\_html\_tags : List\[str\] | None = None_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/docusaurus.html#DocusaurusLoader.__init__)\#     

Initialize DocusaurusLoader

Parameters:     

  * **url** \(_str_\) – The base URL of the Docusaurus website.

  * **custom\_html\_tags** \(_List_ _\[__str_ _\]__|__None_\) – Optional custom html tags to extract content from pages.

  * **kwargs** \(_Any_\) – Additional args to extend the underlying SitemapLoader, for example: filter\_urls, blocksize, meta\_function, is\_local, continue\_on\_failure

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Async lazy load text from the url\(s\) in web\_path.

Return type:     

_AsyncIterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

aload\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Deprecated since version 0.3.14: See API reference for updated usage: <https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.web_base.WebBaseLoader.html> It will not be removed until langchain-community==1.0.

Load text from the urls in web\_path async into Documents.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _ascrape\_all\(

    _urls : List\[str\]_,     _parser : str | None = None_, \) → List\[Any\]\#     

Async fetch all urls, then return soups for all results.

Parameters:     

  * **urls** \(_List_ _\[__str_ _\]_\)

  * **parser** \(_str_ _|__None_\)

Return type:     

_List_\[_Any_\]

_async _fetch\_all\(

    _urls : List\[str\]_, \) → Any\#     

Fetch all urls concurrently with rate limiting.

Parameters:     

**urls** \(_List_ _\[__str_ _\]_\)

Return type:     

_Any_

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load sitemap.

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

parse\_sitemap\(

    _soup : Any_,     _\*_ ,     _depth : int = 0_, \) → List\[dict\]\#     

Parse sitemap xml and load into a list of dicts.

Parameters:     

  * **soup** \(_Any_\) – BeautifulSoup object.

  * **depth** \(_int_\) – current depth of the sitemap. Default: 0

Returns:     

List of dicts.

Return type:     

_List_\[dict\]

scrape\(

    _parser : str | None = None_, \) → Any\#     

Scrape data from webpage and return it in BeautifulSoup format.

Parameters:     

**parser** \(_str_ _|__None_\)

Return type:     

_Any_

scrape\_all\(

    _urls : List\[str\]_,     _parser : str | None = None_, \) → List\[Any\]\#     

Fetch all urls, then return soups for all results.

Parameters:     

  * **urls** \(_List_ _\[__str_ _\]_\)

  * **parser** \(_str_ _|__None_\)

Return type:     

_List_\[_Any_\]

Examples using DocusaurusLoader

  * [Docusaurus](https://python.langchain.com/docs/integrations/document_loaders/docusaurus/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)