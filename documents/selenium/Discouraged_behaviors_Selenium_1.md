# Discouraged behaviors | Selenium

**URL:** https://www.selenium.dev/documentation/test_practices/discouraged/_print
**Word Count:** 1285
**Links Count:** 57
**Scraped:** 2025-07-17 06:15:56
**Status:** completed

---

This is the multi-page printable view of this section. Click here to print.

[Return to the regular view of this page](https://www.selenium.dev/documentation/test_practices/discouraged/).

# Discouraged behaviors

Things to avoid when automating browsers with Selenium.

  * 1: Captchas   * 2: File downloads   * 3: HTTP response codes   * 4: Gmail, email and Facebook logins   * 5: Test dependency   * 6: Performance testing   * 7: Link spidering   * 8: Two Factor Authentication

# 1 - Captchas

CAPTCHA, short for _Completely Automated Public Turing test to tell Computers and Humans Apart_ , is explicitly designed to prevent automation, so do not try\! There are two primary strategies to get around CAPTCHA checks:

  * Disable CAPTCHAs in your test environment   * Add a hook to allow tests to bypass the CAPTCHA

# 2 - File downloads

Whilst it is possible to start a download by clicking a link with a browser under Selenium’s control, the API does not expose download progress, making it less than ideal for testing downloaded files. This is because downloading files is not considered an important aspect of emulating user interaction with the web platform. Instead, find the link using Selenium \(and any required cookies\) and pass it to a HTTP request library like [curl](https://www.selenium.dev//curl.se/).

The [HtmlUnit driver](https://github.com/SeleniumHQ/htmlunit-driver) can download attachments by accessing them as input streams by implementing the [AttachmentHandler](https://htmlunit.sourceforge.io/apidocs/com/gargoylesoftware/htmlunit/attachment/AttachmentHandler.html) interface. The AttachmentHandler can then be added to the [HtmlUnit](https://htmlunit.sourceforge.io/) WebClient.

# 3 - HTTP response codes

For some browser configurations in Selenium RC, Selenium acted as a proxy between the browser and the site being automated. This meant that all browser traffic passed through Selenium could be captured or manipulated. The `captureNetworkTraffic()` method purported to capture all of the network traffic between the browser and the site being automated, including HTTP response codes.

Selenium WebDriver is a completely different approach to browser automation, preferring to act more like a user. This is represented in the way you write tests with WebDriver. In automated functional testing, checking the status code is not a particularly important detail of a test’s failure; the steps that preceded it are more important.

The browser will always represent the HTTP status code, imagine for example a 404 or a 500 error page. A simple way to “fail fast” when you encounter one of these error pages is to check the page title or content of a reliable point \(e.g. the `<h1>` tag\) after every page load. If you are using the page object model, you can include this check in your class constructor or similar point where the page load is expected. Occasionally, the HTTP code may even be represented in the browser’s error page and you could use WebDriver to read this and improve your debugging output.

Checking the webpage itself is in line with WebDriver’s ideal practice of representing and asserting upon the user’s view of the website.

If you insist, an advanced solution to capturing HTTP status codes is to replicate the behaviour of Selenium RC by using a proxy. WebDriver API provides the ability to set a proxy for the browser, and there are a number of proxies that will programmatically allow you to manipulate the contents of requests sent to and received from the web server. Using a proxy lets you decide how you want to respond to redirection response codes. Additionally, not every browser makes the response codes available to WebDriver, so opting to use a proxy allows you to have a solution that works for every browser.

# 4 - Gmail, email and Facebook logins

For multiple reasons, logging into sites like Gmail and Facebook using WebDriver is not recommended. Aside from being against the usage terms for these sites \(where you risk having the account shut down\), it is slow and unreliable.

The ideal practice is to use the APIs that email providers offer, or in the case of Facebook the developer tools service which exposes an API for creating test accounts, friends and so forth. Although using an API might seem like a bit of extra hard work, you will be paid back in speed, reliability, and stability. The API is also unlikely to change, whereas webpages and HTML locators change often and require you to update your test framework.

Logging in to third party sites using WebDriver at any point of your test increases the risk of your test failing because it makes your test longer. A general rule of thumb is that longer tests are more fragile and unreliable.

WebDriver implementations that are [W3C conformant](https://w3c.github.io/webdriver/webdriver-spec.html) also annotate the `navigator` object with a `WebDriver` property so that Denial of Service attacks can be mitigated.

# 5 - Test dependency

A common idea and misconception about automated testing is regarding a specific test order. Your tests should be able to run in **any** order, and not rely on other tests to complete in order to be successful.

# 6 - Performance testing

Performance testing using Selenium and WebDriver is generally not advised. Not because it is incapable, but because it is not optimised for the job and you are unlikely to get good results.

It may seem ideal to performance test in the context of the user but a suite of WebDriver tests are subjected to many points of external and internal fragility which are beyond your control; for example browser startup speed, speed of HTTP servers, response of third party servers that host JavaScript or CSS, and the instrumentation penalty of the WebDriver implementation itself. Variation at these points will cause variation in your results. It is difficult to separate the difference between the performance of your website and the performance of external resources, and it is also hard to tell what the performance penalty is for using WebDriver in the browser, especially if you are injecting scripts.

The other potential attraction is “saving time” — carrying out functional and performance tests at the same time. However, functional and performance tests have opposing objectives. To test functionality, a tester may need to be patient and wait for loading, but this will cloud the performance testing results and vice versa.

To improve the performance of your website, you will need to be able to analyse overall performance independent of environment differences, identify poor code practices, breakdown of performance of individual resources \(i.e. CSS or JavaScript\), in order to know what to improve. There are performance testing tools available that can do this job already, that provide reporting and analysis, and can even make improvement suggestions.

Example \(open source\) packages to use are: [JMeter](https://www.selenium.dev/)

# 7 - Link spidering

Using WebDriver to spider through links is not a recommended practice. Not because it cannot be done, but because WebDriver is definitely not the most ideal tool for this. WebDriver needs time to start up, and can take several seconds, up to a minute depending on how your test is written, just to get to the page and traverse through the DOM.

Instead of using WebDriver for this, you could save a ton of time by executing a [curl](https://curl.se/) command, or using a library such as BeautifulSoup since these methods do not rely on creating a browser and navigating to a page. You are saving tonnes of time by not using WebDriver for this task.

# 8 - Two Factor Authentication

Two Factor Authentication \(2FA\) is an authorization mechanism where a One Time Password \(OTP\) is generated using “Authenticator” mobile apps such as “Google Authenticator”, “Microsoft Authenticator” etc., or by SMS, e-mail to authenticate. Automating this seamlessly and consistently is a big challenge in Selenium. There are some ways to automate this process. But that will be another layer on top of our Selenium tests and not as secure. So, you should avoid automating 2FA.

There are few options to get around 2FA checks:

  * If you want the functionality to still be tested, one option is to ask your team to create a “special token” that will work in test environment. That won’t require usage of a mobile device, and will ensure the test journey is covered.   * Disable 2FA for certain Users in the test environment, so that you can use those user credentials in the automation.   * Disable 2FA in your test environment.   * Disable 2FA if you login from certain IPs. That way we can configure our test machine IPs to avoid this.