# docker scout cache prune | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/scout/cache/prune/
**Word Count:** 803
**Links Count:** 486
**Scraped:** 2025-07-16 01:51:40
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker scout cache prune

Description| Remove temporary or cached data   ---|---   Usage| `docker scout cache prune`      ## Description

The `docker scout cache prune` command removes temporary data and SBOM cache.

By default, `docker scout cache prune` only deletes temporary data. To delete temporary data and clear the SBOM cache, use the `--sboms` flag.

## Options

Option| Default| Description   ---|---|---   `-f, --force`| | Do not prompt for confirmation   `--sboms`| | Prune cached SBOMs      ## Examples

### Delete temporary data               $ docker scout cache prune     ? Are you sure to delete all temporary data? Yes         â temporary data deleted     

### Delete temporary _and_ cache data               $ docker scout cache prune --sboms     ? Are you sure to delete all temporary data and all cached SBOMs? Yes         â temporary data deleted         â cached SBOMs deleted