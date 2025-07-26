# docker scout repo enable | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/scout/repo/enable/
**Word Count:** 814
**Links Count:** 490
**Scraped:** 2025-07-16 01:52:00
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker scout repo enable

Description| Enable Docker Scout   ---|---   Usage| `docker scout repo enable [REPOSITORY]`      ## Description

The docker scout repo enable command enables Docker Scout on repositories.

## Options

Option| Default| Description   ---|---|---   `--all`| | Enable all repositories of the organization. Can not be used with --filter.      `--filter`| | Regular expression to filter repositories by name   `--integration`| | Name of the integration to use for enabling an image   `--org`| | Namespace of the Docker organization   `--registry`| | Container Registry      ## Examples

### Enable a specific repository               $ docker scout repo enable my/repository     

### Enable all repositories of the organization               $ docker scout repo enable --all     

### Enable some repositories based on a filter               $ docker scout repo enable --filter namespace/backend     

### Enable a repository from a specific registry               $ docker scout repo enable my/repository --registry 123456.dkr.ecr.us-east-1.amazonaws.com