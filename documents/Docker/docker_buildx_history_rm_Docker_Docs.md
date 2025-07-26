# docker buildx history rm | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/buildx/history/rm
**Word Count:** 813
**Links Count:** 489
**Scraped:** 2025-07-16 01:57:40
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker buildx history rm

Description| Remove build records   ---|---   Usage| `docker buildx history rm [OPTIONS] [REF...]`      ## Description

Remove one or more build records from the current builderâs history. You can remove specific builds by ID or offset, or delete all records at once using the `--all` flag.

## Options

Option| Default| Description   ---|---|---   `--all`| | Remove all build records      ## Examples

### Remove a specific build               # Using a build ID     docker buildx history rm qu2gsuo8ejqrwdfii23xkkckt          # Or using a relative offset     docker buildx history rm ^1     

### Remove multiple builds               # Using build IDs     docker buildx history rm qu2gsuo8ejqrwdfii23xkkckt qsiifiuf1ad9pa9qvppc0z1l3          # Or using relative offsets     docker buildx history rm ^1 ^2     

### Remove all build records from the current builder \(--all\)               docker buildx history rm --all