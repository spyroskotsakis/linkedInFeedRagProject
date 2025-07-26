# Bake | Docker Docs

**URL:** https://docs.docker.com/build/bake
**Word Count:** 1138
**Links Count:** 638
**Scraped:** 2025-07-16 01:59:00
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Bake

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Bake is a feature of Docker Buildx that lets you define your build configuration using a declarative file, as opposed to specifying a complex CLI expression. It also lets you run multiple builds concurrently with a single invocation.

A Bake file can be written in HCL, JSON, or YAML formats, where the YAML format is an extension of a Docker Compose file. Here's an example Bake file in HCL format:

docker-bake.hcl               group "default" {       targets = ["frontend", "backend"]     }          target "frontend" {       context = "./frontend"       dockerfile = "frontend.Dockerfile"       args = {         NODE_VERSION = "22"       }       tags = ["myapp/frontend:latest"]     }          target "backend" {       context = "./backend"       dockerfile = "backend.Dockerfile"       args = {         GO_VERSION = "1.24"       }       tags = ["myapp/backend:latest"]     }

The `group` block defines a group of targets that can be built concurrently. Each `target` block defines a build target with its own configuration, such as the build context, Dockerfile, and tags.

To invoke a build using the above Bake file, you can run:               $ docker buildx bake     

This executes the `default` group, which builds the `frontend` and `backend` targets concurrently.

## Get started

To learn how to get started with Bake, head over to the [Bake introduction](https://docs.docker.com/build/bake/introduction/).