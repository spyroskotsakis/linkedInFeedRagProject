# docker buildx use | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/buildx/use/
**Word Count:** 773
**Links Count:** 484
**Scraped:** 2025-07-16 01:50:20
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker buildx use

Description| Set the current builder instance   ---|---   Usage| `docker buildx use [OPTIONS] NAME`      ## Description

Switches the current builder instance. Build commands invoked after this command will run on a specified builder. Alternatively, a context name can be used to switch to the default builder of that context.

## Options

Option| Default| Description   ---|---|---   `--default`| | Set builder as default for current context   `--global`| | Builder persists context changes      ## Examples

### Override the configured builder instance \(--builder\)

Same as [`buildx --builder`](https://docs.docker.com/reference/cli/docker/buildx/#builder).