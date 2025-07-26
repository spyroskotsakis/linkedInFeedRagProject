# Run your tests | Docker Docs

**URL:** https://docs.docker.com/guides/php/run-tests
**Word Count:** 372
**Links Count:** 63
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

# Run PHP tests in a container

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Prerequisites

Complete all the previous sections of this guide, starting with [Containerize a PHP application](https://docs.docker.com/guides/php/containerize/).

## Overview

Testing is an essential part of modern software development. Testing can mean a lot of things to different development teams. There are unit tests, integration tests and end-to-end testing. In this guide you take a look at running your unit tests in Docker when developing and when building.

## Run tests when developing locally

The sample application already has a PHPUnit test inside the `tests` directory. When developing locally, you can use Compose to run your tests.

Run the following command in the `docker-php-sample` directory to run the tests inside a container.               $ docker compose run --build --rm server ./vendor/bin/phpunit tests/HelloWorldTest.php     

You should see output that contains the following.               Hello, Docker!PHPUnit 9.6.13 by Sebastian Bergmann and contributors.          .                                                                   1 / 1 (100%)          Time: 00:00.003, Memory: 4.00 MB          OK (1 test, 1 assertion)     

To learn more about the command, see [docker compose run](https://docs.docker.com/reference/cli/docker/compose/run/).

## Run tests when building

To run your tests when building, you need to update your Dockerfile. Create a new test stage that runs the tests.

The following is the updated Dockerfile.               # syntax=docker/dockerfile:1          FROM composer:lts as prod-deps     WORKDIR /app     RUN --mount=type=bind,source=./composer.json,target=composer.json \         --mount=type=bind,source=./composer.lock,target=composer.lock \         --mount=type=cache,target=/tmp/cache \         composer install --no-dev --no-interaction          FROM composer:lts as dev-deps     WORKDIR /app     RUN --mount=type=bind,source=./composer.json,target=composer.json \         --mount=type=bind,source=./composer.lock,target=composer.lock \         --mount=type=cache,target=/tmp/cache \         composer install --no-interaction          FROM php:8.2-apache as base     RUN docker-php-ext-install pdo pdo_mysql     COPY ./src /var/www/html          FROM base as development     COPY ./tests /var/www/html/tests     RUN mv "$PHP_INI_DIR/php.ini-development" "$PHP_INI_DIR/php.ini"     COPY --from=dev-deps app/vendor/ /var/www/html/vendor          FROM development as test     WORKDIR /var/www/html     RUN ./vendor/bin/phpunit tests/HelloWorldTest.php          FROM base as final     RUN mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini"     COPY --from=prod-deps app/vendor/ /var/www/html/vendor     USER www-data

Run the following command to build an image using the test stage as the target and view the test results. Include `--progress plain` to view the build output, `--no-cache` to ensure the tests always run, and `--target test` to target the test stage.               $ docker build -t php-docker-image-test --progress plain --no-cache --target test .     

You should see output containing the following.               #18 [test 2/2] RUN ./vendor/bin/phpunit tests/HelloWorldTest.php     #18 0.385 Hello, Docker!PHPUnit 9.6.13 by Sebastian Bergmann and contributors.     #18 0.392     #18 0.394 .                                                                   1 / 1 (100%)     #18 0.395     #18 0.395 Time: 00:00.003, Memory: 4.00 MB     #18 0.395     #18 0.395 OK (1 test, 1 assertion)     

## Summary

In this section, you learned how to run tests when developing locally using Compose and how to run tests when building your image.

Related information:

  * [docker compose run](https://docs.docker.com/reference/cli/docker/compose/run/)

## Next steps

Next, youâll learn how to set up a CI/CD pipeline using GitHub Actions.

[Configure CI/CD for your PHP application Â»](https://docs.docker.com/guides/php/configure-ci-cd/)