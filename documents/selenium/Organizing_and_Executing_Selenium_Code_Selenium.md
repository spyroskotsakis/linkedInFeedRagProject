# Organizing and Executing Selenium Code | Selenium

**URL:** https://www.selenium.dev/documentation/webdriver/getting_started/using_selenium
**Word Count:** 933
**Links Count:** 261
**Scraped:** 2025-07-17 06:13:36
**Status:** completed

---

# Organizing and Executing Selenium Code

Scaling Selenium execution with an IDE and a Test Runner library

## Content Help

**Note:** This section needs additional and/or updated content      This page is very incomplete and has placeholders for things that need to be added or expounded on.      Check our [contribution guidelines](https://www.selenium.dev/documentation/about/contributing/) if you’d like to help.

If you want to run more than a handful of one-off scripts, you need to be able to organize and work with your code. This page should give you ideas for how to actually do productive things with your Selenium code.

## Common Uses

Most people use Selenium to execute automated tests for web applications, but Selenium supports any use case of browser automation.

### Repetitive Tasks

Perhaps you need to log into a website and download something, or submit a form. You can create a Selenium script to run with a service at preset times.

### Web Scraping

Are you looking to collect data from a site that doesn’t have an API? Selenium will let you do this, but please make sure you are familiar with the website’s terms of service as some websites do not permit it and others will even block Selenium.

### Testing

Running Selenium for testing requires making assertions on actions taken by Selenium. So a good assertion library is required. Additional features to provide structure for tests require use of [Test Runner](https://www.selenium.dev/documentation/webdriver/getting_started/using_selenium/#test-runner).

## IDEs

Regardless of how you use Selenium code, you won’t be very effective writing or executing it without a good Integrated Developer Environment. Here are some common options…

  * [Eclipse](https://www.eclipse.org/)   * [IntelliJ IDEA](https://www.jetbrains.com/idea/)   * [PyCharm](https://www.jetbrains.com/pycharm/)   * [RubyMine](https://www.jetbrains.com/ruby/)   * [Rider](https://www.jetbrains.com/rider/)   * [WebStorm](https://www.jetbrains.com/webstorm/)   * [VS Code](https://code.visualstudio.com/)

## Test Runner

Even if you aren’t using Selenium for testing, if you have advanced use cases, it might make sense to use a test runner to better organize your code. Being able to use before/after hooks and run things in groups or in parallel can be very useful.

### Choosing

There are many different test runners available.

All the code examples in this documentation can be found in \(or is being moved to\) our example directories that use test runners and get executed every release to ensure all the code is correct and updated. Here is a list of test runners with links. The first item is the one that is used by this repository and the one that will be used for all examples on this page.

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

  * [JUnit](https://junit.org/junit5/) \- A widely-used testing framework for Java-based Selenium tests.   * [TestNG](https://testng.org/) \- Offers extra features like parallel test execution and parameterized tests.

  * [pytest](https://pytest.org/) \- A preferred choice for many, thanks to its simplicity and powerful plugins.   * [unittest](https://docs.python.org/3/library/unittest.html) \- Python’s standard library testing framework.

  * [NUnit](https://nunit.org/) \- A popular unit-testing framework for .NET.   * [MS Test](https://docs.microsoft.com/en-us/visualstudio/test/getting-started-with-unit-testing?view=vs-2019) \- Microsoft’s own unit testing framework.

  * [RSpec](https://rspec.info/) \- The most widely used testing library for running Selenium tests in Ruby.   * [Minitest](https://github.com/seattlerb/minitest) \- A lightweight testing framework that comes with Ruby standard library.

  * [Jest](https://jestjs.io/) \- Primarily known as a testing framework for React, it can also be used for Selenium tests.   * [Mocha](https://mochajs.org/) \- The most common JS library for running Selenium tests.

  * [Kotest](https://kotest.io/) \- A flexible and comprehensive testing framework specifically designed for Kotlin.   * [JUnit5](https://junit.org/junit5/) \- The standard Java testing framework, fully compatible with Kotlin.

### Installing

This is very similar to what was required in [Install a Selenium Library](https://www.selenium.dev/documentation/webdriver/getting_started/install_library/). This code is only showing examples for what is being used in our Documentation Examples project.

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

**Maven**

**Gradle**

To use it in a project, add it to the `requirements.txt` file:

in the project’s `csproj` file, specify the dependency as a `PackageReference` in `ItemGroup`:

Add to project’s gemfile

In your project’s `package.json`, add requirement to `dependencies`:

### Asserting

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

              		String title = driver.getTitle();     		assertEquals("Web form", title);

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/java/src/test/java/dev/selenium/getting_started/UsingSeleniumTest.java#L30-L31)

##### examples/java/src/test/java/dev/selenium/getting\_started/UsingSeleniumTest.java

Copy  Close               package dev.selenium.getting_started;          import static org.junit.jupiter.api.Assertions.assertEquals;          import java.time.Duration;          import org.junit.jupiter.api.AfterEach;     import org.junit.jupiter.api.BeforeEach;     import org.junit.jupiter.api.Test;     import org.openqa.selenium.By;     import org.openqa.selenium.WebDriver;     import org.openqa.selenium.WebElement;     import org.openqa.selenium.chrome.ChromeDriver;          public class UsingSeleniumTest {          	WebDriver driver;          	@BeforeEach     	public void setup() {     		driver = new ChromeDriver();     	}          	@Test     	public void eightComponents() {          		driver.manage().timeouts().implicitlyWait(Duration.ofMillis(500));     		driver.get("https://www.selenium.dev/selenium/web/web-form.html");          		String title = driver.getTitle();     		assertEquals("Web form", title);          		WebElement textBox = driver.findElement(By.name("my-text"));     		WebElement submitButton = driver.findElement(By.cssSelector("button"));          		textBox.sendKeys("Selenium");     		submitButton.click();          		WebElement message = driver.findElement(By.id("message"));     		String value = message.getText();     		assertEquals("Received!", value);          	}          	@AfterEach     	public void teardown() {     		driver.quit();     	}          }                        title = driver.title         assert title == "Web form"

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/getting_started/using_selenium_tests.py#L8-L9)

##### examples/python/tests/getting\_started/using\_selenium\_tests.py

Copy  Close               from selenium import webdriver     from selenium.webdriver.common.by import By               def test_eight_components():         driver = setup()              title = driver.title         assert title == "Web form"              driver.implicitly_wait(0.5)              text_box = driver.find_element(by=By.NAME, value="my-text")         submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")              text_box.send_keys("Selenium")         submit_button.click()              message = driver.find_element(by=By.ID, value="message")         value = message.text         assert value == "Received!"              teardown(driver)          def setup():         driver = webdriver.Chrome()         driver.get("https://www.selenium.dev/selenium/web/web-form.html")         return driver          def teardown(driver):         driver.quit()                                var title = driver.Title;                 Assert.AreEqual("Web form", title);

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/dotnet/SeleniumDocs/GettingStarted/UsingSeleniumTest.cs#L19-L20)

##### examples/dotnet/SeleniumDocs/GettingStarted/UsingSeleniumTest.cs

Copy  Close               using System;     using Microsoft.VisualStudio.TestTools.UnitTesting;     using OpenQA.Selenium;     using OpenQA.Selenium.Chrome;          namespace SeleniumDocs.GettingStarted     {         [TestClass]         public class UsingSeleniumTest         {                  [TestMethod]             public void EightComponents()             {                 IWebDriver driver = new ChromeDriver();                      driver.Navigate().GoToUrl("https://www.selenium.dev/selenium/web/web-form.html");                      var title = driver.Title;                 Assert.AreEqual("Web form", title);                      driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromMilliseconds(500);                      var textBox = driver.FindElement(By.Name("my-text"));                 var submitButton = driver.FindElement(By.TagName("button"));                                  textBox.SendKeys("Selenium");                 submitButton.Click();                                  var message = driver.FindElement(By.Id("message"));                 var value = message.Text;                 Assert.AreEqual("Received!", value);                                  driver.Quit();             }         }     }                   title = @driver.title         expect(title).to eq('Web form')

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/ruby/spec/getting_started/using_selenium_spec.rb#L14-L15)

##### examples/ruby/spec/getting\_started/using\_selenium\_spec.rb

Copy  Close               # frozen_string_literal: true          require 'spec_helper'     require 'selenium-webdriver'          RSpec.describe 'Using Selenium' do       before do         @driver = Selenium::WebDriver.for :chrome       end            it 'uses eight components' do         @driver.get('https://www.selenium.dev/selenium/web/web-form.html')              title = @driver.title         expect(title).to eq('Web form')              @driver.manage.timeouts.implicit_wait = 500              text_box = @driver.find_element(name: 'my-text')         submit_button = @driver.find_element(tag_name: 'button')              text_box.send_keys('Selenium')         submit_button.click              message = @driver.find_element(id: 'message')         value = message.text         expect(value).to eq('Received!')       end     end                        let title = await driver.getTitle();         assert.equal("Web form", title);

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/javascript/test/getting_started/runningTests.spec.js#L14-L15)

##### examples/javascript/test/getting\_started/runningTests.spec.js

Copy  Close               const {By, Builder} = require('selenium-webdriver');     const assert = require("assert");          describe('First script', function () {       let driver;            before(async function () {         driver = await new Builder().forBrowser('chrome').build();       });            it('First Selenium script with mocha', async function () {         await driver.get('https://www.selenium.dev/selenium/web/web-form.html');              let title = await driver.getTitle();         assert.equal("Web form", title);              await driver.manage().setTimeouts({implicit: 500});              let textBox = await driver.findElement(By.name('my-text'));         let submitButton = await driver.findElement(By.css('button'));              await textBox.sendKeys('Selenium');         await submitButton.click();              let message = await driver.findElement(By.id('message'));         let value = await message.getText();         assert.equal("Received!", value);       });            after(async () => await driver.quit());     });

[Add Example](https://www.selenium.dev/documentation/about/contributing/#creating-examples)

### Setting Up and Tearing Down

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

### Set Up               	@BeforeEach     	public void setup() {     		driver = new ChromeDriver();     	}

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/java/src/test/java/dev/selenium/getting_started/UsingSeleniumTest.java#L19-L22)

##### examples/java/src/test/java/dev/selenium/getting\_started/UsingSeleniumTest.java

Copy  Close               package dev.selenium.getting_started;          import static org.junit.jupiter.api.Assertions.assertEquals;          import java.time.Duration;          import org.junit.jupiter.api.AfterEach;     import org.junit.jupiter.api.BeforeEach;     import org.junit.jupiter.api.Test;     import org.openqa.selenium.By;     import org.openqa.selenium.WebDriver;     import org.openqa.selenium.WebElement;     import org.openqa.selenium.chrome.ChromeDriver;          public class UsingSeleniumTest {          	WebDriver driver;          	@BeforeEach     	public void setup() {     		driver = new ChromeDriver();     	}          	@Test     	public void eightComponents() {          		driver.manage().timeouts().implicitlyWait(Duration.ofMillis(500));     		driver.get("https://www.selenium.dev/selenium/web/web-form.html");          		String title = driver.getTitle();     		assertEquals("Web form", title);          		WebElement textBox = driver.findElement(By.name("my-text"));     		WebElement submitButton = driver.findElement(By.cssSelector("button"));          		textBox.sendKeys("Selenium");     		submitButton.click();          		WebElement message = driver.findElement(By.id("message"));     		String value = message.getText();     		assertEquals("Received!", value);          	}          	@AfterEach     	public void teardown() {     		driver.quit();     	}          }     

### Tear Down               	@AfterEach     	public void teardown() {     		driver.quit();     	}

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/java/src/test/java/dev/selenium/getting_started/UsingSeleniumTest.java#L45-L48)

##### examples/java/src/test/java/dev/selenium/getting\_started/UsingSeleniumTest.java

Copy  Close               package dev.selenium.getting_started;          import static org.junit.jupiter.api.Assertions.assertEquals;          import java.time.Duration;          import org.junit.jupiter.api.AfterEach;     import org.junit.jupiter.api.BeforeEach;     import org.junit.jupiter.api.Test;     import org.openqa.selenium.By;     import org.openqa.selenium.WebDriver;     import org.openqa.selenium.WebElement;     import org.openqa.selenium.chrome.ChromeDriver;          public class UsingSeleniumTest {          	WebDriver driver;          	@BeforeEach     	public void setup() {     		driver = new ChromeDriver();     	}          	@Test     	public void eightComponents() {          		driver.manage().timeouts().implicitlyWait(Duration.ofMillis(500));     		driver.get("https://www.selenium.dev/selenium/web/web-form.html");          		String title = driver.getTitle();     		assertEquals("Web form", title);          		WebElement textBox = driver.findElement(By.name("my-text"));     		WebElement submitButton = driver.findElement(By.cssSelector("button"));          		textBox.sendKeys("Selenium");     		submitButton.click();          		WebElement message = driver.findElement(By.id("message"));     		String value = message.getText();     		assertEquals("Received!", value);          	}          	@AfterEach     	public void teardown() {     		driver.quit();     	}          }     

### Set Up               def setup():         driver = webdriver.Chrome()         driver.get("https://www.selenium.dev/selenium/web/web-form.html")         return driver

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/getting_started/using_selenium_tests.py#L25-L28)

##### examples/python/tests/getting\_started/using\_selenium\_tests.py

Copy  Close               from selenium import webdriver     from selenium.webdriver.common.by import By               def test_eight_components():         driver = setup()              title = driver.title         assert title == "Web form"              driver.implicitly_wait(0.5)              text_box = driver.find_element(by=By.NAME, value="my-text")         submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")              text_box.send_keys("Selenium")         submit_button.click()              message = driver.find_element(by=By.ID, value="message")         value = message.text         assert value == "Received!"              teardown(driver)          def setup():         driver = webdriver.Chrome()         driver.get("https://www.selenium.dev/selenium/web/web-form.html")         return driver          def teardown(driver):         driver.quit()     

### Tear Down               def teardown(driver):         driver.quit()

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/getting_started/using_selenium_tests.py#L30-31)

##### examples/python/tests/getting\_started/using\_selenium\_tests.py

Copy  Close               from selenium import webdriver     from selenium.webdriver.common.by import By               def test_eight_components():         driver = setup()              title = driver.title         assert title == "Web form"              driver.implicitly_wait(0.5)              text_box = driver.find_element(by=By.NAME, value="my-text")         submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")              text_box.send_keys("Selenium")         submit_button.click()              message = driver.find_element(by=By.ID, value="message")         value = message.text         assert value == "Received!"              teardown(driver)          def setup():         driver = webdriver.Chrome()         driver.get("https://www.selenium.dev/selenium/web/web-form.html")         return driver          def teardown(driver):         driver.quit()     

[Add Example](https://www.selenium.dev/documentation/about/contributing/#creating-examples)

### Set Up                 before do         @driver = Selenium::WebDriver.for :chrome       end

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/ruby/spec/getting_started/using_selenium_spec.rb#L7-L9)

##### examples/ruby/spec/getting\_started/using\_selenium\_spec.rb

Copy  Close               # frozen_string_literal: true          require 'spec_helper'     require 'selenium-webdriver'          RSpec.describe 'Using Selenium' do       before do         @driver = Selenium::WebDriver.for :chrome       end            it 'uses eight components' do         @driver.get('https://www.selenium.dev/selenium/web/web-form.html')              title = @driver.title         expect(title).to eq('Web form')              @driver.manage.timeouts.implicit_wait = 500              text_box = @driver.find_element(name: 'my-text')         submit_button = @driver.find_element(tag_name: 'button')              text_box.send_keys('Selenium')         submit_button.click              message = @driver.find_element(id: 'message')         value = message.text         expect(value).to eq('Received!')       end     end     

### Tear Down                 config.after { @driver&.quit }

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/ruby/spec/spec_helper.rb#L30)

##### examples/ruby/spec/spec\_helper.rb

Copy  Close               # frozen_string_literal: true          require 'selenium-webdriver'     require 'selenium/webdriver/support/guards'          RSpec.configure do |config|       # Enable flags like --only-failures and --next-failure       config.example_status_persistence_file_path = '.rspec_status'            # Disable RSpec exposing methods globally on `Module` and `main`       config.disable_monkey_patching!       Dir.mktmpdir('tmp')       config.example_status_persistence_file_path = 'tmp/examples.txt'            config.expect_with :rspec do |c|         c.syntax = :expect       end            config.before do |example|         bug_tracker = 'https://github.com/SeleniumHQ/seleniumhq.github.io/issues'         guards = Selenium::WebDriver::Support::Guards.new(example,                                                           bug_tracker: bug_tracker)         guards.add_condition(:platform, Selenium::WebDriver::Platform.os)         guards.add_condition(:ci, Selenium::WebDriver::Platform.ci)              results = guards.disposition         send(*results) if results       end            config.after { @driver&.quit }            def start_session         options = Selenium::WebDriver::Chrome::Options.new         options.add_argument('disable-search-engine-choice-screen')         options.add_argument('--no-sandbox')         @driver = Selenium::WebDriver.for(:chrome, options: options)       end            def start_bidi_session         options = Selenium::WebDriver::Chrome::Options.new(web_socket_url: true)         @driver = Selenium::WebDriver.for :chrome, options: options       end            def start_firefox         options = Selenium::WebDriver::Options.firefox(timeouts: {implicit: 1500})         @driver = Selenium::WebDriver.for :firefox, options: options       end     end     

\#\#\# Set Up                 before(async function () {         driver = await new Builder().forBrowser('chrome').build();       });

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/javascript/test/getting_started/runningTests.spec.js#L7-L9)

##### examples/javascript/test/getting\_started/runningTests.spec.js

Copy  Close               const {By, Builder} = require('selenium-webdriver');     const assert = require("assert");          describe('First script', function () {       let driver;            before(async function () {         driver = await new Builder().forBrowser('chrome').build();       });            it('First Selenium script with mocha', async function () {         await driver.get('https://www.selenium.dev/selenium/web/web-form.html');              let title = await driver.getTitle();         assert.equal("Web form", title);              await driver.manage().setTimeouts({implicit: 500});              let textBox = await driver.findElement(By.name('my-text'));         let submitButton = await driver.findElement(By.css('button'));              await textBox.sendKeys('Selenium');         await submitButton.click();              let message = await driver.findElement(By.id('message'));         let value = await message.getText();         assert.equal("Received!", value);       });            after(async () => await driver.quit());     });

\#\#\# Tear Down                 after(async () => await driver.quit());

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/javascript/test/getting_started/runningTests.spec.js#L30)

##### examples/javascript/test/getting\_started/runningTests.spec.js

Copy  Close               const {By, Builder} = require('selenium-webdriver');     const assert = require("assert");          describe('First script', function () {       let driver;            before(async function () {         driver = await new Builder().forBrowser('chrome').build();       });            it('First Selenium script with mocha', async function () {         await driver.get('https://www.selenium.dev/selenium/web/web-form.html');              let title = await driver.getTitle();         assert.equal("Web form", title);              await driver.manage().setTimeouts({implicit: 500});              let textBox = await driver.findElement(By.name('my-text'));         let submitButton = await driver.findElement(By.css('button'));              await textBox.sendKeys('Selenium');         await submitButton.click();              let message = await driver.findElement(By.id('message'));         let value = await message.getText();         assert.equal("Received!", value);       });            after(async () => await driver.quit());     });

[Add Example](https://www.selenium.dev/documentation/about/contributing/#creating-examples)

### Executing

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

### Maven               mvn clean test     

### Gradle               gradle clean test                    ```

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/README.md#L35)

##### examples/python/README.md

Copy  Close               # Running tests from Selenium Python examples          #### 1. Clone this repository          ```     git clone https://github.com/SeleniumHQ/seleniumhq.github.io.git     ```          #### 2. Navigate to `python` directory          ```     cd seleniumhq.github.io/examples/python     ```          #### 3. Create a virtual environment          - On Windows:          ```     py -m venv venv     venv\Scripts\activate     ```          - On Linux/Mac:          ```     python3 -m venv venv     source venv/bin/activate     ```          #### 4. Install dependencies:          ```     pip install -r requirements.txt     ```          > for help, see: https://packaging.python.org/en/latest/tutorials/installing-packages          #### 5. Run tests          - Run all tests with the default Python interpreter:          ```     pytest     ```          - Run all tests with every installed/supported Python interpreter:          ```     tox     ```          > Please have some patience - If you are doing it for the first time, it will take a little while to download the browser drivers          - Run a specific example:          ```     pytest path/to/test_script.py     ```          > Make sure to replace `path/to/test_script.py` with the path and name of the example you want to run     

[Add Example](https://www.selenium.dev/documentation/about/contributing/#creating-examples)               bundle exec rspec

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/ruby/README.md#L26)

##### examples/ruby/README.md

Copy  Close               # Running all tests from Selenium ruby example          Follow these steps to run all test example from selenium ruby          1. Clone this repository          ```     git clone https://github.com/SeleniumHQ/seleniumhq.github.io.git     ```          2. Navigate to `ruby` directory          ```     cd seleniumhq.github.io/examples/ruby     ```          3. Install dependencies using bundler          ```     bundler install     ```          4. Run all tests          ```     bundle exec rspec     ```          > Please keep some patience - If you are doing it for the first time, it will take a little while to verify and download the browser drivers          # Execute a ruby script          Use this command to run a ruby script and follow the first script example          ```     ruby example_script.rb     ```

### Mocha               mocha runningTests.spec.js     

### npx               npx mocha runningTests.spec.js     

[Add Example](https://www.selenium.dev/documentation/about/contributing/#creating-examples)

### Examples

In [First script](https://www.selenium.dev/documentation/webdriver/getting_started/first_script/), we saw each of the components of a Selenium script. Here’s an example of that code using a test runner:

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

              package dev.selenium.getting_started;          import static org.junit.jupiter.api.Assertions.assertEquals;          import java.time.Duration;          import org.junit.jupiter.api.AfterEach;     import org.junit.jupiter.api.BeforeEach;     import org.junit.jupiter.api.Test;     import org.openqa.selenium.By;     import org.openqa.selenium.WebDriver;     import org.openqa.selenium.WebElement;     import org.openqa.selenium.chrome.ChromeDriver;          public class UsingSeleniumTest {          	WebDriver driver;          	@BeforeEach     	public void setup() {     		driver = new ChromeDriver();     	}          	@Test     	public void eightComponents() {          		driver.manage().timeouts().implicitlyWait(Duration.ofMillis(500));     		driver.get("https://www.selenium.dev/selenium/web/web-form.html");          		String title = driver.getTitle();     		assertEquals("Web form", title);          		WebElement textBox = driver.findElement(By.name("my-text"));     		WebElement submitButton = driver.findElement(By.cssSelector("button"));          		textBox.sendKeys("Selenium");     		submitButton.click();          		WebElement message = driver.findElement(By.id("message"));     		String value = message.getText();     		assertEquals("Received!", value);          	}          	@AfterEach     	public void teardown() {     		driver.quit();     	}          }     

[__**View on GitHub**](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/java/src/test/java/dev/selenium/getting_started/UsingSeleniumTest.java)                from selenium import webdriver     from selenium.webdriver.common.by import By               def test_eight_components():         driver = setup()              title = driver.title         assert title == "Web form"              driver.implicitly_wait(0.5)              text_box = driver.find_element(by=By.NAME, value="my-text")         submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")              text_box.send_keys("Selenium")         submit_button.click()              message = driver.find_element(by=By.ID, value="message")         value = message.text         assert value == "Received!"              teardown(driver)          def setup():         driver = webdriver.Chrome()         driver.get("https://www.selenium.dev/selenium/web/web-form.html")         return driver          def teardown(driver):         driver.quit()     

[__**View on GitHub**](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/getting_started/using_selenium_tests.py)                using System;     using Microsoft.VisualStudio.TestTools.UnitTesting;     using OpenQA.Selenium;     using OpenQA.Selenium.Chrome;          namespace SeleniumDocs.GettingStarted     {         [TestClass]         public class UsingSeleniumTest         {                  [TestMethod]             public void EightComponents()             {                 IWebDriver driver = new ChromeDriver();                      driver.Navigate().GoToUrl("https://www.selenium.dev/selenium/web/web-form.html");                      var title = driver.Title;                 Assert.AreEqual("Web form", title);                      driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromMilliseconds(500);                      var textBox = driver.FindElement(By.Name("my-text"));                 var submitButton = driver.FindElement(By.TagName("button"));                                  textBox.SendKeys("Selenium");                 submitButton.Click();                                  var message = driver.FindElement(By.Id("message"));                 var value = message.Text;                 Assert.AreEqual("Received!", value);                                  driver.Quit();             }         }     }

[__**View on GitHub**](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/dotnet/SeleniumDocs/GettingStarted/UsingSeleniumTest.cs)                # frozen_string_literal: true          require 'spec_helper'     require 'selenium-webdriver'          RSpec.describe 'Using Selenium' do       before do         @driver = Selenium::WebDriver.for :chrome       end            it 'uses eight components' do         @driver.get('https://www.selenium.dev/selenium/web/web-form.html')              title = @driver.title         expect(title).to eq('Web form')              @driver.manage.timeouts.implicit_wait = 500              text_box = @driver.find_element(name: 'my-text')         submit_button = @driver.find_element(tag_name: 'button')              text_box.send_keys('Selenium')         submit_button.click              message = @driver.find_element(id: 'message')         value = message.text         expect(value).to eq('Received!')       end     end     

[__**View on GitHub**](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/ruby/spec/getting_started/using_selenium_spec.rb)                const {By, Builder} = require('selenium-webdriver');     const assert = require("assert");          describe('First script', function () {       let driver;            before(async function () {         driver = await new Builder().forBrowser('chrome').build();       });            it('First Selenium script with mocha', async function () {         await driver.get('https://www.selenium.dev/selenium/web/web-form.html');              let title = await driver.getTitle();         assert.equal("Web form", title);              await driver.manage().setTimeouts({implicit: 500});              let textBox = await driver.findElement(By.name('my-text'));         let submitButton = await driver.findElement(By.css('button'));              await textBox.sendKeys('Selenium');         await submitButton.click();              let message = await driver.findElement(By.id('message'));         let value = await message.getText();         assert.equal("Received!", value);       });            after(async () => await driver.quit());     });

[__**View on GitHub**](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/javascript/test/getting_started/runningTests.spec.js)

[ Add Example](https://www.selenium.dev/documentation/about/contributing/#creating-examples)

## Next Steps

Take what you’ve learned and build out your Selenium code\!

As you find more functionality that you need, read up on the rest of our [WebDriver documentation](https://www.selenium.dev/documentation/webdriver/).

Last modified April 6, 2025: [\[rb\] fix code references to spec\_helper \(1ecff866073\)](https://github.com/SeleniumHQ/seleniumhq.github.io/commit/1ecff86607338c62d53bf3dd94ba1291289c9247)