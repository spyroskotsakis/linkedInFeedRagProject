# docker buildx history export | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/buildx/history/export
**Word Count:** 954
**Links Count:** 495
**Scraped:** 2025-07-16 01:55:05
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker buildx history export

Description| Export build records into Docker Desktop bundle   ---|---   Usage| `docker buildx history export [OPTIONS] [REF...]`      ## Description

Export one or more build records to `.dockerbuild` archive files. These archives contain metadata, logs, and build outputs, and can be imported into Docker Desktop or shared across environments.

## Options

Option| Default| Description   ---|---|---   `--all`| | Export all build records for the builder   `--finalize`| | Ensure build records are finalized before exporting   `-o, --output`| | Output file path      ## Examples

### Export all build records to a file \(--all\)

Use the `--all` flag and redirect the output:               docker buildx history export --all > all-builds.dockerbuild     

Or use the `--output` flag:               docker buildx history export --all -o all-builds.dockerbuild     

### Use a specific builder instance \(--builder\)               docker buildx history export --builder builder0 ^1 -o builder0-build.dockerbuild     

### Enable debug logging \(--debug\)               docker buildx history export --debug qu2gsuo8ejqrwdfii23xkkckt -o debug-build.dockerbuild     

### Ensure build records are finalized before exporting \(--finalize\)

Clients can report their own traces concurrently, and not all traces may be saved yet by the time of the export. Use the `--finalize` flag to ensure all traces are finalized before exporting.               docker buildx history export --finalize qu2gsuo8ejqrwdfii23xkkckt -o finalized-build.dockerbuild     

### Export a single build to a custom file \(--output\)               docker buildx history export qu2gsuo8ejqrwdfii23xkkckt --output mybuild.dockerbuild     

You can find build IDs by running:               docker buildx history ls     

To export two builds to separate files:               # Using build IDs     docker buildx history export qu2gsuo8ejqrwdfii23xkkckt qsiifiuf1ad9pa9qvppc0z1l3 -o multi.dockerbuild          # Or using relative offsets     docker buildx history export ^1 ^2 -o multi.dockerbuild     

Or use shell redirection:               docker buildx history export ^1 > mybuild.dockerbuild     docker buildx history export ^2 > backend-build.dockerbuild