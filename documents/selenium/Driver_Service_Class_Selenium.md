# Driver Service Class | Selenium

**URL:** https://www.selenium.dev/documentation/webdriver/drivers/service
**Word Count:** 298
**Links Count:** 231
**Scraped:** 2025-07-17 06:13:36
**Status:** completed

---

# Driver Service Class

The Service classes are for managing the starting and stopping of local drivers. They cannot be used with a Remote WebDriver session.

Service classes allow you to specify information about the driver, like location and which port to use. They also let you specify what arguments get passed to the command line. Most of the useful arguments are related to logging.

## Default Service instance

To start a driver with a default service instance:

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

                  ChromeDriverService service = new ChromeDriverService.Builder().build();         driver = new ChromeDriver(service);

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/java/src/test/java/dev/selenium/drivers/ServiceTest.java#L15-L16)

##### examples/java/src/test/java/dev/selenium/drivers/ServiceTest.java

Copy  Close               package dev.selenium.drivers;          import dev.selenium.BaseTest;     import java.io.File;     import org.junit.jupiter.api.Test;     import org.openqa.selenium.chrome.ChromeDriver;     import org.openqa.selenium.chrome.ChromeDriverService;     import org.openqa.selenium.chrome.ChromeOptions;     import org.openqa.selenium.remote.service.DriverFinder;          public class ServiceTest extends BaseTest {              @Test       public void defaultService() {         ChromeDriverService service = new ChromeDriverService.Builder().build();         driver = new ChromeDriver(service);       }            @Test       public void setDriverLocation() {         setBinaryPaths();         ChromeOptions options = getDefaultChromeOptions();         options.setBinary(browserPath);              ChromeDriverService service =             new ChromeDriverService.Builder().usingDriverExecutable(driverPath).build();              driver = new ChromeDriver(service, options);       }            @Test       public void setPort() {         ChromeDriverService service = new ChromeDriverService.Builder().usingPort(1234).build();              driver = new ChromeDriver(service);       }            private void setBinaryPaths() {         ChromeOptions options = getDefaultChromeOptions();         options.setBrowserVersion("stable");         DriverFinder finder = new DriverFinder(ChromeDriverService.createDefaultService(), options);         driverPath = new File(finder.getDriverPath());         browserPath = new File(finder.getBrowserPath());       }     }     

**Note** : Java Service classes only allow values to be set during construction with a Builder pattern.

[Selenium v4.11](https://github.com/SeleniumHQ/selenium/releases/tag/selenium-4.11.0)                   service = webdriver.ChromeService()         driver = webdriver.Chrome(service=service)

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/drivers/test_service.py#L5-L6)

##### examples/python/tests/drivers/test\_service.py

Copy  Close               from selenium import webdriver               def test_basic_service():         service = webdriver.ChromeService()         driver = webdriver.Chrome(service=service)              driver.quit()               def test_driver_location(chromedriver_bin, chrome_bin):         options = get_default_chrome_options()         options.binary_location = chrome_bin              service = webdriver.ChromeService(executable_path=chromedriver_bin)              driver = webdriver.Chrome(service=service, options=options)              driver.quit()               def test_driver_port():         service = webdriver.ChromeService(port=1234)              driver = webdriver.Chrome(service=service)              driver.quit()          def get_default_chrome_options():         options = webdriver.ChromeOptions()         options.add_argument("--no-sandbox")         return options     

**Note** : Python Service classes only allow values to be set as arguments to the constructor.                           var service = ChromeDriverService.CreateDefaultService();                 driver = new ChromeDriver(service);

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/dotnet/SeleniumDocs/Drivers/ServiceTest.cs#L14-L15)

##### examples/dotnet/SeleniumDocs/Drivers/ServiceTest.cs

Copy  Close               using Microsoft.VisualStudio.TestTools.UnitTesting;     using OpenQA.Selenium;     using OpenQA.Selenium.Chrome;     using SeleniumDocs.TestSupport;          namespace SeleniumDocs.Drivers     {         [TestClass]         public class ServiceTest : BaseTest         {             [TestMethod]             public void BasicService()             {                 var service = ChromeDriverService.CreateDefaultService();                 driver = new ChromeDriver(service);             }                  [TestMethodCustom]             [EnabledOnOs("OSX")]             public void DriverLocation()             {                 var options = GetLatestChromeOptions();                 var service = ChromeDriverService.CreateDefaultService(GetDriverLocation(options));                      driver = new ChromeDriver(service, options);             }                  [TestMethod]             public void DriverPort()             {                 var service = ChromeDriverService.CreateDefaultService();                 service.Port = 1234;                      driver = new ChromeDriver(service);             }                          private static string GetDriverLocation(ChromeOptions options)             {                 return new DriverFinder(options).GetDriverPath();             }                  private static ChromeOptions GetLatestChromeOptions()             {                 return new ChromeOptions                 {                     BrowserVersion = "stable"                 };             }         }     }

**Note** : .NET Service classes allow values to be set as properties.                   service = Selenium::WebDriver::Service.chrome         @driver = Selenium::WebDriver.for :chrome, service: service

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/ruby/spec/drivers/service_spec.rb#L14-L15)

##### examples/ruby/spec/drivers/service\_spec.rb

Copy  Close               # frozen_string_literal: true          require 'spec_helper'          RSpec.describe 'Service' do       let(:file_name) { File.expand_path('driver.log') }       let(:driver_path) { ENV.fetch('CHROMEDRIVER_BIN', nil) }       let(:browser_path) { ENV.fetch('CHROME_BIN', nil) }            before { driver_finder }       after { FileUtils.rm_f(file_name) }            it 'has default service' do         service = Selenium::WebDriver::Service.chrome         @driver = Selenium::WebDriver.for :chrome, service: service       end            it 'specifies driver location' do         user_data_dir = Dir.mktmpdir('chrome-profile-')         options = Selenium::WebDriver::Options.chrome(binary: browser_path)         options.add_argument("--user-data-dir=#{user_data_dir}")         options.add_argument('--no-sandbox')         options.add_argument('--disable-dev-shm-usage')         service = Selenium::WebDriver::Service.chrome              service.executable_path = driver_path              @driver = Selenium::WebDriver.for :chrome, service: service, options: options       end            it 'specifies driver port' do         service = Selenium::WebDriver::Service.chrome         service.port = 1234              @driver = Selenium::WebDriver.for :chrome, service: service       end            def driver_finder         options = Selenium::WebDriver::Options.chrome(browser_version: 'stable')         service = Selenium::WebDriver::Service.chrome         finder = Selenium::WebDriver::DriverFinder.new(options, service)         ENV['CHROMEDRIVER_BIN'] = finder.driver_path         ENV['CHROME_BIN'] = finder.browser_path       end     end     

**Note** : Ruby Service classes allow values to be set either as arguments in the constructor or as attributes.

[Add Example](https://www.selenium.dev/documentation/about/contributing/#creating-examples)

[Add Example](https://www.selenium.dev/documentation/about/contributing/#creating-examples)

## Driver location

**Note:** If you are using Selenium 4.6 or greater, you shouldn’t need to set a driver location. If you cannot update Selenium or have an advanced use case, here is how to specify the driver location:

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

                  ChromeDriverService service =             new ChromeDriverService.Builder().usingDriverExecutable(driverPath).build();

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/java/src/test/java/dev/selenium/drivers/ServiceTest.java#L25-L26)

##### examples/java/src/test/java/dev/selenium/drivers/ServiceTest.java

Copy  Close               package dev.selenium.drivers;          import dev.selenium.BaseTest;     import java.io.File;     import org.junit.jupiter.api.Test;     import org.openqa.selenium.chrome.ChromeDriver;     import org.openqa.selenium.chrome.ChromeDriverService;     import org.openqa.selenium.chrome.ChromeOptions;     import org.openqa.selenium.remote.service.DriverFinder;          public class ServiceTest extends BaseTest {              @Test       public void defaultService() {         ChromeDriverService service = new ChromeDriverService.Builder().build();         driver = new ChromeDriver(service);       }            @Test       public void setDriverLocation() {         setBinaryPaths();         ChromeOptions options = getDefaultChromeOptions();         options.setBinary(browserPath);              ChromeDriverService service =             new ChromeDriverService.Builder().usingDriverExecutable(driverPath).build();              driver = new ChromeDriver(service, options);       }            @Test       public void setPort() {         ChromeDriverService service = new ChromeDriverService.Builder().usingPort(1234).build();              driver = new ChromeDriver(service);       }            private void setBinaryPaths() {         ChromeOptions options = getDefaultChromeOptions();         options.setBrowserVersion("stable");         DriverFinder finder = new DriverFinder(ChromeDriverService.createDefaultService(), options);         driverPath = new File(finder.getDriverPath());         browserPath = new File(finder.getBrowserPath());       }     }     

[Selenium v4.11](https://github.com/SeleniumHQ/selenium/releases/tag/selenium-4.11.0)                   service = webdriver.ChromeService(executable_path=chromedriver_bin)

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/drivers/test_service.py#L15)

##### examples/python/tests/drivers/test\_service.py

Copy  Close               from selenium import webdriver               def test_basic_service():         service = webdriver.ChromeService()         driver = webdriver.Chrome(service=service)              driver.quit()               def test_driver_location(chromedriver_bin, chrome_bin):         options = get_default_chrome_options()         options.binary_location = chrome_bin              service = webdriver.ChromeService(executable_path=chromedriver_bin)              driver = webdriver.Chrome(service=service, options=options)              driver.quit()               def test_driver_port():         service = webdriver.ChromeService(port=1234)              driver = webdriver.Chrome(service=service)              driver.quit()          def get_default_chrome_options():         options = webdriver.ChromeOptions()         options.add_argument("--no-sandbox")         return options     

[Selenium v4.9](https://github.com/SeleniumHQ/selenium/releases/tag/selenium-4.9.0)                           var service = ChromeDriverService.CreateDefaultService(GetDriverLocation(options));

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/dotnet/SeleniumDocs/Drivers/ServiceTest.cs#L23)

##### examples/dotnet/SeleniumDocs/Drivers/ServiceTest.cs

Copy  Close               using Microsoft.VisualStudio.TestTools.UnitTesting;     using OpenQA.Selenium;     using OpenQA.Selenium.Chrome;     using SeleniumDocs.TestSupport;          namespace SeleniumDocs.Drivers     {         [TestClass]         public class ServiceTest : BaseTest         {             [TestMethod]             public void BasicService()             {                 var service = ChromeDriverService.CreateDefaultService();                 driver = new ChromeDriver(service);             }                  [TestMethodCustom]             [EnabledOnOs("OSX")]             public void DriverLocation()             {                 var options = GetLatestChromeOptions();                 var service = ChromeDriverService.CreateDefaultService(GetDriverLocation(options));                      driver = new ChromeDriver(service, options);             }                  [TestMethod]             public void DriverPort()             {                 var service = ChromeDriverService.CreateDefaultService();                 service.Port = 1234;                      driver = new ChromeDriver(service);             }                          private static string GetDriverLocation(ChromeOptions options)             {                 return new DriverFinder(options).GetDriverPath();             }                  private static ChromeOptions GetLatestChromeOptions()             {                 return new ChromeOptions                 {                     BrowserVersion = "stable"                 };             }         }     }

[Selenium v4.8](https://github.com/SeleniumHQ/selenium/releases/tag/selenium-4.8.0)                   service.executable_path = driver_path

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/ruby/spec/drivers/service_spec.rb#L26)

##### examples/ruby/spec/drivers/service\_spec.rb

Copy  Close               # frozen_string_literal: true          require 'spec_helper'          RSpec.describe 'Service' do       let(:file_name) { File.expand_path('driver.log') }       let(:driver_path) { ENV.fetch('CHROMEDRIVER_BIN', nil) }       let(:browser_path) { ENV.fetch('CHROME_BIN', nil) }            before { driver_finder }       after { FileUtils.rm_f(file_name) }            it 'has default service' do         service = Selenium::WebDriver::Service.chrome         @driver = Selenium::WebDriver.for :chrome, service: service       end            it 'specifies driver location' do         user_data_dir = Dir.mktmpdir('chrome-profile-')         options = Selenium::WebDriver::Options.chrome(binary: browser_path)         options.add_argument("--user-data-dir=#{user_data_dir}")         options.add_argument('--no-sandbox')         options.add_argument('--disable-dev-shm-usage')         service = Selenium::WebDriver::Service.chrome              service.executable_path = driver_path              @driver = Selenium::WebDriver.for :chrome, service: service, options: options       end            it 'specifies driver port' do         service = Selenium::WebDriver::Service.chrome         service.port = 1234              @driver = Selenium::WebDriver.for :chrome, service: service       end            def driver_finder         options = Selenium::WebDriver::Options.chrome(browser_version: 'stable')         service = Selenium::WebDriver::Service.chrome         finder = Selenium::WebDriver::DriverFinder.new(options, service)         ENV['CHROMEDRIVER_BIN'] = finder.driver_path         ENV['CHROME_BIN'] = finder.browser_path       end     end     

[Add Example](https://www.selenium.dev/documentation/about/contributing/#creating-examples)

[Add Example](https://www.selenium.dev/documentation/about/contributing/#creating-examples)

## Driver port

If you want the driver to run on a specific port, you may specify it as follows:

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

                  ChromeDriverService service = new ChromeDriverService.Builder().usingPort(1234).build();

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/java/src/test/java/dev/selenium/drivers/ServiceTest.java#L33)

##### examples/java/src/test/java/dev/selenium/drivers/ServiceTest.java

Copy  Close               package dev.selenium.drivers;          import dev.selenium.BaseTest;     import java.io.File;     import org.junit.jupiter.api.Test;     import org.openqa.selenium.chrome.ChromeDriver;     import org.openqa.selenium.chrome.ChromeDriverService;     import org.openqa.selenium.chrome.ChromeOptions;     import org.openqa.selenium.remote.service.DriverFinder;          public class ServiceTest extends BaseTest {              @Test       public void defaultService() {         ChromeDriverService service = new ChromeDriverService.Builder().build();         driver = new ChromeDriver(service);       }            @Test       public void setDriverLocation() {         setBinaryPaths();         ChromeOptions options = getDefaultChromeOptions();         options.setBinary(browserPath);              ChromeDriverService service =             new ChromeDriverService.Builder().usingDriverExecutable(driverPath).build();              driver = new ChromeDriver(service, options);       }            @Test       public void setPort() {         ChromeDriverService service = new ChromeDriverService.Builder().usingPort(1234).build();              driver = new ChromeDriver(service);       }            private void setBinaryPaths() {         ChromeOptions options = getDefaultChromeOptions();         options.setBrowserVersion("stable");         DriverFinder finder = new DriverFinder(ChromeDriverService.createDefaultService(), options);         driverPath = new File(finder.getDriverPath());         browserPath = new File(finder.getBrowserPath());       }     }     

[Selenium v4.11](https://github.com/SeleniumHQ/selenium/releases/tag/selenium-4.11.0)                   service = webdriver.ChromeService(port=1234)

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/drivers/test_service.py#L23)

##### examples/python/tests/drivers/test\_service.py

Copy  Close               from selenium import webdriver               def test_basic_service():         service = webdriver.ChromeService()         driver = webdriver.Chrome(service=service)              driver.quit()               def test_driver_location(chromedriver_bin, chrome_bin):         options = get_default_chrome_options()         options.binary_location = chrome_bin              service = webdriver.ChromeService(executable_path=chromedriver_bin)              driver = webdriver.Chrome(service=service, options=options)              driver.quit()               def test_driver_port():         service = webdriver.ChromeService(port=1234)              driver = webdriver.Chrome(service=service)              driver.quit()          def get_default_chrome_options():         options = webdriver.ChromeOptions()         options.add_argument("--no-sandbox")         return options                                service.Port = 1234;

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/dotnet/SeleniumDocs/Drivers/ServiceTest.cs#L32)

##### examples/dotnet/SeleniumDocs/Drivers/ServiceTest.cs

Copy  Close               using Microsoft.VisualStudio.TestTools.UnitTesting;     using OpenQA.Selenium;     using OpenQA.Selenium.Chrome;     using SeleniumDocs.TestSupport;          namespace SeleniumDocs.Drivers     {         [TestClass]         public class ServiceTest : BaseTest         {             [TestMethod]             public void BasicService()             {                 var service = ChromeDriverService.CreateDefaultService();                 driver = new ChromeDriver(service);             }                  [TestMethodCustom]             [EnabledOnOs("OSX")]             public void DriverLocation()             {                 var options = GetLatestChromeOptions();                 var service = ChromeDriverService.CreateDefaultService(GetDriverLocation(options));                      driver = new ChromeDriver(service, options);             }                  [TestMethod]             public void DriverPort()             {                 var service = ChromeDriverService.CreateDefaultService();                 service.Port = 1234;                      driver = new ChromeDriver(service);             }                          private static string GetDriverLocation(ChromeOptions options)             {                 return new DriverFinder(options).GetDriverPath();             }                  private static ChromeOptions GetLatestChromeOptions()             {                 return new ChromeOptions                 {                     BrowserVersion = "stable"                 };             }         }     }

[Selenium v4.8](https://github.com/SeleniumHQ/selenium/releases/tag/selenium-4.8.0)                   service.port = 1234

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/ruby/spec/drivers/service_spec.rb#L33)

##### examples/ruby/spec/drivers/service\_spec.rb

Copy  Close               # frozen_string_literal: true          require 'spec_helper'          RSpec.describe 'Service' do       let(:file_name) { File.expand_path('driver.log') }       let(:driver_path) { ENV.fetch('CHROMEDRIVER_BIN', nil) }       let(:browser_path) { ENV.fetch('CHROME_BIN', nil) }            before { driver_finder }       after { FileUtils.rm_f(file_name) }            it 'has default service' do         service = Selenium::WebDriver::Service.chrome         @driver = Selenium::WebDriver.for :chrome, service: service       end            it 'specifies driver location' do         user_data_dir = Dir.mktmpdir('chrome-profile-')         options = Selenium::WebDriver::Options.chrome(binary: browser_path)         options.add_argument("--user-data-dir=#{user_data_dir}")         options.add_argument('--no-sandbox')         options.add_argument('--disable-dev-shm-usage')         service = Selenium::WebDriver::Service.chrome              service.executable_path = driver_path              @driver = Selenium::WebDriver.for :chrome, service: service, options: options       end            it 'specifies driver port' do         service = Selenium::WebDriver::Service.chrome         service.port = 1234              @driver = Selenium::WebDriver.for :chrome, service: service       end            def driver_finder         options = Selenium::WebDriver::Options.chrome(browser_version: 'stable')         service = Selenium::WebDriver::Service.chrome         finder = Selenium::WebDriver::DriverFinder.new(options, service)         ENV['CHROMEDRIVER_BIN'] = finder.driver_path         ENV['CHROME_BIN'] = finder.browser_path       end     end     

[Add Example](https://www.selenium.dev/documentation/about/contributing/#creating-examples)

[Add Example](https://www.selenium.dev/documentation/about/contributing/#creating-examples)

## Logging

Logging functionality varies between browsers. Most browsers allow you to specify location and level of logs. Take a look at the respective browser page:

  * [Chrome](https://www.selenium.dev/documentation/webdriver/browsers/chrome/#service)   * [Edge](https://www.selenium.dev/documentation/webdriver/browsers/edge/#service)   * [Firefox](https://www.selenium.dev/documentation/webdriver/browsers/firefox/#service)   * [Internet Explorer](https://www.selenium.dev/documentation/webdriver/browsers/internet_explorer/#service)   * [Safari](https://www.selenium.dev/documentation/webdriver/browsers/safari/#service)

Last modified May 28, 2025: [Update dependency rspec to v3.13.1 \(\#2320\) \(38997fb3970\)](https://github.com/SeleniumHQ/seleniumhq.github.io/commit/38997fb397026763bcc11c239ffc979dbc1fbe11)