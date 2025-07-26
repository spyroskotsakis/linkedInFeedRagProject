# Docker container driver | Docker Docs

**URL:** https://docs.docker.com/build/builders/drivers/docker-container/
**Word Count:** 1520
**Links Count:** 665
**Scraped:** 2025-07-16 01:50:59
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Docker container driver

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

The Docker container driver allows creation of a managed and customizable BuildKit environment in a dedicated Docker container.

Using the Docker container driver has a couple of advantages over the default Docker driver. For example:

  * Specify custom BuildKit versions to use.   * Build multi-arch images, see QEMU   * Advanced options for [cache import and export](https://docs.docker.com/build/cache/backends/)

## Synopsis

Run the following command to create a new builder, named `container`, that uses the Docker container driver:               $ docker buildx create \       --name container \       --driver=docker-container \       --driver-opt=[key=value,...]     container     

The following table describes the available driver-specific options that you can pass to `--driver-opt`:

Parameter| Type| Default| Description   ---|---|---|---   `image`| String| | Sets the BuildKit image to use for the container.   `memory`| String| | Sets the amount of memory the container can use.   `memory-swap`| String| | Sets the memory swap limit for the container.   `cpu-quota`| String| | Imposes a CPU CFS quota on the container.   `cpu-period`| String| | Sets the CPU CFS scheduler period for the container.   `cpu-shares`| String| | Configures CPU shares \(relative weight\) of the container.   `cpuset-cpus`| String| | Limits the set of CPU cores the container can use.   `cpuset-mems`| String| | Limits the set of CPU memory nodes the container can use.   `default-load`| Boolean| `false`| Automatically load images to the Docker Engine image store.   `network`| String| | Sets the network mode for the container.   `cgroup-parent`| String| `/docker/buildx`| Sets the cgroup parent of the container if Docker is using the "cgroupfs" driver.   `restart-policy`| String| `unless-stopped`| Sets the container's [restart policy](https://docs.docker.com/engine/containers/start-containers-automatically/#use-a-restart-policy).   `env.<key>`| String| | Sets the environment variable `key` to the specified `value` in the container.      Before you configure the resource limits for the container, read about [configuring runtime resource constraints for containers](https://docs.docker.com/engine/containers/resource_constraints/).

## Usage

When you run a build, Buildx pulls the specified `image` \(by default, [`moby/buildkit`](https://hub.docker.com/r/moby/buildkit)\). When the container has started, Buildx submits the build submitted to the containerized build server.               $ docker buildx build -t <image> --builder=container .     WARNING: No output specified with docker-container driver. Build result will only remain in the build cache. To push result image into registry use --push or to load image into docker use --load     #1 [internal] booting buildkit     #1 pulling image moby/buildkit:buildx-stable-1     #1 pulling image moby/buildkit:buildx-stable-1 1.9s done     #1 creating container buildx_buildkit_container0     #1 creating container buildx_buildkit_container0 0.5s done     #1 DONE 2.4s     ...     

## Cache persistence

The `docker-container` driver supports cache persistence, as it stores all the BuildKit state and related cache into a dedicated Docker volume.

To persist the `docker-container` driver's cache, even after recreating the driver using `docker buildx rm` and `docker buildx create`, you can destroy the builder using the `--keep-state` flag:

For example, to create a builder named `container` and then remove it while persisting state:               # setup a builder     $ docker buildx create --name=container --driver=docker-container --use --bootstrap     container     $ docker buildx ls     NAME/NODE       DRIVER/ENDPOINT              STATUS   BUILDKIT PLATFORMS     container *     docker-container       container0    desktop-linux                running  v0.10.5  linux/amd64     $ docker volume ls     DRIVER    VOLUME NAME     local     buildx_buildkit_container0_state          # remove the builder while persisting state     $ docker buildx rm --keep-state container     $ docker volume ls     DRIVER    VOLUME NAME     local     buildx_buildkit_container0_state          # the newly created driver with the same name will have all the state of the previous one!     $ docker buildx create --name=container --driver=docker-container --use --bootstrap     container     

## QEMU

The `docker-container` driver supports using [QEMU](https://www.qemu.org/) \(user mode\) to build non-native platforms. Use the `--platform` flag to specify which architectures that you want to build for.

For example, to build a Linux image for `amd64` and `arm64`:               $ docker buildx build \       --builder=container \       --platform=linux/amd64,linux/arm64 \       -t <registry>/<image> \       --push .     

> Note >  > Emulation with QEMU can be much slower than native builds, especially for compute-heavy tasks like compilation and compression or decompression.

## Custom network

You can customize the network that the builder container uses. This is useful if you need to use a specific network for your builds.

For example, let's [create a network](https://docs.docker.com/reference/cli/docker/network/create/) named `foonet`:               $ docker network create foonet     

Now create a [`docker-container` builder](https://docs.docker.com/reference/cli/docker/buildx/create/) that will use this network:               $ docker buildx create --use \       --name mybuilder \       --driver docker-container \       --driver-opt "network=foonet"     

Boot and [inspect `mybuilder`](https://docs.docker.com/reference/cli/docker/buildx/inspect/):               $ docker buildx inspect --bootstrap     

[Inspect the builder container](https://docs.docker.com/reference/cli/docker/inspect/) and see what network is being used:               $ docker inspect buildx_buildkit_mybuilder0 --format={{.NetworkSettings.Networks}}     map[foonet:0xc00018c0c0]     

## Further reading

For more information on the Docker container driver, see the [buildx reference](https://docs.docker.com/reference/cli/docker/buildx/create/#driver).