# BiDirectional functionality | Selenium

**URL:** https://www.selenium.dev/documentation/webdriver/bidi
**Word Count:** 413
**Links Count:** 205
**Scraped:** 2025-07-17 06:15:56
**Status:** completed

---

# BiDirectional functionality

BiDirectional means that communication is happening in two directions simultaneously. The traditional WebDriver model involves strict request/response commands which only allows for communication to happen in one direction at any given time. In most cases this is what you want; it ensures that the browser is doing the expected things in the right order, but there are a number of interesting things that can be done with asynchronous interactions.

This functionality is currently available in a limited fashion with the \[Chrome DevTools Protocol\] \(CDP\), but to address some of its drawbacks, the Selenium team, along with the major browser vendors, have worked to create the new [WebDriver BiDi Protocol](https://w3c.github.io/webdriver-bidi/). This specification aims to create a stable, cross-browser API that leverages bidirectional communication for enhanced browser automation and testing functionality, including streaming events from the user agent to the controlling software via WebSockets. Users will be able to listen for and record or manipulate events as they happen during the course of a Selenium session.

### Enabling BiDi in Selenium

In order to use WebDriver BiDi, setting the capability in the browser options will enable the required functionality:

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

              options.setCapability("webSocketUrl", true);               options.enable_bidi = True               UseWebSocketUrl = true,               options.web_socket_url = true               Options().enableBidi();               options.setCapability("webSocketUrl", true);

This enables the WebSocket connection for bidirectional communication, unlocking the full potential of the WebDriver BiDi protocol.

Note that Selenium is updating its entire implementation from WebDriver Classic to WebDriver BiDi \(while maintaining backwards compatibility as much as possible\), but this section of documentation focuses on the new functionality that bidirectional communication allows. The low-level BiDi domains will be accessible in the code to the end user, but the goal is to provide high-level APIs that are straightforward methods of real-world use cases. As such, the low-level components will not be documented, and this section will focus only on the user-friendly features that we encourage users to take advantage of.

If there is additional functionality you’d like to see, please raise a [feature request](https://github.com/SeleniumHQ/selenium/issues/new?assignees=&labels=&template=feature.md).

* * *

##### [WebDriver BiDi Logging Features](https://www.selenium.dev/documentation/webdriver/bidi/logging/)

These features are related to logging. Because “logging” can refer to so many different things, these methods are made available via a “script” namespace.

##### [WebDriver BiDi Network Features](https://www.selenium.dev/documentation/webdriver/bidi/network/)

These features are related to networking, and are made available via a “network” namespace.

##### [WebDriver BiDi Script Features](https://www.selenium.dev/documentation/webdriver/bidi/script/)

These features are related to scripts, and are made available via a “script” namespace.

##### [Chrome DevTools Protocol](https://www.selenium.dev/documentation/webdriver/bidi/cdp/)

Examples of working with Chrome DevTools Protocol in Selenium. CDP support is temporary until WebDriver BiDi has been implemented.

##### [BiDirectional API \(W3C compliant\)](https://www.selenium.dev/documentation/webdriver/bidi/w3c/)

Examples of working with Chrome DevTools Protocol in Selenium. CDP support is temporary until WebDriver BiDi has been implemented.

Last modified September 26, 2024: [added python example for enabling BiDi \(\#1965\) \(cb40aec6caf\)](https://github.com/SeleniumHQ/seleniumhq.github.io/commit/cb40aec6caf8fa666077e3e047f6c2d1a194df83)