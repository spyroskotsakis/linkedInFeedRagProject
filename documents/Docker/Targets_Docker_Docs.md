# Targets | Docker Docs

**URL:** https://docs.docker.com/build/bake/targets
**Word Count:** 1229
**Links Count:** 651
**Scraped:** 2025-07-16 02:00:53
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Bake targets

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

A target in a Bake file represents a build invocation. It holds all the information you would normally pass to a `docker build` command using flags.

docker-bake.hcl               target "webapp" {       dockerfile = "webapp.Dockerfile"       tags = ["docker.io/username/webapp:latest"]       context = "https://github.com/username/webapp"     }

To build a target with Bake, pass name of the target to the `bake` command.               $ docker buildx bake webapp     

You can build multiple targets at once by passing multiple target names to the `bake` command.               $ docker buildx bake webapp api tests     

## Default target

If you don't specify a target when running `docker buildx bake`, Bake will build the target named `default`.

docker-bake.hcl               target "default" {       dockerfile = "webapp.Dockerfile"       tags = ["docker.io/username/webapp:latest"]       context = "https://github.com/username/webapp"     }

To build this target, run `docker buildx bake` without any arguments:               $ docker buildx bake     

## Target properties

The properties you can set for a target closely resemble the CLI flags for `docker build`, with a few additional properties that are specific to Bake.

For all the properties you can set for a target, see the [Bake reference](https://docs.docker.com/build/bake/reference#target).

## Grouping targets

You can group targets together using the `group` block. This is useful when you want to build multiple targets at once.

docker-bake.hcl               group "all" {       targets = ["webapp", "api", "tests"]     }          target "webapp" {       dockerfile = "webapp.Dockerfile"       tags = ["docker.io/username/webapp:latest"]       context = "https://github.com/username/webapp"     }          target "api" {       dockerfile = "api.Dockerfile"       tags = ["docker.io/username/api:latest"]       context = "https://github.com/username/api"     }          target "tests" {       dockerfile = "tests.Dockerfile"       contexts = {         webapp = "target:webapp"         api = "target:api"       }       output = ["type=local,dest=build/tests"]       context = "."     }

To build all the targets in a group, pass the name of the group to the `bake` command.               $ docker buildx bake all     

## Additional resources

Refer to the following pages to learn more about Bake's features:

  * Learn how to use [variables](https://docs.docker.com/build/bake/variables/) in Bake to make your build configuration more flexible.   * Learn how you can use matrices to build multiple images with different configurations in [Matrices](https://docs.docker.com/build/bake/matrices/).   * Head to the [Bake file reference](https://docs.docker.com/build/bake/reference/) to learn about all the properties you can set in a Bake file, and its syntax.