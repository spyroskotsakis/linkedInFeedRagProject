# Containerize your app | Docker Docs

**URL:** https://docs.docker.com/guides/deno/containerize/
**Word Count:** 586
**Links Count:** 76
**Scraped:** 2025-07-16 01:46:03
**Status:** completed

---

Back

[Guides](https://docs.docker.com/guides/)

  * [Get started](https://docs.docker.com/get-started/)   * [Manuals](https://docs.docker.com/manuals/)   * [Reference](https://docs.docker.com/reference/)

* * *

[Deno language-specific guide](https://docs.docker.com/guides/deno/)

Learn how to containerize JavaScript applications with the Deno runtime using Docker.

![](https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg) JavaScript

10 minutes

[1](https://docs.docker.com/guides/deno/containerize/)

[Containerize your app](https://docs.docker.com/guides/deno/containerize/)

[2](https://docs.docker.com/guides/deno/develop/)

[Develop your app](https://docs.docker.com/guides/deno/develop/)

[3](https://docs.docker.com/guides/deno/configure-ci-cd/)

[Configure CI/CD](https://docs.docker.com/guides/deno/configure-ci-cd/)

[4](https://docs.docker.com/guides/deno/deploy/)

[Test your deployment](https://docs.docker.com/guides/deno/deploy/)

[Â« Back to all guides](https://docs.docker.com/guides/)

# Containerize a Deno application

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Prerequisites

  * You have a [Git client](https://git-scm.com/downloads). The examples in this section use a command-line based Git client, but you can use any client.

## Overview

For a long time, Node.js has been the go-to runtime for server-side JavaScript applications. However, recent years have introduced new alternative runtimes, including [Deno](https://deno.land/). Like Node.js, Deno is a JavaScript and TypeScript runtime, but it takes a fresh approach with modern security features, a built-in standard library, and native support for TypeScript.

Why develop Deno applications with Docker? Having a choice of runtimes is exciting, but managing multiple runtimes and their dependencies consistently across environments can be tricky. This is where Docker proves invaluable. Using containers to create and destroy environments on demand simplifies runtime management and ensures consistency. Additionally, as Deno continues to grow and evolve, Docker helps establish a reliable and reproducible development environment, minimizing setup challenges and streamlining the workflow.

## Get the sample application

Clone the sample application to use with this guide. Open a terminal, change directory to a directory that you want to work in, and run the following command to clone the repository:               $ git clone https://github.com/dockersamples/docker-deno.git && cd docker-deno     

You should now have the following contents in your `deno-docker` directory.               âââ deno-docker/     â âââ compose.yml     â âââ Dockerfile     â âââ LICENSE     â âââ server.ts     â âââ README.md

## Understand the sample application

The sample application is a simple Deno application that uses the Oak framework to create a simple API that returns a JSON response. The application listens on port 8000 and returns a message `{"Status" : "OK"}` when you access the application in a browser.               // server.ts     import { Application, Router } from "https://deno.land/x/oak@v12.0.0/mod.ts";          const app = new Application();     const router = new Router();          // Define a route that returns JSON     router.get("/", (context) => {       context.response.body = { Status: "OK" };       context.response.type = "application/json";     });          app.use(router.routes());     app.use(router.allowedMethods());          console.log("Server running on http://localhost:8000");     await app.listen({ port: 8000 });

## Create a Dockerfile

In the Dockerfile, you'll notice that the `FROM` instruction uses `denoland/deno:latest` as the base image. This is the official image for Deno. This image is [available on the Docker Hub](https://hub.docker.com/r/denoland/deno).               # Use the official Deno image     FROM denoland/deno:latest          # Set the working directory     WORKDIR /app          # Copy server code into the container     COPY server.ts .          # Set permissions (optional but recommended for security)     USER deno          # Expose port 8000     EXPOSE 8000          # Run the Deno server     CMD ["run", "--allow-net", "server.ts"]

Aside from specifying `denoland/deno:latest` as the base image, the Dockerfile:

  * Sets the working directory in the container to `/app`.   * Copies `server.ts` into the container.   * Sets the user to `deno` to run the application as a non-root user.   * Exposes port 8000 to allow traffic to the application.   * Runs the Deno server using the `CMD` instruction.   * Uses the `--allow-net` flag to allow network access to the application. The `server.ts` file uses the Oak framework to create a simple API that listens on port 8000.

## Run the application

Make sure you are in the `deno-docker` directory. Run the following command in a terminal to build and run the application.               $ docker compose up --build     

Open a browser and view the application at <http://localhost:8000>. You will see a message `{"Status" : "OK"}` in the browser.

In the terminal, press `ctrl`+`c` to stop the application.

### Run the application in the background

You can run the application detached from the terminal by adding the `-d` option. Inside the `deno-docker` directory, run the following command in a terminal.               $ docker compose up --build -d     

Open a browser and view the application at <http://localhost:8000>.

In the terminal, run the following command to stop the application.               $ docker compose down     

## Summary

In this section, you learned how you can containerize and run your Deno application using Docker.

Related information:

  * [Dockerfile reference](https://docs.docker.com/reference/dockerfile/)   * [.dockerignore file](https://docs.docker.com/reference/dockerfile/#dockerignore-file)   * [Docker Compose overview](https://docs.docker.com/compose/)   * [Compose file reference](https://docs.docker.com/reference/compose-file/)

## Next steps

In the next section, you'll learn how you can develop your application using containers.

[Use containers for Deno development Â»](https://docs.docker.com/guides/deno/develop/)