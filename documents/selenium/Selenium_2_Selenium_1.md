# Selenium 2 | Selenium

**URL:** https://www.selenium.dev/documentation/legacy/selenium_2/_print
**Word Count:** 9689
**Links Count:** 119
**Scraped:** 2025-07-17 06:17:48
**Status:** completed

---

This is the multi-page printable view of this section. Click here to print.

[Return to the regular view of this page](https://www.selenium.dev/documentation/legacy/selenium_2/).

# Selenium 2

Selenium 2 was a rewrite of Selenium 1 that was implemented with WebDriver code.

  * 1: Migrating from RC to WebDriver   * 2: Backing Selenium with WebDriver   * 3: Legacy Firefox Driver   * 4: Selenium grid 2   * 5: History of Grid Platforms   * 6: Remote WebDriver standalone server   * 7: Limitations of scaling up tests in Selenium 2   * 8: Stealing focus from Firefox in Linux   * 9: Untrusted SSL Certificates   * 10: WebDriver For Mobile Browsers   * 11: Frequently Asked Questions for Selenium 2   * 12: Selenium 2.0 Team

# 1 - Migrating from RC to WebDriver

Information on Updating from Selenium 1 to Selenium 2.

## How to Migrate to Selenium WebDriver

A common question when adopting Selenium 2 is what’s the correct thing to do when adding new tests to an existing set of tests? Users who are new to the framework can begin by using the new WebDriver APIs for writing their tests. But what of users who already have suites of existing tests? This guide is designed to demonstrate how to migrate your existing tests to the new APIs, allowing all new tests to be written using the new features offered by WebDriver.

The method presented here describes a piecemeal migration to the WebDriver APIs without needing to rework everything in one massive push. This means that you can allow more time for migrating your existing tests, which may make it easier for you to decide where to spend your effort.

This guide is written using Java, because this has the best support for making the migration. As we provide better tools for other languages, this guide shall be expanded to include those languages.

## Why Migrate to WebDriver

Moving a suite of tests from one API to another API requires an enormous amount of effort. Why would you and your team consider making this move? Here are some reasons why you should consider migrating your Selenium Tests to use WebDriver.

  * Smaller, compact API. WebDriver’s API is more Object Oriented than the original Selenium RC API. This can make it easier to work with.   * Better emulation of user interactions. Where possible, WebDriver makes use of native events in order to interact with a web page. This more closely mimics the way that your users work with your site and apps. In addition, WebDriver offers the advanced user interactions APIs which allow you to model complex interactions with your site.   * Support by browser vendors. Opera, Mozilla and Google are all active participants in WebDriver’s development, and each have engineers working to improve the framework. Often, this means that support for WebDriver is baked into the browser itself: your tests run as fast and as stably as possible.

## Before Starting

In order to make the process of migrating as painless as possible, make sure that all your tests run properly with the latest Selenium release. This may sound obvious, but it’s best to have it said\!

## Getting Started

The first step when starting the migration is to change how you obtain your instance of Selenium. When using Selenium RC, this is done like so:               Selenium selenium = new DefaultSelenium("localhost", 4444, "*firefox", "http://www.yoursite.com");     selenium.start();     

This should be replaced like so:               WebDriver driver = new FirefoxDriver();     Selenium selenium = new WebDriverBackedSelenium(driver, "http://www.yoursite.com");     

## Next Steps

Once your tests execute without errors, the next stage is to migrate the actual test code to use the WebDriver APIs. Depending on how well abstracted your code is, this might be a short process or a long one. In either case, the approach is the same and can be summed up simply: modify code to use the new API when you come to edit it.

If you need to extract the underlying WebDriver implementation from the Selenium instance, you can simply cast it to WrapsDriver:               WebDriver driver = ((WrapsDriver) selenium).getWrappedDriver();     

This allows you to continue passing the Selenium instance around as normal, but to unwrap the WebDriver instance as required.

At some point, you’re codebase will mostly be using the newer APIs. At this point, you can flip the relationship, using WebDriver throughout and instantiating a Selenium instance on demand:               Selenium selenium = new WebDriverBackedSelenium(driver, baseUrl);     

## Common Problems

Fortunately, you’re not the first person to go through this migration, so here are some common problems that others have seen, and how to solve them.

### Clicking and Typing is More Complete

A common pattern in a Selenium RC test is to see something like:               selenium.type("name", "exciting tex");     selenium.keyDown("name", "t");     selenium.keyPress("name", "t");     selenium.keyUp("name", "t");     

This relies on the fact that “type” simply replaces the content of the identified element without also firing all the events that would normally be fired if a user interacts with the page. The final direct invocations of “key\*” cause the JS handlers to fire as expected.

When using the WebDriverBackedSelenium, the result of filling in the form field would be “exciting texttt”: not what you’d expect\! The reason for this is that WebDriver more accurately emulates user behavior, and so will have been firing events all along.

This same fact may sometimes cause a page load to fire earlier than it would do in a Selenium 1 test. You can tell that this has happened if a “StaleElementException” is thrown by WebDriver.

### WaitForPageToLoad Returns Too Soon

Discovering when a page load is complete is a tricky business. Do we mean “when the load event fires”, “when all AJAX requests are complete”, “when there’s no network traffic”, “when document.readyState has changed” or something else entirely?

WebDriver attempts to simulate the original Selenium behavior, but this doesn’t always work perfectly for various reasons. The most common reason is that it’s hard to tell the difference between a page load not having started yet, and a page load having completed between method calls. This sometimes means that control is returned to your test before the page has finished \(or even started\!\) loading.

The solution to this is to wait on something specific. Commonly, this might be for the element you want to interact with next, or for some Javascript variable to be set to a specific value. An example would be:               Wait<WebDriver> wait = new WebDriverWait(driver, Duration.ofSeconds(30));     WebElement element= wait.until(visibilityOfElementLocated(By.id("some_id")));     

Where “visibilityOfElementLocated” is implemented as:               public ExpectedCondition<WebElement> visibilityOfElementLocated(final By locator) {       return new ExpectedCondition<WebElement>() {         public WebElement apply(WebDriver driver) {           WebElement toReturn = driver.findElement(locator);           if (toReturn.isDisplayed()) {             return toReturn;           }           return null;         }       };     }     

This may look complex, but it’s almost all boiler-plate code. The only interesting bit is that the “ExpectedCondition” will be evaluated repeatedly until the “apply” method returns something that is neither “null” nor Boolean.FALSE.

Of course, adding all these “wait” calls may clutter up your code. If that’s the case, and your needs are simple, consider using the implicit waits:               driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);     

By doing this, every time an element is located, if the element is not present, the location is retried until either it is present, or until 30 seconds have passed.

### Finding By XPath or CSS Selectors Doesn’t Always Work, But It Does In Selenium 1

In Selenium 1, it was common for xpath to use a bundled library rather than the capabilities of the browser itself. WebDriver will always use the native browser methods unless there’s no alternative. That means that complex xpath expressions may break on some browsers.

CSS Selectors in Selenium 1 were implemented using the Sizzle library. This implements a superset of the CSS Selector spec, and it’s not always clear where you’ve crossed the line. If you’re using the WebDriverBackedSelenium and use a Sizzle locator instead of a CSS Selector for finding elements, a warning will be logged to the console. It’s worth taking the time to look for these, particularly if tests are failing because of not being able to find elements.

### There is No Browserbot

Selenium RC was based on Selenium Core, and therefore when you executed Javascript, you could access bits of Selenium Core to make things easier. As WebDriver is not based on Selenium Core, this is no longer possible. How can you tell if you’re using Selenium Core? Simple\! Just look to see if your “getEval” or similar calls are using “selenium” or “browserbot” in the evaluated Javascript.

You might be using the browserbot to obtain a handle to the current window or document of the test. Fortunately, WebDriver always evaluates JS in the context of the current window, so you can use “window” or “document” directly.

Alternatively, you might be using the browserbot to locate elements. In WebDriver, the idiom for doing this is to first locate the element, and then pass that as an argument to the Javascript. Thus:               String name = selenium.getEval(         "selenium.browserbot.findElement('id=foo', browserbot.getCurrentWindow()).tagName");     

becomes:               WebElement element = driver.findElement(By.id("foo"));     String name = (String) ((JavascriptExecutor) driver).executeScript(         "return arguments[0].tagName", element);     

Notice how the passed in “element” variable appears as the first item in the JS standard “arguments” array.

### Executing Javascript Doesn’t Return Anything

WebDriver’s JavascriptExecutor will wrap all JS and evaluate it as an anonymous expression. This means that you need to use the “return” keyword:               String title = selenium.getEval("browserbot.getCurrentWindow().document.title");     

becomes:               ((JavascriptExecutor) driver).executeScript("return document.title;");     

# 2 - Backing Selenium with WebDriver

The Java and .NET versions of Selenium 2 provided implementations of the original Selenium API

\(Previously located: <https://github.com/SeleniumHQ/selenium/wiki/Selenium-Emulation>\)

## Backing Selenium with WebDriver

The Java and .NET versions of WebDriver provide implementations of the existing Selenium API. In Java, it is used like so:               // You may use any WebDriver implementation. Firefox is used here as an example     WebDriver driver = new FirefoxDriver();          // A "base url", used by selenium to resolve relative URLs     String baseUrl = "http://www.google.com";          // Create the Selenium implementation     Selenium selenium = new WebDriverBackedSelenium(driver, baseUrl);          // Perform actions with selenium     selenium.open("http://www.google.com");     selenium.type("name=q", "cheese");     selenium.click("name=btnG");          // And get the underlying WebDriver implementation back. This will refer to the     // same WebDriver instance as the "driver" variable above.     WebDriver driverInstance = ((WebDriverBackedSelenium) selenium).getUnderlyingWebDriver();     

## Pros

  * Allows for WebDriver and Selenium to live side-by-side.   * Provides a simple mechanism for a managed migration from the existing Selenium API to WebDriver’s.   * Does not require the standalone Selenium RC server to be run

## Cons

  * Does not implement every method     * But we’d love feedback\!   * Does also emulate Selenium Core     * So more advanced Selenium usage \(that is, using “browserbot” or other built-in Javascript methods from Selenium Core\) may need work   * Some methods may be slower due to underlying implementation differences   * Does not support Selenium’s “user extensions” \(_i.e._ , user-extensions.js\)

### Notes

After creating a `WebDriverBackedSelenium` instance with a given Driver, one does not have to call `start()` \- as the creation of the Driver already started the session. At the end of the test, `stop()` should be called **instead** of the Driver’s `quit()` method.

This is more similar to WebDriver’s behaviour - as creating a Driver instance starts a session, yet it has to be terminated explicitly with a call to `quit()`.

## Backing Selenium with RemoteWebDriver

Starting with release 2.19, `WebDriverBackedSelenium` can be used from any language supported by WebDriver and Selenium.

For example, in Python:               driver = RemoteWebDriver(desired_capabilities = DesiredCapabilities.FIREFOX)     selenium = DefaultSelenium('localhost', '4444', '*webdriver', 'http://www.google.com')     selenium.start(driver = driver)     

Provided you keep a reference to the original WebDriver and Selenium objects you created, you can use even the two APIs interchangeably. The magic is the “`*webdriver`” browser name passed to the Selenium instance, and that you pass the WebDriver instance when calling `start()`.

In languages where DefaultSelenium doesn’t have `start(driver)`, you can connect the WebDriver and Selenium objects together yourself, by supplying the WebDriver session ID to the Selenium object.

For example, in C\#:               RemoteWebDriver driver = new RemoteWebDriver(DesiredCapabilities.Firefox());     string sessionId = (string) driver.Capabilities.GetCapability("webdriver.remote.sessionid");     DefaultSelenium selenium = new DefaultSelenium("localhost", 4444, "*webdriver", "http://www.google.com");     selenium.Start("webdriver.remote.sessionid=" + sessionId);     

## Backing WebDriver with Selenium

WebDriver doesn’t support as many browsers as Selenium does, so in order to provide that support while still using the webdriver API, you can make use of the `SeleneseCommandExecutor` It is done like this:               Capabilities capabilities = new DesiredCapabilities()     capabilities.setBrowserName("safari");     CommandExecutor executor = new SeleneseCommandExecutor("http:localhost:4444/", "http://www.google.com/", capabilities);     WebDriver driver = new RemoteWebDriver(executor, capabilities);     

There are currently some major limitations with this approach, notably that `findElements` doesn’t work as expected. Also, because we’re using Selenium Core for the heavy lifting of driving the browser, you are limited by the Javascript sandbox.

# 3 - Legacy Firefox Driver

The legacy Firefox Driver was developed as a browser extension by the Selenium Developers. Firefox updated their security model, so it no longer works. You now need to use geckodriver.

This documentation previously located [on the wiki](https://github.com/SeleniumHQ/selenium/wiki/FirefoxDriver)   You can read more about [geckodriver](https://firefox-source-docs.mozilla.org/testing/geckodriver/).

## About

Firefox driver is included in the selenium-server-stanalone.jar available in the downloads. The driver comes in the form of an xpi \(firefox extension\) which is added to the firefox profile when you start a new instance of FirefoxDriver.

### Pros

  * Runs in a real browser and supports Javascript   * Faster than the InternetExplorerDriver

### Cons

  * Slower than the HtmlUnitDriver

### Important System Properties

The following system properties \(read using `System.getProperty()` and set using `System.setProperty()` in Java code or the “`-DpropertyName=value`” command line flag\) are used by the FirefoxDriver:

**Property**| **What it means**   ---|---   webdriver.firefox.bin| The location of the binary used to control firefox.   webdriver.firefox.marionette| Boolean value, if set on standalone-server will ignore any “marionette” desired capability requested and force firefox to use GeckoDriver \(true\) or Legacy Firefox Driver \(false\)   webdriver.firefox.profile| The name of the profile to use when starting firefox. This defaults to webdriver creating an anonymous profile   webdriver.firefox.useExisting| **Never use in production** Use a running instance of firefox if one is present   webdriver.firefox.logfile| Log file to dump firefox stdout/stderr to      Normally the Firefox binary is assumed to be in the default location for your particular operating system:

**OS**| **Expected Location of Firefox**   ---|---   Linux| firefox \(found using “which”\)   Mac| /Applications/Firefox.app/Contents/MacOS/firefox-bin   Windows| %PROGRAMFILES%\Mozilla Firefox\firefox.exe      By default, the Firefox driver creates an anonymous profile

### Running with firebug

Download the firebug xpi file from mozilla and start the profile as follows:                  File file = new File("firebug-1.8.1.xpi");        FirefoxProfile firefoxProfile = new FirefoxProfile();        firefoxProfile.addExtension(file);        firefoxProfile.setPreference("extensions.firebug.currentVersion", "1.8.1"); // Avoid startup screen             WebDriver driver = new FirefoxDriver(firefoxProfile);     

## FirefoxDriver Internals

\(Previously located: <https://github.com/SeleniumHQ/selenium/wiki/FirefoxDriver-Internals>\)

The FirefoxDriver is largely written in the form of a Firefox extension. Language bindings control the driver by connecting over a socket and sending commands \(described in the JsonWireProtocol page\) in UTF-8. The extension makes use of the XPCOM primitives offered by Firefox in order to do its work. The important thing to notice is that the command names map directly on to methods exposed on the “FirefoxDriver.prototype” in the javascript code.

### Working on the FirefoxDriver Code

Firstly, make sure that there’s no old version of the FirefoxDriver installed:

  * Start firefox’s profile manager: `firefox -ProfileManager`   * Delete the existing WebDriver profile if there is one. Delete the files too \(it’s an option that’s offered when you delete the profile in the profile manager\)

Secondly, take a look at the [Mozilla Developer Center](http://developer.mozilla.org/en/docs/Extensions), particularly the section to do with [setting up an extension development environment](http://developer.mozilla.org/en/docs/Setting_up_extension_development_environment). You should now be ready to edit code. It’s best to create a test around the area of code that you’re working on, and to run this using the `SingleTestSuite`. The FirefoxDriver logs errors to Firefox’s error console \(“Tools->Error Console”\), so if a test fails, that’s a great place to start looking.

To actually log information to the console, use the “`Utils.dumpn()`” method in your javascript code. If you find that you’d like to examine an object in detail, use the “`Utils.dump()`” method, which will report which interfaces an object implements, as well as outputting as much information as it can to the console..

### Flow of Control: Starting Firefox

The following steps are performed when instantiating an instance of the FirefoxDriver:

  1. Grab the “locking port”

# 4 - Selenium grid 2

Selenium Grid 2 supported WebDriver and Selenium RC. It was replaced by Grid 3 which removed RC code. Grid 3 was completely rewritten for the new Grid 4.

This documentation previously located [on the wiki](https://github.com/SeleniumHQ/selenium/wiki/Grid2)   You can read our documentation for more information about [Grid 4](https://www.selenium.dev/documentation/grid/)

## Introduction

Grid allows you to :

  * scale by distributing tests on several machines \( parallel execution \)   * manage multiple environments from a central point, making it easy to run the tests against a vast combination of browsers / OS.   * minimize the maintenance time for the grid by allowing you to implement custom hooks to leverage virtual infrastructure for instance.

## Quick Start

> This example will show you how to start the Selenium 2 Hub, and register both a WebDriver node and a Selenium 1 RC legacy node. We’ll also show you how to call the grid from Java. The hub and nodes are shown here running on the same machine, but of course you can copy the selenium-server-standalone to multiple machines. Note: The selenium-server-standalone package includes the Hub, WebDriver, and legacy RC needed to run the grid. Ant is not required anymore. You can download the selenium-server-standalone-`*`.jar from <http://selenium-release.storage.googleapis.com/index.html> This walk-through assumes you already have Java installed.

**Step 1: Start the hub**

The Hub is the central point that will receive all the test request and distribute them the the right nodes.

Open a command prompt and navigate to the directory where you copied the selenium-server-standalone file. Type the following command:               java -jar selenium-server-standalone-<version>.jar -role hub     

The hub will automatically start-up using port 4444 by default. To change the default port, you can add the optional parameter -port when you run the command. You can view the status of the hub by opening a browser window and navigating to: http://localhost:4444/grid/console

**Step 2: Start the nodes**

Regardless on whether you want to run a grid with new WebDriver functionality, or a grid with Selenium 1 RC functionality, or both at the same time, you use the same selenium-server-standalone jar file to start the nodes.               java -jar selenium-server-standalone-<version>.jar -role node  -hub http://localhost:4444/grid/register     

Note: The port defaults to 5555 if not specified whenever the “-role” option is provided and is not hub.

For backwards compatibility “wd” and “rc” roles are still a valid subset of the “node” role. But those roles limit the types of remote connections to their corresponding API, while “node” allows both RC and WebDriver remote connections.

### Using grid to run tests

\( using java as an example \) Now that the grid is in-place, we need to access the grid from our test cases. For the Selenium 1 RC nodes, you can continue to use the DefaultSelenium object and pass in the hub information:               Selenium selenium = new DefaultSelenium(“localhost”, 4444, “*firefox”, “http://www.google.com”);     

For WebDriver nodes, you will need to use the **RemoteWebDriver** and the **DesiredCapabilities** object to define which browser, version and platform you wish to use. Create the target browser capabilities you want to run the tests against:               DesiredCapabilities capability = DesiredCapabilities.firefox();     

Pass that into the RemoteWebDriver object:               WebDriver driver = new RemoteWebDriver(new URL("http://localhost:4444/wd/hub"), capability);     

The hub will then assign the test to a matching node.

A node matches if all the requested capabilities are met. To request specific capabilities on the grid, specify them before passing it into the WebDriver object.               capability.setBrowserName();     capability.setPlatform();     capability.setVersion()     capability.setCapability(,);     

Example: A node registered with the setting:                -browser  browserName=firefox,version=3.6,platform=LINUX     

> will be a match for:               capability.setBrowserName(“firefox” );      capability.setPlatform(“LINUX”);       capability.setVersion(“3.6”);     

and would also be a match for               capability.setBrowserName(“firefox” );      capability.setVersion(“3.6”);     

The capabilities that are not specified will be ignored. If you specify capabilities that do not exist on your grid \(for example, your test specifies Firefox version 4.0, but have no Firefox 4 instance\) then there will be no match and the test will fail to run.

## Configuring the nodes

The node can be configured in 2 different ways; one is by specifying command-line parameters, the other is by specifying a JSON file.

### Configuring the nodes by command line

By default, starting the node allows for concurrent use of 11 browsers…: 5 Firefox, 5 Chrome, 1 Internet Explorer. The maximum number of concurrent tests is set to 5 by default. To change this and other browser settings, you can pass in parameters to each -browser switch \(each switch represents a node based on your parameters\). If you use the -browser parameter, the default browsers will be ignored and only what you specify command line will be used.               -browser browserName=firefox,version=3.6,maxInstances=5,platform=LINUX     

This setting starts 5 Firefox 3.6 nodes on a Linux machine.

If your remote machine has multiple versions of Firefox you’d like to use, you can map the location of each binary to a particular version on the same machine:               -browser browserName=firefox,version=3.6,firefox_binary=/home/myhomedir/firefox36/firefox,maxInstances=3,platform=LINUX -browser browserName=firefox,version=4,firefox_binary=/home/myhomedir/firefox4/firefox,maxInstances=4,platform=LINUX     

Tip: If you need to provide a space somewhere in your browser parameters, then surround the parameters with quotation marks:               -browser “browserName=firefox,version=3.6,firefox_binary=c:\Program Files\firefox ,maxInstances=3, platform=WINDOWS”     

### Optional parameters

  * `-port 4444` \(4444 is default\)   * `-host <IP | hostname>` specify the hostname or IP. usually not needed and determined automatically. For exotic network configuration, network with VPN, specifying the host might be necessary.   * `-timeout 30` \(300 is default\) The timeout in seconds before the hub automatically releases a node that hasn’t received any requests for more than the specified number of seconds. After this time, the node will be released for another test in the queue. This helps to clear client crashes without manual intervention. To remove the timeout completely, specify -timeout 0 and the hub will never release the node.

> Note: This is NOT the WebDriver timeout for all ”wait for WebElement” type of commands.

  * `-maxSession 5` \(5 is default\) The maximum number of browsers that can run in parallel on the node. This is different from the maxInstance of supported browsers \(Example: For a node that supports Firefox 3.6, Firefox 4.0 and Internet Explorer 8, maxSession=1 will ensure that you never have more than 1 browser running. With maxSession=2 you can have 2 Firefox tests at the same time, or 1 Internet Explorer and 1 Firefox test\).

  * `-browser < params >` If -browser is not set, a node will start with 5 firefox, 1 chrome, and 1 internet explorer instance \(assuming it’s on a windows box\). This parameter can be set multiple times on the same line to define multiple types of browsers. Parameters allowed for -browser: browserName=\{android, chrome, firefox, htmlunit, internet explorer, iphone, opera\} version=\{browser version\} firefox\_binary=\{path to executable binary\} chrome\_binary=\{path to executable binary\} maxInstances=\{maximum number of browsers of this type\} platform=\{WINDOWS, LINUX, MAC\}

  * `-registerCycle N` = how often in ms the node will try to register itself again. Allow to restart the hub without having to restart the nodes.

  * Really large \(>50 node\) Hub installations may need to increase the jetty threads by setting -DPOOL\_MAX=512 \(or larger\) on the java command line.

### Configuring timeouts \(Version 2.21 required\)

Timeouts in the grid should normally be handled through webDriver.manage\(\).timeouts\(\), which will control how the different operations time out.

To preserve run-time integrity of a grid with selenium-servers, there are two other timeout values that can be set.

On the hub, setting the -timeout command line option to “30” seconds will ensure all resources are reclaimed 30 seconds after a client crashes. On the hub you can also set -browserTimeout 60 to make the maximum time a node is willing to hang inside the browser 60 seconds. This will ensure all resources are reclaimed slightly after 60 seconds. All the nodes use these two values from the hub if they are set. Locally set parameters on a single node has precedence, it is generally recommended not to set these timeouts on the node.

The browserTimeout **should** be:

  * Higher than the socket lock timeout \(45 seconds\)   * Generally higher than values used in webDriver.manage\(\).timeouts\(\), since this mechanism is a “last line of defense”.

### Configuring the nodes by JSON

> java -jar selenium-server-standalone.jar -role node -nodeConfig nodeconfig.json

A sample nodeconfig file for server version 3.x.x \(>= beta4\) can be seen at <https://github.com/SeleniumHQ/selenium/blob/selenium-3.141.59/java/server/src/org/openqa/grid/common/defaults/DefaultNodeWebDriver.json>

A sample nodeconfig file for server version 2.x.x can be seen at <https://github.com/SeleniumHQ/selenium/blob/selenium-2.53.0/java/server/src/org/openqa/grid/common/defaults/DefaultNode.json>

Note: the `configuration { ... }` object in version 2.x.x has been flattened in version 3.x.x \(>= beta4\)

### Configuring the hub by JSON

> java -jar selenium-server-standalone.jar -role hub -hubConfig hubconfig.json

A sample hubconfig.json file can be seen at <https://github.com/SeleniumHQ/selenium/blob/selenium-3.141.59/java/server/src/org/openqa/grid/common/defaults/DefaultHub.json>

## Hub diagnostic messages

Upon detecting anomalous usage patterns, the hub can give the following message:               Client requested session XYZ that was terminated due to REASON     

**Reason**| **Cause/fix**   ---|---   TIMEOUT| The session timed out because the client did not access it within the timeout. If the client has been somehow suspended, this may happen when it wakes up   BROWSER\_TIMEOUT| The node timed out the browser because it was hanging for too long \(parameter browserTimeout\)   ORPHAN| A client waiting in queue has given up once it was offered a new session   CLIENT\_STOPPED\_SESSION| The session was stopped using an ordinary call to stop/quit on the client. Why are you using it again??   CLIENT\_GONE| The client process \(_your_ code\) appears to have died or otherwise not responded to our requests, intermittent network issues may also cause   FORWARDING\_TO\_NODE\_FAILED| The hub was unable to forward to the node. Out of memory errors/node stability issues or network problems   CREATIONFAILED| The node failed to create the browser. This can typically happen when there are environmental/configuration problems on the node. Try using the node directly to track problem.   PROXY\_REREGISTRATION| The session has been discarded because the node has re-registered on the grid \(in mid-test\)      ### Tips for running with grid

If your tests are running in parallel, make sure that each thread deallocates its webdriver resource independently of any other tests running on other threads. Starting 1 browser per thread at the start of the test-run and deallocating all browsers at the end is **not** a good idea. \(If one test-case decides to consume abnormal amounts of time you may get timeouts on all the other tests because they’re waiting for the slow test. This can be very confusing\)

## Selenium Grid Platforms

\(previously located: <https://github.com/SeleniumHQ/selenium/wiki/Grid-Platforms>\)

This section describes the PLATFORM option used in configuring Selenium Grid Nodes and \[[DesiredCapabilities](https://www.selenium.dev/documentation/legacy/selenium_2/DesiredCapabilities)\] object.

### History of Platforms

When requesting a new WebDriver session from the Grid, user can specify the \[[DesiredCapabilities](https://www.selenium.dev/documentation/legacy/selenium_2/DesiredCapabilities)\] of the remote browser. Things such as the browser name, version, and platform are among the list of options that can be specified by the test. Specifying desired.

The following code demonstrates the DesiredCapability of Internet Explorer, version 9, on Windows XP platform:               	[[DesiredCapabilities]] capability = DesiredCapabilities.internetExplorer();     	capability.setVersion("8");     	capability.setPlatform(Platform.XP);     	WebDriver driver = new RemoteWebDriver(new URL("http://localhost:4444/wd/hub"), capability);     

The request for a new session with specified DesiredCapability is sent to the Grid Hub, which will look through all of the registered nodes to see if any of them match the specification given by the test. If no node matches the specification, a CapabilityNotPresentOnTheGridException will be returned.

It is a common misconception that the PLATFORM determines the ability to choose the Operating System on which the new session will be created. In this situation, platform and operating system are not the same, thus specifying the platform to “Windows 2003 Server” will not allow you to choose between a Windows XP, Vista, and 2003 server. This misconception can be born from platforms such as Mac OSX and Linux, where the name of the platform matches the name of the Operating System.

In case of Selenium Grid, platform refers to the underlying interactions between the Driver Atoms and the web browser. Mac OSX and Linux based Operating Systems \(Centos, Ubuntu, Debian, etc..\) have a relatively stable communication with the web browsers such as Firefox and Chrome. Thus the platform names are simple to understand, as seen in the example bellow:                  capability.setPlatform(Platform.MAC);   //Set platform to OSX        capability.setPlatform(Platform.LINUX); // Set platform to Linux based systems     

The prior to release of Vista, Windows based Operating Systems only had one platform, shown here:               	capability.setPlatform(Platform.WINDOWS); //Set platform to Windows     

However, with the introduction of UAC in Windows Vista, there were major changes done to the underlying interactions between WebDriver and Internet Explorer. To work around the UAC constrains a new platform was added to nodes with Windows based Operating systems:               	capability.setPlatform(Platform.VISTA); //Set platform to VISTA     

With the release of Windows 8, another major overhaul happened in how the WebDriver communicates with Internet Explorer, thus a new platform was added for Windows 8 based nodes:               	capability.setPlatform(Platform.WIN8); //Set platform to Windows 8     

Similar story happened with introduction of Windows 8.1, in this example the platform is set to Windows 8.1:               	capability.setPlatform(Platform.WIN8_1); //Set platform to Windows 8.1     

### Operating System Platforms

The following list demonstrates some of the Operating Systems, and what Platform they are part of:

**MAC\*\*\*\*All OSX Operating Systems** LINUX Centos Ubuntu **UNIX****Solaris**** BSD** XP Windows Server 2003 Windows XP Windows NT **VISTA****Windows Vista**** Windows 2008 Server\*\*\*\*Windows 7** WIN8 Windows 2012 Server Windows 8 **WIN8\_1\*\*\*\*Windows 8.1**

### Families

Different platforms are grouped into “Families” of platform. For example, Win8 and XP platforms are a part of the WINDOWS family. Similarly ANDROID and LINUX are part of the UNIX family.

### Choosing Platform and Platform Family

When setting a platform on the \[[DesiredCapabilities](https://www.selenium.dev/documentation/legacy/selenium_2/DesiredCapabilities)\] object, we can set an individual platform or family of platforms. For example:                 	capability.setPlatform(Platform.VISTA); //Will return a node with Windows Vista or 2008 Server or Windows 7 Operating System.       	capability.setPlatform(Platform.XP);   //Will return a node with Windows XP or 2003 Server or Windows 2000 Professional Operating System.          	capability.setPlatform(Platform.WINDOWS); //Will return a node with ANY Windows Operating System     

### More Information

For more information on the latest platforms, please view this file:

org.openqa.selenium.Platform.java

# 5 - History of Grid Platforms

Information for working with platform names in Grid 2.

This documentation previously located [on the wiki](https://github.com/SeleniumHQ/selenium/wiki/Grid-Platforms)   You can read more about [Grid 2](https://www.selenium.dev/documentation/legacy/selenium_2/grid_2/)

## Selenium Grid Platforms

This section describes the PLATFORM option used in configuring Selenium Grid Nodes and \[[DesiredCapabilities](https://www.selenium.dev/documentation/legacy/selenium_2/DesiredCapabilities)\] object.

### History of Platforms

When requesting a new WebDriver session from the Grid, user can specify the \[[DesiredCapabilities](https://www.selenium.dev/documentation/legacy/selenium_2/DesiredCapabilities)\] of the remote browser. Things such as the browser name, version, and platform are among the list of options that can be specified by the test. Specifying desired.

The following code demonstrates the DesiredCapability of Internet Explorer, version 9, on Windows XP platform:               	[[DesiredCapabilities]] capability = DesiredCapabilities.internetExplorer();     	capability.setVersion("8");     	capability.setPlatform(Platform.XP);     	WebDriver driver = new RemoteWebDriver(new URL("http://localhost:4444/wd/hub"), capability);     

The request for a new session with specified DesiredCapability is sent to the Grid Hub, which will look through all of the registered nodes to see if any of them match the specification given by the test. If no node matches the specification, a CapabilityNotPresentOnTheGridException will be returned.

It is a common misconception that the PLATFORM determines the ability to choose the Operating System on which the new session will be created. In this situation, platform and operating system are not the same, thus specifying the platform to “Windows 2003 Server” will not allow you to choose between a Windows XP, Vista, and 2003 server. This misconception can be born from platforms such as Mac OSX and Linux, where the name of the platform matches the name of the Operating System.

In case of Selenium Grid, platform refers to the underlying interactions between the Driver Atoms and the web browser. Mac OSX and Linux based Operating Systems \(Centos, Ubuntu, Debian, etc..\) have a relatively stable communication with the web browsers such as Firefox and Chrome. Thus the platform names are simple to understand, as seen in the example bellow:                  capability.setPlatform(Platform.MAC);   //Set platform to OSX        capability.setPlatform(Platform.LINUX); // Set platform to Linux based systems     

The prior to release of Vista, Windows based Operating Systems only had one platform, shown here:               	capability.setPlatform(Platform.WINDOWS); //Set platform to Windows     

However, with the introduction of UAC in Windows Vista, there were major changes done to the underlying interactions between WebDriver and Internet Explorer. To work around the UAC constrains a new platform was added to nodes with Windows based Operating systems:               	capability.setPlatform(Platform.VISTA); //Set platform to VISTA     

With the release of Windows 8, another major overhaul happened in how the WebDriver communicates with Internet Explorer, thus a new platform was added for Windows 8 based nodes:               	capability.setPlatform(Platform.WIN8); //Set platform to Windows 8     

Similar story happened with introduction of Windows 8.1, in this example the platform is set to Windows 8.1:               	capability.setPlatform(Platform.WIN8_1); //Set platform to Windows 8.1     

### Operating System Platforms

The following list demonstrates some of the Operating Systems, and what Platform they are part of:

**MAC\*\*\*\*All OSX Operating Systems** LINUX Centos Ubuntu **UNIX****Solaris**** BSD** XP Windows Server 2003 Windows XP Windows NT **VISTA****Windows Vista**** Windows 2008 Server\*\*\*\*Windows 7** WIN8 Windows 2012 Server Windows 8 **WIN8\_1\*\*\*\*Windows 8.1**

### Families

Different platforms are grouped into “Families” of platform. For example, Win8 and XP platforms are a part of the WINDOWS family. Similarly ANDROID and LINUX are part of the UNIX family.

### Choosing Platform and Platform Family

When setting a platform on the \[[DesiredCapabilities](https://www.selenium.dev/documentation/legacy/selenium_2/DesiredCapabilities)\] object, we can set an individual platform or family of platforms. For example:                 	capability.setPlatform(Platform.VISTA); //Will return a node with Windows Vista or 2008 Server or Windows 7 Operating System.       	capability.setPlatform(Platform.XP);   //Will return a node with Windows XP or 2003 Server or Windows 2000 Professional Operating System.          	capability.setPlatform(Platform.WINDOWS); //Will return a node with ANY Windows Operating System     

### More Information

For more information on the latest platforms, please view this file:

org.openqa.selenium.Platform.java

# 6 - Remote WebDriver standalone server

Working with the Standalone Server.

This documentation previously located [on the wiki](https://github.com/SeleniumHQ/selenium/wiki/RemoteWebDriverServer)

The server will always run on the machine with the browser you want to test. The server can be used either from the command line or through code configuration.

## Starting the server from the command line

Once you have downloaded `selenium-server-standalone-{VERSION}.jar`, place it on the computer with the browser you want to test. Then, from the directory with the jar, run the following:               java -jar selenium-server-standalone-{VERSION}.jar     

## Considerations for running the server

The caller is expected to terminate each session properly, calling either `Selenium#stop()` or `WebDriver#quit`.

The selenium-server keeps in-memory logs for each ongoing session, which are cleared when `Selenium#stop()` or `WebDriver#quit` is called. If you forget to terminate these sessions, your server may leak memory. If you keep extremely long-running sessions, you will probably need to stop/quit every now and then \(or increase memory with -Xmx jvm option\).

## Timeouts \(from version 2.21\)

The server has two different timeouts, which can be set as follows:               java -jar selenium-server-standalone-{VERSION}.jar -timeout=20 -browserTimeout=60     

  * browserTimeout     * Controls how long the browser is allowed to hang \(value in seconds\).   * timeout     * Controls how long the client is allowed to be gone before the session is reclaimed \(value in seconds\).

The system property `selenium.server.session.timeout` is no longer supported as of 2.21.

Please note that the `browserTimeout` is intended as a backup timeout mechanism when the ordinary timeout mechanism fails, which should be used mostly in grid/server environments to ensure that crashed/lost processes do not stay around for too long, polluting the runtime environment.

## Configuring the server programmatically

In theory, the process is as simple as mapping the `DriverServlet` to a URL, but it is also possible to host the page in a lightweight container, such as Jetty, configured entirely in code.

  * Download the `selenium-server.zip` and unpack.   * Put the JARs on the CLASSPATH.   * Create a new class called `AppServer`. Here, we are using Jetty, so you will need to [download](https://www.eclipse.org/jetty/download.html) that as well:

              import org.mortbay.jetty.Connector;     import org.mortbay.jetty.Server;     import org.mortbay.jetty.nio.SelectChannelConnector;     import org.mortbay.jetty.security.SslSocketConnector;     import org.mortbay.jetty.webapp.WebAppContext;          import javax.servlet.Servlet;     import java.io.File;          import org.openqa.selenium.remote.server.DriverServlet;          public class AppServer {       private Server server = new Server();            public AppServer() throws Exception {         WebAppContext context = new WebAppContext();         context.setContextPath("");         context.setWar(new File("."));         server.addHandler(context);              context.addServlet(DriverServlet.class, "/wd/*");              SelectChannelConnector connector = new SelectChannelConnector();         connector.setPort(3001);         server.addConnector(connector);              server.start();       }     }     

# 7 - Limitations of scaling up tests in Selenium 2

Summary of additional constraints that arise when running Selenium2 in parallel.

This documentation previously located [on the wiki](https://github.com/SeleniumHQ/selenium/wiki/Scaling-WebDriver)

## Running parallel Selenium2

This page tries to summarize additional constraints that arise when running Selenium2 in parallel.

### WebDriver instantiation

While an individual WebDriver instance cannot be shared among threads, it is easy to create multiple WebDriver instances.

### Ephemeral sockets

There is a general problem of TCP/IP v4, where the TCP/IP stack uses ephemeral ports when making a connection between two sockets. The typical symptom of this is that connection failures start appearing after a short time of running, often a minute or two. The message will vary somewhat but it always appears after some time, and if you reduce the number of browsers it will eventually work fine.

[Wikipedia on Ephemeral ports](http://en.wikipedia.org/wiki/Ephemeral_port) or a quick google of “ephemeral sockets ” will tell you what your current OS delivers and how to set it.

Currently \(2.13.0\) it seems like a firefox running at full blast consumes something in the range of 2000 ephemeral ports per firefox; your mileage will vary here. This means you can run out of ephemeral port on Windows XP with as litttle as 2 browsers, maybe even 1 if you for instance iterate extermly quickly .

#### Will it be fixed ?

The solution to the ephemeral socket problem is HTTP1.1 keep alive on the connections. Firefox does not support keep-alive as of version 2.13.0.

#### Things that are fixed

  * The java client.   * Selenium server \(“rc”\).   * Selenium grid hub & nodes   * The ruby bindings \(see notes in [RubyBindings](https://www.selenium.dev/documentation/legacy/selenium_2/RubyBindings.md)\).   * The IE driver.   * ChromeDriver

The means you can use the java client to scale out to remote boxes running selenium server and never have any problems on the central build server. You may need to solve socket problems on the remote boxes though.

#### Microsoft Windows

If you are using the old versions of Windows \(<=2003, inc XP\) you should not be waiting for port usage to get low enough to fit in this space. That may simply never happen, although some combinations probably will. See <http://support.microsoft.com/kb/196271> on how to adjust it.

If you for technical reasons cannot adjust the port range on your Windows machine you will not be able to run more than 2-3 firefox browsers.

### Avoiding the socket lock

Starting new browsers between each test class/test method is slow, and the socket lock also uses Ephemeral sockets, worsening the problem described above.

If you’re using a suite-less test setup \(like many JUnit4 users\), you often start/stop the browsers in @BeforeClass/@AfterClass methods. Another option is to start the browsers in @BeforeClass and use something like JUnit/TestNG run listeners to shut down all the browsers at the end of the test run. Maven surefire supports run listeners for both JUnit and TestNG.

\(TODO: Strategies to disable the socket lock and manage the ports yourself\)

### Native events

Due to a shared file in the native events logic, the firefox driver should probably not be using native events when running concurrently. \(Watch [this issue](http://code.google.com/p/selenium/issues/detail?id=1326)\).

# 8 - Stealing focus from Firefox in Linux

How to work with Native Events in the Legacy Firefox extension.

This documentation previously located [on the wiki](https://github.com/SeleniumHQ/selenium/wiki/Focus-Stealing-On-Linux)

This page describes an essential component of the native events implementation on Linux - focus maintaining. In order for native events to be processed in Firefox, it must always retain focus. In case the user decides to switch to another window \(a thing which could be understood\), Firefox must not know it lost focus.

### Solution overview

#### Basic idea

The basic idea is to get between the XLib \(X-Windows client library\) layer and the application. X-Windows notifies the application of events \(user input, windows being destroyed, mouse movements\) by asynchronous events. The events that indicate loss of focus [FocusOut](http://tronche.com/gui/x/xlib/events/input-focus/) are discarded. The idea is based on Jordan Sissel’s implementation of a pre-loaded library that over-rides XNextEvent - see <http://www.semicomplete.com/blog/geekery/xsendevent-xdotool-and-ld_preload.html>.

#### Extension

This simple implementation works well as long as there’s one browser window. When multiple windows are involved, several challenges arise:

  * Even though new windows may be opened, native events must continue to flow to the active window. However, most window managers will give focus to newly-opened windows.   * Window Switching: When wishing to switch to another window, the focus has to be moved. This requires cooperation between WebDriver’s Firefox extension and this component.   * Closing windows: When a window is closed, focus must move to another window. By design, WebDriver does not guarantee anything if the active window is closed - until a new window is being switched to. In this situation, special care must be taken.

### Interaction with other components

The basic idea requires no interaction with other components of WebDriver. However, when multiple windows are involved - creating, switching or destroying, this component should be aware of it. New window creation cannot be tracked - as it may happen as a side effect of many operations. Switching and closing can be tracked.

### Involved technologies

To understand this solution, one should be familiar with X-Windows and its events. Knowledge of the GDK event processing loop is also useful.

## Implementation Details

All of this describes the code in `firefox/src/cpp/linux-specific/x_ignore_nofocus.c`.

### The shared library

Hijacking the events is done by over-riding XNextEvent. A shared library containing a modified implementation of `XNextEvent` is loaded using `LD_PRELOAD`. The modified function opens `/usr/lib/libX11.so.6` and invokes the real function. Then the event that the real function returns \(i.e. the real event\) is inspected.

### Identifying events

Under the basic idea, `FocusOut` events will be simply discarded. However, window switching complicates matters.

#### Data structure

There’s a global data structure that remembers the following information:

  * The active window ID \(if there is such one at the moment\)   * The ID of a new window that’s being created \(again, if exists\)   * If window switching is in progress.   * If window closing is in progress.   * Was the focus given to another window and should be stolen back to the active one?   * Was a `FocusIn` event already received by the active window?   * Did we set the currently active window as a result of a close operation?

#### Firefox starts up

`FocusIn` event arrives and the active window ID is 0. A new active window is set. Note that during the creation of the main window, another sub-window is created and a `FocusOut` event is sent to the active window. Fortunately, this `FocusOut` event indicates that the focus is going to move to a sub-window \(identified by `NotifyInferior`\) so it is allowed.

#### The user has switched to another window

This is indicated by a `FocusOut` event with a detail field that is neither `NotifyAncestor` nor `NotifyInferior`. This event is simply discarded and replaced with a `KeymapNotify` event, which is promptly discarded by GDK.

#### A new window is being created

This condition is identified by a `ReparentNotify` event. When this happens, the new\_window field will be set to the ID of the newly created window. Subsequent `FocusOut` events will be allowed - during the new window creation events will flow as usual \(`FocusOut` event from the active window, `FocusIn` event to the new window, `FocusOut` to the new window and `FocusIn` to a sub-window of the new window\). After the sub-window of the new window receives `FocusIn`, a call to `XSetInputFocus` will be issued to return the focus to the active window.

#### A window switch occurs

During a window switch events will flow as normal. A window switch is considered done when the sub-window of a window receives the `FocusIn` event. A window switch starts by identifying the file `/tmp/switch_window_started`. In this file, a `switch:` string following a window ID is written \(the ID is just for debugging purpose\). This will change the active window ID to 0 and the state to “during switch”. During a switch \(or when there’s no active window\) no events are discarded.

#### A window is being closed

Very similar to window switching \(also identified by reading the file\). However, it is indicated that the window is being closed - in case it was closed, no focus stealing will take place. In addition, the `DestroyNotify` event is being identified to find out when the active window is being closed \(explicitly by the user or implicitly by some other operation that is not an explicit call to close\). In this case, the active window ID will be set to 0 as well.

## Important Links

  * Jordan Sissel’s original [XSendEvent hack](http://www.semicomplete.com/blog/geekery/xsendevent-xdotool-and-ld_preload.html)   * [XLib events](http://tronche.com/gui/x/xlib/events/structures.html) and the [XLib programming manual](http://www.sbin.org/doc/Xlib/)   * [The X programming manual / specification](http://www.x.org/docs/X11/xlib.pdf)

# 9 - Untrusted SSL Certificates

Details on how Selenium 2 accepted untrusted SSL certificates

This documentation previously located [on the wiki](https://github.com/SeleniumHQ/selenium/wiki/Untrusted-SSL-Certificates)

## Introduction

This page details how WebDriver is able to accept untrusted SSL certificates, allowing users to test trusted sites in a testing environment, where valid certificates usually do not exist. This feature is turned on by default for all supported browsers \(Currently Firefox\).

## Firefox

### Outline of solution

Firefox has an interface for overriding invalid certificates, called nsICertOverrideService. Implement this interface as a proxy to the original service - **unless** untrusted certificates are allowed. In that case, when asked about a certificate \(a call to hasMatchingOverride for an invalid certificate\) - indicate it’s trusted.

### Implementation details

Implementing the idea is mostly straightforward - badCertListener.js is a stand-alone module, that, when loaded, registers a factory for returning an instance of the service. The interesting function is hasMatchingOverride:               WdCertOverrideService.prototype.hasMatchingOverride = function(         aHostName, aPort, aCert, aOverrideBits, aIsTemporary)     

The aOverrideBits and aIsTemporary are output arguments. This is where things get a bit tricky: There are three possible override bits:                 ERROR_UNTRUSTED: 1,       ERROR_MISMATCH: 2,       ERROR_TIME: 4     

It’s impossible to just set them all, since Firefox expects a perfect match between the offences generated by the certificate and the function’s return value: \(security/manager/ssl/src/SSLServerCertVerification.cpp:302\):                 if (overrideService)       {         PRBool haveOverride;         PRBool isTemporaryOverride; // we don't care                nsrv = overrideService->HasMatchingOverride(hostString, port,                                                     ix509,                                                      &overrideBits,                                                     &isTemporaryOverride,                                                      &haveOverride);         if (NS_SUCCEEDED(nsrv) && haveOverride)          {           // remove the errors that are already overriden           remaining_display_errors -= overrideBits;         }       }            if (!remaining_display_errors) {         // all errors are covered by override rules, so let's accept the cert         return SECSuccess;       }     

The exact mapping of violation to error code can be easily seen at security/manager/pki/resources/content/exceptionDialog.js \(in Firefox source\):                 var flags = 0;       if(gSSLStatus.isUntrusted)         flags |= overrideService.ERROR_UNTRUSTED;       if(gSSLStatus.isDomainMismatch)         flags |= overrideService.ERROR_MISMATCH;       if(gSSLStatus.isNotValidAtThisTime)         flags |= overrideService.ERROR_TIME;     

The SSL status can be obtained from `"@mozilla.org/security/recentbadcerts;1"` usually - However, the certificate \(and its status\) are added to this service only **after** the call to `hasMatchingOverride`, so there is no easy way to find out the certificate’s SSLStatus. Instead, the checks have to be executed manually.

Two checks are carried out:

  * Calling `nsIX509Cert.verifyForUsage`   * Comparing hostname against `nsIX509Cert.commonName`. If those are not equal, `ERROR_MISMATCH` is set.

The second check indicates whether `ERROR_MISMATCH` should be set. The first check should indicate whether `ERROR_UNTRUSTED` and `ERROR_TIME` should be set. Unfortunately, it does not work reliably when the certificate expired **and** is from an untrusted issuer. When the certificate has expired, the return code would be `CERT_EXPIRED` even if it is also untrusted. For this reason, the FirefoxDriver assumes that certificates will be untrusted - it **always** sets the `ERROR_UNTRUSTED` bit - the other two will be set only if the conditions for them are met.

This could pose a problem for someone testing a site with a valid certificate that does not match the host name it’s served from \(e.g. test environment serving production certificates\). An additional feature for `FirefoxProfile` was added: `FirefoxProfile.setAssumeUntrustedCertificateIssuer`. Calling this function with `false` will turn the `ERROR_UNTRUSTED` bit off and allow a user to work in such situation.

## HTMLUnit

Not tested yet.

## IE

Not implemented yet.

## Chrome

Not implemented yet.

# 10 - WebDriver For Mobile Browsers

Describes how Selenium 2 supported Android and iOS before Appium was created

This documentation previously located [on the wiki](https://github.com/SeleniumHQ/selenium/wiki/Untrusted-SSL-Certificates)

## Introduction

We provide mobile drivers for two major mobile platforms: Android and iOS \(iPhone & iPad\).

They can be run on real devices and in an Android emulator or in the iOS Simulator, as appropriate. They are packaged as an app. The app needs to be installed on the emulator or device. The app embeds a [RemoteWebDriver server](https://github.com/SeleniumHQ/selenium/wiki/RemoteWebDriverServer) and a light-weight HTTP server which receive, and respond to, requests from WebDriver Clients i.e. from your automated tests.

The connection between the server on the mobile platform and your tests uses an IP connection. The connection may need to be configured. For Android you can connect establish an IP connection over USB.

In some cases your existing WebDriver tests may run successfully e.g. where a common web site serves mobile and desktop users and where the UI is relatively straight-forward. However in other cases you may end up needing to create specific tests for the mobile site; particularly when the site provides specific capabilities, user interfaces, etc. for mobile browsers.

Even when a common web site serves both desktop and mobile browsers, you may want to consider writing specific tests that incorporate factors such as the screen-size of the mobile devices, and different ways users are likely to interact with your web site or web app.

## Getting Started

[Android Setup](https://github.com/SeleniumHQ/selenium/wiki/AndroidDriver)

[iPhone & iPad Setup](https://github.com/SeleniumHQ/selenium/wiki/IPhoneDriver)

## Additional Mobile Platforms

There are several related opensource projects that include support for other Mobile platforms. These include:

[Blackberry WebDriver](http://code.google.com/p/webdriver-blackberry/), for BlackBerry 5.0 and onward.

[Headless WebKit WebDriver](http://code.google.com/p/webkitdriver/). Many mobile browsers are WebKit based. Headless WebKit provides a fast light-weight solution.

These projects don’t appear to be active, however they may provide a starting point for future work on these platforms.

# 11 - Frequently Asked Questions for Selenium 2

Items of interest for moving from Selenium 1 to Selenium 2

This documentation previously located [on the wiki](https://github.com/SeleniumHQ/selenium/wiki/Frequently-Asked-Questions) \

### Q: What is WebDriver?

A: WebDriver is a tool for writing automated tests of websites. It aims to mimic the behaviour of a real user, and as such interacts with the HTML of the application.

### Q: So, is it like [Selenium](http://www.openqa.org/selenium-core/)? Or [Sahi](http://sahi.co.in/)?

A: The aim is the same \(to allow you to test your webapp\), but the implementation is different. Rather than running as a Javascript application within the browser \(with the limitations this brings, such as the “[same origin](http://www.openqa.org/selenium-rc/tutorial.html)” problem\), WebDriver controls the browser itself. This means that it can take advantage of any facilities offered by the native platform.

### Q: What is Selenium 2.0?

A: WebDriver is part of [Selenium](http://www.openqa.org/selenium). The main contribution that WebDriver makes is its API and the native drivers.

### Q: How do I migrate from using the original Selenium APIs to the new WebDriver APIs?

A: The process is described in the Selenium documentation at <http://seleniumhq.org/docs/appendix_migrating_from_rc_to_webdriver.html>

### Q: Which browsers does WebDriver support?

A: The existing drivers are the ChromeDriver, InternetExplorerDriver, FirefoxDriver, OperaDriver and HtmlUnitDriver. For more information about each of these, including their relative strengths and weaknesses, please follow the links to the relevant pages. There is also support for mobile testing via the AndroidDriver, OperaMobileDriver and IPhoneDriver.

### Q: What does it mean to be “developer focused”?

A: We believe that within a software application’s development team, the people who are best placed to build the tools that everyone else can use are the developers. Although it should be easy to use WebDriver directly, it should also be easy to use it as a building block for more sophisticated tools. Because of this, WebDriver has a small API that’s easy to explore by hitting the “autocomplete” button in your favourite IDE, and aims to work consistently no matter which browser implementation you use.

### Q: How do I execute Javascript directly?

A: We believe that most of the time there is a requirement to execute Javascript there is a failing in the tool being used: it hasn’t emitted the correct events, has not interacted with a page correctly, or has failed to react when an XmlHttpRequest returns. We would rather fix WebDriver to work consistently and correctly than rely on testers working out which Javascript method to call.

We also realise that there will be times when this is a limitation. As a result, for those browsers that support it, you can execute Javascript by casting the WebDriver instance to a JavascriptExecutor \(`http://selenium.googlecode.com/svn/trunk/docs/api/java/org/openqa/selenium/JavascriptExecutor.html`\). In Java, this looks like:               WebDriver driver; // Assigned elsewhere     JavascriptExecutor js = (JavascriptExecutor) driver;     js.executeScript("return document.title");     

Other language bindings will follow a similar approach. Take a look at the UsingJavascript page for more information.

### Q: Why is my Javascript execution always returning null?

A: You need to return from your javascript snippet to return a value, so:               js.executeScript("document.title");     

will return null, but:               js.executeScript("return document.title");     

will return the title of the document.

### Q: My XPath finds elements in one browser, but not in others. Why is this?

A: The short answer is that each supported browser handles XPath slightly differently, and you’re probably running into one of these differences. The long answer is on the XpathInWebDriver page.

### Q: The InternetExplorerDriver does not work well on Vista. How do I get it to work as expected?

A: The InternetExplorerDriver requires that all security domains are set to the same value \(either trusted or untrusted\) If you’re not in a position to modify the security domains, then you can override the check like this:               DesiredCapabilities capabilities = DesiredCapabilities.internetExplorer();     capabilities.setCapability(InternetExplorerDriver.INTRODUCE_FLAKINESS_BY_IGNORING_SECURITY_DOMAINS, true);     WebDriver driver = new InternetExplorerDriver(capabilities);     

As can be told by the name of the constant, this may introduce flakiness in your tests. If all sites are in the same protection domain, you _should_ be okay.

### Q: What about support for languages other than Java?

A: Python, Ruby, C\# and Java are all supported directly by the development team. There are also webdriver implementations for PHP and Perl. Support for a pure JS API is also planned.

### Q: How do I handle pop up windows?

A: WebDriver offers the ability to cope with multiple windows. This is done by using the “WebDriver.switchTo\(\).window\(\)” method to switch to a window with a known name. If the name is not known, you can use “WebDriver.getWindowHandles\(\)” to obtain a list of known windows. You may pass the handle to “switchTo\(\).window\(\)”.

### Q: Does WebDriver support Javascript alerts and prompts?

A: Yes, using the Alerts API \(`http://selenium.googlecode.com/svn/trunk/docs/api/java/org/openqa/selenium/Alert.html`\):               // Get a handle to the open alert, prompt or confirmation     Alert alert = driver.switchTo().alert();     // Get the text of the alert or prompt     alert.getText();       // And acknowledge the alert (equivalent to clicking "OK")     alert.accept();     

### Q: Does WebDriver support file uploads?

A: Yes.

You can’t interact with the native OS file browser dialog directly, but we do some magic so that if you call WebElement\#sendKeys\("/path/to/file"\) on a file upload element, it does the right thing. Make sure you don’t WebElement\#click\(\) the file upload element, or the browser will probably hang.

Handy hint: You can’t interact with hidden elements without making them un-hidden. If your element is hidden, it can probably be un-hidden with some code like:               ((JavascriptExecutor)driver).executeScript("arguments[0].style.visibility = 'visible'; arguments[0].style.height = '1px'; arguments[0].style.width = '1px'; arguments[0].style.opacity = 1", fileUploadElement);     

### Q: The “onchange” event doesn’t fire after a call “sendKeys”

A: WebDriver leaves the focus in the element you called “sendKeys” on. The “onchange” event will only fire when focus leaves that element. As such, you need to move the focus, perhaps using a “click” on another element.

### Q: Can I run multiple instances of the WebDriver sub-classes?

A: Each instance of an HtmlUnitDriver, ChromeDriver and FirefoxDriver is completely independent of every other instance \(in the case of firefox and chrome, each instance has its own anonymous profile it uses\). Because of the way that Windows works, there should only ever be a single InternetExplorerDriver instance at one time. If you need to run more than one instance of the InternetExplorerDriver at a time, consider using the Remote\!WebDriver and virtual machines.

### Q: I need to use a proxy. How do I configure that?

A: Proxy configuration is done via the `org.openqa.selenium.Proxy` class like so:               Proxy proxy = new Proxy();     proxy.setProxyAutoconfigUrl("http://youdomain/config");          // We use firefox as an example here.     DesiredCapabilities capabilities = DesiredCapabilities.firefox();     capabilities.setCapability(CapabilityType.PROXY, proxy);          // You could use any webdriver implementation here     WebDriver driver = new FirefoxDriver(capabilities);     

### Q: How do I handle authentication with the HtmlUnitDriver?

A: When creating your instance of the HtmlUnitDriver, override the “modifyWebClient” method, for example:               WebDriver driver = new HtmlUnitDriver() {       protected WebClient modifyWebClient(WebClient client) {         // This class ships with HtmlUnit itself         DefaultCredentialsProvider creds = new DefaultCredentialsProvider();              // Set some example credentials         creds.addCredentials("username", "password");              // And now add the provider to the webClient instance         client.setCredentialsProvider(creds);              return client;       }     };     

### Q: Is WebDriver thread-safe?

A: WebDriver is not thread-safe. Having said that, if you can serialise access to the underlying driver instance, you can share a reference in more than one thread. This is not advisable. You /can/ on the other hand instantiate one WebDriver instance for each thread.

### Q: How do I type into a contentEditable iframe?

A: Assuming that the iframe is named “foo”:               driver.switchTo().frame("foo");     WebElement editable = driver.switchTo().activeElement();     editable.sendKeys("Your text here");     

Sometimes this doesn’t work, and this is because the iframe doesn’t have any content. On Firefox you can execute the following before “sendKeys”:               ((JavascriptExecutor) driver).executeScript("document.body.innerHTML = '<br>'");     

This is needed because the iframe has no content by default: there’s nothing to send keyboard input to. This method call inserts an empty tag, which sets everything up nicely.

Remember to switch out of the frame once you’re done \(as all further interactions will be with this specific frame\):               driver.switchTo().defaultContent();     

### Q: WebDriver fails to start Firefox on Linux due to java.net.SocketException

A: If, when running WebDriver on Linux, Firefox fails to start and the error looks like:               Caused by: java.net.SocketException: Invalid argument             at java.net.PlainSocketImpl.socketBind(Native Method)             at java.net.PlainSocketImpl.bind(PlainSocketImpl.java:365)             at java.net.Socket.bind(Socket.java:571)             at org.openqa.selenium.firefox.internal.SocketLock.isLockFree(SocketLock.java:99)             at org.openqa.selenium.firefox.internal.SocketLock.lock(SocketLock.java:63)     

It may be caused due to IPv6 settings on the machine. Execute:               sudo sysctl net.ipv6.bindv6only=0     

To get the socket to bind both to IPv6 and IPv4 addresses of the host with the same calls. More permanent solution is disabling this behaviour by editing /etc/sysctl.d/bindv6only.conf

### Q: WebDriver fails to find elements / Does not block on page loads

A: This problem can manifest itself in various ways:

  * Using WebDriver.findElement\(…\) throws ElementNotFoundException, but the element is clearly there - inspecting the DOM \(using Firebug, etc\) clearly shows it.   * Calling Driver.get returns once the HTML has been loaded - but Javascript code triggered by the onload event was not done, so the page is incomplete and some elements cannot be found.   * Clicking on an element / link triggers an operation that creates new element. However, calling findElement\(s\) after click returns does not find it. Isn’t click supposed to be blocking?   * How do I know when a page has finished loading?

Explanation: WebDriver has a blocking API, generally. However, under some conditions it is possible for a get call to return before the page has finished loading. The classic example is Javascript starting to run after the page has loaded \(triggered by onload\). Browsers \(e.g. Firefox\) will notify WebDriver when the basic HTML content has been loaded, which is when WebDriver returns. It’s difficult \(if not impossible\) to know when Javascript has finished executing, since JS code may schedule functions to be called in the future, depend on server response, etc. This is also true for clicking - when the platform supports native events \(Windows, Linux\) clicking is done by sending a mouse click event with the element’s coordinates at the OS level - WebDriver cannot track the exact sequence of operations this click creates. For this reason, the blocking API is imperfect - WebDriver cannot wait for all conditions to be met before the test proceeds because it does not know them. Usually, the important matter is whether the element involved in the next interaction is present and ready.

Solution: Use the Wait class to wait for a specific element to appear. This class simply calls findElement over and over, discarding the NoSuchElementException each time, until the element is found \(or a timeout has expired\). Since this is the behaviour desired by default for many users, a mechanism for implicitly-waiting for elements to appear has been implemented. This is accessible through the [WebDriver.manage\(\).timeouts\(\)](http://selenium.googlecode.com/svn/trunk/docs/api/java/org/openqa/selenium/WebDriver.Timeouts.html) call. \(This was previously tracked on issue [26](http://code.google.com/p/selenium/issues/detail?id=26)\).

### Q: How can I trigger arbitrary events on the page?

A: WebDriver aims to emulate user interaction - so the API reflects the ways a user can interact with various elements.

Triggering a specific event cannot be achieved directly using the API, but one can use the Javascript execution abilities to call methods on an element.

### Q: Why is it not possible to interact with hidden elements?

A: Since a user cannot read text in a hidden element, WebDriver will not allow access to it as well.

However, it is possible to use Javascript execution abilities to call getText directly from the element:               WebElement element = ...;     ((JavascriptExecutor) driver).executeScript("return arguments[0].getText();", element);     

### Q: How do I start Firefox with an extension installed?

A:               FirefoxProfile profile = new FirefoxProfile()     profile.addExtension(....);          WebDriver driver = new FirefoxDriver(profile);     

### Q: I’d like it if WebDriver did….

A: If there’s something that you’d like WebDriver to do, or you’ve found a bug, then please add an [add an issue](https://github.com/SeleniumHQ/selenium/issues) to the WebDriver project page.

### Q: Selenium server sometimes takes a long time to start a new session ?

A: If you’re running on linux, you will need to increase the amount of entropy available for secure random number generation. Most linux distros can install a package called “randomsound” to do this.

On Windows \(XP\), you may be running into <http://bugs.sun.com/view_bug.do?bug_id=6705872>, which usually means clearing out a lot of files from your temp directory. temp directory.

### Q: What’s the Selenium WebDriver API equivalent to **TextPresent ?**

A:               driver.findElement(By.tagName("body")).getText()     

will get you the text of the page. To verifyTextPresent/assertTextPresent, from that you can use your favourite test framework to assert on the text. To waitForTextPresent, you may want to investigate the [WebDriverWait](http://selenium.googlecode.com/svn/trunk/docs/api/java/org/openqa/selenium/support/ui/WebDriverWait.html) class.

### Q: The socket lock seems like a bad design. I can make it better

A: the socket lock that guards the starting of firefox is constructed with the following design constraints:

  * It is shared among all the language bindings; ruby, java and any of the other bindings can coexist at the same time on the same machine.   * Certain critical parts of starting firefox must be exclusive-locked on the machine in question.   * The socket lock itself is not the primary bottleneck, starting firefox is.

The SocketLock is an implementation of the Lock interface. This allows for a pluggable strategy for your own implementation of it. To switch to a different implementation, subclass the FirefoxDriver and override the “obtainLock” method.

### Q: Why do I get a UnicodeEncodeError when I send\_keys in python

A: You likely don’t have a Locale set on your system. Please set a `locale` LANG=en\_US.UTF-8 and LC\_CTYPE=“en\_US.UTF-8” for example.

# 12 - Selenium 2.0 Team

This is who you can blame for the Selenium 2 release.

\(Previously located: <https://github.com/SeleniumHQ/selenium/wiki/The-Team>\)

If you’ve ever wondered who to thank \(or blame\!\) for Selenium, then you’ve come to the right place. This page introduces you to the contributors and shows you what they’re working on.

**SimonStewart** : Original WebDriver developer and leading the Selenium 2 effort. He works mainly with Java and can be seen all over the code base, patching holes and adding features. By day he works as a Software Engineer in Test at Google. By night, he hacks on the crazy fun build grammar.

**Julian Harty** : Dabbled with `WebDriver` since 2007 mainly finding ways to make the code real and useful by testing it, and by documenting it. Currently working at eBay to find ways to make software testing more efficient and effective. He’s also involved in various [open source initiatives](http://code.google.com/u/julianharty), accessibility software, and writing material. Search for “Julian Harty” in your favorite search engine to track down his public work.

**Jari Bakken** : Has been working on WebDriver since late 2009, developed and now maintaining all things Ruby. Lead developer of [Celerity](http://github.com/jarib/celerity) and [watir-webdriver](http://github.com/jarib/watir-webdriver) and a committer on the [Watir](http://rubygems.org/gems/watir) project. Day job is as a test engineer for classified ads website [FINN.no](http://finn.no), and by night I try to make use of my degree in jazz guitar.

**David Burns** : Has been working with Selenium 1 for about 4 years and with WebDriver since the beginning of 2010 and now maintaining the .NET and Python bindings. Senior Software Engineer in Test at [Mozilla](http://www.mozilla.com) helping lead the Test Automation on Web propjects from within WebQA.

**Anthony Long** : Has been working with Selenium since 2008, and is currently working to improve the Selenium Python bindings. Anthony is the organizer of [Quality Assurance](http://meetup.com/Quality-Assurance) and author of numerous python modules for use in the Quality Assurance field. He has used selenium extensively as a QA Lead at [HUGE](http://hugeinc.com/) and most recently and currently, at [AdMeld](http://admeld.com/).

**Jim Evans** : Started working with the WebDriver and Selenium since the end of 2009, working mostly on the .NET bindings. His test automation experience includes 12 years at [Microsoft](http://www.microsoft.com/), and has worked for the past 7 years as a Senior QA Engineer at [Numara Software](http://www.numarasoftware.com/). When he’s not hacking code, he enjoys spending time with his family and performing as a singer and songwriter.