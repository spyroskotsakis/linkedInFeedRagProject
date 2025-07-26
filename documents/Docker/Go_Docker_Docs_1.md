# Go | Docker Docs

**URL:** https://docs.docker.com/guides/golang/
**Word Count:** 332
**Links Count:** 60
**Scraped:** 2025-07-16 01:52:46
**Status:** completed

---

Back

[Guides](https://docs.docker.com/guides/)

  * [Get started](https://docs.docker.com/get-started/)   * [Manuals](https://docs.docker.com/manuals/)   * [Reference](https://docs.docker.com/reference/)

* * *

[Go language-specific guide](https://docs.docker.com/guides/golang/)

This guide teaches you how to containerize Go applications using Docker.

![](https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/go/go-original.svg) Go

30 minutes

[1](https://docs.docker.com/guides/golang/build-images/)

[Build images](https://docs.docker.com/guides/golang/build-images/)

[2](https://docs.docker.com/guides/golang/run-containers/)

[Run containers](https://docs.docker.com/guides/golang/run-containers/)

[3](https://docs.docker.com/guides/golang/develop/)

[Develop your app](https://docs.docker.com/guides/golang/develop/)

[4](https://docs.docker.com/guides/golang/run-tests/)

[Run your tests](https://docs.docker.com/guides/golang/run-tests/)

[5](https://docs.docker.com/guides/golang/configure-ci-cd/)

[Configure CI/CD](https://docs.docker.com/guides/golang/configure-ci-cd/)

[6](https://docs.docker.com/guides/golang/deploy/)

[Test your deployment](https://docs.docker.com/guides/golang/deploy/)

[Â« Back to all guides](https://docs.docker.com/guides/)

# Go language-specific guide

Table of contents

* * *

This guide will show you how to create, test, and deploy containerized Go applications using Docker.

> **Acknowledgment** >  > Docker would like to thank [Oliver Frolovs](https://www.linkedin.com/in/ofr/) for his contribution to this guide.

## What will you learn?

In this guide, youâll learn how to:

  * Create a `Dockerfile` which contains the instructions for building a container image for a program written in Go.   * Run the image as a container in your local Docker instance and manage the container's lifecycle.   * Use multi-stage builds for building small images efficiently while keeping your Dockerfiles easy to read and maintain.   * Use Docker Compose to orchestrate running of multiple related containers together in a development environment.   * Configure a CI/CD pipeline for your application using [GitHub Actions](https://docs.github.com/en/actions)   * Deploy your containerized Go application.

## Prerequisites

Some basic understanding of Go and its toolchain is assumed. This isn't a Go tutorial. If you are new to the : languages:, the [Go website](https://golang.org/) is a great place to explore, so _go_ \(pun intended\) check it out\!

You also must know some basic [Docker concepts](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/) as well as to be at least vaguely familiar with the [Dockerfile format](https://docs.docker.com/build/concepts/dockerfile/).

Your Docker set-up must have BuildKit enabled. BuildKit is enabled by default for all users on [Docker Desktop](https://docs.docker.com/desktop/). If you have installed Docker Desktop, you donât have to manually enable BuildKit. If you are running Docker on Linux, please check out BuildKit [getting started](https://docs.docker.com/build/buildkit/#getting-started) page.

Some familiarity with the command line is also expected.

## What's next?

The aim of this guide is to provide enough examples and instructions for you to containerize your own Go application and deploy it into the Cloud.

Start by building your first Go image.

## Modules

  1. [Build images](https://docs.docker.com/guides/golang/build-images/)

Learn how to build your first Docker image by writing a Dockerfile

  2. [Run containers](https://docs.docker.com/guides/golang/run-containers/)

Learn how to run the image as a container.

  3. [Develop your app](https://docs.docker.com/guides/golang/develop/)

Learn how to develop your application locally.

  4. [Run your tests](https://docs.docker.com/guides/golang/run-tests/)

How to build and run your Go tests in a container

  5. [Configure CI/CD](https://docs.docker.com/guides/golang/configure-ci-cd/)

Learn how to Configure CI/CD for your Go application

  6. [Test your deployment](https://docs.docker.com/guides/golang/deploy/)

Learn how to deploy your Go application