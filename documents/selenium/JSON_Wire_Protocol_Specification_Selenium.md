# JSON Wire Protocol Specification | Selenium

**URL:** https://www.selenium.dev/documentation/legacy/json_wire_protocol
**Word Count:** 8509
**Links Count:** 351
**Scraped:** 2025-07-17 06:13:36
**Status:** completed

---

# JSON Wire Protocol Specification

The endpoints and payloads for the now-obsolete open source protocol that was the precursor to the [W3C specification](https://w3c.github.io/webdriver/).

This documentation previously located [on the wiki](https://github.com/SeleniumHQ/selenium/wiki/JsonWireProtocol)

All implementations of WebDriver that communicate with the browser, or a RemoteWebDriver server shall use a common wire protocol. This wire protocol defines a [RESTful web service](http://www.google.com?q=RESTful+web+service) using [JSON](http://www.json.org) over HTTP.

The protocol will assume that the WebDriver API has been “flattened”, but there is an expectation that client implementations will take a more Object-Oriented approach, as demonstrated in the existing Java API. The wire protocol is implemented in request/response pairs of “commands” and “responses”.

## Terms and Concepts

### Client

The machine on which the WebDriver API is being used.     

### Session

The machine running the RemoteWebDriver. This term may also refer to a specific browser that implements the wire protocol directly, such as the FirefoxDriver or IPhoneDriver.     

The server should maintain one browser per session. Commands sent to a session will be directed to the corresponding browser.     

### WebElement

An object in the WebDriver API that represents a DOM element on the page.     

### WebElement JSON Object

The JSON representation of a WebElement for transmission over the wire. This object will have the following properties:     

**Key**| **Type**| **Description**   ---|---|---   ELEMENT| string| The opaque ID assigned to the element by the server. This ID should be used in all subsequent commands issued against the element.      ### Capabilities JSON Object

Not all server implementations will support every WebDriver feature. Therefore, the client and server should use JSON objects with the properties listed below when describing which features a session supports.     

**Key**| **Type**| **Description**|  browserName| string| The name of the browser being used; should be one of `{android, chrome, firefox, htmlunit, internet explorer, iPhone, iPad, opera, safari}`.   ---|---|---   version| string| The browser version, or the empty string if unknown.   platform| string| A key specifying which platform the browser is running on. This value should be one of `{WINDOWS|XP|VISTA|MAC|LINUX|UNIX}`. When requesting a new session, the client may specify `ANY` to indicate any available platform may be used.   javascriptEnabled| boolean| Whether the session supports executing user supplied JavaScript in the context of the current page.   takesScreenshot| boolean| Whether the session supports taking screenshots of the current page.   handlesAlerts| boolean| Whether the session can interact with modal popups, such as `window.alert` and `window.confirm`.   databaseEnabled| boolean| Whether the session can interact database storage.   locationContextEnabled| boolean| Whether the session can set and query the browser's location context.   applicationCacheEnabled| boolean| Whether the session can interact with the application cache.   browserConnectionEnabled| boolean| Whether the session can query for the browser's connectivity and disable it if desired.   cssSelectorsEnabled| boolean| Whether the session supports CSS selectors when searching for elements.   webStorageEnabled| boolean| Whether the session supports interactions with [storage objects](http://www.w3.org/TR/2009/WD-webstorage-20091029/).   rotatable| boolean| Whether the session can rotate the current page's current layout between portrait and landscape orientations \(only applies to mobile platforms\).   acceptSslCerts| boolean| Whether the session should accept all SSL certs by default.   nativeEvents| boolean| Whether the session is capable of generating native events when simulating user input.   proxy| proxy object| Details of any proxy to use. If no proxy is specified, whatever the system's current or default state is used. The format is specified under Proxy JSON Object.   unexpectedAlertBehaviour| string| What the browser should do with an unhandled alert before throwing out the UnhandledAlertException. Possible values are "accept", "dismiss" and "ignore"   elementScrollBehavior| integer| Allows the user to specify whether elements are scrolled into the viewport for interaction to align with the top \(0\) or bottom \(1\) of the viewport. The default value is to align with the top of the viewport. Supported in IE and Firefox \(since 2.36\)      ### Desired Capabilities

A Capabilities JSON Object sent by the client describing the capabilities a new session created by the server should possess. Any omitted keys implicitly indicate the corresponding capability is irrelevant. More at [DesiredCapabilities](https://www.selenium.dev/documentation/legacy/DesiredCapabilities.md).     

### Actual Capabilities

A Capabilities JSON Object returned by the server describing what features a session actually supports. Any omitted keys implicitly indicate the corresponding capability is not supported.     

### Cookie JSON Object

A JSON object describing a Cookie.     

**Key**| **Type**| **Description**|  name| string| The name of the cookie.   ---|---|---   value| string| The cookie value.   path| string| \(Optional\) The cookie path.1   domain| string| \(Optional\) The domain the cookie is visible to.1   secure| boolean| \(Optional\) Whether the cookie is a secure cookie.1   httpOnly| boolean| \(Optional\) Whether the cookie is an httpOnly cookie.1   expiry| number| \(Optional\) When the cookie expires, specified in seconds since midnight, January 1, 1970 UTC.1      1 When returning Cookie objects, the server should only omit an optional field if it is incapable of providing the information.     

### Log Entry JSON Object

A JSON object describing a log entry.     

**Key**| **Type**| **Description**|  timestamp| number| The timestamp of the entry.   ---|---|---   level| string| The log level of the entry, for example, "INFO" \(see log levels\).   message| string| The log message.      ### Log Levels

Log levels in order, with finest level on top and coarsest level at the bottom.     

**Level**| **Description**|  ALL| All log messages. Used for fetching of logs and configuration of logging.   ---|---   DEBUG| Messages for debugging.   INFO| Messages with user information.   WARNING| Messages corresponding to non-critical problems.   SEVERE| Messages corresponding to critical errors.   OFF| No log messages. Used for configuration of logging.      ### Log Type

The table below lists common log types. Other log types, for instance, for performance logging may also be available.     

**Log Type**| **Description**|  client| Logs from the client.   ---|---   driver| Logs from the webdriver.   browser| Logs from the browser.   server| Logs from the server.      ### Proxy JSON Object

A JSON object describing a Proxy configuration.     

**Key**| **Type**| **Description**|  proxyType| string| \(Required\) The type of proxy being used. Possible values are: **direct** \- A direct connection - no proxy in use, **manual** \- Manual proxy settings configured, e.g. setting a proxy for HTTP, a proxy for FTP, etc, **pac** \- Proxy autoconfiguration from a URL, **autodetect** \- Proxy autodetection, probably with WPAD, **system** \- Use system settings   ---|---|---   proxyAutoconfigUrl| string| \(Required if proxyType == **pac** , Ignored otherwise\) Specifies the URL to be used for proxy autoconfiguration. Expected format example: <http://hostname.com:1234/pacfile>   ftpProxy, httpProxy, sslProxy, socksProxy| string| \(Optional, Ignored if proxyType \!= **manual**\) Specifies the proxies to be used for FTP, HTTP, HTTPS and SOCKS requests respectively. Behaviour is undefined if a request is made, where the proxy for the particular protocol is undefined, if proxyType is **manual**. Expected format example: hostname.com:1234   socksUsername| string| \(Optional, Ignored if proxyType \!= **manual** and socksProxy is not set\) Specifies SOCKS proxy username.   socksPassword| string| \(Optional, Ignored if proxyType \!= **manual** and socksProxy is not set\) Specifies SOCKS proxy password.   noProxy| string| \(Optional, Ignored if proxyType \!= **manual**\) Specifies proxy bypass addresses. Format is driver specific.      ## Messages

### Commands

WebDriver command messages should conform to the [HTTP/1.1 request specification](http://www.w3.org/Protocols/rfc2616/rfc2616-sec5.html#sec5). Although the server may be extended to respond to other content-types, the wire protocol dictates that all commands accept a content-type of `application/json;charset=UTF-8`. Likewise, the message bodies for POST and PUT request must use an `application/json;charset=UTF-8` content-type.

Each command in the WebDriver service will be mapped to an HTTP method at a specific path. Path segments prefixed with a colon \(:\) indicate that segment is a variable used to further identify the underlying resource. For example, consider an arbitrary resource mapped as:               GET /favorite/color/:name     

Given this mapping, the server should respond to GET requests sent to “/favorite/color/Jack” and “/favorite/color/Jill”, with the variable `:name` set to “Jack” and “Jill”, respectively.

### Responses

Command responses shall be sent as [HTTP/1.1 response messages](http://www.w3.org/Protocols/rfc2616/rfc2616-sec6.html#sec6). If the remote server must return a 4xx response, the response body shall have a Content-Type of text/plain and the message body shall be a descriptive message of the bad request. For all other cases, if a response includes a message body, it must have a Content-Type of application/json;charset=UTF-8 and will be a JSON object with the following properties:

**Key**| **Type**| **Description**   ---|---|---   sessionId| string| null   status| number| A status code summarizing the result of the command. A non-zero value indicates that the command failed.   value| `*`| The response JSON value.      #### Response Status Codes

The wire protocol will inherit its status codes from those used by the InternetExplorerDriver:

**Code**| **Summary**| **Detail**   ---|---|---   0| `Success`| The command executed successfully.   6| `NoSuchDriver`| A session is either terminated or not started   7| `NoSuchElement`| An element could not be located on the page using the given search parameters.   8| `NoSuchFrame`| A request to switch to a frame could not be satisfied because the frame could not be found.   9| `UnknownCommand`| The requested resource could not be found, or a request was received using an HTTP method that is not supported by the mapped resource.   10| `StaleElementReference`| An element command failed because the referenced element is no longer attached to the DOM.   11| `ElementNotVisible`| An element command could not be completed because the element is not visible on the page.   12| `InvalidElementState`| An element command could not be completed because the element is in an invalid state \(e.g. attempting to click a disabled element\).   13| `UnknownError`| An unknown server-side error occurred while processing the command.   15| `ElementIsNotSelectable`| An attempt was made to select an element that cannot be selected.   17| `JavaScriptError`| An error occurred while executing user supplied JavaScript.   19| `XPathLookupError`| An error occurred while searching for an element by XPath.   21| `Timeout`| An operation did not complete before its timeout expired.   23| `NoSuchWindow`| A request to switch to a different window could not be satisfied because the window could not be found.   24| `InvalidCookieDomain`| An illegal attempt was made to set a cookie under a different domain than the current page.   25| `UnableToSetCookie`| A request to set a cookie’s value could not be satisfied.   26| `UnexpectedAlertOpen`| A modal dialog was open, blocking this operation   27| `NoAlertOpenError`| An attempt was made to operate on a modal dialog when one was not open.   28| `ScriptTimeout`| A script did not complete before its timeout expired.   29| `InvalidElementCoordinates`| The coordinates provided to an interactions operation are invalid.   30| `IMENotAvailable`| IME was not available.   31| `IMEEngineActivationFailed`| An IME engine could not be started.   32| `InvalidSelector`| Argument was an invalid selector \(e.g. XPath/CSS\).   33| `SessionNotCreatedException`| A new session could not be created.   34| `MoveTargetOutOfBounds`| Target provided for a move action is out of bounds.      The client should interpret a 404 Not Found response from the server as an “Unknown command” response. All other 4xx and 5xx responses from the server that do not define a status field should be interpreted as “Unknown error” responses.

### Error Handling

There are two levels of error handling specified by the wire protocol: invalid requests and failed commands.

#### Invalid Requests

All invalid requests should result in the server returning a 4xx HTTP response. The response Content-Type should be set to text/plain and the message body should be a descriptive error message. The categories of invalid requests are as follows:

**Unknown Commands**      If the server receives a command request whose path is not mapped to a resource in the REST service, it should respond with a `404 Not Found` message.     

**Unimplemented Commands**      Every server implementing the WebDriver wire protocol must respond to every defined command. If an individual command has not been implemented on the server, the server should respond with a `501 Not Implemented` error message. Note this is the only error in the Invalid Request category that does not return a `4xx` status code.     

**Variable Resource Not Found**      If a request path maps to a variable resource, but that resource does not exist, then the server should respond with a `404 Not Found`. For example, if ID `my-session` is not a valid session ID on the server, and a command is sent to `GET /session/my-session HTTP/1.1`, then the server should gracefully return a `404`.     

**Invalid Command Method**      If a request path maps to a valid resource, but that resource does not respond to the request method, the server should respond with a `405 Method Not Allowed`. The response must include an Allows header with a list of the allowed methods for the requested resource.     

**Missing Command Parameters**      If a POST/PUT command maps to a resource that expects a set of JSON parameters, and the response body does not include one of those parameters, the server should respond with a `400 Bad Request`. The response body should list the missing parameters.     

#### Failed Commands

If a request maps to a valid command and contains all of the expected parameters in the request body, yet fails to execute successfully, then the server should send a 500 Internal Server Error. This response should have a Content-Type of `application/json;charset=UTF-8` and the response body should be a well formed JSON response object.

The response status should be one of the defined status codes and the response value should be another JSON object with detailed information for the failing command:

Key| Type| Description   ---|---|---   message| string| A descriptive message for the command failure.   screen| string| \(Optional\) If included, a screenshot of the current page as a base64 encoded string.   class| string| \(Optional\) If included, specifies the fully qualified class name for the exception that was thrown when the command failed.   stackTrace| array| \(Optional\) If included, specifies an array of JSON objects describing the stack trace for the exception that was thrown when the command failed. The zeroeth element of the array represents the top of the stack.      Each JSON object in the stackTrace array must contain the following properties:

**Key**| **Type**| **Description**   ---|---|---   fileName| string| The name of the source file containing the line represented by this frame.   className| string| The fully qualified class name for the class active in this frame. If the class name cannot be determined, or is not applicable for the language the server is implemented in, then this property should be set to the empty string.   methodName| string| The name of the method active in this frame, or the empty string if unknown/not applicable.   lineNumber| number| The line number in the original source file for the frame, or 0 if unknown.      ## Resource Mapping

Resources in the WebDriver REST service are mapped to individual URL patterns. Each resource may respond to one or more HTTP request methods. If a resource responds to a GET request, then it should also respond to HEAD requests. All resources should respond to OPTIONS requests with an `Allow` header field, whose value is a list of all methods that resource responds to.

If a resource is mapped to a URL containing a variable path segment name, that path segment should be used to further route the request. Variable path segments are indicated in the resource mapping by a colon-prefix. For example, consider the following:               /favorite/color/:person     

A resource mapped to this URL should parse the value of the `:person` path segment to further determine how to respond to the request. If this resource received a request for `/favorite/color/Jack`, then it should return Jack’s favorite color. Likewise, the server should return Jill’s favorite color for any requests to `/favorite/color/Jill`.

Two resources may only be mapped to the same URL pattern if one of those resources’ patterns contains variable path segments, and the other does not. In these cases, the server should always route requests to the resource whose path is the best match for the request. Consider the following two resource paths:

  1. `/session/:sessionId/element/active`   2. `/session/:sessionId/element/:id`

Given these mappings, the server should always route requests whose final path segment is active to the first resource. All other requests should be routed to second.

## Command Reference

### Command Summary

**HTTP Method**| **Path**| **Summary**   ---|---|---   GET| [/status](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#status)| Query the server’s current status.   POST| [/session](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#session)| Create a new session.   GET| [/sessions](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessions)| Returns a list of the currently active sessions.   GET| [/session/:sessionId](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionid)| Retrieve the capabilities of the specified session.   DELETE| [/session/:sessionId](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionid)| Delete the session.   POST| [/session/:sessionId/timeouts](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidtimeouts)| Configure the amount of time that a particular type of operation can execute for before they are aborted and a   POST| [/session/:sessionId/timeouts/async\_script](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidtimeoutsasync_script)| Set the amount of time, in milliseconds, that asynchronous scripts executed by `/session/:sessionId/execute_async` are permitted to run before they are aborted and a   POST| [/session/:sessionId/timeouts/implicit\_wait](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidtimeoutsimplicit_wait)| Set the amount of time the driver should wait when searching for elements.   GET| [/session/:sessionId/window\_handle](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidwindow_handle)| Retrieve the current window handle.   GET| [/session/:sessionId/window\_handles](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidwindow_handles)| Retrieve the list of all window handles available to the session.   GET| [/session/:sessionId/url](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidurl)| Retrieve the URL of the current page.   POST| [/session/:sessionId/url](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidurl)| Navigate to a new URL.   POST| [/session/:sessionId/forward](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidforward)| Navigate forwards in the browser history, if possible.   POST| [/session/:sessionId/back](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidback)| Navigate backwards in the browser history, if possible.   POST| [/session/:sessionId/refresh](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidrefresh)| Refresh the current page.   POST| [/session/:sessionId/execute](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidexecute)| Inject a snippet of JavaScript into the page for execution in the context of the currently selected frame.   POST| [/session/:sessionId/execute\_async](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidexecute_async)| Inject a snippet of JavaScript into the page for execution in the context of the currently selected frame.   GET| [/session/:sessionId/screenshot](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidscreenshot)| Take a screenshot of the current page.   GET| [/session/:sessionId/ime/available\_engines](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidimeavailable_engines)| List all available engines on the machine.   GET| [/session/:sessionId/ime/active\_engine](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidimeactive_engine)| Get the name of the active IME engine.   GET| [/session/:sessionId/ime/activated](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidimeactivated)| Indicates whether IME input is active at the moment \(not if it’s available.   POST| [/session/:sessionId/ime/deactivate](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidimedeactivate)| De-activates the currently-active IME engine.   POST| [/session/:sessionId/ime/activate](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidimeactivate)| Make an engines that is available \(appears on the listreturned by getAvailableEngines\) active.   POST| [/session/:sessionId/frame](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidframe)| Change focus to another frame on the page.   POST| [/session/:sessionId/frame/parent](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidframeparent)| Change focus to the parent context.   POST| [/session/:sessionId/window](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidwindow)| Change focus to another window.   DELETE| [/session/:sessionId/window](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidwindow)| Close the current window.   POST| [/session/:sessionId/window/:windowHandle/size](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidwindowwindowhandlesize)| Change the size of the specified window.   GET| [/session/:sessionId/window/:windowHandle/size](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidwindowwindowhandlesize)| Get the size of the specified window.   POST| [/session/:sessionId/window/:windowHandle/position](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidwindowwindowhandleposition)| Change the position of the specified window.   GET| [/session/:sessionId/window/:windowHandle/position](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidwindowwindowhandleposition)| Get the position of the specified window.   POST| [/session/:sessionId/window/:windowHandle/maximize](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidwindowwindowhandlemaximize)| Maximize the specified window if not already maximized.   GET| [/session/:sessionId/cookie](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidcookie)| Retrieve all cookies visible to the current page.   POST| [/session/:sessionId/cookie](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidcookie)| Set a cookie.   DELETE| [/session/:sessionId/cookie](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidcookie)| Delete all cookies visible to the current page.   DELETE| [/session/:sessionId/cookie/:name](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidcookiename)| Delete the cookie with the given name.   GET| [/session/:sessionId/source](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidsource)| Get the current page source.   GET| [/session/:sessionId/title](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidtitle)| Get the current page title.   POST| [/session/:sessionId/element](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidelement)| Search for an element on the page, starting from the document root.   POST| [/session/:sessionId/elements](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidelements)| Search for multiple elements on the page, starting from the document root.   POST| [/session/:sessionId/element/active](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidelementactive)| Get the element on the page that currently has focus.   GET| [/session/:sessionId/element/:id](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidelementid)| Describe the identified element.   POST| [/session/:sessionId/element/:id/element](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidelementidelement)| Search for an element on the page, starting from the identified element.   POST| [/session/:sessionId/element/:id/elements](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidelementidelements)| Search for multiple elements on the page, starting from the identified element.   POST| [/session/:sessionId/element/:id/click](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidelementidclick)| Click on an element.   POST| [/session/:sessionId/element/:id/submit](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidelementidsubmit)| Submit a `FORM` element.   GET| [/session/:sessionId/element/:id/text](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidelementidtext)| Returns the visible text for the element.   POST| [/session/:sessionId/element/:id/value](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidelementidvalue)| Send a sequence of key strokes to an element.   POST| [/session/:sessionId/keys](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidkeys)| Send a sequence of key strokes to the active element.   GET| [/session/:sessionId/element/:id/name](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidelementidname)| Query for an element’s tag name.   POST| [/session/:sessionId/element/:id/clear](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidelementidclear)| Clear a `TEXTAREA` or `text INPUT` element’s value.   GET| [/session/:sessionId/element/:id/selected](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidelementidselected)| Determine if an `OPTION` element, or an `INPUT` element of type `checkbox` or `radiobutton` is currently selected.   GET| [/session/:sessionId/element/:id/enabled](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidelementidenabled)| Determine if an element is currently enabled.   GET| [/session/:sessionId/element/:id/attribute/:name](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidelementidattribute/:name)| Get the value of an element’s attribute.   GET| [/session/:sessionId/element/:id/equals/:other](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidelementidequals/:other)| Test if two element IDs refer to the same DOM element.   GET| [/session/:sessionId/element/:id/displayed](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidelementiddisplayed)| Determine if an element is currently displayed.   GET| [/session/:sessionId/element/:id/location](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidelementidlocation)| Determine an element’s location on the page.   GET| [/session/:sessionId/element/:id/location\_in\_view](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidelementidlocation_in_view)| Determine an element’s location on the screen once it has been scrolled into view.   GET| [/session/:sessionId/element/:id/size](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidelementidsize)| Determine an element’s size in pixels.   GET| [/session/:sessionId/element/:id/css/:propertyName](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidelementidcss/:propertyName)| Query the value of an element’s computed CSS property.   GET| [/session/:sessionId/orientation](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidorientation)| Get the current browser orientation.   POST| [/session/:sessionId/orientation](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidorientation)| Set the browser orientation.   GET| [/session/:sessionId/alert\_text](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidalert_text)| Gets the text of the currently displayed JavaScript `alert()`, `confirm()`, or `prompt()` dialog.   POST| [/session/:sessionId/alert\_text](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidalert_text)| Sends keystrokes to a JavaScript `prompt()` dialog.   POST| [/session/:sessionId/accept\_alert](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidaccept_alert)| Accepts the currently displayed alert dialog.   POST| [/session/:sessionId/dismiss\_alert](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessioniddismiss_alert)| Dismisses the currently displayed alert dialog.   POST| [/session/:sessionId/moveto](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidmoveto)| Move the mouse by an offset of the specificed element.   POST| [/session/:sessionId/click](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidclick)| Click any mouse button \(at the coordinates set by the last moveto command\).   POST| [/session/:sessionId/buttondown](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidbuttondown)| Click and hold the left mouse button \(at the coordinates set by the last moveto command\).   POST| [/session/:sessionId/buttonup](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidbuttonup)| Releases the mouse button previously held \(where the mouse is currently at\).   POST| [/session/:sessionId/doubleclick](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessioniddoubleclick)| Double-clicks at the current mouse coordinates \(set by moveto\).   POST| [/session/:sessionId/touch/click](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidtouchclick)| Single tap on the touch enabled device.   POST| [/session/:sessionId/touch/down](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidtouchdown)| Finger down on the screen.   POST| [/session/:sessionId/touch/up](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidtouchup)| Finger up on the screen.   POST| [session/:sessionId/touch/move](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidtouchmove)| Finger move on the screen.   POST| [session/:sessionId/touch/scroll](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidtouchscroll)| Scroll on the touch screen using finger based motion events.   POST| [session/:sessionId/touch/scroll](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidtouchscroll)| Scroll on the touch screen using finger based motion events.   POST| [session/:sessionId/touch/doubleclick](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidtouchdoubleclick)| Double tap on the touch screen using finger motion events.   POST| [session/:sessionId/touch/longclick](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidtouchlongclick)| Long press on the touch screen using finger motion events.   POST| [session/:sessionId/touch/flick](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidtouchflick)| Flick on the touch screen using finger motion events.   POST| [session/:sessionId/touch/flick](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidtouchflick)| Flick on the touch screen using finger motion events.   GET| [/session/:sessionId/location](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidlocation)| Get the current geo location.   POST| [/session/:sessionId/location](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidlocation)| Set the current geo location.   GET| [/session/:sessionId/local\_storage](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidlocal_storage)| Get all keys of the storage.   POST| [/session/:sessionId/local\_storage](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidlocal_storage)| Set the storage item for the given key.   DELETE| [/session/:sessionId/local\_storage](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidlocal_storage)| Clear the storage.   GET| [/session/:sessionId/local\_storage/key/:key](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidlocal_storagekeykey)| Get the storage item for the given key.   DELETE| [/session/:sessionId/local\_storage/key/:key](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidlocal_storagekeykey)| Remove the storage item for the given key.   GET| [/session/:sessionId/local\_storage/size](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidlocal_storagesize)| Get the number of items in the storage.   GET| [/session/:sessionId/session\_storage](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidsession_storage)| Get all keys of the storage.   POST| [/session/:sessionId/session\_storage](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidsession_storage)| Set the storage item for the given key.   DELETE| [/session/:sessionId/session\_storage](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidsession_storage)| Clear the storage.   GET| [/session/:sessionId/session\_storage/key/:key](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidsession_storagekeykey)| Get the storage item for the given key.   DELETE| [/session/:sessionId/session\_storage/key/:key](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidsession_storagekeykey)| Remove the storage item for the given key.   GET| [/session/:sessionId/session\_storage/size](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidsession_storagesize)| Get the number of items in the storage.   POST| [/session/:sessionId/log](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidlog)| Get the log for a given log type.   GET| [/session/:sessionId/log/types](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidlogtypes)| Get available log types.   GET| [/session/:sessionId/application\_cache/status](https://www.selenium.dev/documentation/legacy/json_wire_protocol/#sessionsessionidapplication_cachestatus)| Get the status of the html5 application cache.      ### Command Detail

#### /status

    

#### GET /status

    

    Query the server's current status. The server should respond with a general "HTTP 200 OK" response if it is alive and accepting commands. The response body should be a JSON object describing the state of the server. All server implementations should return two basic objects describing the server's current platform and when the server was built. All fields are optional; if omitted, the client should assume the value is uknown. Furthermore, server implementations may include additional fields not listed here.      **Key**| **Type**| **Description**|  build| object|    ---|---|---   build.version| string| A generic release label \(i.e. "2.0rc3"\)   build.revision| string| The revision of the local source control client from which the server was built   build.time| string| A timestamp from when the server was built.   os| object|    os.arch| string| The current system architecture.   os.name| string| The name of the operating system the server is currently running on: "windows", "linux", etc.   os.version| string| The operating system version.       

**Returns:**     `{object}` An object describing the general status of the server.

* * *

#### /session

    

#### POST /session

    

    Create a new session. The server should attempt to create a session that most closely matches the desired and required capabilities. Required capabilities have higher priority than desired capabilities and must be set for the session to be created.     

**JSON Parameters:**     `desiredCapabilities` \- `{object}` An object describing the session's desired capabilities.     `requiredCapabilities` \- `{object}` An object describing the session's required capabilities \(Optional\).     

**Returns:**     `{object}` An object describing the session's capabilities.     

**Potential Errors:**     `SessionNotCreatedException` \- If a required capability could not be set.

* * *

#### /sessions

    

#### GET /sessions

    

    Returns a list of the currently active sessions. Each session will be returned as a list of JSON objects with the following keys:      **Key**| **Type**| **Description**|  id| string| The session ID.   ---|---|---   capabilities| object| An object describing the session's capabilities.       

**Returns:**     `{Array.<Object>}` A list of the currently active sessions.

* * *

#### /session/:sessionId

    

#### GET /session/:sessionId

    

    Retrieve the capabilities of the specified session.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**Returns:**     `{object}` An object describing the session's capabilities.

    

#### DELETE /session/:sessionId

    

    Delete the session.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.

* * *

#### /session/:sessionId/timeouts

    

#### POST /session/:sessionId/timeouts

    

    Configure the amount of time that a particular type of operation can execute for before they are aborted and a |Timeout| error is returned to the client.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**JSON Parameters:**     `type` \- `{string}` The type of operation to set the timeout for. Valid values are: "script" for script timeouts, "implicit" for modifying the implicit wait timeout and "page load" for setting a page load timeout.     `ms` \- `{number}` The amount of time, in milliseconds, that time-limited commands are permitted to run.

* * *

#### /session/:sessionId/timeouts/async\_script

    

#### POST /session/:sessionId/timeouts/async\_script

    

    Set the amount of time, in milliseconds, that asynchronous scripts executed by `/session/:sessionId/execute_async` are permitted to run before they are aborted and a |Timeout| error is returned to the client.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**JSON Parameters:**     `ms` \- `{number}` The amount of time, in milliseconds, that time-limited commands are permitted to run.

* * *

#### /session/:sessionId/timeouts/implicit\_wait

    

#### POST /session/:sessionId/timeouts/implicit\_wait

    

    Set the amount of time the driver should wait when searching for elements. When   searching for a single element, the driver should poll the page until an element is found or   the timeout expires, whichever occurs first. When searching for multiple elements, the driver   should poll the page until at least one element is found or the timeout expires, at which point   it should return an empty list.      If this command is never sent, the driver should default to an implicit wait of 0ms.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**JSON Parameters:**     `ms` \- `{number}` The amount of time to wait, in milliseconds. This value has a lower bound of 0.

* * *

#### /session/:sessionId/window\_handle

    

#### GET /session/:sessionId/window\_handle

    

    Retrieve the current window handle.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**Returns:**     `{string}` The current window handle.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.

* * *

#### /session/:sessionId/window\_handles

    

#### GET /session/:sessionId/window\_handles

    

    Retrieve the list of all window handles available to the session.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**Returns:**     `{Array.<string>}` A list of window handles.

* * *

#### /session/:sessionId/url

    

#### GET /session/:sessionId/url

    

    Retrieve the URL of the current page.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**Returns:**     `{string}` The current URL.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.

    

#### POST /session/:sessionId/url

    

    Navigate to a new URL.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**JSON Parameters:**     `url` \- `{string}` The URL to navigate to.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.

* * *

#### /session/:sessionId/forward

    

#### POST /session/:sessionId/forward

    

    Navigate forwards in the browser history, if possible.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.

* * *

#### /session/:sessionId/back

    

#### POST /session/:sessionId/back

    

    Navigate backwards in the browser history, if possible.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.

* * *

#### /session/:sessionId/refresh

    

#### POST /session/:sessionId/refresh

    

    Refresh the current page.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.

* * *

#### /session/:sessionId/execute

    

#### POST /session/:sessionId/execute

    

    Inject a snippet of JavaScript into the page for execution in the context of the currently selected frame. The executed script is assumed to be synchronous and the result of evaluating the script is returned to the client.      The `script` argument defines the script to execute in the form of a function body. The value returned by that function will be returned to the client. The function will be invoked with the provided `args` array and the values may be accessed via the `arguments` object in the order specified.      Arguments may be any JSON-primitive, array, or JSON object. JSON objects that define a WebElement reference will be converted to the corresponding DOM element. Likewise, any WebElements in the script result will be returned to the client as WebElement JSON objects.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**JSON Parameters:**     `script` \- `{string}` The script to execute.     `args` \- `{Array.<*>}` The script arguments.     

**Returns:**     `{*}` The script result.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.     `StaleElementReference` \- If one of the script arguments is a WebElement that is not attached to the page's DOM.     `JavaScriptError` \- If the script throws an Error.

* * *

#### /session/:sessionId/execute\_async

    

#### POST /session/:sessionId/execute\_async

    

    Inject a snippet of JavaScript into the page for execution in the context of the currently selected frame. The executed script is assumed to be asynchronous and must signal that is done by invoking the provided callback, which is always provided as the final argument to the function. The value to this callback will be returned to the client.      Asynchronous script commands may not span page loads. If an `unload` event is fired while waiting for a script result, an error should be returned to the client.      The `script` argument defines the script to execute in teh form of a function body. The function will be invoked with the provided `args` array and the values may be accessed via the `arguments` object in the order specified. The final argument will always be a callback function that must be invoked to signal that the script has finished.      Arguments may be any JSON-primitive, array, or JSON object. JSON objects that define a WebElement reference will be converted to the corresponding DOM element. Likewise, any WebElements in the script result will be returned to the client as WebElement JSON objects.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**JSON Parameters:**     `script` \- `{string}` The script to execute.     `args` \- `{Array.<*>}` The script arguments.     

**Returns:**     `{*}` The script result.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.     `StaleElementReference` \- If one of the script arguments is a WebElement that is not attached to the page's DOM.     `Timeout` \- If the script callback is not invoked before the timout expires. Timeouts are controlled by the `/session/:sessionId/timeout/async_script` command.     `JavaScriptError` \- If the script throws an Error or if an `unload` event is fired while waiting for the script to finish.

* * *

#### /session/:sessionId/screenshot

    

#### GET /session/:sessionId/screenshot

    

    Take a screenshot of the current page.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**Returns:**     `{string}` The screenshot as a base64 encoded PNG.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.

* * *

#### /session/:sessionId/ime/available\_engines

    

#### GET /session/:sessionId/ime/available\_engines

    

    List all available engines on the machine. To use an engine, it has to be present in this list.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**Returns:**     `{Array.<string>}` A list of available engines     

**Potential Errors:**     `ImeNotAvailableException` \- If the host does not support IME

* * *

#### /session/:sessionId/ime/active\_engine

    

#### GET /session/:sessionId/ime/active\_engine

    

    Get the name of the active IME engine. The name string is platform specific.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**Returns:**     `{string}` The name of the active IME engine.     

**Potential Errors:**     `ImeNotAvailableException` \- If the host does not support IME

* * *

#### /session/:sessionId/ime/activated

    

#### GET /session/:sessionId/ime/activated

    

    Indicates whether IME input is active at the moment \(not if it's available.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**Returns:**     `{boolean}` true if IME input is available and currently active, false otherwise     

**Potential Errors:**     `ImeNotAvailableException` \- If the host does not support IME

* * *

#### /session/:sessionId/ime/deactivate

    

#### POST /session/:sessionId/ime/deactivate

    

    De-activates the currently-active IME engine.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**Potential Errors:**     `ImeNotAvailableException` \- If the host does not support IME

* * *

#### /session/:sessionId/ime/activate

    

#### POST /session/:sessionId/ime/activate

    

    Make an engines that is available \(appears on the list   returned by getAvailableEngines\) active. After this call, the engine will   be added to the list of engines loaded in the IME daemon and the input sent   using sendKeys will be converted by the active engine.   Note that this is a platform-independent method of activating IME   \(the platform-specific way being using keyboard shortcuts     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**JSON Parameters:**     `engine` \- `{string}` Name of the engine to activate.     

**Potential Errors:**     `ImeActivationFailedException` \- If the engine is not available or if the activation fails for other reasons.     `ImeNotAvailableException` \- If the host does not support IME

* * *

#### /session/:sessionId/frame

    

#### POST /session/:sessionId/frame

    

    Change focus to another frame on the page. If the frame `id` is `null`, the server   should switch to the page's default content.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**JSON Parameters:**     `id` \- `{string|number|null|WebElement JSON Object}` Identifier for the frame to change focus to.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.     `NoSuchFrame` \- If the frame specified by `id` cannot be found.

* * *

#### /session/:sessionId/frame/parent

    

#### POST /session/:sessionId/frame/parent

    

    Change focus to the parent context. If the current context is the top level browsing context, the context remains unchanged.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.

* * *

#### /session/:sessionId/window

    

#### POST /session/:sessionId/window

    

    Change focus to another window. The window to change focus to may be specified by its   server assigned window handle, or by the value of its `name` attribute.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**JSON Parameters:**     `name` \- `{string}` The window to change focus to.     

**Potential Errors:**     `NoSuchWindow` \- If the window specified by `name` cannot be found.

    

#### DELETE /session/:sessionId/window

    

    Close the current window.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window is already closed

* * *

#### /session/:sessionId/window/:windowHandle/size

    

#### POST /session/:sessionId/window/:windowHandle/size

    

    Change the size of the specified window. If the :windowHandle URL parameter is "current", the currently active window will be resized.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**JSON Parameters:**     `width` \- `{number}` The new window width.     `height` \- `{number}` The new window height.

    

#### GET /session/:sessionId/window/:windowHandle/size

    

    Get the size of the specified window. If the :windowHandle URL parameter is "current", the size of the currently active window will be returned.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**Returns:**     `{width: number, height: number}` The size of the window.     

**Potential Errors:**     `NoSuchWindow` \- If the specified window cannot be found.

* * *

#### /session/:sessionId/window/:windowHandle/position

    

#### POST /session/:sessionId/window/:windowHandle/position

    

    Change the position of the specified window. If the :windowHandle URL parameter is "current", the currently active window will be moved.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**JSON Parameters:**     `x` \- `{number}` The X coordinate to position the window at, relative to the upper left corner of the screen.     `y` \- `{number}` The Y coordinate to position the window at, relative to the upper left corner of the screen.     

**Potential Errors:**     `NoSuchWindow` \- If the specified window cannot be found.

    

#### GET /session/:sessionId/window/:windowHandle/position

    

    Get the position of the specified window. If the :windowHandle URL parameter is "current", the position of the currently active window will be returned.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**Returns:**     `{x: number, y: number}` The X and Y coordinates for the window, relative to the upper left corner of the screen.     

**Potential Errors:**     `NoSuchWindow` \- If the specified window cannot be found.

* * *

#### /session/:sessionId/window/:windowHandle/maximize

    

#### POST /session/:sessionId/window/:windowHandle/maximize

    

    Maximize the specified window if not already maximized. If the :windowHandle URL parameter is "current", the currently active window will be maximized.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**Potential Errors:**     `NoSuchWindow` \- If the specified window cannot be found.

* * *

#### /session/:sessionId/cookie

    

#### GET /session/:sessionId/cookie

    

    Retrieve all cookies visible to the current page.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**Returns:**     `{Array.<object>}` A list of cookies.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.

    

#### POST /session/:sessionId/cookie

    

    Set a cookie. If the cookie path is not specified, it should be set to `"/"`. Likewise, if the domain is omitted, it should default to the current page's domain.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**JSON Parameters:**     `cookie` \- `{object}` A JSON object defining the cookie to add.

    

#### DELETE /session/:sessionId/cookie

    

    Delete all cookies visible to the current page.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**Potential Errors:**     `InvalidCookieDomain` \- If the cookie's `domain` is not visible from the current page.     `NoSuchWindow` \- If the currently selected window has been closed.     `UnableToSetCookie` \- If attempting to set a cookie on a page that does not support cookies \(e.g. pages with mime-type `text/plain`\).

* * *

#### /session/:sessionId/cookie/:name

    

#### DELETE /session/:sessionId/cookie/:name

    

    Delete the cookie with the given name. This command should be a no-op if there is no   such cookie visible to the current page.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     `:name` \- The name of the cookie to delete.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.

* * *

#### /session/:sessionId/source

    

#### GET /session/:sessionId/source

    

    Get the current page source.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**Returns:**     `{string}` The current page source.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.

* * *

#### /session/:sessionId/title

    

#### GET /session/:sessionId/title

    

    Get the current page title.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**Returns:**     `{string}` The current page title.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.

* * *

#### /session/:sessionId/element

    

#### POST /session/:sessionId/element

    

    Search for an element on the page, starting from the document root. The located element will be returned as a WebElement JSON object. The table below lists the locator strategies that each server should support. Each locator must return the first matching element located in the DOM.      **Strategy**| **Description**|  class name| Returns an element whose class name contains the search value; compound class names are not permitted.   ---|---   css selector| Returns an element matching a CSS selector.   id| Returns an element whose ID attribute matches the search value.   name| Returns an element whose NAME attribute matches the search value.   link text| Returns an anchor element whose visible text matches the search value.   partial link text| Returns an anchor element whose visible text partially matches the search value.   tag name| Returns an element whose tag name matches the search value.   xpath| Returns an element matching an XPath expression.       

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**JSON Parameters:**     `using` \- `{string}` The locator strategy to use.     `value` \- `{string}` The The search target.     

**Returns:**     `{ELEMENT:string}` A WebElement JSON object for the located element.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.     `NoSuchElement` \- If the element cannot be found.     `XPathLookupError` \- If using XPath and the input expression is invalid.

* * *

#### /session/:sessionId/elements

    

#### POST /session/:sessionId/elements

    

    Search for multiple elements on the page, starting from the document root. The located elements will be returned as a WebElement JSON objects. The table below lists the locator strategies that each server should support. Elements should be returned in the order located in the DOM.      **Strategy**| **Description**|  class name| Returns all elements whose class name contains the search value; compound class names are not permitted.   ---|---   css selector| Returns all elements matching a CSS selector.   id| Returns all elements whose ID attribute matches the search value.   name| Returns all elements whose NAME attribute matches the search value.   link text| Returns all anchor elements whose visible text matches the search value.   partial link text| Returns all anchor elements whose visible text partially matches the search value.   tag name| Returns all elements whose tag name matches the search value.   xpath| Returns all elements matching an XPath expression.       

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**JSON Parameters:**     `using` \- `{string}` The locator strategy to use.     `value` \- `{string}` The The search target.     

**Returns:**     `{Array.<{ELEMENT:string}>}` A list of WebElement JSON objects for the located elements.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.     `XPathLookupError` \- If using XPath and the input expression is invalid.

* * *

#### /session/:sessionId/element/active

    

#### POST /session/:sessionId/element/active

    

    Get the element on the page that currently has focus. The element will be returned as a WebElement JSON object.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**Returns:**     `{ELEMENT:string}` A WebElement JSON object for the active element.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.

* * *

#### /session/:sessionId/element/:id

    

#### GET /session/:sessionId/element/:id

    

    Describe the identified element.      **Note:** This command is reserved for future use; its return type is currently undefined.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     `:id` \- ID of the element to route the command to.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.     `StaleElementReference` \- If the element referenced by `:id` is no longer attached to the page's DOM.

* * *

#### /session/:sessionId/element/:id/element

    

#### POST /session/:sessionId/element/:id/element

    

    Search for an element on the page, starting from the identified element. The located element will be returned as a WebElement JSON object. The table below lists the locator strategies that each server should support. Each locator must return the first matching element located in the DOM.      **Strategy**| **Description**|  class name| Returns an element whose class name contains the search value; compound class names are not permitted.   ---|---   css selector| Returns an element matching a CSS selector.   id| Returns an element whose ID attribute matches the search value.   name| Returns an element whose NAME attribute matches the search value.   link text| Returns an anchor element whose visible text matches the search value.   partial link text| Returns an anchor element whose visible text partially matches the search value.   tag name| Returns an element whose tag name matches the search value.   xpath| Returns an element matching an XPath expression. The provided XPath expression must be applied to the server "as is"; if the expression is not relative to the element root, the server should not modify it. Consequently, an XPath query may return elements not contained in the root element's subtree.       

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     `:id` \- ID of the element to route the command to.     

**JSON Parameters:**     `using` \- `{string}` The locator strategy to use.     `value` \- `{string}` The The search target.     

**Returns:**     `{ELEMENT:string}` A WebElement JSON object for the located element.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.     `StaleElementReference` \- If the element referenced by `:id` is no longer attached to the page's DOM.     `NoSuchElement` \- If the element cannot be found.     `XPathLookupError` \- If using XPath and the input expression is invalid.

* * *

#### /session/:sessionId/element/:id/elements

    

#### POST /session/:sessionId/element/:id/elements

    

    Search for multiple elements on the page, starting from the identified element. The located elements will be returned as a WebElement JSON objects. The table below lists the locator strategies that each server should support. Elements should be returned in the order located in the DOM.      **Strategy**| **Description**|  class name| Returns all elements whose class name contains the search value; compound class names are not permitted.   ---|---   css selector| Returns all elements matching a CSS selector.   id| Returns all elements whose ID attribute matches the search value.   name| Returns all elements whose NAME attribute matches the search value.   link text| Returns all anchor elements whose visible text matches the search value.   partial link text| Returns all anchor elements whose visible text partially matches the search value.   tag name| Returns all elements whose tag name matches the search value.   xpath| Returns all elements matching an XPath expression. The provided XPath expression must be applied to the server "as is"; if the expression is not relative to the element root, the server should not modify it. Consequently, an XPath query may return elements not contained in the root element's subtree.       

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     `:id` \- ID of the element to route the command to.     

**JSON Parameters:**     `using` \- `{string}` The locator strategy to use.     `value` \- `{string}` The The search target.     

**Returns:**     `{Array.<{ELEMENT:string}>}` A list of WebElement JSON objects for the located elements.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.     `StaleElementReference` \- If the element referenced by `:id` is no longer attached to the page's DOM.     `XPathLookupError` \- If using XPath and the input expression is invalid.

* * *

#### /session/:sessionId/element/:id/click

    

#### POST /session/:sessionId/element/:id/click

    

    Click on an element.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     `:id` \- ID of the element to route the command to.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.     `StaleElementReference` \- If the element referenced by `:id` is no longer attached to the page's DOM.     `ElementNotVisible` \- If the referenced element is not visible on the page \(either is hidden by CSS, has 0-width, or has 0-height\)

* * *

#### /session/:sessionId/element/:id/submit

    

#### POST /session/:sessionId/element/:id/submit

    

    Submit a `FORM` element. The submit command may also be applied to any element that is a descendant of a `FORM` element.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     `:id` \- ID of the element to route the command to.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.     `StaleElementReference` \- If the element referenced by `:id` is no longer attached to the page's DOM.

* * *

#### /session/:sessionId/element/:id/text

    

#### GET /session/:sessionId/element/:id/text

    

    Returns the visible text for the element.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     `:id` \- ID of the element to route the command to.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.     `StaleElementReference` \- If the element referenced by `:id` is no longer attached to the page's DOM.

* * *

#### /session/:sessionId/element/:id/value

    

#### POST /session/:sessionId/element/:id/value

    

    Send a sequence of key strokes to an element.      Any UTF-8 character may be specified, however, if the server does not support native key events, it should simulate key strokes for a standard US keyboard layout. The Unicode [Private Use Area](http://unicode.org/faq/casemap_charprop.html#8) code points, 0xE000-0xF8FF, are used to represent pressable, non-text keys \(see table below\).         | **Key**| **Code**|  NULL| U+E000   ---|---   Cancel| U+E001   Help| U+E002   Back space| U+E003   Tab| U+E004   Clear| U+E005   Return1| U+E006   Enter1| U+E007   Shift| U+E008   Control| U+E009   Alt| U+E00A   Pause| U+E00B   Escape| U+E00C   | **Key**| **Code**|  Space| U+E00D   ---|---   Pageup| U+E00E   Pagedown| U+E00F   End| U+E010   Home| U+E011   Left arrow| U+E012   Up arrow| U+E013   Right arrow| U+E014   Down arrow| U+E015   Insert| U+E016   Delete| U+E017   Semicolon| U+E018   Equals| U+E019   | **Key**| **Code**|  Numpad 0| U+E01A   ---|---   Numpad 1| U+E01B   Numpad 2| U+E01C   Numpad 3| U+E01D   Numpad 4| U+E01E   Numpad 5| U+E01F   Numpad 6| U+E020   Numpad 7| U+E021   Numpad 8| U+E022   Numpad 9| U+E023   | **Key**| **Code**|  Multiply| U+E024   ---|---   Add| U+E025   Separator| U+E026   Subtract| U+E027   Decimal| U+E028   Divide| U+E029   | **Key**| **Code**|  F1| U+E031   ---|---   F2| U+E032   F3| U+E033   F4| U+E034   F5| U+E035   F6| U+E036   F7| U+E037   F8| U+E038   F9| U+E039   F10| U+E03A   F11| U+E03B   F12| U+E03C   Command/Meta| U+E03D   1 The return key is _not the same_ as the [enter key](http://en.wikipedia.org/wiki/Enter_key).      The server must process the key sequence as follows:  

  * Each key that appears on the keyboard without requiring modifiers are sent as a keydown followed by a key up.  

  * If the server does not support native events and must simulate key strokes with JavaScript, it must generate keydown, keypress, and keyup events, in that order. The keypress event should only be fired when the corresponding key is for a printable character.  

  * If a key requires a modifier key \(e.g. "\!" on a standard US keyboard\), the sequence is: modifier down, key down, key up, modifier up, where key is the ideal unmodified key value \(using the previous example, a "1"\).  

  * Modifier keys \(Ctrl, Shift, Alt, and Command/Meta\) are assumed to be "sticky"; each modifier should be held down \(e.g. only a keydown event\) until either the modifier is encountered again in the sequence, or the `NULL` \(U+E000\) key is encountered.  

  * Each key sequence is terminated with an implicit `NULL` key. Subsequently, all depressed modifier keys must be released \(with corresponding keyup events\) at the end of the sequence.  

    

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     `:id` \- ID of the element to route the command to.     

**JSON Parameters:**     `value` \- `{Array.<string>}` The sequence of keys to type. An array must be provided. The server should flatten the array items to a single string to be typed.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.     `StaleElementReference` \- If the element referenced by `:id` is no longer attached to the page's DOM.     `ElementNotVisible` \- If the referenced element is not visible on the page \(either is hidden by CSS, has 0-width, or has 0-height\)

* * *

#### /session/:sessionId/keys

    

#### POST /session/:sessionId/keys

    

    Send a sequence of key strokes to the active element. This command is similar to the [send keys](https://www.selenium.dev/documentation/legacy/JsonWireProtocol#/session/:sessionId/element/:id/value.md) command in every aspect except the implicit termination: The modifiers are **not** released at the end of the call. Rather, the state of the modifier keys is kept between calls, so mouse interactions can be performed while modifier keys are depressed.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**JSON Parameters:**     `value` \- `{Array.<string>}` The keys sequence to be sent. The sequence is defined in the[send keys](https://www.selenium.dev/documentation/legacy/JsonWireProtocol#/session/:sessionId/element/:id/value.md) command.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.

* * *

#### /session/:sessionId/element/:id/name

    

#### GET /session/:sessionId/element/:id/name

    

    Query for an element's tag name.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     `:id` \- ID of the element to route the command to.     

**Returns:**     `{string}` The element's tag name, as a lowercase string.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.     `StaleElementReference` \- If the element referenced by `:id` is no longer attached to the page's DOM.

* * *

#### /session/:sessionId/element/:id/clear

    

#### POST /session/:sessionId/element/:id/clear

    

    Clear a `TEXTAREA` or `text INPUT` element's value.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     `:id` \- ID of the element to route the command to.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.     `StaleElementReference` \- If the element referenced by `:id` is no longer attached to the page's DOM.     `ElementNotVisible` \- If the referenced element is not visible on the page \(either is hidden by CSS, has 0-width, or has 0-height\)     `InvalidElementState` \- If the referenced element is disabled.

* * *

#### /session/:sessionId/element/:id/selected

    

#### GET /session/:sessionId/element/:id/selected

    

    Determine if an `OPTION` element, or an `INPUT` element of type `checkbox` or `radiobutton` is currently selected.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     `:id` \- ID of the element to route the command to.     

**Returns:**     `{boolean}` Whether the element is selected.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.     `StaleElementReference` \- If the element referenced by `:id` is no longer attached to the page's DOM.

* * *

#### /session/:sessionId/element/:id/enabled

    

#### GET /session/:sessionId/element/:id/enabled

    

    Determine if an element is currently enabled.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     `:id` \- ID of the element to route the command to.     

**Returns:**     `{boolean}` Whether the element is enabled.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.     `StaleElementReference` \- If the element referenced by `:id` is no longer attached to the page's DOM.

* * *

#### /session/:sessionId/element/:id/attribute/:name

    

#### GET /session/:sessionId/element/:id/attribute/:name

    

    Get the value of an element's attribute.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     `:id` \- ID of the element to route the command to.     

**Returns:**     `{string|null}` The value of the attribute, or null if it is not set on the element.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.     `StaleElementReference` \- If the element referenced by `:id` is no longer attached to the page's DOM.

* * *

#### /session/:sessionId/element/:id/equals/:other

    

#### GET /session/:sessionId/element/:id/equals/:other

    

    Test if two element IDs refer to the same DOM element.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     `:id` \- ID of the element to route the command to.     `:other` \- ID of the element to compare against.     

**Returns:**     `{boolean}` Whether the two IDs refer to the same element.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.     `StaleElementReference` \- If either the element refered to by `:id` or `:other` is no longer attached to the page's DOM.

* * *

#### /session/:sessionId/element/:id/displayed

    

#### GET /session/:sessionId/element/:id/displayed

    

    Determine if an element is currently displayed.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     `:id` \- ID of the element to route the command to.     

**Returns:**     `{boolean}` Whether the element is displayed.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.     `StaleElementReference` \- If the element referenced by `:id` is no longer attached to the page's DOM.

* * *

#### /session/:sessionId/element/:id/location

    

#### GET /session/:sessionId/element/:id/location

    

    Determine an element's location on the page. The point `(0, 0)` refers to the upper-left corner of the page. The element's coordinates are returned as a JSON object with `x` and `y` properties.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     `:id` \- ID of the element to route the command to.     

**Returns:**     `{x:number, y:number}` The X and Y coordinates for the element on the page.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.     `StaleElementReference` \- If the element referenced by `:id` is no longer attached to the page's DOM.

* * *

#### /session/:sessionId/element/:id/location\_in\_view

    

#### GET /session/:sessionId/element/:id/location\_in\_view

    

    Determine an element's location on the screen once it has been scrolled into view.      **Note:** This is considered an internal command and should **only** be used to determine an element's   location for correctly generating native events.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     `:id` \- ID of the element to route the command to.     

**Returns:**     `{x:number, y:number}` The X and Y coordinates for the element.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.     `StaleElementReference` \- If the element referenced by `:id` is no longer attached to the page's DOM.

* * *

#### /session/:sessionId/element/:id/size

    

#### GET /session/:sessionId/element/:id/size

    

    Determine an element's size in pixels. The size will be returned as a JSON object with `width` and `height` properties.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     `:id` \- ID of the element to route the command to.     

**Returns:**     `{width:number, height:number}` The width and height of the element, in pixels.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.     `StaleElementReference` \- If the element referenced by `:id` is no longer attached to the page's DOM.

* * *

#### /session/:sessionId/element/:id/css/:propertyName

    

#### GET /session/:sessionId/element/:id/css/:propertyName

    

    Query the value of an element's computed CSS property. The CSS property to query should be specified using the CSS property name, **not** the JavaScript property name \(e.g. `background-color` instead of `backgroundColor`\).     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     `:id` \- ID of the element to route the command to.     

**Returns:**     `{string}` The value of the specified CSS property.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.     `StaleElementReference` \- If the element referenced by `:id` is no longer attached to the page's DOM.

* * *

#### /session/:sessionId/orientation

    

#### GET /session/:sessionId/orientation

    

    Get the current browser orientation. The server should return a valid orientation value as defined in [ScreenOrientation](http://selenium.googlecode.com/git/docs/api/java/org/openqa/selenium/ScreenOrientation.html): `{LANDSCAPE|PORTRAIT}`.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**Returns:**     `{string}` The current browser orientation corresponding to a value defined in [ScreenOrientation](http://selenium.googlecode.com/git/docs/api/java/org/openqa/selenium/ScreenOrientation.html): `{LANDSCAPE|PORTRAIT}`.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.

    

#### POST /session/:sessionId/orientation

    

    Set the browser orientation. The orientation should be specified as defined in [ScreenOrientation](http://selenium.googlecode.com/git/docs/api/java/org/openqa/selenium/ScreenOrientation.html): `{LANDSCAPE|PORTRAIT}`.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**JSON Parameters:**     `orientation` \- `{string}` The new browser orientation as defined in [ScreenOrientation](http://selenium.googlecode.com/git/docs/api/java/org/openqa/selenium/ScreenOrientation.html): `{LANDSCAPE|PORTRAIT}`.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.

* * *

#### /session/:sessionId/alert\_text

    

#### GET /session/:sessionId/alert\_text

    

    Gets the text of the currently displayed JavaScript `alert()`, `confirm()`, or `prompt()` dialog.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**Returns:**     `{string}` The text of the currently displayed alert.     

**Potential Errors:**     `NoAlertPresent` \- If there is no alert displayed.

    

#### POST /session/:sessionId/alert\_text

    

    Sends keystrokes to a JavaScript `prompt()` dialog.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**JSON Parameters:**     `text` \- `{string}` Keystrokes to send to the `prompt()` dialog.     

**Potential Errors:**     `NoAlertPresent` \- If there is no alert displayed.

* * *

#### /session/:sessionId/accept\_alert

    

#### POST /session/:sessionId/accept\_alert

    

    Accepts the currently displayed alert dialog. Usually, this is equivalent to clicking on the 'OK' button in the dialog.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**Potential Errors:**     `NoAlertPresent` \- If there is no alert displayed.

* * *

#### /session/:sessionId/dismiss\_alert

    

#### POST /session/:sessionId/dismiss\_alert

    

    Dismisses the currently displayed alert dialog. For `confirm()` and `prompt()` dialogs, this is equivalent to clicking the 'Cancel' button. For `alert()` dialogs, this is equivalent to clicking the 'OK' button.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**Potential Errors:**     `NoAlertPresent` \- If there is no alert displayed.

* * *

#### /session/:sessionId/moveto

    

#### POST /session/:sessionId/moveto

    

    Move the mouse by an offset of the specificed element. If no element is specified, the move is relative to the current mouse cursor. If an element is provided but no offset, the mouse will be moved to the center of the element. If the element is not visible, it will be scrolled into view.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**JSON Parameters:**     `element` \- `{string}` Opaque ID assigned to the element to move to, as described in the WebElement JSON Object. If not specified or is null, the offset is relative to current position of the mouse.     `xoffset` \- `{number}` X offset to move to, relative to the top-left corner of the element. If not specified, the mouse will move to the middle of the element.     `yoffset` \- `{number}` Y offset to move to, relative to the top-left corner of the element. If not specified, the mouse will move to the middle of the element.

* * *

#### /session/:sessionId/click

    

#### POST /session/:sessionId/click

    

    Click any mouse button \(at the coordinates set by the last moveto command\). Note that calling this command after calling buttondown and before calling button up \(or any out-of-order interactions sequence\) will yield undefined behaviour\).     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**JSON Parameters:**     `button` \- `{number}` Which button, enum: `{LEFT = 0, MIDDLE = 1 , RIGHT = 2}`. Defaults to the left mouse button if not specified.

* * *

#### /session/:sessionId/buttondown

    

#### POST /session/:sessionId/buttondown

    

    Click and hold the left mouse button \(at the coordinates set by the last moveto command\). Note that the next mouse-related command that should follow is buttonup . Any other mouse command \(such as click or another call to buttondown\) will yield undefined behaviour.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**JSON Parameters:**     `button` \- `{number}` Which button, enum: `{LEFT = 0, MIDDLE = 1 , RIGHT = 2}`. Defaults to the left mouse button if not specified.

* * *

#### /session/:sessionId/buttonup

    

#### POST /session/:sessionId/buttonup

    

    Releases the mouse button previously held \(where the mouse is currently at\). Must be called once for every buttondown command issued. See the note in click and buttondown about implications of out-of-order commands.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**JSON Parameters:**     `button` \- `{number}` Which button, enum: `{LEFT = 0, MIDDLE = 1 , RIGHT = 2}`. Defaults to the left mouse button if not specified.

* * *

#### /session/:sessionId/doubleclick

    

#### POST /session/:sessionId/doubleclick

    

    Double-clicks at the current mouse coordinates \(set by moveto\).     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.

* * *

#### /session/:sessionId/touch/click

    

#### POST /session/:sessionId/touch/click

    

    Single tap on the touch enabled device.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**JSON Parameters:**     `element` \- `{string}` ID of the element to single tap on.

* * *

#### /session/:sessionId/touch/down

    

#### POST /session/:sessionId/touch/down

    

    Finger down on the screen.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**JSON Parameters:**     `x` \- `{number}` X coordinate on the screen.     `y` \- `{number}` Y coordinate on the screen.

* * *

#### /session/:sessionId/touch/up

    

#### POST /session/:sessionId/touch/up

    

    Finger up on the screen.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**JSON Parameters:**     `x` \- `{number}` X coordinate on the screen.     `y` \- `{number}` Y coordinate on the screen.

* * *

#### session/:sessionId/touch/move

    

#### POST session/:sessionId/touch/move

    

    Finger move on the screen.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**JSON Parameters:**     `x` \- `{number}` X coordinate on the screen.     `y` \- `{number}` Y coordinate on the screen.

* * *

#### session/:sessionId/touch/scroll

    

#### POST session/:sessionId/touch/scroll

    

    Scroll on the touch screen using finger based motion events. Use this command to start scrolling at a particular screen location.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**JSON Parameters:**     `element` \- `{string}` ID of the element where the scroll starts.     `xoffset` \- `{number}` The x offset in pixels to scroll by.     `yoffset` \- `{number}` The y offset in pixels to scroll by.

* * *

#### session/:sessionId/touch/scroll

    

#### POST session/:sessionId/touch/scroll

    

    Scroll on the touch screen using finger based motion events. Use this command if you don't care where the scroll starts on the screen.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**JSON Parameters:**     `xoffset` \- `{number}` The x offset in pixels to scrollby.     `yoffset` \- `{number}` The y offset in pixels to scrollby.

* * *

#### session/:sessionId/touch/doubleclick

    

#### POST session/:sessionId/touch/doubleclick

    

    Double tap on the touch screen using finger motion events.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**JSON Parameters:**     `element` \- `{string}` ID of the element to double tap on.

* * *

#### session/:sessionId/touch/longclick

    

#### POST session/:sessionId/touch/longclick

    

    Long press on the touch screen using finger motion events.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**JSON Parameters:**     `element` \- `{string}` ID of the element to long press on.

* * *

#### session/:sessionId/touch/flick

    

#### POST session/:sessionId/touch/flick

    

    Flick on the touch screen using finger motion events. This flickcommand starts at a particulat screen location.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**JSON Parameters:**     `element` \- `{string}` ID of the element where the flick starts.     `xoffset` \- `{number}` The x offset in pixels to flick by.     `yoffset` \- `{number}` The y offset in pixels to flick by.     `speed` \- `{number}` The speed in pixels per seconds.

* * *

#### session/:sessionId/touch/flick

    

#### POST session/:sessionId/touch/flick

    

    Flick on the touch screen using finger motion events. Use this flick command if you don't care where the flick starts on the screen.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**JSON Parameters:**     `xspeed` \- `{number}` The x speed in pixels per second.     `yspeed` \- `{number}` The y speed in pixels per second.

* * *

#### /session/:sessionId/location

    

#### GET /session/:sessionId/location

    

    Get the current geo location.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**Returns:**     `{latitude: number, longitude: number, altitude: number}` The current geo location.

    

#### POST /session/:sessionId/location

    

    Set the current geo location.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**JSON Parameters:**     `location` \- `{latitude: number, longitude: number, altitude: number}` The new location.

* * *

#### /session/:sessionId/local\_storage

    

#### GET /session/:sessionId/local\_storage

    

    Get all keys of the storage.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**Returns:**     `{Array.<string>}` The list of keys.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.

    

#### POST /session/:sessionId/local\_storage

    

    Set the storage item for the given key.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**JSON Parameters:**     `key` \- `{string}` The key to set.     `value` \- `{string}` The value to set.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.

    

#### DELETE /session/:sessionId/local\_storage

    

    Clear the storage.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.

* * *

#### /session/:sessionId/local\_storage/key/:key

    

#### GET /session/:sessionId/local\_storage/key/:key

    

    Get the storage item for the given key.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     `:key` \- The key to get.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.

    

#### DELETE /session/:sessionId/local\_storage/key/:key

    

    Remove the storage item for the given key.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     `:key` \- The key to remove.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.

* * *

#### /session/:sessionId/local\_storage/size

    

#### GET /session/:sessionId/local\_storage/size

    

    Get the number of items in the storage.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**Returns:**     `{number}` The number of items in the storage.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.

* * *

#### /session/:sessionId/session\_storage

    

#### GET /session/:sessionId/session\_storage

    

    Get all keys of the storage.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**Returns:**     `{Array.<string>}` The list of keys.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.

    

#### POST /session/:sessionId/session\_storage

    

    Set the storage item for the given key.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**JSON Parameters:**     `key` \- `{string}` The key to set.     `value` \- `{string}` The value to set.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.

    

#### DELETE /session/:sessionId/session\_storage

    

    Clear the storage.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.

* * *

#### /session/:sessionId/session\_storage/key/:key

    

#### GET /session/:sessionId/session\_storage/key/:key

    

    Get the storage item for the given key.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     `:key` \- The key to get.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.

    

#### DELETE /session/:sessionId/session\_storage/key/:key

    

    Remove the storage item for the given key.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     `:key` \- The key to remove.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.

* * *

#### /session/:sessionId/session\_storage/size

    

#### GET /session/:sessionId/session\_storage/size

    

    Get the number of items in the storage.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**Returns:**     `{number}` The number of items in the storage.     

**Potential Errors:**     `NoSuchWindow` \- If the currently selected window has been closed.

* * *

#### /session/:sessionId/log

    

#### POST /session/:sessionId/log

    

    Get the log for a given log type. Log buffer is reset after each request.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**JSON Parameters:**     `type` \- `{string}` The log type. This must be provided.     

**Returns:**     `{Array.<object>}` The list of log entries.

* * *

#### /session/:sessionId/log/types

    

#### GET /session/:sessionId/log/types

    

    Get available log types.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**Returns:**     `{Array.<string>}` The list of available log types.

* * *

#### /session/:sessionId/application\_cache/status

    

#### GET /session/:sessionId/application\_cache/status

    

    Get the status of the html5 application cache.     

**URL Parameters:**     `:sessionId` \- ID of the session to route the command to.     

**Returns:**     `{number}` Status code for application cache: \{UNCACHED = 0, IDLE = 1, CHECKING = 2, DOWNLOADING = 3, UPDATE\_READY = 4, OBSOLETE = 5\}

Last modified January 10, 2022: [More wiki \(\#907\) \[deploy site\] \(adcf706a1ad\)](https://github.com/SeleniumHQ/seleniumhq.github.io/commit/adcf706a1ad907d028dc57d10201a265972432af)