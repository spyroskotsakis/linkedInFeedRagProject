# docker buildx build | Docker Docs

**URL:** https://docs.docker.com/engine/reference/commandline/image_build
**Word Count:** 4542
**Links Count:** 670
**Scraped:** 2025-07-16 02:04:08
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker buildx build

Description| Start a build   ---|---   Usage| `docker buildx build [OPTIONS] PATH | URL | -`   AliasesAn alias is a short or memorable alternative for a longer command.| `docker build` `docker builder build` `docker image build` `docker buildx b`      ## Description

The `docker buildx build` command starts a build using BuildKit.

## Options

Option| Default| Description   ---|---|---   `--add-host`| | Add a custom host-to-IP mapping \(format: `host:ip`\)   `--allow`| | Allow extra privileged entitlement \(e.g., `network.host`, `security.insecure`\)      `--annotation`| | Add annotation to the image   `--attest`| | Attestation parameters \(format: `type=sbom,generator=image`\)   `--build-arg`| | Set build-time variables   `--build-context`| | Additional build contexts \(e.g., name=path\)   `--cache-from`| | External cache sources \(e.g., `user/app:cache`, `type=local,src=path/to/dir`\)      `--cache-to`| | Cache export destinations \(e.g., `user/app:cache`, `type=local,dest=path/to/dir`\)      `--call`| `build`| Set method for evaluating build \(`check`, `outline`, `targets`\)   `--cgroup-parent`| | Set the parent cgroup for the `RUN` instructions during build   `--check`| | Shorthand for `--call=check`   `-f, --file`| | Name of the Dockerfile \(default: `PATH/Dockerfile`\)   `--iidfile`| | Write the image ID to a file   `--label`| | Set metadata for an image   `--load`| | Shorthand for `--output=type=docker`   `--metadata-file`| | Write build result metadata to a file   `--network`| | Set the networking mode for the `RUN` instructions during build   `--no-cache`| | Do not use cache when building the image   `--no-cache-filter`| | Do not cache specified stages   `-o, --output`| | Output destination \(format: `type=local,dest=path`\)   `--platform`| | Set target platform for build   `--progress`| `auto`| Set type of progress output \(`auto`, `quiet`, `plain`, `tty`, `rawjson`\). Use plain to show container output      `--provenance`| | Shorthand for `--attest=type=provenance`   `--pull`| | Always attempt to pull all referenced images   `--push`| | Shorthand for `--output=type=registry`   `-q, --quiet`| | Suppress the build output and print image ID on success   `--sbom`| | Shorthand for `--attest=type=sbom`   `--secret`| | Secret to expose to the build \(format: `id=mysecret[,src=/local/secret]`\)      `--shm-size`| | Shared memory size for build containers   `--ssh`| | SSH agent socket or keys to expose to the build \(format: `default|<id>[=<socket>|<key>[,<key>]]`\)      `-t, --tag`| | Name and optionally a tag \(format: `name:tag`\)   `--target`| | Set the target build stage to build   `--ulimit`| | Ulimit options      ## Examples

### Add entries to container hosts file \(--add-host\)

You can add other hosts into a build container's `/etc/hosts` file by using one or more `--add-host` flags. This example adds static addresses for hosts named `my-hostname` and `my_hostname_v6`:               $ docker buildx build --add-host my_hostname=8.8.8.8 --add-host my_hostname_v6=2001:4860:4860::8888 .     

If you need your build to connect to services running on the host, you can use the special `host-gateway` value for `--add-host`. In the following example, build containers resolve `host.docker.internal` to the host's gateway IP.               $ docker buildx build --add-host host.docker.internal=host-gateway .     

You can wrap an IPv6 address in square brackets. `=` and `:` are both valid separators. Both formats in the following example are valid:               $ docker buildx build --add-host my-hostname:10.180.0.1 --add-host my-hostname_v6=[2001:4860:4860::8888] .     

### Create annotations \(--annotation\)               --annotation="key=value"     --annotation="[type:]key=value"

Add OCI annotations to the image index, manifest, or descriptor. The following example adds the `foo=bar` annotation to the image manifests:               $ docker buildx build -t TAG --annotation "foo=bar" --push .     

You can optionally add a type prefix to specify the level of the annotation. By default, the image manifest is annotated. The following example adds the `foo=bar` annotation the image index instead of the manifests:               $ docker buildx build -t TAG --annotation "index:foo=bar" --push .     

You can specify multiple types, separated by a comma \(,\) to add the annotation to multiple image components. The following example adds the `foo=bar` annotation to image index, descriptors, manifests:               $ docker buildx build -t TAG --annotation "index,manifest,manifest-descriptor:foo=bar" --push .     

You can also specify a platform qualifier in square brackets \(`[os/arch]`\) in the type prefix, to apply the annotation to a subset of manifests with the matching platform. The following example adds the `foo=bar` annotation only to the manifest with the `linux/amd64` platform:               $ docker buildx build -t TAG --annotation "manifest[linux/amd64]:foo=bar" --push .     

Wildcards are not supported in the platform qualifier; you can't specify a type prefix like `manifest[linux/*]` to add annotations only to manifests which has `linux` as the OS platform.

For more information about annotations, see [Annotations](https://docs.docker.com/build/building/annotations/).

### Create attestations \(--attest\)               --attest=type=sbom,...     --attest=type=provenance,...

Create [image attestations](https://docs.docker.com/build/metadata/attestations/). BuildKit currently supports:

  * `sbom` \- Software Bill of Materials.

Use `--attest=type=sbom` to generate an SBOM for an image at build-time. Alternatively, you can use the `--sbom` shorthand.

For more information, see [here](https://docs.docker.com/build/metadata/attestations/sbom/).

  * `provenance` \- SLSA Provenance

Use `--attest=type=provenance` to generate provenance for an image at build-time. Alternatively, you can use the `--provenance` shorthand.

By default, a minimal provenance attestation will be created for the build result, which will only be attached for images pushed to registries.

For more information, see [here](https://docs.docker.com/build/metadata/attestations/slsa-provenance/).

### Allow extra privileged entitlement \(--allow\)               --allow=ENTITLEMENT

Allow extra privileged entitlement. List of entitlements:

  * `network.host` \- Allows executions with host networking.   * `security.insecure` \- Allows executions without sandbox. See [related Dockerfile extensions](https://docs.docker.com/reference/dockerfile/#run---security).

For entitlements to be enabled, the BuildKit daemon also needs to allow them with `--allow-insecure-entitlement` \(see [`create --buildkitd-flags`](https://docs.docker.com/reference/cli/docker/buildx/create/#buildkitd-flags)\).               $ docker buildx create --use --name insecure-builder --buildkitd-flags '--allow-insecure-entitlement security.insecure'     $ docker buildx build --allow security.insecure .     

### Set build-time variables \(--build-arg\)

You can use `ENV` instructions in a Dockerfile to define variable values. These values persist in the built image. Often persistence isn't what you want. Users want to specify variables differently depending on which host they build an image on.

A good example is `http_proxy` or source versions for pulling intermediate files. The `ARG` instruction lets Dockerfile authors define values that users can set at build-time using the `--build-arg` flag:               $ docker buildx build --build-arg HTTP_PROXY=http://10.20.30.2:1234 --build-arg FTP_PROXY=http://40.50.60.5:4567 .     

This flag allows you to pass the build-time variables that are accessed like regular environment variables in the `RUN` instruction of the Dockerfile. These values don't persist in the intermediate or final images like `ENV` values do. You must add `--build-arg` for each build argument.

Using this flag doesn't alter the output you see when the build process echoes the`ARG` lines from the Dockerfile.

For detailed information on using `ARG` and `ENV` instructions, see the [Dockerfile reference](https://docs.docker.com/reference/dockerfile/).

You can also use the `--build-arg` flag without a value, in which case the daemon propagates the value from the local environment into the Docker container it's building:               $ export HTTP_PROXY=http://10.20.30.2:1234     $ docker buildx build --build-arg HTTP_PROXY .     

This example is similar to how `docker run -e` works. Refer to the [`docker run` documentation](https://docs.docker.com/reference/cli/docker/container/run/#env) for more information.

There are also useful built-in build arguments, such as:

  * `BUILDKIT_CONTEXT_KEEP_GIT_DIR=<bool>`: trigger git context to keep the `.git` directory   * `BUILDKIT_INLINE_CACHE=<bool>`: inline cache metadata to image config or not   * `BUILDKIT_MULTI_PLATFORM=<bool>`: opt into deterministic output regardless of multi-platform output or not

              $ docker buildx build --build-arg BUILDKIT_MULTI_PLATFORM=1 .     

Learn more about the built-in build arguments in the [Dockerfile reference docs](https://docs.docker.com/reference/dockerfile/#buildkit-built-in-build-args).

### Additional build contexts \(--build-context\)               --build-context=name=VALUE

Define additional build context with specified contents. In Dockerfile the context can be accessed when `FROM name` or `--from=name` is used. When Dockerfile defines a stage with the same name it is overwritten.

The value can be a local source directory, [local OCI layout compliant directory](https://github.com/opencontainers/image-spec/blob/main/image-layout.md), container image \(with docker-image:// prefix\), Git or HTTP URL.

Replace `alpine:latest` with a pinned one:               $ docker buildx build --build-context alpine=docker-image://alpine@sha256:0123456789 .     

Expose a secondary local source directory:               $ docker buildx build --build-context project=path/to/project/source .     # docker buildx build --build-context project=https://github.com/myuser/project.git .                    # syntax=docker/dockerfile:1     FROM alpine     COPY --from=project myfile /

#### Use an OCI layout directory as build context

Source an image from a local [OCI layout compliant directory](https://github.com/opencontainers/image-spec/blob/main/image-layout.md), either by tag, or by digest:               $ docker buildx build --build-context foo=oci-layout:///path/to/local/layout:<tag>     $ docker buildx build --build-context foo=oci-layout:///path/to/local/layout@sha256:<digest>                    # syntax=docker/dockerfile:1     FROM alpine     RUN apk add git     COPY --from=foo myfile /          FROM foo

The OCI layout directory must be compliant with the [OCI layout specification](https://github.com/opencontainers/image-spec/blob/main/image-layout.md). You can reference an image in the layout using either tags, or the exact digest.

### Override the configured builder instance \(--builder\)

Same as [`buildx --builder`](https://docs.docker.com/reference/cli/docker/buildx/#builder).

### Use an external cache source for a build \(--cache-from\)               --cache-from=[NAME|type=TYPE[,KEY=VALUE]]

Use an external cache source for a build. Supported types are `registry`, `local`, `gha` and `s3`.

  * [`registry` source](https://github.com/moby/buildkit#registry-push-image-and-cache-separately) can import cache from a cache manifest or \(special\) image configuration on the registry.   * [`local` source](https://github.com/moby/buildkit#local-directory-1) can import cache from local files previously exported with `--cache-to`.   * [`gha` source](https://github.com/moby/buildkit#github-actions-cache-experimental) can import cache from a previously exported cache with `--cache-to` in your GitHub repository   * [`s3` source](https://github.com/moby/buildkit#s3-cache-experimental) can import cache from a previously exported cache with `--cache-to` in your S3 bucket

If no type is specified, `registry` exporter is used with a specified reference.

`docker` driver currently only supports importing build cache from the registry.               $ docker buildx build --cache-from=user/app:cache .     $ docker buildx build --cache-from=user/app .     $ docker buildx build --cache-from=type=registry,ref=user/app .     $ docker buildx build --cache-from=type=local,src=path/to/cache .     $ docker buildx build --cache-from=type=gha .     $ docker buildx build --cache-from=type=s3,region=eu-west-1,bucket=mybucket .     

More info about cache exporters and available attributes: <https://github.com/moby/buildkit#export-cache>

### Invoke a frontend method \(--call\)               --call=[build|check|outline|targets]

BuildKit frontends can support alternative modes of executions for builds, using frontend methods. Frontend methods are a way to change or extend the behavior of a build invocation, which lets you, for example, inspect, validate, or generate alternative outputs from a build.

The `--call` flag for `docker buildx build` lets you specify the frontend method that you want to execute. If this flag is unspecified, it defaults to executing the build and evaluating [build checks](https://docs.docker.com/reference/build-checks/).

For Dockerfiles, the available methods are:

Command| Description   ---|---   `build` \(default\)| Execute the build and evaluate build checks for the current build target.   `check`| Evaluate build checks for the either the entire Dockerfile or the selected target, without executing a build.   `outline`| Show the build arguments that you can set for a target, and their default values.   `targets`| List all the build targets in the Dockerfile.   `subrequests.describe`| List all the frontend methods that the current frontend supports.      Note that other frontends may implement these or other methods. To see the list of available methods for the frontend you're using, use `--call=subrequests.describe`.               $ docker buildx build -q --call=subrequests.describe .          NAME                 VERSION DESCRIPTION     outline              1.0.0   List all parameters current build target supports     targets              1.0.0   List all targets current build supports     subrequests.describe 1.0.0   List available subrequest types     

#### Descriptions

The `--call=targets` and `--call=outline` methods include descriptions for build targets and arguments, if available. Descriptions are generated from comments in the Dockerfile. A comment on the line before a `FROM` instruction becomes the description of a build target, and a comment before an `ARG` instruction the description of a build argument. The comment must lead with the name of the stage or argument, for example:               # syntax=docker/dockerfile:1          # GO_VERSION sets the Go version for the build     ARG GO_VERSION=1.22          # base-builder is the base stage for building the project     FROM golang:${GO_VERSION} AS base-builder

When you run `docker buildx build --call=outline`, the output includes the descriptions, as follows:               $ docker buildx build -q --call=outline .          TARGET:      base-builder     DESCRIPTION: is the base stage for building the project          BUILD ARG    VALUE   DESCRIPTION     GO_VERSION   1.22    sets the Go version for the build     

For more examples on how to write Dockerfile docstrings, check out [the Dockerfile for Docker docs](https://github.com/docker/docs/blob/main/Dockerfile).

#### Call: check \(--check\)

The `check` method evaluates build checks without executing the build. The `--check` flag is a convenient shorthand for `--call=check`. Use the `check` method to validate the build configuration before starting the build.               $ docker buildx build -q --check https://github.com/docker/docs.git          WARNING: InvalidBaseImagePlatform     Base image wjdp/htmltest:v0.17.0 was pulled with platform "linux/amd64", expected "linux/arm64" for current build     Dockerfile:43     --------------------       41 |         "#content/desktop/previous-versions/*.md"       42 |       43 | >>> FROM wjdp/htmltest:v${HTMLTEST_VERSION} AS test       44 |     WORKDIR /test       45 |     COPY --from=build /out ./public     --------------------     

Using `--check` without specifying a target evaluates the entire Dockerfile. If you want to evaluate a specific target, use the `--target` flag.

#### Call: outline

The `outline` method prints the name of the specified target \(or the default target, if `--target` isn't specified\), and the build arguments that the target consumes, along with their default values, if set.

The following example shows the default target `release` and its build arguments:               $ docker buildx build -q --call=outline https://github.com/docker/docs.git          TARGET:      release     DESCRIPTION: is an empty scratch image with only compiled assets          BUILD ARG          VALUE     DESCRIPTION     GO_VERSION         1.22      sets the Go version for the base stage     HUGO_VERSION       0.127.0     HUGO_ENV                     sets the hugo.Environment (production, development, preview)     DOCS_URL                     sets the base URL for the site     PAGEFIND_VERSION   1.1.0     

This means that the `release` target is configurable using these build arguments:               $ docker buildx build \       --build-arg GO_VERSION=1.22 \       --build-arg HUGO_VERSION=0.127.0 \       --build-arg HUGO_ENV=production \       --build-arg DOCS_URL=https://example.com \       --build-arg PAGEFIND_VERSION=1.1.0 \       --target release https://github.com/docker/docs.git     

#### Call: targets

The `targets` method lists all the build targets in the Dockerfile. These are the stages that you can build using the `--target` flag. It also indicates the default target, which is the target that will be built when you don't specify a target.               $ docker buildx build -q --call=targets https://github.com/docker/docs.git          TARGET            DESCRIPTION     base              is the base stage with build dependencies     node              installs Node.js dependencies     hugo              downloads and extracts the Hugo binary     build-base        is the base stage for building the site     dev               is for local development with Docker Compose     build             creates production builds with Hugo     lint              lints markdown files     test              validates HTML output and checks for broken links     update-modules    downloads and vendors Hugo modules     vendor            is an empty stage with only vendored Hugo modules     build-upstream    builds an upstream project with a replacement module     validate-upstream validates HTML output for upstream builds     unused-media      checks for unused graphics and other media     pagefind          installs the Pagefind runtime     index             generates a Pagefind index     test-go-redirects checks that the /go/ redirects are valid     release (default) is an empty scratch image with only compiled assets     

### Export build cache to an external cache destination \(--cache-to\)               --cache-to=[NAME|type=TYPE[,KEY=VALUE]]

Export build cache to an external cache destination. Supported types are `registry`, `local`, `inline`, `gha` and `s3`.

  * [`registry` type](https://github.com/moby/buildkit#registry-push-image-and-cache-separately) exports build cache to a cache manifest in the registry.   * [`local` type](https://github.com/moby/buildkit#local-directory-1) exports cache to a local directory on the client.   * [`inline` type](https://github.com/moby/buildkit#inline-push-image-and-cache-together) writes the cache metadata into the image configuration.   * [`gha` type](https://github.com/moby/buildkit#github-actions-cache-experimental) exports cache through the [GitHub Actions Cache service API](https://github.com/tonistiigi/go-actions-cache/blob/master/api.md#authentication).   * [`s3` type](https://github.com/moby/buildkit#s3-cache-experimental) exports cache to a S3 bucket.

The `docker` driver only supports cache exports using the `inline` and `local` cache backends.

Attribute key:

  * `mode` \- Specifies how many layers are exported with the cache. `min` on only exports layers already in the final build stage, `max` exports layers for all stages. Metadata is always exported for the whole build.

              $ docker buildx build --cache-to=user/app:cache .     $ docker buildx build --cache-to=type=inline .     $ docker buildx build --cache-to=type=registry,ref=user/app .     $ docker buildx build --cache-to=type=local,dest=path/to/cache .     $ docker buildx build --cache-to=type=gha .     $ docker buildx build --cache-to=type=s3,region=eu-west-1,bucket=mybucket .     

More info about cache exporters and available attributes: <https://github.com/moby/buildkit#export-cache>

### Use a custom parent cgroup \(--cgroup-parent\)

When you run `docker buildx build` with the `--cgroup-parent` option, the daemon runs the containers used in the build with the [corresponding `docker run` flag](https://docs.docker.com/reference/cli/docker/container/run/#cgroup-parent).

### Specify a Dockerfile \(-f, --file\)               $ docker buildx build -f <filepath> .     

Specifies the filepath of the Dockerfile to use. If unspecified, a file named `Dockerfile` at the root of the build context is used by default.

To read a Dockerfile from stdin, you can use `-` as the argument for `--file`.               $ cat Dockerfile | docker buildx build -f - .     

### Load the single-platform build result to `docker images` \(--load\)

Shorthand for `--output=type=docker`. Will automatically load the single-platform build result to `docker images`.

### Write build result metadata to a file \(--metadata-file\)

To output build metadata such as the image digest, pass the `--metadata-file` flag. The metadata will be written as a JSON object to the specified file. The directory of the specified file must already exist and be writable.               $ docker buildx build --load --metadata-file metadata.json .     $ cat metadata.json                    {       "buildx.build.provenance": {},       "buildx.build.ref": "mybuilder/mybuilder0/0fjb6ubs52xx3vygf6fgdl611",       "buildx.build.warnings": {},       "containerimage.config.digest": "sha256:2937f66a9722f7f4a2df583de2f8cb97fc9196059a410e7f00072fc918930e66",       "containerimage.descriptor": {         "annotations": {           "config.digest": "sha256:2937f66a9722f7f4a2df583de2f8cb97fc9196059a410e7f00072fc918930e66",           "org.opencontainers.image.created": "2022-02-08T21:28:03Z"         },         "digest": "sha256:19ffeab6f8bc9293ac2c3fdf94ebe28396254c993aea0b5a542cfb02e0883fa3",         "mediaType": "application/vnd.oci.image.manifest.v1+json",         "size": 506       },       "containerimage.digest": "sha256:19ffeab6f8bc9293ac2c3fdf94ebe28396254c993aea0b5a542cfb02e0883fa3"     }

> Note >  > Build record [provenance](https://docs.docker.com/build/metadata/attestations/slsa-provenance/#provenance-attestation-example) \(`buildx.build.provenance`\) includes minimal provenance by default. Set the `BUILDX_METADATA_PROVENANCE` environment variable to customize this behavior: >  >   * `min` sets minimal provenance \(default\). >   * `max` sets full provenance. >   * `disabled`, `false` or `0` doesn't set any provenance. > 

> Note >  > Build warnings \(`buildx.build.warnings`\) are not included by default. Set the `BUILDX_METADATA_WARNINGS` environment variable to `1` or `true` to include them.

### Set the networking mode for the RUN instructions during build \(--network\)

Available options for the networking mode are:

  * `default` \(default\): Run in the default network.   * `none`: Run with no network access.   * `host`: Run in the hostâs network environment.

Find more details in the [Dockerfile reference](https://docs.docker.com/reference/dockerfile/#run---network).

### Ignore build cache for specific stages \(--no-cache-filter\)

The `--no-cache-filter` lets you specify one or more stages of a multi-stage Dockerfile for which build cache should be ignored. To specify multiple stages, use a comma-separated syntax:               $ docker buildx build --no-cache-filter stage1,stage2,stage3 .     

For example, the following Dockerfile contains four stages:

  * `base`   * `install`   * `test`   * `release`

              # syntax=docker/dockerfile:1          FROM oven/bun:1 AS base     WORKDIR /app          FROM base AS install     WORKDIR /temp/dev     RUN --mount=type=bind,source=package.json,target=package.json \         --mount=type=bind,source=bun.lockb,target=bun.lockb \         bun install --frozen-lockfile          FROM base AS test     COPY --from=install /temp/dev/node_modules node_modules     COPY . .     RUN bun test          FROM base AS release     ENV NODE_ENV=production     COPY --from=install /temp/dev/node_modules node_modules     COPY . .     ENTRYPOINT ["bun", "run", "index.js"]

To ignore the cache for the `install` stage:               $ docker buildx build --no-cache-filter install .     

To ignore the cache the `install` and `release` stages:               $ docker buildx build --no-cache-filter install,release .     

The arguments for the `--no-cache-filter` flag must be names of stages.

### Set the export action for the build result \(-o, --output\)               -o, --output=[PATH,-,type=TYPE[,KEY=VALUE]

Sets the export action for the build result. The default output, when using the `docker` [build driver](https://docs.docker.com/build/builders/drivers/), is a container image exported to the local image store. The `--output` flag makes this step configurable allows export of results directly to the client's filesystem, an OCI image tarball, a registry, and more.

Buildx with `docker` driver only supports the local, tarball, and image [exporters](https://docs.docker.com/build/exporters/). The `docker-container` driver supports all exporters.

If you only specify a filepath as the argument to `--output`, Buildx uses the local exporter. If the value is `-`, Buildx uses the `tar` exporter and writes the output to stdout.               $ docker buildx build -o . .     $ docker buildx build -o outdir .     $ docker buildx build -o - . > out.tar     $ docker buildx build -o type=docker .     $ docker buildx build -o type=docker,dest=- . > myimage.tar     $ docker buildx build -t tonistiigi/foo -o type=registry     

You can export multiple outputs by repeating the flag.

Supported exported types are:

  * `local`   * `tar`   * `oci`   * `docker`   * `image`   * `registry`

#### `local`

The `local` export type writes all result files to a directory on the client. The new files will be owned by the current user. On multi-platform builds, all results will be put in subdirectories by their platform.

Attribute key:

  * `dest` \- destination directory where files will be written

For more information, see [Local and tar exporters](https://docs.docker.com/build/exporters/local-tar/).

#### `tar`

The `tar` export type writes all result files as a single tarball on the client. On multi-platform builds all results will be put in subdirectories by their platform.

Attribute key:

  * `dest` \- destination path where tarball will be written. â-â writes to stdout.

For more information, see [Local and tar exporters](https://docs.docker.com/build/exporters/local-tar/).

#### `oci`

The `oci` export type writes the result image or manifest list as an [OCI image layout](https://github.com/opencontainers/image-spec/blob/v1.0.1/image-layout.md) tarball on the client.

Attribute key:

  * `dest` \- destination path where tarball will be written. â-â writes to stdout.

For more information, see [OCI and Docker exporters](https://docs.docker.com/build/exporters/oci-docker/).

#### `docker`

The `docker` export type writes the single-platform result image as a [Docker image specification](https://github.com/docker/docker/blob/v20.10.2/image/spec/v1.2.md) tarball on the client. Tarballs created by this exporter are also OCI compatible.

The default image store in Docker Engine doesn't support loading multi-platform images. You can enable the containerd image store, or push multi-platform images is to directly push to a registry, see `registry`.

Attribute keys:

  * `dest` \- destination path where tarball will be written. If not specified, the tar will be loaded automatically to the local image store.   * `context` \- name for the Docker context where to import the result

For more information, see [OCI and Docker exporters](https://docs.docker.com/build/exporters/oci-docker/).

#### `image`

The `image` exporter writes the build result as an image or a manifest list. When using `docker` driver the image will appear in `docker images`. Optionally, image can be automatically pushed to a registry by specifying attributes.

Attribute keys:

  * `name` \- name \(references\) for the new image.   * `push` \- Boolean to automatically push the image.

For more information, see [Image and registry exporters](https://docs.docker.com/build/exporters/image-registry/).

#### `registry`

The `registry` exporter is a shortcut for `type=image,push=true`.

For more information, see [Image and registry exporters](https://docs.docker.com/build/exporters/image-registry/).

### Set the target platforms for the build \(--platform\)               --platform=value[,value]

Set the target platform for the build. All `FROM` commands inside the Dockerfile without their own `--platform` flag will pull base images for this platform and this value will also be the platform of the resulting image.

The default value is the platform of the BuildKit daemon where the build runs. The value takes the form of `os/arch` or `os/arch/variant`. For example, `linux/amd64` or `linux/arm/v7`. Additionally, the `--platform` flag also supports a special `local` value, which tells BuildKit to use the platform of the BuildKit client that invokes the build.

When using `docker-container` driver with `buildx`, this flag can accept multiple values as an input separated by a comma. With multiple values the result will be built for all of the specified platforms and joined together into a single manifest list.

If the `Dockerfile` needs to invoke the `RUN` command, the builder needs runtime support for the specified platform. In a clean setup, you can only execute `RUN` commands for your system architecture. If your kernel supports [`binfmt_misc`](https://en.wikipedia.org/wiki/Binfmt_misc) launchers for secondary architectures, buildx will pick them up automatically. Docker Desktop releases come with `binfmt_misc` automatically configured for `arm64` and `arm` architectures. You can see what runtime platforms your current builder instance supports by running `docker buildx inspect --bootstrap`.

Inside a `Dockerfile`, you can access the current platform value through `TARGETPLATFORM` build argument. Refer to the [Dockerfile reference](https://docs.docker.com/reference/dockerfile/#automatic-platform-args-in-the-global-scope) for the full description of automatic platform argument variants .

You can find the formatting definition for the platform specifier in the [containerd source code](https://github.com/containerd/containerd/blob/v1.4.3/platforms/platforms.go#L63).               $ docker buildx build --platform=linux/arm64 .     $ docker buildx build --platform=linux/amd64,linux/arm64,linux/arm/v7 .     $ docker buildx build --platform=darwin .     

### Set type of progress output \(--progress\)               --progress=VALUE

Set type of progress output. Supported values are:

  * `auto` \(default\): Uses the `tty` mode if the client is a TTY, or `plain` otherwise   * `tty`: An interactive stream of the output with color and redrawing   * `plain`: Prints the raw build progress in a plaintext format   * `quiet`: Suppress the build output and print image ID on success \(same as `--quiet`\)   * `rawjson`: Prints the raw build progress as JSON lines

> Note >  > You can also use the `BUILDKIT_PROGRESS` environment variable to set its value.

The following example uses `plain` output during the build:               $ docker buildx build --load --progress=plain .          #1 [internal] load build definition from Dockerfile     #1 transferring dockerfile: 227B 0.0s done     #1 DONE 0.1s          #2 [internal] load .dockerignore     #2 transferring context: 129B 0.0s done     #2 DONE 0.0s     ...     

> Note >  > Check also the [`BUILDKIT_COLORS`](https://docs.docker.com/build/building/variables/#buildkit_colors) environment variable for modifying the colors of the terminal output.

The `rawjson` output marshals the solve status events from BuildKit to JSON lines. This mode is designed to be read by an external program.

### Create provenance attestations \(--provenance\)

Shorthand for `--attest=type=provenance`, used to configure provenance attestations for the build result. For example, `--provenance=mode=max` can be used as an abbreviation for `--attest=type=provenance,mode=max`.

Additionally, `--provenance` can be used with Boolean values to enable or disable provenance attestations. For example, `--provenance=false` disables all provenance attestations, while `--provenance=true` enables all provenance attestations.

By default, a minimal provenance attestation will be created for the build result. Note that the default image store in Docker Engine doesn't support attestations. Provenance attestations only persist for images pushed directly to a registry if you use the default image store. Alternatively, you can switch to using the containerd image store.

For more information about provenance attestations, see [here](https://docs.docker.com/build/metadata/attestations/slsa-provenance/).

### Push the build result to a registry \(--push\)

Shorthand for `--output=type=registry`. Will automatically push the build result to registry.

### Create SBOM attestations \(--sbom\)

Shorthand for `--attest=type=sbom`, used to configure SBOM attestations for the build result. For example, `--sbom=generator=<user>/<generator-image>` can be used as an abbreviation for `--attest=type=sbom,generator=<user>/<generator-image>`.

Additionally, `--sbom` can be used with Boolean values to enable or disable SBOM attestations. For example, `--sbom=false` disables all SBOM attestations.

Note that the default image store in Docker Engine doesn't support attestations. Provenance attestations only persist for images pushed directly to a registry if you use the default image store. Alternatively, you can switch to using the containerd image store.

For more information, see [here](https://docs.docker.com/build/metadata/attestations/sbom/).

### Secret to expose to the build \(--secret\)               --secret=[type=TYPE[,KEY=VALUE]

Exposes secrets \(authentication credentials, tokens\) to the build. A secret can be mounted into the build using a `RUN --mount=type=secret` mount in the [Dockerfile](https://docs.docker.com/reference/dockerfile/#run---mounttypesecret). For more information about how to use build secrets, see [Build secrets](https://docs.docker.com/build/building/secrets/).

Supported types are:

  * `type=file`   * `type=env`

Buildx attempts to detect the `type` automatically if unset. If an environment variable with the same key as `id` is set, then Buildx uses `type=env` and the variable value becomes the secret. If no such environment variable is set, and `type` is not set, then Buildx falls back to `type=file`.

#### `type=file`

Source a build secret from a file.

##### `type=file` synopsis               $ docker buildx build --secret [type=file,]id=<ID>[,src=<FILEPATH>] .     

##### `type=file` attributes

Key| Description| Default   ---|---|---   `id`| ID of the secret.| N/A \(this key is required\)   `src`, `source`| Filepath of the file containing the secret value \(absolute or relative to current working directory\).| `id` if unset.      ###### `type=file` usage

In the following example, `type=file` is automatically detected because no environment variable matching `aws` \(the ID\) is set.               $ docker buildx build --secret id=aws,src=$HOME/.aws/credentials .                    # syntax=docker/dockerfile:1     FROM python:3     RUN pip install awscli     RUN --mount=type=secret,id=aws,target=/root/.aws/credentials \       aws s3 cp s3://... ...

#### `type=env`

Source a build secret from an environment variable.

##### `type=env` synopsis               $ docker buildx build --secret [type=env,]id=<ID>[,env=<VARIABLE>] .     

##### `type=env` attributes

Key| Description| Default   ---|---|---   `id`| ID of the secret.| N/A \(this key is required\)   `env`, `src`, `source`| Environment variable to source the secret from.| `id` if unset.      ##### `type=env` usage

In the following example, `type=env` is automatically detected because an environment variable matching `id` is set.               $ SECRET_TOKEN=token docker buildx build --secret id=SECRET_TOKEN .                    # syntax=docker/dockerfile:1     FROM node:alpine     RUN --mount=type=bind,target=. \       --mount=type=secret,id=SECRET_TOKEN,env=SECRET_TOKEN \       yarn run test

In the following example, the build argument `SECRET_TOKEN` is set to contain the value of the environment variable `API_KEY`.               $ API_KEY=token docker buildx build --secret id=SECRET_TOKEN,env=API_KEY .     

You can also specify the name of the environment variable with `src` or `source`:               $ API_KEY=token docker buildx build --secret type=env,id=SECRET_TOKEN,src=API_KEY .     

> Note >  > Specifying the environment variable name with `src` or `source`, you are required to set `type=env` explicitly, or else Buildx assumes that the secret is `type=file`, and looks for a file with the name of `src` or `source` \(in this case, a file named `API_KEY` relative to the location where the `docker buildx build` command was executed.

### Shared memory size for build containers \(--shm-size\)

Sets the size of the shared memory allocated for build containers when using `RUN` instructions.

The format is `<number><unit>`. `number` must be greater than `0`. Unit is optional and can be `b` \(bytes\), `k` \(kilobytes\), `m` \(megabytes\), or `g` \(gigabytes\). If you omit the unit, the system uses bytes.

> Note >  > In most cases, it is recommended to let the builder automatically determine the appropriate configurations. Manual adjustments should only be considered when specific performance tuning is required for complex build scenarios.

### SSH agent socket or keys to expose to the build \(--ssh\)               --ssh=default|<id>[=<socket>|<key>[,<key>]]

This can be useful when some commands in your Dockerfile need specific SSH authentication \(e.g., cloning a private repository\).

`--ssh` exposes SSH agent socket or keys to the build and can be used with the [`RUN --mount=type=ssh` mount](https://docs.docker.com/reference/dockerfile/#run---mounttypessh).

Example to access Gitlab using an SSH agent socket:               # syntax=docker/dockerfile:1     FROM alpine     RUN apk add --no-cache openssh-client     RUN mkdir -p -m 0700 ~/.ssh && ssh-keyscan gitlab.com >> ~/.ssh/known_hosts     RUN --mount=type=ssh ssh -q -T git@gitlab.com 2>&1 | tee /hello     # "Welcome to GitLab, @GITLAB_USERNAME_ASSOCIATED_WITH_SSHKEY" should be printed here     # with the type of build progress is defined as `plain`.               $ eval $(ssh-agent)     $ ssh-add ~/.ssh/id_rsa     (Input your passphrase here)     $ docker buildx build --ssh default=$SSH_AUTH_SOCK .     

### Tag an image \(-t, --tag\)               $ docker buildx build -t docker/apache:2.0 .     

This examples builds in the same way as the previous example, but it then tags the resulting image. The repository name will be `docker/apache` and the tag `2.0`.

[Read more about valid tags](https://docs.docker.com/reference/cli/docker/image/tag/).

You can apply multiple tags to an image. For example, you can apply the `latest` tag to a newly built image and add another tag that references a specific version.

For example, to tag an image both as `docker/fedora-jboss:latest` and `docker/fedora-jboss:v2.1`, use the following:               $ docker buildx build -t docker/fedora-jboss:latest -t docker/fedora-jboss:v2.1 .     

### Specifying target build stage \(--target\)

When building a Dockerfile with multiple build stages, use the `--target` option to specify an intermediate build stage by name as a final stage for the resulting image. The builder skips commands after the target stage.               FROM debian AS build-env     # ...          FROM alpine AS production-env     # ...               $ docker buildx build -t mybuildimage --target build-env .     

### Set ulimits \(--ulimit\)

`--ulimit` overrides the default ulimits of build's containers when using `RUN` instructions and are specified with a soft and hard limit as such: `<type>=<soft limit>[:<hard limit>]`, for example:               $ docker buildx build --ulimit nofile=1024:1024 .     

> Note >  > If you don't provide a `hard limit`, the `soft limit` is used for both values. If no `ulimits` are set, they're inherited from the default `ulimits` set on the daemon.

> Note >  > In most cases, it is recommended to let the builder automatically determine the appropriate configurations. Manual adjustments should only be considered when specific performance tuning is required for complex build scenarios.