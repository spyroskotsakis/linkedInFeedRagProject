# UnstructuredHtmlEvaluator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.url_playwright.UnstructuredHtmlEvaluator.html
**Word Count:** 50
**Links Count:** 397
**Scraped:** 2025-07-21 08:06:47
**Status:** completed

---

# UnstructuredHtmlEvaluator\#

_class _langchain\_community.document\_loaders.url\_playwright.UnstructuredHtmlEvaluator\(

    _remove\_selectors : List\[str\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/url_playwright.html#UnstructuredHtmlEvaluator)\#     

Evaluate the page HTML content using the unstructured library.

Initialize UnstructuredHtmlEvaluator.

Methods

`__init__`\(\[remove\_selectors\]\) | Initialize UnstructuredHtmlEvaluator.   ---|---   `evaluate`\(page, browser, response\) | Synchronously process the HTML content of the page.   `evaluate_async`\(page, browser, response\) | Asynchronously process the HTML content of the page.      Parameters:     

**remove\_selectors** \(_List_ _\[__str_ _\]__|__None_\)

\_\_init\_\_\(

    _remove\_selectors : List\[str\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/url_playwright.html#UnstructuredHtmlEvaluator.__init__)\#     

Initialize UnstructuredHtmlEvaluator.

Parameters:     

**remove\_selectors** \(_List_ _\[__str_ _\]__|__None_\)

evaluate\(

    _page : Page_,     _browser : Browser_,     _response : Response_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/url_playwright.html#UnstructuredHtmlEvaluator.evaluate)\#     

Synchronously process the HTML content of the page.

Parameters:     

  * **page** \(_Page_\)

  * **browser** \(_Browser_\)

  * **response** \(_Response_\)

Return type:     

str

_async _evaluate\_async\(

    _page : AsyncPage_,     _browser : AsyncBrowser_,     _response : AsyncResponse_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/url_playwright.html#UnstructuredHtmlEvaluator.evaluate_async)\#     

Asynchronously process the HTML content of the page.

Parameters:     

  * **page** \(_AsyncPage_\)

  * **browser** \(_AsyncBrowser_\)

  * **response** \(_AsyncResponse_\)

Return type:     

str

__On this page