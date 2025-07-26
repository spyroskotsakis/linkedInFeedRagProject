# Getting started | Selenium

**URL:** https://www.selenium.dev/documentation/webdriver/getting_started
**Word Count:** 291
**Links Count:** 202
**Scraped:** 2025-07-17 06:15:56
**Status:** completed

---

# Getting started

If you are new to Selenium, we have a few resources that can help you get up to speed right away.

Selenium supports automation of all the major browsers in the market through the use of _WebDriver_. WebDriver is an API and protocol that defines a language-neutral interface for controlling the behaviour of web browsers. Each browser is backed by a specific WebDriver implementation, called a _driver_. The driver is the component responsible for delegating down to the browser, and handles communication to and from Selenium and the browser.

This separation is part of a conscious effort to have browser vendors take responsibility for the implementation for their browsers. Selenium makes use of these third party drivers where possible, but also provides its own drivers maintained by the project for the cases when this is not a reality.

The Selenium framework ties all of these pieces together through a user-facing interface that enables the different browser backends to be used transparently, enabling cross-browser and cross-platform automation.

Selenium setup is quite different from the setup of other commercial tools. Before you can start writing Selenium code, you have to install the language bindings libraries for your language of choice, the browser you want to use, and the driver for that browser.

_**Follow the links below to get up and going with Selenium WebDriver.**_

If you wish to start with a low-code/record and playback tool, please check [Selenium IDE](https://selenium.dev/selenium-ide)

Once you get things working, if you want to scale up your tests, check out the [Selenium Grid](https://www.selenium.dev/documentation/grid/).

* * *

##### [Install a Selenium library](https://www.selenium.dev/documentation/webdriver/getting_started/install_library/)

Setting up the Selenium library for your favourite programming language.

##### [Write your first Selenium script](https://www.selenium.dev/documentation/webdriver/getting_started/first_script/)

Step-by-step instructions for constructing a Selenium script

##### [Organizing and Executing Selenium Code](https://www.selenium.dev/documentation/webdriver/getting_started/using_selenium/)

Scaling Selenium execution with an IDE and a Test Runner library

Last modified January 12, 2022: [Example code \(\#920\) \[deploy site\] \(d22cd1c186e\)](https://github.com/SeleniumHQ/seleniumhq.github.io/commit/d22cd1c186e65418f289ba81455a2e1b7d4d12ab)