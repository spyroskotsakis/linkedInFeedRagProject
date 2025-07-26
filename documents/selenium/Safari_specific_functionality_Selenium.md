# Safari specific functionality | Selenium

**URL:** https://www.selenium.dev/documentation/webdriver/browsers/safari
**Word Count:** 388
**Links Count:** 229
**Scraped:** 2025-07-17 06:15:56
**Status:** completed

---

# Safari specific functionality

These are capabilities and features specific to Apple Safari browsers.

Unlike Chromium and Firefox drivers, the safaridriver is installed with the Operating System. To enable automation on Safari, run the following command from the terminal:               safaridriver --enable     

## Options

Capabilities common to all browsers are described on the [Options page](https://www.selenium.dev/documentation/webdriver/drivers/options/).

Capabilities unique to Safari can be found at Apple’s page [About WebDriver for Safari](https://developer.apple.com/documentation/webkit/about_webdriver_for_safari#2957227)

Starting a Safari session with basic defined options looks like this:

[Move Code](https://www.selenium.dev/documentation/about/contributing/#moving-examples)

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

                      SafariOptions options = new SafariOptions();             driver = new SafariDriver(options);

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/java/src/test/java/dev/selenium/browsers/SafariTest.java#24-L25)

##### /examples/java/src/test/java/dev/selenium/browsers/SafariTest.java

Copy  Close               package dev.selenium.browsers;          import org.junit.jupiter.api.AfterEach;     import org.junit.jupiter.api.Test;     import org.junit.jupiter.api.condition.EnabledOnOs;     import org.junit.jupiter.api.condition.OS;     import org.openqa.selenium.safari.SafariDriver;     import org.openqa.selenium.safari.SafariDriverService;     import org.openqa.selenium.safari.SafariOptions;          @EnabledOnOs(OS.MAC)     public class SafariTest {         public SafariDriver driver;              @AfterEach         public void quit() {             if (driver != null) {                 driver.quit();             }         }              @Test         public void basicOptions() {             SafariOptions options = new SafariOptions();             driver = new SafariDriver(options);         }              @Test         public void enableLogs() {             SafariDriverService service = new SafariDriverService.Builder()                     .withLogging(true)                     .build();                  driver = new SafariDriver(service);         }                  public void safariTechnologyPreview() {             SafariOptions options = new SafariOptions();             options.setUseTechnologyPreview(true);             driver = new SafariDriver(options);         }     }                        options = webdriver.SafariOptions()         driver = webdriver.Safari(options=options)

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/python/tests/browsers/test_safari.py#L9-L10)

##### /examples/python/tests/browsers/test\_safari.py

Copy  Close               import sys          import pytest     from selenium import webdriver               @pytest.mark.skipif(sys.platform != "darwin", reason="requires Mac")     def test_basic_options():         options = webdriver.SafariOptions()         driver = webdriver.Safari(options=options)              driver.quit()               @pytest.mark.skipif(sys.platform != "darwin", reason="requires Mac")     def test_enable_logging():         service = webdriver.SafariService(enable_logging=True)              driver = webdriver.Safari(service=service)              driver.quit()          @pytest.mark.skip(reason="Not installed on Mac GitHub Actions Runner Image")     def test_technology_preview():         options = webdriver.SafariOptions()         options.use_technology_preview = True         service = webdriver.SafariService(             executable_path='/Applications/Safari Technology Preview.app/Contents/MacOS/safaridriver'         )         driver = webdriver.Safari(options=options, service=service)              driver.quit()                                     var options = new SafariOptions();                 driver = new SafariDriver(options);

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/dotnet/SeleniumDocs/Browsers/SafariTest.cs#L22-L23)

##### /examples/dotnet/SeleniumDocs/Browsers/SafariTest.cs

Copy  Close               using Microsoft.VisualStudio.TestTools.UnitTesting;     using OpenQA.Selenium.Safari;     using SeleniumDocs.TestSupport;          namespace SeleniumDocs.Browsers     {         [TestClassCustom]         [EnabledOnOs("OSX")]         public class SafariTest         {             private SafariDriver driver;                  [TestCleanup]             public void QuitDriver()             {                 driver.Quit();             }                  [TestMethod]             public void BasicOptions()             {                 var options = new SafariOptions();                 driver = new SafariDriver(options);             }                  [TestMethod]             [Ignore("Not implemented")]             public void EnableLogs()             {                 var service = SafariDriverService.CreateDefaultService();                      //service.EnableLogging = true;                      driver = new SafariDriver(service);             }         }     }                   it 'basic options' do           options = Selenium::WebDriver::Options.safari

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/ruby/spec/browsers/safari_spec.rb#L8-L9)

##### /examples/ruby/spec/browsers/safari\_spec.rb

Copy  Close               # frozen_string_literal: true          require 'spec_helper'          # rubocop:disable RSpec/MultipleDescribes     RSpec.describe 'Safari', exclusive: {platform: :macosx} do       describe 'Options' do         it 'basic options' do           options = Selenium::WebDriver::Options.safari           @driver = Selenium::WebDriver.for :safari, options: options         end       end            describe 'Service' do         let(:directory) { "#{Dir.home}/Library/Logs/com.apple.WebDriver/*" }              it 'enables logs' do           original_count = Dir[directory].length           service = Selenium::WebDriver::Service.safari                service.args << '--diagnose'                @driver = Selenium::WebDriver.for :safari, service: service           expect(Dir[directory].length - original_count).to eq 1         end              it 'does not set log output' do           service = Selenium::WebDriver::Service.safari                expect {             service.log = $stdout           }.to raise_error(Selenium::WebDriver::Error::WebDriverError, /Safari Service does not support setting log output/)         end       end     end          RSpec.describe 'Safari Technology Preview', skip: 'This test is being skipped as GitHub Actions ' \                                                       'have no support for Safari Technology Preview' do       it 'sets the technology preview' do         Selenium::WebDriver::Safari.technology_preview!         local_driver = Selenium::WebDriver.for :safari         expect(local_driver.capabilities.browser_name).to eq 'Safari Technology Preview'       end     end     # rubocop:enable RSpec/MultipleDescribes                        let driver = new Builder()           .forBrowser(Browser.SAFARI)           .setSafariOptions(options)           .build();

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/javascript/test/browser/safariSpecificCap.spec.js#L8-L11)

##### /examples/javascript/test/browser/safariSpecificCap.spec.js

Copy  Close               const safari = require('selenium-webdriver/safari');     const {Browser, Builder} = require("selenium-webdriver");     const options = new safari.Options();     const process  =  require('node:process');          describe('Should be able to Test Command line arguments', function () {       (process.platform === 'darwin' ? it : it.skip)('headless', async function () {         let driver = new Builder()           .forBrowser(Browser.SAFARI)           .setSafariOptions(options)           .build();              await driver.get('https://www.selenium.dev/selenium/web/blank.html');         await driver.quit();       });     });                 val options = SafariOptions()       val driver = SafariDriver(options)

### Mobile

Those looking to automate Safari on iOS should look to the [Appium project](https://www.selenium.dev/).

## Service

Service settings common to all browsers are described on the [Service page](https://www.selenium.dev/documentation/webdriver/drivers/service/).

### Logging

Unlike other browsers, Safari doesn’t let you choose where logs are output, or change levels. The one option available is to turn logs off or on. If logs are toggled on, they can be found at:`~/Library/Logs/com.apple.WebDriver/`.

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

[Selenium v4.10](https://github.com/SeleniumHQ/selenium/releases/tag/selenium-4.10.0)                               .withLogging(true)

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/java/src/test/java/dev/selenium/browsers/SafariTest.java#L31)

##### examples/java/src/test/java/dev/selenium/browsers/SafariTest.java

Copy  Close               package dev.selenium.browsers;          import org.junit.jupiter.api.AfterEach;     import org.junit.jupiter.api.Test;     import org.junit.jupiter.api.condition.EnabledOnOs;     import org.junit.jupiter.api.condition.OS;     import org.openqa.selenium.safari.SafariDriver;     import org.openqa.selenium.safari.SafariDriverService;     import org.openqa.selenium.safari.SafariOptions;          @EnabledOnOs(OS.MAC)     public class SafariTest {         public SafariDriver driver;              @AfterEach         public void quit() {             if (driver != null) {                 driver.quit();             }         }              @Test         public void basicOptions() {             SafariOptions options = new SafariOptions();             driver = new SafariDriver(options);         }              @Test         public void enableLogs() {             SafariDriverService service = new SafariDriverService.Builder()                     .withLogging(true)                     .build();                  driver = new SafariDriver(service);         }                  public void safariTechnologyPreview() {             SafariOptions options = new SafariOptions();             options.setUseTechnologyPreview(true);             driver = new SafariDriver(options);         }     }     

**Note** : Java also allows setting console output by System Property;   Property key: `SafariDriverService.SAFARI_DRIVER_LOGGING`   Property value: `"true"` or `"false"`

[Selenium v4.26](https://github.com/SeleniumHQ/selenium/releases/tag/selenium-4.26.0)                   service = webdriver.SafariService(enable_logging=True)

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/browsers/test_safari.py#L17)

##### examples/python/tests/browsers/test\_safari.py

Copy  Close               import sys          import pytest     from selenium import webdriver               @pytest.mark.skipif(sys.platform != "darwin", reason="requires Mac")     def test_basic_options():         options = webdriver.SafariOptions()         driver = webdriver.Safari(options=options)              driver.quit()               @pytest.mark.skipif(sys.platform != "darwin", reason="requires Mac")     def test_enable_logging():         service = webdriver.SafariService(enable_logging=True)              driver = webdriver.Safari(service=service)              driver.quit()          @pytest.mark.skip(reason="Not installed on Mac GitHub Actions Runner Image")     def test_technology_preview():         options = webdriver.SafariOptions()         options.use_technology_preview = True         service = webdriver.SafariService(             executable_path='/Applications/Safari Technology Preview.app/Contents/MacOS/safaridriver'         )         driver = webdriver.Safari(options=options, service=service)              driver.quit()          

[Implementation Missing](https://github.com/SeleniumHQ/selenium)

[Selenium v4.8](https://github.com/SeleniumHQ/selenium/releases/tag/selenium-4.8.0)

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/ruby/spec/browsers/safari_spec.rb#L20)

##### examples/ruby/spec/browsers/safari\_spec.rb

Copy  Close               # frozen_string_literal: true          require 'spec_helper'          # rubocop:disable RSpec/MultipleDescribes     RSpec.describe 'Safari', exclusive: {platform: :macosx} do       describe 'Options' do         it 'basic options' do           options = Selenium::WebDriver::Options.safari           @driver = Selenium::WebDriver.for :safari, options: options         end       end            describe 'Service' do         let(:directory) { "#{Dir.home}/Library/Logs/com.apple.WebDriver/*" }              it 'enables logs' do           original_count = Dir[directory].length           service = Selenium::WebDriver::Service.safari                service.args << '--diagnose'                @driver = Selenium::WebDriver.for :safari, service: service           expect(Dir[directory].length - original_count).to eq 1         end              it 'does not set log output' do           service = Selenium::WebDriver::Service.safari                expect {             service.log = $stdout           }.to raise_error(Selenium::WebDriver::Error::WebDriverError, /Safari Service does not support setting log output/)         end       end     end          RSpec.describe 'Safari Technology Preview', skip: 'This test is being skipped as GitHub Actions ' \                                                       'have no support for Safari Technology Preview' do       it 'sets the technology preview' do         Selenium::WebDriver::Safari.technology_preview!         local_driver = Selenium::WebDriver.for :safari         expect(local_driver.capabilities.browser_name).to eq 'Safari Technology Preview'       end     end     # rubocop:enable RSpec/MultipleDescribes     

[Add Example](https://www.selenium.dev/documentation/about/contributing/#creating-examples)

[Add Example](https://www.selenium.dev/documentation/about/contributing/#creating-examples)

## Safari Technology Preview

Apple provides a development version of their browser — [Safari Technology Preview](https://developer.apple.com/safari/technology-preview/)

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

                      options.setUseTechnologyPreview(true);             driver = new SafariDriver(options);

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/java/src/test/java/dev/selenium/browsers/SafariTest.java#L39-L40)

##### examples/java/src/test/java/dev/selenium/browsers/SafariTest.java

Copy  Close               package dev.selenium.browsers;          import org.junit.jupiter.api.AfterEach;     import org.junit.jupiter.api.Test;     import org.junit.jupiter.api.condition.EnabledOnOs;     import org.junit.jupiter.api.condition.OS;     import org.openqa.selenium.safari.SafariDriver;     import org.openqa.selenium.safari.SafariDriverService;     import org.openqa.selenium.safari.SafariOptions;          @EnabledOnOs(OS.MAC)     public class SafariTest {         public SafariDriver driver;              @AfterEach         public void quit() {             if (driver != null) {                 driver.quit();             }         }              @Test         public void basicOptions() {             SafariOptions options = new SafariOptions();             driver = new SafariDriver(options);         }              @Test         public void enableLogs() {             SafariDriverService service = new SafariDriverService.Builder()                     .withLogging(true)                     .build();                  driver = new SafariDriver(service);         }                  public void safariTechnologyPreview() {             SafariOptions options = new SafariOptions();             options.setUseTechnologyPreview(true);             driver = new SafariDriver(options);         }     }                        options = webdriver.SafariOptions()         options.use_technology_preview = True         service = webdriver.SafariService(             executable_path='/Applications/Safari Technology Preview.app/Contents/MacOS/safaridriver'         )         driver = webdriver.Safari(options=options, service=service)

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/browsers/test_safari.py#L25-L30)

##### examples/python/tests/browsers/test\_safari.py

Copy  Close               import sys          import pytest     from selenium import webdriver               @pytest.mark.skipif(sys.platform != "darwin", reason="requires Mac")     def test_basic_options():         options = webdriver.SafariOptions()         driver = webdriver.Safari(options=options)              driver.quit()               @pytest.mark.skipif(sys.platform != "darwin", reason="requires Mac")     def test_enable_logging():         service = webdriver.SafariService(enable_logging=True)              driver = webdriver.Safari(service=service)              driver.quit()          @pytest.mark.skip(reason="Not installed on Mac GitHub Actions Runner Image")     def test_technology_preview():         options = webdriver.SafariOptions()         options.use_technology_preview = True         service = webdriver.SafariService(             executable_path='/Applications/Safari Technology Preview.app/Contents/MacOS/safaridriver'         )         driver = webdriver.Safari(options=options, service=service)              driver.quit()          

[Add Example](https://www.selenium.dev/documentation/about/contributing/#creating-examples)                                                                 'have no support for Safari Technology Preview' do       it 'sets the technology preview' do

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/ruby/spec/browsers/safari_spec.rb#L38-L39)

##### examples/ruby/spec/browsers/safari\_spec.rb

Copy  Close               # frozen_string_literal: true          require 'spec_helper'          # rubocop:disable RSpec/MultipleDescribes     RSpec.describe 'Safari', exclusive: {platform: :macosx} do       describe 'Options' do         it 'basic options' do           options = Selenium::WebDriver::Options.safari           @driver = Selenium::WebDriver.for :safari, options: options         end       end            describe 'Service' do         let(:directory) { "#{Dir.home}/Library/Logs/com.apple.WebDriver/*" }              it 'enables logs' do           original_count = Dir[directory].length           service = Selenium::WebDriver::Service.safari                service.args << '--diagnose'                @driver = Selenium::WebDriver.for :safari, service: service           expect(Dir[directory].length - original_count).to eq 1         end              it 'does not set log output' do           service = Selenium::WebDriver::Service.safari                expect {             service.log = $stdout           }.to raise_error(Selenium::WebDriver::Error::WebDriverError, /Safari Service does not support setting log output/)         end       end     end          RSpec.describe 'Safari Technology Preview', skip: 'This test is being skipped as GitHub Actions ' \                                                       'have no support for Safari Technology Preview' do       it 'sets the technology preview' do         Selenium::WebDriver::Safari.technology_preview!         local_driver = Selenium::WebDriver.for :safari         expect(local_driver.capabilities.browser_name).to eq 'Safari Technology Preview'       end     end     # rubocop:enable RSpec/MultipleDescribes     

[Add Example](https://www.selenium.dev/documentation/about/contributing/#creating-examples)

[Add Example](https://www.selenium.dev/documentation/about/contributing/#creating-examples)

Last modified January 7, 2025: [\[py\] use \`enable\_logging\` for Safari logging \(\#2123\)\[deploy site\] \(8f041763d9e\)](https://github.com/SeleniumHQ/seleniumhq.github.io/commit/8f041763d9e2a97cacc4a24ff86d92f0466ab11f)