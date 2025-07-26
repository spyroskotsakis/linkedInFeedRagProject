# Local and tar exporters | Docker Docs

**URL:** https://docs.docker.com/build/exporters/local-tar/
**Word Count:** 1112
**Links Count:** 642
**Scraped:** 2025-07-16 01:53:28
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Local and tar exporters

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

The `local` and `tar` exporters output the root filesystem of the build result into a local directory. They're useful for producing artifacts that aren't container images.

  * `local` exports files and directories.   * `tar` exports the same, but bundles the export into a tarball.

## Synopsis

Build a container image using the `local` exporter:               $ docker buildx build --output type=local[,parameters] .     $ docker buildx build --output type=tar[,parameters] .     

The following table describes the available parameters:

Parameter| Type| Default| Description   ---|---|---|---   `dest`| String| | Path to copy files to   `platform-split`| Boolean| `true`| When using the local exporter with a multi-platform build, by default, a subfolder matching each target platform is created in the destination directory. Set it to `false` to merge files from all platforms into the same directory.      ## Further reading

For more information on the `local` or `tar` exporters, see the [BuildKit README](https://github.com/moby/buildkit/blob/master/README.md#local-directory).