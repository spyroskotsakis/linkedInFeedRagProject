# React.js | Docker Docs

**URL:** https://docs.docker.com/guides/reactjs/
**Word Count:** 332
**Links Count:** 56
**Scraped:** 2025-07-16 01:54:11
**Status:** completed

---

Back

[Guides](https://docs.docker.com/guides/)

  * [Get started](https://docs.docker.com/get-started/)   * [Manuals](https://docs.docker.com/manuals/)   * [Reference](https://docs.docker.com/reference/)

* * *

[React.js language-specific guide](https://docs.docker.com/guides/reactjs/)

This guide explains how to containerize React.js applications using Docker.

![](https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg) JavaScript

20 minutes

[1](https://docs.docker.com/guides/reactjs/containerize/)

[Containerize](https://docs.docker.com/guides/reactjs/containerize/)

[2](https://docs.docker.com/guides/reactjs/develop/)

[Develop your app](https://docs.docker.com/guides/reactjs/develop/)

[3](https://docs.docker.com/guides/reactjs/run-tests/)

[Run your tests](https://docs.docker.com/guides/reactjs/run-tests/)

[4](https://docs.docker.com/guides/reactjs/configure-github-actions/)

[Automate your builds with GitHub Actions](https://docs.docker.com/guides/reactjs/configure-github-actions/)

[5](https://docs.docker.com/guides/reactjs/deploy/)

[Test your deployment](https://docs.docker.com/guides/reactjs/deploy/)

[Â« Back to all guides](https://docs.docker.com/guides/)

# React.js language-specific guide

Table of contents

* * *

The React.js language-specific guide shows you how to containerize a React.js application using Docker, following best practices for creating efficient, production-ready containers.

[React.js](https://react.dev/) is a widely used library for building interactive user interfaces. However, managing dependencies, environments, and deployments efficiently can be complex. Docker simplifies this process by providing a consistent and containerized environment.

> **Acknowledgment** >  > Docker extends its sincere gratitude to [Kristiyan Velkov](https://www.linkedin.com/in/kristiyan-velkov-763130b3/) for authoring this guide. As a Docker Captain and experienced Front-end engineer, his expertise in Docker, DevOps, and modern web development has made this resource invaluable for the community, helping developers navigate and optimize their Docker workflows.

* * *

## What will you learn?

In this guide, you will learn how to:

  * Containerize and run a React.js application using Docker.   * Set up a local development environment for React.js inside a container.   * Run tests for your React.js application within a Docker container.   * Configure a CI/CD pipeline using GitHub Actions for your containerized app.   * Deploy the containerized React.js application to a local Kubernetes cluster for testing and debugging.

To begin, youâll start by containerizing an existing React.js application.

* * *

## Prerequisites

Before you begin, make sure you're familiar with the following:

  * Basic understanding of [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) or [TypeScript](https://www.typescriptlang.org/).   * Basic knowledge of [Node.js](https://nodejs.org/en) and [npm](https://docs.npmjs.com/about-npm) for managing dependencies and running scripts.   * Familiarity with [React.js](https://react.dev/) fundamentals.   * Understanding of Docker concepts such as images, containers, and Dockerfiles. If you're new to Docker, start with the [Docker basics](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/) guide.

Once you've completed the React.js getting started modules, youâll be ready to containerize your own React.js application using the examples and instructions provided in this guide.

## Modules

  1. [Containerize](https://docs.docker.com/guides/reactjs/containerize/)

Learn how to containerize a React.js application with Docker by creating an optimized, production-ready image using best practices for performance, security, and scalability.

  2. [Develop your app](https://docs.docker.com/guides/reactjs/develop/)

Learn how to develop your React.js application locally using containers.

  3. [Run your tests](https://docs.docker.com/guides/reactjs/run-tests/)

Learn how to run your React.js tests in a container.

  4. [Automate your builds with GitHub Actions](https://docs.docker.com/guides/reactjs/configure-github-actions/)

Learn how to configure CI/CD using GitHub Actions for your React.js application.

  5. [Test your deployment](https://docs.docker.com/guides/reactjs/deploy/)

Learn how to deploy locally to test and debug your Kubernetes deployment