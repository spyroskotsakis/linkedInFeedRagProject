# docker scout config | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/scout/config
**Word Count:** 768
**Links Count:** 485
**Scraped:** 2025-07-16 01:55:27
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker scout config

Description| Manage Docker Scout configuration   ---|---   Usage| `docker scout config [KEY] [VALUE]`      ## Description

`docker scout config` allows you to list, get and set Docker Scout configuration.

Available configuration key:

  * `organization`: Namespace of the Docker organization to be used by default.

## Examples

### List existing configuration               $ docker scout config     organization=my-org-namespace     

### Print configuration value               $ docker scout config organization     my-org-namespace     

### Set configuration value               $ docker scout config organization my-org-namespace         â Successfully set organization to my-org-namespace