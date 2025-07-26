# Filter commands | Docker Docs

**URL:** https://docs.docker.com/engine/cli/filter/
**Word Count:** 1411
**Links Count:** 667
**Scraped:** 2025-07-16 01:47:50
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Filter commands

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

You can use the `--filter` flag to scope your commands. When filtering, the commands only include entries that match the pattern you specify.

## Using filters

The `--filter` flag expects a key-value pair separated by an operator.               $ docker COMMAND --filter "KEY=VALUE"     

The key represents the field that you want to filter on. The value is the pattern that the specified field must match. The operator can be either equals \(`=`\) or not equals \(`!=`\).

For example, the command `docker images --filter reference=alpine` filters the output of the `docker images` command to only print `alpine` images.               $ docker images     REPOSITORY   TAG       IMAGE ID       CREATED          SIZE     ubuntu       24.04     33a5cc25d22c   36 minutes ago   101MB     ubuntu       22.04     152dc042452c   36 minutes ago   88.1MB     alpine       3.21      a8cbb8c69ee7   40 minutes ago   8.67MB     alpine       latest    7144f7bab3d4   40 minutes ago   11.7MB     busybox      uclibc    3e516f71d880   48 minutes ago   2.4MB     busybox      glibc     7338d0c72c65   48 minutes ago   6.09MB     $ docker images --filter reference=alpine     REPOSITORY   TAG       IMAGE ID       CREATED          SIZE     alpine       3.21      a8cbb8c69ee7   40 minutes ago   8.67MB     alpine       latest    7144f7bab3d4   40 minutes ago   11.7MB     

The available fields \(`reference` in this case\) depend on the command you run. Some filters expect an exact match. Others handle partial matches. Some filters let you use regular expressions.

Refer to the CLI reference description for each command to learn about the supported filtering capabilities for each command.

## Combining filters

You can combine multiple filters by passing multiple `--filter` flags. The following example shows how to print all images that match `alpine:latest` or `busybox` \- a logical `OR`.               $ docker images     REPOSITORY   TAG       IMAGE ID       CREATED       SIZE     ubuntu       24.04     33a5cc25d22c   2 hours ago   101MB     ubuntu       22.04     152dc042452c   2 hours ago   88.1MB     alpine       3.21      a8cbb8c69ee7   2 hours ago   8.67MB     alpine       latest    7144f7bab3d4   2 hours ago   11.7MB     busybox      uclibc    3e516f71d880   2 hours ago   2.4MB     busybox      glibc     7338d0c72c65   2 hours ago   6.09MB     $ docker images --filter reference=alpine:latest --filter=reference=busybox     REPOSITORY   TAG       IMAGE ID       CREATED       SIZE     alpine       latest    7144f7bab3d4   2 hours ago   11.7MB     busybox      uclibc    3e516f71d880   2 hours ago   2.4MB     busybox      glibc     7338d0c72c65   2 hours ago   6.09MB     

### Multiple negated filters

Some commands support negated filters on [labels](https://docs.docker.com/engine/manage-resources/labels/). Negated filters only consider results that don't match the specified patterns. The following command prunes all containers that aren't labeled `foo`.               $ docker container prune --filter "label!=foo"     

There's a catch in combining multiple negated label filters. Multiple negated filters create a single negative constraint - a logical `AND`. The following command prunes all containers except those labeled both `foo` and `bar`. Containers labeled either `foo` or `bar`, but not both, will be pruned.               $ docker container prune --filter "label!=foo" --filter "label!=bar"     

## Reference

For more information about filtering commands, refer to the CLI reference description for commands that support the `--filter` flag:

  * [`docker config ls`](https://docs.docker.com/reference/cli/docker/config/ls/)   * [`docker container prune`](https://docs.docker.com/reference/cli/docker/container/prune/)   * [`docker image prune`](https://docs.docker.com/reference/cli/docker/image/prune/)   * [`docker image ls`](https://docs.docker.com/reference/cli/docker/image/ls/)   * [`docker network ls`](https://docs.docker.com/reference/cli/docker/network/ls/)   * [`docker network prune`](https://docs.docker.com/reference/cli/docker/network/prune/)   * [`docker node ls`](https://docs.docker.com/reference/cli/docker/node/ls/)   * [`docker node ps`](https://docs.docker.com/reference/cli/docker/node/ps/)   * [`docker plugin ls`](https://docs.docker.com/reference/cli/docker/plugin/ls/)   * [`docker container ls`](https://docs.docker.com/reference/cli/docker/container/ls/)   * [`docker search`](https://docs.docker.com/reference/cli/docker/search/)   * [`docker secret ls`](https://docs.docker.com/reference/cli/docker/secret/ls/)   * [`docker service ls`](https://docs.docker.com/reference/cli/docker/service/ls/)   * [`docker service ps`](https://docs.docker.com/reference/cli/docker/service/ps/)   * [`docker stack ps`](https://docs.docker.com/reference/cli/docker/stack/ps/)   * [`docker system prune`](https://docs.docker.com/reference/cli/docker/system/prune/)   * [`docker volume ls`](https://docs.docker.com/reference/cli/docker/volume/ls/)   * [`docker volume prune`](https://docs.docker.com/reference/cli/docker/volume/prune/)