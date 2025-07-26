# SitemapLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.sitemap.SitemapLoader.html
**Word Count:** 880
**Links Count:** 436
**Scraped:** 2025-07-21 08:21:12
**Status:** completed

---

# SitemapLoader\#

_class _langchain\_community.document\_loaders.sitemap.SitemapLoader\(

    _web\_path : str_,     _filter\_urls : List\[str\] | None = None_,     _parsing\_function : Callable | None = None_,     _blocksize : int | None = None_,     _blocknum : int = 0_,     _meta\_function : Callable | None = None_,     _is\_local : bool = False_,     _continue\_on\_failure : bool = False_,     _restrict\_to\_same\_domain : bool = True_,     _max\_depth : int = 10_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/sitemap.html#SitemapLoader)\#     

Load a sitemap and its URLs.

**Security Note** : This loader can be used to load all URLs specified in a sitemap.     

If a malicious actor gets access to the sitemap, they could force the server to load URLs from other domains by modifying the sitemap. This could lead to server-side request forgery \(SSRF\) attacks; e.g., with the attacker forcing the server to load URLs from internal service endpoints that are not publicly accessible. While the attacker may not immediately gain access to this data, this data could leak into downstream systems \(e.g., data loader is used to load data for indexing\).

This loader is a crawler and web crawlers should generally NOT be deployed with network access to any internal servers.

Control access to who can submit crawling requests and what network access the crawler has.

By default, the loader will only load URLs from the same domain as the sitemap if the site map is not a local file. This can be disabled by setting restrict\_to\_same\_domain to False \(not recommended\).

If the site map is a local file, no such risk mitigation is applied by default.

Use the filter URLs argument to limit which URLs can be loaded.

See <https://python.langchain.com/docs/security>

Initialize with webpage path and optional filter URLs.

Parameters:     

  * **web\_path** \(_str_\) – url of the sitemap. can also be a local path

  * **filter\_urls** \(_List_ _\[__str_ _\]__|__None_\) – a list of regexes. If specified, only URLS that match one of the filter URLs will be loaded. _WARNING_ The filter URLs are interpreted as regular expressions. Remember to escape special characters if you do not want them to be interpreted as regular expression syntax. For example, . appears frequently in URLs and should be escaped if you want to match a literal . rather than any character. restrict\_to\_same\_domain takes precedence over filter\_urls when restrict\_to\_same\_domain is True and the sitemap is not a local file.

  * **parsing\_function** \(_Callable_ _|__None_\) – Function to parse bs4.Soup output

  * **blocksize** \(_int_ _|__None_\) – number of sitemap locations per block

  * **blocknum** \(_int_\) – the number of the block that should be loaded - zero indexed. Default: 0

  * **meta\_function** \(_Callable_ _|__None_\) – Function to parse bs4.Soup output for metadata remember when setting this method to also copy metadata\[“loc”\] to metadata\[“source”\] if you are using this field

  * **is\_local** \(_bool_\) – whether the sitemap is a local file. Default: False

  * **continue\_on\_failure** \(_bool_\) – whether to continue loading the sitemap if an error occurs loading a url, emitting a warning instead of raising an exception. Setting this to True makes the loader more robust, but also may result in missing data. Default: False

  * **restrict\_to\_same\_domain** \(_bool_\) – whether to restrict loading to URLs to the same domain as the sitemap. Attention: This is only applied if the sitemap is not a local file\!

  * **max\_depth** \(_int_\) – maximum depth to follow sitemap links. Default: 10

  * **kwargs** \(_Any_\)

Attributes

`web_path` |    ---|---      Methods

`__init__`\(web\_path\[, filter\_urls, ...\]\) | Initialize with webpage path and optional filter URLs.   ---|---   `alazy_load`\(\) | Async lazy load text from the url\(s\) in web\_path.   `aload`\(\) |    `ascrape_all`\(urls\[, parser\]\) | Async fetch all urls, then return soups for all results.   `fetch_all`\(urls\) | Fetch all urls concurrently with rate limiting.   `lazy_load`\(\) | Load sitemap.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.   `parse_sitemap`\(soup, \*\[, depth\]\) | Parse sitemap xml and load into a list of dicts.   `scrape`\(\[parser\]\) | Scrape data from webpage and return it in BeautifulSoup format.   `scrape_all`\(urls\[, parser\]\) | Fetch all urls, then return soups for all results.      \_\_init\_\_\(

    _web\_path : str_,     _filter\_urls : List\[str\] | None = None_,     _parsing\_function : Callable | None = None_,     _blocksize : int | None = None_,     _blocknum : int = 0_,     _meta\_function : Callable | None = None_,     _is\_local : bool = False_,     _continue\_on\_failure : bool = False_,     _restrict\_to\_same\_domain : bool = True_,     _max\_depth : int = 10_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/sitemap.html#SitemapLoader.__init__)\#     

Initialize with webpage path and optional filter URLs.

Parameters:     

  * **web\_path** \(_str_\) – url of the sitemap. can also be a local path

  * **filter\_urls** \(_List_ _\[__str_ _\]__|__None_\) – a list of regexes. If specified, only URLS that match one of the filter URLs will be loaded. _WARNING_ The filter URLs are interpreted as regular expressions. Remember to escape special characters if you do not want them to be interpreted as regular expression syntax. For example, . appears frequently in URLs and should be escaped if you want to match a literal . rather than any character. restrict\_to\_same\_domain takes precedence over filter\_urls when restrict\_to\_same\_domain is True and the sitemap is not a local file.

  * **parsing\_function** \(_Callable_ _|__None_\) – Function to parse bs4.Soup output

  * **blocksize** \(_int_ _|__None_\) – number of sitemap locations per block

  * **blocknum** \(_int_\) – the number of the block that should be loaded - zero indexed. Default: 0

  * **meta\_function** \(_Callable_ _|__None_\) – Function to parse bs4.Soup output for metadata remember when setting this method to also copy metadata\[“loc”\] to metadata\[“source”\] if you are using this field

  * **is\_local** \(_bool_\) – whether the sitemap is a local file. Default: False

  * **continue\_on\_failure** \(_bool_\) – whether to continue loading the sitemap if an error occurs loading a url, emitting a warning instead of raising an exception. Setting this to True makes the loader more robust, but also may result in missing data. Default: False

  * **restrict\_to\_same\_domain** \(_bool_\) – whether to restrict loading to URLs to the same domain as the sitemap. Attention: This is only applied if the sitemap is not a local file\!

  * **max\_depth** \(_int_\) – maximum depth to follow sitemap links. Default: 10

  * **kwargs** \(_Any_\)

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

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/sitemap.html#SitemapLoader.lazy_load)\#     

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

    _soup : Any_,     _\*_ ,     _depth : int = 0_, \) → List\[dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/sitemap.html#SitemapLoader.parse_sitemap)\#     

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

Examples using SitemapLoader

  * [Sitemap](https://python.langchain.com/docs/integrations/document_loaders/sitemap/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)