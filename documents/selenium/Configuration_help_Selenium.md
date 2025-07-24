# Configuration help | Selenium

**URL:** https://www.selenium.dev/documentation/grid/configuration/help
**Word Count:** 239
**Links Count:** 212
**Scraped:** 2025-07-17 06:15:56
**Status:** completed

---

# Configuration help

Get information about all the available options to configure Grid.

The help commands display information based on the current code implementation. Hence, it will provide accurate information in case the documentation is not updated. It is the easiest way to learn about Grid 4 configuration for any new version.

## Info Command

The info command provides detailed docs on the following topics:

  * Configuring Selenium   * Security   * Session Map setup   * Tracing

### Config help

Quick config help and overview is provided by running:               java -jar selenium-server-<version>.jar info config     

### Security

To get details on setting up the Grid servers for secure communication and node registration:               java -jar selenium-server-<version>.jar info security     

### Session Map setup

By default, Grid uses a local session map to store session information. Grid supports additional storage options like Redis and JDBC - SQL supported databases. To set up different session storage, use the following command to get setup steps:               java -jar selenium-server-<version>.jar info sessionmap     

### Setting up tracing with OpenTelemetry and Jaeger

By default, tracing is enabled. To export traces and visualize them via Jaeger, use the following command for instructions:               java -jar selenium-server-<version>.jar info tracing     

## List the Selenium Grid commands               java -jar selenium-server-<version>.jar --config-help     

It will show all the available commands and description for each one.

## Component help commands

Pass –help config option after the Selenium role to get component-specific config information.

### Standalone               java -jar selenium-server-<version>.jar standalone --help     

### Hub               java -jar selenium-server-<version>.jar hub --help     

### Sessions               java -jar selenium-server-<version>.jar sessions --help     

### New Session Queue               java -jar selenium-server-<version>.jar sessionqueue --help     

### Distributor               java -jar selenium-server-<version>.jar distributor --help     

### Router               java -jar selenium-server-<version>.jar router --help     

### Node               java -jar selenium-server-<version>.jar node --help     

Last modified December 7, 2021: [reorganize documentation and update titles \(\#861\) \[deploy site\] \(872174bfdd8\)](https://github.com/SeleniumHQ/seleniumhq.github.io/commit/872174bfdd83abf0446f796914acf3e875eeddc6)