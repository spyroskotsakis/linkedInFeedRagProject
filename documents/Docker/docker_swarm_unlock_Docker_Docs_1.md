# docker swarm unlock | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/swarm/unlock/
**Word Count:** 801
**Links Count:** 480
**Scraped:** 2025-07-16 01:52:00
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker swarm unlock

Description| Unlock swarm   ---|---   Usage| `docker swarm unlock`      Swarm This command works with the Swarm orchestrator.

## Description

Unlocks a locked manager using a user-supplied unlock key. This command must be used to reactivate a manager after its Docker daemon restarts if the autolock setting is turned on. The unlock key is printed at the time when autolock is enabled, and is also available from the `docker swarm unlock-key` command.

> Note >  > This is a cluster management command, and must be executed on a swarm manager node. To learn about managers and workers, refer to the [Swarm mode section](https://docs.docker.com/engine/swarm/) in the documentation.

## Examples               $ docker swarm unlock     Enter unlock key: