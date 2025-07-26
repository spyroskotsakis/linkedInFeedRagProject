# Scale the service in the swarm | Docker Docs

**URL:** https://docs.docker.com/engine/swarm/swarm-tutorial/scale-service/
**Word Count:** 1256
**Links Count:** 639
**Scraped:** 2025-07-16 01:48:31
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Scale the service in the swarm

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

* * *

Once you have [deployed a service](https://docs.docker.com/engine/swarm/swarm-tutorial/deploy-service/) to a swarm, you are ready to use the Docker CLI to scale the number of containers in the service. Containers running in a service are called tasks.

  1. If you haven't already, open a terminal and ssh into the machine where you run your manager node. For example, the tutorial uses a machine named `manager1`.

  2. Run the following command to change the desired state of the service running in the swarm:                    $ docker service scale <SERVICE-ID>=<NUMBER-OF-TASKS>          

For example:                    $ docker service scale helloworld=5                    helloworld scaled to 5          

  3. Run `docker service ps <SERVICE-ID>` to see the updated task list:                    $ docker service ps helloworld                    NAME                                    IMAGE   NODE      DESIRED STATE  CURRENT STATE          helloworld.1.8p1vev3fq5zm0mi8g0as41w35  alpine  worker2   Running        Running 7 minutes          helloworld.2.c7a7tcdq5s0uk3qr88mf8xco6  alpine  worker1   Running        Running 24 seconds          helloworld.3.6crl09vdcalvtfehfh69ogfb1  alpine  worker1   Running        Running 24 seconds          helloworld.4.auky6trawmdlcne8ad8phb0f1  alpine  manager1  Running        Running 24 seconds          helloworld.5.ba19kca06l18zujfwxyc5lkyn  alpine  worker2   Running        Running 24 seconds          

You can see that swarm has created 4 new tasks to scale to a total of 5 running instances of Alpine Linux. The tasks are distributed between the three nodes of the swarm. One is running on `manager1`.

  4. Run `docker ps` to see the containers running on the node where you're connected. The following example shows the tasks running on `manager1`:                    $ docker ps                    CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES          528d68040f95        alpine:latest       "ping docker.com"   About a minute ago   Up About a minute                       helloworld.4.auky6trawmdlcne8ad8phb0f1          

If you want to see the containers running on other nodes, ssh into those nodes and run the `docker ps` command.

## Next steps

At this point in the tutorial, you're finished with the `helloworld` service. Next, you'll delete the service

[Delete the service](https://docs.docker.com/engine/swarm/swarm-tutorial/delete-service/)