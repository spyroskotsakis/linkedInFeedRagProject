# Browser interactions | Selenium

**URL:** https://www.selenium.dev/documentation/webdriver/interactions
**Word Count:** 393
**Links Count:** 219
**Scraped:** 2025-07-17 06:13:36
**Status:** completed

---

# Browser interactions

## Get browser information

### Get title

You can read the current page title from the browser:

[Move Code](https://www.selenium.dev/documentation/about/contributing/#moving-examples)

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

                    String title = driver.getTitle();

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/java/src/test/java/dev/selenium/interactions/InteractionsTest.java#L15)

##### examples/java/src/test/java/dev/selenium/interactions/InteractionsTest.java

Copy  Close               package dev.selenium.interactions;          import dev.selenium.BaseChromeTest;     import org.junit.jupiter.api.Assertions;     import org.junit.jupiter.api.Test;     import org.openqa.selenium.Cookie;     import java.util.Set;          public class InteractionsTest extends BaseChromeTest {       @Test       public void getTitle() {         try {           driver.get("https://www.selenium.dev/");           // get title           String title = driver.getTitle();           Assertions.assertEquals(title, "Selenium");         } finally {           driver.quit();         }       }       @Test       public void getCurrentUrl() {         try {           driver.get("https://www.selenium.dev/");           // get current url           String url = driver.getCurrentUrl();           Assertions.assertEquals(url, "https://www.selenium.dev/");         } finally {           driver.quit();         }       }     }               title = driver.title

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/interactions/test_interactions.py#L7)

##### examples/python/tests/interactions/test\_interactions.py

Copy  Close               from selenium import webdriver          driver = webdriver.Chrome()          driver.get("https://www.selenium.dev")          title = driver.title     assert title == "Selenium"          url = driver.current_url     assert url == "https://www.selenium.dev/"          driver.quit()                                String title = driver.Title;

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/dotnet/SeleniumDocs/Interactions/InteractionsTest.cs#L37)

##### examples/dotnet/SeleniumDocs/Interactions/InteractionsTest.cs

Copy  Close               // Licensed to the Software Freedom Conservancy (SFC) under one     // or more contributor license agreements.  See the NOTICE file     // distributed with this work for additional information     // regarding copyright ownership.  The SFC licenses this file     // to you under the Apache License, Version 2.0 (the     // "License"); you may not use this file except in compliance     // with the License.  You may obtain a copy of the License at     //     //   http://www.apache.org/licenses/LICENSE-2.0     //     // Unless required by applicable law or agreed to in writing,     // software distributed under the License is distributed on an     // "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY     // KIND, either express or implied.  See the License for the     // specific language governing permissions and limitations     // under the License.               using System;     using Microsoft.VisualStudio.TestTools.UnitTesting;     using OpenQA.Selenium;     using OpenQA.Selenium.Chrome;     namespace SeleniumDocumentation.SeleniumInteractions     {         [TestClass]         public class InteractionsTest         {             [TestMethod]             public void TestInteractions()             {                 WebDriver driver = new ChromeDriver();                 driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromMilliseconds(500);                      // Navigate to Url                 driver.Url="https://www.selenium.dev/";                 //GetTitle                 String title = driver.Title;                 Assert.AreEqual(title, "Selenium");                      //GetCurrentURL                 String url = driver.Url;                 Assert.AreEqual(url, "https://www.selenium.dev/");                      //quitting driver                 driver.Quit(); //close all windows             }         }     }                 it 'gets the current title' do

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/ruby/spec/interactions/browser_spec.rb#L8)

##### examples/ruby/spec/interactions/browser\_spec.rb

Copy  Close               # frozen_string_literal: true          require 'spec_helper'          RSpec.describe 'Browser' do       let(:driver) { start_session }            it 'gets the current title' do         driver.navigate.to 'https://www.selenium.dev/'         current_title = driver.title         expect(current_title).to eq 'Selenium'       end            it 'gets the current url' do         driver.navigate.to 'https://www.selenium.dev/'         current_url = driver.current_url         expect(current_url).to eq 'https://www.selenium.dev/'       end     end                        let title = await driver.getTitle();

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/javascript/test/interactions/interactionsIndex.spec.js#L20)

##### examples/javascript/test/interactions/interactionsIndex.spec.js

Copy  Close               const {Builder } = require('selenium-webdriver');     const assert = require("node:assert");          describe('Interactions', function () {       let driver;            before(async function () {         driver = new Builder()           .forBrowser('chrome')           .build();       });            after(async () => await driver.quit());            it('Should be able to get title and current url', async function () {         const url = 'https://www.selenium.dev/';         await driver.get(url);              //Get Current title         let title = await driver.getTitle();         assert.equal(title, "Selenium");              //Get Current url         let currentUrl = await driver.getCurrentUrl();         assert.equal(currentUrl, url);       });     });               driver.title

### Get current URL

You can read the current URL from the browser’s address bar using:

[Move Code](https://www.selenium.dev/documentation/about/contributing/#moving-examples)

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

                    String url = driver.getCurrentUrl();

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/java/src/test/java/dev/selenium/interactions/InteractionsTest.java#L26)

##### examples/java/src/test/java/dev/selenium/interactions/InteractionsTest.java

Copy  Close               package dev.selenium.interactions;          import dev.selenium.BaseChromeTest;     import org.junit.jupiter.api.Assertions;     import org.junit.jupiter.api.Test;     import org.openqa.selenium.Cookie;     import java.util.Set;          public class InteractionsTest extends BaseChromeTest {       @Test       public void getTitle() {         try {           driver.get("https://www.selenium.dev/");           // get title           String title = driver.getTitle();           Assertions.assertEquals(title, "Selenium");         } finally {           driver.quit();         }       }       @Test       public void getCurrentUrl() {         try {           driver.get("https://www.selenium.dev/");           // get current url           String url = driver.getCurrentUrl();           Assertions.assertEquals(url, "https://www.selenium.dev/");         } finally {           driver.quit();         }       }     }               url = driver.current_url

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/interactions/test_interactions.py#L10)

##### examples/python/tests/interactions/test\_interactions.py

Copy  Close               from selenium import webdriver          driver = webdriver.Chrome()          driver.get("https://www.selenium.dev")          title = driver.title     assert title == "Selenium"          url = driver.current_url     assert url == "https://www.selenium.dev/"          driver.quit()                                String url = driver.Url;

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/dotnet/SeleniumDocs/Interactions/InteractionsTest.cs#L41)

##### examples/dotnet/SeleniumDocs/Interactions/InteractionsTest.cs

Copy  Close               // Licensed to the Software Freedom Conservancy (SFC) under one     // or more contributor license agreements.  See the NOTICE file     // distributed with this work for additional information     // regarding copyright ownership.  The SFC licenses this file     // to you under the Apache License, Version 2.0 (the     // "License"); you may not use this file except in compliance     // with the License.  You may obtain a copy of the License at     //     //   http://www.apache.org/licenses/LICENSE-2.0     //     // Unless required by applicable law or agreed to in writing,     // software distributed under the License is distributed on an     // "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY     // KIND, either express or implied.  See the License for the     // specific language governing permissions and limitations     // under the License.               using System;     using Microsoft.VisualStudio.TestTools.UnitTesting;     using OpenQA.Selenium;     using OpenQA.Selenium.Chrome;     namespace SeleniumDocumentation.SeleniumInteractions     {         [TestClass]         public class InteractionsTest         {             [TestMethod]             public void TestInteractions()             {                 WebDriver driver = new ChromeDriver();                 driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromMilliseconds(500);                      // Navigate to Url                 driver.Url="https://www.selenium.dev/";                 //GetTitle                 String title = driver.Title;                 Assert.AreEqual(title, "Selenium");                      //GetCurrentURL                 String url = driver.Url;                 Assert.AreEqual(url, "https://www.selenium.dev/");                      //quitting driver                 driver.Quit(); //close all windows             }         }     }                 it 'gets the current url' do

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/ruby/spec/interactions/browser_spec.rb#L14)

##### examples/ruby/spec/interactions/browser\_spec.rb

Copy  Close               # frozen_string_literal: true          require 'spec_helper'          RSpec.describe 'Browser' do       let(:driver) { start_session }            it 'gets the current title' do         driver.navigate.to 'https://www.selenium.dev/'         current_title = driver.title         expect(current_title).to eq 'Selenium'       end            it 'gets the current url' do         driver.navigate.to 'https://www.selenium.dev/'         current_url = driver.current_url         expect(current_url).to eq 'https://www.selenium.dev/'       end     end                        let currentUrl = await driver.getCurrentUrl();

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/javascript/test/interactions/interactionsIndex.spec.js#L24)

##### examples/javascript/test/interactions/interactionsIndex.spec.js

Copy  Close               const {Builder } = require('selenium-webdriver');     const assert = require("node:assert");          describe('Interactions', function () {       let driver;            before(async function () {         driver = new Builder()           .forBrowser('chrome')           .build();       });            after(async () => await driver.quit());            it('Should be able to get title and current url', async function () {         const url = 'https://www.selenium.dev/';         await driver.get(url);              //Get Current title         let title = await driver.getTitle();         assert.equal(title, "Selenium");              //Get Current url         let currentUrl = await driver.getCurrentUrl();         assert.equal(currentUrl, url);       });     });               driver.currentUrl

* * *

##### [Browser navigation](https://www.selenium.dev/documentation/webdriver/interactions/navigation/)

##### [JavaScript alerts, prompts and confirmations](https://www.selenium.dev/documentation/webdriver/interactions/alerts/)

##### [Working with cookies](https://www.selenium.dev/documentation/webdriver/interactions/cookies/)

##### [Working with IFrames and frames](https://www.selenium.dev/documentation/webdriver/interactions/frames/)

##### [Print Page](https://www.selenium.dev/documentation/webdriver/interactions/print_page/)

##### [Working with windows and tabs](https://www.selenium.dev/documentation/webdriver/interactions/windows/)

##### [Virtual Authenticator](https://www.selenium.dev/documentation/webdriver/interactions/virtual_authenticator/)

A representation of the Web Authenticator model.

Last modified September 26, 2024: [added interaction csharp code \(\#1958\) \(914d0c52089\)](https://github.com/SeleniumHQ/seleniumhq.github.io/commit/914d0c52089dc6eab170d70034bca605c1623860)