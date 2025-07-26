# Waiting with Expected Conditions | Selenium

**URL:** https://www.selenium.dev/documentation/webdriver/support_features/expected_conditions
**Word Count:** 130
**Links Count:** 204
**Scraped:** 2025-07-17 06:13:37
**Status:** completed

---

# Waiting with Expected Conditions

These are classes used to describe what needs to be waited for.

Expected Conditions are used with [Explicit Waits](https://www.selenium.dev/documentation/webdriver/waits/#explicit-waits). Instead of defining the block of code to be executed with a _lambda_ , an expected conditions method can be created to represent common things that get waited on. Some methods take locators as arguments, others take elements as arguments.

These methods can include conditions such as:

  * element exists   * element is stale   * element is visible   * text is visible   * title contains specified value

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

[Expected Conditions Documentation](https://www.selenium.dev/selenium/docs/api/java/org/openqa/selenium/support/ui/ExpectedConditions.html)

[Add Example](https://www.selenium.dev/documentation/about/contributing/#creating-examples)                   wait = WebDriverWait(driver, timeout=2)         wait.until(EC.visibility_of_element_located((By.ID, "revealed")))

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/support/test_expected_conditions.py#L14-L15)

##### examples/python/tests/support/test\_expected\_conditions.py

Copy  Close               from selenium.webdriver.common.by import By     from selenium.webdriver.support import expected_conditions as EC     from selenium.webdriver.support.wait import WebDriverWait          # Expected Conditions API Documentation:     # https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html               def test_expected_condition(driver):         driver.get("https://www.selenium.dev/selenium/web/dynamic.html")         revealed = driver.find_element(By.ID, "revealed")         driver.find_element(By.ID, "reveal").click()              wait = WebDriverWait(driver, timeout=2)         wait.until(EC.visibility_of_element_located((By.ID, "revealed")))              revealed.send_keys("Displayed")         assert revealed.get_property("value") == "Displayed"     

.NET stopped supporting Expected Conditions in Selenium 4 to minimize maintenance hassle and redundancy.

Ruby makes frequent use of blocks, procs and lambdas and does not need Expected Conditions classes

[Add Example](https://www.selenium.dev/documentation/about/contributing/#creating-examples)

[Add Example](https://www.selenium.dev/documentation/about/contributing/#creating-examples)

Last modified April 26, 2025: [Add Expected Conditions example for Python \(\#2286\)\[deploy site\] \(46c35d6afb7\)](https://github.com/SeleniumHQ/seleniumhq.github.io/commit/46c35d6afb77f67b360c60f4e1544e992df014cd)