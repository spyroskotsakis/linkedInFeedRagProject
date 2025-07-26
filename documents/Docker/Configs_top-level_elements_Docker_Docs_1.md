# Configs top-level elements | Docker Docs

**URL:** https://docs.docker.com/reference/compose-file/configs
**Word Count:** 1083
**Links Count:** 488
**Scraped:** 2025-07-16 01:55:27
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# Configs top-level elements

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Configs let services to adapt their behaviour without the need to rebuild a Docker image. As with volumes, configs are mounted as files into a container's filesystem. The location of the mount point within the container defaults to `/<config-name>` in Linux containers and `C:\<config-name>` in Windows containers.

Services can only access configs when explicitly granted by a [`configs`](https://docs.docker.com/reference/compose-file/services/#configs) attribute within the `services` top-level element.

By default, the config:

  * Is owned by the user running the container command but can be overridden by service configuration.   * Has world-readable permissions \(mode 0444\), unless the service is configured to override this.

The top-level `configs` declaration defines or references configuration data that is granted to services in your Compose application. The source of the config is either `file` or `external`.

  * `file`: The config is created with the contents of the file at the specified path.   * `environment`: The config content is created with the value of an environment variable. Introduced in Docker Compose version [2.23.1](https://docs.docker.com/compose/releases/release-notes/#2231).   * `content`: The content is created with the inlined value. Introduced in Docker Compose version [2.23.1](https://docs.docker.com/compose/releases/release-notes/#2231).   * `external`: If set to true, `external` specifies that this config has already been created. Compose does not attempt to create it, and if it does not exist, an error occurs.   * `name`: The name of the config object in the container engine to look up. This field can be used to reference configs that contain special characters. The name is used as is and will **not** be scoped with the project name.

## Example 1

`<project_name>_http_config` is created when the application is deployed, by registering the content of the `httpd.conf` as the configuration data.               configs:       http_config:         file: ./httpd.conf

Alternatively, `http_config` can be declared as external. Compose looks up `http_config` to expose the configuration data to relevant services.               configs:       http_config:         external: true

## Example 2

`<project_name>_app_config` is created when the application is deployed, by registering the inlined content as the configuration data. This means Compose infers variables when creating the config, which allows you to adjust content according to service configuration:               configs:       app_config:         content: |           debug=${DEBUG}           spring.application.admin.enabled=${DEBUG}           spring.application.name=${COMPOSE_PROJECT_NAME}

## Example 3

External configs lookup can also use a distinct key by specifying a `name`.

The following example modifies the previous one to look up a config using the parameter `HTTP_CONFIG_KEY`. The actual lookup key is set at deployment time by the [interpolation](https://docs.docker.com/reference/compose-file/interpolation/) of variables, but exposed to containers as hard-coded ID `http_config`.               configs:       http_config:         external: true         name: "${HTTP_CONFIG_KEY}"

If `external` is set to `true`, all other attributes apart from `name` are irrelevant. If Compose detects any other attribute, it rejects the Compose file as invalid.