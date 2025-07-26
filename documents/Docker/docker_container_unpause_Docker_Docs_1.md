# docker container unpause | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/container/unpause/
**Word Count:** 759
**Links Count:** 480
**Scraped:** 2025-07-16 01:50:59
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker container unpause

Description| Unpause all processes within one or more containers   ---|---   Usage| `docker container unpause CONTAINER [CONTAINER...]`   AliasesAn alias is a short or memorable alternative for a longer command.| `docker unpause`      ## Description

The `docker unpause` command un-suspends all processes in the specified containers. On Linux, it does this using the freezer cgroup.

See the [freezer cgroup documentation](https://www.kernel.org/doc/Documentation/cgroup-v1/freezer-subsystem.txt) for further details.

## Examples               $ docker unpause my_container     my_container