# docker scout watch | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/scout/watch
**Word Count:** 923
**Links Count:** 489
**Scraped:** 2025-07-16 01:55:49
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker scout watch

Description| Watch repositories in a registry and push images and indexes to Docker Scout \(experimental\)   ---|---   Usage| `docker scout watch`      **Experimental**

**This command is experimental.**

Experimental features are intended for testing and feedback as their functionality or design may change between releases without warning or can be removed entirely in a future release.

## Description

The `docker scout watch` command watches repositories in a registry and pushes images or analysis results to Docker Scout.

## Options

Option| Default| Description   ---|---|---   `--all-images`| | Push all images instead of only the ones pushed during the watch command is running      `--dry-run`| | Watch images and prepare them, but do not push them   `--interval`| `60`| Interval in seconds between checks   `--org`| | Namespace of the Docker organization to which image will be pushed   `--refresh-registry`| | Refresh the list of repositories of a registry at every run. Only with --registry.      `--registry`| | Registry to watch   `--repository`| | Repository to watch   `--sbom`| `true`| Create and upload SBOMs   `--tag`| | Regular expression to match tags to watch   `--workers`| `3`| Number of concurrent workers      ## Examples

### Watch for new images from two repositories and push them               $ docker scout watch --org my-org --repository registry-1.example.com/repo-1 --repository registry-2.example.com/repo-2     

### Only push images with a specific tag               $ docker scout watch --org my-org --repository registry.example.com/my-service --tag latest     

### Watch all repositories of a registry               $ docker scout watch --org my-org --registry registry.example.com     

### Push all images and not just the new ones               $ docker scout watch--org my-org --repository registry.example.com/my-service --all-images