# docker scout sbom | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/scout/sbom/
**Word Count:** 1040
**Links Count:** 491
**Scraped:** 2025-07-16 01:52:00
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker scout sbom

Description| Generate or display SBOM of an image   ---|---   Usage| `docker scout sbom [IMAGE|DIRECTORY|ARCHIVE]`      ## Description

The `docker scout sbom` command analyzes a software artifact to generate a Software Bill Of Materials \(SBOM\).

The SBOM contains a list of all packages in the image. You can use the `--format` flag to filter the output of the command to display only packages of a specific type.

If no image is specified, the most recently built image is used.

The following artifact types are supported:

  * Images   * OCI layout directories   * Tarball archives, as created by `docker save`   * Local directory or file

By default, the tool expects an image reference, such as:

  * `redis`   * `curlimages/curl:7.87.0`   * `mcr.microsoft.com/dotnet/runtime:7.0`

If the artifact you want to analyze is an OCI directory, a tarball archive, a local file or directory, or if you want to control from where the image will be resolved, you must prefix the reference with one of the following:

  * `image://` \(default\) use a local image, or fall back to a registry lookup   * `local://` use an image from the local image store \(don't do a registry lookup\)   * `registry://` use an image from a registry \(don't use a local image\)   * `oci-dir://` use an OCI layout directory   * `archive://` use a tarball archive, as created by `docker save`   * `fs://` use a local directory or file

## Options

Option| Default| Description   ---|---|---   `--format`| `json`| Output format:   \- list: list of packages of the image   \- json: json representation of the SBOM   \- spdx: spdx representation of the SBOM   \- cyclonedx: cyclone dx representation of the SBOM   `--only-package-type`| | Comma separated list of package types \(like apk, deb, rpm, npm, pypi, golang, etc\)   Can only be used with --format list   `-o, --output`| | Write the report to a file   `--platform`| | Platform of image to analyze   `--ref`| | Reference to use if the provided tarball contains multiple references.   Can only be used with archive      ## Examples

### Display the list of packages               $ docker scout sbom --format list alpine     

### Only display packages of a specific type                $ docker scout sbom --format list --only-package-type apk alpine     

### Display the full SBOM in JSON format               $ docker scout sbom alpine     

### Display the full SBOM of the most recently built image               $ docker scout sbom     

### Write SBOM to a file               $ docker scout sbom --output alpine.sbom alpine