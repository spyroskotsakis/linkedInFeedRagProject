# Host network driver | Docker Docs

**URL:** https://docs.docker.com/engine/network/drivers/host
**Word Count:** 1546
**Links Count:** 654
**Scraped:** 2025-07-16 02:03:45
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Host network driver

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

If you use the `host` network mode for a container, that container's network stack isn't isolated from the Docker host \(the container shares the host's networking namespace\), and the container doesn't get its own IP-address allocated. For instance, if you run a container which binds to port 80 and you use `host` networking, the container's application is available on port 80 on the host's IP address.

> Note >  > Given that the container does not have its own IP-address when using `host` mode networking, [port-mapping](https://docs.docker.com/engine/network/drivers/overlay/#publish-ports) doesn't take effect, and the `-p`, `--publish`, `-P`, and `--publish-all` option are ignored, producing a warning instead: >      >      >     WARNING: Published ports are discarded when using host network mode >     

Host mode networking can be useful for the following use cases:

  * To optimize performance   * In situations where a container needs to handle a large range of ports

This is because it doesn't require network address translation \(NAT\), and no "userland-proxy" is created for each port.

The host networking driver is supported on Docker Engine \(Linux only\) and Docker Desktop version 4.34 and later.

You can also use a `host` network for a swarm service, by passing `--network host` to the `docker service create` command. In this case, control traffic \(traffic related to managing the swarm and the service\) is still sent across an overlay network, but the individual swarm service containers send data using the Docker daemon's host network and ports. This creates some extra limitations. For instance, if a service container binds to port 80, only one service container can run on a given swarm node.

## Docker Desktop

Host networking is supported on Docker Desktop version 4.34 and later. To enable this feature:

  1. Sign in to your Docker account in Docker Desktop.   2. Navigate to **Settings**.   3. Under the **Resources** tab, select **Network**.   4. Check the **Enable host networking** option.   5. Select **Apply and restart**.

This feature works in both directions. This means you can access a server that is running in a container from your host and you can access servers running on your host from any container that is started with host networking enabled. TCP as well as UDP are supported as communication protocols.

### Examples

The following command starts netcat in a container that listens on port `8000`:               $ docker run --rm -it --net=host nicolaka/netshoot nc -lkv 0.0.0.0 8000     

Port `8000` will then be available on the host and you can connect to it with the following command from another terminal:               $ nc localhost 8000     

What you type in here will then appear on the terminal where the container is running.

To access a service running on the host from the container, you can start a container with host networking enabled with this command:               $ docker run --rm -it --net=host nicolaka/netshoot     

If you then want to access a service on your host from the container \(in this example a web server running on port `80`\), you can do it like this:               $ nc localhost 80     

### Limitations

  * Processes inside the container cannot bind to the IP addresses of the host because the container has no direct access to the interfaces of the host.   * The host network feature of Docker Desktop works on layer 4. This means that unlike with Docker on Linux, network protocols that operate below TCP or UDP are not supported.   * This feature doesn't work with Enhanced Container Isolation enabled, since isolating your containers from the host and allowing them access to the host network contradict each other.   * Only Linux containers are supported. Host networking does not work with Windows containers.

## Next steps

  * Go through the [host networking tutorial](https://docs.docker.com/engine/network/tutorials/host/)   * Learn about [networking from the container's point of view](https://docs.docker.com/engine/network/)   * Learn about [bridge networks](https://docs.docker.com/engine/network/drivers/bridge/)   * Learn about [overlay networks](https://docs.docker.com/engine/network/drivers/overlay/)   * Learn about [Macvlan networks](https://docs.docker.com/engine/network/drivers/macvlan/)