# Network drivers | Docker Docs

**URL:** https://docs.docker.com/engine/network/drivers
**Word Count:** 1457
**Links Count:** 652
**Scraped:** 2025-07-16 02:02:19
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Network drivers

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Docker's networking subsystem is pluggable, using drivers. Several drivers exist by default, and provide core networking functionality:

  * `bridge`: The default network driver. If you don't specify a driver, this is the type of network you are creating. Bridge networks are commonly used when your application runs in a container that needs to communicate with other containers on the same host. See [Bridge network driver](https://docs.docker.com/engine/network/drivers/bridge/).

  * `host`: Remove network isolation between the container and the Docker host, and use the host's networking directly. See [Host network driver](https://docs.docker.com/engine/network/drivers/host/).

  * `overlay`: Overlay networks connect multiple Docker daemons together and enable Swarm services and containers to communicate across nodes. This strategy removes the need to do OS-level routing. See [Overlay network driver](https://docs.docker.com/engine/network/drivers/overlay/).

  * `ipvlan`: IPvlan networks give users total control over both IPv4 and IPv6 addressing. The VLAN driver builds on top of that in giving operators complete control of layer 2 VLAN tagging and even IPvlan L3 routing for users interested in underlay network integration. See [IPvlan network driver](https://docs.docker.com/engine/network/drivers/ipvlan/).

  * `macvlan`: Macvlan networks allow you to assign a MAC address to a container, making it appear as a physical device on your network. The Docker daemon routes traffic to containers by their MAC addresses. Using the `macvlan` driver is sometimes the best choice when dealing with legacy applications that expect to be directly connected to the physical network, rather than routed through the Docker host's network stack. See [Macvlan network driver](https://docs.docker.com/engine/network/drivers/macvlan/).

  * `none`: Completely isolate a container from the host and other containers. `none` is not available for Swarm services. See [None network driver](https://docs.docker.com/engine/network/drivers/none/).

  * [Network plugins](https://docs.docker.com/engine/extend/plugins_network/): You can install and use third-party network plugins with Docker.

### Network driver summary

  * The default bridge network is good for running containers that don't require special networking capabilities.   * User-defined bridge networks enable containers on the same Docker host to communicate with each other. A user-defined network typically defines an isolated network for multiple containers belonging to a common project or component.   * Host network shares the host's network with the container. When you use this driver, the container's network isn't isolated from the host.   * Overlay networks are best when you need containers running on different Docker hosts to communicate, or when multiple applications work together using Swarm services.   * Macvlan networks are best when you are migrating from a VM setup or need your containers to look like physical hosts on your network, each with a unique MAC address.   * IPvlan is similar to Macvlan, but doesn't assign unique MAC addresses to containers. Consider using IPvlan when there's a restriction on the number of MAC addresses that can be assigned to a network interface or port.   * Third-party network plugins allow you to integrate Docker with specialized network stacks.

## Networking tutorials

Now that you understand the basics about Docker networks, deepen your understanding using the following tutorials:

  * [Standalone networking tutorial](https://docs.docker.com/engine/network/tutorials/standalone/)   * [Host networking tutorial](https://docs.docker.com/engine/network/tutorials/host/)   * [Overlay networking tutorial](https://docs.docker.com/engine/network/tutorials/overlay/)   * [Macvlan networking tutorial](https://docs.docker.com/engine/network/tutorials/macvlan/)