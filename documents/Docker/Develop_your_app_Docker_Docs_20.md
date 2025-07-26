# Develop your app | Docker Docs

**URL:** https://docs.docker.com/guides/php/develop
**Word Count:** 1164
**Links Count:** 92
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

# Use containers for PHP development

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Prerequisites

Complete [Containerize a PHP application](https://docs.docker.com/guides/php/containerize/).

## Overview

In this section, you'll learn how to set up a development environment for your containerized application. This includes:

  * Adding a local database and persisting data   * Adding phpMyAdmin to interact with the database   * Configuring Compose to automatically update your running Compose services as you edit and save your code   * Creating a development container that contains the dev dependencies

## Add a local database and persist data

You can use containers to set up local services, like a database. To do this for the sample application, you'll need to do the following:

  * Update the `Dockerfile` to install extensions to connect to the database   * Update the `compose.yaml` file to add a database service and volume to persist data

### Update the Dockerfile to install extensions

To install PHP extensions, you need to update the `Dockerfile`. Open your Dockerfile in an IDE or text editor and then update the contents. The following `Dockerfile` includes one new line that installs the `pdo` and `pdo_mysql` extensions. All comments have been removed.               # syntax=docker/dockerfile:1          FROM composer:lts as deps     WORKDIR /app     RUN --mount=type=bind,source=composer.json,target=composer.json \         --mount=type=bind,source=composer.lock,target=composer.lock \         --mount=type=cache,target=/tmp/cache \         composer install --no-dev --no-interaction          FROM php:8.2-apache as final     RUN docker-php-ext-install pdo pdo_mysql     RUN mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini"     COPY --from=deps app/vendor/ /var/www/html/vendor     COPY ./src /var/www/html     USER www-data

For more details about installing PHP extensions, see the [Official Docker Image for PHP](https://hub.docker.com/_/php).

### Update the compose.yaml file to add a db and persist data

Open the `compose.yaml` file in an IDE or text editor. You'll notice it already contains commented-out instructions for a PostgreSQL database and volume. For this application, you'll use MariaDB. For more details about MariaDB, see the [MariaDB Official Docker image](https://hub.docker.com/_/mariadb).

Open the `src/database.php` file in an IDE or text editor. You'll notice that it reads environment variables in order to connect to the database.

In the `compose.yaml` file, you'll need to update the following:

  1. Uncomment and update the database instructions for MariaDB.   2. Add a secret to the server service to pass in the database password.   3. Add the database connection environment variables to the server service.   4. Uncomment the volume instructions to persist data.

The following is the updated `compose.yaml` file. All comments have been removed.               services:       server:         build:           context: .         ports:           - 9000:80         depends_on:           db:             condition: service_healthy         secrets:           - db-password         environment:           - PASSWORD_FILE_PATH=/run/secrets/db-password           - DB_HOST=db           - DB_NAME=example           - DB_USER=root       db:         image: mariadb         restart: always         user: root         secrets:           - db-password         volumes:           - db-data:/var/lib/mysql         environment:           - MARIADB_ROOT_PASSWORD_FILE=/run/secrets/db-password           - MARIADB_DATABASE=example         expose:           - 3306         healthcheck:           test:             [               "CMD",               "/usr/local/bin/healthcheck.sh",               "--su-mysql",               "--connect",               "--innodb_initialized",             ]           interval: 10s           timeout: 5s           retries: 5     volumes:       db-data:     secrets:       db-password:         file: db/password.txt

> Note >  > To learn more about the instructions in the Compose file, see [Compose file reference](https://docs.docker.com/reference/compose-file/).

Before you run the application using Compose, notice that this Compose file uses `secrets` and specifies a `password.txt` file to hold the database's password. You must create this file as it's not included in the source repository.

In the `docker-php-sample` directory, create a new directory named `db` and inside that directory create a file named `password.txt`. Open `password.txt` in an IDE or text editor and add the following password. The password must be on a single line, with no additional lines in the file.               example

Save and close the `password.txt` file.

You should now have the following in your `docker-php-sample` directory.               âââ docker-php-sample/     â âââ .git/     â âââ db/     â â âââ password.txt     â âââ src/     â âââ tests/     â âââ .dockerignore     â âââ .gitignore     â âââ compose.yaml     â âââ composer.json     â âââ composer.lock     â âââ Dockerfile     â âââ README.Docker.md     â âââ README.md

Run the following command to start your application.               $ docker compose up --build     

Open a browser and view the application at <http://localhost:9000/database.php>. You should see a simple web application with text and a counter that increments every time you refresh.

Press `ctrl+c` in the terminal to stop your application.

## Verify that data persists in the database

In the terminal, run `docker compose rm` to remove your containers and then run `docker compose up` to run your application again.               $ docker compose rm     $ docker compose up --build     

Refresh <http://localhost:9000/database.php> in your browser and verify that the previous count still exists. Without a volume, the database data wouldn't persist after you remove the container.

Press `ctrl+c` in the terminal to stop your application.

## Add phpMyAdmin to interact with the database

You can easily add services to your application stack by updating the `compose.yaml` file.

Update your `compose.yaml` to add a new service for phpMyAdmin. For more details, see the [phpMyAdmin Official Docker Image](https://hub.docker.com/_/phpmyadmin). The following is the updated `compose.yaml` file.               services:       server:         build:           context: .         ports:           - 9000:80         depends_on:           db:             condition: service_healthy         secrets:           - db-password         environment:           - PASSWORD_FILE_PATH=/run/secrets/db-password           - DB_HOST=db           - DB_NAME=example           - DB_USER=root       db:         image: mariadb         restart: always         user: root         secrets:           - db-password         volumes:           - db-data:/var/lib/mysql         environment:           - MARIADB_ROOT_PASSWORD_FILE=/run/secrets/db-password           - MARIADB_DATABASE=example         expose:           - 3306         healthcheck:           test:             [               "CMD",               "/usr/local/bin/healthcheck.sh",               "--su-mysql",               "--connect",               "--innodb_initialized",             ]           interval: 10s           timeout: 5s           retries: 5       phpmyadmin:         image: phpmyadmin         ports:           - 8080:80         depends_on:           - db         environment:           - PMA_HOST=db     volumes:       db-data:     secrets:       db-password:         file: db/password.txt

In the terminal, run `docker compose up` to run your application again.               $ docker compose up --build     

Open <http://localhost:8080> in your browser to access phpMyAdmin. Log in using `root` as the username and `example` as the password. You can now interact with the database through phpMyAdmin.

Press `ctrl+c` in the terminal to stop your application.

## Automatically update services

Use Compose Watch to automatically update your running Compose services as you edit and save your code. For more details about Compose Watch, see [Use Compose Watch](https://docs.docker.com/compose/how-tos/file-watch/).

Open your `compose.yaml` file in an IDE or text editor and then add the Compose Watch instructions. The following is the updated `compose.yaml` file.               services:       server:         build:           context: .         ports:           - 9000:80         depends_on:           db:             condition: service_healthy         secrets:           - db-password         environment:           - PASSWORD_FILE_PATH=/run/secrets/db-password           - DB_HOST=db           - DB_NAME=example           - DB_USER=root         develop:           watch:             - action: sync               path: ./src               target: /var/www/html       db:         image: mariadb         restart: always         user: root         secrets:           - db-password         volumes:           - db-data:/var/lib/mysql         environment:           - MARIADB_ROOT_PASSWORD_FILE=/run/secrets/db-password           - MARIADB_DATABASE=example         expose:           - 3306         healthcheck:           test:             [               "CMD",               "/usr/local/bin/healthcheck.sh",               "--su-mysql",               "--connect",               "--innodb_initialized",             ]           interval: 10s           timeout: 5s           retries: 5       phpmyadmin:         image: phpmyadmin         ports:           - 8080:80         depends_on:           - db         environment:           - PMA_HOST=db     volumes:       db-data:     secrets:       db-password:         file: db/password.txt

Run the following command to run your application with Compose Watch.               $ docker compose watch     

Open a browser and verify that the application is running at <http://localhost:9000/hello.php>.

Any changes to the application's source files on your local machine will now be immediately reflected in the running container.

Open `hello.php` in an IDE or text editor and update the string `Hello, world!` to `Hello, Docker!`.

Save the changes to `hello.php` and then wait a few seconds for the application to sync. Refresh <http://localhost:9000/hello.php> in your browser and verify that the updated text appears.

Press `ctrl+c` in the terminal to stop Compose Watch. Run `docker compose down` in the terminal to stop the application.

## Create a development container

At this point, when you run your containerized application, Composer isn't installing the dev dependencies. While this small image is good for production, it lacks the tools and dependencies you may need when developing and it doesn't include the `tests` directory. You can use multi-stage builds to build stages for both development and production in the same Dockerfile. For more details, see [Multi-stage builds](https://docs.docker.com/build/building/multi-stage/).

In the `Dockerfile`, you'll need to update the following:

  1. Split the `deps` staged into two stages. One stage for production \(`prod-deps`\) and one stage \(`dev-deps`\) to install development dependencies.   2. Create a common `base` stage.   3. Create a new `development` stage for development.   4. Update the `final` stage to copy dependencies from the new `prod-deps` stage.

The following is the `Dockerfile` before and after the changes.

Before  After               # syntax=docker/dockerfile:1          FROM composer:lts as deps     WORKDIR /app     RUN --mount=type=bind,source=composer.json,target=composer.json \         --mount=type=bind,source=composer.lock,target=composer.lock \         --mount=type=cache,target=/tmp/cache \         composer install --no-dev --no-interaction          FROM php:8.2-apache as final     RUN docker-php-ext-install pdo pdo_mysql     RUN mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini"     COPY --from=deps app/vendor/ /var/www/html/vendor     COPY ./src /var/www/html     USER www-data               # syntax=docker/dockerfile:1          FROM composer:lts as prod-deps     WORKDIR /app     RUN --mount=type=bind,source=./composer.json,target=composer.json \         --mount=type=bind,source=./composer.lock,target=composer.lock \         --mount=type=cache,target=/tmp/cache \         composer install --no-dev --no-interaction          FROM composer:lts as dev-deps     WORKDIR /app     RUN --mount=type=bind,source=./composer.json,target=composer.json \         --mount=type=bind,source=./composer.lock,target=composer.lock \         --mount=type=cache,target=/tmp/cache \         composer install --no-interaction          FROM php:8.2-apache as base     RUN docker-php-ext-install pdo pdo_mysql     COPY ./src /var/www/html          FROM base as development     COPY ./tests /var/www/html/tests     RUN mv "$PHP_INI_DIR/php.ini-development" "$PHP_INI_DIR/php.ini"     COPY --from=dev-deps app/vendor/ /var/www/html/vendor          FROM base as final     RUN mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini"     COPY --from=prod-deps app/vendor/ /var/www/html/vendor     USER www-data

Update your `compose.yaml` file by adding an instruction to target the development stage.

The following is the updated section of the `compose.yaml` file.               services:       server:         build:           context: .           target: development           # ...

Your containerized application will now install the dev dependencies.

Run the following command to start your application.               $ docker compose up --build     

Open a browser and view the application at <http://localhost:9000/hello.php>. You should still see the simple "Hello, Docker\!" application.

Press `ctrl+c` in the terminal to stop your application.

While the application appears the same, you can now make use of the dev dependencies. Continue to the next section to learn how you can run tests using Docker.

## Summary

In this section, you took a look at setting up your Compose file to add a local database and persist data. You also learned how to use Compose Watch to automatically sync your application when you update your code. And finally, you learned how to create a development container that contains the dependencies needed for development.

Related information:

  * [Compose file reference](https://docs.docker.com/reference/compose-file/)   * [Compose file watch](https://docs.docker.com/compose/how-tos/file-watch/)   * [Dockerfile reference](https://docs.docker.com/reference/dockerfile/)   * [Official Docker Image for PHP](https://hub.docker.com/_/php)

## Next steps

In the next section, you'll learn how to run unit tests using Docker.

[Run PHP tests in a container Â»](https://docs.docker.com/guides/php/run-tests/)