# Prune unused Docker objects | Docker Docs

**URL:** https://docs.docker.com/engine/manage-resources/pruning
**Word Count:** 1728
**Links Count:** 655
**Scraped:** 2025-07-16 01:58:31
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Prune unused Docker objects

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Docker takes a conservative approach to cleaning up unused objects \(often referred to as "garbage collection"\), such as images, containers, volumes, and networks. These objects are generally not removed unless you explicitly ask Docker to do so. This can cause Docker to use extra disk space. For each type of object, Docker provides a `prune` command. In addition, you can use `docker system prune` to clean up multiple types of objects at once. This topic shows how to use these `prune` commands.

## Prune images

The `docker image prune` command allows you to clean up unused images. By default, `docker image prune` only cleans up _dangling_ images. A dangling image is one that isn't tagged, and isn't referenced by any container. To remove dangling images:               $ docker image prune          WARNING! This will remove all dangling images.     Are you sure you want to continue? [y/N] y     

To remove all images which aren't used by existing containers, use the `-a` flag:               $ docker image prune -a          WARNING! This will remove all images without at least one container associated to them.     Are you sure you want to continue? [y/N] y     

By default, you are prompted to continue. To bypass the prompt, use the `-f` or `--force` flag.

You can limit which images are pruned using filtering expressions with the `--filter` flag. For example, to only consider images created more than 24 hours ago:               $ docker image prune -a --filter "until=24h"     

Other filtering expressions are available. See the [`docker image prune` reference](https://docs.docker.com/reference/cli/docker/image/prune/) for more examples.

## Prune containers

When you stop a container, it isn't automatically removed unless you started it with the `--rm` flag. To see all containers on the Docker host, including stopped containers, use `docker ps -a`. You may be surprised how many containers exist, especially on a development system\! A stopped container's writable layers still take up disk space. To clean this up, you can use the `docker container prune` command.               $ docker container prune          WARNING! This will remove all stopped containers.     Are you sure you want to continue? [y/N] y     

By default, you're prompted to continue. To bypass the prompt, use the `-f` or `--force` flag.

By default, all stopped containers are removed. You can limit the scope using the `--filter` flag. For instance, the following command only removes stopped containers older than 24 hours:               $ docker container prune --filter "until=24h"     

Other filtering expressions are available. See the [`docker container prune` reference](https://docs.docker.com/reference/cli/docker/container/prune/) for more examples.

## Prune volumes

Volumes can be used by one or more containers, and take up space on the Docker host. Volumes are never removed automatically, because to do so could destroy data.               $ docker volume prune          WARNING! This will remove all volumes not used by at least one container.     Are you sure you want to continue? [y/N] y     

By default, you are prompted to continue. To bypass the prompt, use the `-f` or `--force` flag.

By default, all unused volumes are removed. You can limit the scope using the `--filter` flag. For instance, the following command only removes volumes which aren't labelled with the `keep` label:               $ docker volume prune --filter "label!=keep"     

Other filtering expressions are available. See the [`docker volume prune` reference](https://docs.docker.com/reference/cli/docker/volume/prune/) for more examples.

## Prune networks

Docker networks don't take up much disk space, but they do create `iptables` rules, bridge network devices, and routing table entries. To clean these things up, you can use `docker network prune` to clean up networks which aren't used by any containers.               $ docker network prune          WARNING! This will remove all networks not used by at least one container.     Are you sure you want to continue? [y/N] y     

By default, you're prompted to continue. To bypass the prompt, use the `-f` or `--force` flag.

By default, all unused networks are removed. You can limit the scope using the `--filter` flag. For instance, the following command only removes networks older than 24 hours:               $ docker network prune --filter "until=24h"     

Other filtering expressions are available. See the [`docker network prune` reference](https://docs.docker.com/reference/cli/docker/network/prune/) for more examples.

## Prune everything

The `docker system prune` command is a shortcut that prunes images, containers, and networks. Volumes aren't pruned by default, and you must specify the `--volumes` flag for `docker system prune` to prune volumes.               $ docker system prune          WARNING! This will remove:             - all stopped containers             - all networks not used by at least one container             - all dangling images             - unused build cache          Are you sure you want to continue? [y/N] y     

To also prune volumes, add the `--volumes` flag:               $ docker system prune --volumes          WARNING! This will remove:             - all stopped containers             - all networks not used by at least one container             - all volumes not used by at least one container             - all dangling images             - all build cache          Are you sure you want to continue? [y/N] y     

By default, you're prompted to continue. To bypass the prompt, use the `-f` or `--force` flag.

By default, all unused containers, networks, and images are removed. You can limit the scope using the `--filter` flag. For instance, the following command removes items older than 24 hours:               $ docker system prune --filter "until=24h"     

Other filtering expressions are available. See the [`docker system prune` reference](https://docs.docker.com/reference/cli/docker/system/prune/) for more examples.