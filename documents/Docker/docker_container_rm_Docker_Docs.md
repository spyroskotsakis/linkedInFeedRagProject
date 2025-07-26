# docker container rm | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/container/rm
**Word Count:** 1073
**Links Count:** 498
**Scraped:** 2025-07-16 01:55:05
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker container rm

Description| Remove one or more containers   ---|---   Usage| `docker container rm [OPTIONS] CONTAINER [CONTAINER...]`   AliasesAn alias is a short or memorable alternative for a longer command.| `docker container remove` `docker rm`      ## Description

Remove one or more containers

## Options

Option| Default| Description   ---|---|---   `-f, --force`| | Force the removal of a running container \(uses SIGKILL\)   `-l, --link`| | Remove the specified link   `-v, --volumes`| | Remove anonymous volumes associated with the container      ## Examples

### Remove a container

This removes the container referenced under the link `/redis`.               $ docker rm /redis          /redis     

### Remove a link specified with `--link` on the default bridge network \(--link\)

This removes the underlying link between `/webapp` and the `/redis` containers on the default bridge network, removing all network communication between the two containers. This does not apply when `--link` is used with user-specified networks.               $ docker rm --link /webapp/redis          /webapp/redis     

### Force-remove a running container \(--force\)

This command force-removes a running container.               $ docker rm --force redis          redis     

The main process inside the container referenced under the link `redis` will receive `SIGKILL`, then the container will be removed.

### Remove all stopped containers

Use the [`docker container prune`](https://docs.docker.com/reference/cli/docker/container/prune/) command to remove all stopped containers, or refer to the [`docker system prune`](https://docs.docker.com/reference/cli/docker/system/prune/) command to remove unused containers in addition to other Docker resources, such as \(unused\) images and networks.

Alternatively, you can use the `docker ps` with the `-q` / `--quiet` option to generate a list of container IDs to remove, and use that list as argument for the `docker rm` command.

Combining commands can be more flexible, but is less portable as it depends on features provided by the shell, and the exact syntax may differ depending on what shell is used. To use this approach on Windows, consider using PowerShell or Bash.

The example below uses `docker ps -q` to print the IDs of all containers that have exited \(`--filter status=exited`\), and removes those containers with the `docker rm` command:               $ docker rm $(docker ps --filter status=exited -q)     

Or, using the `xargs` Linux utility:               $ docker ps --filter status=exited -q | xargs docker rm     

### Remove a container and its volumes \(-v, --volumes\)               $ docker rm --volumes redis     redis     

This command removes the container and any volumes associated with it. Note that if a volume was specified with a name, it will not be removed.

### Remove a container and selectively remove volumes               $ docker create -v awesome:/foo -v /bar --name hello redis     hello          $ docker rm -v hello     

In this example, the volume for `/foo` remains intact, but the volume for `/bar` is removed. The same behavior holds for volumes inherited with `--volumes-from`.