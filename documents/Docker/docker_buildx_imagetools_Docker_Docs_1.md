# docker buildx imagetools | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/buildx/imagetools/
**Word Count:** 775
**Links Count:** 486
**Scraped:** 2025-07-16 01:50:20
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker buildx imagetools

Description| Commands to work on images in registry   ---|---   Usage| `docker buildx imagetools`      ## Description

The `imagetools` commands contains subcommands for working with manifest lists in container registries. These commands are useful for inspecting manifests to check multi-platform configuration and attestations.

## Examples

### Override the configured builder instance \(--builder\)

Same as [`buildx --builder`](https://docs.docker.com/reference/cli/docker/buildx/#builder).

## Subcommands

Command| Description   ---|---   [`docker buildx imagetools create`](https://docs.docker.com/reference/cli/docker/buildx/imagetools/create/)| Create a new image based on source images   [`docker buildx imagetools inspect`](https://docs.docker.com/reference/cli/docker/buildx/imagetools/inspect/)| Show details of an image in the registry