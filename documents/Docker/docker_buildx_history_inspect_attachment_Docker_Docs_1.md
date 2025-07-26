# docker buildx history inspect attachment | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/buildx/history/inspect/attachment/
**Word Count:** 869
**Links Count:** 490
**Scraped:** 2025-07-16 01:50:20
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker buildx history inspect attachment

Description| Inspect a build record attachment   ---|---   Usage| `docker buildx history inspect attachment [OPTIONS] REF [DIGEST]`      ## Description

Inspect a specific attachment from a build record, such as a provenance file or SBOM. Attachments are optional artifacts stored with the build and may be platform-specific.

## Options

Option| Default| Description   ---|---|---   `--platform`| | Platform of attachment   `--type`| | Type of attachment      ## Examples

### Inspect a provenance attachment from a build \(--type\)

Supported types include `provenance` and `sbom`.               $ docker buildx history inspect attachment qu2gsuo8ejqrwdfii23xkkckt --type provenance     {       "_type": "https://slsa.dev/provenance/v0.2",       "buildDefinition": {         "buildType": "https://build.docker.com/BuildKit@v1",         "externalParameters": {           "target": "app",           "platforms": ["linux/amd64"]         }       },       "runDetails": {         "builder": "docker",         "by": "ci@docker.com"       }     }     

### Inspect a SBOM for linux/amd64               $ docker buildx history inspect attachment ^0 \       --type sbom \       --platform linux/amd64     {       "bomFormat": "CycloneDX",       "specVersion": "1.5",       "version": 1,       "components": [         {           "type": "library",           "name": "alpine",           "version": "3.18.2"         }       ]     }     

### Inspect an attachment by digest

You can inspect an attachment directly using its digset, which you can get from the `inspect` output:               # Using a build ID     docker buildx history inspect attachment qu2gsuo8ejqrwdfii23xkkckt sha256:abcdef123456...          # Or using a relative offset     docker buildx history inspect attachment ^0 sha256:abcdef123456...     

Use `--type sbom` or `--type provenance` to filter attachments by type. To inspect a specific attachment by digest, omit the `--type` flag.