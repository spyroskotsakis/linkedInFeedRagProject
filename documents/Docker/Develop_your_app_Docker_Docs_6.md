# Develop your app | Docker Docs

**URL:** https://docs.docker.com/guides/deno/develop
**Word Count:** 308
**Links Count:** 63
**Scraped:** 2025-07-16 02:04:23
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

# Use containers for Deno development

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Prerequisites

Complete [Containerize a Deno application](https://docs.docker.com/guides/deno/containerize/).

## Overview

In this section, you'll learn how to set up a development environment for your containerized application. This includes:

  * Configuring Compose to automatically update your running Compose services as you edit and save your code

## Get the sample application

Clone the sample application to use with this guide. Open a terminal, change directory to a directory that you want to work in, and run the following command to clone the repository:               $ git clone https://github.com/dockersamples/docker-deno.git && cd docker-deno     

## Automatically update services

Use Compose Watch to automatically update your running Compose services as you edit and save your code. For more details about Compose Watch, see [Use Compose Watch](https://docs.docker.com/compose/how-tos/file-watch/).

Open your `compose.yml` file in an IDE or text editor and then add the Compose Watch instructions. The following example shows how to add Compose Watch to your `compose.yml` file.                1      2      3      4      5      6      7      8      9     10     11     12     

|                services:       server:         image: deno-server         build:           context: .           dockerfile: Dockerfile         ports:           - "8000:8000"         develop:           watch:             - action: rebuild               path: .      ---|---      Run the following command to run your application with Compose Watch.               $ docker compose watch     

Now, if you modify your `server.ts` you will see the changes in real time without re-building the image.

To test it out, open the `server.ts` file in your favorite text editor and change the message from `{"Status" : "OK"}` to `{"Status" : "Updated"}`. Save the file and refresh your browser at `http://localhost:8000`. You should see the updated message.

Press `ctrl+c` in the terminal to stop your application.

## Summary

In this section, you also learned how to use Compose Watch to automatically rebuild and run your container when you update your code.

Related information:

  * [Compose file reference](https://docs.docker.com/reference/compose-file/)   * [Compose file watch](https://docs.docker.com/compose/how-tos/file-watch/)   * [Multi-stage builds](https://docs.docker.com/build/building/multi-stage/)

## Next steps

In the next section, you'll take a look at how to set up a CI/CD pipeline using GitHub Actions.

[Configure CI/CD for your Deno application Â»](https://docs.docker.com/guides/deno/configure-ci-cd/)