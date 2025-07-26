# Amazon S3 cache | Docker Docs

**URL:** https://docs.docker.com/build/cache/backends/s3
**Word Count:** 1196
**Links Count:** 655
**Scraped:** 2025-07-16 02:03:17
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Amazon S3 cache

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Availability: Experimental 

The `s3` cache storage uploads your resulting build cache to [Amazon S3 file storage service](https://aws.amazon.com/s3/) or other S3-compatible services, such as [MinIO](https://min.io/).

This cache storage backend is not supported with the default `docker` driver. To use this feature, create a new builder using a different driver. See [Build drivers](https://docs.docker.com/build/builders/drivers/) for more information.

## Synopsis               $ docker buildx build --push -t <user>/<image> \       --cache-to type=s3,region=<region>,bucket=<bucket>,name=<cache-image>[,parameters...] \       --cache-from type=s3,region=<region>,bucket=<bucket>,name=<cache-image> .     

The following table describes the available CSV parameters that you can pass to `--cache-to` and `--cache-from`.

Name| Option| Type| Default| Description   ---|---|---|---|---   `region`| `cache-to`,`cache-from`| String| | Required. Geographic location.   `bucket`| `cache-to`,`cache-from`| String| | Required. Name of the S3 bucket.   `name`| `cache-to`,`cache-from`| String| | Name of the cache image.   `endpoint_url`| `cache-to`,`cache-from`| String| | Endpoint of the S3 bucket.   `blobs_prefix`| `cache-to`,`cache-from`| String| | Prefix to prepend to blob filenames.   `upload_parallelism`| `cache-to`| Integer| `4`| Number of parallel layer uploads.   `touch_refresh`| `cache-to`| Time| `24h`| Interval for updating the timestamp of unchanged cache layers.   `manifests_prefix`| `cache-to`,`cache-from`| String| | Prefix to prepend on manifest filenames.   `use_path_style`| `cache-to`,`cache-from`| Boolean| `false`| When `true`, uses `bucket` in the URL instead of hostname.   `access_key_id`| `cache-to`,`cache-from`| String| | See authentication.   `secret_access_key`| `cache-to`,`cache-from`| String| | See authentication.   `session_token`| `cache-to`,`cache-from`| String| | See authentication.   `mode`| `cache-to`| `min`,`max`| `min`| Cache layers to export, see [cache mode](https://docs.docker.com/build/cache/backends/#cache-mode).   `ignore-error`| `cache-to`| Boolean| `false`| Ignore errors caused by failed cache exports.      ## Authentication

Buildx can reuse existing AWS credentials, configured either using a credentials file or environment variables, for pushing and pulling cache to S3. Alternatively, you can use the `access_key_id`, `secret_access_key`, and `session_token` attributes to specify credentials directly on the CLI.

Refer to [AWS Go SDK, Specifying Credentials](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/configuring-sdk.html#specifying-credentials) for details about authentication using environment variables and credentials file.

## Further reading

For an introduction to caching see [Docker build cache](https://docs.docker.com/build/cache/).

For more information on the `s3` cache backend, see the [BuildKit README](https://github.com/moby/buildkit#s3-cache-experimental).