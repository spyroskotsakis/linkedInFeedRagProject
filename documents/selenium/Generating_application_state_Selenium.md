# Generating application state | Selenium

**URL:** https://www.selenium.dev/documentation/test_practices/encouraged/generating_application_state
**Word Count:** 124
**Links Count:** 198
**Scraped:** 2025-07-17 06:15:03
**Status:** completed

---

# Generating application state

Selenium should not be used to prepare a test case. All repetitive actions and preparations for a test case, should be done through other methods. For example, most web UIs have authentication \(e.g. a login form\). Eliminating logging in via web browser before every test will improve both the speed and stability of the test. A method should be created to gain access to the AUT\* \(e.g. using an API to login and set a cookie\). Also, creating methods to pre-load data for testing should not be done using Selenium. As mentioned previously, existing APIs should be leveraged to create data for the AUT\*.

\* **AUT** : Application under test

Last modified December 7, 2021: [reorganize documentation and update titles \(\#861\) \[deploy site\] \(872174bfdd8\)](https://github.com/SeleniumHQ/seleniumhq.github.io/commit/872174bfdd83abf0446f796914acf3e875eeddc6)