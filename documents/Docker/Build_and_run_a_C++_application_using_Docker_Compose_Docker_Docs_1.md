# Build and run a C++ application using Docker Compose | Docker Docs

**URL:** https://docs.docker.com/guides/cpp/containerize/
**Word Count:** 315
**Links Count:** 73
**Scraped:** 2025-07-16 01:46:03
**Status:** completed

---

Back

[Guides](https://docs.docker.com/guides/)

  * [Get started](https://docs.docker.com/get-started/)   * [Manuals](https://docs.docker.com/manuals/)   * [Reference](https://docs.docker.com/reference/)

* * *

[C++ language-specific guide](https://docs.docker.com/guides/cpp/)

This guide explains how to containerize C++ applications using Docker.

![](https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/cplusplus/cplusplus-original.svg) C++

20 minutes

[1](https://docs.docker.com/guides/cpp/multistage/)

[Containerize your app using a multi-stage build](https://docs.docker.com/guides/cpp/multistage/)

[2](https://docs.docker.com/guides/cpp/containerize/)

[Build and run a C++ application using Docker Compose](https://docs.docker.com/guides/cpp/containerize/)

[3](https://docs.docker.com/guides/cpp/develop/)

[Develop your app](https://docs.docker.com/guides/cpp/develop/)

[4](https://docs.docker.com/guides/cpp/configure-ci-cd/)

[Configure CI/CD](https://docs.docker.com/guides/cpp/configure-ci-cd/)

[5](https://docs.docker.com/guides/cpp/deploy/)

[Test your deployment](https://docs.docker.com/guides/cpp/deploy/)

[6](https://docs.docker.com/guides/cpp/security/)

[Supply-chain security](https://docs.docker.com/guides/cpp/security/)

[Â« Back to all guides](https://docs.docker.com/guides/)

# Containerize a C++ application

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Prerequisites

  * You have a [Git client](https://git-scm.com/downloads). The examples in this section use a command-line based Git client, but you can use any client.

## Overview

This section walks you through containerizing and running a C++ application, using Docker Compose.

## Get the sample application

We're using the same sample repository that you used in the previous sections of this guide. If you haven't already cloned the repository, clone it now:               $ git clone https://github.com/dockersamples/c-plus-plus-docker.git     

You should now have the following contents in your `c-plus-plus-docker` \(root\) directory.               âââ c-plus-plus-docker/     â âââ compose.yml     â âââ Dockerfile     â âââ LICENSE     â âââ ok_api.cpp     â âââ README.md

To learn more about the files in the repository, see the following:

  * [Dockerfile](https://docs.docker.com/reference/dockerfile/)   * [.dockerignore](https://docs.docker.com/reference/dockerfile/#dockerignore-file)   * [compose.yml](https://docs.docker.com/reference/compose-file/)

## Run the application

Inside the `c-plus-plus-docker` directory, run the following command in a terminal.               $ docker compose up --build     

Open a browser and view the application at <http://localhost:8080>. You will see a message `{"Status" : "OK"}` in the browser.

In the terminal, press `ctrl`+`c` to stop the application.

### Run the application in the background

You can run the application detached from the terminal by adding the `-d` option. Inside the `c-plus-plus-docker` directory, run the following command in a terminal.               $ docker compose up --build -d     

Open a browser and view the application at <http://localhost:8080>.

In the terminal, run the following command to stop the application.               $ docker compose down     

For more information about Compose commands, see the [Compose CLI reference](https://docs.docker.com/reference/cli/docker/compose/).

## Summary

In this section, you learned how you can containerize and run your C++ application using Docker.

Related information:

  * [Docker Compose overview](https://docs.docker.com/compose/)

## Next steps

In the next section, you'll learn how you can develop your application using containers.

[Use containers for C++ development Â»](https://docs.docker.com/guides/cpp/develop/)