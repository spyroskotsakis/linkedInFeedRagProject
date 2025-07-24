# Selenium Overview | Selenium

**URL:** https://www.selenium.dev/documentation/overview/_print
**Word Count:** 1258
**Links Count:** 48
**Scraped:** 2025-07-17 06:17:48
**Status:** completed

---

This is the multi-page printable view of this section. Click here to print.

[Return to the regular view of this page](https://www.selenium.dev/documentation/overview/).

# Selenium Overview

Is Selenium for you? See an overview of the different project components.

  * 1: Selenium components   * 2: A deeper look at Selenium

Selenium is not just one tool or API; it comprises many tools.

## WebDriver

If you are beginning with desktop website or mobile website test automation, then you are going to be using WebDriver APIs. [WebDriver](https://www.selenium.dev/documentation/webdriver/) uses browser automation APIs provided by browser vendors to control the browser and run tests. This is as if a real user is operating the browser. Since WebDriver does not require its API to be compiled with application code, it is not intrusive. Hence, you are testing the same application which you push live.

## IDE

[IDE](https://selenium.dev/selenium-ide) \(Integrated Development Environment\) is the tool you use to develop your Selenium test cases. It’s an easy-to-use Chrome and Firefox extension and is generally the most efficient way to develop test cases. It records the users’ actions in the browser for you, using existing Selenium commands, with parameters defined by the context of that element. This is not only a time-saver but also an excellent way of learning Selenium script syntax.

## Grid

Selenium Grid allows you to run test cases in different machines across different platforms. The control of triggering the test cases is on the local end, and when the test cases are triggered, they are automatically executed by the remote end.

After the development of the WebDriver tests, you may face the need to run your tests on multiple browsers and operating system combinations. This is where [Grid](https://www.selenium.dev/documentation/grid/) comes into the picture.

# 1 - Selenium components

Building a test suite using WebDriver will require you to understand and effectively use several components. As with everything in software, different people use different terms for the same idea. Below is a breakdown of how terms are used in this description.

### Terminology

  * **API:** Application Programming Interface. This is the set of “commands” you use to manipulate WebDriver.   * **Library:** A code module that contains the APIs and the code necessary to implement them. Libraries are specific to each language binding, eg .jar files for Java, .dll files for .NET, etc.   * **Driver:** Responsible for controlling the actual browser. Most drivers are created by the browser vendors themselves. Drivers are generally executable modules that run on the system with the browser itself, not the system executing the test suite. \(Although those may be the same system.\) NOTE: _Some people refer to the drivers as proxies._   * **Framework:** An additional library that is used as a support for WebDriver suites. These frameworks may be test frameworks such as JUnit or NUnit. They may also be frameworks supporting natural language features such as Cucumber or Robotium. Frameworks may also be written and used for tasks such as manipulating or configuring the system under test, data creation, test oracles, etc.

### The Parts and Pieces

At its minimum, WebDriver talks to a browser through a driver. Communication is two-way: WebDriver passes commands to the browser through the driver, and receives information back via the same route.

![Basic Communication](https://www.selenium.dev/images/documentation/webdriver/basic_comms.png)

The driver is specific to the browser, such as ChromeDriver for Google’s Chrome/Chromium, GeckoDriver for Mozilla’s Firefox, etc. The driver runs on the same system as the browser. This may or may not be the same system where the tests themselves are executed.

This simple example above is _direct_ communication. Communication to the browser may also be _remote_ communication through Selenium Server or RemoteWebDriver. RemoteWebDriver runs on the same system as the driver and the browser.

![Remote Communication](https://www.selenium.dev/images/documentation/webdriver/remote_comms.png)

Remote communication can also take place using Selenium Server or Selenium Grid, both of which in turn talk to the driver on the host system

![Remote Communication with Grid](https://www.selenium.dev/images/documentation/webdriver/remote_comms_server.png)

## Where Frameworks fit in

WebDriver has one job and one job only: communicate with the browser via any of the methods above. WebDriver does not know a thing about testing: it does not know how to compare things, assert pass or fail, and it certainly does not know a thing about reporting or Given/When/Then grammar.

This is where various frameworks come into play. At a minimum, you will need a test framework that matches the language bindings, e.g., NUnit for .NET, JUnit for Java, RSpec for Ruby, etc.

The test framework is responsible for running and executing your WebDriver and related steps in your tests. As such, you can think of it looking akin to the following image.

![Test Framework](https://www.selenium.dev/images/documentation/webdriver/test_framework.png)

Natural language frameworks/tools such as Cucumber may exist as part of that Test Framework box in the figure above, or they may wrap the Test Framework entirely in their custom implementation.

# 2 - A deeper look at Selenium

Selenium is an umbrella project for a range of tools and libraries that enable and support the automation of web browsers.

### Selenium controls web browsers

 _Selenium_ is many things but at its core, it is a toolset for web browser automation that uses the best techniques available to remotely control browser instances and emulate a user’s interaction with the browser.

Selenium allows users to simulate common activities performed by end-users; entering text into fields, selecting drop-down values and checking boxes, and clicking links in documents. It also provides many other controls such as mouse movement, arbitrary JavaScript execution, and much more.

Although used primarily for front-end testing of websites, Selenium is, at its core, a browser user agent _library_. The interfaces are ubiquitous to their application, encouraging composition with other libraries to suit your purpose.

### One interface to rule them all

One of the project’s guiding principles is to support a common interface for all \(major\) browser technologies. Web browsers are incredibly complex, highly engineered applications, performing their operations in entirely different ways but which frequently look the same while doing so. Even though the text is rendered in the same fonts, the images are displayed in the same place, and the links take you to the same destination. What is happening underneath is as different as night and day. Selenium “abstracts” these differences, hiding their details and intricacies from the person writing the code. This allows you to write several lines of code to perform a complicated workflow, but these same lines will execute on Firefox, Internet Explorer, Chrome, and all other supported browsers.

### Tools and support

Selenium’s minimalist design approach gives it the versatility to be included as a component in bigger applications. The surrounding infrastructure provided under the Selenium umbrella gives you the tools to put together your [grid of browsers](https://www.selenium.dev/documentation/grid/) so tests can be run on different browsers and multiple operating systems across a range of machines.

Imagine a bank of computers in your server room or data center all firing up browsers at the same time hitting your site’s links, forms, and tables—testing your application 24 hours a day. Through the simple programming interface provided for the most common languages, these tests will run tirelessly in parallel, reporting back to you when errors occur.

It is an aim to help make this a reality for you, by providing users with tools and documentation to not only control browsers but to make it easy to scale and deploy such grids.

### Who uses Selenium

Many of the most important companies in the world have adopted Selenium for their browser-based testing, often replacing years-long efforts involving other proprietary tools. As it has grown in popularity, so have its requirements and challenges multiplied.

As the web becomes more complicated and new technologies are added to websites, it’s the mission of this project to keep up with them where possible. Being an open-source project, this support is provided through the generous donation of time from many volunteers, every one of which has a “day job.”

Another mission of the project is to encourage more volunteers to partake in this effort, and build a strong community so that the project can continue to keep up with emerging technologies and remain a dominant platform for functional test automation.