# Local file logging driver | Docker Docs

**URL:** https://docs.docker.com/engine/logging/drivers/local/
**Word Count:** 1316
**Links Count:** 646
**Scraped:** 2025-07-16 01:53:28
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Local file logging driver

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

The `local` logging driver captures output from container's stdout/stderr and writes them to an internal storage that's optimized for performance and disk use.

By default, the `local` driver preserves 100MB of log messages per container and uses automatic compression to reduce the size on disk. The 100MB default value is based on a 20M default size for each file and a default count of 5 for the number of such files \(to account for log rotation\).

> Warning >  > The `local` logging driver uses file-based storage. These files are designed to be exclusively accessed by the Docker daemon. Interacting with these files with external tools may interfere with Docker's logging system and result in unexpected behavior, and should be avoided.

## Usage

To use the `local` driver as the default logging driver, set the `log-driver` and `log-opt` keys to appropriate values in the `daemon.json` file, which is located in `/etc/docker/` on Linux hosts or `C:\ProgramData\docker\config\daemon.json` on Windows Server. For more about configuring Docker using `daemon.json`, see [daemon.json](https://docs.docker.com/reference/cli/dockerd/#daemon-configuration-file).

The following example sets the log driver to `local` and sets the `max-size` option.               {       "log-driver": "local",       "log-opts": {         "max-size": "10m"       }     }

Restart Docker for the changes to take effect for newly created containers. Existing containers don't use the new logging configuration automatically.

You can set the logging driver for a specific container by using the `--log-driver` flag to `docker container create` or `docker run`:               $ docker run \           --log-driver local --log-opt max-size=10m \           alpine echo hello world     

Note that `local` is a bash reserved keyword, so you may need to quote it in scripts.

### Options

The `local` logging driver supports the following logging options:

Option| Description| Example value   ---|---|---   `max-size`| The maximum size of the log before it's rolled. A positive integer plus a modifier representing the unit of measure \(`k`, `m`, or `g`\). Defaults to 20m.| `--log-opt max-size=10m`   `max-file`| The maximum number of log files that can be present. If rolling the logs creates excess files, the oldest file is removed. A positive integer. Defaults to 5.| `--log-opt max-file=3`   `compress`| Toggle compression of rotated log files. Enabled by default.| `--log-opt compress=false`      ### Examples

This example starts an `alpine` container which can have a maximum of 3 log files no larger than 10 megabytes each.               $ docker run -it --log-driver local --log-opt max-size=10m --log-opt max-file=3 alpine ash