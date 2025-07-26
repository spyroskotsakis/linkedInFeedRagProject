# containerd image store | Docker Docs

**URL:** https://docs.docker.com/desktop/features/containerd
**Word Count:** 1443
**Links Count:** 652
**Scraped:** 2025-07-16 02:00:24
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# containerd image store

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Docker Desktop is transitioning to use containerd for image and filesystem management. This page outlines the benefits, setup process, and new capabilities enabled by the containerd image store.

> Note >  > Docker Desktop maintains separate image stores for the classic and containerd image stores. When switching between them, images and containers from the inactive store remain on disk but are hidden until you switch back.

## What is `containerd`?

`containerd` is a container runtime that provides a lightweight, consistent interface for container lifecycle management. It is already used under the hood by Docker Engine for creating, starting, and stopping containers.

Docker Desktopâs ongoing integration of containerd now extends to the image store, offering more flexibility and modern image support.

## What is the `containerd` image store?

The image store is the component responsible for pushing, pulling, and storing images on the filesystem.

The classic Docker image store is limited in the types of images that it supports. For example, it doesn't support image indices, containing manifest lists. When you create multi-platform images, for example, the image index resolves all the platform-specific variants of the image. An image index is also required when building images with attestations.

The containerd image store extends the range of image types that the Docker Engine can natively interact with. While this is a low-level architectural change, it's a prerequisite for unlocking a range of new use cases, including:

  * Build multi-platform images and images with attestations   * Support for using containerd snapshotters with unique characteristics, such as [stargz](https://github.com/containerd/stargz-snapshotter) for lazy-pulling images on container startup, or [nydus](https://github.com/containerd/nydus-snapshotter) and [dragonfly](https://github.com/dragonflyoss/image-service) for peer-to-peer image distribution.   * Ability to run [Wasm](https://docs.docker.com/desktop/features/wasm/) containers

## Enable the containerd image store

The containerd image store is enabled by default in Docker Desktop version 4.34 and later, but only for clean installs or if you perform a factory reset. If you upgrade from an earlier version of Docker Desktop, or if you use an older version of Docker Desktop you must manually switch to the containerd image store.

To manually enable this feature in Docker Desktop:

  1. Navigate to **Settings** in Docker Desktop.   2. In the **General** tab, check **Use containerd for pulling and storing images**.   3. Select **Apply**.

To disable the containerd image store, clear the **Use containerd for pulling and storing images** checkbox.

## Build multi-platform images

The term multi-platform image refers to a bundle of images for multiple different architectures. Out of the box, the default builder for Docker Desktop doesn't support building multi-platform images.               $ docker build --platform=linux/amd64,linux/arm64 .     [+] Building 0.0s (0/0)     ERROR: Multi-platform build is not supported for the docker driver.     Switch to a different driver, or turn on the containerd image store, and try again.     Learn more at https://docs.docker.com/go/build-multi-platform/     

Enabling the containerd image store lets you build multi-platform images and load them to your local image store: