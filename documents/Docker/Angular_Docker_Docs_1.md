# Angular | Docker Docs

**URL:** https://docs.docker.com/guides/angular/
**Word Count:** 349
**Links Count:** 56
**Scraped:** 2025-07-16 01:49:39
**Status:** completed

---

Back

[Guides](https://docs.docker.com/guides/)

  * [Get started](https://docs.docker.com/get-started/)   * [Manuals](https://docs.docker.com/manuals/)   * [Reference](https://docs.docker.com/reference/)

* * *

[Angular language-specific guide](https://docs.docker.com/guides/angular/)

This guide explains how to containerize Angular applications using Docker.

![](https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg) JavaScript

20 minutes

[1](https://docs.docker.com/guides/angular/containerize/)

[Containerize](https://docs.docker.com/guides/angular/containerize/)

[2](https://docs.docker.com/guides/angular/develop/)

[Develop your app](https://docs.docker.com/guides/angular/develop/)

[3](https://docs.docker.com/guides/angular/run-tests/)

[Run your tests](https://docs.docker.com/guides/angular/run-tests/)

[4](https://docs.docker.com/guides/angular/configure-github-actions/)

[Automate your builds with GitHub Actions](https://docs.docker.com/guides/angular/configure-github-actions/)

[5](https://docs.docker.com/guides/angular/deploy/)

[Test your deployment](https://docs.docker.com/guides/angular/deploy/)

[Â« Back to all guides](https://docs.docker.com/guides/)

# Angular language-specific guide

Table of contents

* * *

The Angular language-specific guide shows you how to containerize an Angular application using Docker, following best practices for creating efficient, production-ready containers.

[Angular](https://angular.dev/) is a robust and widely adopted framework for building dynamic, enterprise-grade web applications. However, managing dependencies, environments, and deployments can become complex as applications scale. Docker streamlines these challenges by offering a consistent, isolated environment for development and production.

> **Acknowledgment** >  > Docker extends its sincere gratitude to [Kristiyan Velkov](https://www.linkedin.com/in/kristiyan-velkov-763130b3/) for authoring this guide. As a Docker Captain and experienced Front-end engineer, his expertise in Docker, DevOps, and modern web development has made this resource essential for the community, helping developers navigate and optimize their Docker workflows.

* * *

## What will you learn?

In this guide, you will learn how to:

  * Containerize and run an Angular application using Docker.   * Set up a local development environment for Angular inside a container.   * Run tests for your Angular application within a Docker container.   * Configure a CI/CD pipeline using GitHub Actions for your containerized app.   * Deploy the containerized Angular application to a local Kubernetes cluster for testing and debugging.

You'll start by containerizing an existing Angular application and work your way up to production-level deployments.

* * *

## Prerequisites

Before you begin, ensure you have a working knowledge of:

  * Basic understanding of [TypeScript](https://www.typescriptlang.org/) and [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript).   * Familiarity with [Node.js](https://nodejs.org/en) and [npm](https://docs.npmjs.com/about-npm) for managing dependencies and running scripts.   * Familiarity with [Angular](https://angular.io/) fundamentals.   * Understanding of core Docker concepts such as images, containers, and Dockerfiles. If you're new to Docker, start with the [Docker basics](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/) guide.

Once you've completed the Angular getting started modules, youâll be fully prepared to containerize your own Angular application using the detailed examples and best practices outlined in this guide.

## Modules

  1. [Containerize](https://docs.docker.com/guides/angular/containerize/)

Learn how to containerize an Angular application with Docker by creating an optimized, production-ready image using best practices for performance, security, and scalability.

  2. [Develop your app](https://docs.docker.com/guides/angular/develop/)

Learn how to develop your Angular application locally using containers.

  3. [Run your tests](https://docs.docker.com/guides/angular/run-tests/)

Learn how to run your Angular tests in a container.

  4. [Automate your builds with GitHub Actions](https://docs.docker.com/guides/angular/configure-github-actions/)

Learn how to configure CI/CD using GitHub Actions for your Angular application.

  5. [Test your deployment](https://docs.docker.com/guides/angular/deploy/)

Learn how to deploy locally to test and debug your Kubernetes deployment