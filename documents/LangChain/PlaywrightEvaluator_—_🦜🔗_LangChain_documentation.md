# PlaywrightEvaluator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.url_playwright.PlaywrightEvaluator.html
**Word Count:** 110
**Links Count:** 393
**Scraped:** 2025-07-21 08:19:13
**Status:** completed

---

# PlaywrightEvaluator\#

_class _langchain\_community.document\_loaders.url\_playwright.PlaywrightEvaluator[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/url_playwright.html#PlaywrightEvaluator)\#     

Abstract base class for all evaluators.

Each evaluator should take a page, a browser instance, and a response object, process the page as necessary, and return the resulting text.

Methods

`evaluate`\(page, browser, response\) | Synchronously process the page and return the resulting text.   ---|---   `evaluate_async`\(page, browser, response\) | Asynchronously process the page and return the resulting text.      _abstractmethod _evaluate\(

    _page : Page_,     _browser : Browser_,     _response : Response_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/url_playwright.html#PlaywrightEvaluator.evaluate)\#     

Synchronously process the page and return the resulting text.

Parameters:     

  * **page** \(_Page_\) – The page to process.

  * **browser** \(_Browser_\) – The browser instance.

  * **response** \(_Response_\) – The response from page.goto\(\).

Returns:     

The text content of the page.

Return type:     

text

_abstractmethod async _evaluate\_async\(

    _page : AsyncPage_,     _browser : AsyncBrowser_,     _response : AsyncResponse_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/url_playwright.html#PlaywrightEvaluator.evaluate_async)\#     

Asynchronously process the page and return the resulting text.

Parameters:     

  * **page** \(_AsyncPage_\) – The page to process.

  * **browser** \(_AsyncBrowser_\) – The browser instance.

  * **response** \(_AsyncResponse_\) – The response from page.goto\(\).

Returns:     

The text content of the page.

Return type:     

text

__On this page