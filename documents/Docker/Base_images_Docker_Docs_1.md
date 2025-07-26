# Base images | Docker Docs

**URL:** https://docs.docker.com/build/building/base-images/
**Word Count:** 1525
**Links Count:** 658
**Scraped:** 2025-07-16 01:48:52
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Base images

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

All Dockerfiles start from a base image. A base is the image that your image extends. It refers to the contents of the `FROM` instruction in the Dockerfile.               FROM debian

For most cases, you don't need to create your own base image. Docker Hub contains a vast library of Docker images that are suitable for use as a base image in your build. [Docker Official Images](https://docs.docker.com/docker-hub/image-library/trusted-content/#docker-official-images) have clear documentation, promote best practices, and are regularly updated. There are also [Docker Verified Publisher](https://docs.docker.com/docker-hub/image-library/trusted-content/#verified-publisher-images) images, created by trusted publishing partners, verified by Docker.

## Create a base image

If you need to completely control the contents of your image, you can create your own base image from a Linux distribution of your choosing, or use the special `FROM scratch` base:               FROM scratch

The `scratch` image is typically used to create minimal images containing only just what an application needs. See Create a minimal base image using scratch.

To create a distribution base image, you can use a root filesystem, packaged as a `tar` file, and import it to Docker with `docker import`. The process for creating your own base image depends on the Linux distribution you want to package. See Create a full image using tar.

## Create a minimal base image using scratch

The reserved, minimal `scratch` image serves as a starting point for building containers. Using the `scratch` image signals to the build process that you want the next command in the `Dockerfile` to be the first filesystem layer in your image.

While `scratch` appears in Docker's [repository on Docker Hub](https://hub.docker.com/_/scratch), you can't pull it, run it, or tag any image with the name `scratch`. Instead, you can refer to it in your `Dockerfile`. For example, to create a minimal container using `scratch`:               # syntax=docker/dockerfile:1     FROM scratch     ADD hello /     CMD ["/hello"]

Assuming an executable binary named `hello` exists at the root of the [build context](https://docs.docker.com/build/concepts/context/). You can build this Docker image using the following `docker build` command:               $ docker build --tag hello .     

To run your new image, use the `docker run` command:               $ docker run --rm hello     

This example image can only be successfully executed as long as the `hello` binary doesn't have any runtime dependencies. Computer programs tend to depend on certain other programs or resources to exist in the runtime environment. For example:

  * Programming language runtimes   * Dynamically linked C libraries   * CA certificates

When building a base image, or any image, this is an important aspect to consider. And this is why creating a base image using `FROM scratch` can be difficult, for anything other than small, simple programs. On the other hand, it's also important to include only the things you need in your image, to reduce the image size and attack surface.

## Create a full image using tar

In general, start with a working machine that is running the distribution you'd like to package as a base image, though that is not required for some tools like Debian's [Debootstrap](https://wiki.debian.org/Debootstrap), which you can also use to build Ubuntu images.

For example, to create an Ubuntu base image:               $ sudo debootstrap noble noble > /dev/null     $ sudo tar -C noble -c . | docker import - noble          sha256:81ec9a55a92a5618161f68ae691d092bf14d700129093158297b3d01593f4ee3          $ docker run noble cat /etc/lsb-release          DISTRIB_ID=Ubuntu     DISTRIB_RELEASE=24.04     DISTRIB_CODENAME=noble     DISTRIB_DESCRIPTION="Ubuntu 24.04.2 LTS"

There are more example scripts for creating base images in [the Moby GitHub repository](https://github.com/moby/moby/blob/master/contrib).

## More resources

For more information about building images and writing Dockerfiles, see:

  * [Dockerfile reference](https://docs.docker.com/reference/dockerfile/)   * [Dockerfile best practices](https://docs.docker.com/build/building/best-practices/)   * [Docker Official Images](https://docs.docker.com/docker-hub/image-library/trusted-content/#docker-official-images)