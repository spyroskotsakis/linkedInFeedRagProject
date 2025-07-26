# Legacy Selenium Desired Capabilities | Selenium

**URL:** https://www.selenium.dev/documentation/legacy/desired_capabilities
**Word Count:** 416
**Links Count:** 209
**Scraped:** 2025-07-17 06:15:03
**Status:** completed

---

# Legacy Selenium Desired Capabilities

These capabilities worked with the legacy JSON Wire Protocol

This documentation previously located [on the wiki](https://github.com/SeleniumHQ/selenium/wiki/DesiredCapabilities)   See [JSON Wire Protocol](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#capabilities-json-object) for common capabilities.

## Remote Driver Specific

**Key**| **Type**| **Description**|  webdriver.remote.sessionid| string| WebDriver session ID for the session. Readonly and only returned if the server implements a server-side webdriver-backed selenium.   ---|---|---   webdriver.remote.quietExceptions| boolean| Disable automatic screnshot capture on exceptions. This is False by default.      ## Grid Specific

**Key**| **Type**| **Description**|  path| string| Path to route request to, or maybe listen on.   ---|---|---   seleniumProtocol| string| Which protocol to use. Accepted values: WebDriver, Selenium.   maxInstances| integer| Maximum number of instances to allow to connect to grid   environment| string| Possible duplicate of browserName? See RegistrationRequest      ## Selenium RC Specific

Key| Type| Description   ---|---|---   proxy\_pac| boolean| Legacy proxy mechanism. Do not use.   commandLineFlags| string| Flags to pass to browser command line.   executablePath| string| Path to browser executable.   timeoutInSeconds| long integer| Timeout to wait for the browser to launch, in seconds.   onlyProxySeleniumTraffic| boolean| Whether to only proxy selenium traffic. See browserlaunchers.Proxies   avoidProxy| boolean| ??? See browserlaunchers.Proxies   proxyEverything| boolean| ??? See browserlaunchers.Proxies   proxyRequired| boolean| ??? See browserlaunchers.Proxies   browserSideLog| boolean| ??? See AbstractBrowserLauncher.   optionsSet| boolean| ??? See BrowserOptions.   singleWindow| boolean| Whether to enable single window mode.   dontInjectRegex| javascript RegExp| Regular expression that proxy injection mode can use to know when to bypss injection. Ignored if not in proxy injection mode.   userJSInjection| boolean| ??? Whether to inject user JS. Ignored if not in proxy injection mode.   userExtensions| string| Path to a JavaScript file that will be loaded into selenium.      ## Selenese-Backed-WebDriver specific

Key| Type| Description   ---|---|---   selenium.server.url| string| URL of Selenium server to use, to back this WebDriver      ## Firefox specific

Key| Type| Description   ---|---|---   captureNetworkTraffic| boolean| Whether to capture network traffic.   addCustomRequestHeaders| boolean| Whether to add custom request headers.   trustAllSSLCertificates| boolean| Whether to trust all SSL certificates.   changeMaxConnections| boolean| ??? See FirefoxChromeLauncher.   firefoxProfileTemplate| string| ??? See FirefoxChromeLauncher.   profile| string| ??? See FirefoxChromeLauncher      ### FirefoxProfile settings

Preferences accepted by the FirefoxProfile with special meaning, in the WebDriver API:

**Key**| **Type**| **Description**   ---|---|---   webdriver\_accept\_untrusted\_certs| boolean| Whether to trust all SSL certificates. TODO: Maybe in some way different to the acceptSslCerts or trustAllSSLCertificates capabilities.   webdriver\_assume\_untrusted\_issuer| boolean| Whether to trust all SSL certificate issuers. TODO: Maybe in some way different to the acceptSslCerts or trustAllSSLCertificates capabilities.   webdriver.log.driver| string| Level at which to log FirefoxDriver logging statements to a temporary file, so that they can be retrieved by a getLogs command. Available options; DEBUG, INFO, WARNING, ERROR, OFF. Defaults to OFF.   webdriver.log.file| string| Path to file to which to copy firefoxdriver logging output. Defaults to no file \(like /dev/null\).   webdriver.load.strategy| string| Experimental API. Defines different strategies for how long to wait until a page is loaded. Values: unstable, conservative. Defaults to conservative.   webdriver\_firefox\_port| integer| Port to listen on for WebDriver commands. Defaults to 7055.      ## IE specific

Key| Type| Description   ---|---|---   killProcessesByName| boolean| Whether to try to kill processes by name, instead \(or addition\) to killing processes we happen to have handles to.   honorSystemProxy| boolean| Whether to honor the system proxy.   ensureCleanSession| boolean| Whether to make sure the session has no cookies or temporary internet files on Windows. I believe this is passed to the IEDriver as well, but ignored by it.      ## Safari specific

Key| Type| Description   ---|---|---   honorSystemProxy| boolean| Whether to honour the sysem proxy.   ensureCleanSession| boolean| Whether to make sure the session has no cookies, cache entries. And that any registry and proxy settings are restored after the session.      Last modified January 10, 2022: [More wiki \(\#907\) \[deploy site\] \(adcf706a1ad\)](https://github.com/SeleniumHQ/seleniumhq.github.io/commit/adcf706a1ad907d028dc57d10201a265972432af)