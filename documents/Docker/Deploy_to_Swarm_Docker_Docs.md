# Deploy to Swarm | Docker Docs

**URL:** https://docs.docker.com/guides/swarm-deploy
**Word Count:** 878
**Links Count:** 64
**Scraped:** 2025-07-16 02:05:41
**Status:** completed

---

Back

[Guides](https://docs.docker.com/guides/)

  * [Get started](https://docs.docker.com/get-started/)   * [Manuals](https://docs.docker.com/manuals/)   * [Reference](https://docs.docker.com/reference/)

* * *

[Deploy to Swarm](https://docs.docker.com/guides/swarm-deploy/)

Discover how to deploy and manage Docker containers using Docker Swarm.

[ Deployment](https://docs.docker.com/tags/deploy/)

10 minutes

[Â« Back to all guides](https://docs.docker.com/guides/)

# Deploy to Swarm

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

> Note >  > Swarm mode is an advanced feature for managing a cluster of Docker daemons. >  > Use Swarm mode if you intend to use Swarm as a production runtime environment. >  > If you're not planning on deploying with Swarm, use [Docker Compose](https://docs.docker.com/compose/) instead. If you're developing for a Kubernetes deployment, consider using the [integrated Kubernetes feature](https://docs.docker.com/desktop/features/kubernetes/) in Docker Desktop.

## Prerequisites

  * Download and install Docker Desktop as described in [Get Docker](https://docs.docker.com/get-started/get-docker/).

  * Work through containerizing an application in [Docker workshop part 2](https://docs.docker.com/get-started/workshop/02_our_app/)

  * Make sure that Swarm is enabled on your Docker Desktop by typing `docker system info`, and looking for a message `Swarm: active` \(you might have to scroll up a little\).

If Swarm isn't running, simply type `docker swarm init` in a shell prompt to set it up.

## Introduction

Now that you've demonstrated that the individual components of your application run as stand-alone containers and shown how to deploy it using Kubernetes, you can look at how to arrange for them to be managed by Docker Swarm. Swarm provides many tools for scaling, networking, securing and maintaining your containerized applications, above and beyond the abilities of containers themselves.

In order to validate that your containerized application works well on Swarm, you'll use Docker Desktop's built in Swarm environment right on your development machine to deploy your application, before handing it off to run on a full Swarm cluster in production. The Swarm environment created by Docker Desktop is fully featured, meaning it has all the Swarm features your app will enjoy on a real cluster, accessible from the convenience of your development machine.

## Describe apps using stack files

Swarm never creates individual containers like you did in the previous step of this tutorial. Instead, all Swarm workloads are scheduled as services, which are scalable groups of containers with added networking features maintained automatically by Swarm. Furthermore, all Swarm objects can and should be described in manifests called stack files. These YAML files describe all the components and configurations of your Swarm app, and can be used to create and destroy your app in any Swarm environment.

Now you can write a simple stack file to run and manage your Todo app, the container `getting-started` image created in [Part 2](https://docs.docker.com/get-started/workshop/02_our_app/) of the tutorial. Place the following in a file called `bb-stack.yaml`:

> Note >  > The `docker stack deploy` command uses the legacy [Compose file version 3](https://docs.docker.com/reference/compose-file/legacy-versions/) format, used by Compose V1. The latest format, defined by the [Compose specification](https://docs.docker.com/reference/compose-file/) isn't compatible with the `docker stack deploy` command. >  > For more information about the evolution of Compose, see [History of Compose](https://docs.docker.com/compose/history/).               version: "3.7"          services:       bb-app:         image: getting-started         ports:           - "8000:3000"

In this Swarm YAML file, there is one object, a `service`, describing a scalable group of identical containers. In this case, you'll get just one container \(the default\), and that container will be based on your `getting-started` image created in [Part 2](https://docs.docker.com/get-started/workshop/02_our_app/) of the tutorial. In addition, you've asked Swarm to forward all traffic arriving at port 8000 on your development machine to port 3000 inside our getting-started container.

> **Kubernetes Services and Swarm Services are very different** >  > Despite the similar name, the two orchestrators mean very different things by the term 'service'. In Swarm, a service provides both scheduling and networking facilities, creating containers and providing tools for routing traffic to them. In Kubernetes, scheduling and networking are handled separately, deployments \(or other controllers\) handle the scheduling of containers as pods, while services are responsible only for adding networking features to those pods.

## Deploy and check your application

  1. Deploy your application to Swarm:                    $ docker stack deploy -c bb-stack.yaml demo          

If all goes well, Swarm will report creating all your stack objects with no complaints:                    Creating network demo_default          Creating service demo_bb-app

Notice that in addition to your service, Swarm also creates a Docker network by default to isolate the containers deployed as part of your stack.

  2. Make sure everything worked by listing your service:                    $ docker service ls          

If all has gone well, your service will report with 1/1 of its replicas created:                    ID                  NAME                MODE                REPLICAS            IMAGE               PORTS          il7elwunymbs        demo_bb-app         replicated          1/1                 getting-started:latest   *:8000->3000/tcp

This indicates 1/1 containers you asked for as part of your services are up and running. Also, you see that port 8000 on your development machine is getting forwarded to port 3000 in your getting-started container.

  3. Open a browser and visit your Todo app at `localhost:8000`; you should see your Todo application, the same as when you ran it as a stand-alone container in [Part 2](https://docs.docker.com/get-started/workshop/02_our_app/) of the tutorial.

  4. Once satisfied, tear down your application:                    $ docker stack rm demo          

## Conclusion

At this point, you've successfully used Docker Desktop to deploy your application to a fully-featured Swarm environment on your development machine. You can now add other components to your app and taking advantage of all the features and power of Swarm, right on your own machine.

In addition to deploying to Swarm, you've also described your application as a stack file. This simple text file contains everything you need to create your application in a running state; you can check it in to version control and share it with your colleagues, letting you to distribute your applications to other clusters \(like the testing and production clusters that probably come after your development environments\).

## Swarm and CLI references

Further documentation for all new Swarm objects and CLI commands used in this article are available here:

  * [Swarm Mode](https://docs.docker.com/engine/swarm/)   * [Swarm Mode Services](https://docs.docker.com/engine/swarm/how-swarm-mode-works/services/)   * [Swarm Stacks](https://docs.docker.com/engine/swarm/stack-deploy/)   * [`docker stack *`](https://docs.docker.com/reference/cli/docker/stack/)   * [`docker service *`](https://docs.docker.com/reference/cli/docker/service/)