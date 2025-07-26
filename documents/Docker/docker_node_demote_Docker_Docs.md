# docker node demote | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/node/demote
**Word Count:** 773
**Links Count:** 480
**Scraped:** 2025-07-16 01:56:56
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker node demote

Description| Demote one or more nodes from manager in the swarm   ---|---   Usage| `docker node demote NODE [NODE...]`      Swarm This command works with the Swarm orchestrator.

## Description

Demotes an existing manager so that it is no longer a manager.

> Note >  > This is a cluster management command, and must be executed on a swarm manager node. To learn about managers and workers, refer to the [Swarm mode section](https://docs.docker.com/engine/swarm/) in the documentation.

## Examples               $ docker node demote <node name>