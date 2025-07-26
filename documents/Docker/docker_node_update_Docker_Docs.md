# docker node update | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/node/update
**Word Count:** 917
**Links Count:** 488
**Scraped:** 2025-07-16 01:55:49
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker node update

Description| Update a node   ---|---   Usage| `docker node update [OPTIONS] NODE`      Swarm This command works with the Swarm orchestrator.

## Description

Update metadata about a node, such as its availability, labels, or roles.

> Note >  > This is a cluster management command, and must be executed on a swarm manager node. To learn about managers and workers, refer to the [Swarm mode section](https://docs.docker.com/engine/swarm/) in the documentation.

## Options

Option| Default| Description   ---|---|---   `--availability`| | Availability of the node \(`active`, `pause`, `drain`\)   `--label-add`| | Add or update a node label \(`key=value`\)   `--label-rm`| | Remove a node label if exists   `--role`| | Role of the node \(`worker`, `manager`\)      ## Examples

### Add label metadata to a node \(--label-add\)

Add metadata to a swarm node using node labels. You can specify a node label as a key with an empty value:               $ docker node update --label-add foo worker1

To add multiple labels to a node, pass the `--label-add` flag for each label:               $ docker node update --label-add foo --label-add bar worker1     

When you [create a service](https://docs.docker.com/reference/cli/docker/service/create/), you can use node labels as a constraint. A constraint limits the nodes where the scheduler deploys tasks for a service.

For example, to add a `type` label to identify nodes where the scheduler should deploy message queue service tasks:               $ docker node update --label-add type=queue worker1

The labels you set for nodes using `docker node update` apply only to the node entity within the swarm. Do not confuse them with the docker daemon labels for [dockerd](https://docs.docker.com/reference/cli/dockerd/).

For more information about labels, refer to [apply custom metadata](https://docs.docker.com/engine/userguide/labels-custom-metadata/).