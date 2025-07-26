# create_sync_playwright_browser — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.playwright.utils.create_sync_playwright_browser.html
**Word Count:** 31
**Links Count:** 407
**Scraped:** 2025-07-21 08:12:36
**Status:** completed

---

# create\_sync\_playwright\_browser\#

langchain\_community.tools.playwright.utils.create\_sync\_playwright\_browser\(

    _headless : bool = True_,     _args : List\[str\] | None = None_, \) → SyncBrowser[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/playwright/utils.html#create_sync_playwright_browser)\#     

Create a playwright browser.

Parameters:     

  * **headless** \(_bool_\) – Whether to run the browser in headless mode. Defaults to True.

  * **args** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – arguments to pass to browser.chromium.launch

Returns:     

The playwright browser.

Return type:     

SyncBrowser

__On this page