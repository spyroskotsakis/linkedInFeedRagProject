# Upgrade to Selenium 4 | Selenium

**URL:** https://www.selenium.dev/documentation/webdriver/troubleshooting/upgrade_to_selenium_4
**Word Count:** 1166
**Links Count:** 227
**Scraped:** 2025-07-17 06:15:03
**Status:** completed

---

# Upgrade to Selenium 4

Are you still using Selenium 3? This guide will help you upgrade to the latest release\!

Upgrading to Selenium 4 should be a painless process if you are using one of the officially supported languages \(Ruby, JavaScript, C\#, Python, and Java\). There might be some cases where a few issues can happen, and this guide will help you to sort them out. We will go through the steps to upgrade your project dependencies and understand the major deprecations and changes the version upgrade brings.

These are the steps we will follow to upgrade to Selenium 4:

  * Preparing our test code   * Upgrading dependencies   * Potential errors and deprecation messages

Note: while Selenium 3.x versions were being developed, support for the W3C WebDriver standard was implemented. Both this new protocol and the legacy JSON Wire Protocol were supported. Around version 3.11, Selenium code became compliant with the level W3C 1 specification. The W3C compliant code in the latest version of Selenium 3 will work as expected in Selenium 4.

## Preparing our test code

Selenium 4 removes support for the legacy protocol and uses the W3C WebDriver standard by default under the hood. For most things, this implementation will not affect end users. The major exceptions are `Capabilities` and the `Actions` class.

### Capabilities

If the test capabilities are not structured to be W3C compliant, may cause a session to not be started. Here is the list of W3C WebDriver standard capabilities:

  * `browserName`   * `browserVersion` \(replaces `version`\)   * `platformName` \(replaces `platform`\)   * `acceptInsecureCerts`   * `pageLoadStrategy`   * `proxy`   * `timeouts`   * `unhandledPromptBehavior`

An up-to-date list of standard capabilities can be found at [W3C WebDriver](https://www.w3.org/TR/webdriver1/#capabilities).

Any capability that is not contained in the list above, needs to include a vendor prefix. This applies to browser specific capabilities as well as cloud vendor specific capabilities. For example, if your cloud vendor uses `build` and `name` capabilities for your tests, you need to wrap them in a `cloud:options` block \(check with your cloud vendor for the appropriate prefix\).

#### Before

[Move Code](https://www.selenium.dev/documentation/about/contributing/#moving-examples)

  * Java   * JavaScript   * CSharp   * Ruby   * Python

              DesiredCapabilities caps = DesiredCapabilities.firefox();     caps.setCapability("platform", "Windows 10");     caps.setCapability("version", "92");     caps.setCapability("build", myTestBuild);     caps.setCapability("name", myTestName);     WebDriver driver = new RemoteWebDriver(new URL(cloudUrl), caps);                    caps = {};     caps['browserName'] = 'Firefox';     caps['platform'] = 'Windows 10';     caps['version'] = '92';     caps['build'] = myTestBuild;     caps['name'] = myTestName;                    DesiredCapabilities caps = new DesiredCapabilities();     caps.SetCapability("browserName", "firefox");     caps.SetCapability("platform", "Windows 10");     caps.SetCapability("version", "92");     caps.SetCapability("build", myTestBuild);     caps.SetCapability("name", myTestName);     var driver = new RemoteWebDriver(new Uri(CloudURL), caps);                          caps = Selenium::WebDriver::Remote::Capabilities.firefox           caps[:platform] = 'Windows 10'           caps[:version] = '92'           caps[:build] = my_test_build           caps[:name] = my_test_name           driver = Selenium::WebDriver.for :remote, url: cloud_url, desired_capabilities: caps           driver.get(url)           driver.quit

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/ruby/spec/drivers/options_spec.rb#L123-L130)

##### examples/ruby/spec/drivers/options\_spec.rb

Copy  Close               # frozen_string_literal: true          require 'spec_helper'          RSpec.describe 'Chrome' do       describe 'Driver Options' do         let(:chrome_location) { driver_finder && ENV.fetch('CHROME_BIN', nil) }         let(:url) { 'https://www.selenium.dev/selenium/web/' }              it 'page load strategy normal' do           options = Selenium::WebDriver::Options.chrome           options.page_load_strategy = :normal                driver = Selenium::WebDriver.for :chrome, options: options           driver.get(url)           driver.quit         end              it 'page load strategy eager' do           options = Selenium::WebDriver::Options.chrome           options.page_load_strategy = :eager                driver = Selenium::WebDriver.for :chrome, options: options           driver.get(url)           driver.quit         end              it 'page load strategy none' do           options = Selenium::WebDriver::Options.chrome           options.page_load_strategy = :none                driver = Selenium::WebDriver.for :chrome, options: options           driver.get(url)           driver.quit         end              it 'sets remote capabilities', skip: 'this is example code that will not execute' do           options = Selenium::WebDriver::Options.firefox           options.platform_name = 'Windows 10'           options.browser_version = 'latest'           cloud_options = {}           cloud_options[:build] = my_test_build           cloud_options[:name] = my_test_name           options.add_option('cloud:options', cloud_options)           driver = Selenium::WebDriver.for :remote, capabilities: options           driver.get(url)           driver.quit         end              it 'accepts untrusted certificates' do           options = Selenium::WebDriver::Options.chrome           options.accept_insecure_certs = true                driver = Selenium::WebDriver.for :chrome, options: options           driver.get(url)           driver.quit         end              it 'sets unhandled prompt behavior' do           options = Selenium::WebDriver::Options.chrome           options.unhandled_prompt_behavior = :accept                driver = Selenium::WebDriver.for :chrome, options: options           driver.get(url)           driver.quit         end              it 'sets window rect' do           options = Selenium::WebDriver::Options.firefox           options.set_window_rect = true                driver = Selenium::WebDriver.for :firefox, options: options           driver.get(url)           driver.quit         end              it 'sets strict file interactability' do           options = Selenium::WebDriver::Options.chrome           options.strict_file_interactability = true                driver = Selenium::WebDriver.for :chrome, options: options           driver.get(url)           driver.quit         end              it 'sets the proxy' do           options = Selenium::WebDriver::Options.chrome           options.proxy = Selenium::WebDriver::Proxy.new(http: 'myproxy.com:8080')                driver = Selenium::WebDriver.for :chrome, options: options           driver.get(url)           driver.quit         end              it 'sets the implicit timeout' do           options = Selenium::WebDriver::Options.chrome           options.timeouts = {implicit: 1}                driver = Selenium::WebDriver.for :chrome, options: options           driver.get(url)           driver.quit         end              it 'sets the page load timeout' do           options = Selenium::WebDriver::Options.chrome           options.timeouts = {page_load: 400_000}                driver = Selenium::WebDriver.for :chrome, options: options           driver.get(url)           driver.quit         end              it 'sets the script timeout' do           options = Selenium::WebDriver::Options.chrome           options.timeouts = {script: 40_000}                driver = Selenium::WebDriver.for :chrome, options: options           driver.get(url)           driver.quit         end              it 'sets capabilities in the pre-selenium 4 way', skip: 'this is example code that will not execute' do           caps = Selenium::WebDriver::Remote::Capabilities.firefox           caps[:platform] = 'Windows 10'           caps[:version] = '92'           caps[:build] = my_test_build           caps[:name] = my_test_name           driver = Selenium::WebDriver.for :remote, url: cloud_url, desired_capabilities: caps           driver.get(url)           driver.quit         end       end     end                    caps = {}     caps['browserName'] = 'firefox'     caps['platform'] = 'Windows 10'     caps['version'] = '92'     caps['build'] = my_test_build     caps['name'] = my_test_name     driver = webdriver.Remote(cloud_url, desired_capabilities=caps)     

#### After

[Move Code](https://www.selenium.dev/documentation/about/contributing/#moving-examples)

  * Java   * JavaScript   * CSharp   * Ruby   * Python

              FirefoxOptions browserOptions = new FirefoxOptions();     browserOptions.setPlatformName("Windows 10");     browserOptions.setBrowserVersion("92");     Map<String, Object> cloudOptions = new HashMap<>();     cloudOptions.put("build", myTestBuild);     cloudOptions.put("name", myTestName);     browserOptions.setCapability("cloud:options", cloudOptions);     WebDriver driver = new RemoteWebDriver(new URL(cloudUrl), browserOptions);                    capabilities = {       browserName: 'firefox',       browserVersion: '92',       platformName: 'Windows 10',       'cloud:options': {          build: myTestBuild,          name: myTestName,       }     }                    var browserOptions = new FirefoxOptions();     browserOptions.PlatformName = "Windows 10";     browserOptions.BrowserVersion = "92";     var cloudOptions = new Dictionary<string, object>();     cloudOptions.Add("build", myTestBuild);     cloudOptions.Add("name", myTestName);     browserOptions.AddAdditionalOption("cloud:options", cloudOptions);     var driver = new RemoteWebDriver(new Uri(CloudURL), browserOptions);                          options = Selenium::WebDriver::Options.firefox           options.platform_name = 'Windows 10'           options.browser_version = 'latest'           cloud_options = {}           cloud_options[:build] = my_test_build           cloud_options[:name] = my_test_name           options.add_option('cloud:options', cloud_options)           driver = Selenium::WebDriver.for :remote, capabilities: options           driver.get(url)           driver.quit

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/ruby/spec/drivers/options_spec.rb#L38-L47)

##### examples/ruby/spec/drivers/options\_spec.rb

Copy  Close               # frozen_string_literal: true          require 'spec_helper'          RSpec.describe 'Chrome' do       describe 'Driver Options' do         let(:chrome_location) { driver_finder && ENV.fetch('CHROME_BIN', nil) }         let(:url) { 'https://www.selenium.dev/selenium/web/' }              it 'page load strategy normal' do           options = Selenium::WebDriver::Options.chrome           options.page_load_strategy = :normal                driver = Selenium::WebDriver.for :chrome, options: options           driver.get(url)           driver.quit         end              it 'page load strategy eager' do           options = Selenium::WebDriver::Options.chrome           options.page_load_strategy = :eager                driver = Selenium::WebDriver.for :chrome, options: options           driver.get(url)           driver.quit         end              it 'page load strategy none' do           options = Selenium::WebDriver::Options.chrome           options.page_load_strategy = :none                driver = Selenium::WebDriver.for :chrome, options: options           driver.get(url)           driver.quit         end              it 'sets remote capabilities', skip: 'this is example code that will not execute' do           options = Selenium::WebDriver::Options.firefox           options.platform_name = 'Windows 10'           options.browser_version = 'latest'           cloud_options = {}           cloud_options[:build] = my_test_build           cloud_options[:name] = my_test_name           options.add_option('cloud:options', cloud_options)           driver = Selenium::WebDriver.for :remote, capabilities: options           driver.get(url)           driver.quit         end              it 'accepts untrusted certificates' do           options = Selenium::WebDriver::Options.chrome           options.accept_insecure_certs = true                driver = Selenium::WebDriver.for :chrome, options: options           driver.get(url)           driver.quit         end              it 'sets unhandled prompt behavior' do           options = Selenium::WebDriver::Options.chrome           options.unhandled_prompt_behavior = :accept                driver = Selenium::WebDriver.for :chrome, options: options           driver.get(url)           driver.quit         end              it 'sets window rect' do           options = Selenium::WebDriver::Options.firefox           options.set_window_rect = true                driver = Selenium::WebDriver.for :firefox, options: options           driver.get(url)           driver.quit         end              it 'sets strict file interactability' do           options = Selenium::WebDriver::Options.chrome           options.strict_file_interactability = true                driver = Selenium::WebDriver.for :chrome, options: options           driver.get(url)           driver.quit         end              it 'sets the proxy' do           options = Selenium::WebDriver::Options.chrome           options.proxy = Selenium::WebDriver::Proxy.new(http: 'myproxy.com:8080')                driver = Selenium::WebDriver.for :chrome, options: options           driver.get(url)           driver.quit         end              it 'sets the implicit timeout' do           options = Selenium::WebDriver::Options.chrome           options.timeouts = {implicit: 1}                driver = Selenium::WebDriver.for :chrome, options: options           driver.get(url)           driver.quit         end              it 'sets the page load timeout' do           options = Selenium::WebDriver::Options.chrome           options.timeouts = {page_load: 400_000}                driver = Selenium::WebDriver.for :chrome, options: options           driver.get(url)           driver.quit         end              it 'sets the script timeout' do           options = Selenium::WebDriver::Options.chrome           options.timeouts = {script: 40_000}                driver = Selenium::WebDriver.for :chrome, options: options           driver.get(url)           driver.quit         end              it 'sets capabilities in the pre-selenium 4 way', skip: 'this is example code that will not execute' do           caps = Selenium::WebDriver::Remote::Capabilities.firefox           caps[:platform] = 'Windows 10'           caps[:version] = '92'           caps[:build] = my_test_build           caps[:name] = my_test_name           driver = Selenium::WebDriver.for :remote, url: cloud_url, desired_capabilities: caps           driver.get(url)           driver.quit         end       end     end                    from selenium.webdriver.firefox.options import Options as FirefoxOptions     options = FirefoxOptions()     options.browser_version = '92'     options.platform_name = 'Windows 10'     cloud_options = {}     cloud_options['build'] = my_test_build     cloud_options['name'] = my_test_name     options.set_capability('cloud:options', cloud_options)     driver = webdriver.Remote(cloud_url, options=options)     

### Find element\(s\) utility methods in Java

The utility methods to find elements in the Java bindings \(`FindsBy` interfaces\) have been removed as they were meant for internal use only. The following code samples explain this better.

Finding a single element with `findElement*`

Before               driver.findElementByClassName("className");     driver.findElementByCssSelector(".className");     driver.findElementById("elementId");     driver.findElementByLinkText("linkText");     driver.findElementByName("elementName");     driver.findElementByPartialLinkText("partialText");     driver.findElementByTagName("elementTagName");     driver.findElementByXPath("xPath");     

After               driver.findElement(By.className("className"));     driver.findElement(By.cssSelector(".className"));     driver.findElement(By.id("elementId"));     driver.findElement(By.linkText("linkText"));     driver.findElement(By.name("elementName"));     driver.findElement(By.partialLinkText("partialText"));     driver.findElement(By.tagName("elementTagName"));     driver.findElement(By.xpath("xPath"));     

Finding a multiple elements with `findElements*`

Before               driver.findElementsByClassName("className");     driver.findElementsByCssSelector(".className");     driver.findElementsById("elementId");     driver.findElementsByLinkText("linkText");     driver.findElementsByName("elementName");     driver.findElementsByPartialLinkText("partialText");     driver.findElementsByTagName("elementTagName");     driver.findElementsByXPath("xPath");     

After               driver.findElements(By.className("className"));     driver.findElements(By.cssSelector(".className"));     driver.findElements(By.id("elementId"));     driver.findElements(By.linkText("linkText"));     driver.findElements(By.name("elementName"));     driver.findElements(By.partialLinkText("partialText"));     driver.findElements(By.tagName("elementTagName"));     driver.findElements(By.xpath("xPath"));     

## Upgrading dependencies

Check the subsections below to install Selenium 4 and have your project dependencies upgraded.

### Java

The process of upgrading Selenium depends on which build tool is being used. We will cover the most common ones for Java, which are [Maven](https://maven.apache.org/) and [Gradle](https://gradle.org/). The minimum Java version required is still 8.

#### Maven

Before               <dependencies>       <!-- more dependencies ... -->       <dependency>         <groupId>org.seleniumhq.selenium</groupId>         <artifactId>selenium-java</artifactId>         <version>3.141.59</version>       </dependency>       <!-- more dependencies ... -->     </dependencies>     

After               <dependencies>         <!-- more dependencies ... -->         <dependency>             <groupId>org.seleniumhq.selenium</groupId>             <artifactId>selenium-java</artifactId>             <version>4.4.0</version>         </dependency>         <!-- more dependencies ... -->     </dependencies>     

After making the change, you could execute `mvn clean compile` on the same directory where the `pom.xml` file is.

#### Gradle

Before               plugins {         id 'java'     }     group 'org.example'     version '1.0-SNAPSHOT'     repositories {         mavenCentral()     }     dependencies {         testImplementation 'org.junit.jupiter:junit-jupiter-api:5.7.0'         testRuntimeOnly 'org.junit.jupiter:junit-jupiter-engine:5.7.0'         implementation group: 'org.seleniumhq.selenium', name: 'selenium-java', version: '3.141.59'     }     test {         useJUnitPlatform()     }     

After               plugins {         id 'java'     }     group 'org.example'     version '1.0-SNAPSHOT'     repositories {         mavenCentral()     }     dependencies {         testImplementation 'org.junit.jupiter:junit-jupiter-api:5.7.0'         testRuntimeOnly 'org.junit.jupiter:junit-jupiter-engine:5.7.0'         implementation group: 'org.seleniumhq.selenium', name: 'selenium-java', version: '4.4.0'     }     test {         useJUnitPlatform()     }     

After making the change, you could execute `./gradlew clean build` on the same directory where the `build.gradle` file is.

To check all the Java releases, you can head to [MVNRepository](https://mvnrepository.com/artifact/org.seleniumhq.selenium/selenium-java).

### C\#

The place to get updates for Selenium 4 in C\# is [NuGet](https://www.nuget.org/). Under the [`Selenium.WebDriver`](https://www.nuget.org/packages/Selenium.WebDriver/4.4.0) package you can get the instructions to update to the latest version. Inside of Visual Studio, through the NuGet Package Manager you can execute:               PM> Install-Package Selenium.WebDriver -Version 4.4.0     

### Python

The most important change to use Python is the minimum required version. Selenium 4 will require a minimum Python 3.7 or higher. More details can be found at the [Python Package Index](https://pypi.org/project/selenium/4.4.3/). To upgrade from the command line, you can execute:               pip install selenium==4.4.3     

### Ruby

The update details for Selenium 4 can be seen at the [selenium-webdriver](https://rubygems.org/gems/selenium-webdriver/versions/4.4.0) gem in RubyGems. To install the latest version, you can execute:               gem install selenium-webdriver     

To add it to your Gemfile:               gem 'selenium-webdriver', '~> 4.4.0'     

### JavaScript

The selenium-webdriver package can be found at the Node package manager, [npmjs](https://www.npmjs.com). Selenium 4 can be found [here](https://www.npmjs.com/package/selenium-webdriver/v/4.4.0). To install it, you could either execute:               npm install selenium-webdriver     

Or, update your package.json and run` npm install`:               {       "name": "selenium-tests",       "version": "1.0.0",       "dependencies": {         "selenium-webdriver": "^4.4.0"       }     }     

## Potential errors and deprecation messages

Here is a set of code examples that will help to overcome the deprecation messages you might encounter after upgrading to Selenium 4.

### Java

#### Waits and Timeout

The parameters received in Timeout have switched from expecting `(long time, TimeUnit unit)` to expect `(Duration duration)`.

Before               driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);     driver.manage().timeouts().setScriptTimeout(2, TimeUnit.MINUTES);     driver.manage().timeouts().pageLoadTimeout(10, TimeUnit.SECONDS);     

After               driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));     driver.manage().timeouts().scriptTimeout(Duration.ofMinutes(2));     driver.manage().timeouts().pageLoadTimeout(Duration.ofSeconds(10));     

Waits are also expecting different parameters now. `WebDriverWait` is now expecting a `Duration` instead of a `long` for timeout in seconds and milliseconds. The `withTimeout` and `pollingEvery` utility methods from `FluentWait` have switched from expecting `(long time, TimeUnit unit)` to expect `(Duration duration)`.

Before               new WebDriverWait(driver, 3)     .until(ExpectedConditions.elementToBeClickable(By.cssSelector("#id")));          Wait<WebDriver> wait = new FluentWait<WebDriver>(driver)       .withTimeout(30, TimeUnit.SECONDS)       .pollingEvery(5, TimeUnit.SECONDS)       .ignoring(NoSuchElementException.class);     

After               new WebDriverWait(driver, Duration.ofSeconds(3))       .until(ExpectedConditions.elementToBeClickable(By.cssSelector("#id")));            Wait<WebDriver> wait = new FluentWait<WebDriver>(driver)       .withTimeout(Duration.ofSeconds(30))       .pollingEvery(Duration.ofSeconds(5))       .ignoring(NoSuchElementException.class);     

#### Merging capabilities is no longer changing the calling object

It was possible to merge a different set of capabilities into another set, and it was mutating the calling object. Now, the result of the merge operation needs to be assigned.

Before               MutableCapabilities capabilities = new MutableCapabilities();     capabilities.setCapability("platformVersion", "Windows 10");     FirefoxOptions options = new FirefoxOptions();     options.setHeadless(true);     options.merge(capabilities);          // As a result, the `options` object was getting modified.     

After               MutableCapabilities capabilities = new MutableCapabilities();     capabilities.setCapability("platformVersion", "Windows 10");     FirefoxOptions options = new FirefoxOptions();     options.setHeadless(true);     options = options.merge(capabilities);          // The result of the `merge` call needs to be assigned to an object.     

#### Firefox Legacy

Before GeckoDriver was around, the Selenium project had a driver implementation to automate Firefox \(version <48\). However, this implementation is not needed anymore as it does not work in recent versions of Firefox. To avoid major issues when upgrading to Selenium 4, the `setLegacy` option will be shown as deprecated. The recommendation is to stop using the old implementation and rely only on GeckoDriver. The following code will show the `setLegacy` line deprecated after upgrading.               FirefoxOptions options = new FirefoxOptions();     options.setLegacy(true);     

#### `BrowserType`

The `BrowserType` interface has been around for a long time, however it is getting deprecated in favour of the new `Browser` interface.

Before               MutableCapabilities capabilities = new MutableCapabilities();     capabilities.setCapability("browserVersion", "92");     capabilities.setCapability("browserName", BrowserType.FIREFOX);     

After               MutableCapabilities capabilities = new MutableCapabilities();     capabilities.setCapability("browserVersion", "92");     capabilities.setCapability("browserName", Browser.FIREFOX);     

### C\#

#### `AddAdditionalCapability` is deprecated

Instead of it, `AddAdditionalOption` is recommended. Here is an example showing this:

Before               var browserOptions = new ChromeOptions();     browserOptions.PlatformName = "Windows 10";     browserOptions.BrowserVersion = "latest";     var cloudOptions = new Dictionary<string, object>();     browserOptions.AddAdditionalCapability("cloud:options", cloudOptions, true);     

After               var browserOptions = new ChromeOptions();     browserOptions.PlatformName = "Windows 10";     browserOptions.BrowserVersion = "latest";     var cloudOptions = new Dictionary<string, object>();     browserOptions.AddAdditionalOption("cloud:options", cloudOptions);     

### Python

#### `executable_path has been deprecated, please pass in a Service object`

In Selenium 4, you’ll need to set the driver’s `executable_path` from a Service object to prevent deprecation warnings. \(Or don’t set the path and instead make sure that the driver you need is on the System PATH.\)

Before               from selenium import webdriver     options = webdriver.ChromeOptions()     driver = webdriver.Chrome(         executable_path=CHROMEDRIVER_PATH,          options=options     )     

After               from selenium import webdriver     from selenium.webdriver.chrome.service import Service as ChromeService     options = webdriver.ChromeOptions()     service = ChromeService(executable_path=CHROMEDRIVER_PATH)     driver = webdriver.Chrome(service=service, options=options)     

## Summary

We went through the major changes to be taken into consideration when upgrading to Selenium 4. Covering the different aspects to cover when test code is prepared for the upgrade, including suggestions on how to prevent potential issues that can show up when using the new version of Selenium. To finalize, we also covered a set of possible issues that you can bump into after upgrading, and we shared potential fixes for those issues.

_This was originally posted at<https://saucelabs.com/resources/articles/how-to-upgrade-to-selenium-4>_

Last modified April 29, 2024: [Upgrade selenium 4 ruby examples & rendering issue \(\#1695\)\[deploy site\] \(76d80d0a98a\)](https://github.com/SeleniumHQ/seleniumhq.github.io/commit/76d80d0a98a75cd30aaa6034d5ccea6f01214061)