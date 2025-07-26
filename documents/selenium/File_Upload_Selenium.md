# File Upload | Selenium

**URL:** https://www.selenium.dev/documentation/webdriver/elements/file_upload
**Word Count:** 127
**Links Count:** 204
**Scraped:** 2025-07-17 06:15:03
**Status:** completed

---

# File Upload

Because Selenium cannot interact with the file upload dialog, it provides a way to upload files without opening the dialog. If the element is an `input` element with type `file`, you can use the send keys method to send the full path to the file that will be uploaded.

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

                  WebElement fileInput = driver.findElement(By.cssSelector("input[type=file]"));         fileInput.sendKeys(uploadFile.getAbsolutePath());         driver.findElement(By.id("file-submit")).click();

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/java/src/test/java/dev/selenium/elements/FileUploadTest.java#L17-L19)

##### examples/java/src/test/java/dev/selenium/elements/FileUploadTest.java

Copy  Close               package dev.selenium.elements;          import dev.selenium.BaseChromeTest;     import java.io.File;     import org.junit.jupiter.api.Assertions;     import org.junit.jupiter.api.Test;     import org.openqa.selenium.By;     import org.openqa.selenium.WebElement;          public class FileUploadTest extends BaseChromeTest {            @Test       public void fileUploadTest() {         driver.get("https://the-internet.herokuapp.com/upload");         File uploadFile = new File("src/test/resources/selenium-snapshot.png");              WebElement fileInput = driver.findElement(By.cssSelector("input[type=file]"));         fileInput.sendKeys(uploadFile.getAbsolutePath());         driver.findElement(By.id("file-submit")).click();              WebElement fileName = driver.findElement(By.id("uploaded-files"));         Assertions.assertEquals("selenium-snapshot.png", fileName.getText());       }     }                        file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")         file_input.send_keys(upload_file)         driver.find_element(By.ID, "file-submit").click()

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/elements/test_file_upload.py#L12-L14)

##### examples/python/tests/elements/test\_file\_upload.py

Copy  Close               import os          from selenium import webdriver     from selenium.webdriver.common.by import By               def test_uploads(driver):         driver.get("https://the-internet.herokuapp.com/upload")         upload_file = os.path.abspath(             os.path.join(os.path.dirname(__file__), "..", "selenium-snapshot.png"))              file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")         file_input.send_keys(upload_file)         driver.find_element(By.ID, "file-submit").click()              file_name_element = driver.find_element(By.ID, "uploaded-files")         file_name = file_name_element.text              assert file_name == "selenium-snapshot.png"                                IWebElement fileInput = driver.FindElement(By.CssSelector("input[type=file]"));                 fileInput.SendKeys(uploadFile);                 driver.FindElement(By.Id("file-submit")).Click();

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/dotnet/SeleniumDocs/Elements/FileUploadTest.cs#L21-L23)

##### examples/dotnet/SeleniumDocs/Elements/FileUploadTest.cs

Copy  Close               using System;     using System.IO;     using Microsoft.VisualStudio.TestTools.UnitTesting;     using OpenQA.Selenium;          namespace SeleniumDocs.Elements     {         [TestClass]         public class FileUploadTest : BaseChromeTest         {             [TestMethod]             public void Uploads()             {                 driver.Url = "https://the-internet.herokuapp.com/upload";                      string baseDirectory = AppContext.BaseDirectory;                 string relativePath = "../../../TestSupport/selenium-snapshot.png";                      string uploadFile = Path.GetFullPath(Path.Combine(baseDirectory, relativePath));                      IWebElement fileInput = driver.FindElement(By.CssSelector("input[type=file]"));                 fileInput.SendKeys(uploadFile);                 driver.FindElement(By.Id("file-submit")).Click();                      IWebElement fileName = driver.FindElement(By.Id("uploaded-files"));                 Assert.AreEqual("selenium-snapshot.png", fileName.Text);             }         }     }                   file_input = driver.find_element(css: 'input[type=file]')         file_input.send_keys(upload_file)         driver.find_element(id: 'file-submit').click

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/ruby/spec/elements/file_upload_spec.rb#L12-L14)

##### examples/ruby/spec/elements/file\_upload\_spec.rb

Copy  Close               # frozen_string_literal: true          require 'spec_helper'          RSpec.describe 'File Upload' do       let(:driver) { start_session }            it 'uploads' do         driver.get('https://the-internet.herokuapp.com/upload')         upload_file = File.expand_path('../spec_support/selenium-snapshot.png', __dir__)              file_input = driver.find_element(css: 'input[type=file]')         file_input.send_keys(upload_file)         driver.find_element(id: 'file-submit').click              file_name = driver.find_element(id: 'uploaded-files')         expect(file_name.text).to eq 'selenium-snapshot.png'       end     end                        await driver.get('https://the-internet.herokuapp.com/upload');         // Upload snapshot     

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk//examples/javascript/test/elements/fileUpload.spec.js#L24-L25)

##### /examples/javascript/test/elements/fileUpload.spec.js

Copy  Close               const {Browser, By, until, Builder} = require("selenium-webdriver");     const path = require("path");     const assert = require('node:assert');               describe('File Upload Test', function() {       let driver;            before(async function() {         driver = new Builder()           .forBrowser(Browser.CHROME)           .build();       });            after(async() => await driver.quit());            it('Should be able to upload a file successfully', async function() {         const image = path.resolve('./test/resources/selenium-snapshot.png')              await driver.manage().setTimeouts({implicit: 5000});              // Navigate to URL         await driver.get('https://the-internet.herokuapp.com/upload');         // Upload snapshot         await driver.findElement(By.id("file-upload")).sendKeys(image);         await driver.findElement(By.id("file-submit")).submit();              const revealed = await driver.findElement(By.id('uploaded-files'))         await driver.wait(until.elementIsVisible(revealed), 2000);         const data = await driver.findElement(By.css('h3'));              assert.equal(await data.getText(), `File Uploaded!`);       });     });

[Move Code](https://www.selenium.dev/documentation/about/contributing/#moving-examples)

\`\`\`java import org.openqa.selenium.By import org.openqa.selenium.chrome.ChromeDriver fun main\(\) \{ val driver = ChromeDriver\(\) driver.get\("https://the-internet.herokuapp.com/upload"\) driver.findElement\(By.id\("file-upload"\)\).sendKeys\("selenium-snapshot.jpg"\) driver.findElement\(By.id\("file-submit"\)\).submit\(\) if\(driver.pageSource.contains\("File Uploaded\!"\)\) \{ println\("file uploaded"\) \} else\{ println\("file not uploaded"\) \} \} \`\`\`

Last modified November 17, 2023: [Upgrade to Docsy 0 7 2 \(\#1529\) \(48f43616907\)](https://github.com/SeleniumHQ/seleniumhq.github.io/commit/48f43616907dc77f3f849bfbfb2f476c863e8991)