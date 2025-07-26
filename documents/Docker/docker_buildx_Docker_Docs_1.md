# docker buildx | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/buildx
**Word Count:** 808
**Links Count:** 499
**Scraped:** 2025-07-16 01:56:12
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker buildx

Description| Docker Buildx   ---|---   Usage| `docker buildx`      ## Description

Extended build capabilities with BuildKit

## Options

Option| Default| Description   ---|---|---   `--builder`| | Override the configured builder instance   `-D, --debug`| | Enable debug logging      ## Examples

### Override the configured builder instance \(--builder\)

You can also use the `BUILDX_BUILDER` environment variable.

## Subcommands

Command| Description   ---|---   [`docker buildx bake`](https://docs.docker.com/reference/cli/docker/buildx/bake/)| Build from a file   [`docker buildx build`](https://docs.docker.com/reference/cli/docker/buildx/build/)| Start a build   [`docker buildx create`](https://docs.docker.com/reference/cli/docker/buildx/create/)| Create a new builder instance   [`docker buildx debug`](https://docs.docker.com/reference/cli/docker/buildx/debug/)| Start debugger   [`docker buildx du`](https://docs.docker.com/reference/cli/docker/buildx/du/)| Disk usage   [`docker buildx history`](https://docs.docker.com/reference/cli/docker/buildx/history/)| Commands to work on build records   [`docker buildx imagetools`](https://docs.docker.com/reference/cli/docker/buildx/imagetools/)| Commands to work on images in registry   [`docker buildx inspect`](https://docs.docker.com/reference/cli/docker/buildx/inspect/)| Inspect current builder instance   [`docker buildx ls`](https://docs.docker.com/reference/cli/docker/buildx/ls/)| List builder instances   [`docker buildx prune`](https://docs.docker.com/reference/cli/docker/buildx/prune/)| Remove build cache   [`docker buildx rm`](https://docs.docker.com/reference/cli/docker/buildx/rm/)| Remove one or more builder instances   [`docker buildx stop`](https://docs.docker.com/reference/cli/docker/buildx/stop/)| Stop builder instance   [`docker buildx use`](https://docs.docker.com/reference/cli/docker/buildx/use/)| Set the current builder instance   [`docker buildx version`](https://docs.docker.com/reference/cli/docker/buildx/version/)| Show buildx version information