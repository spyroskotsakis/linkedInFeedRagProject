# docker plugin push | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/plugin/push/
**Word Count:** 778
**Links Count:** 482
**Scraped:** 2025-07-16 01:51:40
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker plugin push

Description| Push a plugin to a registry   ---|---   Usage| `docker plugin push [OPTIONS] PLUGIN[:TAG]`      ## Description

After you have created a plugin using `docker plugin create` and the plugin is ready for distribution, use `docker plugin push` to share your images to Docker Hub or a self-hosted registry.

Registry credentials are managed by [docker login](https://docs.docker.com/reference/cli/docker/login/).

## Options

Option| Default| Description   ---|---|---   `--disable-content-trust`| `true`| Skip image signing      ## Examples

The following example shows how to push a sample `user/plugin`.               $ docker plugin ls          ID             NAME                    DESCRIPTION                  ENABLED     69553ca1d456   user/plugin:latest      A sample plugin for Docker   false          $ docker plugin push user/plugin