# Containerize your app | Docker Docs

**URL:** https://docs.docker.com/guides/php/containerize
**Word Count:** 510
**Links Count:** 75
**Scraped:** 2025-07-16 02:04:38
**Status:** completed

---

Back

[Guides](https://docs.docker.com/guides/)

  * [Get started](https://docs.docker.com/get-started/)   * [Manuals](https://docs.docker.com/manuals/)   * [Reference](https://docs.docker.com/reference/)

* * *

[PHP language-specific guide](https://docs.docker.com/guides/php/)

This guide explains how to containerize PHP applications using Docker.

![](https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/php/php-original.svg) PHP

20 minutes

[1](https://docs.docker.com/guides/php/containerize/)

[Containerize your app](https://docs.docker.com/guides/php/containerize/)

[2](https://docs.docker.com/guides/php/develop/)

[Develop your app](https://docs.docker.com/guides/php/develop/)

[3](https://docs.docker.com/guides/php/run-tests/)

[Run your tests](https://docs.docker.com/guides/php/run-tests/)

[4](https://docs.docker.com/guides/php/configure-ci-cd/)

[Configure CI/CD](https://docs.docker.com/guides/php/configure-ci-cd/)

[5](https://docs.docker.com/guides/php/deploy/)

[Test your deployment](https://docs.docker.com/guides/php/deploy/)

[Â« Back to all guides](https://docs.docker.com/guides/)

# Containerize a PHP application

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Prerequisites

  * You have installed the latest version of [Docker Desktop](https://docs.docker.com/get-started/get-docker/).   * You have a [git client](https://git-scm.com/downloads). The examples in this section use a command-line based git client, but you can use any client.

## Overview

This section walks you through containerizing and running a PHP application.

## Get the sample applications

In this guide, you will use a pre-built PHP application. The application uses Composer for library dependency management. You'll serve the application via an Apache web server.

Open a terminal, change directory to a directory that you want to work in, and run the following command to clone the repository.               $ git clone https://github.com/docker/docker-php-sample     

The sample application is a basic hello world application and an application that increments a counter in a database. In addition, the application uses PHPUnit for testing.

## Initialize Docker assets

Now that you have an application, you can use `docker init` to create the necessary Docker assets to containerize your application. Inside the `docker-php-sample` directory, run the `docker init` command in a terminal. `docker init` provides some default configuration, but you'll need to answer a few questions about your application. For example, this application uses PHP version 8.2. Refer to the following `docker init` example and use the same answers for your prompts.               $ docker init     Welcome to the Docker Init CLI!          This utility will walk you through creating the following files with sensible defaults for your project:       - .dockerignore       - Dockerfile       - compose.yaml       - README.Docker.md          Let's get started!          ? What application platform does your project use? PHP with Apache     ? What version of PHP do you want to use? 8.2     ? What's the relative directory (with a leading .) for your app? ./src     ? What local port do you want to use to access your server? 9000     

You should now have the following contents in your `docker-php-sample` directory.               âââ docker-php-sample/     â âââ .git/     â âââ src/     â âââ tests/     â âââ .dockerignore     â âââ .gitignore     â âââ compose.yaml     â âââ composer.json     â âââ composer.lock     â âââ Dockerfile     â âââ README.Docker.md     â âââ README.md

To learn more about the files that `docker init` added, see the following:

  * [Dockerfile](https://docs.docker.com/reference/dockerfile/)   * [.dockerignore](https://docs.docker.com/reference/dockerfile/#dockerignore-file)   * [compose.yaml](https://docs.docker.com/reference/compose-file/)

## Run the application

Inside the `docker-php-sample` directory, run the following command in a terminal.               $ docker compose up --build     

Open a browser and view the application at <http://localhost:9000/hello.php>. You should see a simple hello world application.

In the terminal, press `ctrl`+`c` to stop the application.

### Run the application in the background

You can run the application detached from the terminal by adding the `-d` option. Inside the `docker-php-sample` directory, run the following command in a terminal.               $ docker compose up --build -d     

Open a browser and view the application at <http://localhost:9000/hello.php>. You should see a simple hello world application.

In the terminal, run the following command to stop the application.               $ docker compose down     

For more information about Compose commands, see the [Compose CLI reference](https://docs.docker.com/reference/cli/docker/compose/).

## Summary

In this section, you learned how you can containerize and run a simple PHP application using Docker.

Related information:

  * [docker init reference](https://docs.docker.com/reference/cli/docker/init/)

## Next steps

In the next section, you'll learn how you can develop your application using Docker containers.

[Use containers for PHP development Â»](https://docs.docker.com/guides/php/develop/)