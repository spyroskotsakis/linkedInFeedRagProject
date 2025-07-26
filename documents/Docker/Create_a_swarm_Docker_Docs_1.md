# Create a swarm | Docker Docs

**URL:** https://docs.docker.com/engine/swarm/swarm-tutorial/create-swarm/
**Word Count:** 1253
**Links Count:** 639
**Scraped:** 2025-07-16 01:46:25
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Create a swarm

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

* * *

After you complete the [tutorial setup](https://docs.docker.com/engine/swarm/swarm-tutorial/) steps, you're ready to create a swarm. Make sure the Docker Engine daemon is started on the host machines.

  1. Open a terminal and ssh into the machine where you want to run your manager node. This tutorial uses a machine named `manager1`.

  2. Run the following command to create a new swarm:                    $ docker swarm init --advertise-addr <MANAGER-IP>          

In the tutorial, the following command creates a swarm on the `manager1` machine:                    $ docker swarm init --advertise-addr 192.168.99.100          Swarm initialized: current node (dxn1zf6l61qsb1josjja83ngz) is now a manager.                    To add a worker to this swarm, run the following command:                        docker swarm join \              --token SWMTKN-1-49nj1cmql0jkz5s954yi3oex3nedyz0fb0xx14ie39trti4wxv-8vxv8rssmk743ojnwacrr2e7c \              192.168.99.100:2377                    To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.          

The `--advertise-addr` flag configures the manager node to publish its address as `192.168.99.100`. The other nodes in the swarm must be able to access the manager at the IP address.

The output includes the commands to join new nodes to the swarm. Nodes will join as managers or workers depending on the value for the `--token` flag.

  3. Run `docker info` to view the current state of the swarm:                    $ docker info                    Containers: 2          Running: 0          Paused: 0          Stopped: 2            ...snip...          Swarm: active            NodeID: dxn1zf6l61qsb1josjja83ngz            Is Manager: true            Managers: 1            Nodes: 1            ...snip...          

  4. Run the `docker node ls` command to view information about nodes:                    $ docker node ls                    ID                           HOSTNAME  STATUS  AVAILABILITY  MANAGER STATUS          dxn1zf6l61qsb1josjja83ngz *  manager1  Ready   Active        Leader          

The `*` next to the node ID indicates that you're currently connected on this node.

Docker Engine Swarm mode automatically names the node with the machine host name. The tutorial covers other columns in later steps.

## Next steps

Next, you'll add two more nodes to the cluster.

[Add two more nodes](https://docs.docker.com/engine/swarm/swarm-tutorial/add-nodes/)