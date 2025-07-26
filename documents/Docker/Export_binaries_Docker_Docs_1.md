# Export binaries | Docker Docs

**URL:** https://docs.docker.com/build/building/export/
**Word Count:** 1511
**Links Count:** 649
**Scraped:** 2025-07-16 01:48:31
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Export binaries

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Did you know that you can use Docker to build your application to standalone binaries? Sometimes, you donât want to package and distribute your application as a Docker image. Use Docker to build your application, and use exporters to save the output to disk.

The default output format for `docker build` is a container image. That image is automatically loaded to your local image store, where you can run a container from that image, or push it to a registry. Under the hood, this uses the default exporter, called the `docker` exporter.

To export your build results as files instead, you can use the `--output` flag, or `-o` for short. the `--output` flag lets you change the output format of your build.

## Export binaries from a build

If you specify a filepath to the `docker build --output` flag, Docker exports the contents of the build container at the end of the build to the specified location on your host's filesystem. This uses the `local` [exporter](https://docs.docker.com/build/exporters/local-tar/).

The neat thing about this is that you can use Docker's powerful isolation and build features to create standalone binaries. This works well for Go, Rust, and other languages that can compile to a single binary.

The following example creates a simple Rust program that prints "Hello, World\!", and exports the binary to the host filesystem.

  1. Create a new directory for this example, and navigate to it:                    $ mkdir hello-world-bin          $ cd hello-world-bin          

  2. Create a Dockerfile with the following contents:                    # syntax=docker/dockerfile:1          FROM rust:alpine AS build          WORKDIR /src          COPY <<EOT hello.rs          fn main() {              println!("Hello World!");          }          EOT          RUN rustc -o /bin/hello hello.rs                    FROM scratch          COPY --from=build /bin/hello /          ENTRYPOINT ["/hello"]

> Tip >  > The `COPY <<EOT` syntax is a [here-document](https://docs.docker.com/reference/dockerfile/#here-documents). It lets you write multi-line strings in a Dockerfile. Here it's used to create a simple Rust program inline in the Dockerfile.

This Dockerfile uses a multi-stage build to compile the program in the first stage, and then copies the binary to a scratch image in the second. The final image is a minimal image that only contains the binary. This use case for the `scratch` image is common for creating minimal build artifacts for programs that don't require a full operating system to run.

  3. Build the Dockerfile and export the binary to the current working directory:                    $ docker build --output=. .          

This command builds the Dockerfile and exports the binary to the current working directory. The binary is named `hello`, and it's created in the current working directory.

## Exporting multi-platform builds

You use the `local` exporter to export binaries in combination with [multi-platform builds](https://docs.docker.com/build/building/multi-platform/). This lets you compile multiple binaries at once, that can be run on any machine of any architecture, provided that the target platform is supported by the compiler you use.

Continuing on the example Dockerfile in the Export binaries from a build section:               # syntax=docker/dockerfile:1     FROM rust:alpine AS build     WORKDIR /src     COPY <<EOT hello.rs     fn main() {         println!("Hello World!");     }     EOT     RUN rustc -o /bin/hello hello.rs          FROM scratch     COPY --from=build /bin/hello /     ENTRYPOINT ["/hello"]

You can build this Rust program for multiple platforms using the `--platform` flag with the `docker build` command. In combination with the `--output` flag, the build exports the binaries for each target to the specified directory.

For example, to build the program for both `linux/amd64` and `linux/arm64`:               $ docker build --platform=linux/amd64,linux/arm64 --output=out .     $ tree out/     out/     âââ linux_amd64     âÂ Â  âââ hello     âââ linux_arm64         âââ hello          3 directories, 2 files     

## Additional information

In addition to the `local` exporter, there are other exporters available. To learn more about the available exporters and how to use them, see the [exporters](https://docs.docker.com/build/exporters/) documentation.