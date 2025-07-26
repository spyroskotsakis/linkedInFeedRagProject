# Compose Develop Specification | Docker Docs

**URL:** https://docs.docker.com/reference/compose-file/develop
**Word Count:** 1339
**Links Count:** 494
**Scraped:** 2025-07-16 01:56:12
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# Compose Develop Specification

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

> Note >  > Develop is an optional part of the Compose Specification. It is available with Docker Compose version 2.22.0 and later.

This page defines how Compose behaves to efficiently assist you and defines the development constraints and workflows set by Compose. Only a subset of Compose file services may require a `develop` subsection.

## Illustrative example               services:       frontend:         image: example/webapp         build: ./webapp         develop:           watch:              # sync static content             - path: ./webapp/html               action: sync               target: /var/www               ignore:                 - node_modules/            backend:         image: example/backend         build: ./backend         develop:           watch:              # rebuild image and recreate service             - path: ./backend/src               action: rebuild

## Attributes

The `develop` subsection defines configuration options that are applied by Compose to assist you during development of a service with optimized workflows.

### `watch`

The `watch` attribute defines a list of rules that control automatic service updates based on local file changes. `watch` is a sequence, each individual item in the sequence defines a rule to be applied by Compose to monitor source code for changes. For more information, see [Use Compose Watch](https://docs.docker.com/compose/how-tos/file-watch/).

#### `action`

`action` defines the action to take when changes are detected. If `action` is set to:

  * `rebuild`: Compose rebuilds the service image based on the `build` section and recreates the service with the updated image.   * `restart`: Compose restarts the service container. Available with Docker Compose version 2.32.0 and later.   * `sync`: Compose keeps the existing service container\(s\) running, but synchronizes source files with container content according to the `target` attribute.   * `sync+restart`: Compose synchronizes source files with container content according to the `target` attribute, and then restarts the container. Available with Docker Compose version 2.23.0 and later.   * `sync+exec`: Compose synchronizes source files with container content according to the `target` attribute, and then executes a command inside the container. Available with Docker Compose version 2.32.0 and later.

#### `exec`

Requires: Docker Compose [2.32.2](https://docs.docker.com/compose/releases/release-notes/#2232) and later

`exec` is only relevant when `action` is set to `sync+exec`. Like [service hooks](https://docs.docker.com/reference/compose-file/services/#post_start), `exec` is used to define the command to be run inside the container once it has started.

  * `command`: Specifies the command to run once the container starts. This attribute is required, and you can choose to use either the shell form or the exec form.   * `user`: The user to run the command. If not set, the command is run with the same user as the main service command.   * `privileged`: Lets the command run with privileged access.   * `working_dir`: The working directory in which to run the command. If not set, it is run in the same working directory as the main service command.   * `environment`: Sets the environment variables to run the command. While the command inherits the environment variables defined for the serviceâs main command, this section lets you add new variables or override existing ones.

              services:       frontend:         image: ...         develop:           watch:              # sync content then run command to reload service without interruption             - path: ./etc/config               action: sync+exec               target: /etc/config/               exec:                 command: app reload

#### `ignore`

The `ignore` attribute is used to define a list of patterns for paths to be ignored. Any updated file that matches a pattern, or belongs to a folder that matches a pattern, won't trigger services to be re-created. The syntax is the same as `.dockerignore` file:

  * `*` matches 0 or more characters in a filename.   * `?` matches a single character in filename.   * `*/*` matches two nested folders with arbitrary names   * `**` matches an arbitrary number of nested folders

If the build context includes a `.dockerignore` file, the patterns in this file is loaded as implicit content for the `ignores` file, and values set in the Compose model are appended.

#### `include`

It is sometimes easier to select files to be watched instead of declaring those that shouldn't be watched with `ignore`.

The `include` attribute is used to define a pattern, or a list of patterns, for paths to be considered for watching. Only files that match these patterns will be considered when applying a watch rule. The syntax is the same as `ignore`.               services:       backend:         image: example/backend         develop:           watch:              # rebuild image and recreate service             - path: ./src               include: "*.go"                 action: rebuild

> Note >  > In many cases `include` patterns start with a wildcard \(`*`\) character. This has special meaning in YAML syntax to define an [alias node](https://yaml.org/spec/1.2.2/#alias-nodes) so you have to wrap pattern expression with quotes.

#### `path`

`path` attribute defines the path to source code \(relative to the project directory\) to monitor for changes. Updates to any file inside the path, which doesn't match any `ignore` rule, triggers the configured action.

#### `target`

`target` attribute only applies when `action` is configured for `sync`. Files within `path` that have changes are synchronized with the container's filesystem, so that the latter is always running with up-to-date content.