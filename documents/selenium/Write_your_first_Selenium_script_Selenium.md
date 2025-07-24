# Write your first Selenium script | Selenium

**URL:** https://www.selenium.dev/documentation/webdriver/getting_started/first_script
**Word Count:** 1027
**Links Count:** 273
**Scraped:** 2025-07-17 06:13:36
**Status:** completed

---

# Write your first Selenium script

Step-by-step instructions for constructing a Selenium script

Once you have [Selenium installed](https://www.selenium.dev/documentation/webdriver/getting_started/install_library/), you’re ready to write Selenium code.

## Eight Basic Components

Everything Selenium does is send the browser commands to do something or send requests for information. Most of what you’ll do with Selenium is a combination of these basic commands

Click on the link to “View full example on GitHub” to see the code in context.

### 1\. Start the session

For more details on starting a session read our documentation on [driver sessions](https://www.selenium.dev/documentation/webdriver/drivers/)

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

                      WebDriver driver = new ChromeDriver();

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/java/src/test/java/dev/selenium/getting_started/FirstScript.java#L12)

##### examples/java/src/test/java/dev/selenium/getting\_started/FirstScript.java

Copy  Close               package dev.selenium.getting_started;          import org.openqa.selenium.By;     import org.openqa.selenium.WebDriver;     import org.openqa.selenium.WebElement;     import org.openqa.selenium.chrome.ChromeDriver;          import java.time.Duration;          public class FirstScript {         public static void main(String[] args) {             WebDriver driver = new ChromeDriver();                  driver.get("https://www.selenium.dev/selenium/web/web-form.html");                  driver.getTitle();                  driver.manage().timeouts().implicitlyWait(Duration.ofMillis(500));                  WebElement textBox = driver.findElement(By.name("my-text"));             WebElement submitButton = driver.findElement(By.cssSelector("button"));                  textBox.sendKeys("Selenium");             submitButton.click();                  WebElement message = driver.findElement(By.id("message"));             message.getText();                  driver.quit();         }     }                    driver = webdriver.Chrome()

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/getting_started/first_script.py#L4)

##### examples/python/tests/getting\_started/first\_script.py

Copy  Close               from selenium import webdriver     from selenium.webdriver.common.by import By          driver = webdriver.Chrome()          driver.get("https://www.selenium.dev/selenium/web/web-form.html")          title = driver.title          driver.implicitly_wait(0.5)          text_box = driver.find_element(by=By.NAME, value="my-text")     submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")          text_box.send_keys("Selenium")     submit_button.click()          message = driver.find_element(by=By.ID, value="message")     text = message.text          driver.quit()                            IWebDriver driver = new ChromeDriver();

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/dotnet/SeleniumDocs/GettingStarted/FirstScript.cs#L11)

##### examples/dotnet/SeleniumDocs/GettingStarted/FirstScript.cs

Copy  Close               using System;     using OpenQA.Selenium;     using OpenQA.Selenium.Chrome;          namespace SeleniumDocs.GettingStarted;          public static class FirstScript     {         public static void Main()         {             IWebDriver driver = new ChromeDriver();                  driver.Navigate().GoToUrl("https://www.selenium.dev/selenium/web/web-form.html");                  var title = driver.Title;                  driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromMilliseconds(500);                  var textBox = driver.FindElement(By.Name("my-text"));             var submitButton = driver.FindElement(By.TagName("button"));                              textBox.SendKeys("Selenium");             submitButton.Click();                              var message = driver.FindElement(By.Id("message"));             var value = message.Text;                              driver.Quit();         }     }               driver = Selenium::WebDriver.for :chrome

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/ruby/spec/getting_started/first_script.rb#L3)

##### examples/ruby/spec/getting\_started/first\_script.rb

Copy  Close               require 'selenium-webdriver'          driver = Selenium::WebDriver.for :chrome          driver.get('https://www.selenium.dev/selenium/web/web-form.html')          driver.title          driver.manage.timeouts.implicit_wait = 500          text_box = driver.find_element(name: 'my-text')     submit_button = driver.find_element(tag_name: 'button')          text_box.send_keys('Selenium')     submit_button.click          message = driver.find_element(id: 'message')     message.text          driver.quit                        driver = await new Builder().forBrowser(Browser.CHROME).build();

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/javascript/test/getting_started/firstScript.spec.js#L8)

##### examples/javascript/test/getting\_started/firstScript.spec.js

Copy  Close               const {By, Builder, Browser} = require('selenium-webdriver');     const assert = require("assert");          (async function firstTest() {       let driver;              try {         driver = await new Builder().forBrowser(Browser.CHROME).build();         await driver.get('https://www.selenium.dev/selenium/web/web-form.html');                let title = await driver.getTitle();         assert.equal("Web form", title);                await driver.manage().setTimeouts({implicit: 500});                let textBox = await driver.findElement(By.name('my-text'));         let submitButton = await driver.findElement(By.css('button'));                await textBox.sendKeys('Selenium');         await submitButton.click();                let message = await driver.findElement(By.id('message'));         let value = await message.getText();         assert.equal("Received!", value);       } catch (e) {         console.log(e)       } finally {         await driver.quit();       }     }())                            driver = ChromeDriver()

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/kotlin/src/test/kotlin/dev/selenium/getting_started/FirstScriptTest.kt#L16)

##### examples/kotlin/src/test/kotlin/dev/selenium/getting\_started/FirstScriptTest.kt

Copy  Close               package dev.selenium.getting_started          import org.junit.jupiter.api.*     import org.junit.jupiter.api.Assertions.assertEquals     import org.openqa.selenium.By     import org.openqa.selenium.WebDriver     import org.openqa.selenium.chrome.ChromeDriver     import java.time.Duration          @TestInstance(TestInstance.Lifecycle.PER_CLASS)     class FirstScriptTest {         private lateinit var driver: WebDriver              @Test         fun eightComponents() {             driver = ChromeDriver()                  driver.get("https://www.selenium.dev/selenium/web/web-form.html")                  val title = driver.title             assertEquals("Web form", title)                  driver.manage().timeouts().implicitlyWait(Duration.ofMillis(500))                  var textBox = driver.findElement(By.name("my-text"))             val submitButton = driver.findElement(By.cssSelector("button"))                  textBox.sendKeys("Selenium")             submitButton.click()                  val message = driver.findElement(By.id("message"))             val value = message.getText()             assertEquals("Received!", value)                  driver.quit()         }          }

### 2\. Take action on browser

In this example we are [navigating](https://www.selenium.dev/documentation/webdriver/interactions/navigation/) to a web page.

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

                      driver.get("https://www.selenium.dev/selenium/web/web-form.html");

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/java/src/test/java/dev/selenium/getting_started/FirstScript.java#L14)

##### examples/java/src/test/java/dev/selenium/getting\_started/FirstScript.java

Copy  Close               package dev.selenium.getting_started;          import org.openqa.selenium.By;     import org.openqa.selenium.WebDriver;     import org.openqa.selenium.WebElement;     import org.openqa.selenium.chrome.ChromeDriver;          import java.time.Duration;          public class FirstScript {         public static void main(String[] args) {             WebDriver driver = new ChromeDriver();                  driver.get("https://www.selenium.dev/selenium/web/web-form.html");                  driver.getTitle();                  driver.manage().timeouts().implicitlyWait(Duration.ofMillis(500));                  WebElement textBox = driver.findElement(By.name("my-text"));             WebElement submitButton = driver.findElement(By.cssSelector("button"));                  textBox.sendKeys("Selenium");             submitButton.click();                  WebElement message = driver.findElement(By.id("message"));             message.getText();                  driver.quit();         }     }                    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/getting_started/first_script.py#L6)

##### examples/python/tests/getting\_started/first\_script.py

Copy  Close               from selenium import webdriver     from selenium.webdriver.common.by import By          driver = webdriver.Chrome()          driver.get("https://www.selenium.dev/selenium/web/web-form.html")          title = driver.title          driver.implicitly_wait(0.5)          text_box = driver.find_element(by=By.NAME, value="my-text")     submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")          text_box.send_keys("Selenium")     submit_button.click()          message = driver.find_element(by=By.ID, value="message")     text = message.text          driver.quit()                            driver.Navigate().GoToUrl("https://www.selenium.dev/selenium/web/web-form.html");

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/dotnet/SeleniumDocs/GettingStarted/FirstScript.cs#L13)

##### examples/dotnet/SeleniumDocs/GettingStarted/FirstScript.cs

Copy  Close               using System;     using OpenQA.Selenium;     using OpenQA.Selenium.Chrome;          namespace SeleniumDocs.GettingStarted;          public static class FirstScript     {         public static void Main()         {             IWebDriver driver = new ChromeDriver();                  driver.Navigate().GoToUrl("https://www.selenium.dev/selenium/web/web-form.html");                  var title = driver.Title;                  driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromMilliseconds(500);                  var textBox = driver.FindElement(By.Name("my-text"));             var submitButton = driver.FindElement(By.TagName("button"));                              textBox.SendKeys("Selenium");             submitButton.Click();                              var message = driver.FindElement(By.Id("message"));             var value = message.Text;                              driver.Quit();         }     }               driver.get('https://www.selenium.dev/selenium/web/web-form.html')

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/ruby/spec/getting_started/first_script.rb#L5)

##### examples/ruby/spec/getting\_started/first\_script.rb

Copy  Close               require 'selenium-webdriver'          driver = Selenium::WebDriver.for :chrome          driver.get('https://www.selenium.dev/selenium/web/web-form.html')          driver.title          driver.manage.timeouts.implicit_wait = 500          text_box = driver.find_element(name: 'my-text')     submit_button = driver.find_element(tag_name: 'button')          text_box.send_keys('Selenium')     submit_button.click          message = driver.find_element(id: 'message')     message.text          driver.quit                        await driver.get('https://www.selenium.dev/selenium/web/web-form.html');

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/javascript/test/getting_started/firstScript.spec.js#L9)

##### examples/javascript/test/getting\_started/firstScript.spec.js

Copy  Close               const {By, Builder, Browser} = require('selenium-webdriver');     const assert = require("assert");          (async function firstTest() {       let driver;              try {         driver = await new Builder().forBrowser(Browser.CHROME).build();         await driver.get('https://www.selenium.dev/selenium/web/web-form.html');                let title = await driver.getTitle();         assert.equal("Web form", title);                await driver.manage().setTimeouts({implicit: 500});                let textBox = await driver.findElement(By.name('my-text'));         let submitButton = await driver.findElement(By.css('button'));                await textBox.sendKeys('Selenium');         await submitButton.click();                let message = await driver.findElement(By.id('message'));         let value = await message.getText();         assert.equal("Received!", value);       } catch (e) {         console.log(e)       } finally {         await driver.quit();       }     }())                            driver.get("https://www.selenium.dev/selenium/web/web-form.html")

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/kotlin/src/test/kotlin/dev/selenium/getting_started/FirstScriptTest.kt#L18)

##### examples/kotlin/src/test/kotlin/dev/selenium/getting\_started/FirstScriptTest.kt

Copy  Close               package dev.selenium.getting_started          import org.junit.jupiter.api.*     import org.junit.jupiter.api.Assertions.assertEquals     import org.openqa.selenium.By     import org.openqa.selenium.WebDriver     import org.openqa.selenium.chrome.ChromeDriver     import java.time.Duration          @TestInstance(TestInstance.Lifecycle.PER_CLASS)     class FirstScriptTest {         private lateinit var driver: WebDriver              @Test         fun eightComponents() {             driver = ChromeDriver()                  driver.get("https://www.selenium.dev/selenium/web/web-form.html")                  val title = driver.title             assertEquals("Web form", title)                  driver.manage().timeouts().implicitlyWait(Duration.ofMillis(500))                  var textBox = driver.findElement(By.name("my-text"))             val submitButton = driver.findElement(By.cssSelector("button"))                  textBox.sendKeys("Selenium")             submitButton.click()                  val message = driver.findElement(By.id("message"))             val value = message.getText()             assertEquals("Received!", value)                  driver.quit()         }          }

### 3\. Request browser information

There are a bunch of types of [information about the browser](https://www.selenium.dev/documentation/webdriver/interactions/) you can request, including window handles, browser size / position, cookies, alerts, etc.

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

                      driver.getTitle();

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/java/src/test/java/dev/selenium/getting_started/FirstScript.java#16)

##### examples/java/src/test/java/dev/selenium/getting\_started/FirstScript.java

Copy  Close               package dev.selenium.getting_started;          import org.openqa.selenium.By;     import org.openqa.selenium.WebDriver;     import org.openqa.selenium.WebElement;     import org.openqa.selenium.chrome.ChromeDriver;          import java.time.Duration;          public class FirstScript {         public static void main(String[] args) {             WebDriver driver = new ChromeDriver();                  driver.get("https://www.selenium.dev/selenium/web/web-form.html");                  driver.getTitle();                  driver.manage().timeouts().implicitlyWait(Duration.ofMillis(500));                  WebElement textBox = driver.findElement(By.name("my-text"));             WebElement submitButton = driver.findElement(By.cssSelector("button"));                  textBox.sendKeys("Selenium");             submitButton.click();                  WebElement message = driver.findElement(By.id("message"));             message.getText();                  driver.quit();         }     }                    title = driver.title

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/getting_started/first_script.py#L8)

##### examples/python/tests/getting\_started/first\_script.py

Copy  Close               from selenium import webdriver     from selenium.webdriver.common.by import By          driver = webdriver.Chrome()          driver.get("https://www.selenium.dev/selenium/web/web-form.html")          title = driver.title          driver.implicitly_wait(0.5)          text_box = driver.find_element(by=By.NAME, value="my-text")     submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")          text_box.send_keys("Selenium")     submit_button.click()          message = driver.find_element(by=By.ID, value="message")     text = message.text          driver.quit()                            var title = driver.Title;

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/dotnet/SeleniumDocs/GettingStarted/FirstScript.cs#L15)

##### examples/dotnet/SeleniumDocs/GettingStarted/FirstScript.cs

Copy  Close               using System;     using OpenQA.Selenium;     using OpenQA.Selenium.Chrome;          namespace SeleniumDocs.GettingStarted;          public static class FirstScript     {         public static void Main()         {             IWebDriver driver = new ChromeDriver();                  driver.Navigate().GoToUrl("https://www.selenium.dev/selenium/web/web-form.html");                  var title = driver.Title;                  driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromMilliseconds(500);                  var textBox = driver.FindElement(By.Name("my-text"));             var submitButton = driver.FindElement(By.TagName("button"));                              textBox.SendKeys("Selenium");             submitButton.Click();                              var message = driver.FindElement(By.Id("message"));             var value = message.Text;                              driver.Quit();         }     }               driver.title

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/ruby/spec/getting_started/first_script.rb#L7)

##### examples/ruby/spec/getting\_started/first\_script.rb

Copy  Close               require 'selenium-webdriver'          driver = Selenium::WebDriver.for :chrome          driver.get('https://www.selenium.dev/selenium/web/web-form.html')          driver.title          driver.manage.timeouts.implicit_wait = 500          text_box = driver.find_element(name: 'my-text')     submit_button = driver.find_element(tag_name: 'button')          text_box.send_keys('Selenium')     submit_button.click          message = driver.find_element(id: 'message')     message.text          driver.quit                        let title = await driver.getTitle();

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/javascript/test/getting_started/firstScript.spec.js#L11)

##### examples/javascript/test/getting\_started/firstScript.spec.js

Copy  Close               const {By, Builder, Browser} = require('selenium-webdriver');     const assert = require("assert");          (async function firstTest() {       let driver;              try {         driver = await new Builder().forBrowser(Browser.CHROME).build();         await driver.get('https://www.selenium.dev/selenium/web/web-form.html');                let title = await driver.getTitle();         assert.equal("Web form", title);                await driver.manage().setTimeouts({implicit: 500});                let textBox = await driver.findElement(By.name('my-text'));         let submitButton = await driver.findElement(By.css('button'));                await textBox.sendKeys('Selenium');         await submitButton.click();                let message = await driver.findElement(By.id('message'));         let value = await message.getText();         assert.equal("Received!", value);       } catch (e) {         console.log(e)       } finally {         await driver.quit();       }     }())                            val title = driver.title

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/kotlin/src/test/kotlin/dev/selenium/getting_started/FirstScriptTest.kt#L20)

##### examples/kotlin/src/test/kotlin/dev/selenium/getting\_started/FirstScriptTest.kt

Copy  Close               package dev.selenium.getting_started          import org.junit.jupiter.api.*     import org.junit.jupiter.api.Assertions.assertEquals     import org.openqa.selenium.By     import org.openqa.selenium.WebDriver     import org.openqa.selenium.chrome.ChromeDriver     import java.time.Duration          @TestInstance(TestInstance.Lifecycle.PER_CLASS)     class FirstScriptTest {         private lateinit var driver: WebDriver              @Test         fun eightComponents() {             driver = ChromeDriver()                  driver.get("https://www.selenium.dev/selenium/web/web-form.html")                  val title = driver.title             assertEquals("Web form", title)                  driver.manage().timeouts().implicitlyWait(Duration.ofMillis(500))                  var textBox = driver.findElement(By.name("my-text"))             val submitButton = driver.findElement(By.cssSelector("button"))                  textBox.sendKeys("Selenium")             submitButton.click()                  val message = driver.findElement(By.id("message"))             val value = message.getText()             assertEquals("Received!", value)                  driver.quit()         }          }

### 4\. Establish Waiting Strategy

Synchronizing the code with the current state of the browser is one of the biggest challenges with Selenium, and doing it well is an advanced topic.

Essentially you want to make sure that the element is on the page before you attempt to locate it and the element is in an interactable state before you attempt to interact with it.

An implicit wait is rarely the best solution, but it’s the easiest to demonstrate here, so we’ll use it as a placeholder.

Read more about [Waiting strategies](https://www.selenium.dev/documentation/webdriver/waits/).

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

                      driver.manage().timeouts().implicitlyWait(Duration.ofMillis(500));

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/java/src/test/java/dev/selenium/getting_started/FirstScript.java#L18)

##### examples/java/src/test/java/dev/selenium/getting\_started/FirstScript.java

Copy  Close               package dev.selenium.getting_started;          import org.openqa.selenium.By;     import org.openqa.selenium.WebDriver;     import org.openqa.selenium.WebElement;     import org.openqa.selenium.chrome.ChromeDriver;          import java.time.Duration;          public class FirstScript {         public static void main(String[] args) {             WebDriver driver = new ChromeDriver();                  driver.get("https://www.selenium.dev/selenium/web/web-form.html");                  driver.getTitle();                  driver.manage().timeouts().implicitlyWait(Duration.ofMillis(500));                  WebElement textBox = driver.findElement(By.name("my-text"));             WebElement submitButton = driver.findElement(By.cssSelector("button"));                  textBox.sendKeys("Selenium");             submitButton.click();                  WebElement message = driver.findElement(By.id("message"));             message.getText();                  driver.quit();         }     }                    driver.implicitly_wait(0.5)

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/getting_started/first_script.py#L10)

##### examples/python/tests/getting\_started/first\_script.py

Copy  Close               from selenium import webdriver     from selenium.webdriver.common.by import By          driver = webdriver.Chrome()          driver.get("https://www.selenium.dev/selenium/web/web-form.html")          title = driver.title          driver.implicitly_wait(0.5)          text_box = driver.find_element(by=By.NAME, value="my-text")     submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")          text_box.send_keys("Selenium")     submit_button.click()          message = driver.find_element(by=By.ID, value="message")     text = message.text          driver.quit()                            driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromMilliseconds(500);

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/dotnet/SeleniumDocs/GettingStarted/FirstScript.cs#L17)

##### examples/dotnet/SeleniumDocs/GettingStarted/FirstScript.cs

Copy  Close               using System;     using OpenQA.Selenium;     using OpenQA.Selenium.Chrome;          namespace SeleniumDocs.GettingStarted;          public static class FirstScript     {         public static void Main()         {             IWebDriver driver = new ChromeDriver();                  driver.Navigate().GoToUrl("https://www.selenium.dev/selenium/web/web-form.html");                  var title = driver.Title;                  driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromMilliseconds(500);                  var textBox = driver.FindElement(By.Name("my-text"));             var submitButton = driver.FindElement(By.TagName("button"));                              textBox.SendKeys("Selenium");             submitButton.Click();                              var message = driver.FindElement(By.Id("message"));             var value = message.Text;                              driver.Quit();         }     }               driver.manage.timeouts.implicit_wait = 500

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/ruby/spec/getting_started/first_script.rb#L9)

##### examples/ruby/spec/getting\_started/first\_script.rb

Copy  Close               require 'selenium-webdriver'          driver = Selenium::WebDriver.for :chrome          driver.get('https://www.selenium.dev/selenium/web/web-form.html')          driver.title          driver.manage.timeouts.implicit_wait = 500          text_box = driver.find_element(name: 'my-text')     submit_button = driver.find_element(tag_name: 'button')          text_box.send_keys('Selenium')     submit_button.click          message = driver.find_element(id: 'message')     message.text          driver.quit                        await driver.manage().setTimeouts({implicit: 500});

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/javascript/test/getting_started/firstScript.spec.js#L14)

##### examples/javascript/test/getting\_started/firstScript.spec.js

Copy  Close               const {By, Builder, Browser} = require('selenium-webdriver');     const assert = require("assert");          (async function firstTest() {       let driver;              try {         driver = await new Builder().forBrowser(Browser.CHROME).build();         await driver.get('https://www.selenium.dev/selenium/web/web-form.html');                let title = await driver.getTitle();         assert.equal("Web form", title);                await driver.manage().setTimeouts({implicit: 500});                let textBox = await driver.findElement(By.name('my-text'));         let submitButton = await driver.findElement(By.css('button'));                await textBox.sendKeys('Selenium');         await submitButton.click();                let message = await driver.findElement(By.id('message'));         let value = await message.getText();         assert.equal("Received!", value);       } catch (e) {         console.log(e)       } finally {         await driver.quit();       }     }())                            driver.manage().timeouts().implicitlyWait(Duration.ofMillis(500))

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/kotlin/src/test/kotlin/dev/selenium/getting_started/FirstScriptTest.kt#L23)

##### examples/kotlin/src/test/kotlin/dev/selenium/getting\_started/FirstScriptTest.kt

Copy  Close               package dev.selenium.getting_started          import org.junit.jupiter.api.*     import org.junit.jupiter.api.Assertions.assertEquals     import org.openqa.selenium.By     import org.openqa.selenium.WebDriver     import org.openqa.selenium.chrome.ChromeDriver     import java.time.Duration          @TestInstance(TestInstance.Lifecycle.PER_CLASS)     class FirstScriptTest {         private lateinit var driver: WebDriver              @Test         fun eightComponents() {             driver = ChromeDriver()                  driver.get("https://www.selenium.dev/selenium/web/web-form.html")                  val title = driver.title             assertEquals("Web form", title)                  driver.manage().timeouts().implicitlyWait(Duration.ofMillis(500))                  var textBox = driver.findElement(By.name("my-text"))             val submitButton = driver.findElement(By.cssSelector("button"))                  textBox.sendKeys("Selenium")             submitButton.click()                  val message = driver.findElement(By.id("message"))             val value = message.getText()             assertEquals("Received!", value)                  driver.quit()         }          }

### 5\. Find an element

The majority of commands in most Selenium sessions are element related, and you can’t interact with one without first [finding an element](https://www.selenium.dev/documentation/webdriver/elements/)

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

                      WebElement textBox = driver.findElement(By.name("my-text"));             WebElement submitButton = driver.findElement(By.cssSelector("button"));

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/java/src/test/java/dev/selenium/getting_started/FirstScript.java#L20-L21)

##### examples/java/src/test/java/dev/selenium/getting\_started/FirstScript.java

Copy  Close               package dev.selenium.getting_started;          import org.openqa.selenium.By;     import org.openqa.selenium.WebDriver;     import org.openqa.selenium.WebElement;     import org.openqa.selenium.chrome.ChromeDriver;          import java.time.Duration;          public class FirstScript {         public static void main(String[] args) {             WebDriver driver = new ChromeDriver();                  driver.get("https://www.selenium.dev/selenium/web/web-form.html");                  driver.getTitle();                  driver.manage().timeouts().implicitlyWait(Duration.ofMillis(500));                  WebElement textBox = driver.findElement(By.name("my-text"));             WebElement submitButton = driver.findElement(By.cssSelector("button"));                  textBox.sendKeys("Selenium");             submitButton.click();                  WebElement message = driver.findElement(By.id("message"));             message.getText();                  driver.quit();         }     }                    text_box = driver.find_element(by=By.NAME, value="my-text")     submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/getting_started/first_script.py#L12-L13)

##### examples/python/tests/getting\_started/first\_script.py

Copy  Close               from selenium import webdriver     from selenium.webdriver.common.by import By          driver = webdriver.Chrome()          driver.get("https://www.selenium.dev/selenium/web/web-form.html")          title = driver.title          driver.implicitly_wait(0.5)          text_box = driver.find_element(by=By.NAME, value="my-text")     submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")          text_box.send_keys("Selenium")     submit_button.click()          message = driver.find_element(by=By.ID, value="message")     text = message.text          driver.quit()                            var textBox = driver.FindElement(By.Name("my-text"));             var submitButton = driver.FindElement(By.TagName("button"));

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/dotnet/SeleniumDocs/GettingStarted/FirstScript.cs#L19-L20)

##### examples/dotnet/SeleniumDocs/GettingStarted/FirstScript.cs

Copy  Close               using System;     using OpenQA.Selenium;     using OpenQA.Selenium.Chrome;          namespace SeleniumDocs.GettingStarted;          public static class FirstScript     {         public static void Main()         {             IWebDriver driver = new ChromeDriver();                  driver.Navigate().GoToUrl("https://www.selenium.dev/selenium/web/web-form.html");                  var title = driver.Title;                  driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromMilliseconds(500);                  var textBox = driver.FindElement(By.Name("my-text"));             var submitButton = driver.FindElement(By.TagName("button"));                              textBox.SendKeys("Selenium");             submitButton.Click();                              var message = driver.FindElement(By.Id("message"));             var value = message.Text;                              driver.Quit();         }     }               text_box = driver.find_element(name: 'my-text')     submit_button = driver.find_element(tag_name: 'button')

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/ruby/spec/getting_started/first_script.rb#L11-L12)

##### examples/ruby/spec/getting\_started/first\_script.rb

Copy  Close               require 'selenium-webdriver'          driver = Selenium::WebDriver.for :chrome          driver.get('https://www.selenium.dev/selenium/web/web-form.html')          driver.title          driver.manage.timeouts.implicit_wait = 500          text_box = driver.find_element(name: 'my-text')     submit_button = driver.find_element(tag_name: 'button')          text_box.send_keys('Selenium')     submit_button.click          message = driver.find_element(id: 'message')     message.text          driver.quit                        let textBox = await driver.findElement(By.name('my-text'));         let submitButton = await driver.findElement(By.css('button'));

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/javascript/test/getting_started/firstScript.spec.js#L16-L17)

##### examples/javascript/test/getting\_started/firstScript.spec.js

Copy  Close               const {By, Builder, Browser} = require('selenium-webdriver');     const assert = require("assert");          (async function firstTest() {       let driver;              try {         driver = await new Builder().forBrowser(Browser.CHROME).build();         await driver.get('https://www.selenium.dev/selenium/web/web-form.html');                let title = await driver.getTitle();         assert.equal("Web form", title);                await driver.manage().setTimeouts({implicit: 500});                let textBox = await driver.findElement(By.name('my-text'));         let submitButton = await driver.findElement(By.css('button'));                await textBox.sendKeys('Selenium');         await submitButton.click();                let message = await driver.findElement(By.id('message'));         let value = await message.getText();         assert.equal("Received!", value);       } catch (e) {         console.log(e)       } finally {         await driver.quit();       }     }())                            var textBox = driver.findElement(By.name("my-text"))             val submitButton = driver.findElement(By.cssSelector("button"))

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/kotlin/src/test/kotlin/dev/selenium/getting_started/FirstScriptTest.kt#L25-L26)

##### examples/kotlin/src/test/kotlin/dev/selenium/getting\_started/FirstScriptTest.kt

Copy  Close               package dev.selenium.getting_started          import org.junit.jupiter.api.*     import org.junit.jupiter.api.Assertions.assertEquals     import org.openqa.selenium.By     import org.openqa.selenium.WebDriver     import org.openqa.selenium.chrome.ChromeDriver     import java.time.Duration          @TestInstance(TestInstance.Lifecycle.PER_CLASS)     class FirstScriptTest {         private lateinit var driver: WebDriver              @Test         fun eightComponents() {             driver = ChromeDriver()                  driver.get("https://www.selenium.dev/selenium/web/web-form.html")                  val title = driver.title             assertEquals("Web form", title)                  driver.manage().timeouts().implicitlyWait(Duration.ofMillis(500))                  var textBox = driver.findElement(By.name("my-text"))             val submitButton = driver.findElement(By.cssSelector("button"))                  textBox.sendKeys("Selenium")             submitButton.click()                  val message = driver.findElement(By.id("message"))             val value = message.getText()             assertEquals("Received!", value)                  driver.quit()         }          }

### 6\. Take action on element

There are only a handful of [actions to take on an element](https://www.selenium.dev/documentation/webdriver/elements/interactions/), but you will use them frequently.

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

                      textBox.sendKeys("Selenium");             submitButton.click();

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/java/src/test/java/dev/selenium/getting_started/FirstScript.java#L23-L24)

##### examples/java/src/test/java/dev/selenium/getting\_started/FirstScript.java

Copy  Close               package dev.selenium.getting_started;          import org.openqa.selenium.By;     import org.openqa.selenium.WebDriver;     import org.openqa.selenium.WebElement;     import org.openqa.selenium.chrome.ChromeDriver;          import java.time.Duration;          public class FirstScript {         public static void main(String[] args) {             WebDriver driver = new ChromeDriver();                  driver.get("https://www.selenium.dev/selenium/web/web-form.html");                  driver.getTitle();                  driver.manage().timeouts().implicitlyWait(Duration.ofMillis(500));                  WebElement textBox = driver.findElement(By.name("my-text"));             WebElement submitButton = driver.findElement(By.cssSelector("button"));                  textBox.sendKeys("Selenium");             submitButton.click();                  WebElement message = driver.findElement(By.id("message"));             message.getText();                  driver.quit();         }     }                    text_box.send_keys("Selenium")     submit_button.click()

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/getting_started/first_script.py#L15-L16)

##### examples/python/tests/getting\_started/first\_script.py

Copy  Close               from selenium import webdriver     from selenium.webdriver.common.by import By          driver = webdriver.Chrome()          driver.get("https://www.selenium.dev/selenium/web/web-form.html")          title = driver.title          driver.implicitly_wait(0.5)          text_box = driver.find_element(by=By.NAME, value="my-text")     submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")          text_box.send_keys("Selenium")     submit_button.click()          message = driver.find_element(by=By.ID, value="message")     text = message.text          driver.quit()                            textBox.SendKeys("Selenium");             submitButton.Click();

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/dotnet/SeleniumDocs/GettingStarted/FirstScript.cs#L22-L23)

##### examples/dotnet/SeleniumDocs/GettingStarted/FirstScript.cs

Copy  Close               using System;     using OpenQA.Selenium;     using OpenQA.Selenium.Chrome;          namespace SeleniumDocs.GettingStarted;          public static class FirstScript     {         public static void Main()         {             IWebDriver driver = new ChromeDriver();                  driver.Navigate().GoToUrl("https://www.selenium.dev/selenium/web/web-form.html");                  var title = driver.Title;                  driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromMilliseconds(500);                  var textBox = driver.FindElement(By.Name("my-text"));             var submitButton = driver.FindElement(By.TagName("button"));                              textBox.SendKeys("Selenium");             submitButton.Click();                              var message = driver.FindElement(By.Id("message"));             var value = message.Text;                              driver.Quit();         }     }               text_box.send_keys('Selenium')     submit_button.click

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/ruby/spec/getting_started/first_script.rb#L14-L15)

##### examples/ruby/spec/getting\_started/first\_script.rb

Copy  Close               require 'selenium-webdriver'          driver = Selenium::WebDriver.for :chrome          driver.get('https://www.selenium.dev/selenium/web/web-form.html')          driver.title          driver.manage.timeouts.implicit_wait = 500          text_box = driver.find_element(name: 'my-text')     submit_button = driver.find_element(tag_name: 'button')          text_box.send_keys('Selenium')     submit_button.click          message = driver.find_element(id: 'message')     message.text          driver.quit                        await textBox.sendKeys('Selenium');         await submitButton.click();

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/javascript/test/getting_started/firstScript.spec.js#L19-L20)

##### examples/javascript/test/getting\_started/firstScript.spec.js

Copy  Close               const {By, Builder, Browser} = require('selenium-webdriver');     const assert = require("assert");          (async function firstTest() {       let driver;              try {         driver = await new Builder().forBrowser(Browser.CHROME).build();         await driver.get('https://www.selenium.dev/selenium/web/web-form.html');                let title = await driver.getTitle();         assert.equal("Web form", title);                await driver.manage().setTimeouts({implicit: 500});                let textBox = await driver.findElement(By.name('my-text'));         let submitButton = await driver.findElement(By.css('button'));                await textBox.sendKeys('Selenium');         await submitButton.click();                let message = await driver.findElement(By.id('message'));         let value = await message.getText();         assert.equal("Received!", value);       } catch (e) {         console.log(e)       } finally {         await driver.quit();       }     }())                            textBox.sendKeys("Selenium")             submitButton.click()

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/kotlin/src/test/kotlin/dev/selenium/getting_started/FirstScriptTest.kt#L28-L29)

##### examples/kotlin/src/test/kotlin/dev/selenium/getting\_started/FirstScriptTest.kt

Copy  Close               package dev.selenium.getting_started          import org.junit.jupiter.api.*     import org.junit.jupiter.api.Assertions.assertEquals     import org.openqa.selenium.By     import org.openqa.selenium.WebDriver     import org.openqa.selenium.chrome.ChromeDriver     import java.time.Duration          @TestInstance(TestInstance.Lifecycle.PER_CLASS)     class FirstScriptTest {         private lateinit var driver: WebDriver              @Test         fun eightComponents() {             driver = ChromeDriver()                  driver.get("https://www.selenium.dev/selenium/web/web-form.html")                  val title = driver.title             assertEquals("Web form", title)                  driver.manage().timeouts().implicitlyWait(Duration.ofMillis(500))                  var textBox = driver.findElement(By.name("my-text"))             val submitButton = driver.findElement(By.cssSelector("button"))                  textBox.sendKeys("Selenium")             submitButton.click()                  val message = driver.findElement(By.id("message"))             val value = message.getText()             assertEquals("Received!", value)                  driver.quit()         }          }

### 7\. Request element information

Elements store a lot of [information that can be requested](https://www.selenium.dev/documentation/webdriver/elements/information/).

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

                      WebElement message = driver.findElement(By.id("message"));             message.getText();

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/java/src/test/java/dev/selenium/getting_started/FirstScript.java#L26-27)

##### examples/java/src/test/java/dev/selenium/getting\_started/FirstScript.java

Copy  Close               package dev.selenium.getting_started;          import org.openqa.selenium.By;     import org.openqa.selenium.WebDriver;     import org.openqa.selenium.WebElement;     import org.openqa.selenium.chrome.ChromeDriver;          import java.time.Duration;          public class FirstScript {         public static void main(String[] args) {             WebDriver driver = new ChromeDriver();                  driver.get("https://www.selenium.dev/selenium/web/web-form.html");                  driver.getTitle();                  driver.manage().timeouts().implicitlyWait(Duration.ofMillis(500));                  WebElement textBox = driver.findElement(By.name("my-text"));             WebElement submitButton = driver.findElement(By.cssSelector("button"));                  textBox.sendKeys("Selenium");             submitButton.click();                  WebElement message = driver.findElement(By.id("message"));             message.getText();                  driver.quit();         }     }                    message = driver.find_element(by=By.ID, value="message")     text = message.text

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/getting_started/first_script.py#L18-19)

##### examples/python/tests/getting\_started/first\_script.py

Copy  Close               from selenium import webdriver     from selenium.webdriver.common.by import By          driver = webdriver.Chrome()          driver.get("https://www.selenium.dev/selenium/web/web-form.html")          title = driver.title          driver.implicitly_wait(0.5)          text_box = driver.find_element(by=By.NAME, value="my-text")     submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")          text_box.send_keys("Selenium")     submit_button.click()          message = driver.find_element(by=By.ID, value="message")     text = message.text          driver.quit()                            var message = driver.FindElement(By.Id("message"));             var value = message.Text;

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/dotnet/SeleniumDocs/GettingStarted/FirstScript.cs#L25-26)

##### examples/dotnet/SeleniumDocs/GettingStarted/FirstScript.cs

Copy  Close               using System;     using OpenQA.Selenium;     using OpenQA.Selenium.Chrome;          namespace SeleniumDocs.GettingStarted;          public static class FirstScript     {         public static void Main()         {             IWebDriver driver = new ChromeDriver();                  driver.Navigate().GoToUrl("https://www.selenium.dev/selenium/web/web-form.html");                  var title = driver.Title;                  driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromMilliseconds(500);                  var textBox = driver.FindElement(By.Name("my-text"));             var submitButton = driver.FindElement(By.TagName("button"));                              textBox.SendKeys("Selenium");             submitButton.Click();                              var message = driver.FindElement(By.Id("message"));             var value = message.Text;                              driver.Quit();         }     }               message = driver.find_element(id: 'message')     message.text

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/ruby/spec/getting_started/first_script.rb#L17-18)

##### examples/ruby/spec/getting\_started/first\_script.rb

Copy  Close               require 'selenium-webdriver'          driver = Selenium::WebDriver.for :chrome          driver.get('https://www.selenium.dev/selenium/web/web-form.html')          driver.title          driver.manage.timeouts.implicit_wait = 500          text_box = driver.find_element(name: 'my-text')     submit_button = driver.find_element(tag_name: 'button')          text_box.send_keys('Selenium')     submit_button.click          message = driver.find_element(id: 'message')     message.text          driver.quit                        let message = await driver.findElement(By.id('message'));         let value = await message.getText();

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/javascript/test/getting_started/firstScript.spec.js#L22-23)

##### examples/javascript/test/getting\_started/firstScript.spec.js

Copy  Close               const {By, Builder, Browser} = require('selenium-webdriver');     const assert = require("assert");          (async function firstTest() {       let driver;              try {         driver = await new Builder().forBrowser(Browser.CHROME).build();         await driver.get('https://www.selenium.dev/selenium/web/web-form.html');                let title = await driver.getTitle();         assert.equal("Web form", title);                await driver.manage().setTimeouts({implicit: 500});                let textBox = await driver.findElement(By.name('my-text'));         let submitButton = await driver.findElement(By.css('button'));                await textBox.sendKeys('Selenium');         await submitButton.click();                let message = await driver.findElement(By.id('message'));         let value = await message.getText();         assert.equal("Received!", value);       } catch (e) {         console.log(e)       } finally {         await driver.quit();       }     }())                            val message = driver.findElement(By.id("message"))             val value = message.getText()

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/kotlin/src/test/kotlin/dev/selenium/getting_started/FirstScriptTest.kt#L31-32)

##### examples/kotlin/src/test/kotlin/dev/selenium/getting\_started/FirstScriptTest.kt

Copy  Close               package dev.selenium.getting_started          import org.junit.jupiter.api.*     import org.junit.jupiter.api.Assertions.assertEquals     import org.openqa.selenium.By     import org.openqa.selenium.WebDriver     import org.openqa.selenium.chrome.ChromeDriver     import java.time.Duration          @TestInstance(TestInstance.Lifecycle.PER_CLASS)     class FirstScriptTest {         private lateinit var driver: WebDriver              @Test         fun eightComponents() {             driver = ChromeDriver()                  driver.get("https://www.selenium.dev/selenium/web/web-form.html")                  val title = driver.title             assertEquals("Web form", title)                  driver.manage().timeouts().implicitlyWait(Duration.ofMillis(500))                  var textBox = driver.findElement(By.name("my-text"))             val submitButton = driver.findElement(By.cssSelector("button"))                  textBox.sendKeys("Selenium")             submitButton.click()                  val message = driver.findElement(By.id("message"))             val value = message.getText()             assertEquals("Received!", value)                  driver.quit()         }          }

### 8\. End the session

This ends the driver process, which by default closes the browser as well. No more commands can be sent to this driver instance. See [Quitting Sessions](https://www.selenium.dev/documentation/webdriver/drivers/#quitting-sessions).

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

                      driver.quit();

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/java/src/test/java/dev/selenium/getting_started/FirstScript.java#L29)

##### examples/java/src/test/java/dev/selenium/getting\_started/FirstScript.java

Copy  Close               package dev.selenium.getting_started;          import org.openqa.selenium.By;     import org.openqa.selenium.WebDriver;     import org.openqa.selenium.WebElement;     import org.openqa.selenium.chrome.ChromeDriver;          import java.time.Duration;          public class FirstScript {         public static void main(String[] args) {             WebDriver driver = new ChromeDriver();                  driver.get("https://www.selenium.dev/selenium/web/web-form.html");                  driver.getTitle();                  driver.manage().timeouts().implicitlyWait(Duration.ofMillis(500));                  WebElement textBox = driver.findElement(By.name("my-text"));             WebElement submitButton = driver.findElement(By.cssSelector("button"));                  textBox.sendKeys("Selenium");             submitButton.click();                  WebElement message = driver.findElement(By.id("message"));             message.getText();                  driver.quit();         }     }                    driver.quit()

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/getting_started/first_script.py#L21)

##### examples/python/tests/getting\_started/first\_script.py

Copy  Close               from selenium import webdriver     from selenium.webdriver.common.by import By          driver = webdriver.Chrome()          driver.get("https://www.selenium.dev/selenium/web/web-form.html")          title = driver.title          driver.implicitly_wait(0.5)          text_box = driver.find_element(by=By.NAME, value="my-text")     submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")          text_box.send_keys("Selenium")     submit_button.click()          message = driver.find_element(by=By.ID, value="message")     text = message.text          driver.quit()                            driver.Quit();

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/dotnet/SeleniumDocs/GettingStarted/FirstScript.cs#L28)

##### examples/dotnet/SeleniumDocs/GettingStarted/FirstScript.cs

Copy  Close               using System;     using OpenQA.Selenium;     using OpenQA.Selenium.Chrome;          namespace SeleniumDocs.GettingStarted;          public static class FirstScript     {         public static void Main()         {             IWebDriver driver = new ChromeDriver();                  driver.Navigate().GoToUrl("https://www.selenium.dev/selenium/web/web-form.html");                  var title = driver.Title;                  driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromMilliseconds(500);                  var textBox = driver.FindElement(By.Name("my-text"));             var submitButton = driver.FindElement(By.TagName("button"));                              textBox.SendKeys("Selenium");             submitButton.Click();                              var message = driver.FindElement(By.Id("message"));             var value = message.Text;                              driver.Quit();         }     }               driver.quit

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/ruby/spec/getting_started/first_script.rb#L20)

##### examples/ruby/spec/getting\_started/first\_script.rb

Copy  Close               require 'selenium-webdriver'          driver = Selenium::WebDriver.for :chrome          driver.get('https://www.selenium.dev/selenium/web/web-form.html')          driver.title          driver.manage.timeouts.implicit_wait = 500          text_box = driver.find_element(name: 'my-text')     submit_button = driver.find_element(tag_name: 'button')          text_box.send_keys('Selenium')     submit_button.click          message = driver.find_element(id: 'message')     message.text          driver.quit                        await driver.quit();

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/javascript/test/getting_started/firstScript.spec.js#L28)

##### examples/javascript/test/getting\_started/firstScript.spec.js

Copy  Close               const {By, Builder, Browser} = require('selenium-webdriver');     const assert = require("assert");          (async function firstTest() {       let driver;              try {         driver = await new Builder().forBrowser(Browser.CHROME).build();         await driver.get('https://www.selenium.dev/selenium/web/web-form.html');                let title = await driver.getTitle();         assert.equal("Web form", title);                await driver.manage().setTimeouts({implicit: 500});                let textBox = await driver.findElement(By.name('my-text'));         let submitButton = await driver.findElement(By.css('button'));                await textBox.sendKeys('Selenium');         await submitButton.click();                let message = await driver.findElement(By.id('message'));         let value = await message.getText();         assert.equal("Received!", value);       } catch (e) {         console.log(e)       } finally {         await driver.quit();       }     }())                            driver.quit()

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/kotlin/src/test/kotlin/dev/selenium/getting_started/FirstScriptTest.kt#L35)

##### examples/kotlin/src/test/kotlin/dev/selenium/getting\_started/FirstScriptTest.kt

Copy  Close               package dev.selenium.getting_started          import org.junit.jupiter.api.*     import org.junit.jupiter.api.Assertions.assertEquals     import org.openqa.selenium.By     import org.openqa.selenium.WebDriver     import org.openqa.selenium.chrome.ChromeDriver     import java.time.Duration          @TestInstance(TestInstance.Lifecycle.PER_CLASS)     class FirstScriptTest {         private lateinit var driver: WebDriver              @Test         fun eightComponents() {             driver = ChromeDriver()                  driver.get("https://www.selenium.dev/selenium/web/web-form.html")                  val title = driver.title             assertEquals("Web form", title)                  driver.manage().timeouts().implicitlyWait(Duration.ofMillis(500))                  var textBox = driver.findElement(By.name("my-text"))             val submitButton = driver.findElement(By.cssSelector("button"))                  textBox.sendKeys("Selenium")             submitButton.click()                  val message = driver.findElement(By.id("message"))             val value = message.getText()             assertEquals("Received!", value)                  driver.quit()         }          }

## Running Selenium File

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

              mvn exec:java -D"exec.mainClass"="dev.selenium.getting_started.FirstScript" -D"exec.classpathScope"=test

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/java/README.md#L60)

##### examples/java/README.md

Copy  Close               # Running Selenium Java Tests     The following steps will guide you on how to      run Selenium Java tests using a repository      of `SeleniumHQ/seleniumhq.github.io` examples.          ## Initial Setup          ### Prerequisites          Ensure that Java Development Kit (JDK) and Maven      are installed on your system. If they are not installed,      you will need to download and install them. You can      find detailed installation guides for both on their      respective official sites.          ### Clone the repository     First, we need to get the Selenium Java examples      on your local machine. This can be done by      cloning the `SeleniumHQ/seleniumhq.github.io` Git repository.      Run the following command in your terminal:          ```bash     git clone https://github.com/SeleniumHQ/seleniumhq.github.io.git     ```     ## Navigate to the java directory     After cloning the repository, navigate into the      directory where the Selenium Java examples are      located. Run the following command:          ```bash     cd seleniumhq.github.io/examples/java     ```          ## Running the Tests     ### Install dependencies     Before running the tests, we need to install all      necessary dependencies. Maven, a software      project management tool, can do this for us.      Run the following command:          ```bash     mvn test-compile     ```          ### Run all tests     To verify if everything is installed correctly and      functioning properly, we should run all      available tests. This can be done with the following command:          ```bash     mvn test     ```          Please be patient! If this is your first time running these tests,      it might take a while to download and verify all necessary browser drivers.          ## Execute a specific example     To run a specific Selenium Java example, use the following command:     ```bash     mvn exec:java -D"exec.mainClass"="dev.selenium.getting_started.FirstScript" -D"exec.classpathScope"=test     ```          Make sure to replace `dev.selenium.getting_started.FirstScript` with the path and name of the example you want to run.               ```

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/README.md#L35)

##### examples/python/README.md

Copy  Close               # Running tests from Selenium Python examples          #### 1. Clone this repository          ```     git clone https://github.com/SeleniumHQ/seleniumhq.github.io.git     ```          #### 2. Navigate to `python` directory          ```     cd seleniumhq.github.io/examples/python     ```          #### 3. Create a virtual environment          - On Windows:          ```     py -m venv venv     venv\Scripts\activate     ```          - On Linux/Mac:          ```     python3 -m venv venv     source venv/bin/activate     ```          #### 4. Install dependencies:          ```     pip install -r requirements.txt     ```          > for help, see: https://packaging.python.org/en/latest/tutorials/installing-packages          #### 5. Run tests          - Run all tests with the default Python interpreter:          ```     pytest     ```          - Run all tests with every installed/supported Python interpreter:          ```     tox     ```          > Please have some patience - If you are doing it for the first time, it will take a little while to download the browser drivers          - Run a specific example:          ```     pytest path/to/test_script.py     ```          > Make sure to replace `path/to/test_script.py` with the path and name of the example you want to run     

[Add Example](https://www.selenium.dev/documentation/about/contributing/#creating-examples)               ruby example_script.rb

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/ruby/README.md#L36)

##### examples/ruby/README.md

Copy  Close               # Running all tests from Selenium ruby example          Follow these steps to run all test example from selenium ruby          1. Clone this repository          ```     git clone https://github.com/SeleniumHQ/seleniumhq.github.io.git     ```          2. Navigate to `ruby` directory          ```     cd seleniumhq.github.io/examples/ruby     ```          3. Install dependencies using bundler          ```     bundler install     ```          4. Run all tests          ```     bundle exec rspec     ```          > Please keep some patience - If you are doing it for the first time, it will take a little while to verify and download the browser drivers          # Execute a ruby script          Use this command to run a ruby script and follow the first script example          ```     ruby example_script.rb     ```               node example_script.spec.js

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/javascript/README.md#L36)

##### examples/javascript/README.md

Copy  Close               # Running all tests from Selenium javascript example          Follow these steps to run all test example from selenium javascript          1. Clone this repository          ```     git clone https://github.com/SeleniumHQ/seleniumhq.github.io.git     ```          2. Navigate to `javascript` directory          ```     cd seleniumhq.github.io/examples/javascript     ```          3. Install dependencies using node          ```     npm install     ```          4. Run all all tests          ```     npm test     ```          > Please keep some patience - If you are doing it for the first time, it will take a little while to verify and download the browser drivers          # Execute a javascript test          Use this command to run a JavaScript and follow the first script example          ```     node example_script.spec.js     ```

[Add Example](https://www.selenium.dev/documentation/about/contributing/#creating-examples)

## Next Steps

Most Selenium users execute many sessions and need to organize them to minimize duplication and keep the code more maintainable. Read on to learn about how to put this code into context for your use case with [Using Selenium](https://www.selenium.dev/documentation/webdriver/getting_started/using_selenium/).

Last modified March 9, 2025: [fix line numbers for first script \[deploy site\] \(7eecdbd24e6\)](https://github.com/SeleniumHQ/seleniumhq.github.io/commit/7eecdbd24e6cf7c51288118d70a2e988c010bf25)