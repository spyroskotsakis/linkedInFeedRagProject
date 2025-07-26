# Containerize your app using a multi-stage build | Docker Docs

**URL:** https://docs.docker.com/guides/cpp/multistage
**Word Count:** 508
**Links Count:** 66
**Scraped:** 2025-07-16 02:04:08
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

# Create a multi-stage build for your C++ application

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Prerequisites

  * You have a [Git client](https://git-scm.com/downloads). The examples in this section use a command-line based Git client, but you can use any client.

## Overview

This section walks you through creating a multi-stage Docker build for a C++ application. A multi-stage build is a Docker feature that allows you to use different base images for different stages of the build process, so you can optimize the size of your final image and separate build dependencies from runtime dependencies.

The standard practice for compiled languages like C++ is to have a build stage that compiles the code and a runtime stage that runs the compiled binary, because the build dependencies are not needed at runtime.

## Get the sample application

Let's use a simple C++ application that prints `Hello, World!` to the terminal. To do so, clone the sample repository to use with this guide:               $ git clone https://github.com/dockersamples/c-plus-plus-docker.git

The example for this section is under the `hello` directory in the repository. Get inside it and take a look at the files:               $ cd c-plus-plus-docker/hello     $ ls

You should see the following files:               Dockerfile  hello.cpp

## Check the Dockerfile

Open the `Dockerfile` in an IDE or text editor. The `Dockerfile` contains the instructions for building the Docker image.               # Stage 1: Build stage     FROM ubuntu:latest AS build          # Install build-essential for compiling C++ code     RUN apt-get update && apt-get install -y build-essential          # Set the working directory     WORKDIR /app          # Copy the source code into the container     COPY hello.cpp .          # Compile the C++ code statically to ensure it doesn't depend on runtime libraries     RUN g++ -o hello hello.cpp -static          # Stage 2: Runtime stage     FROM scratch          # Copy the static binary from the build stage     COPY --from=build /app/hello /hello          # Command to run the binary     CMD ["/hello"]

The `Dockerfile` has two stages:

  1. **Build stage** : This stage uses the `ubuntu:latest` image to compile the C++ code and create a static binary.   2. **Runtime stage** : This stage uses the `scratch` image, which is an empty image, to copy the static binary from the build stage and run it.

## Build the Docker image

To build the Docker image, run the following command in the `hello` directory:               $ docker build -t hello .

The `-t` flag tags the image with the name `hello`.

## Run the Docker container

To run the Docker container, use the following command:               $ docker run hello

You should see the output `Hello, World!` in the terminal.

## Summary

In this section, you learned how to create a multi-stage build for a C++ application. Multi-stage builds help you optimize the size of your final image and separate build dependencies from runtime dependencies. In this example, the final image only contains the static binary and doesn't include any build dependencies.

As the image has an empty base, the usual OS tools are also absent. So, for example, you can't run a simple `ls` command in the container:               $ docker run hello ls

This makes the image very lightweight and secure.

[Containerize a C++ application Â»](https://docs.docker.com/guides/cpp/containerize/)