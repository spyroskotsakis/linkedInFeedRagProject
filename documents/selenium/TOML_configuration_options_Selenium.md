# TOML configuration options | Selenium

**URL:** https://www.selenium.dev/documentation/grid/configuration/toml_options
**Word Count:** 615
**Links Count:** 215
**Scraped:** 2025-07-17 06:15:03
**Status:** completed

---

# TOML configuration options

Grid configuration examples using Toml files.

All the options shown in [CLI options](https://www.selenium.dev/documentation/grid/configuration/cli_options/) can be configured through a [TOML](https://github.com/toml-lang/toml) file. This page shows configuration examples for the different Grid components.

Note that this documentation could be outdated if an option was modified or added but has not been documented yet. In case you bump into this situation, please check the [“Config help”](https://www.selenium.dev/documentation/grid/configuration/help/) section and feel free to send us a pull request updating this page.

## Overview

Selenium Grid uses [TOML](https://github.com/toml-lang/toml) format for config files. The config file consists of sections and each section has options and its respective value\(s\).

Refer to the [TOML documentation](https://toml.io/en/) for detailed usage guidance. In case of parsing errors, validate the config using [TOML linter](https://www.toml-lint.com/).

The general configuration structure has the following pattern:               [section1]     option1="value"          [section2]     option2=["value1","value2"]     option3=true     

Below are some examples of Grid components configured with a Toml file, the component can be started in the following way:               java -jar selenium-server-<version>.jar <component> --config /path/to/file/<file-name>.toml     

### Standalone

A Standalone server, running on port 4449, and a new session request timeout of 500 seconds.               [server]     port = 4449          [sessionqueue]     session-request-timeout = 500     

### Specific browsers and a limit of max sessions

A Standalone server or a Node which only has Firefox and Chrome enabled by default.               [node]     drivers = ["chrome", "firefox"]     max-sessions = 3     

### Configuring and customising drivers

Standalone or Node server with customised drivers, which allows things like having Firefox Beta or Nightly, and having different browser versions.               [node]     detect-drivers = false     [[node.driver-configuration]]     max-sessions = 100     display-name = "Firefox Nightly"     stereotype = "{\"browserName\": \"firefox\", \"browserVersion\": \"93\", \"platformName\": \"MAC\", \"moz:firefoxOptions\": {\"binary\": \"/Applications/Firefox Nightly.app/Contents/MacOS/firefox-bin\"}}"     [[node.driver-configuration]]     display-name = "Chrome Beta"     stereotype = "{\"browserName\": \"chrome\", \"browserVersion\": \"94\", \"platformName\": \"MAC\", \"goog:chromeOptions\": {\"binary\": \"/Applications/Google Chrome Beta.app/Contents/MacOS/Google Chrome Beta\"}}"     [[node.driver-configuration]]     display-name = "Chrome Dev"     stereotype = "{\"browserName\": \"chrome\", \"browserVersion\": \"95\", \"platformName\": \"MAC\", \"goog:chromeOptions\": {\"binary\": \"/Applications/Google Chrome Dev.app/Contents/MacOS/Google Chrome Dev\"}}"     webdriver-executable = '/path/to/chromedriver/95/chromedriver'     

### Standalone or Node with Docker

A Standalone or Node server that is able to run each new session in a Docker container. Disabling drivers detection, having maximum 2 concurrent sessions. Stereotypes configured need to be mapped to a Docker image, and the Docker daemon needs to be exposed via http/tcp. In addition, it is possible to define which device files, accessible on the host, will be available in containers through the `devices` property. Refer to the [docker](https://docs.docker.com/engine/reference/commandline/run/#add-host-device-to-container---device) documentation for more information about how docker device mapping works.               [node]     detect-drivers = false     max-sessions = 2          [docker]     configs = [         "selenium/standalone-chrome:93.0", "{\"browserName\": \"chrome\", \"browserVersion\": \"91\"}",          "selenium/standalone-firefox:92.0", "{\"browserName\": \"firefox\", \"browserVersion\": \"92\"}"     ]     #Optionally define all device files that should be mapped to docker containers     #devices = [     #    "/dev/kvm:/dev/kvm"     #]     url = "http://localhost:2375"     video-image = "selenium/video:latest"     

### Relaying commands to a service endpoint that supports WebDriver

It is useful to connect an external service that supports WebDriver to Selenium Grid. An example of such service could be a cloud provider or an Appium server. In this way, Grid can enable more coverage to platforms and versions not present locally.

The following is an en example of connecting an Appium server to Grid.               [node]     detect-drivers = false          [relay]     # Default Appium/Cloud server endpoint     url = "http://localhost:4723/wd/hub"     status-endpoint = "/status"     # Optional, enforce a specific protocol version in HttpClient when communicating with the endpoint service status (e.g. HTTP/1.1, HTTP/2)     protocol-version = "HTTP/1.1"     # Stereotypes supported by the service. The initial number is "max-sessions", and will allocate      # that many test slots to that particular configuration     configs = [       "5", "{\"browserName\": \"chrome\", \"platformName\": \"android\", \"appium:platformVersion\": \"11\"}"     ]     

### Basic auth enabled

It is possible to protect a Grid with basic auth by configuring the Router/Hub/Standalone with a username and password. This user/password combination will be needed when loading the Grid UI or starting a new session.               [router]     username = "admin"     password = "myStrongPassword"     

Here is a Java example showing how to start a session using the configured user and password.               ClientConfig clientConfig = ClientConfig.defaultConfig()       .baseUrl(new URL("http://localhost:4444"))       .authenticateAs(new UsernameAndPassword("admin", "myStrongPassword"));     HttpCommandExecutor executor = new HttpCommandExecutor(clientConfig);     RemoteWebDriver driver = new RemoteWebDriver(executor, new ChromeOptions());     

In other languages, you can use the URL http://admin:myStrongPassword@localhost:4444

### Setting custom capabilities for matching specific Nodes

**Important:** Custom capabilities need to be set in the configuration in all Nodes. They also need to be included always in every session request.               [node]     detect-drivers = false          [[node.driver-configuration]]     display-name = "firefox"     stereotype = '{"browserName": "firefox", "platformName": "macOS", "browserVersion":"96", "networkname:applicationName":"node_1", "nodename:applicationName":"app_1" }'     max-sessions = 5     

Here is a Java example showing how to match that Node               FirefoxOptions options = new FirefoxOptions();     options.setCapability("networkname:applicationName", "node_1");     options.setCapability("nodename:applicationName", "app_1");     options.setBrowserVersion("96");     options.setPlatformName("macOS");     WebDriver driver = new RemoteWebDriver(new URL("http://localhost:4444"), options);     driver.get("https://selenium.dev");     driver.quit();     

### Enabling Managed downloads by the Node.

The Node can be instructed to manage downloads automatically. This will cause the Node to save all files that were downloaded for a particular session into a temp directory, which can later be retrieved from the node. To turn this capability on, use the below configuration:               [node]     enable-managed-downloads = true     

Refer to the [CLI section](https://www.selenium.dev/documentation/grid/configuration/cli_options/#enabling-managed-downloads-by-the-node) for a complete example.

Last modified April 23, 2024: [\[grid\] update list CLI/TOML options \(\#1683\) \(1f27efd060f\)](https://github.com/SeleniumHQ/seleniumhq.github.io/commit/1f27efd060fbacdd93b29416182faa8636bd6604)