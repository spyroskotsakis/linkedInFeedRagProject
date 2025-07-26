# Understanding Common Errors | Selenium

**URL:** https://www.selenium.dev/documentation/webdriver/troubleshooting/errors/_print
**Word Count:** 1823
**Links Count:** 69
**Scraped:** 2025-07-17 06:17:48
**Status:** completed

---

This is the multi-page printable view of this section. Click here to print.

[Return to the regular view of this page](https://www.selenium.dev/documentation/webdriver/troubleshooting/errors/).

# Understanding Common Errors

How to solve various problems in your Selenium code.

  * 1: Unable to Locate Driver Error

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

# 1 - Unable to Locate Driver Error

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