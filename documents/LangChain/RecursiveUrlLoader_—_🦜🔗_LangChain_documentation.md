# RecursiveUrlLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.recursive_url_loader.RecursiveUrlLoader.html
**Word Count:** 1283
**Links Count:** 425
**Scraped:** 2025-07-21 08:20:13
**Status:** completed

---

# RecursiveUrlLoader\#

_class _langchain\_community.document\_loaders.recursive\_url\_loader.RecursiveUrlLoader\(

    _url : str_,     _max\_depth : int | None = 2_,     _use\_async : bool | None = None_,     _extractor : Callable\[\[str\], str\] | None = None_,     _metadata\_extractor : Callable\[\[str, str\], dict\] | Callable\[\[str, str, Response | ClientResponse\], dict\] | None = None_,     _exclude\_dirs : Sequence\[str\] | None = \(\)_,     _timeout : int | None = 10_,     _prevent\_outside : bool = True_,     _link\_regex : str | Pattern | None = None_,     _headers : dict | None = None_,     _check\_response\_status : bool = False_,     _continue\_on\_failure : bool = True_,     _\*_ ,     _base\_url : str | None = None_,     _autoset\_encoding : bool = True_,     _encoding : str | None = None_,     _proxies : dict | None = None_,     _ssl : bool = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/recursive_url_loader.html#RecursiveUrlLoader)\#     

Recursively load all child links from a root URL.

**Security Note** :     

This loader is a crawler that will start crawling at a given URL and then expand to crawl child links recursively.

Web crawlers should generally NOT be deployed with network access to any internal servers.

Control access to who can submit crawling requests and what network access the crawler has.

While crawling, the crawler may encounter malicious URLs that would lead to a server-side request forgery \(SSRF\) attack.

To mitigate risks, the crawler by default will only load URLs from the same domain as the start URL \(controlled via prevent\_outside named argument\).

This will mitigate the risk of SSRF attacks, but will not eliminate it.

For example, if crawling a host which hosts several sites:

<https://some_host/alice_site/> <https://some_host/bob_site/>

A malicious URL on Alice’s site could cause the crawler to make a malicious GET request to an endpoint on Bob’s site. Both sites are hosted on the same host, so such a request would not be prevented by default.

See <https://python.langchain.com/docs/security/>

Setup:

> This class has no required additional dependencies. You can optionally install `beautifulsoup4` for richer default metadata extraction: >      >      >     pip install -U beautifulsoup4 >     

Instantiate:                    from langchain_community.document_loaders import RecursiveUrlLoader          loader = RecursiveUrlLoader(         "https://docs.python.org/3.9/",         # max_depth=2,         # use_async=False,         # extractor=None,         # metadata_extractor=None,         # exclude_dirs=(),         # timeout=10,         # check_response_status=True,         # continue_on_failure=True,         # prevent_outside=True,         # base_url=None,         # ...     )     

Lazy load:                    docs = []     docs_lazy = loader.lazy_load()          # async variant:     # docs_lazy = await loader.alazy_load()          for doc in docs_lazy:         docs.append(doc)     print(docs[0].page_content[:100])     print(docs[0].metadata)                    <!DOCTYPE html>          <html xmlns="http://www.w3.org/1999/xhtml">     <head>         <meta charset="utf-8" /><     {'source': 'https://docs.python.org/3.9/', 'content_type': 'text/html', 'title': '3.9.19 Documentation', 'language': None}     

Async load:                    docs = await loader.aload()     print(docs[0].page_content[:100])     print(docs[0].metadata)                    <!DOCTYPE html>          <html xmlns="http://www.w3.org/1999/xhtml">     <head>         <meta charset="utf-8" /><     {'source': 'https://docs.python.org/3.9/', 'content_type': 'text/html', 'title': '3.9.19 Documentation', 'language': None}     

Content parsing / extraction:     

By default the loader sets the raw HTML from each link as the Document page content. To parse this HTML into a more human/LLM-friendly format you can pass in a custom `extractor` method:               # This example uses `beautifulsoup4` and `lxml`     import re     from bs4 import BeautifulSoup          def bs4_extractor(html: str) -> str:         soup = BeautifulSoup(html, "lxml")         return re.sub(r"\n\n+", "\n\n", soup.text).strip()          loader = RecursiveUrlLoader(         "https://docs.python.org/3.9/",         extractor=bs4_extractor,     )     print(loader.load()[0].page_content[:200])                    3.9.19 Documentation          Download     Download these documents     Docs by version          Python 3.13 (in development)     Python 3.12 (stable)     Python 3.11 (security-fixes)     Python 3.10 (security-fixes)     Python 3.9 (securit     

Metadata extraction:     

Similarly to content extraction, you can specify a metadata extraction function to customize how Document metadata is extracted from the HTTP response.               import aiohttp     import requests     from typing import Union          def simple_metadata_extractor(         raw_html: str, url: str, response: Union[requests.Response, aiohttp.ClientResponse]     ) -> dict:         content_type = getattr(response, "headers").get("Content-Type", "")         return {"source": url, "content_type": content_type}          loader = RecursiveUrlLoader(         "https://docs.python.org/3.9/",         metadata_extractor=simple_metadata_extractor,     )     loader.load()[0].metadata                    {'source': 'https://docs.python.org/3.9/', 'content_type': 'text/html'}     

Filtering URLs:     

You may not always want to pull every URL from a website. There are four parameters that allow us to control what URLs we pull recursively. First, we can set the `prevent_outside` parameter to prevent URLs outside of the `base_url` from being pulled. Note that the `base_url` does not need to be the same as the URL we pass in, as shown below. We can also use `link_regex` and `exclude_dirs` to be more specific with the URLs that we select. In this example, we only pull websites from the python docs, which contain the string “index” somewhere and are not located in the FAQ section of the website.               loader = RecursiveUrlLoader(         "https://docs.python.org/3.9/",         prevent_outside=True,         base_url="https://docs.python.org",         link_regex=r'<a\s+(?:[^>]*?\s+)?href="([^"]*(?=index)[^"]*)"',         exclude_dirs=['https://docs.python.org/3.9/faq']     )     docs = loader.load()                    ['https://docs.python.org/3.9/',     'https://docs.python.org/3.9/py-modindex.html',     'https://docs.python.org/3.9/genindex.html',     'https://docs.python.org/3.9/tutorial/index.html',     'https://docs.python.org/3.9/using/index.html',     'https://docs.python.org/3.9/extending/index.html',     'https://docs.python.org/3.9/installing/index.html',     'https://docs.python.org/3.9/library/index.html',     'https://docs.python.org/3.9/c-api/index.html',     'https://docs.python.org/3.9/howto/index.html',     'https://docs.python.org/3.9/distributing/index.html',     'https://docs.python.org/3.9/reference/index.html',     'https://docs.python.org/3.9/whatsnew/index.html']     

Initialize with URL to crawl and any subdirectories to exclude.

Parameters:     

  * **url** \(_str_\) – The URL to crawl.

  * **max\_depth** \(_Optional_ _\[__int_ _\]_\) – The max depth of the recursive loading.

  * **use\_async** \(_Optional_ _\[__bool_ _\]_\) – Whether to use asynchronous loading. If `True`, `lazy_load()` will not be lazy, but it will still work in the expected way, just not lazy.

  * **extractor** \(_Optional_ _\[__Callable_ _\[__\[__str_ _\]__,__str_ _\]__\]_\) – A function to extract document contents from raw HTML. When extract function returns an empty string, the document is ignored. Default returns the raw HTML.

  * **metadata\_extractor** \(_Optional_ _\[__\_MetadataExtractorType_ _\]_\) – 

A function to extract metadata from args: raw HTML, the source url, and the requests.Response/aiohttp.ClientResponse object \(args in that order\).

Default extractor will attempt to use BeautifulSoup4 to extract the title, description and language of the page.

..code-block:: python

> import requests import aiohttp >  > def simple\_metadata\_extractor\( >      >  > raw\_html: str, url: str, response: Union\[requests.Response, aiohttp.ClientResponse\] >  > \) -> dict: >      >  > content\_type = getattr\(response, “headers”\).get\(“Content-Type”, “”\) return \{“source”: url, “content\_type”: content\_type\}

  * **exclude\_dirs** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – A list of subdirectories to exclude.

  * **timeout** \(_Optional_ _\[__int_ _\]_\) – The timeout for the requests, in the unit of seconds. If `None` then connection will not timeout.

  * **prevent\_outside** \(_bool_\) – If `True`, prevent loading from urls which are not children of the root url.

  * **link\_regex** \(_Union_ _\[__str_ _,__re.Pattern_ _,__None_ _\]_\) – Regex for extracting sub-links from the raw html of a web page.

  * **headers** \(_Optional_ _\[__dict_ _\]_\) – Default request headers to use for all requests.

  * **check\_response\_status** \(_bool_\) – If `True`, check HTTP response status and skip URLs with error responses \(`400-599`\).

  * **continue\_on\_failure** \(_bool_\) – If `True`, continue if getting or parsing a link raises an exception. Otherwise, raise the exception.

  * **base\_url** \(_Optional_ _\[__str_ _\]_\) – The base url to check for outside links against.

  * **autoset\_encoding** \(_bool_\) – Whether to automatically set the encoding of the response. If `True`, the encoding of the response will be set to the apparent encoding, unless the `encoding` argument has already been explicitly set.

  * **encoding** \(_Optional_ _\[__str_ _\]_\) – The encoding of the response. If manually set, the encoding will be set to given value, regardless of the `autoset_encoding` argument.

  * **proxies** \(_Optional_ _\[__dict_ _\]_\) – 

A dictionary mapping protocol names to the proxy URLs to be used for requests. This allows the crawler to route its requests through specified proxy servers. If `None`, no proxies will be used and requests will go directly to the target URL.

Example usage:

..code-block:: python

> proxies = \{ >      >  > “http”: “<http://10.10.1.10:3128>”, “https”: “<https://10.10.1.10:1080>”, >  > \}

  * **ssl** \(_bool_\) – 

Whether to verify SSL certificates during requests. By default, SSL certificate verification is enabled \(`ssl=True`\), ensuring secure HTTPS connections. Setting this to `False` disables SSL certificate verification, which can be useful when crawling internal services, development environments, or sites with misconfigured or self-signed certificates.

**Use with caution:** Disabling SSL verification exposes your crawler to man-in-the-middle \(MitM\) attacks, data tampering, and potential interception of sensitive information. This significantly compromises the security and integrity of the communication. It should never be used in production or when handling sensitive data.

Methods

`__init__`\(url\[, max\_depth, use\_async, ...\]\) | Initialize with URL to crawl and any subdirectories to exclude.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Lazy load web pages.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _url : str_,     _max\_depth : int | None = 2_,     _use\_async : bool | None = None_,     _extractor : Callable\[\[str\], str\] | None = None_,     _metadata\_extractor : Callable\[\[str, str\], dict\] | Callable\[\[str, str, Response | ClientResponse\], dict\] | None = None_,     _exclude\_dirs : Sequence\[str\] | None = \(\)_,     _timeout : int | None = 10_,     _prevent\_outside : bool = True_,     _link\_regex : str | Pattern | None = None_,     _headers : dict | None = None_,     _check\_response\_status : bool = False_,     _continue\_on\_failure : bool = True_,     _\*_ ,     _base\_url : str | None = None_,     _autoset\_encoding : bool = True_,     _encoding : str | None = None_,     _proxies : dict | None = None_,     _ssl : bool = True_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/recursive_url_loader.html#RecursiveUrlLoader.__init__)\#     

Initialize with URL to crawl and any subdirectories to exclude.

Parameters:     

  * **url** \(_str_\) – The URL to crawl.

  * **max\_depth** \(_int_ _|__None_\) – The max depth of the recursive loading.

  * **use\_async** \(_bool_ _|__None_\) – Whether to use asynchronous loading. If `True`, `lazy_load()` will not be lazy, but it will still work in the expected way, just not lazy.

  * **extractor** \(_Callable_ _\[__\[__str_ _\]__,__str_ _\]__|__None_\) – A function to extract document contents from raw HTML. When extract function returns an empty string, the document is ignored. Default returns the raw HTML.

  * **metadata\_extractor** \(_Callable_ _\[__\[__str_ _,__str_ _\]__,__dict_ _\]__|__Callable_ _\[__\[__str_ _,__str_ _,__Response_ _|__ClientResponse_ _\]__,__dict_ _\]__|__None_\) – 

A function to extract metadata from args: raw HTML, the source url, and the requests.Response/aiohttp.ClientResponse object \(args in that order\).

Default extractor will attempt to use BeautifulSoup4 to extract the title, description and language of the page.

..code-block:: python

> import requests import aiohttp >  > def simple\_metadata\_extractor\( >      >  > raw\_html: str, url: str, response: Union\[requests.Response, aiohttp.ClientResponse\] >  > \) -> dict: >      >  > content\_type = getattr\(response, “headers”\).get\(“Content-Type”, “”\) return \{“source”: url, “content\_type”: content\_type\}

  * **exclude\_dirs** \(_Sequence_ _\[__str_ _\]__|__None_\) – A list of subdirectories to exclude.

  * **timeout** \(_int_ _|__None_\) – The timeout for the requests, in the unit of seconds. If `None` then connection will not timeout.

  * **prevent\_outside** \(_bool_\) – If `True`, prevent loading from urls which are not children of the root url.

  * **link\_regex** \(_str_ _|__Pattern_ _|__None_\) – Regex for extracting sub-links from the raw html of a web page.

  * **headers** \(_dict_ _|__None_\) – Default request headers to use for all requests.

  * **check\_response\_status** \(_bool_\) – If `True`, check HTTP response status and skip URLs with error responses \(`400-599`\).

  * **continue\_on\_failure** \(_bool_\) – If `True`, continue if getting or parsing a link raises an exception. Otherwise, raise the exception.

  * **base\_url** \(_str_ _|__None_\) – The base url to check for outside links against.

  * **autoset\_encoding** \(_bool_\) – Whether to automatically set the encoding of the response. If `True`, the encoding of the response will be set to the apparent encoding, unless the `encoding` argument has already been explicitly set.

  * **encoding** \(_str_ _|__None_\) – The encoding of the response. If manually set, the encoding will be set to given value, regardless of the `autoset_encoding` argument.

  * **proxies** \(_dict_ _|__None_\) – 

A dictionary mapping protocol names to the proxy URLs to be used for requests. This allows the crawler to route its requests through specified proxy servers. If `None`, no proxies will be used and requests will go directly to the target URL.

Example usage:

..code-block:: python

> proxies = \{ >      >  > “http”: “<http://10.10.1.10:3128>”, “https”: “<https://10.10.1.10:1080>”, >  > \}

  * **ssl** \(_bool_\) – 

Whether to verify SSL certificates during requests. By default, SSL certificate verification is enabled \(`ssl=True`\), ensuring secure HTTPS connections. Setting this to `False` disables SSL certificate verification, which can be useful when crawling internal services, development environments, or sites with misconfigured or self-signed certificates.

**Use with caution:** Disabling SSL verification exposes your crawler to man-in-the-middle \(MitM\) attacks, data tampering, and potential interception of sensitive information. This significantly compromises the security and integrity of the communication. It should never be used in production or when handling sensitive data.

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

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/recursive_url_loader.html#RecursiveUrlLoader.lazy_load)\#     

Lazy load web pages. When use\_async is True, this function will not be lazy, but it will still work in the expected way, just not lazy.

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

Examples using RecursiveUrlLoader

  * [Recursive URL](https://python.langchain.com/docs/integrations/document_loaders/recursive_url/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)