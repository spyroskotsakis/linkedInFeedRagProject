# docker scout repo list | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/scout/repo/list
**Word Count:** 771
**Links Count:** 480
**Scraped:** 2025-07-16 01:56:34
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker scout repo list

Description| List Docker Scout repositories   ---|---   Usage| `docker scout repo list`      ## Description

The docker scout repo list command shows all repositories in an organization.

If ORG is not provided the default configured organization will be used.

## Options

Option| Default| Description   ---|---|---   `--filter`| | Regular expression to filter repositories by name   `--only-disabled`| | Filter to disabled repositories only   `--only-enabled`| | Filter to enabled repositories only   `--only-registry`| | Filter to a specific registry only:   \- hub.docker.com   \- ecr \(AWS ECR\)   `--org`| | Namespace of the Docker organization