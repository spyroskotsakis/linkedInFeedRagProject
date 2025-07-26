# Develop your app | Docker Docs

**URL:** https://docs.docker.com/guides/angular/develop
**Word Count:** 673
**Links Count:** 80
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

# Use containers for Angular development

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Prerequisites

Complete [Containerize Angular application](https://docs.docker.com/guides/angular/containerize/).

* * *

## Overview

In this section, you'll learn how to set up both production and development environments for your containerized Angular application using Docker Compose. This setup allows you to serve a static production build via Nginx and to develop efficiently inside containers using a live-reloading dev server with Compose Watch.

Youâll learn how to:

  * Configure separate containers for production and development   * Enable automatic file syncing using Compose Watch in development   * Debug and live-preview your changes in real-time without manual rebuilds

* * *

## Automatically update services \(Development Mode\)

Use Compose Watch to automatically sync source file changes into your containerized development environment. This provides a seamless, efficient development experience without restarting or rebuilding containers manually.

## Step 1: Create a development Dockerfile

Create a file named `Dockerfile.dev` in your project root with the following content:               # =========================================     # Stage 1: Development - Angular Application     # =========================================          # Define the Node.js version to use (Alpine for a small footprint)     ARG NODE_VERSION=22.14.0-alpine          # Set the base image for development     FROM node:${NODE_VERSION} AS dev          # Set environment variable to indicate development mode     ENV NODE_ENV=development          # Set the working directory inside the container     WORKDIR /app          # Copy only the dependency files first to optimize Docker caching     COPY package.json package-lock.json ./          # Install dependencies using npm with caching to speed up subsequent builds     RUN --mount=type=cache,target=/root/.npm npm ci          # Copy all application source files into the container     COPY . .          # Expose the port Angular uses for the dev server (default is 4200)     EXPOSE 4200          # Start the Angular dev server and bind it to all network interfaces     CMD ["npm", "start", "--", "--host=0.0.0.0"]

This file sets up a lightweight development environment for your Angular application using the dev server.

### Step 2: Update your `compose.yaml` file

Open your `compose.yaml` file and define two services: one for production \(`angular-prod`\) and one for development \(`angular-dev`\).

Hereâs an example configuration for an Angular application:               services:       angular-prod:         build:           context: .           dockerfile: Dockerfile         image: docker-angular-sample         ports:           - "8080:8080"            angular-dev:         build:           context: .           dockerfile: Dockerfile.dev         ports:           - "4200:4200"         develop:           watch:             - action: sync               path: .               target: /app

  * The `angular-prod` service builds and serves your static production app using Nginx.   * The `angular-dev` service runs your Angular development server with live reload and hot module replacement.   * `watch` triggers file sync with Compose Watch.

> Note >  > For more details, see the official guide: [Use Compose Watch](https://docs.docker.com/compose/how-tos/file-watch/).

After completing the previous steps, your project directory should now contain the following files:               âââ docker-angular-sample/     â âââ Dockerfile     â âââ Dockerfile.dev     â âââ .dockerignore     â âââ compose.yaml     â âââ nginx.conf     â âââ README.Docker.md

### Step 4: Start Compose Watch

Run the following command from the project root to start the container in watch mode               $ docker compose watch angular-dev     

### Step 5: Test Compose Watch with Angular

To verify that Compose Watch is working correctly:

  1. Open the `src/app/app.component.html` file in your text editor.

  2. Locate the following line:                    <h1>Docker Angular Sample Application</h1>

  3. Change it to:                    <h1>Hello from Docker Compose Watch</h1>

  4. Save the file.

  5. Open your browser at <http://localhost:4200>.

You should see the updated text appear instantly, without needing to rebuild the container manually. This confirms that file watching and automatic synchronization are working as expected.

* * *

## Summary

In this section, you set up a complete development and production workflow for your Angular application using Docker and Docker Compose.

Hereâs what you accomplished:

  * Created a `Dockerfile.dev` to streamline local development with hot reloading   * Defined separate `angular-dev` and `angular-prod` services in your `compose.yaml` file   * Enabled real-time file syncing using Compose Watch for a smoother development experience   * Verified that live updates work seamlessly by modifying and previewing a component

With this setup, you're now equipped to build, run, and iterate on your Angular app entirely within containersâefficiently and consistently across environments.

* * *

## Related resources

Deepen your knowledge and improve your containerized development workflow with these guides:

  * [Using Compose Watch](https://docs.docker.com/compose/how-tos/file-watch/) â Automatically sync source changes during development   * [Multi-stage builds](https://docs.docker.com/build/building/multi-stage/) â Create efficient, production-ready Docker images   * [Dockerfile best practices](https://docs.docker.com/build/building/best-practices/) â Write clean, secure, and optimized Dockerfiles.   * [Compose file reference](https://docs.docker.com/compose/compose-file/) â Learn the full syntax and options available for configuring services in `compose.yaml`.   * [Docker volumes](https://docs.docker.com/storage/volumes/) â Persist and manage data between container runs

## Next steps

In the next section, you'll learn how to run unit tests for your Angular application inside Docker containers. This ensures consistent testing across all environments and removes dependencies on local machine setup.

[Run Angular tests in a container Â»](https://docs.docker.com/guides/angular/run-tests/)