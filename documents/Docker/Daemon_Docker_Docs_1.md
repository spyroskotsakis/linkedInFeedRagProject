# Daemon | Docker Docs

**URL:** https://docs.docker.com/config/daemon
**Word Count:** 1379
**Links Count:** 657
**Scraped:** 2025-07-16 02:04:56
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Docker daemon configuration overview

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

This page shows you how to customize the Docker daemon, `dockerd`.

> Note >  > This page is for users who've installed Docker Engine manually. If you're using Docker Desktop, refer to the [settings page](https://docs.docker.com/desktop/settings-and-maintenance/settings/#docker-engine).

## Configure the Docker daemon

There are two ways to configure the Docker daemon:

  * Use a JSON configuration file. This is the preferred option, since it keeps all configurations in a single place.   * Use flags when starting `dockerd`.

You can use both of these options together as long as you don't specify the same option both as a flag and in the JSON file. If that happens, the Docker daemon won't start and prints an error message.

### Configuration file

The following table shows the location where the Docker daemon expects to find the configuration file by default, depending on your system and how you're running the daemon.

OS and configuration| File location   ---|---   Linux, regular setup| `/etc/docker/daemon.json`   Linux, rootless mode| `~/.config/docker/daemon.json`   Windows| `C:\ProgramData\docker\config\daemon.json`      For rootless mode, the daemon respects the `XDG_CONFIG_HOME` variable. If set, the expected file location is `$XDG_CONFIG_HOME/docker/daemon.json`.

You can also explicitly specify the location of the configuration file on startup, using the `dockerd --config-file` flag.

Learn about the available configuration options in the [dockerd reference docs](https://docs.docker.com/reference/cli/dockerd/#daemon-configuration-file)

### Configuration using flags

You can also start the Docker daemon manually and configure it using flags. This can be useful for troubleshooting problems.

Here's an example of how to manually start the Docker daemon, using the same configurations as shown in the previous JSON configuration:               $ dockerd --debug \       --tls=true \       --tlscert=/var/docker/server.pem \       --tlskey=/var/docker/serverkey.pem \       --host tcp://192.168.59.3:2376     

Learn about the available configuration options in the [dockerd reference docs](https://docs.docker.com/reference/cli/dockerd/), or by running:               $ dockerd --help     

## Daemon data directory

The Docker daemon persists all data in a single directory. This tracks everything related to Docker, including containers, images, volumes, service definition, and secrets.

By default this directory is:

  * `/var/lib/docker` on Linux.   * `C:\ProgramData\docker` on Windows.

You can configure the Docker daemon to use a different directory, using the `data-root` configuration option. For example:               {       "data-root": "/mnt/docker-data"     }

Since the state of a Docker daemon is kept on this directory, make sure you use a dedicated directory for each daemon. If two daemons share the same directory, for example, an NFS share, you are going to experience errors that are difficult to troubleshoot.

## Next steps

Many specific configuration options are discussed throughout the Docker documentation. Some places to go next include:

  * [Automatically start containers](https://docs.docker.com/engine/containers/start-containers-automatically/)   * [Limit a container's resources](https://docs.docker.com/engine/containers/resource_constraints/)   * [Configure storage drivers](https://docs.docker.com/engine/storage/drivers/select-storage-driver/)   * [Container security](https://docs.docker.com/engine/security/)   * [Configure the Docker daemon to use a proxy](https://docs.docker.com/engine/daemon/proxy/)