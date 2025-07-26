# Use a logging driver plugin | Docker Docs

**URL:** https://docs.docker.com/engine/logging/plugins/
**Word Count:** 1276
**Links Count:** 648
**Scraped:** 2025-07-16 01:54:28
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Use a logging driver plugin

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Docker logging plugins allow you to extend and customize Docker's logging capabilities beyond those of the [built-in logging drivers](https://docs.docker.com/engine/logging/configure/). A logging service provider can [implement their own plugins](https://docs.docker.com/engine/extend/plugins_logging/) and make them available on Docker Hub, or a private registry. This topic shows how a user of that logging service can configure Docker to use the plugin.

## Install the logging driver plugin

To install a logging driver plugin, use `docker plugin install <org/image>`, using the information provided by the plugin developer.

You can list all installed plugins using `docker plugin ls`, and you can inspect a specific plugin using `docker inspect`.

## Configure the plugin as the default logging driver

When the plugin is installed, you can configure the Docker daemon to use it as the default by setting the plugin's name as the value of the `log-driver` key in the `daemon.json`, as detailed in the [logging overview](https://docs.docker.com/engine/logging/configure/#configure-the-default-logging-driver). If the logging driver supports additional options, you can set those as the values of the `log-opts` array in the same file.

## Configure a container to use the plugin as the logging driver

After the plugin is installed, you can configure a container to use the plugin as its logging driver by specifying the `--log-driver` flag to `docker run`, as detailed in the [logging overview](https://docs.docker.com/engine/logging/configure/#configure-the-logging-driver-for-a-container). If the logging driver supports additional options, you can specify them using one or more `--log-opt` flags with the option name as the key and the option value as the value.