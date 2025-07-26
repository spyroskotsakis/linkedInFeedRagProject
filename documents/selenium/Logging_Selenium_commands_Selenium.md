# Logging Selenium commands | Selenium

**URL:** https://www.selenium.dev/documentation/webdriver/troubleshooting/logging
**Word Count:** 1451
**Links Count:** 238
**Scraped:** 2025-07-17 06:13:37
**Status:** completed

---

# Logging Selenium commands

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

Last modified March 9, 2025: [Update Python logging examples in documentation. \(\#2206\)\[deploy site\] \(e4f3470901b\)](https://github.com/SeleniumHQ/seleniumhq.github.io/commit/e4f3470901b8f5ab5255c2ee8a7a110955b421c8)