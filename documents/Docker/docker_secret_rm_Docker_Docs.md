# docker secret rm | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/secret/rm
**Word Count:** 803
**Links Count:** 481
**Scraped:** 2025-07-16 01:56:12
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker secret rm

Description| Remove one or more secrets   ---|---   Usage| `docker secret rm SECRET [SECRET...]`   AliasesAn alias is a short or memorable alternative for a longer command.| `docker secret remove`      Swarm This command works with the Swarm orchestrator.

## Description

Removes the specified secrets from the swarm.

For detailed information about using secrets, refer to [manage sensitive data with Docker secrets](https://docs.docker.com/engine/swarm/secrets/).

> Note >  > This is a cluster management command, and must be executed on a swarm manager node. To learn about managers and workers, refer to the [Swarm mode section](https://docs.docker.com/engine/swarm/) in the documentation.

## Examples

This example removes a secret:               $ docker secret rm secret.json     sapth4csdo5b6wz2p5uimh5xg     

> Warning >  > Unlike `docker rm`, this command does not ask for confirmation before removing a secret.