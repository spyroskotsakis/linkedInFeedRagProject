# docker scout repo disable | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/scout/repo/disable/
**Word Count:** 822
**Links Count:** 490
**Scraped:** 2025-07-16 01:52:00
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker scout repo disable

Description| Disable Docker Scout   ---|---   Usage| `docker scout repo disable [REPOSITORY]`      ## Description

The docker scout repo disable command disables Docker Scout on repositories.

## Options

Option| Default| Description   ---|---|---   `--all`| | Disable all repositories of the organization. Can not be used with --filter.      `--filter`| | Regular expression to filter repositories by name   `--integration`| | Name of the integration to use for enabling an image   `--org`| | Namespace of the Docker organization   `--registry`| | Container Registry      ## Examples

### Disable a specific repository               $ docker scout repo disable my/repository     

### Disable all repositories of the organization               $ docker scout repo disable --all     

### Disable some repositories based on a filter               $ docker scout repo disable --filter namespace/backend     

### Disable a repository from a specific registry               $ docker scout repo disable my/repository --registry 123456.dkr.ecr.us-east-1.amazonaws.com