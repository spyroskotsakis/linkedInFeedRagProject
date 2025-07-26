# How nodes work | Docker Docs

**URL:** https://docs.docker.com/engine/swarm/how-swarm-mode-works/nodes
**Word Count:** 1434
**Links Count:** 659
**Scraped:** 2025-07-16 02:03:45
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# How nodes work

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Swarm mode lets you create a cluster of one or more Docker Engines called a swarm. A swarm consists of one or more nodes: physical or virtual machines running Docker Engine.

There are two types of nodes: managers and workers.

![Swarm mode cluster](https://docs.docker.com/engine/swarm/images/swarm-diagram.webp)

![Swarm mode cluster](https://docs.docker.com/engine/swarm/images/swarm-diagram.webp)

If you haven't already, read through the [Swarm mode overview](https://docs.docker.com/engine/swarm/) and [key concepts](https://docs.docker.com/engine/swarm/key-concepts/).

## Manager nodes

Manager nodes handle cluster management tasks:

  * Maintaining cluster state   * Scheduling services   * Serving Swarm mode [HTTP API endpoints](https://docs.docker.com/reference/api/engine/)

Using a [Raft](https://raft.github.io/raft.pdf) implementation, the managers maintain a consistent internal state of the entire swarm and all the services running on it. For testing purposes it is OK to run a swarm with a single manager. If the manager in a single-manager swarm fails, your services continue to run, but you need to create a new cluster to recover.

To take advantage of Swarm mode's fault-tolerance features, we recommend you implement an odd number of nodes according to your organization's high-availability requirements. When you have multiple managers you can recover from the failure of a manager node without downtime.

  * A three-manager swarm tolerates a maximum loss of one manager.

  * A five-manager swarm tolerates a maximum simultaneous loss of two manager nodes.

  * An odd number `N` of manager nodes in the cluster tolerates the loss of at most `(N-1)/2` managers. Docker recommends a maximum of seven manager nodes for a swarm.

> Important >  > Adding more managers does NOT mean increased scalability or higher performance. In general, the opposite is true.

## Worker nodes

Worker nodes are also instances of Docker Engine whose sole purpose is to execute containers. Worker nodes don't participate in the Raft distributed state, make scheduling decisions, or serve the swarm mode HTTP API.

You can create a swarm of one manager node, but you cannot have a worker node without at least one manager node. By default, all managers are also workers. In a single manager node cluster, you can run commands like `docker service create` and the scheduler places all tasks on the local engine.

To prevent the scheduler from placing tasks on a manager node in a multi-node swarm, set the availability for the manager node to `Drain`. The scheduler gracefully stops tasks on nodes in `Drain` mode and schedules the tasks on an `Active` node. The scheduler does not assign new tasks to nodes with `Drain` availability.

Refer to the [`docker node update`](https://docs.docker.com/reference/cli/docker/node/update/) command line reference to see how to change node availability.

## Change roles

You can promote a worker node to be a manager by running `docker node promote`. For example, you may want to promote a worker node when you take a manager node offline for maintenance. See [node promote](https://docs.docker.com/reference/cli/docker/node/promote/).

You can also demote a manager node to a worker node. See [node demote](https://docs.docker.com/reference/cli/docker/node/demote/).

## Learn more

  * Read about how Swarm mode [services](https://docs.docker.com/engine/swarm/how-swarm-mode-works/services/) work.   * Learn how [PKI](https://docs.docker.com/engine/swarm/how-swarm-mode-works/pki/) works in Swarm mode.