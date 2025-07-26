# docker scout quickview | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/scout/quickview
**Word Count:** 1127
**Links Count:** 487
**Scraped:** 2025-07-16 01:55:49
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker scout quickview

Description| Quick overview of an image   ---|---   Usage| `docker scout quickview [IMAGE|DIRECTORY|ARCHIVE]`   AliasesAn alias is a short or memorable alternative for a longer command.| `docker scout qv`      ## Description

The `docker scout quickview` command displays a quick overview of an image. It displays a summary of the vulnerabilities in the specified image and vulnerabilities from the base image. If available, it also displays base image refresh and update recommendations.

If no image is specified, the most recently built image is used.

The following artifact types are supported:

  * Images   * OCI layout directories   * Tarball archives, as created by `docker save`   * Local directory or file

By default, the tool expects an image reference, such as:

  * `redis`   * `curlimages/curl:7.87.0`   * `mcr.microsoft.com/dotnet/runtime:7.0`

If the artifact you want to analyze is an OCI directory, a tarball archive, a local file or directory, or if you want to control from where the image will be resolved, you must prefix the reference with one of the following:

  * `image://` \(default\) use a local image, or fall back to a registry lookup   * `local://` use an image from the local image store \(don't do a registry lookup\)   * `registry://` use an image from a registry \(don't use a local image\)   * `oci-dir://` use an OCI layout directory   * `archive://` use a tarball archive, as created by `docker save`   * `fs://` use a local directory or file   * `sbom://` SPDX file or in-toto attestation file with SPDX predicate or `syft` json SBOM file In case of `sbom://` prefix, if the file is not defined then it will try to read it from the standard input.

## Options

Option| Default| Description   ---|---|---   `--env`| | Name of the environment   `--ignore-suppressed`| | Filter CVEs found in Scout exceptions based on the specified exception scope      `--latest`| | Latest indexed image   `--only-policy`| | Comma separated list of policies to evaluate   `--only-vex-affected`| | Filter CVEs by VEX statements with status not affected   `--org`| | Namespace of the Docker organization   `-o, --output`| | Write the report to a file   `--platform`| | Platform of image to analyze   `--ref`| | Reference to use if the provided tarball contains multiple references.   Can only be used with archive   `--vex-author`| | List of VEX statement authors to accept   `--vex-location`| | File location of directory or file containing VEX statements      ## Examples

### Quick overview of an image               $ docker scout quickview golang:1.19.4         ...Pulling         â Pulled         â SBOM of image already cached, 278 packages indexed            Your image  golang:1.19.4                          â    5C     3H     6M    63L       Base image  buildpack-deps:bullseye-scm            â    5C     1H     3M    48L     6?       Refreshed base image  buildpack-deps:bullseye-scm  â    0C     0H     0M    42L                                                          â    -5     -1     -3     -6     -6       Updated base image  buildpack-deps:sid-scm         â    0C     0H     1M    29L                                                          â    -5     -1     -2    -19     -6     

### Quick overview of the most recently built image               $ docker scout qv     

### Quick overview from an SPDX file               $  syft -o spdx-json alpine:3.16.1 | docker scout quickview sbom://      â Loaded image                                                                                                                              alpine:3.16.1      â Parsed image                                                                    sha256:3d81c46cd8756ddb6db9ec36fa06a6fb71c287fb265232ba516739dc67a5f07d      â Cataloged contents                                                                     274a317d88b54f9e67799244a1250cad3fe7080f45249fa9167d1f871218d35f        âââ â Packages                        [14 packages]        âââ â File digests                    [75 files]        âââ â File metadata                   [75 locations]        âââ â Executables                     [16 executables]            Target   â <stdin>        â    1C     2H     8M     0L         digest â  274a317d88b5  â