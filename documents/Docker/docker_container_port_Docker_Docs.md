# docker container port | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/container/port
**Word Count:** 804
**Links Count:** 481
**Scraped:** 2025-07-16 01:55:05
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker container port

Description| List port mappings or a specific mapping for the container   ---|---   Usage| `docker container port CONTAINER [PRIVATE_PORT[/PROTO]]`   AliasesAn alias is a short or memorable alternative for a longer command.| `docker port`      ## Description

List port mappings or a specific mapping for the container

## Examples

### Show all mapped ports

You can find out all the ports mapped by not specifying a `PRIVATE_PORT`, or just a specific mapping:               $ docker ps          CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                                            NAMES     b650456536c7        busybox:latest      top                 54 minutes ago      Up 54 minutes       0.0.0.0:1234->9876/tcp, 0.0.0.0:4321->7890/tcp   test          $ docker port test          7890/tcp -> 0.0.0.0:4321     9876/tcp -> 0.0.0.0:1234          $ docker port test 7890/tcp          0.0.0.0:4321          $ docker port test 7890/udp          2014/06/24 11:53:36 Error: No public port '7890/udp' published for test          $ docker port test 7890          0.0.0.0:4321