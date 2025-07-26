# docker compose bridge convert | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/compose/bridge/convert/
**Word Count:** 757
**Links Count:** 480
**Scraped:** 2025-07-16 01:50:39
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker compose bridge convert

Description| Convert compose files to Kubernetes manifests, Helm charts, or another model   ---|---   Usage| `docker compose bridge convert`      ## Description

Convert compose files to Kubernetes manifests, Helm charts, or another model

## Options

Option| Default| Description   ---|---|---   `-o, --output`| `out`| The output directory for the Kubernetes resources   `--templates`| | Directory containing transformation templates   `-t, --transformation`| | Transformation to apply to compose model \(default: docker/compose-bridge-kubernetes\)