# docker scout attestation add | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/scout/attestation/add/
**Word Count:** 799
**Links Count:** 480
**Scraped:** 2025-07-16 01:51:40
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker scout attestation add

Description| Add attestation to image   ---|---   Usage| `docker scout attestation add OPTIONS IMAGE [IMAGE...]`   AliasesAn alias is a short or memorable alternative for a longer command.| `docker scout attest add`      **Experimental**

**This command is experimental.**

Experimental features are intended for testing and feedback as their functionality or design may change between releases without warning or can be removed entirely in a future release.

## Description

The docker scout attestation add command adds attestations to images.

## Options

Option| Default| Description   ---|---|---   `--file`| | File location of attestations to attach   `--org`| | Namespace of the Docker organization   `--predicate-type`| | Predicate-type for attestations   `--referrer`| | Use OCI referrer API for pushing attestation   `--referrer-repository`| `registry.scout.docker.com`| Repository to push referrer to