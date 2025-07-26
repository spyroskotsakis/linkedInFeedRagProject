# Crawler — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chains/langchain.chains.natbot.crawler.Crawler.html
**Word Count:** 75
**Links Count:** 217
**Scraped:** 2025-07-21 07:51:08
**Status:** completed

---

# Crawler\#

_class _langchain.chains.natbot.crawler.Crawler[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/natbot/crawler.html#Crawler)\#     

A crawler for web pages.

**Security Note** : This is an implementation of a crawler that uses a browser via     

Playwright.

This crawler can be used to load arbitrary webpages INCLUDING content from the local file system.

Control access to who can submit crawling requests and what network access the crawler has.

Make sure to scope permissions to the minimal permissions necessary for the application.

See <https://python.langchain.com/docs/security> for more information.

Methods

`__init__`\(\) |    ---|---   `click`\(id\_\) |    `crawl`\(\) |    `enter`\(\) |    `go_to_page`\(url\) |    `scroll`\(direction\) |    `type`\(id\_, text\) |       \_\_init\_\_\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/natbot/crawler.html#Crawler.__init__)\#     

Return type:     

None

click\(_id\_ : str | int_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/natbot/crawler.html#Crawler.click)\#     

Parameters:     

**id\_** \(_str_ _|__int_\)

Return type:     

None

crawl\(\) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/natbot/crawler.html#Crawler.crawl)\#     

Return type:     

list\[str\]

enter\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/natbot/crawler.html#Crawler.enter)\#     

Return type:     

None

go\_to\_page\(_url : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/natbot/crawler.html#Crawler.go_to_page)\#     

Parameters:     

**url** \(_str_\)

Return type:     

None

scroll\(_direction : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/natbot/crawler.html#Crawler.scroll)\#     

Parameters:     

**direction** \(_str_\)

Return type:     

None

type\(_id\_ : str | int_, _text : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/natbot/crawler.html#Crawler.type)\#     

Parameters:     

  * **id\_** \(_str_ _|__int_\)

  * **text** \(_str_\)

Return type:     

None

__On this page