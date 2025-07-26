# Run your tests | Docker Docs

**URL:** https://docs.docker.com/guides/reactjs/run-tests/
**Word Count:** 579
**Links Count:** 83
**Scraped:** 2025-07-16 01:48:09
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

# Run React.js tests in a container

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Prerequisites

Complete all the previous sections of this guide, starting with [Containerize React.js application](https://docs.docker.com/guides/reactjs/containerize/).

## Overview

Testing is a critical part of the development process. In this section, you'll learn how to:

  * Run unit tests using Vitest inside a Docker container.   * Use Docker Compose to run tests in an isolated, reproducible environment.

Youâll use [Vitest](https://vitest.dev) â a blazing fast test runner designed for Vite â along with [Testing Library](https://testing-library.com/) for assertions.

* * *

## Run tests during development

`docker-reactjs-sample` application includes a sample test file at location:               $ src/App.test.tsx     

This file uses Vitest and React Testing Library to verify the behavior of `App` component.

### Step 1: Install Vitest and React Testing Library

If you havenât already added the necessary testing tools, install them by running:               $ npm install --save-dev vitest @testing-library/react @testing-library/jest-dom jsdom     

Then, update the scripts section of your `package.json` file to include the following:               "scripts": {       "test": "vitest run"     }

* * *

### Step 2: Configure Vitest

Update `vitest.config.ts` file in your project root with the following configuration:                1      2      3      4      5      6      7      8      9     10     11     12     13     14     15     16     17     18     19     

|                /// <reference types="vitest" />          import { defineConfig } from "vite";     import react from "@vitejs/plugin-react";          export default defineConfig({       base: "/",       plugins: [react()],       server: {         host: true,         port: 5173,         strictPort: true,       },       test: {         environment: "jsdom",         setupFiles: "./src/setupTests.ts",         globals: true,       },     });      ---|---      > Note >  > The `test` options in `vitest.config.ts` are essential for reliable testing inside Docker: >  >   * `environment: "jsdom"` simulates a browser-like environment for rendering and DOM interactions. >   * `setupFiles: "./src/setupTests.ts"` loads global configuration or mocks before each test file \(optional but recommended\). >   * `globals: true` enables global test functions like `describe`, `it`, and `expect` without importing them. > 

>  > For more details, see the official [Vitest configuration docs](https://vitest.dev/config/).

### Step 3: Update compose.yaml

Add a new service named `react-test` to your `compose.yaml` file. This service allows you to run your test suite in an isolated containerized environment.                1      2      3      4      5      6      7      8      9     10     11     12     13     14     15     16     17     18     19     20     21     22     23     24     25     26     

|                services:       react-dev:         build:           context: .           dockerfile: Dockerfile.dev         ports:           - "5173:5173"         develop:           watch:             - action: sync               path: .               target: /app            react-prod:         build:           context: .           dockerfile: Dockerfile         image: docker-reactjs-sample         ports:           - "8080:8080"            react-test:         build:           context: .           dockerfile: Dockerfile.dev         command: ["npm", "run", "test"]      ---|---      The react-test service reuses the same `Dockerfile.dev` used for [development](https://docs.docker.com/guides/reactjs/develop/) and overrides the default command to run tests with `npm run test`. This setup ensures a consistent test environment that matches your local development configuration.

After completing the previous steps, your project directory should contain the following files:               âââ docker-reactjs-sample/     â âââ Dockerfile     â âââ Dockerfile.dev     â âââ .dockerignore     â âââ compose.yaml     â âââ nginx.conf     â âââ README.Docker.md

### Step 4: Run the tests

To execute your test suite inside the container, run the following command from your project root:               $ docker compose run --rm react-test     

This command will:

  * Start the `react-test` service defined in your `compose.yaml` file.   * Execute the `npm run test` script using the same environment as development.   * Automatically remove the container after the tests complete [`docker compose run --rm`](https://docs.docker.com/engine/reference/commandline/compose_run) command.

> Note >  > For more information about Compose commands, see the [Compose CLI reference](https://docs.docker.com/reference/cli/docker/compose/).

* * *

## Summary

In this section, you learned how to run unit tests for your React.js application inside a Docker container using Vitest and Docker Compose.

What you accomplished:

  * Installed and configured Vitest and React Testing Library for testing React components.   * Created a `react-test` service in `compose.yaml` to isolate test execution.   * Reused the development `Dockerfile.dev` to ensure consistency between dev and test environments.   * Ran tests inside the container using `docker compose run --rm react-test`.   * Ensured reliable, repeatable testing across environments without relying on local machine setup.

* * *

## Related resources

Explore official references and best practices to sharpen your Docker testing workflow:

  * [Dockerfile reference](https://docs.docker.com/reference/dockerfile/) â Understand all Dockerfile instructions and syntax.   * [Best practices for writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/) â Write efficient, maintainable, and secure Dockerfiles.   * [Compose file reference](https://docs.docker.com/compose/compose-file/) â Learn the full syntax and options available for configuring services in `compose.yaml`.   * [`docker compose run` CLI reference](https://docs.docker.com/reference/cli/docker/compose/run/) â Run one-off commands in a service container.

* * *

## Next steps

Next, youâll learn how to set up a CI/CD pipeline using GitHub Actions to automatically build and test your React.js application in a containerized environment. This ensures your code is validated on every push or pull request, maintaining consistency and reliability across your development workflow.

[Automate your builds with GitHub Actions Â»](https://docs.docker.com/guides/reactjs/configure-github-actions/)