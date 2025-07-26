# Chrome DevTools Logging Features | Selenium

**URL:** https://www.selenium.dev/documentation/webdriver/bidi/cdp/logging
**Word Count:** 117
**Links Count:** 213
**Scraped:** 2025-07-17 06:13:36
**Status:** completed

---

# Chrome DevTools Logging Features

Logging features using CDP.

While Selenium 4 provides direct access to the Chrome DevTools Protocol, these methods will eventually be removed when WebDriver BiDi implemented.

## Console Logs

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

                  ((HasLogEvents) driver).onLogEvent(consoleEvent(e -> messages.add(e.getMessages().get(0))));

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/java/src/test/java/dev/selenium/bidi/cdp/LoggingTest.java#L31)

##### /examples/java/src/test/java/dev/selenium/bidi/cdp/LoggingTest.java

Copy  Close               package dev.selenium.bidi.cdp;          import static org.openqa.selenium.devtools.events.CdpEventTypes.consoleEvent;          import dev.selenium.BaseTest;          import java.time.Duration;     import java.util.concurrent.CopyOnWriteArrayList;          import org.junit.jupiter.api.Assertions;     import org.junit.jupiter.api.BeforeEach;     import org.junit.jupiter.api.Test;     import org.openqa.selenium.*;     import org.openqa.selenium.chrome.ChromeDriver;     import org.openqa.selenium.logging.HasLogEvents;     import org.openqa.selenium.support.ui.WebDriverWait;          public class LoggingTest extends BaseTest {            @BeforeEach       public void createSession() {         driver = new ChromeDriver();         wait = new WebDriverWait(driver, Duration.ofSeconds(10));       }            @Test       public void consoleLogs() {         driver.get("https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html");         CopyOnWriteArrayList<String> messages = new CopyOnWriteArrayList<>();              ((HasLogEvents) driver).onLogEvent(consoleEvent(e -> messages.add(e.getMessages().get(0))));              driver.findElement(By.id("consoleLog")).click();         driver.findElement(By.id("consoleError")).click();              wait.until(_d -> messages.size() > 1);         Assertions.assertTrue(messages.contains("Hello, world!"));         Assertions.assertTrue(messages.contains("I am console error"));       }     }                        async with driver.bidi_connection() as session:             async with Log(driver, session).add_listener(Console.ALL) as messages:

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/python/tests/bidi/cdp/test_logs.py#L11-12)

##### /examples/python/tests/bidi/cdp/test\_logs.py

Copy  Close               import pytest     from selenium.webdriver.common.bidi.console import Console     from selenium.webdriver.common.by import By     from selenium.webdriver.common.log import Log               @pytest.mark.trio     async def test_console_log(driver):         driver.get('https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html')              async with driver.bidi_connection() as session:             async with Log(driver, session).add_listener(Console.ALL) as messages:                 driver.find_element(by=By.ID, value='consoleLog').click()                  assert messages["message"] == "Hello, world!"               @pytest.mark.trio     async def test_js_error(driver):         driver.get('https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html')              async with driver.bidi_connection() as session:             async with Log(driver, session).add_js_error_listener() as messages:                 driver.find_element(by=By.ID, value='jsException').click()                  assert "Error: Not working" in messages.exception_details.exception.description                                using IJavaScriptEngine monitor = new JavaScriptEngine(driver);                 var messages = new List<string>();                 monitor.JavaScriptConsoleApiCalled += (_, e) =>                 {                     messages.Add(e.MessageContent);                 };                 await monitor.StartEventMonitoring();

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/dotnet/SeleniumDocs/BiDi/CDP/LoggingTest.cs#L19-L25)

##### /examples/dotnet/SeleniumDocs/BiDi/CDP/LoggingTest.cs

Copy  Close               using System;     using System.Collections.Generic;     using System.Threading.Tasks;     using Microsoft.IdentityModel.Tokens;     using Microsoft.VisualStudio.TestTools.UnitTesting;     using OpenQA.Selenium;     using OpenQA.Selenium.Support.UI;          namespace SeleniumDocs.BiDi.CDP     {         [TestClass]         public class LoggingTest : BaseChromeTest         {             [TestMethod]             public async Task ConsoleLogs()             {                 driver.Url = "https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html";                      using IJavaScriptEngine monitor = new JavaScriptEngine(driver);                 var messages = new List<string>();                 monitor.JavaScriptConsoleApiCalled += (_, e) =>                 {                     messages.Add(e.MessageContent);                 };                 await monitor.StartEventMonitoring();                      driver.FindElement(By.Id("consoleLog")).Click();                 driver.FindElement(By.Id("consoleError")).Click();                 new WebDriverWait(driver, TimeSpan.FromSeconds(5)).Until(_ => messages.Count > 1);                 monitor.StopEventMonitoring();                      Assert.IsTrue(messages.Contains("Hello, world!"));                 Assert.IsTrue(messages.Contains("I am console error"));             }                          [TestMethod]             public async Task JsErrors()             {                 driver.Url = "https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html";                      using IJavaScriptEngine monitor = new JavaScriptEngine(driver);                 var messages = new List<string>();                 monitor.JavaScriptExceptionThrown += (_, e) =>                 {                     messages.Add(e.Message);                 };                 await monitor.StartEventMonitoring();                      driver.FindElement(By.Id("jsException")).Click();                 new WebDriverWait(driver, TimeSpan.FromSeconds(5)).Until(_ => !messages.IsNullOrEmpty());                 monitor.StopEventMonitoring();                      Assert.IsTrue(messages.Contains("Uncaught"));             }         }     }                   driver.on_log_event(:console) { |log| logs << log.args.first }

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/ruby/spec/bidi/cdp/logging_spec.rb#L12)

##### /examples/ruby/spec/bidi/cdp/logging\_spec.rb

Copy  Close               # frozen_string_literal: true          require 'spec_helper'          RSpec.describe 'Logging' do       let(:driver) { start_session }            it 'listens for console logs' do         driver.get('https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html')              logs = []         driver.on_log_event(:console) { |log| logs << log.args.first }              driver.find_element(id: 'consoleLog').click         driver.find_element(id: 'consoleError').click              Selenium::WebDriver::Wait.new.until { logs.size > 1 }         expect(logs).to include 'Hello, world!'         expect(logs).to include 'I am console error'       end            it 'listens for js exception' do         driver.get('https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html')              exceptions = []         driver.on_log_event(:exception) { |exception| exceptions << exception }              driver.find_element(id: 'jsException').click              Selenium::WebDriver::Wait.new.until { exceptions.any? }         expect(exceptions.first&.description).to include 'Error: Not working'       end     end     

[Implementation Missing](https://github.com/SeleniumHQ/selenium)

[Add Example](https://www.selenium.dev/documentation/about/contributing/#creating-examples)

## JavaScript Exceptions

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

[Implementation Missing](https://github.com/SeleniumHQ/selenium)                   async with driver.bidi_connection() as session:             async with Log(driver, session).add_js_error_listener() as messages:

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/python/tests/bidi/cdp/test_logs.py#L22-L23)

##### /examples/python/tests/bidi/cdp/test\_logs.py

Copy  Close               import pytest     from selenium.webdriver.common.bidi.console import Console     from selenium.webdriver.common.by import By     from selenium.webdriver.common.log import Log               @pytest.mark.trio     async def test_console_log(driver):         driver.get('https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html')              async with driver.bidi_connection() as session:             async with Log(driver, session).add_listener(Console.ALL) as messages:                 driver.find_element(by=By.ID, value='consoleLog').click()                  assert messages["message"] == "Hello, world!"               @pytest.mark.trio     async def test_js_error(driver):         driver.get('https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html')              async with driver.bidi_connection() as session:             async with Log(driver, session).add_js_error_listener() as messages:                 driver.find_element(by=By.ID, value='jsException').click()                  assert "Error: Not working" in messages.exception_details.exception.description                                using IJavaScriptEngine monitor = new JavaScriptEngine(driver);                 var messages = new List<string>();                 monitor.JavaScriptExceptionThrown += (_, e) =>                 {                     messages.Add(e.Message);                 };                 await monitor.StartEventMonitoring();

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/dotnet/SeleniumDocs/BiDi/CDP/LoggingTest.cs#L41-L47)

##### /examples/dotnet/SeleniumDocs/BiDi/CDP/LoggingTest.cs

Copy  Close               using System;     using System.Collections.Generic;     using System.Threading.Tasks;     using Microsoft.IdentityModel.Tokens;     using Microsoft.VisualStudio.TestTools.UnitTesting;     using OpenQA.Selenium;     using OpenQA.Selenium.Support.UI;          namespace SeleniumDocs.BiDi.CDP     {         [TestClass]         public class LoggingTest : BaseChromeTest         {             [TestMethod]             public async Task ConsoleLogs()             {                 driver.Url = "https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html";                      using IJavaScriptEngine monitor = new JavaScriptEngine(driver);                 var messages = new List<string>();                 monitor.JavaScriptConsoleApiCalled += (_, e) =>                 {                     messages.Add(e.MessageContent);                 };                 await monitor.StartEventMonitoring();                      driver.FindElement(By.Id("consoleLog")).Click();                 driver.FindElement(By.Id("consoleError")).Click();                 new WebDriverWait(driver, TimeSpan.FromSeconds(5)).Until(_ => messages.Count > 1);                 monitor.StopEventMonitoring();                      Assert.IsTrue(messages.Contains("Hello, world!"));                 Assert.IsTrue(messages.Contains("I am console error"));             }                          [TestMethod]             public async Task JsErrors()             {                 driver.Url = "https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html";                      using IJavaScriptEngine monitor = new JavaScriptEngine(driver);                 var messages = new List<string>();                 monitor.JavaScriptExceptionThrown += (_, e) =>                 {                     messages.Add(e.Message);                 };                 await monitor.StartEventMonitoring();                      driver.FindElement(By.Id("jsException")).Click();                 new WebDriverWait(driver, TimeSpan.FromSeconds(5)).Until(_ => !messages.IsNullOrEmpty());                 monitor.StopEventMonitoring();                      Assert.IsTrue(messages.Contains("Uncaught"));             }         }     }                   driver.on_log_event(:exception) { |exception| exceptions << exception }

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/ruby/spec/bidi/cdp/logging_spec.rb#L26)

##### /examples/ruby/spec/bidi/cdp/logging\_spec.rb

Copy  Close               # frozen_string_literal: true          require 'spec_helper'          RSpec.describe 'Logging' do       let(:driver) { start_session }            it 'listens for console logs' do         driver.get('https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html')              logs = []         driver.on_log_event(:console) { |log| logs << log.args.first }              driver.find_element(id: 'consoleLog').click         driver.find_element(id: 'consoleError').click              Selenium::WebDriver::Wait.new.until { logs.size > 1 }         expect(logs).to include 'Hello, world!'         expect(logs).to include 'I am console error'       end            it 'listens for js exception' do         driver.get('https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html')              exceptions = []         driver.on_log_event(:exception) { |exception| exceptions << exception }              driver.find_element(id: 'jsException').click              Selenium::WebDriver::Wait.new.until { exceptions.any? }         expect(exceptions.first&.description).to include 'Error: Not working'       end     end     

[Implementation Missing](https://github.com/SeleniumHQ/selenium)

[Add Example](https://www.selenium.dev/documentation/about/contributing/#creating-examples)

Last modified July 10, 2024: [Release 4.22 Updates \(\#1765\) \(fa7b1165ed0\)](https://github.com/SeleniumHQ/seleniumhq.github.io/commit/fa7b1165ed03cb8051d18522e1775a247f48ade9)