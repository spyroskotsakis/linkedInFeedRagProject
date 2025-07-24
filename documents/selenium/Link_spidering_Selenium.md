# Link spidering | Selenium

**URL:** https://www.selenium.dev/documentation/test_practices/discouraged/link_spidering
**Word Count:** 127
**Links Count:** 199
**Scraped:** 2025-07-17 06:15:56
**Status:** completed

---

# Link spidering

Using WebDriver to spider through links is not a recommended practice. Not because it cannot be done, but because WebDriver is definitely not the most ideal tool for this. WebDriver needs time to start up, and can take several seconds, up to a minute depending on how your test is written, just to get to the page and traverse through the DOM.

Instead of using WebDriver for this, you could save a ton of time by executing a [curl](https://curl.se/) command, or using a library such as BeautifulSoup since these methods do not rely on creating a browser and navigating to a page. You are saving tonnes of time by not using WebDriver for this task.

Last modified July 10, 2025: [Fix curl command name, syntax, and url \(\#2377\) \(93be0373967\)](https://github.com/SeleniumHQ/seleniumhq.github.io/commit/93be03739671d63c153916bd79b94e602b2a574c)