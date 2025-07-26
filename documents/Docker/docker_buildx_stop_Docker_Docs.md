# docker buildx stop | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/buildx/stop
**Word Count:** 752
**Links Count:** 482
**Scraped:** 2025-07-16 01:56:56
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker buildx stop

Description| Stop builder instance   ---|---   Usage| `docker buildx stop [NAME]`      ## Description

Stops the specified or current builder. This does not prevent buildx build to restart the builder. The implementation of stop depends on the driver.

## Examples

### Override the configured builder instance \(--builder\)

Same as [`buildx --builder`](https://docs.docker.com/reference/cli/docker/buildx/#builder).