# docker scout recommendations | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/scout/recommendations
**Word Count:** 964
**Links Count:** 487
**Scraped:** 2025-07-16 01:55:05
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker scout recommendations

Description| Display available base image updates and remediation recommendations   ---|---   Usage| `docker scout recommendations [IMAGE|DIRECTORY|ARCHIVE]`      ## Description

The `docker scout recommendations` command display recommendations for base images updates. It analyzes the image and display recommendations to refresh or update the base image. For each recommendation it shows a list of benefits, such as fewer vulnerabilities or smaller image size.

If no image is specified, the most recently built image is used.

The following artifact types are supported:

  * Images   * OCI layout directories   * Tarball archives, as created by `docker save`   * Local directory or file

By default, the tool expects an image reference, such as:

  * `redis`   * `curlimages/curl:7.87.0`   * `mcr.microsoft.com/dotnet/runtime:7.0`

If the artifact you want to analyze is an OCI directory, a tarball archive, a local file or directory, or if you want to control from where the image will be resolved, you must prefix the reference with one of the following:

  * `image://` \(default\) use a local image, or fall back to a registry lookup   * `local://` use an image from the local image store \(don't do a registry lookup\)   * `registry://` use an image from a registry \(don't use a local image\)   * `oci-dir://` use an OCI layout directory   * `archive://` use a tarball archive, as created by `docker save`   * `fs://` use a local directory or file

## Options

Option| Default| Description   ---|---|---   `--only-refresh`| | Only display base image refresh recommendations   `--only-update`| | Only display base image update recommendations   `--org`| | Namespace of the Docker organization   `-o, --output`| | Write the report to a file   `--platform`| | Platform of image to analyze   `--ref`| | Reference to use if the provided tarball contains multiple references.   Can only be used with archive   `--tag`| | Specify tag      ## Examples

### Display base image update recommendations               $ docker scout recommendations golang:1.19.4     

### Display base image refresh only recommendations               $ docker scout recommendations --only-refresh golang:1.19.4     

### Display base image update only recommendations               $ docker scout recommendations --only-update golang:1.19.4