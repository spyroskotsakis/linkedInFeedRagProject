# Run your tests | Docker Docs

**URL:** https://docs.docker.com/guides/angular/run-tests
**Word Count:** 470
**Links Count:** 74
**Scraped:** 2025-07-16 02:04:23
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

# Run Angular tests in a container

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Prerequisites

Complete all the previous sections of this guide, starting with [Containerize Angular application](https://docs.docker.com/guides/angular/containerize/).

## Overview

Testing is a critical part of the development process. In this section, you'll learn how to:

  * Run Jasmine unit tests using the Angular CLI inside a Docker container.   * Use Docker Compose to isolate your test environment.   * Ensure consistency between local and container-based testing.

The `docker-angular-sample` project comes pre-configured with Jasmine, so you can get started quickly without extra setup.

* * *

## Run tests during development

The `docker-angular-sample` application includes a sample test file at the following location:               $ src/app/app.component.spec.ts     

This test uses Jasmine to validate the AppComponent logic.

### Step 1: Update compose.yaml

Add a new service named `angular-test` to your `compose.yaml` file. This service allows you to run your test suite in an isolated, containerized environment.                1      2      3      4      5      6      7      8      9     10     11     12     13     14     15     16     17     18     19     20     21     22     23     24     25     26     

|                services:       angular-dev:         build:           context: .           dockerfile: Dockerfile.dev         ports:           - "5173:5173"         develop:           watch:             - action: sync               path: .               target: /app            angular-prod:         build:           context: .           dockerfile: Dockerfile         image: docker-angular-sample         ports:           - "8080:8080"            angular-test:         build:           context: .           dockerfile: Dockerfile.dev         command: ["npm", "run", "test"]      ---|---      The angular-test service reuses the same `Dockerfile.dev` used for [development](https://docs.docker.com/guides/angular/develop/) and overrides the default command to run tests with `npm run test`. This setup ensures a consistent test environment that matches your local development configuration.

After completing the previous steps, your project directory should contain the following files:               âââ docker-angular-sample/     â âââ Dockerfile     â âââ Dockerfile.dev     â âââ .dockerignore     â âââ compose.yaml     â âââ nginx.conf     â âââ README.Docker.md

### Step 2: Run the tests

To execute your test suite inside the container, run the following command from your project root:               $ docker compose run --rm angular-test     

This command will:

  * Start the `angular-test` service defined in your `compose.yaml` file.   * Execute the `npm run test` script using the same environment as development.   * Automatically removes the container after tests complete, using the [`docker compose run --rm`](https://docs.docker.com/engine/reference/commandline/compose_run) command.

You should see output similar to the following:               Test Suites: 1 passed, 1 total     Tests:       3 passed, 3 total     Snapshots:   0 total     Time:        1.529 s

> Note >  > For more information about Compose commands, see the [Compose CLI reference](https://docs.docker.com/reference/cli/docker/compose/).

* * *

## Summary

In this section, you learned how to run unit tests for your Angular application inside a Docker container using Jasmine and Docker Compose.

What you accomplished:

  * Created a `angular-test` service in `compose.yaml` to isolate test execution.   * Reused the development `Dockerfile.dev` to ensure consistency between dev and test environments.   * Ran tests inside the container using `docker compose run --rm angular-test`.   * Ensured reliable, repeatable testing across environments without depending on your local machine setup.

* * *

## Related resources

Explore official references and best practices to sharpen your Docker testing workflow:

  * [Dockerfile reference](https://docs.docker.com/reference/dockerfile/) â Understand all Dockerfile instructions and syntax.   * [Best practices for writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/) â Write efficient, maintainable, and secure Dockerfiles.   * [Compose file reference](https://docs.docker.com/compose/compose-file/) â Learn the full syntax and options available for configuring services in `compose.yaml`.   * [`docker compose run` CLI reference](https://docs.docker.com/reference/cli/docker/compose/run/) â Run one-off commands in a service container.

* * *

## Next steps

Next, youâll learn how to set up a CI/CD pipeline using GitHub Actions to automatically build and test your Angular application in a containerized environment. This ensures your code is validated on every push or pull request, maintaining consistency and reliability across your development workflow.

[Automate your builds with GitHub Actions Â»](https://docs.docker.com/guides/angular/configure-github-actions/)