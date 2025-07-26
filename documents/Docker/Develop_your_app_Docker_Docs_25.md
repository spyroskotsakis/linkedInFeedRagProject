# Develop your app | Docker Docs

**URL:** https://docs.docker.com/guides/r/develop/
**Word Count:** 585
**Links Count:** 70
**Scraped:** 2025-07-16 01:47:07
**Status:** completed

---

Back

[Guides](https://docs.docker.com/guides/)

  * [Get started](https://docs.docker.com/get-started/)   * [Manuals](https://docs.docker.com/manuals/)   * [Reference](https://docs.docker.com/reference/)

* * *

[R language-specific guide](https://docs.docker.com/guides/r/)

This guide details how to containerize R applications using Docker.

![](https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/r/r-original.svg) R

10 minutes

[1](https://docs.docker.com/guides/r/containerize/)

[Containerize your app](https://docs.docker.com/guides/r/containerize/)

[2](https://docs.docker.com/guides/r/develop/)

[Develop your app](https://docs.docker.com/guides/r/develop/)

[3](https://docs.docker.com/guides/r/configure-ci-cd/)

[Configure CI/CD](https://docs.docker.com/guides/r/configure-ci-cd/)

[4](https://docs.docker.com/guides/r/deploy/)

[Test your deployment](https://docs.docker.com/guides/r/deploy/)

[Â« Back to all guides](https://docs.docker.com/guides/)

# Use containers for R development

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Prerequisites

Complete [Containerize a R application](https://docs.docker.com/guides/r/containerize/).

## Overview

In this section, you'll learn how to set up a development environment for your containerized application. This includes:

  * Adding a local database and persisting data   * Configuring Compose to automatically update your running Compose services as you edit and save your code

## Get the sample application

You'll need to clone a new repository to get a sample application that includes logic to connect to the database.

Change to a directory where you want to clone the repository and run the following command.               $ git clone https://github.com/mfranzon/r-docker-dev.git     

## Configure the application to use the database

To try the connection between the Shiny application and the local database you have to modify the `Dockerfile` changing the `COPY` instruction:               -COPY src/ .     +COPY src_db/ .     

## Add a local database and persist data

You can use containers to set up local services, like a database. In this section, you'll update the `compose.yaml` file to define a database service and a volume to persist data.

In the cloned repository's directory, open the `compose.yaml` file in an IDE or text editor.

In the `compose.yaml` file, you need to un-comment the properties for configuring the database. You must also mount the database password file and set an environment variable on the `shiny-app` service pointing to the location of the file in the container.

The following is the updated `compose.yaml` file.               services:       shiny-app:         build:           context: .           dockerfile: Dockerfile         ports:           - 3838:3838         environment:           - POSTGRES_PASSWORD_FILE=/run/secrets/db-password         depends_on:           db:             condition: service_healthy         secrets:           - db-password       db:         image: postgres         restart: always         user: postgres         secrets:           - db-password         volumes:           - db-data:/var/lib/postgresql/data         environment:           - POSTGRES_DB=example           - POSTGRES_PASSWORD_FILE=/run/secrets/db-password         expose:           - 5432         healthcheck:           test: ["CMD", "pg_isready"]           interval: 10s           timeout: 5s           retries: 5     volumes:       db-data:     secrets:       db-password:         file: db/password.txt

> Note >  > To learn more about the instructions in the Compose file, see [Compose file reference](https://docs.docker.com/reference/compose-file/).

Before you run the application using Compose, notice that this Compose file specifies a `password.txt` file to hold the database's password. You must create this file as it's not included in the source repository.

In the cloned repository's directory, create a new directory named `db` and inside that directory create a file named `password.txt` that contains the password for the database. Using your favorite IDE or text editor, add the following contents to the `password.txt` file.               mysecretpassword

Save and close the `password.txt` file.

You should now have the following contents in your `r-docker-dev` directory.               âââ r-docker-dev/     â âââ db/     â â âââ password.txt     â âââ src/     â â âââ app.R     â âââ src_db/     â â âââ app_db.R     â âââ requirements.txt     â âââ .dockerignore     â âââ compose.yaml     â âââ Dockerfile     â âââ README.Docker.md     â âââ README.md

Now, run the following `docker compose up` command to start your application.               $ docker compose up --build     

Now test your DB connection opening a browser at:               http://localhost:3838     

You should see a pop-up message:               DB CONNECTED

Press `ctrl+c` in the terminal to stop your application.

## Automatically update services

Use Compose Watch to automatically update your running Compose services as you edit and save your code. For more details about Compose Watch, see [Use Compose Watch](https://docs.docker.com/compose/how-tos/file-watch/).

Lines 15 to 18 in the `compose.yaml` file contain properties that trigger Docker to rebuild the image when a file in the current working directory is changed:                1      2      3      4      5      6      7      8      9     10     11     12     13     14     15     16     17     18     19     20     21     22     23     24     25     26     27     28     29     30     31     32     33     34     35     36     37     38     39     40     41     

|                services:       shiny-app:         build:           context: .           dockerfile: Dockerfile         ports:           - 3838:3838         environment:           - POSTGRES_PASSWORD_FILE=/run/secrets/db-password         depends_on:           db:             condition: service_healthy         secrets:           - db-password         develop:           watch:             - action: rebuild               path: .       db:         image: postgres         restart: always         user: postgres         secrets:           - db-password         volumes:           - db-data:/var/lib/postgresql/data         environment:           - POSTGRES_DB=example           - POSTGRES_PASSWORD_FILE=/run/secrets/db-password         expose:           - 5432         healthcheck:           test: ["CMD", "pg_isready"]           interval: 10s           timeout: 5s           retries: 5     volumes:       db-data:     secrets:       db-password:         file: db/password.txt      ---|---      Run the following command to run your application with Compose Watch.               $ docker compose watch     

Now, if you modify your `app.R` you will see the changes in real time without re-building the image\!

Press `ctrl+c` in the terminal to stop your application.

## Summary

In this section, you took a look at setting up your Compose file to add a local database and persist data. You also learned how to use Compose Watch to automatically rebuild and run your container when you update your code.

Related information:

  * [Compose file reference](https://docs.docker.com/reference/compose-file/)   * [Compose file watch](https://docs.docker.com/compose/how-tos/file-watch/)   * [Multi-stage builds](https://docs.docker.com/build/building/multi-stage/)

## Next steps

In the next section, you'll take a look at how to set up a CI/CD pipeline using GitHub Actions.

[Configure CI/CD for your R application Â»](https://docs.docker.com/guides/r/configure-ci-cd/)