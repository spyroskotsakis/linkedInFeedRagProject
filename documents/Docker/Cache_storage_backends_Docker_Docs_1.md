# Cache storage backends | Docker Docs

**URL:** https://docs.docker.com/build/cache/backends/
**Word Count:** 1783
**Links Count:** 670
**Scraped:** 2025-07-16 01:49:59
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Cache storage backends

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

To ensure fast builds, BuildKit automatically caches the build result in its own internal cache. Additionally, BuildKit also supports exporting build cache to an external location, making it possible to import in future builds.

An external cache becomes almost essential in CI/CD build environments. Such environments usually have little-to-no persistence between runs, but it's still important to keep the runtime of image builds as low as possible.

The default `docker` driver supports the `inline`, `local`, `registry`, and `gha` cache backends, but only if you have enabled the [containerd image store](https://docs.docker.com/desktop/features/containerd/). Other cache backends require you to select a different [driver](https://docs.docker.com/build/builders/drivers/).

> Warning >  > If you use secrets or credentials inside your build process, ensure you manipulate them using the dedicated [`--secret` option](https://docs.docker.com/reference/cli/docker/buildx/build/#secret). Manually managing secrets using `COPY` or `ARG` could result in leaked credentials.

## Backends

Buildx supports the following cache storage backends:

  * `inline`: embeds the build cache into the image.

The inline cache gets pushed to the same location as the main output result. This only works with the [`image` exporter](https://docs.docker.com/build/exporters/image-registry/).

  * `registry`: embeds the build cache into a separate image, and pushes to a dedicated location separate from the main output.

  * `local`: writes the build cache to a local directory on the filesystem.

  * `gha`: uploads the build cache to [GitHub Actions cache](https://docs.github.com/en/rest/actions/cache) \(beta\).

  * `s3`: uploads the build cache to an [AWS S3 bucket](https://aws.amazon.com/s3/) \(unreleased\).

  * `azblob`: uploads the build cache to [Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/) \(unreleased\).

## Command syntax

To use any of the cache backends, you first need to specify it on build with the [`--cache-to` option](https://docs.docker.com/reference/cli/docker/buildx/build/#cache-to) to export the cache to your storage backend of choice. Then, use the [`--cache-from` option](https://docs.docker.com/reference/cli/docker/buildx/build/#cache-from) to import the cache from the storage backend into the current build. Unlike the local BuildKit cache \(which is always enabled\), all of the cache storage backends must be explicitly exported to, and explicitly imported from.

Example `buildx` command using the `registry` backend, using import and export cache:               $ docker buildx build --push -t <registry>/<image> \       --cache-to type=registry,ref=<registry>/<cache-image>[,parameters...] \       --cache-from type=registry,ref=<registry>/<cache-image>[,parameters...] .     

> Warning >  > As a general rule, each cache writes to some location. No location can be written to twice, without overwriting the previously cached data. If you want to maintain multiple scoped caches \(for example, a cache per Git branch\), then ensure that you use different locations for exported cache.

## Multiple caches

BuildKit supports multiple cache exporters, allowing you to push cache to more than one destination. You can also import from as many remote caches as you'd like. For example, a common pattern is to use the cache of both the current branch and the main branch. The following example shows importing cache from multiple locations using the registry cache backend:               $ docker buildx build --push -t <registry>/<image> \       --cache-to type=registry,ref=<registry>/<cache-image>:<branch> \       --cache-from type=registry,ref=<registry>/<cache-image>:<branch> \       --cache-from type=registry,ref=<registry>/<cache-image>:main .     

## Configuration options

This section describes some configuration options available when generating cache exports. The options described here are common for at least two or more backend types. Additionally, the different backend types support specific parameters as well. See the detailed page about each backend type for more information about which configuration parameters apply.

The common parameters described here are:

  * Cache mode   * Cache compression   * OCI media type

### Cache mode

When generating a cache output, the `--cache-to` argument accepts a `mode` option for defining which layers to include in the exported cache. This is supported by all cache backends except for the `inline` cache.

Mode can be set to either of two options: `mode=min` or `mode=max`. For example, to build the cache with `mode=max` with the registry backend:               $ docker buildx build --push -t <registry>/<image> \       --cache-to type=registry,ref=<registry>/<cache-image>,mode=max \       --cache-from type=registry,ref=<registry>/<cache-image> .     

This option is only set when exporting a cache, using `--cache-to`. When importing a cache \(`--cache-from`\) the relevant parameters are automatically detected.

In `min` cache mode \(the default\), only layers that are exported into the resulting image are cached, while in `max` cache mode, all layers are cached, even those of intermediate steps.

While `min` cache is typically smaller \(which speeds up import/export times, and reduces storage costs\), `max` cache is more likely to get more cache hits. Depending on the complexity and location of your build, you should experiment with both parameters to find the results that work best for you.

### Cache compression

The cache compression options are the same as the [exporter compression options](https://docs.docker.com/build/exporters/#compression). This is supported by the `local` and `registry` cache backends.

For example, to compress the `registry` cache with `zstd` compression:               $ docker buildx build --push -t <registry>/<image> \       --cache-to type=registry,ref=<registry>/<cache-image>,compression=zstd \       --cache-from type=registry,ref=<registry>/<cache-image> .     

### OCI media types

The cache OCI options are the same as the [exporter OCI options](https://docs.docker.com/build/exporters/#oci-media-types). These are supported by the `local` and `registry` cache backends.

For example, to export OCI media type cache, use the `oci-mediatypes` property:               $ docker buildx build --push -t <registry>/<image> \       --cache-to type=registry,ref=<registry>/<cache-image>,oci-mediatypes=true \       --cache-from type=registry,ref=<registry>/<cache-image> .     

This property is only meaningful with the `--cache-to` flag. When fetching cache, BuildKit will auto-detect the correct media types to use.

By default, the OCI media type generates an image index for the cache image. Some OCI registries, such as Amazon ECR, don't support the image index media type: `application/vnd.oci.image.index.v1+json`. If you export cache images to ECR, or any other registry that doesn't support image indices, set the `image-manifest` parameter to `true` to generate a single image manifest instead of an image index for the cache image:               $ docker buildx build --push -t <registry>/<image> \       --cache-to type=registry,ref=<registry>/<cache-image>,oci-mediatypes=true,image-manifest=true \       --cache-from type=registry,ref=<registry>/<cache-image> .     

> Note >  > Since BuildKit v0.21, `image-manifest` is enabled by default.