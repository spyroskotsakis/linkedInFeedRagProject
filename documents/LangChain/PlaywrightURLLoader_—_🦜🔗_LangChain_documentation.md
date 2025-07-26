# PlaywrightURLLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.url_playwright.PlaywrightURLLoader.html
**Word Count:** 235
**Links Count:** 434
**Scraped:** 2025-07-21 08:22:10
**Status:** completed

---

# PlaywrightURLLoader\#

_class _langchain\_community.document\_loaders.url\_playwright.PlaywrightURLLoader\(

    _urls : List\[str\]_,     _continue\_on\_failure : bool = True_,     _headless : bool = True_,     _remove\_selectors : List\[str\] | None = None_,     _evaluator : [PlaywrightEvaluator](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.url_playwright.PlaywrightEvaluator.html#langchain_community.document_loaders.url_playwright.PlaywrightEvaluator "langchain_community.document_loaders.url_playwright.PlaywrightEvaluator") | None = None_,     _proxy : Dict\[str, str\] | None = None_,     _browser\_session : str | PathLike\[str\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/url_playwright.html#PlaywrightURLLoader)\#     

Load HTML pages with Playwright and parse with Unstructured.

This is useful for loading pages that require javascript to render.

Parameters:     

  * **urls** \(_List_ _\[__str_ _\]_\)

  * **continue\_on\_failure** \(_bool_\)

  * **headless** \(_bool_\)

  * **remove\_selectors** \(_List_ _\[__str_ _\]__|__None_\)

  * **evaluator** \([_PlaywrightEvaluator_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.url_playwright.PlaywrightEvaluator.html#langchain_community.document_loaders.url_playwright.PlaywrightEvaluator "langchain_community.document_loaders.url_playwright.PlaywrightEvaluator") _|__None_\)

  * **proxy** \(_Dict_ _\[__str_ _,__str_ _\]__|__None_\)

  * **browser\_session** \(_str_ _|__PathLike_ _\[__str_ _\]__|__None_\)

urls\#     

List of URLs to load.

Type:     

List\[str\]

continue\_on\_failure\#     

If True, continue loading other URLs on failure.

Type:     

bool

headless\#     

If True, the browser will run in headless mode.

Type:     

bool

proxy\#     

If set, the browser will access URLs through the specified proxy.

Type:     

Optional\[Dict\[str, str\]\]

browser\_session\#     

Path to a file with browser session data that can be used to restore the browser session.

Type:     

Optional\[Union\[str, os.PathLike\[str\]\]\]

Example               from langchain_community.document_loaders import PlaywrightURLLoader          urls = ["https://api.ipify.org/?format=json",]     proxy={         "server": "https://xx.xx.xx:15818", # https://<host>:<port>         "username": "username",         "password": "password"     }     loader = PlaywrightURLLoader(urls, proxy=proxy)     data = loader.load()     

Load a list of URLs using Playwright.

Methods

`__init__`\(urls\[, continue\_on\_failure, ...\]\) | Load a list of URLs using Playwright.   ---|---   `alazy_load`\(\) | Load the specified URLs with Playwright and create Documents asynchronously.   `aload`\(\) | Load the specified URLs with Playwright and create Documents asynchronously.   `lazy_load`\(\) | Load the specified URLs using Playwright and create Document instances.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _urls : List\[str\]_,     _continue\_on\_failure : bool = True_,     _headless : bool = True_,     _remove\_selectors : List\[str\] | None = None_,     _evaluator : [PlaywrightEvaluator](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.url_playwright.PlaywrightEvaluator.html#langchain_community.document_loaders.url_playwright.PlaywrightEvaluator "langchain_community.document_loaders.url_playwright.PlaywrightEvaluator") | None = None_,     _proxy : Dict\[str, str\] | None = None_,     _browser\_session : str | PathLike\[str\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/url_playwright.html#PlaywrightURLLoader.__init__)\#     

Load a list of URLs using Playwright.

Parameters:     

  * **urls** \(_List_ _\[__str_ _\]_\)

  * **continue\_on\_failure** \(_bool_\)

  * **headless** \(_bool_\)

  * **remove\_selectors** \(_List_ _\[__str_ _\]__|__None_\)

  * **evaluator** \([_PlaywrightEvaluator_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.url_playwright.PlaywrightEvaluator.html#langchain_community.document_loaders.url_playwright.PlaywrightEvaluator "langchain_community.document_loaders.url_playwright.PlaywrightEvaluator") _|__None_\)

  * **proxy** \(_Dict_ _\[__str_ _,__str_ _\]__|__None_\)

  * **browser\_session** \(_str_ _|__PathLike_ _\[__str_ _\]__|__None_\)

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/url_playwright.html#PlaywrightURLLoader.alazy_load)\#     

Load the specified URLs with Playwright and create Documents asynchronously. Use this function when in a jupyter notebook environment.

Returns:     

A list of Document instances with loaded content.

Return type:     

_AsyncIterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/url_playwright.html#PlaywrightURLLoader.aload)\#     

Load the specified URLs with Playwright and create Documents asynchronously. Use this function when in a jupyter notebook environment.

Returns:     

A list of Document instances with loaded content.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/url_playwright.html#PlaywrightURLLoader.lazy_load)\#     

Load the specified URLs using Playwright and create Document instances.

Returns:     

A list of Document instances with loaded content.

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

Examples using PlaywrightURLLoader

  * [URL](https://python.langchain.com/docs/integrations/document_loaders/url/)

__On this page