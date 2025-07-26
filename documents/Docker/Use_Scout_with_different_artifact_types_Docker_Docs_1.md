# Use Scout with different artifact types | Docker Docs

**URL:** https://docs.docker.com/scout/how-tos/artifact-types/
**Word Count:** 1707
**Links Count:** 656
**Scraped:** 2025-07-16 01:54:28
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Use Scout with different artifact types

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Some of the Docker Scout CLI commands support prefixes for specifying the location or type of artifact that you would like to analyze.

By default, image analysis with the `docker scout cves` command targets images in the local image store of the Docker Engine. The following command always uses a local image if it exists:               $ docker scout cves <image>     

If the image doesn't exist locally, Docker pulls the image before running the analysis. Analyzing the same image again would use the same local version by default, even if the tag has since changed in the registry.

By adding a `registry://` prefix to the image reference, you can force Docker Scout to analyze the registry version of the image:               $ docker scout cves registry://<image>     

## Supported prefixes

The supported prefixes are:

Prefix| Description   ---|---   `image://` \(default\)| Use a local image, or fall back to a registry lookup   `local://`| Use an image from the local image store \(don't do a registry lookup\)   `registry://`| Use an image from a registry \(don't use a local image\)   `oci-dir://`| Use an OCI layout directory   `archive://`| Use a tarball archive, as created by `docker save`   `fs://`| Use a local directory or file      You can use prefixes with the following commands:

  * `docker scout compare`   * `docker scout cves`   * `docker scout quickview`   * `docker scout recommendations`   * `docker scout sbom`

## Examples

This section contains a few examples showing how you can use prefixes to specify artifacts for `docker scout` commands.

### Analyze a local project

The `fs://` prefix lets you analyze local source code directly, without having to build it into a container image. The following `docker scout quickview` command gives you an at-a-glance vulnerability summary of the source code in the current working directory:               $ docker scout quickview fs://.     

To view the details of vulnerabilities found in your local source code, you can use the `docker scout cves --details fs://.` command. Combine it with other flags to narrow down the results to the packages and vulnerabilities that you're interested in.               $ docker scout cves --details --only-severity high fs://.         â File system read         â Indexed 323 packages         â Detected 1 vulnerable package with 1 vulnerability          â## Overview                              â        Analyzed path     âââââââââââââââââââââ¼ââââââââââââââââââââââââââââââ       Path              â  /Users/david/demo/scoutfs         vulnerabilities â    0C     1H     0M     0L          â## Packages and Vulnerabilities             0C     1H     0M     0L  fastify 3.29.0     pkg:npm/fastify@3.29.0              â HIGH CVE-2022-39288 [OWASP Top Ten 2017 Category A9 - Using Components with Known Vulnerabilities]           https://scout.docker.com/v/CVE-2022-39288                fastify is a fast and low overhead web framework, for Node.js. Affected versions of           fastify are subject to a denial of service via malicious use of the Content-Type           header. An attacker can send an invalid Content-Type header that can cause the           application to crash. This issue has been addressed in commit  fbb07e8d  and will be           included in release version 4.8.1. Users are advised to upgrade. Users unable to           upgrade may manually filter out http content with malicious Content-Type headers.                Affected range : <4.8.1           Fixed version  : 4.8.1           CVSS Score     : 7.5           CVSS Vector    : CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H          1 vulnerability found in 1 package       LOW       0       MEDIUM    0       HIGH      1       CRITICAL  0     

### Compare a local project to an image

With `docker scout compare`, you can compare the analysis of source code on your local filesystem with the analysis of a container image. The following example compares local source code \(`fs://.`\) with a registry image `registry://docker/scout-cli:latest`. In this case, both the baseline and target for the comparison use prefixes.               $ docker scout compare fs://. --to registry://docker/scout-cli:latest --ignore-unchanged     WARN 'docker scout compare' is experimental and its behaviour might change in the future         â File system read         â Indexed 268 packages         â SBOM of image already cached, 234 packages indexed                 ## Overview                                     â              Analyzed File System              â              Comparison Image       ââââââââââââââââââââââââââ¼âââââââââââââââââââââââââââââââââââââââââââââââââ¼âââââââââââââââââââââââââââââââââââââââââââââ         Path / Image reference â  /Users/david/src/docker/scout-cli-plugin      â  docker/scout-cli:latest                                â                                                â  bb0b01303584           platform             â                                                â linux/arm64           provenance           â https://github.com/dvdksn/scout-cli-plugin.git â https://github.com/docker/scout-cli-plugin                                â  6ea3f7369dbdfec101ac7c0fa9d78ef05ffa6315      â  67cb4ef78bd69545af0e223ba5fb577b27094505           vulnerabilities      â    0C     0H     1M     1L                     â    0C     0H     1M     1L                                â                                                â           size                 â 7.4 MB (-14 MB)                                â 21 MB           packages             â 268 (+34)                                      â 234                                â                                                â                 ## Packages and Vulnerabilities                   +   55 packages added         -   21 packages removed            213 packages unchanged     

The previous example is truncated for brevity.

### View the SBOM of an image tarball

The following example shows how you can use the `archive://` prefix to get the SBOM of an image tarball, created with `docker save`. The image in this case is `docker/scout-cli:latest`, and the SBOM is exported to file `sbom.spdx.json` in SPDX format.               $ docker pull docker/scout-cli:latest     latest: Pulling from docker/scout-cli     257973a141f5: Download complete      1f2083724dd1: Download complete      5c8125a73507: Download complete      Digest: sha256:13318bb059b0f8b0b87b35ac7050782462b5d0ac3f96f9f23d165d8ed68d0894     $ docker save docker/scout-cli:latest -o scout-cli.tar     $ docker scout sbom --format spdx -o sbom.spdx.json archive://scout-cli.tar     

## Learn more

Read about the commands and supported flags in the CLI reference documentation:

  * [`docker scout quickview`](https://docs.docker.com/reference/cli/docker/scout/quickview/)   * [`docker scout cves`](https://docs.docker.com/reference/cli/docker/scout/cves/)   * [`docker scout compare`](https://docs.docker.com/reference/cli/docker/scout/compare/)