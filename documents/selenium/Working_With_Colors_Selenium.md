# Working With Colors | Selenium

**URL:** https://www.selenium.dev/documentation/webdriver/support_features/colors
**Word Count:** 315
**Links Count:** 220
**Scraped:** 2025-07-17 06:13:36
**Status:** completed

---

# Working With Colors

You will occasionally want to validate the colour of something as part of your tests; the problem is that colour definitions on the web are not constant. Would it not be nice if there was an easy way to compare a HEX representation of a colour with a RGB representation of a colour, or a RGBA representation of a colour with a HSLA representation of a colour?

Worry not. There is a solution: the _Color_ class\!

First of all, you will need to import the class:

[Move Code](https://www.selenium.dev/documentation/about/contributing/#moving-examples)

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

              import org.openqa.selenium.support.Color;                      from selenium.webdriver.support.color import Color       

[Implementation Missing](https://github.com/SeleniumHQ/selenium)               include Selenium::WebDriver::Support       

[Implementation Missing](https://github.com/SeleniumHQ/selenium)               import org.openqa.selenium.support.Color

You can now start creating colour objects. Every colour object will need to be created from a string representation of your colour. Supported colour representations are:

[Move Code](https://www.selenium.dev/documentation/about/contributing/#moving-examples)

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

              private final Color HEX_COLOUR = Color.fromString("#2F7ED8");     private final Color RGB_COLOUR = Color.fromString("rgb(255, 255, 255)");     private final Color RGB_COLOUR = Color.fromString("rgb(40%, 20%, 40%)");     private final Color RGBA_COLOUR = Color.fromString("rgba(255, 255, 255, 0.5)");     private final Color RGBA_COLOUR = Color.fromString("rgba(40%, 20%, 40%, 0.5)");     private final Color HSL_COLOUR = Color.fromString("hsl(100, 0%, 50%)");     private final Color HSLA_COLOUR = Color.fromString("hsla(100, 0%, 50%, 0.5)");                      HEX_COLOUR = Color.from_string('#2F7ED8')     RGB_COLOUR = Color.from_string('rgb(255, 255, 255)')     RGB_COLOUR = Color.from_string('rgb(40%, 20%, 40%)')     RGBA_COLOUR = Color.from_string('rgba(255, 255, 255, 0.5)')     RGBA_COLOUR = Color.from_string('rgba(40%, 20%, 40%, 0.5)')     HSL_COLOUR = Color.from_string('hsl(100, 0%, 50%)')     HSLA_COLOUR = Color.from_string('hsla(100, 0%, 50%, 0.5)')       

[Implementation Missing](https://github.com/SeleniumHQ/selenium)               HEX_COLOUR = Color.from_string('#2F7ED8')     RGB_COLOUR = Color.from_string('rgb(255, 255, 255)')     RGB_COLOUR = Color.from_string('rgb(40%, 20%, 40%)')     RGBA_COLOUR = Color.from_string('rgba(255, 255, 255, 0.5)')     RGBA_COLOUR = Color.from_string('rgba(40%, 20%, 40%, 0.5)')     HSL_COLOUR = Color.from_string('hsl(100, 0%, 50%)')     HSLA_COLOUR = Color.from_string('hsla(100, 0%, 50%, 0.5)')       

[Implementation Missing](https://github.com/SeleniumHQ/selenium)               private val HEX_COLOUR = Color.fromString("#2F7ED8")     private val RGB_COLOUR = Color.fromString("rgb(255, 255, 255)")     private val RGB_COLOUR_PERCENT = Color.fromString("rgb(40%, 20%, 40%)")     private val RGBA_COLOUR = Color.fromString("rgba(255, 255, 255, 0.5)")     private val RGBA_COLOUR_PERCENT = Color.fromString("rgba(40%, 20%, 40%, 0.5)")     private val HSL_COLOUR = Color.fromString("hsl(100, 0%, 50%)")     private val HSLA_COLOUR = Color.fromString("hsla(100, 0%, 50%, 0.5)")       

The Color class also supports all of the base colour definitions specified in [http://www.w3.org/TR/css3-color/\#html4](https://www.w3.org/TR/css3-color/#html4).

[Move Code](https://www.selenium.dev/documentation/about/contributing/#moving-examples)

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

              private final Color BLACK = Color.fromString("black");     private final Color CHOCOLATE = Color.fromString("chocolate");     private final Color HOTPINK = Color.fromString("hotpink");                      BLACK = Color.from_string('black')     CHOCOLATE = Color.from_string('chocolate')     HOTPINK = Color.from_string('hotpink')       

[Implementation Missing](https://github.com/SeleniumHQ/selenium)               BLACK = Color.from_string('black')     CHOCOLATE = Color.from_string('chocolate')     HOTPINK = Color.from_string('hotpink')       

[Implementation Missing](https://github.com/SeleniumHQ/selenium)               private val BLACK = Color.fromString("black")     private val CHOCOLATE = Color.fromString("chocolate")     private val HOTPINK = Color.fromString("hotpink")       

Sometimes browsers will return a colour value of “transparent” if no colour has been set on an element. The Color class also supports this:

[Move Code](https://www.selenium.dev/documentation/about/contributing/#moving-examples)

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

              private final Color TRANSPARENT = Color.fromString("transparent");                      TRANSPARENT = Color.from_string('transparent')       

[Implementation Missing](https://github.com/SeleniumHQ/selenium)               TRANSPARENT = Color.from_string('transparent')       

[Implementation Missing](https://github.com/SeleniumHQ/selenium)               private val TRANSPARENT = Color.fromString("transparent")       

You can now safely query an element to get its colour/background colour knowing that any response will be correctly parsed and converted into a valid Color object:

[Move Code](https://www.selenium.dev/documentation/about/contributing/#moving-examples)

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

              Color loginButtonColour = Color.fromString(driver.findElement(By.id("login")).getCssValue("color"));          Color loginButtonBackgroundColour = Color.fromString(driver.findElement(By.id("login")).getCssValue("background-color"));                      login_button_colour = Color.from_string(driver.find_element(By.ID,'login').value_of_css_property('color'))          login_button_background_colour = Color.from_string(driver.find_element(By.ID,'login').value_of_css_property('background-color'))       

[Implementation Missing](https://github.com/SeleniumHQ/selenium)               login_button_colour = Color.from_string(driver.find_element(id: 'login').css_value('color'))          login_button_background_colour = Color.from_string(driver.find_element(id: 'login').css_value('background-color'))       

[Implementation Missing](https://github.com/SeleniumHQ/selenium)               val loginButtonColour = Color.fromString(driver.findElement(By.id("login")).getCssValue("color"))          val loginButtonBackgroundColour = Color.fromString(driver.findElement(By.id("login")).getCssValue("background-color"))       

You can then directly compare colour objects:

[Move Code](https://www.selenium.dev/documentation/about/contributing/#moving-examples)

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

              assert loginButtonBackgroundColour.equals(HOTPINK);                      assert login_button_background_colour == HOTPINK       

[Implementation Missing](https://github.com/SeleniumHQ/selenium)               assert(login_button_background_colour == HOTPINK)       

[Implementation Missing](https://github.com/SeleniumHQ/selenium)               assert(loginButtonBackgroundColour.equals(HOTPINK))       

Or you can convert the colour into one of the following formats and perform a static validation:

[Move Code](https://www.selenium.dev/documentation/about/contributing/#moving-examples)

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

              assert loginButtonBackgroundColour.asHex().equals("#ff69b4");     assert loginButtonBackgroundColour.asRgba().equals("rgba(255, 105, 180, 1)");     assert loginButtonBackgroundColour.asRgb().equals("rgb(255, 105, 180)");                      assert login_button_background_colour.hex == '#ff69b4'     assert login_button_background_colour.rgba == 'rgba(255, 105, 180, 1)'     assert login_button_background_colour.rgb == 'rgb(255, 105, 180)'       

[Implementation Missing](https://github.com/SeleniumHQ/selenium)               assert(login_button_background_colour.hex == '#ff69b4')     assert(login_button_background_colour.rgba == 'rgba(255, 105, 180, 1)')     assert(login_button_background_colour.rgb == 'rgb(255, 105, 180)')       

[Implementation Missing](https://github.com/SeleniumHQ/selenium)               assert(loginButtonBackgroundColour.asHex().equals("#ff69b4"))     assert(loginButtonBackgroundColour.asRgba().equals("rgba(255, 105, 180, 1)"))     assert(loginButtonBackgroundColour.asRgb().equals("rgb(255, 105, 180)"))       

Colours are no longer a problem.

Last modified September 12, 2023: [replace code alerts with tabpanes that have code badges in each tab \(59dc7de8fa6\)](https://github.com/SeleniumHQ/seleniumhq.github.io/commit/59dc7de8fa68b56032da3f6415f2dc2e11f9fd69)