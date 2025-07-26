# Containerize your app | Docker Docs

**URL:** https://docs.docker.com/guides/nodejs/containerize/
**Word Count:** 861
**Links Count:** 77
**Scraped:** 2025-07-16 01:46:03
**Status:** completed

---

Back

[Guides](https://docs.docker.com/guides/)

  * [Get started](https://docs.docker.com/get-started/)   * [Manuals](https://docs.docker.com/manuals/)   * [Reference](https://docs.docker.com/reference/)

* * *

[Node.js language-specific guide](https://docs.docker.com/guides/nodejs/)

This guide explains how to containerize Node.js applications using Docker.

![](https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg) JavaScript

20 minutes

[1](https://docs.docker.com/guides/nodejs/containerize/)

[Containerize your app](https://docs.docker.com/guides/nodejs/containerize/)

[2](https://docs.docker.com/guides/nodejs/develop/)

[Develop your app](https://docs.docker.com/guides/nodejs/develop/)

[3](https://docs.docker.com/guides/nodejs/run-tests/)

[Run your tests](https://docs.docker.com/guides/nodejs/run-tests/)

[4](https://docs.docker.com/guides/nodejs/configure-ci-cd/)

[Configure CI/CD](https://docs.docker.com/guides/nodejs/configure-ci-cd/)

[5](https://docs.docker.com/guides/nodejs/deploy/)

[Test your deployment](https://docs.docker.com/guides/nodejs/deploy/)

[Â« Back to all guides](https://docs.docker.com/guides/)

# Containerize a Node.js application

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Prerequisites

  * You have installed the latest version of [Docker Desktop](https://docs.docker.com/get-started/get-docker/).   * You have a [git client](https://git-scm.com/downloads). The examples in this section use a command-line based git client, but you can use any client.

## Overview

This section walks you through containerizing and running a Node.js application.

## Get the sample application

Clone the sample application to use with this guide. Open a terminal, change directory to a directory that you want to work in, and run the following command to clone the repository:               $ git clone https://github.com/docker/docker-nodejs-sample && cd docker-nodejs-sample     

## Initialize Docker assets

Now that you have an application, you can create the necessary Docker assets to containerize your application. You can use Docker Desktop's built-in Docker Init feature to help streamline the process, or you can manually create the assets.

Use Docker Init  Manually create assets

Inside the `docker-nodejs-sample` directory, run the `docker init` command in a terminal. `docker init` provides some default configuration, but you'll need to answer a few questions about your application. Refer to the following example to answer the prompts from `docker init` and use the same answers for your prompts.               $ docker init     Welcome to the Docker Init CLI!          This utility will walk you through creating the following files with sensible defaults for your project:       - .dockerignore       - Dockerfile       - compose.yaml       - README.Docker.md          Let's get started!          ? What application platform does your project use? Node     ? What version of Node do you want to use? 18.0.0     ? Which package manager do you want to use? npm     ? What command do you want to use to start the app: node src/index.js     ? What port does your server listen on? 3000     

If you don't have Docker Desktop installed or prefer creating the assets manually, you can create the following files in your project directory.

Create a file named `Dockerfile` with the following contents.

Dockerfile

Show more               # syntax=docker/dockerfile:1          # Comments are provided throughout this file to help you get started.     # If you need more help, visit the Dockerfile reference guide at     # https://docs.docker.com/go/dockerfile-reference/          # Want to help us make this template better? Share your feedback here: https://forms.gle/ybq9Krt8jtBL3iCk7          ARG NODE_VERSION=18.0.0          FROM node:${NODE_VERSION}-alpine          # Use production node environment by default.     ENV NODE_ENV production               WORKDIR /usr/src/app          # Download dependencies as a separate step to take advantage of Docker's caching.     # Leverage a cache mount to /root/.npm to speed up subsequent builds.     # Leverage a bind mounts to package.json and package-lock.json to avoid having to copy them into     # into this layer.     RUN --mount=type=bind,source=package.json,target=package.json \         --mount=type=bind,source=package-lock.json,target=package-lock.json \         --mount=type=cache,target=/root/.npm \         npm ci --omit=dev          # Run the application as a non-root user.     USER node          # Copy the rest of the source files into the image.     COPY . .          # Expose the port that the application listens on.     EXPOSE 3000          # Run the application.     CMD node src/index.js

Hide

Create a file named `compose.yaml` with the following contents.

compose.yaml

Show more               # Comments are provided throughout this file to help you get started.     # If you need more help, visit the Docker Compose reference guide at     # https://docs.docker.com/go/compose-spec-reference/          # Here the instructions define your application as a service called "server".     # This service is built from the Dockerfile in the current directory.     # You can add other services your application may depend on here, such as a     # database or a cache. For examples, see the Awesome Compose repository:     # https://github.com/docker/awesome-compose     services:       server:         build:           context: .         environment:           NODE_ENV: production         ports:           - 3000:3000     # The commented out section below is an example of how to define a PostgreSQL     # database that your application can use. `depends_on` tells Docker Compose to     # start the database before your application. The `db-data` volume persists the     # database data between container restarts. The `db-password` secret is used     # to set the database password. You must create `db/password.txt` and add     # a password of your choosing to it before running `docker compose up`.     #     depends_on:     #       db:     #         condition: service_healthy     #   db:     #     image: postgres     #     restart: always     #     user: postgres     #     secrets:     #       - db-password     #     volumes:     #       - db-data:/var/lib/postgresql/data     #     environment:     #       - POSTGRES_DB=example     #       - POSTGRES_PASSWORD_FILE=/run/secrets/db-password     #     expose:     #       - 5432     #     healthcheck:     #       test: [ "CMD", "pg_isready" ]     #       interval: 10s     #       timeout: 5s     #       retries: 5     # volumes:     #   db-data:     # secrets:     #   db-password:     #     file: db/password.txt

Hide

Create a file named `.dockerignore` with the following contents.

.dockerignore

Show more               # Include any files or directories that you don't want to be copied to your     # container here (e.g., local build artifacts, temporary files, etc.).     #     # For more help, visit the .dockerignore file reference guide at     # https://docs.docker.com/go/build-context-dockerignore/          **/.classpath     **/.dockerignore     **/.env     **/.git     **/.gitignore     **/.project     **/.settings     **/.toolstarget     **/.vs     **/.vscode     **/.next     **/.cache     **/*.*proj.user     **/*.dbmdl     **/*.jfm     **/charts     **/docker-compose*     **/compose.y*ml     **/Dockerfile*     **/node_modules     **/npm-debug.log     **/obj     **/secrets.dev.yaml     **/values.dev.yaml     **/build     **/dist     LICENSE     README.md

Hide

You should now have at least the following contents in your `docker-nodejs-sample` directory.               âââ docker-nodejs-sample/     â âââ spec/     â âââ src/     â âââ .dockerignore     â âââ .gitignore     â âââ compose.yaml     â âââ Dockerfile     â âââ package-lock.json     â âââ package.json     â âââ README.md

To learn more about the files, see the following:

  * [Dockerfile](https://docs.docker.com/reference/dockerfile/)   * [.dockerignore](https://docs.docker.com/reference/dockerfile/#dockerignore-file)   * [compose.yaml](https://docs.docker.com/reference/compose-file/)

## Run the application

Inside the `docker-nodejs-sample` directory, run the following command in a terminal.               $ docker compose up --build     

Open a browser and view the application at <http://localhost:3000>. You should see a simple todo application.

In the terminal, press `ctrl`+`c` to stop the application.

### Run the application in the background

You can run the application detached from the terminal by adding the `-d` option. Inside the `docker-nodejs-sample` directory, run the following command in a terminal.               $ docker compose up --build -d     

Open a browser and view the application at <http://localhost:3000>.

You should see a simple todo application.

In the terminal, run the following command to stop the application.               $ docker compose down     

For more information about Compose commands, see the [Compose CLI reference](https://docs.docker.com/reference/cli/docker/compose/).

## Summary

In this section, you learned how you can containerize and run your Node.js application using Docker.

Related information:

  * [Dockerfile reference](https://docs.docker.com/reference/dockerfile/)   * [.dockerignore file reference](https://docs.docker.com/reference/dockerfile/#dockerignore-file)   * [Docker Compose overview](https://docs.docker.com/compose/)

## Next steps

In the next section, you'll learn how you can develop your application using containers.

[Use containers for Node.js development Â»](https://docs.docker.com/guides/nodejs/develop/)