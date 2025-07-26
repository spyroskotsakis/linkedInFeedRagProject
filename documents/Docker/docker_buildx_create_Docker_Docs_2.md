# docker buildx create | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/buildx/create/
**Word Count:** 1491
**Links Count:** 534
**Scraped:** 2025-07-16 01:50:20
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker buildx create

Description| Create a new builder instance   ---|---   Usage| `docker buildx create [OPTIONS] [CONTEXT|ENDPOINT]`      ## Description

Create makes a new builder instance pointing to a Docker context or endpoint, where context is the name of a context from `docker context ls` and endpoint is the address for Docker socket \(eg. `DOCKER_HOST` value\).

By default, the current Docker configuration is used for determining the context/endpoint value.

Builder instances are isolated environments where builds can be invoked. All Docker contexts also get the default builder instance.

## Options

Option| Default| Description   ---|---|---   `--append`| | Append a node to builder instead of changing it   `--bootstrap`| | Boot builder after creation   `--buildkitd-config`| | BuildKit daemon config file   `--buildkitd-flags`| | BuildKit daemon flags   `--driver`| | Driver to use \(available: `docker-container`, `kubernetes`, `remote`\)      `--driver-opt`| | Options for the driver   `--leave`| | Remove a node from builder instead of changing it   `--name`| | Builder instance name   `--node`| | Create/modify node with given name   `--platform`| | Fixed platforms for current node   `--use`| | Set the current builder instance      ## Examples

### Append a new node to an existing builder \(--append\)

The `--append` flag changes the action of the command to append a new node to an existing builder specified by `--name`. Buildx will choose an appropriate node for a build based on the platforms it supports.               $ docker buildx create mycontext1     eager_beaver          $ docker buildx create --name eager_beaver --append mycontext2     eager_beaver     

### Specify a configuration file for the BuildKit daemon \(--buildkitd-config\)               --buildkitd-config FILE

Specifies the configuration file for the BuildKit daemon to use. The configuration can be overridden by `--buildkitd-flags`. See an [example BuildKit daemon configuration file](https://github.com/moby/buildkit/blob/master/docs/buildkitd.toml.md).

If you don't specify a configuration file, Buildx looks for one by default in:

  * `$BUILDX_CONFIG/buildkitd.default.toml`   * `$DOCKER_CONFIG/buildx/buildkitd.default.toml`   * `~/.docker/buildx/buildkitd.default.toml`

Note that if you create a `docker-container` builder and have specified certificates for registries in the `buildkitd.toml` configuration, the files will be copied into the container under `/etc/buildkit/certs` and configuration will be updated to reflect that.

### Specify options for the BuildKit daemon \(--buildkitd-flags\)               --buildkitd-flags FLAGS

Adds flags when starting the BuildKit daemon. They take precedence over the configuration file specified by `--buildkitd-config`. See `buildkitd --help` for the available flags.               --buildkitd-flags '--debug --debugaddr 0.0.0.0:6666'

#### BuildKit daemon network mode

You can specify the network mode for the BuildKit daemon with either the configuration file specified by `--buildkitd-config` using the `worker.oci.networkMode` option or `--oci-worker-net` flag here. The default value is `auto` and can be one of `bridge`, `cni`, `host`:               --buildkitd-flags '--oci-worker-net bridge'

> Note >  > Network mode "bridge" is supported since BuildKit v0.13 and will become the default in next v0.14.

### Set the builder driver to use \(--driver\)               --driver DRIVER

Sets the builder driver to be used. A driver is a configuration of a BuildKit backend. Buildx supports the following drivers:

  * `docker` \(default\)   * `docker-container`   * `kubernetes`   * `remote`

For more information about build drivers, see [here](https://docs.docker.com/build/builders/drivers/).

#### `docker` driver

Uses the builder that is built into the Docker daemon. With this driver, the [`--load`](https://docs.docker.com/reference/cli/docker/buildx/build/#load) flag is implied by default on `buildx build`. However, building multi-platform images or exporting cache is not currently supported.

#### `docker-container` driver

Uses a BuildKit container that will be spawned via Docker. With this driver, both building multi-platform images and exporting cache are supported.

Unlike `docker` driver, built images will not automatically appear in `docker images` and [`build --load`](https://docs.docker.com/reference/cli/docker/buildx/build/#load) needs to be used to achieve that.

#### `kubernetes` driver

Uses Kubernetes pods. With this driver, you can spin up pods with defined BuildKit container image to build your images.

Unlike `docker` driver, built images will not automatically appear in `docker images` and [`build --load`](https://docs.docker.com/reference/cli/docker/buildx/build/#load) needs to be used to achieve that.

#### `remote` driver

Uses a remote instance of BuildKit daemon over an arbitrary connection. With this driver, you manually create and manage instances of buildkit yourself, and configure buildx to point at it.

Unlike `docker` driver, built images will not automatically appear in `docker images` and [`build --load`](https://docs.docker.com/reference/cli/docker/buildx/build/#load) needs to be used to achieve that.

### Set additional driver-specific options \(--driver-opt\)               --driver-opt OPTIONS

Passes additional driver-specific options. For information about available driver options, refer to the detailed documentation for the specific driver:

  * [`docker` driver](https://docs.docker.com/build/builders/drivers/docker/)   * [`docker-container` driver](https://docs.docker.com/build/builders/drivers/docker-container/)   * [`kubernetes` driver](https://docs.docker.com/build/builders/drivers/kubernetes/)   * [`remote` driver](https://docs.docker.com/build/builders/drivers/remote/)

### Remove a node from a builder \(--leave\)

The `--leave` flag changes the action of the command to remove a node from a builder. The builder needs to be specified with `--name` and node that is removed is set with `--node`.               $ docker buildx create --name mybuilder --node mybuilder0 --leave     

### Specify the name of the builder \(--name\)               --name NAME

The `--name` flag specifies the name of the builder to be created or modified. If none is specified, one will be automatically generated.

### Specify the name of the node \(--node\)               --node NODE

The `--node` flag specifies the name of the node to be created or modified. If you don't specify a name, the node name defaults to the name of the builder it belongs to, with an index number suffix.

### Set the platforms supported by the node \(--platform\)               --platform PLATFORMS

The `--platform` flag sets the platforms supported by the node. It expects a comma-separated list of platforms of the form OS/architecture/variant. The node will also automatically detect the platforms it supports, but manual values take priority over the detected ones and can be used when multiple nodes support building for the same platform.               $ docker buildx create --platform linux/amd64     $ docker buildx create --platform linux/arm64,linux/arm/v7     

### Automatically switch to the newly created builder \(--use\)

The `--use` flag automatically switches the current builder to the newly created one. Equivalent to running `docker buildx use $(docker buildx create ...)`.