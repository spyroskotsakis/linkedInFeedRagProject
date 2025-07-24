# Fresh browser per test | Selenium

**URL:** https://www.selenium.dev/documentation/test_practices/encouraged/fresh_browser_per_test
**Word Count:** 74
**Links Count:** 198
**Scraped:** 2025-07-17 06:13:36
**Status:** completed

---

# Fresh browser per test

Start each test from a clean, known state. Ideally, spin up a new virtual machine for each test. If spinning up a new virtual machine is not practical, at least start a new WebDriver for each test. Most browser drivers like GeckoDriver and ChromeDriver will start with a clean known state with a new user profile, by default.               WebDriver driver = new FirefoxDriver();     

Last modified September 4, 2022: [Overview spelling, punctuation fixes \(\#1156\) \(6b87463b637\)](https://github.com/SeleniumHQ/seleniumhq.github.io/commit/6b87463b63700d38146e82130776bf4d832bf82d)