# Deploy a service to the swarm | Docker Docs

**URL:** https://docs.docker.com/engine/swarm/swarm-tutorial/deploy-service
**Word Count:** 1137
**Links Count:** 640
**Scraped:** 2025-07-16 02:02:47
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Deploy a service to the swarm

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

* * *

After you [create a swarm](https://docs.docker.com/engine/swarm/swarm-tutorial/create-swarm/), you can deploy a service to the swarm. For this tutorial, you also [added worker nodes](https://docs.docker.com/engine/swarm/swarm-tutorial/add-nodes/), but that is not a requirement to deploy a service.

  1. Open a terminal and ssh into the machine where you run your manager node. For example, the tutorial uses a machine named `manager1`.

  2. Run the following command:                    $ docker service create --replicas 1 --name helloworld alpine ping docker.com                    9uk4639qpg7npwf3fn2aasksr          

     * The `docker service create` command creates the service.      * The `--name` flag names the service `helloworld`.      * The `--replicas` flag specifies the desired state of 1 running instance.      * The arguments `alpine ping docker.com` define the service as an Alpine Linux container that executes the command `ping docker.com`.   3. Run `docker service ls` to see the list of running services:                    $ docker service ls                    ID            NAME        SCALE  IMAGE   COMMAND          9uk4639qpg7n  helloworld  1/1    alpine  ping docker.com          

## Next steps

Now you're ready to inspect the service.

[Inspect the service](https://docs.docker.com/engine/swarm/swarm-tutorial/inspect-service/)