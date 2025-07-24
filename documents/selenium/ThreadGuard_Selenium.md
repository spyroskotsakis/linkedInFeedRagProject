# ThreadGuard | Selenium

**URL:** https://www.selenium.dev/documentation/webdriver/support_features/thread_guard
**Word Count:** 187
**Links Count:** 198
**Scraped:** 2025-07-17 06:13:37
**Status:** completed

---

# ThreadGuard

This class is only available in the Java Binding

ThreadGuard checks that a driver is called only from the same thread that created it. Threading issues especially when running tests in Parallel may have mysterious and hard to diagnose errors. Using this wrapper prevents this category of errors and will raise an exception when it happens.

The following example simulate a clash of threads:               public class DriverClash {       //thread main (id 1) created this driver       private WebDriver protectedDriver = ThreadGuard.protect(new ChromeDriver());             static {         System.setProperty("webdriver.chrome.driver", "<Set path to your Chromedriver>");       }              //Thread-1 (id 24) is calling the same driver causing the clash to happen       Runnable r1 = () -> {protectedDriver.get("https://selenium.dev");};       Thread thr1 = new Thread(r1);               void runThreads(){         thr1.start();       }            public static void main(String[] args) {         new DriverClash().runThreads();       }     }     

The result shown below:               Exception in thread "Thread-1" org.openqa.selenium.WebDriverException:     Thread safety error; this instance of WebDriver was constructed     on thread main (id 1)and is being accessed by thread Thread-1 (id 24)     This is not permitted and *will* cause undefined behaviour     

As seen in the example:

  * `protectedDriver` Will be created in Main thread   * We use Java `Runnable` to spin up a new process and a new `Thread` to run the process   * Both `Thread` will clash because the Main Thread does not have `protectedDriver` in it’s memory.   * `ThreadGuard.protect` will throw an exception.

#### Note:

This does not replace the need for using `ThreadLocal` to manage drivers when running parallel.

Last modified September 23, 2022: [rename additional features section back to support features to re-emphasize the distinct purpose of support classes \(c70272e7f8b\)](https://github.com/SeleniumHQ/seleniumhq.github.io/commit/c70272e7f8be03fada236fd1f6dc75e81ec79638)