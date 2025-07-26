# create_async_playwright_browser — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.playwright.utils.create_async_playwright_browser.html
**Word Count:** 36
**Links Count:** 408
**Scraped:** 2025-07-21 08:12:36
**Status:** completed

---

# create\_async\_playwright\_browser\#

langchain\_community.tools.playwright.utils.create\_async\_playwright\_browser\(

    _headless : bool = True_,     _args : List\[str\] | None = None_, \) → AsyncBrowser[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/playwright/utils.html#create_async_playwright_browser)\#     

Create an async playwright browser.

Parameters:     

  * **headless** \(_bool_\) – Whether to run the browser in headless mode. Defaults to True.

  * **args** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – arguments to pass to browser.chromium.launch

Returns:     

The playwright browser.

Return type:     

AsyncBrowser

Examples using create\_async\_playwright\_browser

  * [PlayWright Browser Toolkit](https://python.langchain.com/docs/integrations/tools/playwright/)

__On this page