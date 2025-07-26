# docker node promote | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/node/promote/
**Word Count:** 776
**Links Count:** 480
**Scraped:** 2025-07-16 01:51:40
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker node promote

Description| Promote one or more nodes to manager in the swarm   ---|---   Usage| `docker node promote NODE [NODE...]`      Swarm This command works with the Swarm orchestrator.

## Description

Promotes a node to manager. This command can only be executed on a manager node.

> Note >  > This is a cluster management command, and must be executed on a swarm manager node. To learn about managers and workers, refer to the [Swarm mode section](https://docs.docker.com/engine/swarm/) in the documentation.

## Examples               $ docker node promote <node name>