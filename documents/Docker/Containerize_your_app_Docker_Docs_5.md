# Containerize your app | Docker Docs

**URL:** https://docs.docker.com/guides/dotnet/containerize/
**Word Count:** 471
**Links Count:** 78
**Scraped:** 2025-07-16 01:46:03
**Status:** completed

---

Back

[Guides](https://docs.docker.com/guides/)

  * [Get started](https://docs.docker.com/get-started/)   * [Manuals](https://docs.docker.com/manuals/)   * [Reference](https://docs.docker.com/reference/)

* * *

[.NET language-specific guide](https://docs.docker.com/guides/dotnet/)

Learn how to containerize .NET applications using Docker.

![](https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/csharp/csharp-original.svg) C\#

20 minutes

[1](https://docs.docker.com/guides/dotnet/containerize/)

[Containerize your app](https://docs.docker.com/guides/dotnet/containerize/)

[2](https://docs.docker.com/guides/dotnet/develop/)

[Develop your app](https://docs.docker.com/guides/dotnet/develop/)

[3](https://docs.docker.com/guides/dotnet/run-tests/)

[Run your tests](https://docs.docker.com/guides/dotnet/run-tests/)

[4](https://docs.docker.com/guides/dotnet/configure-ci-cd/)

[Configure CI/CD](https://docs.docker.com/guides/dotnet/configure-ci-cd/)

[5](https://docs.docker.com/guides/dotnet/deploy/)

[Test your deployment](https://docs.docker.com/guides/dotnet/deploy/)

[Â« Back to all guides](https://docs.docker.com/guides/)

# Containerize a .NET application

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Prerequisites

  * You have installed the latest version of [Docker Desktop](https://docs.docker.com/get-started/get-docker/).   * You have a [git client](https://git-scm.com/downloads). The examples in this section use a command-line based git client, but you can use any client.

## Overview

This section walks you through containerizing and running a .NET application.

## Get the sample applications

In this guide, you will use a pre-built .NET application. The application is similar to the application built in the Docker Blog article, [Building a Multi-Container .NET App Using Docker Desktop](https://www.docker.com/blog/building-multi-container-net-app-using-docker-desktop/).

Open a terminal, change directory to a directory that you want to work in, and run the following command to clone the repository.               $ git clone https://github.com/docker/docker-dotnet-sample     

## Initialize Docker assets

Now that you have an application, you can use `docker init` to create the necessary Docker assets to containerize your application. Inside the `docker-dotnet-sample` directory, run the `docker init` command in a terminal. `docker init` provides some default configuration, but you'll need to answer a few questions about your application. Refer to the following example to answer the prompts from `docker init` and use the same answers for your prompts.               $ docker init     Welcome to the Docker Init CLI!          This utility will walk you through creating the following files with sensible defaults for your project:       - .dockerignore       - Dockerfile       - compose.yaml       - README.Docker.md          Let's get started!          ? What application platform does your project use? ASP.NET Core     ? What's the name of your solution's main project? myWebApp     ? What version of .NET do you want to use? 8.0     ? What local port do you want to use to access your server? 8080     

You should now have the following contents in your `docker-dotnet-sample` directory.               âââ docker-dotnet-sample/     â âââ .git/     â âââ src/     â âââ .dockerignore     â âââ compose.yaml     â âââ Dockerfile     â âââ README.Docker.md     â âââ README.md

To learn more about the files that `docker init` added, see the following:

  * [Dockerfile](https://docs.docker.com/reference/dockerfile/)   * [.dockerignore](https://docs.docker.com/reference/dockerfile/#dockerignore-file)   * [compose.yaml](https://docs.docker.com/reference/compose-file/)

## Run the application

Inside the `docker-dotnet-sample` directory, run the following command in a terminal.               $ docker compose up --build     

Open a browser and view the application at <http://localhost:8080>. You should see a simple web application.

In the terminal, press `ctrl`+`c` to stop the application.

### Run the application in the background

You can run the application detached from the terminal by adding the `-d` option. Inside the `docker-dotnet-sample` directory, run the following command in a terminal.               $ docker compose up --build -d     

Open a browser and view the application at <http://localhost:8080>. You should see a simple web application.

In the terminal, run the following command to stop the application.               $ docker compose down     

For more information about Compose commands, see the [Compose CLI reference](https://docs.docker.com/reference/cli/docker/compose/).

## Summary

In this section, you learned how you can containerize and run your .NET application using Docker.

Related information:

  * [Dockerfile reference](https://docs.docker.com/reference/dockerfile/)   * [.dockerignore file reference](https://docs.docker.com/reference/dockerfile/#dockerignore-file)   * [Docker Compose overview](https://docs.docker.com/compose/)

## Next steps

In the next section, you'll learn how you can develop your application using Docker containers.

[Use containers for .NET development Â»](https://docs.docker.com/guides/dotnet/develop/)