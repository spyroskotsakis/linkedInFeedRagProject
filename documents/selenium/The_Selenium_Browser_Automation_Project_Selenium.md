# The Selenium Browser Automation Project | Selenium

**URL:** https://www.selenium.dev/documentation
**Word Count:** 390
**Links Count:** 219
**Scraped:** 2025-07-17 06:13:36
**Status:** completed

---

# The Selenium Browser Automation Project

Selenium is an umbrella project for a range of tools and libraries that enable and support the automation of web browsers.

It provides extensions to emulate user interaction with browsers, a distribution server for scaling browser allocation, and the infrastructure for implementations of the [W3C WebDriver specification](https://www.w3.org/TR/webdriver/) that lets you write interchangeable code for all major web browsers.

This project is made possible by volunteer contributors who have put in thousands of hours of their own time, and made the source code [freely available](https://www.selenium.dev/documentation/about/copyright/#license) for anyone to use, enjoy, and improve.

Selenium brings together browser vendors, engineers, and enthusiasts to further an open discussion around automation of the web platform. The project organises [an annual conference](https://www.selenium.dev/) to teach and nurture the community.

At the core of Selenium is [WebDriver](https://www.selenium.dev/documentation/webdriver/), an interface to write instruction sets that can be run interchangeably in many browsers. Once you’ve installed everything, only a few lines of code get you inside a browser. You can find a more comprehensive example in [Writing your first Selenium script](https://www.selenium.dev/documentation/webdriver/getting_started/first_script/)

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

              package dev.selenium.hello;          import org.openqa.selenium.WebDriver;     import org.openqa.selenium.chrome.ChromeDriver;          public class HelloSelenium {         public static void main(String[] args) {             WebDriver driver = new ChromeDriver();                  driver.get("https://selenium.dev");                  driver.quit();         }     }     

[__**View on GitHub**](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/java/src/test/java/dev/selenium/hello/HelloSelenium.java)                from selenium import webdriver               driver = webdriver.Chrome()          driver.get("http://selenium.dev")          driver.quit()     

[__**View on GitHub**](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/python/tests/hello/hello_selenium.py)                using OpenQA.Selenium.Chrome;          namespace SeleniumDocs.Hello;          public static class HelloSelenium     {         public static void Main()         {             var driver = new ChromeDriver();                              driver.Navigate().GoToUrl("https://selenium.dev");                              driver.Quit();         }     }

[__**View on GitHub**](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/dotnet/HelloSelenium.cs)                # frozen_string_literal: true          require 'selenium-webdriver'          driver = Selenium::WebDriver.for :chrome          driver.get 'https://selenium.dev'          driver.quit     

[__**View on GitHub**](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/ruby/spec/hello/hello_selenium.rb)                const {Builder, Browser} = require('selenium-webdriver');          (async function helloSelenium() {       let driver = await new Builder().forBrowser(Browser.CHROME).build();            await driver.get('https://selenium.dev');            await driver.quit();     })();

[__**View on GitHub**](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/javascript/test/hello/helloSelenium.js)                package dev.selenium.hello          import org.openqa.selenium.chrome.ChromeDriver          fun main() {         val driver = ChromeDriver()              driver.get("https://selenium.dev")              driver.quit()     }     

[__**View on GitHub**](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/kotlin/src/test/kotlin/dev/selenium/hello/HelloSelenium.kt)

See the [Overview](https://www.selenium.dev/documentation/overview/) to check the different project components and decide if Selenium is the right tool for you.

You should continue on to [Getting Started](https://www.selenium.dev/documentation/webdriver/getting_started/) to understand how you can install Selenium and successfully use it as a test automation tool, and scaling simple tests like this to run in large, distributed environments on multiple browsers, on several different operating systems.

* * *

##### [Selenium Overview](https://www.selenium.dev/documentation/overview/)

Is Selenium for you? See an overview of the different project components.

##### [WebDriver](https://www.selenium.dev/documentation/webdriver/)

WebDriver drives a browser natively; learn more about it.

##### [Selenium Manager \(Beta\)](https://www.selenium.dev/documentation/selenium_manager/)

Selenium Manager is a command-line tool implemented in Rust that provides automated driver and browser management for Selenium. Selenium bindings use this tool by default, so you do not need to download it or add anything to your code or do anything else to use it.

##### [Grid](https://www.selenium.dev/documentation/grid/)

Want to run tests in parallel across multiple machines? Then, Grid is for you.

##### [IE Driver Server](https://www.selenium.dev/documentation/ie_driver_server/)

The Internet Explorer Driver is a standalone server that implements the WebDriver specification.

##### [Selenium IDE](https://www.selenium.dev/documentation/ide/)

The Selenium IDE is a browser extension that records and plays back a user’s actions.

##### [Test Practices](https://www.selenium.dev/documentation/test_practices/)

Some guidelines and recommendations on testing from the Selenium project.

##### [Legacy](https://www.selenium.dev/documentation/legacy/)

Documentation related to the legacy components of Selenium. Meant to be kept purely for historical reasons and not as a incentive to use deprecated components.

##### [About this documentation](https://www.selenium.dev/documentation/about/)

Last modified April 6, 2025: [\[rb\] do not run hello selenium in examples \(efaae63f2b6\)](https://github.com/SeleniumHQ/seleniumhq.github.io/commit/efaae63f2b66029b5022e5b0348414a1a29c631f)