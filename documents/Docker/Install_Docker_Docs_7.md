# Install | Docker Docs

**URL:** https://docs.docker.com/engine/install/
**Word Count:** 1442
**Links Count:** 674
**Scraped:** 2025-07-16 01:46:25
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Install Docker Engine

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

This section describes how to install Docker Engine on Linux, also known as Docker CE. Docker Engine is also available for Windows, macOS, and Linux, through Docker Desktop. For instructions on how to install Docker Desktop, see: [Overview of Docker Desktop](https://docs.docker.com/desktop/).

## Supported platforms

Platform| x86\_64 / amd64| arm64 / aarch64| arm \(32-bit\)| ppc64le| s390x   ---|---|---|---|---|---   [CentOS](https://docs.docker.com/engine/install/centos/)| â | â | | â |    [Debian](https://docs.docker.com/engine/install/debian/)| â | â | â | â |    [Fedora](https://docs.docker.com/engine/install/fedora/)| â | â | | â |    [Raspberry Pi OS \(32-bit\)](https://docs.docker.com/engine/install/raspberry-pi-os/)| | | â | |    [RHEL](https://docs.docker.com/engine/install/rhel/)| â | â | | | â    [SLES](https://docs.docker.com/engine/install/sles/)| | | | | â    [Ubuntu](https://docs.docker.com/engine/install/ubuntu/)| â | â | â | â | â    [Binaries](https://docs.docker.com/engine/install/binaries/)| â | â | â | |       ### Other Linux distributions

> Note >  > While the following instructions may work, Docker doesn't test or verify installation on distribution derivatives.

  * If you use Debian derivatives such as "BunsenLabs Linux", "Kali Linux" or "LMDE" \(Debian-based Mint\) should follow the installation instructions for [Debian](https://docs.docker.com/engine/install/debian/), substitute the version of your distribution for the corresponding Debian release. Refer to the documentation of your distribution to find which Debian release corresponds with your derivative version.   * Likewise, if you use Ubuntu derivatives such as "Kubuntu", "Lubuntu" or "Xubuntu" you should follow the installation instructions for [Ubuntu](https://docs.docker.com/engine/install/ubuntu/), substituting the version of your distribution for the corresponding Ubuntu release. Refer to the documentation of your distribution to find which Ubuntu release corresponds with your derivative version.   * Some Linux distributions provide a package of Docker Engine through their package repositories. These packages are built and maintained by the Linux distribution's package maintainers and may have differences in configuration or are built from modified source code. Docker isn't involved in releasing these packages and you should report any bugs or issues involving these packages to your Linux distribution's issue tracker.

Docker provides [binaries](https://docs.docker.com/engine/install/binaries/) for manual installation of Docker Engine. These binaries are statically linked and you can use them on any Linux distribution.

## Release channels

Docker Engine has two types of update channels, **stable** and **test** :

  * The **stable** channel gives you the latest versions released for general availability.   * The **test** channel gives you pre-release versions that are ready for testing before general availability.

Use the test channel with caution. Pre-release versions include experimental and early-access features that are subject to breaking changes.

## Support

Docker Engine is an open source project, supported by the Moby project maintainers and community members. Docker doesn't provide support for Docker Engine. Docker provides support for Docker products, including Docker Desktop, which uses Docker Engine as one of its components.

For information about the open source project, refer to the [Moby project website](https://mobyproject.org/).

### Upgrade path

Patch releases are always backward compatible with its major and minor version.

### Licensing

Docker Engine is licensed under the Apache License, Version 2.0. See [LICENSE](https://github.com/moby/moby/blob/master/LICENSE) for the full license text.

## Reporting security issues

If you discover a security issue, we request that you bring it to our attention immediately.

DO NOT file a public issue. Instead, submit your report privately to [security@docker.com](mailto:security@docker.com).

Security reports are greatly appreciated, and Docker will publicly thank you for it.

## Get started

After setting up Docker, you can learn the basics with [Getting started with Docker](https://docs.docker.com/get-started/introduction/).