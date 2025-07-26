# docker buildx history logs | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/buildx/history/logs/
**Word Count:** 887
**Links Count:** 489
**Scraped:** 2025-07-16 01:50:20
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker buildx history logs

Description| Print the logs of a build record   ---|---   Usage| `docker buildx history logs [OPTIONS] [REF]`      ## Description

Print the logs for a completed build. The output appears in the same format as `--progress=plain`, showing the full logs for each step.

By default, this shows logs for the most recent build on the current builder.

You can also specify an earlier build using an offset. For example:

  * `^1` shows logs for the build before the most recent   * `^2` shows logs for the build two steps back

## Options

Option| Default| Description   ---|---|---   `--progress`| `plain`| Set type of progress output \(plain, rawjson, tty\)      ## Examples

### Print logs for the most recent build               $ docker buildx history logs     #1 [internal] load build definition from Dockerfile     #1 transferring dockerfile: 31B done     #1 DONE 0.0s     #2 [internal] load .dockerignore     #2 transferring context: 2B done     #2 DONE 0.0s     ...     

By default, this shows logs for the most recent build on the current builder.

### Print logs for a specific build

To print logs for a specific build, use a build ID or offset:               # Using a build ID     docker buildx history logs qu2gsuo8ejqrwdfii23xkkckt          # Or using a relative offset     docker buildx history logs ^1     

### Set type of progress output \(--progress\)               $ docker buildx history logs ^1 --progress rawjson     {"id":"buildx_step_1","status":"START","timestamp":"2024-05-01T12:34:56.789Z","detail":"[internal] load build definition from Dockerfile"}     {"id":"buildx_step_1","status":"COMPLETE","timestamp":"2024-05-01T12:34:57.001Z","duration":212000000}     ...