# docker stack rm | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/stack/rm/
**Word Count:** 868
**Links Count:** 486
**Scraped:** 2025-07-16 01:52:00
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker stack rm

Description| Remove one or more stacks   ---|---   Usage| `docker stack rm [OPTIONS] STACK [STACK...]`   AliasesAn alias is a short or memorable alternative for a longer command.| `docker stack remove` `docker stack down`      Swarm This command works with the Swarm orchestrator.

## Description

Remove the stack from the swarm.

> Note >  > This is a cluster management command, and must be executed on a swarm manager node. To learn about managers and workers, refer to the [Swarm mode section](https://docs.docker.com/engine/swarm/) in the documentation.

## Options

Option| Default| Description   ---|---|---   `-d, --detach`| `true`| Do not wait for stack removal      ## Examples

### Remove a stack

This will remove the stack with the name `myapp`. Services, networks, and secrets associated with the stack will be removed.               $ docker stack rm myapp          Removing service myapp_redis     Removing service myapp_web     Removing service myapp_lb     Removing network myapp_default     Removing network myapp_frontend     

### Remove multiple stacks

This will remove all the specified stacks, `myapp` and `vossibility`. Services, networks, and secrets associated with all the specified stacks will be removed.               $ docker stack rm myapp vossibility          Removing service myapp_redis     Removing service myapp_web     Removing service myapp_lb     Removing network myapp_default     Removing network myapp_frontend     Removing service vossibility_nsqd     Removing service vossibility_logstash     Removing service vossibility_elasticsearch     Removing service vossibility_kibana     Removing service vossibility_ghollector     Removing service vossibility_lookupd     Removing network vossibility_default     Removing network vossibility_vossibility