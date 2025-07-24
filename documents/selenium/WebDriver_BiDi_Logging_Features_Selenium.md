# WebDriver BiDi Logging Features | Selenium

**URL:** https://www.selenium.dev/documentation/webdriver/bidi/logging
**Word Count:** 225
**Links Count:** 229
**Scraped:** 2025-07-17 06:15:56
**Status:** completed

---

# WebDriver BiDi Logging Features

These features are related to logging. Because “logging” can refer to so many different things, these methods are made available via a “script” namespace.

Remember that to use WebDriver BiDi, you must enable it in Options. For more details, see [Enabling BiDi](https://www.selenium.dev/documentation/webdriver/bidi/)

## Console Message Handlers

Record or take actions on `console.log` events.

### Add Handler

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

[Implementation Missing](https://github.com/SeleniumHQ/selenium)                   driver.script.add_console_message_handler(log_entries.append)

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/python/tests/bidi/test_bidi_logging.py#L11)

##### /examples/python/tests/bidi/test\_bidi\_logging.py

Copy  Close               import pytest     from selenium.webdriver.common.by import By     from selenium.webdriver.support.wait import WebDriverWait               @pytest.mark.driver_type("bidi")     def test_add_console_log_handler(driver):         driver.get('https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html')         log_entries = []              driver.script.add_console_message_handler(log_entries.append)              driver.find_element(By.ID, "consoleLog").click()         WebDriverWait(driver, 5).until(lambda _: log_entries)         assert log_entries[0].text == "Hello, world!"               @pytest.mark.driver_type("bidi")     def test_remove_console_log_handler(driver):         driver.get('https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html')         log_entries = []              id = driver.script.add_console_message_handler(log_entries.append)         driver.script.remove_console_message_handler(id)              driver.find_element(By.ID, "consoleLog").click()         assert len(log_entries) == 0               @pytest.mark.driver_type("bidi")     def test_add_js_exception_handler(driver):         driver.get('https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html')         log_entries = []              driver.script.add_javascript_error_handler(log_entries.append)              driver.find_element(By.ID, "jsException").click()         WebDriverWait(driver, 5).until(lambda _: log_entries)         assert log_entries[0].text == "Error: Not working"               @pytest.mark.driver_type("bidi")     def test_remove_js_exception_handler(driver):         driver.get('https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html')         log_entries = []              id = driver.script.add_javascript_error_handler(log_entries.append)         driver.script.remove_javascript_error_handler(id)              driver.find_element(By.ID, "consoleLog").click()         assert len(log_entries) == 0     

[Implementation Missing](https://github.com/SeleniumHQ/selenium)                   log_entries = []

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/ruby/spec/bidi/logging_spec.rb#L11)

##### /examples/ruby/spec/bidi/logging\_spec.rb

Copy  Close               # frozen_string_literal: true          require 'spec_helper'          RSpec.describe 'Logging' do       let(:driver) { start_bidi_session }       let(:wait) { Selenium::WebDriver::Wait.new(timeout: 2) }            it 'adds console message handler' do         driver.navigate.to 'https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html'         log_entries = []              driver.script.add_console_message_handler { |log| log_entries << log }              driver.find_element(id: 'consoleLog').click         wait.until { log_entries.any? }         expect(log_entries.first&.text).to eq 'Hello, world!'       end            it 'removes console message handler' do         driver.navigate.to 'https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html'         log_entries = []              id = driver.script.add_console_message_handler { |log| log_entries << log }         driver.script.remove_console_message_handler(id)              driver.find_element(id: 'consoleLog').click         expect(log_entries).to be_empty       end            it 'adds JavaScript error handler' do         driver.navigate.to 'https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html'         log_entries = []              driver.script.add_javascript_error_handler { |error| log_entries << error }              driver.find_element(id: 'jsException').click         wait.until { log_entries.any? }         expect(log_entries.first&.text).to eq 'Error: Not working'       end            it 'removes JavaScript error handler' do         driver.navigate.to 'https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html'         log_entries = []              id = driver.script.add_javascript_error_handler { |error| log_entries << error }         driver.script.remove_javascript_error_handler(id)              driver.find_element(id: 'jsException').click         expect(log_entries).to be_empty       end     end     

[Implementation Missing](https://github.com/SeleniumHQ/selenium)

[Implementation Missing](https://github.com/SeleniumHQ/selenium)

### Remove Handler

You need to store the ID returned when adding the handler to delete it.

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

[Implementation Missing](https://github.com/SeleniumHQ/selenium)                   id = driver.script.add_console_message_handler(log_entries.append)         driver.script.remove_console_message_handler(id)

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/python/tests/bidi/test_bidi_logging.py#L23-24)

##### /examples/python/tests/bidi/test\_bidi\_logging.py

Copy  Close               import pytest     from selenium.webdriver.common.by import By     from selenium.webdriver.support.wait import WebDriverWait               @pytest.mark.driver_type("bidi")     def test_add_console_log_handler(driver):         driver.get('https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html')         log_entries = []              driver.script.add_console_message_handler(log_entries.append)              driver.find_element(By.ID, "consoleLog").click()         WebDriverWait(driver, 5).until(lambda _: log_entries)         assert log_entries[0].text == "Hello, world!"               @pytest.mark.driver_type("bidi")     def test_remove_console_log_handler(driver):         driver.get('https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html')         log_entries = []              id = driver.script.add_console_message_handler(log_entries.append)         driver.script.remove_console_message_handler(id)              driver.find_element(By.ID, "consoleLog").click()         assert len(log_entries) == 0               @pytest.mark.driver_type("bidi")     def test_add_js_exception_handler(driver):         driver.get('https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html')         log_entries = []              driver.script.add_javascript_error_handler(log_entries.append)              driver.find_element(By.ID, "jsException").click()         WebDriverWait(driver, 5).until(lambda _: log_entries)         assert log_entries[0].text == "Error: Not working"               @pytest.mark.driver_type("bidi")     def test_remove_js_exception_handler(driver):         driver.get('https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html')         log_entries = []              id = driver.script.add_javascript_error_handler(log_entries.append)         driver.script.remove_javascript_error_handler(id)              driver.find_element(By.ID, "consoleLog").click()         assert len(log_entries) == 0     

[Implementation Missing](https://github.com/SeleniumHQ/selenium)                   log_entries = []     

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/ruby/spec/bidi/logging_spec.rb#L22-L23)

##### /examples/ruby/spec/bidi/logging\_spec.rb

Copy  Close               # frozen_string_literal: true          require 'spec_helper'          RSpec.describe 'Logging' do       let(:driver) { start_bidi_session }       let(:wait) { Selenium::WebDriver::Wait.new(timeout: 2) }            it 'adds console message handler' do         driver.navigate.to 'https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html'         log_entries = []              driver.script.add_console_message_handler { |log| log_entries << log }              driver.find_element(id: 'consoleLog').click         wait.until { log_entries.any? }         expect(log_entries.first&.text).to eq 'Hello, world!'       end            it 'removes console message handler' do         driver.navigate.to 'https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html'         log_entries = []              id = driver.script.add_console_message_handler { |log| log_entries << log }         driver.script.remove_console_message_handler(id)              driver.find_element(id: 'consoleLog').click         expect(log_entries).to be_empty       end            it 'adds JavaScript error handler' do         driver.navigate.to 'https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html'         log_entries = []              driver.script.add_javascript_error_handler { |error| log_entries << error }              driver.find_element(id: 'jsException').click         wait.until { log_entries.any? }         expect(log_entries.first&.text).to eq 'Error: Not working'       end            it 'removes JavaScript error handler' do         driver.navigate.to 'https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html'         log_entries = []              id = driver.script.add_javascript_error_handler { |error| log_entries << error }         driver.script.remove_javascript_error_handler(id)              driver.find_element(id: 'jsException').click         expect(log_entries).to be_empty       end     end     

[Implementation Missing](https://github.com/SeleniumHQ/selenium)

[Implementation Missing](https://github.com/SeleniumHQ/selenium)

## JavaScript Exception Handlers

Record or take actions on JavaScript exception events.

### Add Handler

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

[Implementation Missing](https://github.com/SeleniumHQ/selenium)                   driver.script.add_javascript_error_handler(log_entries.append)

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/python/tests/bidi/test_bidi_logging.py#L35)

##### /examples/python/tests/bidi/test\_bidi\_logging.py

Copy  Close               import pytest     from selenium.webdriver.common.by import By     from selenium.webdriver.support.wait import WebDriverWait               @pytest.mark.driver_type("bidi")     def test_add_console_log_handler(driver):         driver.get('https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html')         log_entries = []              driver.script.add_console_message_handler(log_entries.append)              driver.find_element(By.ID, "consoleLog").click()         WebDriverWait(driver, 5).until(lambda _: log_entries)         assert log_entries[0].text == "Hello, world!"               @pytest.mark.driver_type("bidi")     def test_remove_console_log_handler(driver):         driver.get('https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html')         log_entries = []              id = driver.script.add_console_message_handler(log_entries.append)         driver.script.remove_console_message_handler(id)              driver.find_element(By.ID, "consoleLog").click()         assert len(log_entries) == 0               @pytest.mark.driver_type("bidi")     def test_add_js_exception_handler(driver):         driver.get('https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html')         log_entries = []              driver.script.add_javascript_error_handler(log_entries.append)              driver.find_element(By.ID, "jsException").click()         WebDriverWait(driver, 5).until(lambda _: log_entries)         assert log_entries[0].text == "Error: Not working"               @pytest.mark.driver_type("bidi")     def test_remove_js_exception_handler(driver):         driver.get('https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html')         log_entries = []              id = driver.script.add_javascript_error_handler(log_entries.append)         driver.script.remove_javascript_error_handler(id)              driver.find_element(By.ID, "consoleLog").click()         assert len(log_entries) == 0     

[Implementation Missing](https://github.com/SeleniumHQ/selenium)                   log_entries = []

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/ruby/spec/bidi/logging_spec.rb#L33)

##### /examples/ruby/spec/bidi/logging\_spec.rb

Copy  Close               # frozen_string_literal: true          require 'spec_helper'          RSpec.describe 'Logging' do       let(:driver) { start_bidi_session }       let(:wait) { Selenium::WebDriver::Wait.new(timeout: 2) }            it 'adds console message handler' do         driver.navigate.to 'https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html'         log_entries = []              driver.script.add_console_message_handler { |log| log_entries << log }              driver.find_element(id: 'consoleLog').click         wait.until { log_entries.any? }         expect(log_entries.first&.text).to eq 'Hello, world!'       end            it 'removes console message handler' do         driver.navigate.to 'https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html'         log_entries = []              id = driver.script.add_console_message_handler { |log| log_entries << log }         driver.script.remove_console_message_handler(id)              driver.find_element(id: 'consoleLog').click         expect(log_entries).to be_empty       end            it 'adds JavaScript error handler' do         driver.navigate.to 'https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html'         log_entries = []              driver.script.add_javascript_error_handler { |error| log_entries << error }              driver.find_element(id: 'jsException').click         wait.until { log_entries.any? }         expect(log_entries.first&.text).to eq 'Error: Not working'       end            it 'removes JavaScript error handler' do         driver.navigate.to 'https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html'         log_entries = []              id = driver.script.add_javascript_error_handler { |error| log_entries << error }         driver.script.remove_javascript_error_handler(id)              driver.find_element(id: 'jsException').click         expect(log_entries).to be_empty       end     end     

[Implementation Missing](https://github.com/SeleniumHQ/selenium)

[Implementation Missing](https://github.com/SeleniumHQ/selenium)

### Remove Handler

You need to store the ID returned when adding the handler to delete it.

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

[Implementation Missing](https://github.com/SeleniumHQ/selenium)                   id = driver.script.add_javascript_error_handler(log_entries.append)         driver.script.remove_javascript_error_handler(id)

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/python/tests/bidi/test_bidi_logging.py#L47-48)

##### /examples/python/tests/bidi/test\_bidi\_logging.py

Copy  Close               import pytest     from selenium.webdriver.common.by import By     from selenium.webdriver.support.wait import WebDriverWait               @pytest.mark.driver_type("bidi")     def test_add_console_log_handler(driver):         driver.get('https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html')         log_entries = []              driver.script.add_console_message_handler(log_entries.append)              driver.find_element(By.ID, "consoleLog").click()         WebDriverWait(driver, 5).until(lambda _: log_entries)         assert log_entries[0].text == "Hello, world!"               @pytest.mark.driver_type("bidi")     def test_remove_console_log_handler(driver):         driver.get('https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html')         log_entries = []              id = driver.script.add_console_message_handler(log_entries.append)         driver.script.remove_console_message_handler(id)              driver.find_element(By.ID, "consoleLog").click()         assert len(log_entries) == 0               @pytest.mark.driver_type("bidi")     def test_add_js_exception_handler(driver):         driver.get('https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html')         log_entries = []              driver.script.add_javascript_error_handler(log_entries.append)              driver.find_element(By.ID, "jsException").click()         WebDriverWait(driver, 5).until(lambda _: log_entries)         assert log_entries[0].text == "Error: Not working"               @pytest.mark.driver_type("bidi")     def test_remove_js_exception_handler(driver):         driver.get('https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html')         log_entries = []              id = driver.script.add_javascript_error_handler(log_entries.append)         driver.script.remove_javascript_error_handler(id)              driver.find_element(By.ID, "consoleLog").click()         assert len(log_entries) == 0     

[Implementation Missing](https://github.com/SeleniumHQ/selenium)                   log_entries = []     

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/ruby/spec/bidi/logging_spec.rb#L44-L45)

##### /examples/ruby/spec/bidi/logging\_spec.rb

Copy  Close               # frozen_string_literal: true          require 'spec_helper'          RSpec.describe 'Logging' do       let(:driver) { start_bidi_session }       let(:wait) { Selenium::WebDriver::Wait.new(timeout: 2) }            it 'adds console message handler' do         driver.navigate.to 'https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html'         log_entries = []              driver.script.add_console_message_handler { |log| log_entries << log }              driver.find_element(id: 'consoleLog').click         wait.until { log_entries.any? }         expect(log_entries.first&.text).to eq 'Hello, world!'       end            it 'removes console message handler' do         driver.navigate.to 'https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html'         log_entries = []              id = driver.script.add_console_message_handler { |log| log_entries << log }         driver.script.remove_console_message_handler(id)              driver.find_element(id: 'consoleLog').click         expect(log_entries).to be_empty       end            it 'adds JavaScript error handler' do         driver.navigate.to 'https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html'         log_entries = []              driver.script.add_javascript_error_handler { |error| log_entries << error }              driver.find_element(id: 'jsException').click         wait.until { log_entries.any? }         expect(log_entries.first&.text).to eq 'Error: Not working'       end            it 'removes JavaScript error handler' do         driver.navigate.to 'https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html'         log_entries = []              id = driver.script.add_javascript_error_handler { |error| log_entries << error }         driver.script.remove_javascript_error_handler(id)              driver.find_element(id: 'jsException').click         expect(log_entries).to be_empty       end     end     

[Implementation Missing](https://github.com/SeleniumHQ/selenium)

[Implementation Missing](https://github.com/SeleniumHQ/selenium)

Last modified September 20, 2024: [Fix link text \[deploy site\] \(82bbba5a7a5\)](https://github.com/SeleniumHQ/seleniumhq.github.io/commit/82bbba5a7a58fcf5fefb7e94e8f3e919d5c5585e)