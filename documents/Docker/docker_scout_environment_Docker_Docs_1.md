# docker scout environment | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/scout/environment/
**Word Count:** 868
**Links Count:** 487
**Scraped:** 2025-07-16 01:51:40
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker scout environment

Description| Manage environments \(experimental\)   ---|---   Usage| `docker scout environment [ENVIRONMENT] [IMAGE]`   AliasesAn alias is a short or memorable alternative for a longer command.| `docker scout env`      **Experimental**

**This command is experimental.**

Experimental features are intended for testing and feedback as their functionality or design may change between releases without warning or can be removed entirely in a future release.

## Description

The `docker scout environment` command lists the environments. If you pass an image reference, the image is recorded to the specified environment.

Once recorded, environments can be referred to by their name. For example, you can refer to the `production` environment with the `docker scout compare` command as follows:               $ docker scout compare --to-env production     

## Options

Option| Default| Description   ---|---|---   `--org`| | Namespace of the Docker organization   `-o, --output`| | Write the report to a file   `--platform`| | Platform of image to record      ## Examples

### List existing environments               $ docker scout environment     prod     staging     

### List images of an environment               $ docker scout environment staging     namespace/repo:tag@sha256:9a4df4fadc9bbd44c345e473e0688c2066a6583d4741679494ba9228cfd93e1b     namespace/other-repo:tag@sha256:0001d6ce124855b0a158569c584162097fe0ca8d72519067c2c8e3ce407c580f     

### Record an image to an environment, for a specific platform               $ docker scout environment staging namespace/repo:stage-latest --platform linux/amd64     â Pulled     â Successfully recorded namespace/repo:stage-latest in environment staging