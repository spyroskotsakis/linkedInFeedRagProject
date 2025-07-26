# docker buildx debug | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/buildx/debug/
**Word Count:** 779
**Links Count:** 482
**Scraped:** 2025-07-16 01:50:20
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker buildx debug

Description| Start debugger   ---|---   Usage| `docker buildx debug`      **Experimental**

**This command is experimental.**

Experimental features are intended for testing and feedback as their functionality or design may change between releases without warning or can be removed entirely in a future release.

## Description

Start debugger

## Options

Option| Default| Description   ---|---|---   `--invoke`| | experimental \(CLI\) Launch a monitor with executing specified command   `--on`| `error`| experimental \(CLI\) When to launch the monitor \(\[always, error\]\)   `--progress`| `auto`| Set type of progress output \(`auto`, `plain`, `tty`, `rawjson`\) for the monitor. Use plain to show container output         ## Subcommands

Command| Description   ---|---   [`docker buildx debug build`](https://docs.docker.com/reference/cli/docker/buildx/debug/build/)| Start a build