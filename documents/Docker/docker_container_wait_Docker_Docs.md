# docker container wait | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/container/wait
**Word Count:** 794
**Links Count:** 479
**Scraped:** 2025-07-16 01:57:40
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker container wait

Description| Block until one or more containers stop, then print their exit codes   ---|---   Usage| `docker container wait CONTAINER [CONTAINER...]`   AliasesAn alias is a short or memorable alternative for a longer command.| `docker wait`      ## Description

Block until one or more containers stop, then print their exit codes

## Examples

Start a container in the background.               $ docker run -dit --name=my_container ubuntu bash     

Run `docker wait`, which should block until the container exits.               $ docker wait my_container     

In another terminal, stop the first container. The `docker wait` command above returns the exit code.               $ docker stop my_container     

This is the same `docker wait` command from above, but it now exits, returning `0`.               $ docker wait my_container          0