# docker scout compare | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/scout/compare
**Word Count:** 1234
**Links Count:** 493
**Scraped:** 2025-07-16 01:57:40
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker scout compare

Description| Compare two images and display differences \(experimental\)   ---|---   Usage| `docker scout compare --to IMAGE|DIRECTORY|ARCHIVE [IMAGE|DIRECTORY|ARCHIVE]`   AliasesAn alias is a short or memorable alternative for a longer command.| `docker scout diff`      **Experimental**

**This command is experimental.**

Experimental features are intended for testing and feedback as their functionality or design may change between releases without warning or can be removed entirely in a future release.

## Description

The `docker scout compare` command analyzes two images and displays a comparison.

> This command is **experimental** and its behaviour might change in the future

The intended use of this command is to compare two versions of the same image. For instance, when a new image is built and compared to the version running in production.

If no image is specified, the most recently built image is used as a comparison target.

The following artifact types are supported:

  * Images   * OCI layout directories   * Tarball archives, as created by `docker save`   * Local directory or file

By default, the tool expects an image reference, such as:

  * `redis`   * `curlimages/curl:7.87.0`   * `mcr.microsoft.com/dotnet/runtime:7.0`

If the artifact you want to analyze is an OCI directory, a tarball archive, a local file or directory, or if you want to control from where the image will be resolved, you must prefix the reference with one of the following:

  * `image://` \(default\) use a local image, or fall back to a registry lookup   * `local://` use an image from the local image store \(don't do a registry lookup\)   * `registry://` use an image from a registry \(don't use a local image\)   * `oci-dir://` use an OCI layout directory   * `archive://` use a tarball archive, as created by `docker save`   * `fs://` use a local directory or file   * `sbom://` SPDX file or in-toto attestation file with SPDX predicate or `syft` json SBOM file

## Options

Option| Default| Description   ---|---|---   `-x, --exit-on`| | Comma separated list of conditions to fail the action step if worse or changed, options are: vulnerability, policy, package      `--format`| `text`| Output format of the generated vulnerability report:   \- text: default output, plain text with or without colors depending on the terminal   \- markdown: Markdown output   `--hide-policies`| | Hide policy status from the output   `--ignore-base`| | Filter out CVEs introduced from base image   `--ignore-unchanged`| | Filter out unchanged packages   `--multi-stage`| | Show packages from multi-stage Docker builds   `--only-fixed`| | Filter to fixable CVEs   `--only-package-type`| | Comma separated list of package types \(like apk, deb, rpm, npm, pypi, golang, etc\)      `--only-policy`| | Comma separated list of policies to evaluate   `--only-severity`| | Comma separated list of severities \(critical, high, medium, low, unspecified\) to filter CVEs by      `--only-stage`| | Comma separated list of multi-stage Docker build stage names   `--only-unfixed`| | Filter to unfixed CVEs   `--org`| | Namespace of the Docker organization   `-o, --output`| | Write the report to a file   `--platform`| | Platform of image to analyze   `--ref`| | Reference to use if the provided tarball contains multiple references.   Can only be used with archive   `--to`| | Image, directory, or archive to compare to   `--to-env`| | Name of environment to compare to   `--to-latest`| | Latest image processed to compare to   `--to-ref`| | Reference to use if the provided tarball contains multiple references.   Can only be used with archive.      ## Examples

### Compare the most recently built image to the latest tag               $ docker scout compare --to namespace/repo:latest     

### Compare local build to the same tag from the registry               $ docker scout compare local://namespace/repo:latest --to registry://namespace/repo:latest     

### Ignore base images               $ docker scout compare --ignore-base --to namespace/repo:latest namespace/repo:v1.2.3-pre     

### Generate a markdown output               $ docker scout compare --format markdown --to namespace/repo:latest namespace/repo:v1.2.3-pre     

### Only compare maven packages and only display critical vulnerabilities for maven packages               $ docker scout compare --only-package-type maven --only-severity critical --to namespace/repo:latest namespace/repo:v1.2.3-pre     

### Show all policy results for both images               docker scout compare --to namespace/repo:latest namespace/repo:v1.2.3-pre