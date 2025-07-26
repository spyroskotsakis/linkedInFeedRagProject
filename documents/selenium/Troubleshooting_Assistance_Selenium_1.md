# Troubleshooting Assistance | Selenium

**URL:** https://www.selenium.dev/documentation/webdriver/troubleshooting/_print
**Word Count:** 4551
**Links Count:** 124
**Scraped:** 2025-07-17 06:17:48
**Status:** completed

---

This is the multi-page printable view of this section. Click here to print.

[Return to the regular view of this page](https://www.selenium.dev/documentation/webdriver/troubleshooting/).

# Troubleshooting Assistance

How to solve WebDriver problems.

  * 1: Understanding Common Errors     * 1.1: Unable to Locate Driver Error   * 2: Logging Selenium commands   * 3: Upgrade to Selenium 4

It is not always obvious the root cause of errors in Selenium.

  1. The most common Selenium-related error is a result of poor synchronization. Read about [Waiting Strategies](https://www.selenium.dev/documentation/webdriver/waits/). If you aren’t sure if it is a synchronization strategy you can try _temporarily_ hard coding a large sleep where you see the issue, and you’ll know if adding an explicit wait can help.

  2. Note that many errors that get reported to the project are actually caused by issues in the underlying drivers that Selenium sends the commands to. You can rule out a driver problem by executing the command in multiple [browsers](https://www.selenium.dev/documentation/webdriver/browsers/).

  3. If you have questions about how to do things, check out the [Support options](https://www.selenium.dev/support/) for ways get assistance.

  4. If you think you’ve found a problem with Selenium code, go ahead and file a [Bug Report](https://github.com/SeleniumHQ/selenium/issues/new?assignees=&labels=I-defect%2Cneeds-triaging&template=bug-report.yml&title=%5B%F0%9F%90%9B+Bug%5D%3A+) on GitHub.

# 1 - Understanding Common Errors

How to solve various problems in your Selenium code.

## InvalidSelectorException

CSS and XPath Selectors are sometimes difficult to get correct.

### Likely Cause

The CSS or XPath selector you are trying to use has invalid characters or an invalid query.

### Possible Solutions

Run your selector through a validator service:

  * [CSS Validator](http://csslint.net/)   * [xPath Validator](http://www.freeformatter.com/xpath-tester.html)

Or use a browser extension to get a known good value:

  * [SelectorsHub](https://selectorshub.com/selectorshub/)

## NoSuchElementException

The element can not be found at the exact moment you attempted to locate it.

### Likely Cause

  * You are looking for the element in the wrong place \(perhaps a previous action was unsuccessful\).   * You are looking for the element at the wrong time \(the element has not shown up in the DOM, yet\)   * The locator has changed since you wrote the code

### Possible Solutions

  * Make sure you are on the page you expect to be on, and that previous actions in your code completed correctly   * Make sure you are using a proper [Waiting Strategy](https://www.selenium.dev/documentation/webdriver/waits/)   * Update the locator with the browser’s devtools console or use a browser extension like:     * [SelectorsHub](https://selectorshub.com/selectorshub/)

## StaleElementReferenceException

An element goes stale when it was previously located, but can not be currently accessed. Elements do not get relocated automatically; the driver creates a reference ID for the element and has a particular place it expects to find it in the DOM. If it can not find the element in the current DOM, any action using that element will result in this exception.

### Likely Cause

This can happen when:

  * You have refreshed the page, or the DOM of the page has dynamically changed.   * You have navigated to a different page.   * You have switched to another window or into or out of a frame or iframe.

### Possible Solutions

**The DOM has changed**

When the page is refreshed or items on the page have moved around, there is still an element with the desired locator on the page, it is just no longer accessible by the element object being used, and the element must be relocated before it can be used again. This is often done in one of two ways:

  * Always relocate the element every time you go to use it. The likelihood of the element going stale in the microseconds between locating and using the element is small, though possible. The downside is that this is not the most efficient approach, especially when running on a remote grid.

  * Wrap the Web Element with another object that stores the locator, and caches the located Selenium element. When taking actions with this wrapped object, you can attempt to use the cached object if previously located, and if it is stale, exception can be caught, the element relocated with the stored locator, and the method re-tried. This is more efficient, but it can cause problems if the locator you’re using references a different element \(and not the one you want\) after the page has changed.

**The Context has changed**

Element objects are stored for a given context, so if you move to a different context — like a different window or a different frame or iframe — the element reference will still be valid, but will be temporarily inaccessible. In this scenario, it won’t help to relocate the element, because it doesn’t exist in the current context. To fix this, you need to make sure to switch back to the correct context before using the element.

**The Page has changed**

This scenario is when you haven’t just changed contexts, you have navigated to another page and have destroyed the context in which the element was located. You can’t just relocate it from the current context, and you can’t switch back to an active context where it is valid. If this is the reason for your error, you must both navigate back to the correct location and relocate it.

## ElementClickInterceptedException

This exception occurs when Selenium tries to click an element, but the click would instead be received by a different element. Before Selenium will click an element, it checks if the element is visible, unobscured by any other elements, and enabled - if the element is obscured, it will raise this exception.

### Likely Cause

**UI Elements Overlapping**

Elements on the UI are typically placed next to each other, but occasionally elements may overlap. For example, a navbar always staying at the top of your window as you scroll a page. If that navbar happens to be covering an element we are trying to click, Selenium might believe it to be visible and enabled, but when you try to click it will throw this exception. Pop-ups and Modals are also common offenders here.

**Animations**

Elements with animations have the potential to cause this exception as well - it is recommended to wait for animations to cease before attempting to click an element.

### Possible Solutions

**Use Explicit Waits**

[Explicit Waits](https://www.selenium.dev/documentation/webdriver/waits/) will likely be your best friend in these instances. A great way is to use `ExpectedCondition.ToBeClickable()` with `WebDriverWait` to wait until the right moment.

**Scroll the Element into View**

In instances where the element is out of view, but Selenium still registers the element as visible \(e.g. navbars overlapping a section at the top of your screen\), you can use the `WebDriver.executeScript()` method to execute a javascript function to scroll \(e.g. `WebDriver.executeScript('window.scrollBy(0,-250)')`\) or you can utilize the Actions class with `Actions.moveToElement(element)`.

## InvalidSessionIdException

Sometimes the session you’re trying to access is different than what’s currently available

### Likely Cause

This usually occurs when the session has been deleted \(e.g. `driver.quit()`\) or if the session has changed, like when the last tab/browser has closed \(e.g. `driver.close()`\)

### Possible Solutions

Check your script for instances of `driver.close()` and `driver.quit()`, and any other possible causes of closed tabs/browsers. It could be that you are locating an element before you should/can.

## SessionNotCreatedException

This exception occurs when the WebDriver is unable to create a new session for the browser. This often happens due to version mismatches, system-level restrictions, or configuration issues.

### Likely Cause

  * The browser version and WebDriver version are incompatible \(e.g., ChromeDriver v113 with Chrome v115\).   * macOS privacy settings may block the WebDriver from running.   * The WebDriver binary is missing, inaccessible, or lacks the necessary execution permissions \(e.g., on Linux/macOS, the driver file may not be executable\).

### Possible Solutions

  * Ensure the WebDriver version matches the browser version. For Chrome, check the browser version at `chrome://settings/help` and download the matching driver from [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads).   * On macOS, go to **System Settings > Privacy & Security**, and allow the driver to run if blocked.   * Verify the driver binary is executable \(`chmod +x /path/to/driver` on Linux/macOS\).

## ElementNotInteractableException

This exception occurs when Selenium tries to interact with an element that is not interactable in its current state.

### Likely Cause

  1. **Unsupported Operation** : Performing an action, like `sendKeys`, on an element that doesn’t support it \(e.g., `<form>` or `<label>`\).   2. **Multiple Elements Matching Locator** : The locator targets a non-interactable element, such as a `<td>` tag, instead of the intended `<input>` field.   3. **Hidden Elements** : The element is present in the DOM but not visible on the page due to CSS, the `hidden` attribute, or being outside the visible viewport.

### Possible Solutions

  1. Use actions appropriate for the element type \(e.g., use `sendKeys` with `<input>` fields only\).   2. Ensure locators uniquely identify the intended element to avoid incorrect matches.   3. Check if the element is visible on the page before interacting with it. Use scrolling to bring the element into view, if required.   4. Use explicit waits to ensure the element is interactable before performing actions.

## ElementNotVisibleException

This exception is thrown when the element you are trying to interact with _is_ present in the DOM, but is not visible.

### Likely Cause

This can occur in several situations:

  * Another element is blocking your intended element   * The element is disabled/invisible to the user

### Possible Solutions

This issue cannot always be resolved on the user’s end, however when it can it is usually solved by the following: using an explicit wait, or interacting with the page in such a way to make the element visible \(scrolling, clicking a button, etc.\)

# 1.1 - Unable to Locate Driver Error

Troubleshooting missing path to driver executable.

Historically, this is the most common error beginning Selenium users get when trying to run code for the first time:

  * Java   * Python   * CSharp   * Ruby

The path to the driver executable must be set by the webdriver.chrome.driver system property; for more information, see https://chromedriver.chromium.org/. The latest version can be downloaded from https://chromedriver.chromium.org/downloads

The executable chromedriver needs to be available in the path.

The file geckodriver does not exist. The driver can be downloaded at https://github.com/mozilla/geckodriver/releases"

Unable to locate the chromedriver executable;

## Likely cause

Through WebDriver, Selenium supports all major browsers. In order to drive the requested browser, Selenium needs to send commands to it via an executable driver. This error means the necessary driver could not be found by any of the means Selenium attempts to use.

## Possible solutions

There are several ways to ensure Selenium gets the driver it needs.

### Use the latest version of Selenium

As of Selenium 4.6, Selenium downloads the correct driver for you. You shouldn’t need to do anything. If you are using the latest version of Selenium and you are getting an error, please [turn on logging](https://www.selenium.dev/documentation/webdriver/troubleshooting/logging/) and [file a bug report](https://github.com/seleniumhq/selenium/issues) with that information.

If you want to read more information about how Selenium manages driver downloads for you, you can read about the [Selenium Manager](https://www.selenium.dev/documentation/selenium_manager/).

### Use the `PATH` environment variable

This option first requires manually [downloading the driver](https://www.selenium.dev/documentation/webdriver/troubleshooting/errors/driver_location/#download-the-driver).

This is a flexible option to change location of drivers without having to update your code, and will work on multiple machines without requiring that each machine put the drivers in the same place.

You can either place the drivers in a directory that is already listed in `PATH`, or you can place them in a directory and add it to `PATH`.

  * Bash   * Zsh   * Windows

To see what directories are already on `PATH`, open a Terminal and execute:               echo $PATH     

If the location to your driver is not already in a directory listed, you can add a new directory to PATH:               echo 'export PATH=$PATH:/path/to/driver' >> ~/.bash_profile     source ~/.bash_profile     

You can test if it has been added correctly by checking the version of the driver:               chromedriver --version     

To see what directories are already on `PATH`, open a Terminal and execute:               echo $PATH     

If the location to your driver is not already in a directory listed, you can add a new directory to PATH:               echo 'export PATH=$PATH:/path/to/driver' >> ~/.zshenv     source ~/.zshenv     

You can test if it has been added correctly by checking the version of the driver:               chromedriver --version     

To see what directories are already on `PATH`, open a Command Prompt and execute:               echo %PATH%     

If the location to your driver is not already in a directory listed, you can add a new directory to PATH:               setx PATH "%PATH%;C:\WebDriver\bin"     

You can test if it has been added correctly by checking the version of the driver:               chromedriver.exe --version     

### Specify the location of the driver

If you cannot upgrade to the latest version of Selenium, you do not want Selenium to download drivers for you, and you can’t figure out the environment variables, you can specify the location of the driver in the Service object.

You first need to [download the desired driver](https://www.selenium.dev/documentation/webdriver/troubleshooting/errors/driver_location/#download-the-driver), then create an instance of the applicable `Service` class and [set the path](https://www.selenium.dev/documentation/webdriver/drivers/service/#driver-location).

Specifying the location in the code itself has the advantage of not needing to figure out Environment Variables on your system, but has the drawback of making the code less flexible.

### Driver management libraries

Before Selenium managed drivers itself, other projects were created to do so for you.

If you can’t use Selenium Manager because you are using an older version of Selenium \(please upgrade\), or need an advanced feature not yet implemented by Selenium Manager, you might try one of these tools to keep your drivers automatically updated:

  * [WebDriverManager](https://github.com/bonigarcia/webdrivermanager) \(Java\)   * [WebDriver Manager](https://github.com/SergeyPirogov/webdriver_manager) \(Python\)   * [WebDriver Manager Package](https://github.com/rosolko/WebDriverManager.Net) \(.NET\)   * [webdrivers gem](https://github.com/titusfortner/webdrivers) \(Ruby\)

## Download the driver

Browser| Supported OS| Maintained by| Download| Issue Tracker   ---|---|---|---|---   Chromium/Chrome| Windows/macOS/Linux| Google| [Downloads](https://www.selenium.dev/downloads/)| [Issues](https://bugs.chromium.org/p/chromedriver/issues/list)   Firefox| Windows/macOS/Linux| Mozilla| [Downloads](https://github.com/mozilla/geckodriver/releases)| [Issues](https://github.com/mozilla/geckodriver/issues)   Edge| Windows/macOS/Linux| Microsoft| [Downloads](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)| [Issues](https://github.com/MicrosoftEdge/EdgeWebDriver/issues)   Internet Explorer| Windows| Selenium Project| [Downloads](https://www.selenium.dev/downloads/)| [Issues](https://github.com/SeleniumHQ/selenium/labels/D-IE)   Safari| macOS High Sierra and newer| Apple| Built in| [Issues](https://bugreport.apple.com/logon)      Note: The Opera driver no longer works with the latest functionality of Selenium and is currently officially unsupported.

# 2 - Logging Selenium commands

Getting information about Selenium execution.

Turning on logging is a valuable way to get extra information that might help you determine why you might be having a problem.

## Getting a logger

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

Java logs are typically created per class. You can work with the default logger to work with all loggers. To filter out specific classes, see [Filtering](https://www.selenium.dev/documentation/webdriver/troubleshooting/logging/#logger-filtering)

Get the root logger:                       Logger logger = Logger.getLogger("");

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/java/src/test/java/dev/selenium/troubleshooting/LoggingTest.java#L31)

##### /examples/java/src/test/java/dev/selenium/troubleshooting/LoggingTest.java

Copy  Close               package dev.selenium.troubleshooting;          import java.io.IOException;     import java.nio.file.Files;     import java.nio.file.Paths;     import java.util.Arrays;     import java.util.logging.FileHandler;     import java.util.logging.Handler;     import java.util.logging.Level;     import java.util.logging.Logger;          import org.junit.jupiter.api.AfterEach;     import org.junit.jupiter.api.Assertions;     import org.junit.jupiter.api.Test;     import org.openqa.selenium.manager.SeleniumManager;     import org.openqa.selenium.remote.RemoteWebDriver;          public class LoggingTest {              @AfterEach         public void loggingOff() {             Logger logger = Logger.getLogger("");             logger.setLevel(Level.INFO);             Arrays.stream(logger.getHandlers()).forEach(handler -> {                 handler.setLevel(Level.INFO);             });         }              @Test         public void logging() throws IOException {             Logger logger = Logger.getLogger("");             logger.setLevel(Level.FINE);             Arrays.stream(logger.getHandlers()).forEach(handler -> {                 handler.setLevel(Level.FINE);             });                  Handler handler = new FileHandler("selenium.xml");             logger.addHandler(handler);                  Logger.getLogger(RemoteWebDriver.class.getName()).setLevel(Level.FINEST);             Logger.getLogger(SeleniumManager.class.getName()).setLevel(Level.SEVERE);                  Logger localLogger = Logger.getLogger(this.getClass().getName());             localLogger.warning("this is a warning");             localLogger.info("this is useful information");             localLogger.fine("this is detailed debug information");                  byte[] bytes = Files.readAllBytes(Paths.get("selenium.xml"));             String fileContent = new String(bytes);                  Assertions.assertTrue(fileContent.contains("this is a warning"));             Assertions.assertTrue(fileContent.contains("this is useful information"));             Assertions.assertTrue(fileContent.contains("this is detailed debug information"));         }     }     

Java Logging is not exactly straightforward, and if you are just looking for an easy way to look at the important Selenium logs, take a look at the [Selenium Logger project](https://github.com/titusfortner/selenium-logger#selenium-logger)

Python logs are typically created per module. You can match all submodules by referencing the top level module. So to work with all loggers in selenium module, you can do this:                   logger = logging.getLogger('selenium')

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/python/tests/troubleshooting/test_logging.py#L5)

##### /examples/python/tests/troubleshooting/test\_logging.py

Copy  Close               import logging               def test_logging(log_path):         logger = logging.getLogger('selenium')              logger.setLevel(logging.DEBUG)              handler = logging.FileHandler(log_path)         logger.addHandler(handler)              logging.getLogger('selenium.webdriver.remote').setLevel(logging.WARN)         logging.getLogger('selenium.webdriver.common').setLevel(logging.DEBUG)              logger.info("this is useful information")         logger.warning("this is a warning")         logger.debug("this is detailed debug information")              with open(log_path, 'r') as fp:             assert len(fp.readlines()) == 3     

You must also create and add a log handler \(`StreamHandler`, `FileHandler`, etc\).

To save logs to a file, you can do this:               log_path = '/path/to/log'     handler = logging.FileHandler(log_path)     logger.addHandler(handler)     

To display logs in the console, you can do this:               handler = logging.StreamHandler()     logger.addHandler(handler)     

.NET logger is managed with a static class, so all access to logging is managed simply by referencing `Log` from the `OpenQA.Selenium.Internal.Logging` namespace.

If you want to see as much debugging as possible in all the classes, you can turn on debugging globally in Ruby by setting `$DEBUG = true`.

For more fine-tuned control, Ruby Selenium created its own Logger class to wrap the default `Logger` class. This implementation provides some interesting additional features. Obtain the logger directly from the `#logger`class method on the `Selenium::WebDriver` module:

[Selenium v4.10](https://github.com/SeleniumHQ/selenium/releases/tag/selenium-4.10.0)                   logger = Selenium::WebDriver.logger

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/ruby/spec/troubleshooting/logging_spec.rb#L11)

##### /examples/ruby/spec/troubleshooting/logging\_spec.rb

Copy  Close               # frozen_string_literal: true          require 'spec_helper'          RSpec.describe 'Logging' do       let(:file_name) { Tempfile.new('logging').path }            after { FileUtils.rm_f(file_name) }            it 'logs things' do         logger = Selenium::WebDriver.logger              logger.level = :debug              logger.output = file_name              logger.ignore(:jwp_caps, :logger_info)         logger.allow(%i[selenium_manager example_id])              logger.warn('this is a warning', id: :example_id)         logger.info('this is useful information', id: :example_id)         logger.debug('this is detailed debug information', id: :example_id)              expect(File.readlines(file_name).grep(/\[:example_id\]/).size).to eq 3       end     end                    const logging = require('selenium-webdriver/lib/logging')     logger = logging.getLogger('webdriver')     

## Content Help

**Note:** This section needs additional and/or updated content      Check our [contribution guidelines](https://www.selenium.dev/documentation/about/contributing/) if you’d like to help.

## Logger level

Logger level helps to filter out logs based on their severity.

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

Java has 7 logger levels: `SEVERE`, `WARNING`, `INFO`, `CONFIG`, `FINE`, `FINER`, and `FINEST`. The default is `INFO`.

You have to change both the level of the logger and the level of the handlers on the root logger:                       logger.setLevel(Level.FINE);             Arrays.stream(logger.getHandlers()).forEach(handler -> {                 handler.setLevel(Level.FINE);             });

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/java/src/test/java/dev/selenium/troubleshooting/LoggingTest.java#L32-L35)

##### /examples/java/src/test/java/dev/selenium/troubleshooting/LoggingTest.java

Copy  Close               package dev.selenium.troubleshooting;          import java.io.IOException;     import java.nio.file.Files;     import java.nio.file.Paths;     import java.util.Arrays;     import java.util.logging.FileHandler;     import java.util.logging.Handler;     import java.util.logging.Level;     import java.util.logging.Logger;          import org.junit.jupiter.api.AfterEach;     import org.junit.jupiter.api.Assertions;     import org.junit.jupiter.api.Test;     import org.openqa.selenium.manager.SeleniumManager;     import org.openqa.selenium.remote.RemoteWebDriver;          public class LoggingTest {              @AfterEach         public void loggingOff() {             Logger logger = Logger.getLogger("");             logger.setLevel(Level.INFO);             Arrays.stream(logger.getHandlers()).forEach(handler -> {                 handler.setLevel(Level.INFO);             });         }              @Test         public void logging() throws IOException {             Logger logger = Logger.getLogger("");             logger.setLevel(Level.FINE);             Arrays.stream(logger.getHandlers()).forEach(handler -> {                 handler.setLevel(Level.FINE);             });                  Handler handler = new FileHandler("selenium.xml");             logger.addHandler(handler);                  Logger.getLogger(RemoteWebDriver.class.getName()).setLevel(Level.FINEST);             Logger.getLogger(SeleniumManager.class.getName()).setLevel(Level.SEVERE);                  Logger localLogger = Logger.getLogger(this.getClass().getName());             localLogger.warning("this is a warning");             localLogger.info("this is useful information");             localLogger.fine("this is detailed debug information");                  byte[] bytes = Files.readAllBytes(Paths.get("selenium.xml"));             String fileContent = new String(bytes);                  Assertions.assertTrue(fileContent.contains("this is a warning"));             Assertions.assertTrue(fileContent.contains("this is useful information"));             Assertions.assertTrue(fileContent.contains("this is detailed debug information"));         }     }     

Python has 6 logger levels: `CRITICAL`, `ERROR`, `WARNING`, `INFO`, `DEBUG`, and `NOTSET`. The default is `WARNING`

To change the level of the logger:                   logger.setLevel(logging.DEBUG)

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/python/tests/troubleshooting/test_logging.py#L7)

##### /examples/python/tests/troubleshooting/test\_logging.py

Copy  Close               import logging               def test_logging(log_path):         logger = logging.getLogger('selenium')              logger.setLevel(logging.DEBUG)              handler = logging.FileHandler(log_path)         logger.addHandler(handler)              logging.getLogger('selenium.webdriver.remote').setLevel(logging.WARN)         logging.getLogger('selenium.webdriver.common').setLevel(logging.DEBUG)              logger.info("this is useful information")         logger.warning("this is a warning")         logger.debug("this is detailed debug information")              with open(log_path, 'r') as fp:             assert len(fp.readlines()) == 3     

Things get complicated when you use PyTest, though. By default, PyTest hides logging unless the test fails. You need to set 3 things to get PyTest to display logs on passing tests.

To always output logs with PyTest you need to run with additional arguments. First, `-s` to prevent PyTest from capturing the console. Second, `-p no:logging`, which allows you to override the default PyTest logging settings so logs can be displayed regardless of errors.

So you need to set these flags in your IDE, or run PyTest on command line like:               pytest -s -p no:logging     

Finally, since you turned off logging in the arguments above, you now need to add configuration to turn it back on:               logging.basicConfig(level=logging.WARN)     

.NET has 6 logger levels: `Error`, `Warn`, `Info`, `Debug`, `Trace` and `None`. The default level is `Info`.

To change the level of the logger:                           Log.SetLevel(LogEventLevel.Trace);

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/dotnet/SeleniumDocs/Troubleshooting/LoggingTest.cs#L18)

##### /examples/dotnet/SeleniumDocs/Troubleshooting/LoggingTest.cs

Copy  Close               ﻿using Microsoft.VisualStudio.TestTools.UnitTesting;     using OpenQA.Selenium;     using OpenQA.Selenium.Internal.Logging;     using OpenQA.Selenium.Remote;     using System;     using System.IO;          namespace SeleniumDocs.Troubleshooting     {         [TestClass]         public class LoggingTest         {             private const string filePath = "Selenium.log";                  [TestMethod]             public void Logging()             {                 Log.SetLevel(LogEventLevel.Trace);                      Log.Handlers.Add(new FileLogHandler(filePath));                      Log.SetLevel(typeof(RemoteWebDriver), LogEventLevel.Debug);                 Log.SetLevel(typeof(SeleniumManager), LogEventLevel.Info);                      Warn("this is a warning");                 Info("this is useful information");                 Debug("this is detailed debug information");                      using (var fileStream = File.Open(filePath, FileMode.Open, FileAccess.Read, FileShare.ReadWrite))                 {                     using (var streamReader = new StreamReader(fileStream))                     {                         var fileLogContent = streamReader.ReadToEnd();                              StringAssert.Contains(fileLogContent, "this is a warning");                         StringAssert.Contains(fileLogContent, "this is useful information");                         StringAssert.Contains(fileLogContent, "this is detailed debug information");                     }                 }             }                  [TestCleanup]             public void TestCleanup()             {                 // reset log to default                 Log.SetLevel(LogEventLevel.Info)                     .Handlers.Clear()                     .Handlers.Add(new ConsoleLogHandler());             }                  // logging is only for internal usage             // hacking it via reflection                  private void Debug(string message)             {                 LogMessage("Debug", message);             }                  private void Warn(string message)             {                 LogMessage("Warn", message);             }                  private void Info(string message)             {                 LogMessage("Info", message);             }                  private void LogMessage(string methodName, string message)             {                 var getLoggerMethod = typeof(Log).GetMethod("GetLogger", System.Reflection.BindingFlags.Static | System.Reflection.BindingFlags.NonPublic, new Type[] { typeof(Type) });                      var logger = getLoggerMethod.Invoke(null, new object[] { typeof(LoggingTest) });                      var emitMethod = logger.GetType().GetMethod(methodName);                      emitMethod.Invoke(logger, new object[] { message });             }         }     }     

Ruby logger has 5 logger levels: `:debug`, `:info`, `:warn`, `:error`, `:fatal`. The default is `:info`.

To change the level of the logger:

[Selenium v4.10](https://github.com/SeleniumHQ/selenium/releases/tag/selenium-4.10.0)                   logger.level = :debug

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/ruby/spec/troubleshooting/logging_spec.rb#L13)

##### /examples/ruby/spec/troubleshooting/logging\_spec.rb

Copy  Close               # frozen_string_literal: true          require 'spec_helper'          RSpec.describe 'Logging' do       let(:file_name) { Tempfile.new('logging').path }            after { FileUtils.rm_f(file_name) }            it 'logs things' do         logger = Selenium::WebDriver.logger              logger.level = :debug              logger.output = file_name              logger.ignore(:jwp_caps, :logger_info)         logger.allow(%i[selenium_manager example_id])              logger.warn('this is a warning', id: :example_id)         logger.info('this is useful information', id: :example_id)         logger.debug('this is detailed debug information', id: :example_id)              expect(File.readlines(file_name).grep(/\[:example_id\]/).size).to eq 3       end     end     

JavaScript has 9 logger levels: `OFF`, `SEVERE`, `WARNING`, `INFO`, `DEBUG`, `FINE`, `FINER`, `FINEST`, `ALL`. The default is `OFF`.

To change the level of the logger:               logger.setLevel(logging.Level.INFO)     

## Content Help

**Note:** This section needs additional and/or updated content      Check our [contribution guidelines](https://www.selenium.dev/documentation/about/contributing/) if you’d like to help.

### Actionable items

Things are logged as warnings if they are something the user needs to take action on. This is often used for deprecations. For various reasons, Selenium project does not follow standard Semantic Versioning practices. Our policy is to mark things as deprecated for 3 releases and then remove them, so deprecations may be logged as warnings.

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

Java logs actionable content at logger level `WARN`

Example:               May 08, 2023 9:23:38 PM dev.selenium.troubleshooting.LoggingTest logging     WARNING: this is a warning     

Python logs actionable content at logger level — `WARNING` Details about deprecations are logged at this level.

Example:               WARNING  selenium:test_logging.py:23 this is a warning     

.NET logs actionable content at logger level `Warn`.

Example:               11:04:40.986 WARN LoggingTest: this is a warning     

Ruby logs actionable content at logger level — `:warn`. Details about deprecations are logged at this level.

For example:               2023-05-08 20:53:13 WARN Selenium [:example_id] this is a warning      

Because these items can get annoying, we’ve provided an easy way to turn them off, see [filtering section](https://www.selenium.dev/documentation/webdriver/troubleshooting/logging/#logger-filtering) below.

## Content Help

**Note:** This section needs additional and/or updated content      Check our [contribution guidelines](https://www.selenium.dev/documentation/about/contributing/) if you’d like to help.

## Content Help

**Note:** This section needs additional and/or updated content      Check our [contribution guidelines](https://www.selenium.dev/documentation/about/contributing/) if you’d like to help.

### Useful information

This is the default level where Selenium logs things that users should be aware of but do not need to take actions on. This might reference a new method or direct users to more information about something

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

Java logs useful information at logger level `INFO`

Example:               May 08, 2023 9:23:38 PM dev.selenium.troubleshooting.LoggingTest logging     INFO: this is useful information     

Python logs useful information at logger level — `INFO`

Example:               INFO     selenium:test_logging.py:22 this is useful information     

.NET logs useful information at logger level `Info`.

Example:               11:04:40.986 INFO LoggingTest: this is useful information     

Ruby logs useful information at logger level — `:info`.

Example:               2023-05-08 20:53:13 INFO Selenium [:example_id] this is useful information      

Logs useful information at level: `INFO`

## Content Help

**Note:** This section needs additional and/or updated content      Check our [contribution guidelines](https://www.selenium.dev/documentation/about/contributing/) if you’d like to help.

### Debugging Details

The debug log level is used for information that may be needed for diagnosing issues and troubleshooting problems.

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

Java logs most debug content at logger level `FINE`

Example:               May 08, 2023 9:23:38 PM dev.selenium.troubleshooting.LoggingTest logging     FINE: this is detailed debug information     

Python logs debugging details at logger level — `DEBUG`

Example:               DEBUG    selenium:test_logging.py:24 this is detailed debug information     

.NET logs most debug content at logger level `Debug`.

Example:               11:04:40.986 DEBUG LoggingTest: this is detailed debug information     

Ruby only provides one level for debugging, so all details are at logger level — `:debug`.

Example:               2023-05-08 20:53:13 DEBUG Selenium [:example_id] this is detailed debug information      

Logs debugging details at level: `FINER` and `FINEST`

## Content Help

**Note:** This section needs additional and/or updated content      Check our [contribution guidelines](https://www.selenium.dev/documentation/about/contributing/) if you’d like to help.

## Logger output

Logs can be displayed in the console or stored in a file. Different languages have different defaults.

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

By default all logs are sent to `System.err`. To direct output to a file, you need to add a handler:                       Handler handler = new FileHandler("selenium.xml");             logger.addHandler(handler);

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/java/src/test/java/dev/selenium/troubleshooting/LoggingTest.java#L37-L38)

##### /examples/java/src/test/java/dev/selenium/troubleshooting/LoggingTest.java

Copy  Close               package dev.selenium.troubleshooting;          import java.io.IOException;     import java.nio.file.Files;     import java.nio.file.Paths;     import java.util.Arrays;     import java.util.logging.FileHandler;     import java.util.logging.Handler;     import java.util.logging.Level;     import java.util.logging.Logger;          import org.junit.jupiter.api.AfterEach;     import org.junit.jupiter.api.Assertions;     import org.junit.jupiter.api.Test;     import org.openqa.selenium.manager.SeleniumManager;     import org.openqa.selenium.remote.RemoteWebDriver;          public class LoggingTest {              @AfterEach         public void loggingOff() {             Logger logger = Logger.getLogger("");             logger.setLevel(Level.INFO);             Arrays.stream(logger.getHandlers()).forEach(handler -> {                 handler.setLevel(Level.INFO);             });         }              @Test         public void logging() throws IOException {             Logger logger = Logger.getLogger("");             logger.setLevel(Level.FINE);             Arrays.stream(logger.getHandlers()).forEach(handler -> {                 handler.setLevel(Level.FINE);             });                  Handler handler = new FileHandler("selenium.xml");             logger.addHandler(handler);                  Logger.getLogger(RemoteWebDriver.class.getName()).setLevel(Level.FINEST);             Logger.getLogger(SeleniumManager.class.getName()).setLevel(Level.SEVERE);                  Logger localLogger = Logger.getLogger(this.getClass().getName());             localLogger.warning("this is a warning");             localLogger.info("this is useful information");             localLogger.fine("this is detailed debug information");                  byte[] bytes = Files.readAllBytes(Paths.get("selenium.xml"));             String fileContent = new String(bytes);                  Assertions.assertTrue(fileContent.contains("this is a warning"));             Assertions.assertTrue(fileContent.contains("this is useful information"));             Assertions.assertTrue(fileContent.contains("this is detailed debug information"));         }     }     

By default all logs are sent to `sys.stderr`. To direct output somewhere else, you need to add a handler with either a `StreamHandler` or a `FileHandler`:                   handler = logging.FileHandler(log_path)         logger.addHandler(handler)

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/python/tests/troubleshooting/test_logging.py#L9-L10)

##### /examples/python/tests/troubleshooting/test\_logging.py

Copy  Close               import logging               def test_logging(log_path):         logger = logging.getLogger('selenium')              logger.setLevel(logging.DEBUG)              handler = logging.FileHandler(log_path)         logger.addHandler(handler)              logging.getLogger('selenium.webdriver.remote').setLevel(logging.WARN)         logging.getLogger('selenium.webdriver.common').setLevel(logging.DEBUG)              logger.info("this is useful information")         logger.warning("this is a warning")         logger.debug("this is detailed debug information")              with open(log_path, 'r') as fp:             assert len(fp.readlines()) == 3     

By default all logs are sent to `System.Console.Error` output. To direct output somewhere else, you need to add a handler with a `FileLogHandler`:                           Log.Handlers.Add(new FileLogHandler(filePath));

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/dotnet/SeleniumDocs/Troubleshooting/LoggingTest.cs#L20)

##### /examples/dotnet/SeleniumDocs/Troubleshooting/LoggingTest.cs

Copy  Close               ﻿using Microsoft.VisualStudio.TestTools.UnitTesting;     using OpenQA.Selenium;     using OpenQA.Selenium.Internal.Logging;     using OpenQA.Selenium.Remote;     using System;     using System.IO;          namespace SeleniumDocs.Troubleshooting     {         [TestClass]         public class LoggingTest         {             private const string filePath = "Selenium.log";                  [TestMethod]             public void Logging()             {                 Log.SetLevel(LogEventLevel.Trace);                      Log.Handlers.Add(new FileLogHandler(filePath));                      Log.SetLevel(typeof(RemoteWebDriver), LogEventLevel.Debug);                 Log.SetLevel(typeof(SeleniumManager), LogEventLevel.Info);                      Warn("this is a warning");                 Info("this is useful information");                 Debug("this is detailed debug information");                      using (var fileStream = File.Open(filePath, FileMode.Open, FileAccess.Read, FileShare.ReadWrite))                 {                     using (var streamReader = new StreamReader(fileStream))                     {                         var fileLogContent = streamReader.ReadToEnd();                              StringAssert.Contains(fileLogContent, "this is a warning");                         StringAssert.Contains(fileLogContent, "this is useful information");                         StringAssert.Contains(fileLogContent, "this is detailed debug information");                     }                 }             }                  [TestCleanup]             public void TestCleanup()             {                 // reset log to default                 Log.SetLevel(LogEventLevel.Info)                     .Handlers.Clear()                     .Handlers.Add(new ConsoleLogHandler());             }                  // logging is only for internal usage             // hacking it via reflection                  private void Debug(string message)             {                 LogMessage("Debug", message);             }                  private void Warn(string message)             {                 LogMessage("Warn", message);             }                  private void Info(string message)             {                 LogMessage("Info", message);             }                  private void LogMessage(string methodName, string message)             {                 var getLoggerMethod = typeof(Log).GetMethod("GetLogger", System.Reflection.BindingFlags.Static | System.Reflection.BindingFlags.NonPublic, new Type[] { typeof(Type) });                      var logger = getLoggerMethod.Invoke(null, new object[] { typeof(LoggingTest) });                      var emitMethod = logger.GetType().GetMethod(methodName);                      emitMethod.Invoke(logger, new object[] { message });             }         }     }     

By default, logs are sent to the console in `stdout`.   To store the logs in a file:

[Selenium v4.10](https://github.com/SeleniumHQ/selenium/releases/tag/selenium-4.10.0)                   logger.output = file_name

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/ruby/spec/troubleshooting/logging_spec.rb#L15)

##### /examples/ruby/spec/troubleshooting/logging\_spec.rb

Copy  Close               # frozen_string_literal: true          require 'spec_helper'          RSpec.describe 'Logging' do       let(:file_name) { Tempfile.new('logging').path }            after { FileUtils.rm_f(file_name) }            it 'logs things' do         logger = Selenium::WebDriver.logger              logger.level = :debug              logger.output = file_name              logger.ignore(:jwp_caps, :logger_info)         logger.allow(%i[selenium_manager example_id])              logger.warn('this is a warning', id: :example_id)         logger.info('this is useful information', id: :example_id)         logger.debug('this is detailed debug information', id: :example_id)              expect(File.readlines(file_name).grep(/\[:example_id\]/).size).to eq 3       end     end     

JavaScript does not currently support sending output to a file.

To send logs to console output:               logging.installConsoleHandler()     

## Content Help

**Note:** This section needs additional and/or updated content      Check our [contribution guidelines](https://www.selenium.dev/documentation/about/contributing/) if you’d like to help.

## Logger filtering

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

Java logging is managed on a per class level, so instead of using the root logger \(`Logger.getLogger("")`\), set the level you want to use on a per-class basis:                       Logger.getLogger(RemoteWebDriver.class.getName()).setLevel(Level.FINEST);             Logger.getLogger(SeleniumManager.class.getName()).setLevel(Level.SEVERE);

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/java/src/test/java/dev/selenium/troubleshooting/LoggingTest.java#L40-L41)

##### /examples/java/src/test/java/dev/selenium/troubleshooting/LoggingTest.java

Copy  Close               package dev.selenium.troubleshooting;          import java.io.IOException;     import java.nio.file.Files;     import java.nio.file.Paths;     import java.util.Arrays;     import java.util.logging.FileHandler;     import java.util.logging.Handler;     import java.util.logging.Level;     import java.util.logging.Logger;          import org.junit.jupiter.api.AfterEach;     import org.junit.jupiter.api.Assertions;     import org.junit.jupiter.api.Test;     import org.openqa.selenium.manager.SeleniumManager;     import org.openqa.selenium.remote.RemoteWebDriver;          public class LoggingTest {              @AfterEach         public void loggingOff() {             Logger logger = Logger.getLogger("");             logger.setLevel(Level.INFO);             Arrays.stream(logger.getHandlers()).forEach(handler -> {                 handler.setLevel(Level.INFO);             });         }              @Test         public void logging() throws IOException {             Logger logger = Logger.getLogger("");             logger.setLevel(Level.FINE);             Arrays.stream(logger.getHandlers()).forEach(handler -> {                 handler.setLevel(Level.FINE);             });                  Handler handler = new FileHandler("selenium.xml");             logger.addHandler(handler);                  Logger.getLogger(RemoteWebDriver.class.getName()).setLevel(Level.FINEST);             Logger.getLogger(SeleniumManager.class.getName()).setLevel(Level.SEVERE);                  Logger localLogger = Logger.getLogger(this.getClass().getName());             localLogger.warning("this is a warning");             localLogger.info("this is useful information");             localLogger.fine("this is detailed debug information");                  byte[] bytes = Files.readAllBytes(Paths.get("selenium.xml"));             String fileContent = new String(bytes);                  Assertions.assertTrue(fileContent.contains("this is a warning"));             Assertions.assertTrue(fileContent.contains("this is useful information"));             Assertions.assertTrue(fileContent.contains("this is detailed debug information"));         }     }     

Because logging is managed by module, instead of working with just "selenium", you can specify different levels for different modules:                   logging.getLogger('selenium.webdriver.remote').setLevel(logging.WARN)         logging.getLogger('selenium.webdriver.common').setLevel(logging.DEBUG)

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/python/tests/troubleshooting/test_logging.py#L12-L13)

##### /examples/python/tests/troubleshooting/test\_logging.py

Copy  Close               import logging               def test_logging(log_path):         logger = logging.getLogger('selenium')              logger.setLevel(logging.DEBUG)              handler = logging.FileHandler(log_path)         logger.addHandler(handler)              logging.getLogger('selenium.webdriver.remote').setLevel(logging.WARN)         logging.getLogger('selenium.webdriver.common').setLevel(logging.DEBUG)              logger.info("this is useful information")         logger.warning("this is a warning")         logger.debug("this is detailed debug information")              with open(log_path, 'r') as fp:             assert len(fp.readlines()) == 3     

.NET logging is managed on a per class level, set the level you want to use on a per-class basis:                           Log.SetLevel(typeof(RemoteWebDriver), LogEventLevel.Debug);                 Log.SetLevel(typeof(SeleniumManager), LogEventLevel.Info);

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/dotnet/SeleniumDocs/Troubleshooting/LoggingTest.cs#L22-L23)

##### /examples/dotnet/SeleniumDocs/Troubleshooting/LoggingTest.cs

Copy  Close               ﻿using Microsoft.VisualStudio.TestTools.UnitTesting;     using OpenQA.Selenium;     using OpenQA.Selenium.Internal.Logging;     using OpenQA.Selenium.Remote;     using System;     using System.IO;          namespace SeleniumDocs.Troubleshooting     {         [TestClass]         public class LoggingTest         {             private const string filePath = "Selenium.log";                  [TestMethod]             public void Logging()             {                 Log.SetLevel(LogEventLevel.Trace);                      Log.Handlers.Add(new FileLogHandler(filePath));                      Log.SetLevel(typeof(RemoteWebDriver), LogEventLevel.Debug);                 Log.SetLevel(typeof(SeleniumManager), LogEventLevel.Info);                      Warn("this is a warning");                 Info("this is useful information");                 Debug("this is detailed debug information");                      using (var fileStream = File.Open(filePath, FileMode.Open, FileAccess.Read, FileShare.ReadWrite))                 {                     using (var streamReader = new StreamReader(fileStream))                     {                         var fileLogContent = streamReader.ReadToEnd();                              StringAssert.Contains(fileLogContent, "this is a warning");                         StringAssert.Contains(fileLogContent, "this is useful information");                         StringAssert.Contains(fileLogContent, "this is detailed debug information");                     }                 }             }                  [TestCleanup]             public void TestCleanup()             {                 // reset log to default                 Log.SetLevel(LogEventLevel.Info)                     .Handlers.Clear()                     .Handlers.Add(new ConsoleLogHandler());             }                  // logging is only for internal usage             // hacking it via reflection                  private void Debug(string message)             {                 LogMessage("Debug", message);             }                  private void Warn(string message)             {                 LogMessage("Warn", message);             }                  private void Info(string message)             {                 LogMessage("Info", message);             }                  private void LogMessage(string methodName, string message)             {                 var getLoggerMethod = typeof(Log).GetMethod("GetLogger", System.Reflection.BindingFlags.Static | System.Reflection.BindingFlags.NonPublic, new Type[] { typeof(Type) });                      var logger = getLoggerMethod.Invoke(null, new object[] { typeof(LoggingTest) });                      var emitMethod = logger.GetType().GetMethod(methodName);                      emitMethod.Invoke(logger, new object[] { message });             }         }     }     

Ruby’s logger allows you to opt in \(“allow”\) or opt out \(“ignore”\) of log messages based on their IDs. Everything that Selenium logs includes an ID. You can also turn on or off all deprecation notices by using `:deprecations`.

These methods accept one or more symbols or an array of symbols:

[Selenium v4.10](https://github.com/SeleniumHQ/selenium/releases/tag/selenium-4.10.0)                   logger.ignore(:jwp_caps, :logger_info)

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/ruby/spec/troubleshooting/logging_spec.rb#17)

##### /examples/ruby/spec/troubleshooting/logging\_spec.rb

Copy  Close               # frozen_string_literal: true          require 'spec_helper'          RSpec.describe 'Logging' do       let(:file_name) { Tempfile.new('logging').path }            after { FileUtils.rm_f(file_name) }            it 'logs things' do         logger = Selenium::WebDriver.logger              logger.level = :debug              logger.output = file_name              logger.ignore(:jwp_caps, :logger_info)         logger.allow(%i[selenium_manager example_id])              logger.warn('this is a warning', id: :example_id)         logger.info('this is useful information', id: :example_id)         logger.debug('this is detailed debug information', id: :example_id)              expect(File.readlines(file_name).grep(/\[:example_id\]/).size).to eq 3       end     end     

or

[Selenium v4.10](https://github.com/SeleniumHQ/selenium/releases/tag/selenium-4.10.0)                   logger.allow(%i[selenium_manager example_id])

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/ruby/spec/troubleshooting/logging_spec.rb#L18)

##### /examples/ruby/spec/troubleshooting/logging\_spec.rb

Copy  Close               # frozen_string_literal: true          require 'spec_helper'          RSpec.describe 'Logging' do       let(:file_name) { Tempfile.new('logging').path }            after { FileUtils.rm_f(file_name) }            it 'logs things' do         logger = Selenium::WebDriver.logger              logger.level = :debug              logger.output = file_name              logger.ignore(:jwp_caps, :logger_info)         logger.allow(%i[selenium_manager example_id])              logger.warn('this is a warning', id: :example_id)         logger.info('this is useful information', id: :example_id)         logger.debug('this is detailed debug information', id: :example_id)              expect(File.readlines(file_name).grep(/\[:example_id\]/).size).to eq 3       end     end     

## Content Help

**Note:** This section needs additional and/or updated content      Check our [contribution guidelines](https://www.selenium.dev/documentation/about/contributing/) if you’d like to help.

## Content Help

**Note:** This section needs additional and/or updated content      Check our [contribution guidelines](https://www.selenium.dev/documentation/about/contributing/) if you’d like to help.

# 3 - Upgrade to Selenium 4

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