# Troubleshooting Assistance | Selenium

**URL:** https://www.selenium.dev/documentation/webdriver/troubleshooting
**Word Count:** 173
**Links Count:** 204
**Scraped:** 2025-07-17 06:15:03
**Status:** completed

---

# Troubleshooting Assistance

How to solve WebDriver problems.

It is not always obvious the root cause of errors in Selenium.

  1. The most common Selenium-related error is a result of poor synchronization. Read about [Waiting Strategies](https://www.selenium.dev/documentation/webdriver/waits/). If you aren’t sure if it is a synchronization strategy you can try _temporarily_ hard coding a large sleep where you see the issue, and you’ll know if adding an explicit wait can help.

  2. Note that many errors that get reported to the project are actually caused by issues in the underlying drivers that Selenium sends the commands to. You can rule out a driver problem by executing the command in multiple [browsers](https://www.selenium.dev/documentation/webdriver/browsers/).

  3. If you have questions about how to do things, check out the [Support options](https://www.selenium.dev/support/) for ways get assistance.

  4. If you think you’ve found a problem with Selenium code, go ahead and file a [Bug Report](https://github.com/SeleniumHQ/selenium/issues/new?assignees=&labels=I-defect%2Cneeds-triaging&template=bug-report.yml&title=%5B%F0%9F%90%9B+Bug%5D%3A+) on GitHub.

* * *

##### [Understanding Common Errors](https://www.selenium.dev/documentation/webdriver/troubleshooting/errors/)

How to solve various problems in your Selenium code.

##### [Logging Selenium commands](https://www.selenium.dev/documentation/webdriver/troubleshooting/logging/)

Getting information about Selenium execution.

##### [Upgrade to Selenium 4](https://www.selenium.dev/documentation/webdriver/troubleshooting/upgrade_to_selenium_4/)

Are you still using Selenium 3? This guide will help you upgrade to the latest release\!

Last modified November 7, 2024: [Rephrase/reformat a few sentences \(\#1981\) \(77ae509e3ca\)](https://github.com/SeleniumHQ/seleniumhq.github.io/commit/77ae509e3ca40109ca5e74fec1f4f05f69df75f7)