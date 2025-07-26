# Build dependent images | Docker Docs

**URL:** https://docs.docker.com/compose/how-tos/dependent-images/
**Word Count:** 1427
**Links Count:** 651
**Scraped:** 2025-07-16 01:48:31
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Build dependent images

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Requires: Docker Compose [2.22.0](https://docs.docker.com/compose/releases/release-notes/#2220) and later

To reduce push/pull time and image weight, a common practice for Compose applications is to have services share base layers as much as possible. You typically select the same operating system base image for all services. But you can also get one step further by sharing image layers when your images share the same system packages. The challenge to address is then to avoid repeating the exact same Dockerfile instruction in all services.

For illustration, this page assumes you want all your services to be built with an `alpine` base image and install the system package `openssl`.

## Multi-stage Dockerfile

The recommended approach is to group the shared declaration in a single Dockerfile, and use multi-stage features so that service images are built from this shared declaration.

Dockerfile:               FROM alpine as base     RUN /bin/sh -c apk add --update --no-cache openssl          FROM base as service_a     # build service a     ...          FROM base as service_b     # build service b     ...

Compose file:               services:       a:          build:            target: service_a       b:          build:            target: service_b

## Use another service's image as the base image

A popular pattern is to reuse a service image as a base image in another service. As Compose does not parse the Dockerfile, it can't automatically detect this dependency between services to correctly order the build execution.

a.Dockerfile:               FROM alpine     RUN /bin/sh -c apk add --update --no-cache openssl

b.Dockerfile:               FROM service_a     # build service b

Compose file:               services:       a:          image: service_a           build:            dockerfile: a.Dockerfile       b:          image: service_b          build:            dockerfile: b.Dockerfile

Legacy Docker Compose v1 used to build images sequentially, which made this pattern usable out of the box. Compose v2 uses BuildKit to optimise builds and build images in parallel and requires an explicit declaration.

The recommended approach is to declare the dependent base image as an additional build context:

Compose file:               services:       a:          image: service_a          build:             dockerfile: a.Dockerfile       b:          image: service_b          build:            dockerfile: b.Dockerfile            additional_contexts:              # `FROM service_a` will be resolved as a dependency on service "a" which has to be built first              service_a: "service:a"

With the `additional_contexts` attribute, you can refer to an image built by another service without needing to explicitly name it:

b.Dockerfile:               FROM base_image       # `base_image` doesn't resolve to an actual image. This is used to point to a named additional context          # build service b

Compose file:               services:       a:          build:             dockerfile: a.Dockerfile            # built image will be tagged <project_name>_a       b:          build:            dockerfile: b.Dockerfile            additional_contexts:              # `FROM base_image` will be resolved as a dependency on service "a" which has to be built first              base_image: "service:a"

## Build with Bake

Using [Bake](https://docs.docker.com/build/bake/) let you pass the complete build definition for all services and to orchestrate build execution in the most efficient way.

To enable this feature, run Compose with the `COMPOSE_BAKE=true` variable set in your environment.               $ COMPOSE_BAKE=true docker compose build     [+] Building 0.0s (0/1)                                                               => [internal] load local bake definitions                                 0.0s     ...     [+] Building 2/2 manifest list sha256:4bd2e88a262a02ddef525c381a5bdb08c83  0.0s      â service_b  Built                                                        0.7s       â service_a  Built         

Bake can also be selected as the default builder by editing your `$HOME/.docker/config.json` config file:               {       ...       "plugins": {         "compose": {           "build": "bake"         }       }       ...     }

## Additional resources

  * [Docker Compose build reference](https://docs.docker.com/reference/cli/docker/compose/build/)   * [Learn about multi-stage Dockerfiles](https://docs.docker.com/build/building/multi-stage/)