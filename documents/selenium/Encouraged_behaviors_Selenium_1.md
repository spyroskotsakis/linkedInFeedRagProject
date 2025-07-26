# Encouraged behaviors | Selenium

**URL:** https://www.selenium.dev/documentation/test_practices/encouraged/_print
**Word Count:** 3588
**Links Count:** 66
**Scraped:** 2025-07-17 06:17:48
**Status:** completed

---

This is the multi-page printable view of this section. Click here to print.

[Return to the regular view of this page](https://www.selenium.dev/documentation/test_practices/encouraged/).

# Encouraged behaviors

Some guidelines and recommendations on testing from the Selenium project.

  * 1: Page object models   * 2: Domain specific language   * 3: Generating application state   * 4: Mock external services   * 5: Improved reporting   * 6: Avoid sharing state   * 7: Tips on working with locators   * 8: Test independency   * 9: Consider using a fluent API   * 10: Fresh browser per test

A note on “Best Practices”: We’ve intentionally avoided the phrase “Best Practices” in this documentation. No one approach works for all situations. We prefer the idea of “Guidelines and Recommendations”. We encourage you to read through these and thoughtfully decide what approaches will work for you in your particular environment.

Functional testing is difficult to get right for many reasons. As if application state, complexity, and dependencies do not make testing difficult enough, dealing with browsers \(especially with cross-browser incompatibilities\) makes writing good tests a challenge.

Selenium provides tools to make functional user interaction easier, but does not help you write well-architected test suites. In this chapter we offer advice, guidelines, and recommendations on how to approach functional web page automation.

This chapter records software design patterns popular amongst many of the users of Selenium that have proven successful over the years.

# 1 - Page object models

Note: this page has merged contents from multiple sources, including the [Selenium wiki](https://github.com/SeleniumHQ/selenium/wiki/PageObjects)

## Overview

Within your web app’s UI, there are areas where your tests interact with. A Page Object only models these as objects within the test code. This reduces the amount of duplicated code and means that if the UI changes, the fix needs only to be applied in one place.

Page Object is a Design Pattern that has become popular in test automation for enhancing test maintenance and reducing code duplication. A page object is an object-oriented class that serves as an interface to a page of your AUT. The tests then use the methods of this page object class whenever they need to interact with the UI of that page. The benefit is that if the UI changes for the page, the tests themselves don’t need to change, only the code within the page object needs to change. Subsequently, all changes to support that new UI are located in one place.

### Advantages

  * There is a clean separation between the test code and page-specific code, such as locators \(or their use if you’re using a UI Map\) and layout.   * There is a single repository for the services or operations the page offers rather than having these services scattered throughout the tests.

In both cases, this allows any modifications required due to UI changes to all be made in one place. Helpful information on this technique can be found on numerous blogs as this ‘test design pattern’ is becoming widely used. We encourage readers who wish to know more to search the internet for blogs on this subject. Many have written on this design pattern and can provide helpful tips beyond the scope of this user guide. To get you started, we’ll illustrate page objects with a simple example.

### Examples

First, consider an example, typical of test automation, that does not use a page object:               /***      * Tests login feature      */     public class Login {            public void testLogin() {         // fill login data on sign-in page         driver.findElement(By.name("user_name")).sendKeys("userName");         driver.findElement(By.name("password")).sendKeys("my supersecret password");         driver.findElement(By.name("sign-in")).click();              // verify h1 tag is "Hello userName" after login         driver.findElement(By.tagName("h1")).isDisplayed();         assertThat(driver.findElement(By.tagName("h1")).getText(), is("Hello userName"));       }     }     

There are two problems with this approach.

  * There is no separation between the test method and the AUT’s locators \(IDs in this example\); both are intertwined in a single method. If the AUT’s UI changes its identifiers, layout, or how a login is input and processed, the test itself must change.   * The ID-locators would be spread in multiple tests, in all tests that had to use this login page.

Applying the page object techniques, this example could be rewritten like this in the following example of a page object for a Sign-in page.               import org.openqa.selenium.By;     import org.openqa.selenium.WebDriver;          /**      * Page Object encapsulates the Sign-in page.      */     public class SignInPage {       protected WebDriver driver;            // <input name="user_name" type="text" value="">       private By usernameBy = By.name("user_name");       // <input name="password" type="password" value="">       private By passwordBy = By.name("password");       // <input name="sign_in" type="submit" value="SignIn">       private By signinBy = By.name("sign_in");            public SignInPage(WebDriver driver){         this.driver = driver;          if (!driver.getTitle().equals("Sign In Page")) {           throw new IllegalStateException("This is not Sign In Page," +                 " current page is: " + driver.getCurrentUrl());         }       }            /**         * Login as valid user         *         * @param userName         * @param password         * @return HomePage object         */       public HomePage loginValidUser(String userName, String password) {         driver.findElement(usernameBy).sendKeys(userName);         driver.findElement(passwordBy).sendKeys(password);         driver.findElement(signinBy).click();         return new HomePage(driver);       }     }     

and page object for a Home page could look like this.               import org.openqa.selenium.By;     import org.openqa.selenium.WebDriver;          /**      * Page Object encapsulates the Home Page      */     public class HomePage {       protected WebDriver driver;            // <h1>Hello userName</h1>       private By messageBy = By.tagName("h1");            public HomePage(WebDriver driver){         this.driver = driver;         if (!driver.getTitle().equals("Home Page of logged in user")) {           throw new IllegalStateException("This is not Home Page of logged in user," +                 " current page is: " + driver.getCurrentUrl());         }       }            /**         * Get message (h1 tag)         *         * @return String message text         */       public String getMessageText() {         return driver.findElement(messageBy).getText();       }            public HomePage manageProfile() {         // Page encapsulation to manage profile functionality         return new HomePage(driver);       }       /* More methods offering the services represented by Home Page       of Logged User. These methods in turn might return more Page Objects       for example click on Compose mail button could return ComposeMail class object */     }     

So now, the login test would use these two page objects as follows.               /***      * Tests login feature      */     public class TestLogin {            @Test       public void testLogin() {         SignInPage signInPage = new SignInPage(driver);         HomePage homePage = signInPage.loginValidUser("userName", "password");         assertThat(homePage.getMessageText(), is("Hello userName"));       }          }     

There is a lot of flexibility in how the page objects may be designed, but there are a few basic rules for getting the desired maintainability of your test code.

## Assertions in Page Objects

Page objects themselves should never make verifications or assertions. This is part of your test and should always be within the test’s code, never in a page object. The page object will contain the representation of the page, and the services the page provides via methods but no code related to what is being tested should be within the page object.

There is one, single, verification which can, and should, be within the page object and that is to verify that the page, and possibly critical elements on the page, were loaded correctly. This verification should be done while instantiating the page object. In the examples above, both the SignInPage and HomePage constructors check that the expected page is available and ready for requests from the test.

## Page Component Objects

A page object does not necessarily need to represent all the parts of a page itself. This was [noted by Martin Fowler](https://martinfowler.com/bliki/PageObject.html#footnote-panel-object) in the early days, while first coining the term “panel objects”.

The same principles used for page objects can be used to create “Page _Component_ Objects”, as it was later called, that represent discrete chunks of the page and **can be included in page objects**. These component objects can provide references to the elements inside those discrete chunks, and methods to leverage the functionality or behavior provided by them.

For example, a Products page has multiple products.               <!-- Products Page -->     <div class="header_container">         <span class="title">Products</span>     </div>          <div class="inventory_list">         <div class="inventory_item">         </div>         <div class="inventory_item">         </div>         <div class="inventory_item">         </div>         <div class="inventory_item">         </div>         <div class="inventory_item">         </div>         <div class="inventory_item">         </div>     </div>     

Each product is a component of the Products page.               <!-- Inventory Item -->     <div class="inventory_item">         <div class="inventory_item_name">Backpack</div>         <div class="pricebar">             <div class="inventory_item_price">$29.99</div>             <button id="add-to-cart-backpack">Add to cart</button>         </div>     </div>     

The Products page HAS-A list of products. This object relationship is called Composition. In simpler terms, something is _composed of_ another thing.               public abstract class BasePage {         protected WebDriver driver;              public BasePage(WebDriver driver) {             this.driver = driver;         }     }          // Page Object     public class ProductsPage extends BasePage {         public ProductsPage(WebDriver driver) {             super(driver);             // No assertions, throws an exception if the element is not loaded             new WebDriverWait(driver, Duration.ofSeconds(3))                 .until(d -> d.findElement(By.className​("header_container")));         }              // Returning a list of products is a service of the page         public List<Product> getProducts() {             return driver.findElements(By.className​("inventory_item"))                 .stream()                 .map(e -> new Product(e)) // Map WebElement to a product component                 .toList();         }              // Return a specific product using a boolean-valued function (predicate)         // This is the behavioral Strategy Pattern from GoF         public Product getProduct(Predicate<Product> condition) {             return getProducts()                 .stream()                 .filter(condition) // Filter by product name or price                 .findFirst()                 .orElseThrow();         }     }     

The Product component object is used inside the Products page object.               public abstract class BaseComponent {         protected WebElement root;              public BaseComponent(WebElement root) {             this.root = root;         }     }          // Page Component Object     public class Product extends BaseComponent {         // The root element contains the entire component         public Product(WebElement root) {             super(root); // inventory_item         }              public String getName() {             // Locating an element begins at the root of the component             return root.findElement(By.className("inventory_item_name")).getText();         }              public BigDecimal getPrice() {             return new BigDecimal(                     root.findElement(By.className("inventory_item_price"))                         .getText()                         .replace("$", "")                 ).setScale(2, RoundingMode.UNNECESSARY); // Sanitation and formatting         }              public void addToCart() {             root.findElement(By.id("add-to-cart-backpack")).click();         }     }     

So now, the products test would use the page object and the page component object as follows.               public class ProductsTest {         @Test         public void testProductInventory() {             var productsPage = new ProductsPage(driver); // page object             var products = productsPage.getProducts();             assertEquals(6, products.size()); // expected, actual         }                  @Test         public void testProductPrices() {             var productsPage = new ProductsPage(driver);                  // Pass a lambda expression (predicate) to filter the list of products             // The predicate or "strategy" is the behavior passed as parameter             var backpack = productsPage.getProduct(p -> p.getName().equals("Backpack")); // page component object             var bikeLight = productsPage.getProduct(p -> p.getName().equals("Bike Light"));                  assertEquals(new BigDecimal("29.99"), backpack.getPrice());             assertEquals(new BigDecimal("9.99"), bikeLight.getPrice());         }     }     

The page and component are represented by their own objects. Both objects only have methods for the **services** they offer, which matches the real-world application in object-oriented programming.

You can even nest component objects inside other component objects for more complex pages. If a page in the AUT has multiple components, or common components used throughout the site \(e.g. a navigation bar\), then it may improve maintainability and reduce code duplication.

## Other Design Patterns Used in Testing

There are other design patterns that also may be used in testing. Discussing all of these is beyond the scope of this user guide. Here, we merely want to introduce the concepts to make the reader aware of some of the things that can be done. As was mentioned earlier, many have blogged on this topic and we encourage the reader to search for blogs on these topics.

## Implementation Notes

PageObjects can be thought of as facing in two directions simultaneously. Facing toward the developer of a test, they represent the **services** offered by a particular page. Facing away from the developer, they should be the only thing that has a deep knowledge of the structure of the HTML of a page \(or part of a page\) It’s simplest to think of the methods on a Page Object as offering the “services” that a page offers rather than exposing the details and mechanics of the page. As an example, think of the inbox of any web-based email system. Amongst the services it offers are the ability to compose a new email, choose to read a single email, and list the subject lines of the emails in the inbox. How these are implemented shouldn’t matter to the test.

Because we’re encouraging the developer of a test to try and think about the services they’re interacting with rather than the implementation, PageObjects should seldom expose the underlying WebDriver instance. To facilitate this, **methods on the PageObject should return other PageObjects**. This means we can effectively model the user’s journey through our application. It also means that should the way that pages relate to one another change \(like when the login page asks the user to change their password the first time they log into a service when it previously didn’t do that\), simply changing the appropriate method’s signature will cause the tests to fail to compile. Put another way; we can tell which tests would fail without needing to run them when we change the relationship between pages and reflect this in the PageObjects.

One consequence of this approach is that it may be necessary to model \(for example\) both a successful and unsuccessful login; or a click could have a different result depending on the app’s state. When this happens, it is common to have multiple methods on the PageObject:               public class LoginPage {         public HomePage loginAs(String username, String password) {             // ... clever magic happens here         }                  public LoginPage loginAsExpectingError(String username, String password) {             //  ... failed login here, maybe because one or both of the username and password are wrong         }                  public String getErrorMessage() {             // So we can verify that the correct error is shown         }     }     

The code presented above shows an important point: the tests, not the PageObjects, should be responsible for making assertions about the state of a page. For example:               public void testMessagesAreReadOrUnread() {         Inbox inbox = new Inbox(driver);         inbox.assertMessageWithSubjectIsUnread("I like cheese");         inbox.assertMessageWithSubjectIsNotUnread("I'm not fond of tofu");     }     

could be re-written as:               public void testMessagesAreReadOrUnread() {         Inbox inbox = new Inbox(driver);         assertTrue(inbox.isMessageWithSubjectIsUnread("I like cheese"));         assertFalse(inbox.isMessageWithSubjectIsUnread("I'm not fond of tofu"));     }     

Of course, as with every guideline, there are exceptions, and one that is commonly seen with PageObjects is to check that the WebDriver is on the correct page when we instantiate the PageObject. This is done in the example below.

Finally, a PageObject need not represent an entire page. It may represent a section that appears frequently within a site or page, such as site navigation. The essential principle is that there is only one place in your test suite with knowledge of the structure of the HTML of a particular \(part of a\) page.

## Summary

  * The public methods represent the services that the page offers   * Try not to expose the internals of the page   * Generally don’t make assertions   * Methods return other PageObjects   * Need not represent an entire page   * Different results for the same action are modelled as different methods

## Example               public class LoginPage {         private final WebDriver driver;              public LoginPage(WebDriver driver) {             this.driver = driver;                  // Check that we're on the right page.             if (!"Login".equals(driver.getTitle())) {                 // Alternatively, we could navigate to the login page, perhaps logging out first                 throw new IllegalStateException("This is not the login page");             }         }              // The login page contains several HTML elements that will be represented as WebElements.         // The locators for these elements should only be defined once.             By usernameLocator = By.id("username");             By passwordLocator = By.id("passwd");             By loginButtonLocator = By.id("login");              // The login page allows the user to type their username into the username field         public LoginPage typeUsername(String username) {             // This is the only place that "knows" how to enter a username             driver.findElement(usernameLocator).sendKeys(username);                  // Return the current page object as this action doesn't navigate to a page represented by another PageObject             return this;	         }              // The login page allows the user to type their password into the password field         public LoginPage typePassword(String password) {             // This is the only place that "knows" how to enter a password             driver.findElement(passwordLocator).sendKeys(password);                  // Return the current page object as this action doesn't navigate to a page represented by another PageObject             return this;	         }              // The login page allows the user to submit the login form         public HomePage submitLogin() {             // This is the only place that submits the login form and expects the destination to be the home page.             // A seperate method should be created for the instance of clicking login whilst expecting a login failure.              driver.findElement(loginButtonLocator).submit();                  // Return a new page object representing the destination. Should the login page ever             // go somewhere else (for example, a legal disclaimer) then changing the method signature             // for this method will mean that all tests that rely on this behaviour won't compile.             return new HomePage(driver);	         }              // The login page allows the user to submit the login form knowing that an invalid username and / or password were entered         public LoginPage submitLoginExpectingFailure() {             // This is the only place that submits the login form and expects the destination to be the login page due to login failure.             driver.findElement(loginButtonLocator).submit();                  // Return a new page object representing the destination. Should the user ever be navigated to the home page after submiting a login with credentials              // expected to fail login, the script will fail when it attempts to instantiate the LoginPage PageObject.             return new LoginPage(driver);	         }              // Conceptually, the login page offers the user the service of being able to "log into"         // the application using a user name and password.          public HomePage loginAs(String username, String password) {             // The PageObject methods that enter username, password & submit login have already defined and should not be repeated here.             typeUsername(username);             typePassword(password);             return submitLogin();         }     }     

# 2 - Domain specific language

A domain specific language \(DSL\) is a system which provides the user with an expressive means of solving a problem. It allows a user to interact with the system on their terms – not just programmer-speak.

Your users, in general, do not care how your site looks. They do not care about the decoration, animations, or graphics. They want to use your system to push their new employees through the process with minimal difficulty; they want to book travel to Alaska; they want to configure and buy unicorns at a discount. Your job as tester is to come as close as you can to “capturing” this mind-set. With that in mind, we set about “modeling” the application you are working on, such that the test scripts \(the user’s only pre-release proxy\) “speak” for, and represent the user.

The goal is to use _ubiquitous language_. Rather than referring to “load data into this table” or “click on the third column” it should be possible to use language such as “create a new account” or “order displayed results by name”

With Selenium, DSL is usually represented by methods, written to make the API simple and readable – they enable a report between the developers and the stakeholders \(users, product owners, business intelligence specialists, etc.\).

## Benefits

  * **Readable:** Business stakeholders can understand it.   * **Writable:** Easy to write, avoids unnecessary duplication.   * **Extensible:** Functionality can \(reasonably\) be added without breaking contracts and existing functionality.   * **Maintainable:** By leaving the implementation details out of test cases, you are well-insulated against changes to the AUT\*.

## Further Reading

\(previously located: <https://github.com/SeleniumHQ/selenium/wiki/Domain-Driven-Design>\)

There is a good book on Domain Driven Design by Eric Evans <http://www.amazon.com/exec/obidos/ASIN/0321125215/domainlanguag-20>

And to whet your appetite there’s a useful smaller book available online for download at <http://www.infoq.com/minibooks/domain-driven-design-quickly>

## Java

Here is an example of a reasonable DSL method in Java. For brevity’s sake, it assumes the `driver` object is pre-defined and available to the method.               /**      * Takes a username and password, fills out the fields, and clicks "login".      * @return An instance of the AccountPage      */     public AccountPage loginAsUser(String username, String password) {       WebElement loginField = driver.findElement(By.id("loginField"));       loginField.clear();       loginField.sendKeys(username);            // Fill out the password field. The locator we're using is "By.id", and we should       // have it defined elsewhere in the class.       WebElement passwordField = driver.findElement(By.id("password"));       passwordField.clear();       passwordField.sendKeys(password);            // Click the login button, which happens to have the id "submit".       driver.findElement(By.id("submit")).click();            // Create and return a new instance of the AccountPage (via the built-in Selenium       // PageFactory).       return PageFactory.newInstance(AccountPage.class);     }     

This method completely abstracts the concepts of input fields, buttons, clicking, and even pages from your test code. Using this approach, all a tester has to do is call this method. This gives you a maintenance advantage: if the login fields ever changed, you would only ever have to change this method - not your tests.               public void loginTest() {         loginAsUser("cbrown", "cl0wn3");              // Now that we're logged in, do some other stuff--since we used a DSL to support         // our testers, it's as easy as choosing from available methods.         do.something();         do.somethingElse();         Assert.assertTrue("Something should have been done!", something.wasDone());              // Note that we still haven't referred to a button or web control anywhere in this         // script...     }     

It bears repeating: one of your primary goals should be writing an API that allows your tests to address **the problem at hand, and NOT the problem of the UI**. The UI is a secondary concern for your users – they do not care about the UI, they just want to get their job done. Your test scripts should read like a laundry list of things the user wants to DO, and the things they want to KNOW. The tests should not concern themselves with HOW the UI requires you to go about it.

\* **AUT** : Application under test

# 3 - Generating application state

Selenium should not be used to prepare a test case. All repetitive actions and preparations for a test case, should be done through other methods. For example, most web UIs have authentication \(e.g. a login form\). Eliminating logging in via web browser before every test will improve both the speed and stability of the test. A method should be created to gain access to the AUT\* \(e.g. using an API to login and set a cookie\). Also, creating methods to pre-load data for testing should not be done using Selenium. As mentioned previously, existing APIs should be leveraged to create data for the AUT\*.

\* **AUT** : Application under test

# 4 - Mock external services

Eliminating the dependencies on external services will greatly improve the speed and stability of your tests.

# 5 - Improved reporting

Selenium is not designed to report on the status of test cases run. Taking advantage of the built-in reporting capabilities of unit test frameworks is a good start. Most unit test frameworks have reports that can generate xUnit or HTML formatted reports. xUnit reports are popular for importing results to a Continuous Integration \(CI\) server like Jenkins, Travis, Bamboo, etc. Here are some links for more information regarding report outputs for several languages.

[NUnit 3 Console Runner](https://github.com/nunit/docs/wiki/Console-Runner)

[NUnit 3 Console Command Line](https://github.com/nunit/docs/wiki/Console-Command-Line)

[xUnit getting test results in TeamCity](https://xunit.net/docs/getting-test-results-in-teamcity)

[xUnit getting test results in CruiseControl.NET](https://xunit.net/docs/getting-test-results-in-ccnet)

[xUnit getting test results in Azure DevOps](https://xunit.net/docs/getting-test-results-in-azure-devops)

# 6 - Avoid sharing state

Although mentioned in several places, it is worth mentioning again. We must ensure that the tests are isolated from one another.

  * Do not share test data. Imagine several tests that each query the database for valid orders before picking one to perform an action on. Should two tests pick up the same order you are likely to get unexpected behavior.

  * Clean up stale data in the application that might be picked up by another test e.g. invalid order records.

  * Create a new WebDriver instance per test. This helps ensure test isolation and makes parallelization simpler.

    * If you choose [pytest](https://pytest.org/) as your test runner, this can be easily done by yielding your driver in a global fixture. This way each test gets its own driver instance, and you can ensure that drivers always quit after a test is finished \(pass or fail\).

# 7 - Tips on working with locators

When to use which locators and how best to manage them in your code.

Take a look at examples of the [supported locator strategies](https://www.selenium.dev/documentation/webdriver/elements/locators/).

In general, if HTML IDs are available, unique, and consistently predictable, they are the preferred method for locating an element on a page. They tend to work very quickly, and forego much processing that comes with complicated DOM traversals.

If unique IDs are unavailable, a well-written CSS selector is the preferred method of locating an element. XPath works as well as CSS selectors, but the syntax is complicated and frequently difficult to debug. Though XPath selectors are very flexible, they are typically not performance tested by browser vendors and tend to be quite slow.

Selection strategies based on _linkText_ and _partialLinkText_ have drawbacks in that they only work on link elements. Additionally, they call down to [querySelectorAll](https://www.w3.org/TR/webdriver/#link-text) selectors internally in WebDriver.

Tag name can be a dangerous way to locate elements. There are frequently multiple elements of the same tag present on the page. This is mostly useful when calling the _findElements\(By\)_ method which returns a collection of elements.

The recommendation is to keep your locators as compact and readable as possible. Asking WebDriver to traverse the DOM structure is an expensive operation, and the more you can narrow the scope of your search, the better.

# 8 - Test independency

Write each test as its own unit. Write the tests in a way that will not be reliant on other tests to complete:

Let us say there is a content management system with which you can create some custom content which then appears on your website as a module after publishing, and it may take some time to sync between the CMS and the application.

A wrong way of testing your module is that the content is created and published in one test, and then checking the module in another test. This is not feasible as the content may not be available immediately for the other test after publishing.

Instead, you can create a stub content which can be turned on and off within the affected test, and use that for validating the module. However, for content creation, you can still have a separate test.

# 9 - Consider using a fluent API

Martin Fowler coined the term [“Fluent API”](https://www.martinfowler.com/bliki/FluentInterface.html). Selenium already implements something like this in their `FluentWait` class, which is meant as an alternative to the standard `Wait` class. You could enable the Fluent API design pattern in your page object and then query the Google search page with a code snippet like this one:               driver.get( "http://www.google.com/webhp?hl=en&amp;tab=ww" );     GoogleSearchPage gsp = new GoogleSearchPage(driver);     gsp.setSearchString().clickSearchButton();     

The Google page object class with this fluent behavior might look like this:               public abstract class BasePage {         protected WebDriver driver;              public BasePage(WebDriver driver) {             this.driver = driver;         }     }          public class GoogleSearchPage extends BasePage {         public GoogleSearchPage(WebDriver driver) {             super(driver);             // Generally do not assert within pages or components.             // Effectively throws an exception if the lambda condition is not met.             new WebDriverWait(driver, Duration.ofSeconds(3)).until(d -> d.findElement(By.id("logo")));         }              public GoogleSearchPage setSearchString(String sstr) {             driver.findElement(By.id("gbqfq")).sendKeys(sstr);             return this;         }              public void clickSearchButton() {             driver.findElement(By.id("gbqfb")).click();         }     }     

# 10 - Fresh browser per test

Start each test from a clean, known state. Ideally, spin up a new virtual machine for each test. If spinning up a new virtual machine is not practical, at least start a new WebDriver for each test. Most browser drivers like GeckoDriver and ChromeDriver will start with a clean known state with a new user profile, by default.               WebDriver driver = new FirefoxDriver();