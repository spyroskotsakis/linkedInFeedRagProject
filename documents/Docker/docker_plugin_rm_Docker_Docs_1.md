# docker plugin rm | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/plugin/rm/
**Word Count:** 792
**Links Count:** 482
**Scraped:** 2025-07-16 01:51:40
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker plugin rm

Description| Remove one or more plugins   ---|---   Usage| `docker plugin rm [OPTIONS] PLUGIN [PLUGIN...]`   AliasesAn alias is a short or memorable alternative for a longer command.| `docker plugin remove`      ## Description

Removes a plugin. You cannot remove a plugin if it is enabled, you must disable a plugin using the [`docker plugin disable`](https://docs.docker.com/reference/cli/docker/plugin/disable/) before removing it, or use `--force`. Use of `--force` is not recommended, since it can affect functioning of running containers using the plugin.

## Options

Option| Default| Description   ---|---|---   `-f, --force`| | Force the removal of an active plugin      ## Examples

The following example disables and removes the `sample-volume-plugin:latest` plugin:               $ docker plugin disable tiborvass/sample-volume-plugin          tiborvass/sample-volume-plugin          $ docker plugin rm tiborvass/sample-volume-plugin:latest          tiborvass/sample-volume-plugin