# docker buildx history trace | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/buildx/history/trace/
**Word Count:** 911
**Links Count:** 492
**Scraped:** 2025-07-16 01:50:20
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker buildx history trace

Description| Show the OpenTelemetry trace of a build record   ---|---   Usage| `docker buildx history trace [OPTIONS] [REF]`      ## Description

View the OpenTelemetry trace for a completed build. This command loads the trace into a Jaeger UI viewer and opens it in your browser.

This helps analyze build performance, step timing, and internal execution flows.

## Options

Option| Default| Description   ---|---|---   `--addr`| `127.0.0.1:0`| Address to bind the UI server   `--compare`| | Compare with another build record      ## Examples

### Open the OpenTelemetry trace for the most recent build

This command starts a temporary Jaeger UI server and opens your default browser to view the trace.               docker buildx history trace     

### Open the trace for a specific build               # Using a build ID     docker buildx history trace qu2gsuo8ejqrwdfii23xkkckt          # Or using a relative offset     docker buildx history trace ^1     

### Run the Jaeger UI on a specific port \(--addr\)               # Using a build ID     docker buildx history trace qu2gsuo8ejqrwdfii23xkkckt --addr 127.0.0.1:16686          # Or using a relative offset     docker buildx history trace ^1 --addr 127.0.0.1:16686     

### Compare two build traces \(--compare\)

Compare two specific builds by name:               # Using build IDs     docker buildx history trace --compare=qu2gsuo8ejqrwdfii23xkkckt qsiifiuf1ad9pa9qvppc0z1l3          # Or using a single relative offset     docker buildx history trace --compare=^1     

When you use a single reference with `--compare`, it compares that build against the most recent one.