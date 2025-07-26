# OCI and Docker exporters | Docker Docs

**URL:** https://docs.docker.com/build/exporters/oci-docker/
**Word Count:** 1142
**Links Count:** 653
**Scraped:** 2025-07-16 01:53:49
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# OCI and Docker exporters

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

The `oci` exporter outputs the build result into an [OCI image layout](https://github.com/opencontainers/image-spec/blob/main/image-layout.md) tarball. The `docker` exporter behaves the same way, except it exports a Docker image layout instead.

The [`docker` driver](https://docs.docker.com/build/builders/drivers/docker/) doesn't support these exporters. You must use `docker-container` or some other driver if you want to generate these outputs.

## Synopsis

Build a container image using the `oci` and `docker` exporters:               $ docker buildx build --output type=oci[,parameters] .                    $ docker buildx build --output type=docker[,parameters] .     

The following table describes the available parameters:

Parameter| Type| Default| Description   ---|---|---|---   `name`| String| | Specify image name\(s\)   `dest`| String| | Path   `tar`| `true`,`false`| `true`| Bundle the output into a tarball layout   `compression`| `uncompressed`,`gzip`,`estargz`,`zstd`| `gzip`| Compression type, see [compression](https://docs.docker.com/build/exporters/#compression)   `compression-level`| `0..22`| | Compression level, see [compression](https://docs.docker.com/build/exporters/#compression)   `force-compression`| `true`,`false`| `false`| Forcefully apply compression, see [compression](https://docs.docker.com/build/exporters/#compression)   `oci-mediatypes`| `true`,`false`| | Use OCI media types in exporter manifests. Defaults to `true` for `type=oci`, and `false` for `type=docker`. See [OCI Media types](https://docs.docker.com/build/exporters/#oci-media-types)   `annotation.<key>`| String| | Attach an annotation with the respective `key` and `value` to the built image,see annotations      ## Annotations

These exporters support adding OCI annotation using `annotation` parameter, followed by the annotation name using dot notation. The following example sets the `org.opencontainers.image.title` annotation:               $ docker buildx build \         --output "type=<type>,name=<registry>/<image>,annotation.org.opencontainers.image.title=<title>" .     

For more information about annotations, see [BuildKit documentation](https://github.com/moby/buildkit/blob/master/docs/annotations.md).

## Further reading

For more information on the `oci` or `docker` exporters, see the [BuildKit README](https://github.com/moby/buildkit/blob/master/README.md#docker-tarball).