# docker buildx prune | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/buildx/prune
**Word Count:** 833
**Links Count:** 484
**Scraped:** 2025-07-16 01:55:49
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker buildx prune

Description| Remove build cache   ---|---   Usage| `docker buildx prune`      ## Description

Clears the build cache of the selected builder.

You can finely control what cache data is kept using:

  * The `--filter=until=<duration>` flag to keep images that have been used in the last `<duration>` time.

`<duration>` is a duration string, e.g. `24h` or `2h30m`, with allowable units of `(h)ours`, `(m)inutes` and `(s)econds`.

  * The `--keep-storage=<size>` flag to keep `<size>` bytes of data in the cache.

`<size>` is a human-readable memory string, e.g. `128mb`, `2gb`, etc. Units are case-insensitive.

  * The `--all` flag to allow clearing internal helper images and frontend images set using the `#syntax=` directive or the `BUILDKIT_SYNTAX` build argument.

## Options

Option| Default| Description   ---|---|---   `-a, --all`| | Include internal/frontend images   `--filter`| | Provide filter values \(e.g., `until=24h`\)   `-f, --force`| | Do not prompt for confirmation   `--max-used-space`| | Maximum amount of disk space allowed to keep for cache   `--min-free-space`| | Target amount of free disk space after pruning   `--reserved-space`| | Amount of disk space always allowed to keep for cache   `--verbose`| | Provide a more verbose output      ## Examples

### Override the configured builder instance \(--builder\)

Same as [`buildx --builder`](https://docs.docker.com/reference/cli/docker/buildx/#builder).