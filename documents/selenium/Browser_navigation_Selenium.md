# Browser navigation | Selenium

**URL:** https://www.selenium.dev/documentation/webdriver/interactions/navigation
**Word Count:** 285
**Links Count:** 222
**Scraped:** 2025-07-17 06:13:36
**Status:** completed

---

# Browser navigation

## Navigate to

The first thing you will want to do after launching a browser is to open your website. This can be achieved in a single line:

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

                      //Convenient             driver.get("https://selenium.dev");                              //Longer way             driver.navigate().to("https://selenium.dev");

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/java/src/test/java/dev/selenium/interactions/NavigationTest.java#L14-L18)

##### examples/java/src/test/java/dev/selenium/interactions/NavigationTest.java

Copy  Close               package dev.selenium.interactions;          import org.junit.jupiter.api.Test;     import org.openqa.selenium.WebDriver;     import org.openqa.selenium.chrome.ChromeDriver;     import static org.junit.jupiter.api.Assertions.assertEquals;          public class NavigationTest {         @Test         public void navigateBrowser() {                          WebDriver driver = new ChromeDriver();                        //Convenient             driver.get("https://selenium.dev");                              //Longer way             driver.navigate().to("https://selenium.dev");             String title = driver.getTitle();             assertEquals(title, "Selenium");                          //Back             driver.navigate().back();             title = driver.getTitle();             assertEquals(title, "Selenium");                          //Forward             driver.navigate().forward();             title = driver.getTitle();             assertEquals(title, "Selenium");                  //Refresh             driver.navigate().refresh();             title = driver.getTitle();             assertEquals(title, "Selenium");                  driver.quit();         }     }                    driver.get("https://www.selenium.dev/selenium/web/index.html")

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/interactions/test_navigation.py#L6)

##### examples/python/tests/interactions/test\_navigation.py

Copy  Close               from selenium import webdriver          driver = webdriver.Chrome()          driver.get("https://www.selenium.dev")     driver.get("https://www.selenium.dev/selenium/web/index.html")          title = driver.title     assert title == "Index of Available Pages"          driver.back()     title = driver.title     assert title == "Selenium"          driver.forward()     title = driver.title     assert title == "Index of Available Pages"          driver.refresh()     title = driver.title     assert title == "Index of Available Pages"          driver.quit()                                //Convenient                 driver.Url = "https://selenium.dev";                 //Longer                 driver.Navigate().GoToUrl("https://selenium.dev");

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/dotnet/SeleniumDocs/Interactions/NavigationTest.cs#L17-L20)

##### examples/dotnet/SeleniumDocs/Interactions/NavigationTest.cs

Copy  Close               using System;     using Microsoft.VisualStudio.TestTools.UnitTesting;     using OpenQA.Selenium;     using OpenQA.Selenium.Chrome;          namespace SeleniumDocumentation.SeleniumInteractions     {         [TestClass]         public class NavigationTest         {             [TestMethod]             public void TestNavigationCommands()             {                 IWebDriver driver = new ChromeDriver();                 driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromMilliseconds(500);                      //Convenient                 driver.Url = "https://selenium.dev";                 //Longer                 driver.Navigate().GoToUrl("https://selenium.dev");                 var title = driver.Title;                 Assert.AreEqual("Selenium", title);                      //Back                 driver.Navigate().Back();                 title = driver.Title;                 Assert.AreEqual("Selenium", title);                      //Forward                 driver.Navigate().Forward();                 title = driver.Title;                 Assert.AreEqual("Selenium", title);                      //Refresh                 driver.Navigate().Refresh();                 title = driver.Title;                 Assert.AreEqual("Selenium", title);                      //Quit the browser                 driver.Quit();             }         }     }                      it 'navigates to a page' do         driver.navigate.to 'https://www.selenium.dev/'

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/ruby/spec/interactions/navigation_spec.rb#L7-L9)

##### examples/ruby/spec/interactions/navigation\_spec.rb

Copy  Close               # frozen_string_literal: true          require 'spec_helper'          RSpec.describe 'Browser' do       let(:driver) { start_session }            it 'navigates to a page' do         driver.navigate.to 'https://www.selenium.dev/'         driver.get 'https://www.selenium.dev/'         expect(driver.current_url).to eq 'https://www.selenium.dev/'       end            it 'navigates back' do         driver.navigate.to 'https://www.selenium.dev/'         driver.navigate.to 'https://www.selenium.dev/selenium/web/inputs.html'         driver.navigate.back         expect(driver.current_url).to eq 'https://www.selenium.dev/'       end            it 'navigates forward' do         driver.navigate.to 'https://www.selenium.dev/'         driver.navigate.to 'https://www.selenium.dev/selenium/web/inputs.html'         driver.navigate.back         driver.navigate.forward         expect(driver.current_url).to eq 'https://www.selenium.dev/selenium/web/inputs.html'       end            it 'refreshes the page' do         driver.navigate.to 'https://www.selenium.dev/'         driver.navigate.refresh         expect(driver.current_url).to eq 'https://www.selenium.dev/'       end     end                        //Convenient           await driver.get('https://www.selenium.dev');                  //Longer way           await driver.navigate().to("https://www.selenium.dev/selenium/web/index.html");

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/javascript/test/interactions/navigation.spec.js#L16-L20)

##### examples/javascript/test/interactions/navigation.spec.js

Copy  Close               const {Builder } = require('selenium-webdriver');       const assert = require("node:assert");              describe('Interactions - Navigation', function () {         let driver;                before(async function () {           driver = new Builder()             .forBrowser('chrome')             .build();         });                after(async () => await driver.quit());                it('Browser navigation test', async function () {           //Convenient           await driver.get('https://www.selenium.dev');                  //Longer way           await driver.navigate().to("https://www.selenium.dev/selenium/web/index.html");           let title = await driver.getTitle();           assert.equal(title, "Index of Available Pages");                  //Back           await driver.navigate().back();           title = await driver.getTitle();           assert.equal(title, "Selenium");                  //Forward           await driver.navigate().forward();           title = await driver.getTitle();           assert.equal(title, "Index of Available Pages");                  //Refresh           await driver.navigate().refresh();           title = await driver.getTitle();           assert.equal(title, "Index of Available Pages");         });       });               //Convenient     driver.get("https://selenium.dev")          //Longer way     driver.navigate().to("https://selenium.dev")       

## Back

Pressing the browser’s back button:

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

                      //Back             driver.navigate().back();

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/java/src/test/java/dev/selenium/interactions/NavigationTest.java#L22-L23)

##### examples/java/src/test/java/dev/selenium/interactions/NavigationTest.java

Copy  Close               package dev.selenium.interactions;          import org.junit.jupiter.api.Test;     import org.openqa.selenium.WebDriver;     import org.openqa.selenium.chrome.ChromeDriver;     import static org.junit.jupiter.api.Assertions.assertEquals;          public class NavigationTest {         @Test         public void navigateBrowser() {                          WebDriver driver = new ChromeDriver();                        //Convenient             driver.get("https://selenium.dev");                              //Longer way             driver.navigate().to("https://selenium.dev");             String title = driver.getTitle();             assertEquals(title, "Selenium");                          //Back             driver.navigate().back();             title = driver.getTitle();             assertEquals(title, "Selenium");                          //Forward             driver.navigate().forward();             title = driver.getTitle();             assertEquals(title, "Selenium");                  //Refresh             driver.navigate().refresh();             title = driver.getTitle();             assertEquals(title, "Selenium");                  driver.quit();         }     }                    driver.back()

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/interactions/test_navigation.py#L11)

##### examples/python/tests/interactions/test\_navigation.py

Copy  Close               from selenium import webdriver          driver = webdriver.Chrome()          driver.get("https://www.selenium.dev")     driver.get("https://www.selenium.dev/selenium/web/index.html")          title = driver.title     assert title == "Index of Available Pages"          driver.back()     title = driver.title     assert title == "Selenium"          driver.forward()     title = driver.title     assert title == "Index of Available Pages"          driver.refresh()     title = driver.title     assert title == "Index of Available Pages"          driver.quit()                                //Back                  driver.Navigate().Back();

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/dotnet/SeleniumDocs/Interactions/NavigationTest.cs#L24-L25)

##### examples/dotnet/SeleniumDocs/Interactions/NavigationTest.cs

Copy  Close               using System;      using Microsoft.VisualStudio.TestTools.UnitTesting;      using OpenQA.Selenium;      using OpenQA.Selenium.Chrome;            namespace SeleniumDocumentation.SeleniumInteractions      {          [TestClass]          public class NavigationTest          {              [TestMethod]              public void TestNavigationCommands()              {                  IWebDriver driver = new ChromeDriver();                  driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromMilliseconds(500);                        //Convenient                  driver.Url = "https://selenium.dev";                  //Longer                  driver.Navigate().GoToUrl("https://selenium.dev");                  var title = driver.Title;                  Assert.AreEqual("Selenium", title);                        //Back                  driver.Navigate().Back();                  title = driver.Title;                  Assert.AreEqual("Selenium", title);                        //Forward                  driver.Navigate().Forward();                  title = driver.Title;                  Assert.AreEqual("Selenium", title);                        //Refresh                  driver.Navigate().Refresh();                  title = driver.Title;                  Assert.AreEqual("Selenium", title);                        //Quit the browser                  driver.Quit();              }          }      }                         driver.navigate.to 'https://www.selenium.dev/'

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/ruby/spec/interactions/navigation_spec.rb#L15)

##### examples/ruby/spec/interactions/navigation\_spec.rb

Copy  Close               # frozen_string_literal: true          require 'spec_helper'          RSpec.describe 'Browser' do       let(:driver) { start_session }            it 'navigates to a page' do         driver.navigate.to 'https://www.selenium.dev/'         driver.get 'https://www.selenium.dev/'         expect(driver.current_url).to eq 'https://www.selenium.dev/'       end            it 'navigates back' do         driver.navigate.to 'https://www.selenium.dev/'         driver.navigate.to 'https://www.selenium.dev/selenium/web/inputs.html'         driver.navigate.back         expect(driver.current_url).to eq 'https://www.selenium.dev/'       end            it 'navigates forward' do         driver.navigate.to 'https://www.selenium.dev/'         driver.navigate.to 'https://www.selenium.dev/selenium/web/inputs.html'         driver.navigate.back         driver.navigate.forward         expect(driver.current_url).to eq 'https://www.selenium.dev/selenium/web/inputs.html'       end            it 'refreshes the page' do         driver.navigate.to 'https://www.selenium.dev/'         driver.navigate.refresh         expect(driver.current_url).to eq 'https://www.selenium.dev/'       end     end                        //Back           await driver.navigate().back();

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/javascript/test/interactions/navigation.spec.js#L24-L25)

##### examples/javascript/test/interactions/navigation.spec.js

Copy  Close               const {Builder } = require('selenium-webdriver');       const assert = require("node:assert");              describe('Interactions - Navigation', function () {         let driver;                before(async function () {           driver = new Builder()             .forBrowser('chrome')             .build();         });                after(async () => await driver.quit());                it('Browser navigation test', async function () {           //Convenient           await driver.get('https://www.selenium.dev');                  //Longer way           await driver.navigate().to("https://www.selenium.dev/selenium/web/index.html");           let title = await driver.getTitle();           assert.equal(title, "Index of Available Pages");                  //Back           await driver.navigate().back();           title = await driver.getTitle();           assert.equal(title, "Selenium");                  //Forward           await driver.navigate().forward();           title = await driver.getTitle();           assert.equal(title, "Index of Available Pages");                  //Refresh           await driver.navigate().refresh();           title = await driver.getTitle();           assert.equal(title, "Index of Available Pages");         });       });               driver.navigate().back() 

## Forward

Pressing the browser’s forward button:

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

                      //Forward             driver.navigate().forward();

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/java/src/test/java/dev/selenium/interactions/NavigationTest.java#L27-L28)

##### examples/java/src/test/java/dev/selenium/interactions/NavigationTest.java

Copy  Close               package dev.selenium.interactions;          import org.junit.jupiter.api.Test;     import org.openqa.selenium.WebDriver;     import org.openqa.selenium.chrome.ChromeDriver;     import static org.junit.jupiter.api.Assertions.assertEquals;          public class NavigationTest {         @Test         public void navigateBrowser() {                          WebDriver driver = new ChromeDriver();                        //Convenient             driver.get("https://selenium.dev");                              //Longer way             driver.navigate().to("https://selenium.dev");             String title = driver.getTitle();             assertEquals(title, "Selenium");                          //Back             driver.navigate().back();             title = driver.getTitle();             assertEquals(title, "Selenium");                          //Forward             driver.navigate().forward();             title = driver.getTitle();             assertEquals(title, "Selenium");                  //Refresh             driver.navigate().refresh();             title = driver.getTitle();             assertEquals(title, "Selenium");                  driver.quit();         }     }                    driver.forward()

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/interactions/test_navigation.py#L15)

##### examples/python/tests/interactions/test\_navigation.py

Copy  Close               from selenium import webdriver          driver = webdriver.Chrome()          driver.get("https://www.selenium.dev")     driver.get("https://www.selenium.dev/selenium/web/index.html")          title = driver.title     assert title == "Index of Available Pages"          driver.back()     title = driver.title     assert title == "Selenium"          driver.forward()     title = driver.title     assert title == "Index of Available Pages"          driver.refresh()     title = driver.title     assert title == "Index of Available Pages"          driver.quit()                                //Forward                  driver.Navigate().Forward();

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/dotnet/SeleniumDocs/Interactions/NavigationTest.cs#L29-L30)

##### examples/dotnet/SeleniumDocs/Interactions/NavigationTest.cs

Copy  Close               using System;      using Microsoft.VisualStudio.TestTools.UnitTesting;      using OpenQA.Selenium;      using OpenQA.Selenium.Chrome;            namespace SeleniumDocumentation.SeleniumInteractions      {          [TestClass]          public class NavigationTest          {              [TestMethod]              public void TestNavigationCommands()              {                  IWebDriver driver = new ChromeDriver();                  driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromMilliseconds(500);                        //Convenient                  driver.Url = "https://selenium.dev";                  //Longer                  driver.Navigate().GoToUrl("https://selenium.dev");                  var title = driver.Title;                  Assert.AreEqual("Selenium", title);                        //Back                  driver.Navigate().Back();                  title = driver.Title;                  Assert.AreEqual("Selenium", title);                        //Forward                  driver.Navigate().Forward();                  title = driver.Title;                  Assert.AreEqual("Selenium", title);                        //Refresh                  driver.Navigate().Refresh();                  title = driver.Title;                  Assert.AreEqual("Selenium", title);                        //Quit the browser                  driver.Quit();              }          }      }                         driver.navigate.to 'https://www.selenium.dev/selenium/web/inputs.html'

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/ruby/spec/interactions/navigation_spec.rb#L23)

##### examples/ruby/spec/interactions/navigation\_spec.rb

Copy  Close               # frozen_string_literal: true          require 'spec_helper'          RSpec.describe 'Browser' do       let(:driver) { start_session }            it 'navigates to a page' do         driver.navigate.to 'https://www.selenium.dev/'         driver.get 'https://www.selenium.dev/'         expect(driver.current_url).to eq 'https://www.selenium.dev/'       end            it 'navigates back' do         driver.navigate.to 'https://www.selenium.dev/'         driver.navigate.to 'https://www.selenium.dev/selenium/web/inputs.html'         driver.navigate.back         expect(driver.current_url).to eq 'https://www.selenium.dev/'       end            it 'navigates forward' do         driver.navigate.to 'https://www.selenium.dev/'         driver.navigate.to 'https://www.selenium.dev/selenium/web/inputs.html'         driver.navigate.back         driver.navigate.forward         expect(driver.current_url).to eq 'https://www.selenium.dev/selenium/web/inputs.html'       end            it 'refreshes the page' do         driver.navigate.to 'https://www.selenium.dev/'         driver.navigate.refresh         expect(driver.current_url).to eq 'https://www.selenium.dev/'       end     end                        //Forward         await driver.navigate().forward();

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/javascript/test/interactions/navigation.spec.js#L29-L30)

##### examples/javascript/test/interactions/navigation.spec.js

Copy  Close               const {Builder } = require('selenium-webdriver');     const assert = require("node:assert");          describe('Interactions - Navigation', function () {       let driver;            before(async function () {         driver = new Builder()           .forBrowser('chrome')           .build();       });            after(async () => await driver.quit());            it('Browser navigation test', async function () {         //Convenient         await driver.get('https://www.selenium.dev');              //Longer way         await driver.navigate().to("https://www.selenium.dev/selenium/web/index.html");         let title = await driver.getTitle();         assert.equal(title, "Index of Available Pages");              //Back         await driver.navigate().back();         title = await driver.getTitle();         assert.equal(title, "Selenium");              //Forward         await driver.navigate().forward();         title = await driver.getTitle();         assert.equal(title, "Index of Available Pages");              //Refresh         await driver.navigate().refresh();         title = await driver.getTitle();         assert.equal(title, "Index of Available Pages");       });     });               driver.navigate().forward()

## Refresh

Refresh the current page:

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

                      //Refresh             driver.navigate().refresh();

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/java/src/test/java/dev/selenium/interactions/NavigationTest.java#L32-L33)

##### examples/java/src/test/java/dev/selenium/interactions/NavigationTest.java

Copy  Close               package dev.selenium.interactions;          import org.junit.jupiter.api.Test;     import org.openqa.selenium.WebDriver;     import org.openqa.selenium.chrome.ChromeDriver;     import static org.junit.jupiter.api.Assertions.assertEquals;          public class NavigationTest {         @Test         public void navigateBrowser() {                          WebDriver driver = new ChromeDriver();                        //Convenient             driver.get("https://selenium.dev");                              //Longer way             driver.navigate().to("https://selenium.dev");             String title = driver.getTitle();             assertEquals(title, "Selenium");                          //Back             driver.navigate().back();             title = driver.getTitle();             assertEquals(title, "Selenium");                          //Forward             driver.navigate().forward();             title = driver.getTitle();             assertEquals(title, "Selenium");                  //Refresh             driver.navigate().refresh();             title = driver.getTitle();             assertEquals(title, "Selenium");                  driver.quit();         }     }                    driver.refresh()

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/interactions/test_navigation.py#L19)

##### examples/python/tests/interactions/test\_navigation.py

Copy  Close               from selenium import webdriver          driver = webdriver.Chrome()          driver.get("https://www.selenium.dev")     driver.get("https://www.selenium.dev/selenium/web/index.html")          title = driver.title     assert title == "Index of Available Pages"          driver.back()     title = driver.title     assert title == "Selenium"          driver.forward()     title = driver.title     assert title == "Index of Available Pages"          driver.refresh()     title = driver.title     assert title == "Index of Available Pages"          driver.quit()                                //Refresh                  driver.Navigate().Refresh();

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/dotnet/SeleniumDocs/Interactions/NavigationTest.cs#L34-L35)

##### examples/dotnet/SeleniumDocs/Interactions/NavigationTest.cs

Copy  Close               using System;      using Microsoft.VisualStudio.TestTools.UnitTesting;      using OpenQA.Selenium;      using OpenQA.Selenium.Chrome;            namespace SeleniumDocumentation.SeleniumInteractions      {          [TestClass]          public class NavigationTest          {              [TestMethod]              public void TestNavigationCommands()              {                  IWebDriver driver = new ChromeDriver();                  driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromMilliseconds(500);                        //Convenient                  driver.Url = "https://selenium.dev";                  //Longer                  driver.Navigate().GoToUrl("https://selenium.dev");                  var title = driver.Title;                  Assert.AreEqual("Selenium", title);                        //Back                  driver.Navigate().Back();                  title = driver.Title;                  Assert.AreEqual("Selenium", title);                        //Forward                  driver.Navigate().Forward();                  title = driver.Title;                  Assert.AreEqual("Selenium", title);                        //Refresh                  driver.Navigate().Refresh();                  title = driver.Title;                  Assert.AreEqual("Selenium", title);                        //Quit the browser                  driver.Quit();              }          }      }                       it 'refreshes the page' do

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/ruby/spec/interactions/navigation_spec.rb#L29)

##### examples/ruby/spec/interactions/navigation\_spec.rb

Copy  Close               # frozen_string_literal: true          require 'spec_helper'          RSpec.describe 'Browser' do       let(:driver) { start_session }            it 'navigates to a page' do         driver.navigate.to 'https://www.selenium.dev/'         driver.get 'https://www.selenium.dev/'         expect(driver.current_url).to eq 'https://www.selenium.dev/'       end            it 'navigates back' do         driver.navigate.to 'https://www.selenium.dev/'         driver.navigate.to 'https://www.selenium.dev/selenium/web/inputs.html'         driver.navigate.back         expect(driver.current_url).to eq 'https://www.selenium.dev/'       end            it 'navigates forward' do         driver.navigate.to 'https://www.selenium.dev/'         driver.navigate.to 'https://www.selenium.dev/selenium/web/inputs.html'         driver.navigate.back         driver.navigate.forward         expect(driver.current_url).to eq 'https://www.selenium.dev/selenium/web/inputs.html'       end            it 'refreshes the page' do         driver.navigate.to 'https://www.selenium.dev/'         driver.navigate.refresh         expect(driver.current_url).to eq 'https://www.selenium.dev/'       end     end                        //Refresh         await driver.navigate().refresh();

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/javascript/test/interactions/navigation.spec.js#L34-L35)

##### examples/javascript/test/interactions/navigation.spec.js

Copy  Close               const {Builder } = require('selenium-webdriver');     const assert = require("node:assert");          describe('Interactions - Navigation', function () {       let driver;            before(async function () {         driver = new Builder()           .forBrowser('chrome')           .build();       });            after(async () => await driver.quit());            it('Browser navigation test', async function () {         //Convenient         await driver.get('https://www.selenium.dev');              //Longer way         await driver.navigate().to("https://www.selenium.dev/selenium/web/index.html");         let title = await driver.getTitle();         assert.equal(title, "Index of Available Pages");              //Back         await driver.navigate().back();         title = await driver.getTitle();         assert.equal(title, "Selenium");              //Forward         await driver.navigate().forward();         title = await driver.getTitle();         assert.equal(title, "Index of Available Pages");              //Refresh         await driver.navigate().refresh();         title = await driver.getTitle();         assert.equal(title, "Index of Available Pages");       });     });               driver.navigate().refresh()

Last modified August 5, 2024: [\[rb\] Move documentation examples for general interactions and navigation \(\#1837\)\[deploy site\] \(1d9f037a766\)](https://github.com/SeleniumHQ/seleniumhq.github.io/commit/1d9f037a7669f4b714062ca2d39150e681330b77)