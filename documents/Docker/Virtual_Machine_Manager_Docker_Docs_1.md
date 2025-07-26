# Virtual Machine Manager | Docker Docs

**URL:** https://docs.docker.com/desktop/features/vmm
**Word Count:** 1484
**Links Count:** 653
**Scraped:** 2025-07-16 02:03:17
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Virtual Machine Manager for Docker Desktop on Mac

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Docker Desktop supports multiple Virtual Machine Managers \(VMMs\) to power the Linux VM that runs containers. You can choose the most suitable option based on your system architecture \(Intel or Apple Silicon\), performance needs, and feature requirements. This page provides an overview of the available options.

To change the VMM, go to **Settings** > **General** > **Virtual Machine Manager**.

## Docker VMM

Requires: Docker Desktop [4.35.0](https://docs.docker.com/desktop/release-notes/#4350) and later

For: Docker Desktop on Mac with Apple Silicon

Docker VMM is a new, container-optimized hypervisor. By optimizing both the Linux kernel and hypervisor layers, Docker VMM delivers significant performance enhancements across common developer tasks.

Some key performance enhancements provided by Docker VMM include:

  * Faster I/O operations: With a cold cache, iterating over a large shared filesystem with `find` is 2x faster than when the Apple Virtualization framework is used.   * Improved caching: With a warm cache, performance can improve by as much as 25x, even surpassing native Mac operations.

These improvements directly impact developers who rely on frequent file access and overall system responsiveness during containerized development. Docker VMM marks a significant leap in speed, enabling smoother workflows and faster iteration cycles.

> Note >  > Docker VMM requires a minimum of 4GB of memory to be allocated to the Docker Linux VM. The memory needs to be increased before Docker VMM is enabled, and this can be done from the **Resources** tab in **Settings**.

### Known issues

As Docker VMM is still in Beta, there are a few known limitations:

  * Docker VMM does not currently support Rosetta, so emulation of amd64 architectures is slow. Docker is exploring potential solutions.   * Certain databases, like MongoDB and Cassandra, may fail when using virtiofs with Docker VMM. This issue is expected to be resolved in a future release.

## Apple Virtualization framework

The Apple Virtualization framework is a stable and well-established option for managing virtual machines on Mac. It has been a reliable choice for many Mac users over the years. This framework is best suited for developers who prefer a proven solution with solid performance and broad compatibility.

## QEMU \(Legacy\) for Apple Silicon

> Note >  > QEMU will be deprecated on July 14, 2025. For more information, see the [blog announcement](https://www.docker.com/blog/docker-desktop-for-mac-qemu-virtualization-option-to-be-deprecated-in-90-days/)

QEMU is a legacy virtualization option for Apple Silicon Macs, primarily supported for older use cases.

Docker recommends transitioning to newer alternatives, such as Docker VMM or the Apple Virtualization framework, as they offer superior performance and ongoing support. Docker VMM, in particular, offers substantial speed improvements and a more efficient development environment, making it a compelling choice for developers working with Apple Silicon.

Note that this is not related to using QEMU to emulate non-native architectures in [multi-platform builds](https://docs.docker.com/build/building/multi-platform/#qemu).

## HyperKit \(Legacy\) for Intel-based Macs

> Note >  > HyperKit will be deprecated in a future release.

HyperKit is another legacy virtualization option, specifically for Intel-based Macs. Like QEMU, it is still available but considered deprecated. Docker recommends switching to modern alternatives for better performance and to future-proof your setup.