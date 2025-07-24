# Install a Selenium library | Selenium

**URL:** https://www.selenium.dev/documentation/webdriver/getting_started/install_library
**Word Count:** 466
**Links Count:** 216
**Scraped:** 2025-07-17 06:15:03
**Status:** completed

---

# Install a Selenium library

Setting up the Selenium library for your favourite programming language.

First you need to install the Selenium bindings for your automation project. The installation process for libraries depends on the language you choose to use. Make sure you check the [Selenium downloads page](https://www.selenium.dev/downloads/) to make sure you are using the latest version.

## Requirements by language

  * Java   * Python   * CSharp   * Ruby   * JavaScript   * Kotlin

View the minimum supported Java version [here](https://github.com/SeleniumHQ/selenium/blob/trunk/.bazelrc#L13).

Installation of Selenium libraries for Java is accomplished using a build tool.

### Maven

Specify the dependencies in the project’s `pom.xml` file:                       <dependency>                 <groupId>org.seleniumhq.selenium</groupId>                 <artifactId>selenium-java</artifactId>                 <version>${selenium.version}</version>             </dependency>

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/java/pom.xml#L30-L34)

##### examples/java/pom.xml

Copy  Close               <?xml version="1.0" encoding="UTF-8"?>     <project xmlns="http://maven.apache.org/POM/4.0.0"              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"              xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">         <modelVersion>4.0.0</modelVersion>              <groupId>dev.selenium</groupId>         <artifactId>selenium-examples</artifactId>         <version>1.0.0</version>              <properties>             <surefire.parallel>1</surefire.parallel>             <maven.compiler.source>17</maven.compiler.source>             <maven.compiler.target>17</maven.compiler.target>             <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>             <selenium.version>4.34.0</selenium.version>         </properties>              <repositories>             <repository>             <id>sonatype-nexus-snapshots</id>             <url>https://oss.sonatype.org/content/repositories/snapshots/</url>             <snapshots>                 <enabled>true</enabled>             </snapshots>             </repository>         </repositories>              <dependencies>             <dependency>                 <groupId>org.seleniumhq.selenium</groupId>                 <artifactId>selenium-java</artifactId>                 <version>${selenium.version}</version>             </dependency>             <dependency>                 <groupId>org.seleniumhq.selenium</groupId>                 <artifactId>selenium-grid</artifactId>                 <version>${selenium.version}</version>             </dependency>             <dependency>                 <groupId>org.junit.jupiter</groupId>                 <artifactId>junit-jupiter-engine</artifactId>                 <version>5.13.3</version>                 <scope>test</scope>             </dependency>             <dependency>                 <groupId>com.titusfortner</groupId>                 <artifactId>selenium-logger</artifactId>                 <version>2.4.0</version>             </dependency>         </dependencies>              <build>             <plugins>                 <plugin>                     <groupId>org.apache.maven.plugins</groupId>                     <artifactId>maven-surefire-plugin</artifactId>                     <version>3.5.3</version>                     <configuration>                         <properties>                             <configurationParameters>                                 junit.jupiter.execution.parallel.enabled = true                                 junit.jupiter.execution.parallel.mode.default = concurrent                                 junit.jupiter.execution.parallel.config.strategy = fixed                                 junit.jupiter.execution.parallel.config.fixed.parallelism = ${surefire.parallel}                                 junit.jupiter.execution.parallel.config.fixed.max-pool-size = ${surefire.parallel}                             </configurationParameters>                         </properties>                         <rerunFailingTestsCount>3</rerunFailingTestsCount>                     </configuration>                 </plugin>             </plugins>         </build>     </project>     

### Gradle

Specify the dependency in the project `build.gradle` file as `testImplementation`:                   testImplementation 'org.seleniumhq.selenium:selenium-java:4.34.0'         testImplementation 'org.junit.jupiter:junit-jupiter-engine:5.13.3'

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/java/build.gradle#L13-L14)

##### examples/java/build.gradle

Copy  Close               plugins {         id 'java'     }          group 'dev.selenium'     version '1.0-SNAPSHOT'          repositories {         mavenCentral()     }          dependencies {         testImplementation 'org.seleniumhq.selenium:selenium-java:4.34.0'         testImplementation 'org.junit.jupiter:junit-jupiter-engine:5.13.3'     }          test {         useJUnitPlatform()     }     

The minimum supported Python version for each Selenium version can be found in “Supported Python Versions” on [PyPi](https://pypi.org/project/selenium/).

There are a couple different ways to install Selenium.

### Pip               pip install selenium     

  

### Download

Alternatively you can download the [PyPI Built Distribution](https://pypi.org/project/selenium/#files) \(selenium-x.x.x.-py3-none-any.whl\) and install it using _pip_ :               pip install selenium-x.x.x.-py3-none-any.whl     

  

### Require in project

To use it in a project, add it to the `requirements.txt` file:               selenium==4.34.2

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/requirements.txt#L1)

##### examples/python/requirements.txt

Copy  Close               selenium==4.34.2     pytest==8.4.1     trio==0.30.0     pytest-trio==0.8.0     pytest-rerunfailures==15.1     flake8==7.3.0     requests==2.32.4     tox==4.27.0     

A list of all supported frameworks for each version of Selenium is available on [Nuget](https://www.nuget.org/packages/Selenium.WebDriver)

There are a few options for installing Selenium.

### Packet Manager               Install-Package Selenium.WebDriver     

  

### .NET CLI               dotnet add package Selenium.WebDriver     

  

### CSProj

in the project’s `csproj` file, specify the dependency as a `PackageReference` in `ItemGroup`:                     <PackageReference Include="Selenium.WebDriver" Version="4.33.0" />

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/dotnet/SeleniumDocs/SeleniumDocs.csproj#L14)

##### examples/dotnet/SeleniumDocs/SeleniumDocs.csproj

Copy  Close               <Project Sdk="Microsoft.NET.Sdk">              <PropertyGroup>             <TargetFramework>net8.0</TargetFramework>             <GenerateProgramFile>false</GenerateProgramFile>         </PropertyGroup>              <ItemGroup>           <PackageReference Include="Microsoft.NET.Test.Sdk" Version="17.11.1" />           <PackageReference Include="Microsoft.IdentityModel.Tokens" Version="7.7.1" />           <PackageReference Include="MSTest.TestAdapter" Version="3.6.0" />           <PackageReference Include="MSTest.TestFramework" Version="3.6.0" />           <PackageReference Include="Selenium.Support" Version="4.33.0" />           <PackageReference Include="Selenium.WebDriver" Version="4.33.0" />         </ItemGroup>              <ItemGroup>           <Folder Include="LocalPackages" />         </ItemGroup>          </Project>     

### Additional considerations

Further items of note for using Visual Studio Code \(vscode\) and C\#

Install the compatible .NET SDK as per the section above. Also install the vscode extensions \(Ctrl-Shift-X\) for C\# and NuGet. Follow the [instruction here](https://docs.microsoft.com/en-us/dotnet/core/tutorials/with-visual-studio-code?pivots=dotnet-5-0) to create and run the “Hello World” console project using C\#. You may also create a NUnit starter project using the command line `dotnet new NUnit`. Make sure the file `%appdata%\NuGet\nuget.config` is configured properly as some developers reported that it will be empty due to some issues. If `nuget.config` is empty, or not configured properly, then .NET builds will fail for Selenium Projects. Add the following section to the file `nuget.config` if it is empty:               <configuration>       <packageSources>         <add key="nuget.org" value="https://api.nuget.org/v3/index.json" protocolVersion="3" />         <add key="nuget.org" value="https://www.nuget.org/api/v2/" />          </packageSources>     ...     

For more info about `nuget.config` [click here](https://docs.microsoft.com/en-us/nuget/reference/nuget-config-file). You may have to customize `nuget.config` to meet you needs.

Now, go back to vscode, press Ctrl-Shift-P, and type “NuGet Add Package”, and enter the required Selenium packages such as `Selenium.WebDriver`. Press Enter and select the version. Now you can use the examples in the documentation related to C\# with vscode.

You can see the minimum required version of Ruby for any given Selenium version on [rubygems.org](https://rubygems.org/gems/selenium-webdriver/)

Selenium can be installed two different ways.

### Install manually               gem install selenium-webdriver     

  

### Add to project’s gemfile               gem 'selenium-devtools', '= 0.138.0'

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/ruby/Gemfile#L10)

##### examples/ruby/Gemfile

Copy  Close               # frozen_string_literal: true          source 'https://rubygems.org'          gem 'ffi', '~> 1.15', '>= 1.15.5' if Gem.win_platform? # Windows only     gem 'rake', '~> 13.0'     gem 'rspec', '~> 3.0'     gem 'rubocop', '~> 1.35'     gem 'rubocop-rspec', '~> 3.0'     gem 'selenium-devtools', '= 0.138.0'     gem 'selenium-webdriver', '= 4.34.0'     

You can find the minimum required version of Node for any given version of Selenium in the `Node Support Policy` section on [npmjs](https://www.npmjs.com/package/selenium-webdriver)

Selenium is typically installed using npm.

### Install locally               npm install selenium-webdriver     

  

### Add to project

In your project’s `package.json`, add requirement to `dependencies`:                       "mocha": "11.7.1"

View Complete Code [__View on GitHub](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/javascript/package.json#L14)

##### examples/javascript/package.json

Copy  Close               {         "name": "javascript-examples",         "version": "1.0.0",         "scripts": {             "test": "npx mocha test/**/*.spec.js --timeout 90000"         },         "author": "The Selenium project",         "license": "Apache-2.0",         "dependencies": {             "assert": "2.1.0",             "selenium-webdriver": "4.34.0"         },         "devDependencies": {             "mocha": "11.7.1"         }     }     

Use the Java bindings for Kotlin.

## Next Step

[Create your first Selenium script](https://www.selenium.dev/documentation/webdriver/getting_started/first_script/)

Last modified March 25, 2025: [Update Python package installation instructions \(\#2235\)\[deploy site\] \(a6bd46e5149\)](https://github.com/SeleniumHQ/seleniumhq.github.io/commit/a6bd46e5149c0fe1caaf60c5f1e06e499b9697a7)