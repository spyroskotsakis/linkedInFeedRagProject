# docker network disconnect | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/network/disconnect/
**Word Count:** 750
**Links Count:** 481
**Scraped:** 2025-07-16 01:51:20
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker network disconnect

Description| Disconnect a container from a network   ---|---   Usage| `docker network disconnect [OPTIONS] NETWORK CONTAINER`      ## Description

Disconnects a container from a network. The container must be running to disconnect it from the network.

## Options

Option| Default| Description   ---|---|---   `-f, --force`| | Force the container to disconnect from a network      ## Examples               $ docker network disconnect multi-host-network container1