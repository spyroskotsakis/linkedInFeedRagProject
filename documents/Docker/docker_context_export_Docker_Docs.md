# docker context export | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/context/export
**Word Count:** 756
**Links Count:** 477
**Scraped:** 2025-07-16 01:56:56
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker context export

Description| Export a context to a tar archive FILE or a tar stream on STDOUT.   ---|---   Usage| `docker context export [OPTIONS] CONTEXT [FILE|-]`      ## Description

Exports a context to a file that can then be used with `docker context import`.

The default output filename is `<CONTEXT>.dockercontext`. To export to `STDOUT`, use `-` as filename, for example:               $ docker context export my-context -