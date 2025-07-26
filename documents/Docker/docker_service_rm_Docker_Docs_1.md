# docker service rm | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/service/rm/
**Word Count:** 795
**Links Count:** 480
**Scraped:** 2025-07-16 01:52:00
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker service rm

Description| Remove one or more services   ---|---   Usage| `docker service rm SERVICE [SERVICE...]`   AliasesAn alias is a short or memorable alternative for a longer command.| `docker service remove`      Swarm This command works with the Swarm orchestrator.

## Description

Removes the specified services from the swarm.

> Note >  > This is a cluster management command, and must be executed on a swarm manager node. To learn about managers and workers, refer to the [Swarm mode section](https://docs.docker.com/engine/swarm/) in the documentation.

## Examples

Remove the `redis` service:               $ docker service rm redis          redis          $ docker service ls          ID  NAME  MODE  REPLICAS  IMAGE     

> Warning >  > Unlike `docker rm`, this command does not ask for confirmation before removing a running service.