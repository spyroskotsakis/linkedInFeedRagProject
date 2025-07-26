# Consider using a fluent API | Selenium

**URL:** https://www.selenium.dev/documentation/test_practices/encouraged/consider_using_a_fluent_api
**Word Count:** 102
**Links Count:** 199
**Scraped:** 2025-07-17 06:15:56
**Status:** completed

---

# Consider using a fluent API

Martin Fowler coined the term [“Fluent API”](https://www.martinfowler.com/bliki/FluentInterface.html). Selenium already implements something like this in their `FluentWait` class, which is meant as an alternative to the standard `Wait` class. You could enable the Fluent API design pattern in your page object and then query the Google search page with a code snippet like this one:               driver.get( "http://www.google.com/webhp?hl=en&amp;tab=ww" );     GoogleSearchPage gsp = new GoogleSearchPage(driver);     gsp.setSearchString().clickSearchButton();     

The Google page object class with this fluent behavior might look like this:               public abstract class BasePage {         protected WebDriver driver;              public BasePage(WebDriver driver) {             this.driver = driver;         }     }          public class GoogleSearchPage extends BasePage {         public GoogleSearchPage(WebDriver driver) {             super(driver);             // Generally do not assert within pages or components.             // Effectively throws an exception if the lambda condition is not met.             new WebDriverWait(driver, Duration.ofSeconds(3)).until(d -> d.findElement(By.id("logo")));         }              public GoogleSearchPage setSearchString(String sstr) {             driver.findElement(By.id("gbqfq")).sendKeys(sstr);             return this;         }              public void clickSearchButton() {             driver.findElement(By.id("gbqfb")).click();         }     }     

Last modified May 17, 2023: [Consider Using a Fluent API - Fix usage \(\#1378\) \(332da70d909\)](https://github.com/SeleniumHQ/seleniumhq.github.io/commit/332da70d90970623288d2e98fbcff098b7812995)