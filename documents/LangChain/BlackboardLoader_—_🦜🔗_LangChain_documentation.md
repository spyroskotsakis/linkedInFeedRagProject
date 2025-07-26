# BlackboardLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.blackboard.BlackboardLoader.html
**Word Count:** 474
**Links Count:** 443
**Scraped:** 2025-07-21 08:12:08
**Status:** completed

---

# BlackboardLoader\#

_class _langchain\_community.document\_loaders.blackboard.BlackboardLoader\(

    _blackboard\_course\_url : str_,     _bbrouter : str_,     _load\_all\_recursively : bool = True_,     _basic\_auth : Tuple\[str, str\] | None = None_,     _cookies : dict | None = None_,     _continue\_on\_failure : bool = False_,     _show\_progress : bool = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/blackboard.html#BlackboardLoader)\#     

Load a Blackboard course.

This loader is not compatible with all Blackboard courses. It is only compatible with courses that use the new Blackboard interface. To use this loader, you must have the BbRouter cookie. You can get this cookie by logging into the course and then copying the value of the BbRouter cookie from the browser’s developer tools.

Example               from langchain_community.document_loaders import BlackboardLoader          loader = BlackboardLoader(         blackboard_course_url="https://blackboard.example.com/webapps/blackboard/execute/announcement?method=search&context=course_entry&course_id=_123456_1",         bbrouter="expires:12345...",     )     documents = loader.load()     

Initialize with blackboard course url.

The BbRouter cookie is required for most blackboard courses.

Parameters:     

  * **blackboard\_course\_url** \(_str_\) – Blackboard course url.

  * **bbrouter** \(_str_\) – BbRouter cookie.

  * **load\_all\_recursively** \(_bool_\) – If True, load all documents recursively.

  * **basic\_auth** \(_Tuple_ _\[__str_ _,__str_ _\]__|__None_\) – Basic auth credentials.

  * **cookies** \(_dict_ _|__None_\) – Cookies.

  * **continue\_on\_failure** \(_bool_\) – whether to continue loading the sitemap if an error occurs loading a url, emitting a warning instead of raising an exception. Setting this to True makes the loader more robust, but also may result in missing data. Default: False

  * **show\_progress** \(_bool_\) – whether to show a progress bar while loading. Default: True

Raises:     

**ValueError** – If blackboard course url is invalid.

Attributes

`web_path` |    ---|---      Methods

`__init__`\(blackboard\_course\_url, bbrouter\[, ...\]\) | Initialize with blackboard course url.   ---|---   `alazy_load`\(\) | Async lazy load text from the url\(s\) in web\_path.   `aload`\(\) |    `ascrape_all`\(urls\[, parser\]\) | Async fetch all urls, then return soups for all results.   `check_bs4`\(\) | Check if BeautifulSoup4 is installed.   `download`\(path\) | Download a file from an url.   `fetch_all`\(urls\) | Fetch all urls concurrently with rate limiting.   `lazy_load`\(\) | Lazy load text from the url\(s\) in web\_path.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.   `parse_filename`\(url\) | Parse the filename from an url.   `scrape`\(\[parser\]\) | Scrape data from webpage and return it in BeautifulSoup format.   `scrape_all`\(urls\[, parser\]\) | Fetch all urls, then return soups for all results.      \_\_init\_\_\(

    _blackboard\_course\_url : str_,     _bbrouter : str_,     _load\_all\_recursively : bool = True_,     _basic\_auth : Tuple\[str, str\] | None = None_,     _cookies : dict | None = None_,     _continue\_on\_failure : bool = False_,     _show\_progress : bool = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/blackboard.html#BlackboardLoader.__init__)\#     

Initialize with blackboard course url.

The BbRouter cookie is required for most blackboard courses.

Parameters:     

  * **blackboard\_course\_url** \(_str_\) – Blackboard course url.

  * **bbrouter** \(_str_\) – BbRouter cookie.

  * **load\_all\_recursively** \(_bool_\) – If True, load all documents recursively.

  * **basic\_auth** \(_Tuple_ _\[__str_ _,__str_ _\]__|__None_\) – Basic auth credentials.

  * **cookies** \(_dict_ _|__None_\) – Cookies.

  * **continue\_on\_failure** \(_bool_\) – whether to continue loading the sitemap if an error occurs loading a url, emitting a warning instead of raising an exception. Setting this to True makes the loader more robust, but also may result in missing data. Default: False

  * **show\_progress** \(_bool_\) – whether to show a progress bar while loading. Default: True

Raises:     

**ValueError** – If blackboard course url is invalid.

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

check\_bs4\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/blackboard.html#BlackboardLoader.check_bs4)\#     

Check if BeautifulSoup4 is installed.

Raises:     

**ImportError** – If BeautifulSoup4 is not installed.

Return type:     

None

download\(_path : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/blackboard.html#BlackboardLoader.download)\#     

Download a file from an url.

Parameters:     

**path** \(_str_\) – Path to the file.

Return type:     

None

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

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/blackboard.html#BlackboardLoader.load)\#     

Load data into Document objects.

Returns:     

List of Documents.

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

parse\_filename\(_url : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/blackboard.html#BlackboardLoader.parse_filename)\#     

Parse the filename from an url.

Parameters:     

**url** \(_str_\) – Url to parse the filename from.

Returns:     

The filename.

Return type:     

str

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

Examples using BlackboardLoader

  * [Blackboard](https://python.langchain.com/docs/integrations/document_loaders/blackboard/)

__On this page