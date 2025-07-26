# Containerize your app | Docker Docs

**URL:** https://docs.docker.com/guides/r/containerize
**Word Count:** 313
**Links Count:** 70
**Scraped:** 2025-07-16 02:04:38
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

# Containerize a R application

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Prerequisites

  * You have a [git client](https://git-scm.com/downloads). The examples in this section use a command-line based git client, but you can use any client.

## Overview

This section walks you through containerizing and running a R application.

## Get the sample application

The sample application uses the popular [Shiny](https://shiny.posit.co/) framework.

Clone the sample application to use with this guide. Open a terminal, change directory to a directory that you want to work in, and run the following command to clone the repository:               $ git clone https://github.com/mfranzon/r-docker-dev.git && cd r-docker-dev     

You should now have the following contents in your `r-docker-dev` directory.               âââ r-docker-dev/     â âââ src/     â â âââ app.R     â âââ src_db/     â â âââ app_db.R     â âââ compose.yaml     â âââ Dockerfile     â âââ README.md

To learn more about the files in the repository, see the following:

  * [Dockerfile](https://docs.docker.com/reference/dockerfile/)   * [.dockerignore](https://docs.docker.com/reference/dockerfile/#dockerignore-file)   * [compose.yaml](https://docs.docker.com/reference/compose-file/)

## Run the application

Inside the `r-docker-dev` directory, run the following command in a terminal.               $ docker compose up --build     

Open a browser and view the application at <http://localhost:3838>. You should see a simple Shiny application.

In the terminal, press `ctrl`+`c` to stop the application.

### Run the application in the background

You can run the application detached from the terminal by adding the `-d` option. Inside the `r-docker-dev` directory, run the following command in a terminal.               $ docker compose up --build -d     

Open a browser and view the application at <http://localhost:3838>.

You should see a simple Shiny application.

In the terminal, run the following command to stop the application.               $ docker compose down     

For more information about Compose commands, see the [Compose CLI reference](https://docs.docker.com/reference/cli/docker/compose/).

## Summary

In this section, you learned how you can containerize and run your R application using Docker.

Related information:

  * [Docker Compose overview](https://docs.docker.com/compose/)

## Next steps

In the next section, you'll learn how you can develop your application using containers.

[Use containers for R development Â»](https://docs.docker.com/guides/r/develop/)