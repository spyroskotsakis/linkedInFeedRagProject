# Chrome DevTools Protocol | Selenium

**URL:** https://www.selenium.dev/documentation/webdriver/bidi/cdp
**Word Count:** 433
**Links Count:** 209
**Scraped:** 2025-07-17 06:15:56
**Status:** completed

---

# Chrome DevTools Protocol

Examples of working with Chrome DevTools Protocol in Selenium. CDP support is temporary until WebDriver BiDi has been implemented.

Many browsers provide “DevTools” – a set of tools that are integrated with the browser that developers can use to debug web apps and explore the performance of their pages. Google Chrome’s DevTools make use of a protocol called the Chrome DevTools Protocol \(or “CDP” for short\). As the name suggests, this is not designed for testing, nor to have a stable API, so functionality is highly dependent on the version of the browser.

Selenium is working to implement a standards-based, cross-browser, stable alternative to CDP called \[WebDriver BiDi\]. Until the support for this new protocol has finished, Selenium plans to provide access to CDP features where applicable.

### Using Chrome DevTools Protocol with Selenium

Chrome and Edge have a method to send basic CDP commands. This does not work for features that require bidirectional communication, and you need to know what domains to enable when and the exact names and types of domains/methods/parameters.

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

                  Map<String, Object> cookie = new HashMap<>();         cookie.put("name", "cheese");         cookie.put("value", "gouda");         cookie.put("domain", "www.selenium.dev");         cookie.put("secure", true);         ((HasCdp) driver).executeCdpCommand("Network.setCookie", cookie);

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/java/src/test/java/dev/selenium/bidi/cdp/CdpTest.java#L22-L27)

##### /examples/java/src/test/java/dev/selenium/bidi/cdp/CdpTest.java

Copy  Close               package dev.selenium.bidi.cdp;          import dev.selenium.BaseTest;     import org.junit.jupiter.api.Assertions;     import org.junit.jupiter.api.BeforeEach;     import org.junit.jupiter.api.Test;     import org.openqa.selenium.Cookie;     import org.openqa.selenium.chrome.ChromeDriver;     import org.openqa.selenium.chromium.HasCdp;          import java.util.HashMap;     import java.util.Map;          public class CdpTest extends BaseTest {       @BeforeEach       public void createSession() {         driver = new ChromeDriver();       }            @Test       public void setCookie() {         Map<String, Object> cookie = new HashMap<>();         cookie.put("name", "cheese");         cookie.put("value", "gouda");         cookie.put("domain", "www.selenium.dev");         cookie.put("secure", true);         ((HasCdp) driver).executeCdpCommand("Network.setCookie", cookie);              driver.get("https://www.selenium.dev");         Cookie cheese = driver.manage().getCookieNamed("cheese");         Assertions.assertEquals("gouda", cheese.getValue());       }     }                        cookie = {'name': 'cheese',                   'value': 'gouda',                   'domain': 'www.selenium.dev',                   'secure': True}              driver.execute_cdp_cmd('Network.setCookie', cookie)

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/python/tests/bidi/cdp/test_cdp.py#L2-L7)

##### /examples/python/tests/bidi/cdp/test\_cdp.py

Copy  Close               def test_set_cookie(driver):         cookie = {'name': 'cheese',                   'value': 'gouda',                   'domain': 'www.selenium.dev',                   'secure': True}              driver.execute_cdp_cmd('Network.setCookie', cookie)              driver.get('https://www.selenium.dev')         cheese = driver.get_cookie(cookie['name'])              assert cheese['value'] == 'gouda'                                var cookie = new Dictionary<string, object>                 {                     { "name", "cheese" },                     { "value", "gouda" },                     { "domain", "www.selenium.dev" },                     { "secure", true }                 };                 ((ChromeDriver)driver).ExecuteCdpCommand("Network.setCookie", cookie);

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/dotnet/SeleniumDocs/BiDi/CDP/CDPTest.cs#L14-L21)

##### /examples/dotnet/SeleniumDocs/BiDi/CDP/CDPTest.cs

Copy  Close               using System.Collections.Generic;     using Microsoft.VisualStudio.TestTools.UnitTesting;     using OpenQA.Selenium;     using OpenQA.Selenium.Chrome;          namespace SeleniumDocs.BiDi.CDP     {         [TestClass]         public class CDPTest : BaseChromeTest         {             [TestMethod]             public void SetCookie()             {                 var cookie = new Dictionary<string, object>                 {                     { "name", "cheese" },                     { "value", "gouda" },                     { "domain", "www.selenium.dev" },                     { "secure", true }                 };                 ((ChromeDriver)driver).ExecuteCdpCommand("Network.setCookie", cookie);                                  driver.Url = "https://www.selenium.dev";                 Cookie cheese = driver.Manage().Cookies.GetCookieNamed("cheese");                 Assert.AreEqual("gouda", cheese.Value);                  }         }     }                   driver.execute_cdp('Network.setCookie',                            name: 'cheese',                            value: 'gouda',                            domain: 'www.selenium.dev',                            secure: true)

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/ruby/spec/bidi/cdp/cdp_spec.rb#L9-L13)

##### /examples/ruby/spec/bidi/cdp/cdp\_spec.rb

Copy  Close               # frozen_string_literal: true          require 'spec_helper'          RSpec.describe 'Logging' do       let(:driver) { start_session }            it 'sets cookie' do         driver.execute_cdp('Network.setCookie',                            name: 'cheese',                            value: 'gouda',                            domain: 'www.selenium.dev',                            secure: true)              driver.get('https://www.selenium.dev')         cheese = driver.manage.cookie_named('cheese')              expect(cheese[:value]).to eq 'gouda'       end     end     

[Add Example](https://www.selenium.dev/documentation/about/contributing/#creating-examples)

[Add Example](https://www.selenium.dev/documentation/about/contributing/#creating-examples)

To make working with CDP easier, and to provide access to the more advanced features, Selenium bindings automatically generate classes and methods for the most common domains. CDP methods and implementations can change from version to version, though, so you want to keep the version of Chrome and the version of DevTools matching. Selenium supports the 3 most recent versions of Chrome at any given time, and tries to time releases to ensure that access to the latest versions are available.

This limitation provides additional challenges for several bindings, where dynamically generated CDP support requires users to regularly update their code to reference the proper version of CDP. In some cases an idealized implementation has been created that should work for any version of CDP without the user needing to change their code, but that is not always available.

Examples of how to use CDP in your Selenium tests can be found on the following pages, but we want to call out a couple commonly cited examples that are of limited practical value.

  * **Geo Location** — almost all sites use the IP address to determine physical location, so setting an emulated geolocation rarely has the desired effect.   * **Overriding Device Metrics** — Chrome provides a great API for setting [Mobile Emulation](https://chromedriver.chromium.org/mobile-emulation) in the Options classes, which is generally superior to attempting to do this with CDP.

* * *

##### [Chrome DevTools Logging Features](https://www.selenium.dev/documentation/webdriver/bidi/cdp/logging/)

Logging features using CDP.

##### [Chrome DevTools Network Features](https://www.selenium.dev/documentation/webdriver/bidi/cdp/network/)

Network features using CDP.

##### [Chrome DevTools Script Features](https://www.selenium.dev/documentation/webdriver/bidi/cdp/script/)

Script features using CDP.

Last modified July 10, 2024: [Release 4.22 Updates \(\#1765\) \(fa7b1165ed0\)](https://github.com/SeleniumHQ/seleniumhq.github.io/commit/fa7b1165ed03cb8051d18522e1775a247f48ade9)