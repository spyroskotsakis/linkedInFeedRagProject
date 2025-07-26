# docker container export | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/container/export
**Word Count:** 805
**Links Count:** 482
**Scraped:** 2025-07-16 01:58:03
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker container export

Description| Export a container's filesystem as a tar archive   ---|---   Usage| `docker container export [OPTIONS] CONTAINER`   AliasesAn alias is a short or memorable alternative for a longer command.| `docker export`      ## Description

The `docker export` command doesn't export the contents of volumes associated with the container. If a volume is mounted on top of an existing directory in the container, `docker export` exports the contents of the underlying directory, not the contents of the volume.

Refer to [Backup, restore, or migrate data volumes](https://docs.docker.com/engine/storage/volumes/#back-up-restore-or-migrate-data-volumes) in the user guide for examples on exporting data in a volume.

## Options

Option| Default| Description   ---|---|---   `-o, --output`| | Write to a file, instead of STDOUT      ## Examples

The following commands produce the same result.               $ docker export red_panda > latest.tar                    $ docker export --output="latest.tar" red_panda