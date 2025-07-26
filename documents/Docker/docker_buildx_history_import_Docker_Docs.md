# docker buildx history import | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/buildx/history/import
**Word Count:** 829
**Links Count:** 489
**Scraped:** 2025-07-16 01:56:34
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker buildx history import

Description| Import build records into Docker Desktop   ---|---   Usage| `docker buildx history import [OPTIONS] -`      ## Description

Import a build record from a `.dockerbuild` archive into Docker Desktop. This lets you view, inspect, and analyze builds created in other environments or CI pipelines.

## Options

Option| Default| Description   ---|---|---   `-f, --file`| | Import from a file path      ## Examples

### Import a `.dockerbuild` archive from standard input               docker buildx history import < mybuild.dockerbuild     

### Import a build archive from a file \(--file\)               docker buildx history import --file ./artifacts/backend-build.dockerbuild     

### Open a build manually

By default, the `import` command automatically opens the imported build in Docker Desktop. You don't need to run `open` unless you're opening a specific build or re-opening it later.

If you've imported multiple builds, you can open one manually:               docker buildx history open ci-build