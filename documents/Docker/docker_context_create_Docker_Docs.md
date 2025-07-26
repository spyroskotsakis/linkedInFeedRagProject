# docker context create | Docker Docs

**URL:** http://docs.docker.com/reference/cli/docker/context/create
**Word Count:** 895
**Links Count:** 488
**Scraped:** 2025-07-16 02:10:49
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](http://docs.docker.com/get-started/)   * [Guides](http://docs.docker.com/guides/)   * [Manuals](http://docs.docker.com/manuals/)

* * *

# docker context create

Description| Create a context   ---|---   Usage| `docker context create [OPTIONS] CONTEXT`      ## Description

Creates a new `context`. This lets you switch the daemon your `docker` CLI connects to.

## Options

Option| Default| Description   ---|---|---   `--description`| | Description of the context   `--docker`| | set the docker endpoint   `--from`| | create context from a named context      ## Examples

### Create a context with a Docker endpoint \(--docker\)

Use the `--docker` flag to create a context with a custom endpoint. The following example creates a context named `my-context` with a docker endpoint of `/var/run/docker.sock`:               $ docker context create \         --docker host=unix:///var/run/docker.sock \         my-context     

### Create a context based on an existing context \(--from\)

Use the `--from=<context-name>` option to create a new context from an existing context. The example below creates a new context named `my-context` from the existing context `existing-context`:               $ docker context create --from existing-context my-context     

If the `--from` option isn't set, the `context` is created from the current context:               $ docker context create my-context     

This can be used to create a context out of an existing `DOCKER_HOST` based script:               $ source my-setup-script.sh     $ docker context create my-context     

To source the `docker` endpoint configuration from an existing context use the `--docker from=<context-name>` option. The example below creates a new context named `my-context` using the docker endpoint configuration from the existing context `existing-context`:               $ docker context create \         --docker from=existing-context \         my-context     

Docker endpoints configurations, as well as the description can be modified with `docker context update`.

Refer to the [`docker context update` reference](http://docs.docker.com/reference/cli/docker/context/update/) for details.