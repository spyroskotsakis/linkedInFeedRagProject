# AZLyricsLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.azlyrics.AZLyricsLoader.html
**Word Count:** 338
**Links Count:** 430
**Scraped:** 2025-07-21 08:20:13
**Status:** completed

---

# AZLyricsLoader\#

_class _langchain\_community.document\_loaders.azlyrics.AZLyricsLoader\(

    _web\_path : str | Sequence\[str\] = ''_,     _header\_template : dict | None = None_,     _verify\_ssl : bool = True_,     _proxies : dict | None = None_,     _continue\_on\_failure : bool = False_,     _autoset\_encoding : bool = True_,     _encoding : str | None = None_,     _web\_paths : Sequence\[str\] = \(\)_,     _requests\_per\_second : int = 2_,     _default\_parser : str = 'html.parser'_,     _requests\_kwargs : Dict\[str, Any\] | None = None_,     _raise\_for\_status : bool = False_,     _bs\_get\_text\_kwargs : Dict\[str, Any\] | None = None_,     _bs\_kwargs : Dict\[str, Any\] | None = None_,     _session : Any = None_,     _\*_ ,     _show\_progress : bool = True_,     _trust\_env : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/azlyrics.html#AZLyricsLoader)\#     

Load AZLyrics webpages.

Initialize loader.

Parameters:     

  * **web\_paths** \(_Sequence_ _\[__str_ _\]_\) – Web paths to load from.

  * **requests\_per\_second** \(_int_\) – Max number of concurrent requests to make.

  * **default\_parser** \(_str_\) – Default parser to use for BeautifulSoup.

  * **requests\_kwargs** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – kwargs for requests

  * **raise\_for\_status** \(_bool_\) – Raise an exception if http status code denotes an error.

  * **bs\_get\_text\_kwargs** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – kwargs for beatifulsoup4 get\_text

  * **bs\_kwargs** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – kwargs for beatifulsoup4 web page parsing

  * **show\_progress** \(_bool_\) – Show progress bar when loading pages.

  * **trust\_env** \(_bool_\) – set to True if using proxy to make web requests, for example using http\(s\)\_proxy environment variables. Defaults to False.

  * **web\_path** \(_str_ _|__Sequence_ _\[__str_ _\]_\)

  * **header\_template** \(_dict_ _|__None_\)

  * **verify\_ssl** \(_bool_\)

  * **proxies** \(_dict_ _|__None_\)

  * **continue\_on\_failure** \(_bool_\)

  * **autoset\_encoding** \(_bool_\)

  * **encoding** \(_str_ _|__None_\)

  * **session** \(_Any_\)

Attributes

`web_path` |    ---|---      Methods

`__init__`\(\[web\_path, header\_template, ...\]\) | Initialize loader.   ---|---   `alazy_load`\(\) | Async lazy load text from the url\(s\) in web\_path.   `aload`\(\) |    `ascrape_all`\(urls\[, parser\]\) | Async fetch all urls, then return soups for all results.   `fetch_all`\(urls\) | Fetch all urls concurrently with rate limiting.   `lazy_load`\(\) | Lazy load text from the url\(s\) in web\_path.   `load`\(\) | Load webpages into Documents.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.   `scrape`\(\[parser\]\) | Scrape data from webpage and return it in BeautifulSoup format.   `scrape_all`\(urls\[, parser\]\) | Fetch all urls, then return soups for all results.      \_\_init\_\_\(

    _web\_path : str | Sequence\[str\] = ''_,     _header\_template : dict | None = None_,     _verify\_ssl : bool = True_,     _proxies : dict | None = None_,     _continue\_on\_failure : bool = False_,     _autoset\_encoding : bool = True_,     _encoding : str | None = None_,     _web\_paths : Sequence\[str\] = \(\)_,     _requests\_per\_second : int = 2_,     _default\_parser : str = 'html.parser'_,     _requests\_kwargs : Dict\[str, Any\] | None = None_,     _raise\_for\_status : bool = False_,     _bs\_get\_text\_kwargs : Dict\[str, Any\] | None = None_,     _bs\_kwargs : Dict\[str, Any\] | None = None_,     _session : Any = None_,     _\*_ ,     _show\_progress : bool = True_,     _trust\_env : bool = False_, \) → None\#     

Initialize loader.

Parameters:     

  * **web\_paths** \(_Sequence_ _\[__str_ _\]_\) – Web paths to load from.

  * **requests\_per\_second** \(_int_\) – Max number of concurrent requests to make.

  * **default\_parser** \(_str_\) – Default parser to use for BeautifulSoup.

  * **requests\_kwargs** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – kwargs for requests

  * **raise\_for\_status** \(_bool_\) – Raise an exception if http status code denotes an error.

  * **bs\_get\_text\_kwargs** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – kwargs for beatifulsoup4 get\_text

  * **bs\_kwargs** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – kwargs for beatifulsoup4 web page parsing

  * **show\_progress** \(_bool_\) – Show progress bar when loading pages.

  * **trust\_env** \(_bool_\) – set to True if using proxy to make web requests, for example using http\(s\)\_proxy environment variables. Defaults to False.

  * **web\_path** \(_str_ _|__Sequence_ _\[__str_ _\]_\)

  * **header\_template** \(_dict_ _|__None_\)

  * **verify\_ssl** \(_bool_\)

  * **proxies** \(_dict_ _|__None_\)

  * **continue\_on\_failure** \(_bool_\)

  * **autoset\_encoding** \(_bool_\)

  * **encoding** \(_str_ _|__None_\)

  * **session** \(_Any_\)

Return type:     

None

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

Lazy load text from the url\(s\) in web\_path.

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/azlyrics.html#AZLyricsLoader.load)\#     

Load webpages into Documents.

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

Examples using AZLyricsLoader

  * [AZLyrics](https://python.langchain.com/docs/integrations/document_loaders/azlyrics/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)