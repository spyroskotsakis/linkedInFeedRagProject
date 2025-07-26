# Avoid sharing state | Selenium

**URL:** https://www.selenium.dev/documentation/test_practices/encouraged/avoid_sharing_state
**Word Count:** 154
**Links Count:** 199
**Scraped:** 2025-07-17 06:13:36
**Status:** completed

---

# Avoid sharing state

Although mentioned in several places, it is worth mentioning again. We must ensure that the tests are isolated from one another.

  * Do not share test data. Imagine several tests that each query the database for valid orders before picking one to perform an action on. Should two tests pick up the same order you are likely to get unexpected behavior.

  * Clean up stale data in the application that might be picked up by another test e.g. invalid order records.

  * Create a new WebDriver instance per test. This helps ensure test isolation and makes parallelization simpler.

    * If you choose [pytest](https://pytest.org/) as your test runner, this can be easily done by yielding your driver in a global fixture. This way each test gets its own driver instance, and you can ensure that drivers always quit after a test is finished \(pass or fail\).

Last modified September 23, 2024: [Added more detail to Avoid Sharing State Documentation \(\#1948\)\[deploy site\] \(e1fa2da1696\)](https://github.com/SeleniumHQ/seleniumhq.github.io/commit/e1fa2da1696971bd7e22f613dce09a8934fd56ff)