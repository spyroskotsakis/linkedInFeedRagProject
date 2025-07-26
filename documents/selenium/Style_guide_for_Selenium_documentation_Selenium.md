# Style guide for Selenium documentation | Selenium

**URL:** https://www.selenium.dev/documentation/about/style
**Word Count:** 825
**Links Count:** 217
**Scraped:** 2025-07-17 06:13:37
**Status:** completed

---

# Style guide for Selenium documentation

Conventions for contributions to the Selenium documentation and code examples

Read our [contributing documentation](https://www.selenium.dev/documentation/about/contributing/) for complete instructions on how to add content to this documentation.

## Alerts

Alerts have been added to direct potential contributors to where specific content is missing.               {{< alert-content />}}

or               {{< alert-content >}}     Additional information about what specific content is needed     {{< /alert-content >}}

Which gets displayed like this:

## Content Help

**Note:** This section needs additional and/or updated content      Additional information about what specific content is needed      Check our [contribution guidelines](https://www.selenium.dev/documentation/about/contributing/) if you’d like to help.

## Capitalization of titles

Our documentation uses Title Capitalization for `linkTitle` which should be short and Sentence capitalization for `title` which can be longer and more descriptive. For example, a `linkTitle` of _Special Heading_ might have a `title` of _The importance of a special heading in documentation_

## Line length

When editing the documentation’s source, which is written in plain HTML, limit your line lengths to around 100 characters.

Some of us take this one step further and use what is called [_semantic linefeeds_](https://rhodesmill.org/brandon/2012/one-sentence-per-line), which is a technique whereby the HTML source lines, which are not read by the public, are split at ‘natural breaks’ in the prose. In other words, sentences are split at natural breaks between clauses. Instead of fussing with the lines of each paragraph so that they all end near the right margin, linefeeds can be added anywhere that there is a break between ideas.

This can make diffs very easy to read when collaborating through git, but it is not something we enforce contributors to use.

## Translations

Selenium now has official translators for each of the supported languages.

  * If you add a code example to the `important_documentation.en.md` file, also add it to `important_documentation.ja.md`, `important_documentation.pt-br.md`, `important_documentation.zh-cn.md`.   * If you make text changes in the English version, just make a Pull Request. The new process is for issues to be created and tagged as needs translation based on changes made in a given PR.

## Code examples

All references to code should be language independent, and the code itself should be placed inside code tabs.

### Default Code Tabs

The Docsy code tabs look like this:

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

              WebDriver driver = new ChromeDriver();               driver = webdriver.Chrome()               var driver = new ChromeDriver();               driver = Selenium::WebDriver.for :chrome               let driver = await new Builder().forBrowser('chrome').build();               val driver = ChromeDriver()

To generate the above tabs, this is what you need to write. Note that the `tabpane` includes `langEqualsHeader=true`. This auto-formats the code in each tab to match the header name, and ensures that all tabs on the page with a language are set to the same thing.               {{< tabpane langEqualsHeader=true >}}       {{< tab header="Java" >}}         WebDriver driver = new ChromeDriver();       {{< /tab >}}       {{< tab header="Python" >}}         driver = webdriver.Chrome()       {{< /tab >}}       {{< tab header="CSharp" >}}         var driver = new ChromeDriver();       {{< /tab >}}       {{< tab header="Ruby" >}}         driver = Selenium::WebDriver.for :chrome       {{< /tab >}}       {{< tab header="JavaScript" >}}         let driver = await new Builder().forBrowser('chrome').build();       {{< /tab >}}       {{< tab header="Kotlin" >}}         val driver = ChromeDriver()       {{< /tab >}}     {{< /tabpane >}}     

#### Reference GitHub Examples

To ensure that all code is kept up to date, our goal is to write the code in the repo where it can be executed when Selenium versions are updated to ensure that everything is correct.

All code examples to be in our [example directories](https://github.com/SeleniumHQ/seleniumhq.github.io/tree/dev/examples).

This code can be automatically displayed in the documentation using the `gh-codeblock` shortcode. The shortcode automatically generates its own html, so we do not want it to auto-format with the language header. If all tabs are using this shortcode, set `text=true` in the `tabpane` and remove `langEqualsHeader=true`. If only some tabs are using this shortcode, keep `langEqualsHeader=true` in the `tabpane` and add `text=true` to the `tab`. Note that the `gh-codeblock` line can not be indented at all.

One great thing about using `gh-codeblock` is that it adds a link to the full example. This means you don’t have to include any additional context code, just the line\(s\) that are needed, and the user can navigate to the repo to see how to use it.

A basic comparison of code looks like:               {{< tabpane text=true >}}     {{< tab header="Java" >}}     {{< gh-codeblock path="examples/java/src/test/java/dev/selenium/getting_started/FirstScript.java#L26-L27" >}}     {{< /tab >}}     {{< tab header="Python" >}}     {{< gh-codeblock path="examples/python/tests/getting_started/first_script.py#L18-L19" >}}     {{< /tab >}}     {{< tab header="CSharp" >}}     {{< gh-codeblock path="examples/dotnet/SeleniumDocs/GettingStarted/FirstScript.cs#L25-L26" >}}     {{< /tab >}}     {{< tab header="Ruby" >}}     {{< gh-codeblock path="examples/ruby/spec/getting_started/first_script.rb#L17-L18" >}}     {{< /tab >}}     {{< tab header="JavaScript" >}}     {{< gh-codeblock path="examples/javascript/test/getting_started/firstScript.spec.js#L22-L23" >}}     {{< /tab >}}     {{< tab header="Kotlin" >}}     {{< gh-codeblock path="examples/kotlin/src/test/kotlin/dev/selenium/getting_started/FirstScriptTest.kt#L31-L32" >}}     {{< /tab >}}     {{< /tabpane >}}     

Which looks like this:

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

                      WebElement message = driver.findElement(By.id("message"));             message.getText();

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/java/src/test/java/dev/selenium/getting_started/FirstScript.java#L26-L27)

##### examples/java/src/test/java/dev/selenium/getting\_started/FirstScript.java

Copy  Close               package dev.selenium.getting_started;          import org.openqa.selenium.By;     import org.openqa.selenium.WebDriver;     import org.openqa.selenium.WebElement;     import org.openqa.selenium.chrome.ChromeDriver;          import java.time.Duration;          public class FirstScript {         public static void main(String[] args) {             WebDriver driver = new ChromeDriver();                  driver.get("https://www.selenium.dev/selenium/web/web-form.html");                  driver.getTitle();                  driver.manage().timeouts().implicitlyWait(Duration.ofMillis(500));                  WebElement textBox = driver.findElement(By.name("my-text"));             WebElement submitButton = driver.findElement(By.cssSelector("button"));                  textBox.sendKeys("Selenium");             submitButton.click();                  WebElement message = driver.findElement(By.id("message"));             message.getText();                  driver.quit();         }     }                    message = driver.find_element(by=By.ID, value="message")     text = message.text

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/getting_started/first_script.py#L18-L19)

##### examples/python/tests/getting\_started/first\_script.py

Copy  Close               from selenium import webdriver     from selenium.webdriver.common.by import By          driver = webdriver.Chrome()          driver.get("https://www.selenium.dev/selenium/web/web-form.html")          title = driver.title          driver.implicitly_wait(0.5)          text_box = driver.find_element(by=By.NAME, value="my-text")     submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")          text_box.send_keys("Selenium")     submit_button.click()          message = driver.find_element(by=By.ID, value="message")     text = message.text          driver.quit()                            var message = driver.FindElement(By.Id("message"));             var value = message.Text;

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/dotnet/SeleniumDocs/GettingStarted/FirstScript.cs#L25-L26)

##### examples/dotnet/SeleniumDocs/GettingStarted/FirstScript.cs

Copy  Close               using System;     using OpenQA.Selenium;     using OpenQA.Selenium.Chrome;          namespace SeleniumDocs.GettingStarted;          public static class FirstScript     {         public static void Main()         {             IWebDriver driver = new ChromeDriver();                  driver.Navigate().GoToUrl("https://www.selenium.dev/selenium/web/web-form.html");                  var title = driver.Title;                  driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromMilliseconds(500);                  var textBox = driver.FindElement(By.Name("my-text"));             var submitButton = driver.FindElement(By.TagName("button"));                              textBox.SendKeys("Selenium");             submitButton.Click();                              var message = driver.FindElement(By.Id("message"));             var value = message.Text;                              driver.Quit();         }     }               message = driver.find_element(id: 'message')     message.text

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/ruby/spec/getting_started/first_script.rb#L17-L18)

##### examples/ruby/spec/getting\_started/first\_script.rb

Copy  Close               require 'selenium-webdriver'          driver = Selenium::WebDriver.for :chrome          driver.get('https://www.selenium.dev/selenium/web/web-form.html')          driver.title          driver.manage.timeouts.implicit_wait = 500          text_box = driver.find_element(name: 'my-text')     submit_button = driver.find_element(tag_name: 'button')          text_box.send_keys('Selenium')     submit_button.click          message = driver.find_element(id: 'message')     message.text          driver.quit                        let message = await driver.findElement(By.id('message'));         let value = await message.getText();

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/javascript/test/getting_started/firstScript.spec.js#L22-L23)

##### examples/javascript/test/getting\_started/firstScript.spec.js

Copy  Close               const {By, Builder, Browser} = require('selenium-webdriver');     const assert = require("assert");          (async function firstTest() {       let driver;              try {         driver = await new Builder().forBrowser(Browser.CHROME).build();         await driver.get('https://www.selenium.dev/selenium/web/web-form.html');                let title = await driver.getTitle();         assert.equal("Web form", title);                await driver.manage().setTimeouts({implicit: 500});                let textBox = await driver.findElement(By.name('my-text'));         let submitButton = await driver.findElement(By.css('button'));                await textBox.sendKeys('Selenium');         await submitButton.click();                let message = await driver.findElement(By.id('message'));         let value = await message.getText();         assert.equal("Received!", value);       } catch (e) {         console.log(e)       } finally {         await driver.quit();       }     }())                            val message = driver.findElement(By.id("message"))             val value = message.getText()

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/kotlin/src/test/kotlin/dev/selenium/getting_started/FirstScriptTest.kt#L31-L32)

##### examples/kotlin/src/test/kotlin/dev/selenium/getting\_started/FirstScriptTest.kt

Copy  Close               package dev.selenium.getting_started          import org.junit.jupiter.api.*     import org.junit.jupiter.api.Assertions.assertEquals     import org.openqa.selenium.By     import org.openqa.selenium.WebDriver     import org.openqa.selenium.chrome.ChromeDriver     import java.time.Duration          @TestInstance(TestInstance.Lifecycle.PER_CLASS)     class FirstScriptTest {         private lateinit var driver: WebDriver              @Test         fun eightComponents() {             driver = ChromeDriver()                  driver.get("https://www.selenium.dev/selenium/web/web-form.html")                  val title = driver.title             assertEquals("Web form", title)                  driver.manage().timeouts().implicitlyWait(Duration.ofMillis(500))                  var textBox = driver.findElement(By.name("my-text"))             val submitButton = driver.findElement(By.cssSelector("button"))                  textBox.sendKeys("Selenium")             submitButton.click()                  val message = driver.findElement(By.id("message"))             val value = message.getText()             assertEquals("Received!", value)                  driver.quit()         }          }

### Using Markdown in a Tab

If you want your example to include something other than code \(default\) or html \(from `gh-codeblock`\), you need to first set `text=true`, then change the Hugo syntax for the `tab`to use `%` instead of `<` and `>` with curly braces:               {{< tabpane text=true >}}     {{% tab header="Java" %}}     1. Start the driver     {{< gh-codeblock path="examples/java/src/test/java/dev/selenium/getting_started/FirstScript.java#L12" >}}     2. Navigate to a page     {{< gh-codeblock path="examples/java/src/test/java/dev/selenium/getting_started/FirstScript.java#L14" >}}     3. Quit the driver     {{< gh-codeblock path="examples/java/src/test/java/dev/selenium/getting_started/FirstScript.java#L29" >}}     {{% /tab %}}     < ... >     {{< /tabpane >}}     

This produces:

  * Java

  1. Start the driver                    WebDriver driver = new ChromeDriver();

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/java/src/test/java/dev/selenium/getting_started/FirstScript.java#L12)

##### examples/java/src/test/java/dev/selenium/getting\_started/FirstScript.java

Copy  Close                    package dev.selenium.getting_started;                    import org.openqa.selenium.By;          import org.openqa.selenium.WebDriver;          import org.openqa.selenium.WebElement;          import org.openqa.selenium.chrome.ChromeDriver;                    import java.time.Duration;                    public class FirstScript {              public static void main(String[] args) {                  WebDriver driver = new ChromeDriver();                            driver.get("https://www.selenium.dev/selenium/web/web-form.html");                            driver.getTitle();                            driver.manage().timeouts().implicitlyWait(Duration.ofMillis(500));                            WebElement textBox = driver.findElement(By.name("my-text"));                  WebElement submitButton = driver.findElement(By.cssSelector("button"));                            textBox.sendKeys("Selenium");                  submitButton.click();                            WebElement message = driver.findElement(By.id("message"));                  message.getText();                            driver.quit();              }          }          

  2. Navigate to a page                    driver.get("https://www.selenium.dev/selenium/web/web-form.html");

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/java/src/test/java/dev/selenium/getting_started/FirstScript.java#L14)

##### examples/java/src/test/java/dev/selenium/getting\_started/FirstScript.java

Copy  Close                    package dev.selenium.getting_started;                    import org.openqa.selenium.By;          import org.openqa.selenium.WebDriver;          import org.openqa.selenium.WebElement;          import org.openqa.selenium.chrome.ChromeDriver;                    import java.time.Duration;                    public class FirstScript {              public static void main(String[] args) {                  WebDriver driver = new ChromeDriver();                            driver.get("https://www.selenium.dev/selenium/web/web-form.html");                            driver.getTitle();                            driver.manage().timeouts().implicitlyWait(Duration.ofMillis(500));                            WebElement textBox = driver.findElement(By.name("my-text"));                  WebElement submitButton = driver.findElement(By.cssSelector("button"));                            textBox.sendKeys("Selenium");                  submitButton.click();                            WebElement message = driver.findElement(By.id("message"));                  message.getText();                            driver.quit();              }          }          

  3. Quit the driver                    driver.quit();

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/java/src/test/java/dev/selenium/getting_started/FirstScript.java#L29)

##### examples/java/src/test/java/dev/selenium/getting\_started/FirstScript.java

Copy  Close                    package dev.selenium.getting_started;                    import org.openqa.selenium.By;          import org.openqa.selenium.WebDriver;          import org.openqa.selenium.WebElement;          import org.openqa.selenium.chrome.ChromeDriver;                    import java.time.Duration;                    public class FirstScript {              public static void main(String[] args) {                  WebDriver driver = new ChromeDriver();                            driver.get("https://www.selenium.dev/selenium/web/web-form.html");                            driver.getTitle();                            driver.manage().timeouts().implicitlyWait(Duration.ofMillis(500));                            WebElement textBox = driver.findElement(By.name("my-text"));                  WebElement submitButton = driver.findElement(By.cssSelector("button"));                            textBox.sendKeys("Selenium");                  submitButton.click();                            WebElement message = driver.findElement(By.id("message"));                  message.getText();                            driver.quit();              }          }          

This is preferred to writing code comments because those will not be translated. Only include the code that is needed for the documentation, and avoid over-explaining. Finally, remember not to indent plain text or it will rendered as a codeblock.

Last modified October 19, 2024: [Fix : Invalid line numbers reference on style page \(\#2007\)\[deploy site\] \(8d5ae7c86bf\)](https://github.com/SeleniumHQ/seleniumhq.github.io/commit/8d5ae7c86bf382d6b51d5cd75e8e3fb6a56a6327)