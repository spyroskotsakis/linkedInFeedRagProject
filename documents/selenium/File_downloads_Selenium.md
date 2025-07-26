# File downloads | Selenium

**URL:** https://www.selenium.dev/documentation/test_practices/discouraged/file_downloads
**Word Count:** 107
**Links Count:** 202
**Scraped:** 2025-07-17 06:15:03
**Status:** completed

---

# File downloads

Whilst it is possible to start a download by clicking a link with a browser under Selenium’s control, the API does not expose download progress, making it less than ideal for testing downloaded files. This is because downloading files is not considered an important aspect of emulating user interaction with the web platform. Instead, find the link using Selenium \(and any required cookies\) and pass it to a HTTP request library like [curl](https://www.selenium.dev//curl.se/).

The [HtmlUnit driver](https://github.com/SeleniumHQ/htmlunit-driver) can download attachments by accessing them as input streams by implementing the [AttachmentHandler](https://htmlunit.sourceforge.io/apidocs/com/gargoylesoftware/htmlunit/attachment/AttachmentHandler.html) interface. The AttachmentHandler can then be added to the [HtmlUnit](https://htmlunit.sourceforge.io/) WebClient.

Last modified July 10, 2025: [Fix curl command name, syntax, and url \(\#2377\) \(93be0373967\)](https://github.com/SeleniumHQ/seleniumhq.github.io/commit/93be03739671d63c153916bd79b94e602b2a574c)