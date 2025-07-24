# Grid 3 | Selenium

**URL:** https://www.selenium.dev/documentation/legacy/selenium_3/grid_3
**Word Count:** 183
**Links Count:** 199
**Scraped:** 2025-07-17 06:15:56
**Status:** completed

---

# Grid 3

Selenium Grid 3 supported WebDriver without Selenium RC code. Grid 3 was completely rewritten for the new Grid 4.

You can read our documentation for more information about [Grid 4](https://www.selenium.dev/documentation/grid/)

 _Selenium Grid_ is a smart proxy server that allows Selenium tests to route commands to remote web browser instances. Its aim is to provide an easy way to run tests in parallel on multiple machines.

With Selenium Grid, one server acts as the hub that routes JSON formatted test commands to one or more registered Grid nodes. Tests contact the hub to obtain access to remote browser instances. The hub has a list of registered servers that it provides access to, and allows control of these instances.

Selenium Grid allows us to run tests in parallel on multiple machines, and to manage different browser versions and browser configurations centrally \(instead of in each individual test\).

Selenium Grid is not a silver bullet. It solves a subset of common delegation and distribution problems, but will for example not manage your infrastructure, and might not suit your specific needs.

Last modified January 10, 2022: [More wiki \(\#907\) \[deploy site\] \(adcf706a1ad\)](https://github.com/SeleniumHQ/seleniumhq.github.io/commit/adcf706a1ad907d028dc57d10201a265972432af)