# Getting started | Selenium

**URL:** https://www.selenium.dev/documentation/webdriver/getting_started/_print
**Word Count:** 2664
**Links Count:** 177
**Scraped:** 2025-07-17 06:17:48
**Status:** completed

---

This is the multi-page printable view of this section. Click here to print.

[Return to the regular view of this page](https://www.selenium.dev/documentation/webdriver/getting_started/).

# Getting started

If you are new to Selenium, we have a few resources that can help you get up to speed right away.

  * 1: Install a Selenium library   * 2: Write your first Selenium script   * 3: Organizing and Executing Selenium Code

Selenium supports automation of all the major browsers in the market through the use of _WebDriver_. WebDriver is an API and protocol that defines a language-neutral interface for controlling the behaviour of web browsers. Each browser is backed by a specific WebDriver implementation, called a _driver_. The driver is the component responsible for delegating down to the browser, and handles communication to and from Selenium and the browser.

This separation is part of a conscious effort to have browser vendors take responsibility for the implementation for their browsers. Selenium makes use of these third party drivers where possible, but also provides its own drivers maintained by the project for the cases when this is not a reality.

The Selenium framework ties all of these pieces together through a user-facing interface that enables the different browser backends to be used transparently, enabling cross-browser and cross-platform automation.

Selenium setup is quite different from the setup of other commercial tools. Before you can start writing Selenium code, you have to install the language bindings libraries for your language of choice, the browser you want to use, and the driver for that browser.

_**Follow the links below to get up and going with Selenium WebDriver.**_

If you wish to start with a low-code/record and playback tool, please check [Selenium IDE](https://selenium.dev/selenium-ide)

Once you get things working, if you want to scale up your tests, check out the [Selenium Grid](https://www.selenium.dev/documentation/grid/).

# 1 - Install a Selenium library

Setting up the Selenium library for your favourite programming language.

First you need to install the Selenium bindings for your automation project. The installation process for libraries depends on the language you choose to use. Make sure you check the [Selenium downloads page](https://www.selenium.dev/downloads/) to make sure you are using the latest version.

## Requirements by language

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

View the minimum supported Java version [here](https://github.com/SeleniumHQ/selenium/blob/trunk/.bazelrc#L13).

Installation of Selenium libraries for Java is accomplished using a build tool.

### Maven

Specify the dependencies in the project’s `pom.xml` file:                       <dependency>                 <groupId>org.seleniumhq.selenium</groupId>                 <artifactId>selenium-java</artifactId>                 <version>${selenium.version}</version>             </dependency>

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/java/pom.xml#L30-L34)

##### examples/java/pom.xml

Copy  Close               <?xml version="1.0" encoding="UTF-8"?>     <project xmlns="http://maven.apache.org/POM/4.0.0"              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"              xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">         <modelVersion>4.0.0</modelVersion>              <groupId>dev.selenium</groupId>         <artifactId>selenium-examples</artifactId>         <version>1.0.0</version>              <properties>             <surefire.parallel>1</surefire.parallel>             <maven.compiler.source>17</maven.compiler.source>             <maven.compiler.target>17</maven.compiler.target>             <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>             <selenium.version>4.34.0</selenium.version>         </properties>              <repositories>             <repository>             <id>sonatype-nexus-snapshots</id>             <url>https://oss.sonatype.org/content/repositories/snapshots/</url>             <snapshots>                 <enabled>true</enabled>             </snapshots>             </repository>         </repositories>              <dependencies>             <dependency>                 <groupId>org.seleniumhq.selenium</groupId>                 <artifactId>selenium-java</artifactId>                 <version>${selenium.version}</version>             </dependency>             <dependency>                 <groupId>org.seleniumhq.selenium</groupId>                 <artifactId>selenium-grid</artifactId>                 <version>${selenium.version}</version>             </dependency>             <dependency>                 <groupId>org.junit.jupiter</groupId>                 <artifactId>junit-jupiter-engine</artifactId>                 <version>5.13.3</version>                 <scope>test</scope>             </dependency>             <dependency>                 <groupId>com.titusfortner</groupId>                 <artifactId>selenium-logger</artifactId>                 <version>2.4.0</version>             </dependency>         </dependencies>              <build>             <plugins>                 <plugin>                     <groupId>org.apache.maven.plugins</groupId>                     <artifactId>maven-surefire-plugin</artifactId>                     <version>3.5.3</version>                     <configuration>                         <properties>                             <configurationParameters>                                 junit.jupiter.execution.parallel.enabled = true                                 junit.jupiter.execution.parallel.mode.default = concurrent                                 junit.jupiter.execution.parallel.config.strategy = fixed                                 junit.jupiter.execution.parallel.config.fixed.parallelism = ${surefire.parallel}                                 junit.jupiter.execution.parallel.config.fixed.max-pool-size = ${surefire.parallel}                             </configurationParameters>                         </properties>                         <rerunFailingTestsCount>3</rerunFailingTestsCount>                     </configuration>                 </plugin>             </plugins>         </build>     </project>     

### Gradle

Specify the dependency in the project `build.gradle` file as `testImplementation`:                   testImplementation 'org.seleniumhq.selenium:selenium-java:4.34.0'         testImplementation 'org.junit.jupiter:junit-jupiter-engine:5.13.3'

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/java/build.gradle#L13-L14)

##### examples/java/build.gradle

Copy  Close               plugins {         id 'java'     }          group 'dev.selenium'     version '1.0-SNAPSHOT'          repositories {         mavenCentral()     }          dependencies {         testImplementation 'org.seleniumhq.selenium:selenium-java:4.34.0'         testImplementation 'org.junit.jupiter:junit-jupiter-engine:5.13.3'     }          test {         useJUnitPlatform()     }     

The minimum supported Python version for each Selenium version can be found in “Supported Python Versions” on [PyPi](https://pypi.org/project/selenium/).

There are a couple different ways to install Selenium.

### Pip               pip install selenium     

  

### Download

Alternatively you can download the [PyPI Built Distribution](https://pypi.org/project/selenium/#files) \(selenium-x.x.x.-py3-none-any.whl\) and install it using _pip_ :               pip install selenium-x.x.x.-py3-none-any.whl     

  

### Require in project

To use it in a project, add it to the `requirements.txt` file:               selenium==4.34.2

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/requirements.txt#L1)

##### examples/python/requirements.txt

Copy  Close               selenium==4.34.2     pytest==8.4.1     trio==0.30.0     pytest-trio==0.8.0     pytest-rerunfailures==15.1     flake8==7.3.0     requests==2.32.4     tox==4.27.0     

A list of all supported frameworks for each version of Selenium is available on [Nuget](https://www.nuget.org/packages/Selenium.WebDriver)

There are a few options for installing Selenium.

### Packet Manager               Install-Package Selenium.WebDriver     

  

### .NET CLI               dotnet add package Selenium.WebDriver     

  

### CSProj

in the project’s `csproj` file, specify the dependency as a `PackageReference` in `ItemGroup`:                     <PackageReference Include="Selenium.WebDriver" Version="4.33.0" />

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/dotnet/SeleniumDocs/SeleniumDocs.csproj#L14)

##### examples/dotnet/SeleniumDocs/SeleniumDocs.csproj

Copy  Close               <Project Sdk="Microsoft.NET.Sdk">              <PropertyGroup>             <TargetFramework>net8.0</TargetFramework>             <GenerateProgramFile>false</GenerateProgramFile>         </PropertyGroup>              <ItemGroup>           <PackageReference Include="Microsoft.NET.Test.Sdk" Version="17.11.1" />           <PackageReference Include="Microsoft.IdentityModel.Tokens" Version="7.7.1" />           <PackageReference Include="MSTest.TestAdapter" Version="3.6.0" />           <PackageReference Include="MSTest.TestFramework" Version="3.6.0" />           <PackageReference Include="Selenium.Support" Version="4.33.0" />           <PackageReference Include="Selenium.WebDriver" Version="4.33.0" />         </ItemGroup>              <ItemGroup>           <Folder Include="LocalPackages" />         </ItemGroup>          </Project>     

### Additional considerations

Further items of note for using Visual Studio Code \(vscode\) and C\#

Install the compatible .NET SDK as per the section above. Also install the vscode extensions \(Ctrl-Shift-X\) for C\# and NuGet. Follow the [instruction here](https://docs.microsoft.com/en-us/dotnet/core/tutorials/with-visual-studio-code?pivots=dotnet-5-0) to create and run the “Hello World” console project using C\#. You may also create a NUnit starter project using the command line `dotnet new NUnit`. Make sure the file `%appdata%\NuGet\nuget.config` is configured properly as some developers reported that it will be empty due to some issues. If `nuget.config` is empty, or not configured properly, then .NET builds will fail for Selenium Projects. Add the following section to the file `nuget.config` if it is empty:               <configuration>       <packageSources>         <add key="nuget.org" value="https://api.nuget.org/v3/index.json" protocolVersion="3" />         <add key="nuget.org" value="https://www.nuget.org/api/v2/" />          </packageSources>     ...     

For more info about `nuget.config` [click here](https://docs.microsoft.com/en-us/nuget/reference/nuget-config-file). You may have to customize `nuget.config` to meet you needs.

Now, go back to vscode, press Ctrl-Shift-P, and type “NuGet Add Package”, and enter the required Selenium packages such as `Selenium.WebDriver`. Press Enter and select the version. Now you can use the examples in the documentation related to C\# with vscode.

You can see the minimum required version of Ruby for any given Selenium version on [rubygems.org](https://rubygems.org/gems/selenium-webdriver/)

Selenium can be installed two different ways.

### Install manually               gem install selenium-webdriver     

  

### Add to project’s gemfile               gem 'selenium-devtools', '= 0.138.0'

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/ruby/Gemfile#L10)

##### examples/ruby/Gemfile

Copy  Close               # frozen_string_literal: true          source 'https://rubygems.org'          gem 'ffi', '~> 1.15', '>= 1.15.5' if Gem.win_platform? # Windows only     gem 'rake', '~> 13.0'     gem 'rspec', '~> 3.0'     gem 'rubocop', '~> 1.35'     gem 'rubocop-rspec', '~> 3.0'     gem 'selenium-devtools', '= 0.138.0'     gem 'selenium-webdriver', '= 4.34.0'     

You can find the minimum required version of Node for any given version of Selenium in the `Node Support Policy` section on [npmjs](https://www.npmjs.com/package/selenium-webdriver)

Selenium is typically installed using npm.

### Install locally               npm install selenium-webdriver     

  

### Add to project

In your project’s `package.json`, add requirement to `dependencies`:                       "mocha": "11.7.1"

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/javascript/package.json#L14)

##### examples/javascript/package.json

Copy  Close               {         "name": "javascript-examples",         "version": "1.0.0",         "scripts": {             "test": "npx mocha test/**/*.spec.js --timeout 90000"         },         "author": "The Selenium project",         "license": "Apache-2.0",         "dependencies": {             "assert": "2.1.0",             "selenium-webdriver": "4.34.0"         },         "devDependencies": {             "mocha": "11.7.1"         }     }     

Use the Java bindings for Kotlin.

## Next Step

[Create your first Selenium script](https://www.selenium.dev/documentation/webdriver/getting_started/first_script/)

# 2 - Write your first Selenium script

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

# 3 - Organizing and Executing Selenium Code

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