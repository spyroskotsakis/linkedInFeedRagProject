# Networking using the host network | Docker Docs

**URL:** https://docs.docker.com/engine/network/tutorials/host
**Word Count:** 1289
**Links Count:** 654
**Scraped:** 2025-07-16 02:02:19
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Networking using the host network

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

This series of tutorials deals with networking standalone containers which bind directly to the Docker host's network, with no network isolation. For other networking topics, see the [overview](https://docs.docker.com/engine/network/).

## Goal

The goal of this tutorial is to start a `nginx` container which binds directly to port 80 on the Docker host. From a networking point of view, this is the same level of isolation as if the `nginx` process were running directly on the Docker host and not in a container. However, in all other ways, such as storage, process namespace, and user namespace, the `nginx` process is isolated from the host.

## Prerequisites

  * This procedure requires port 80 to be available on the Docker host. To make Nginx listen on a different port, see the [documentation for the `nginx` image](https://hub.docker.com/_/nginx/)

  * The `host` networking driver only works on Linux hosts, and as an opt-in feature in Docker Desktop version 4.34 and later. To enable this feature in Docker Desktop, navigate to the **Resources** tab in **Settings** , and then under **Network** select **Enable host networking**.

## Procedure

  1. Create and start the container as a detached process. The `--rm` option means to remove the container once it exits/stops. The `-d` flag means to start the container detached \(in the background\).                    $ docker run --rm -d --network host --name my_nginx nginx          

  2. Access Nginx by browsing to <http://localhost:80/>.

  3. Examine your network stack using the following commands:

     * Examine all network interfaces and verify that a new one was not created.                        $ ip addr show            

     * Verify which process is bound to port 80, using the `netstat` command. You need to use `sudo` because the process is owned by the Docker daemon user and you otherwise won't be able to see its name or PID.                        $ sudo netstat -tulpn | grep :80            

  4. Stop the container. It will be removed automatically as it was started using the `--rm` option.                    docker container stop my_nginx          

## Other networking tutorials

  * [Standalone networking tutorial](https://docs.docker.com/engine/network/tutorials/standalone/)   * [Overlay networking tutorial](https://docs.docker.com/engine/network/tutorials/overlay/)   * [Macvlan networking tutorial](https://docs.docker.com/engine/network/tutorials/macvlan/)