# docker buildx history ls | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/buildx/history/ls
**Word Count:** 909
**Links Count:** 500
**Scraped:** 2025-07-16 01:57:18
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker buildx history ls

Description| List build records   ---|---   Usage| `docker buildx history ls [OPTIONS]`      ## Description

List completed builds recorded by the active builder. Each entry includes the build ID, name, status, timestamp, and duration.

By default, only records for the current builder are shown. You can filter results using flags.

## Options

Option| Default| Description   ---|---|---   `--filter`| | Provide filter values \(e.g., `status=error`\)   `--format`| `table`| Format the output   `--local`| | List records for current repository only   `--no-trunc`| | Don't truncate output      ## Examples

### List all build records for the current builder               $ docker buildx history ls     BUILD ID                    NAME           STATUS     CREATED AT        DURATION     qu2gsuo8ejqrwdfii23xkkckt   .dev/2850      Completed  3 days ago        1.4s     qsiifiuf1ad9pa9qvppc0z1l3   .dev/2850      Completed  3 days ago        1.3s     g9808bwrjrlkbhdamxklx660b   .dev/3120      Completed  5 days ago        2.1s     

### List failed builds \(--filter\)               docker buildx history ls --filter status=error     

You can filter the list using the `--filter` flag. Supported filters include:

Filter| Supported comparisons| Example   ---|---|---   `ref`, `repository`, `status`| Support `=` and `!=` comparisons| `--filter status!=success`   `startedAt`, `completedAt`, `duration`| Support `<` and `>` comparisons with time values| `--filter duration>30s`      You can combine multiple filters by repeating the `--filter` flag:               docker buildx history ls --filter status=error --filter duration>30s     

### List builds from the current project \(--local\)               docker buildx history ls --local     

### Display full output without truncation \(--no-trunc\)               docker buildx history ls --no-trunc     

### Format output \(--format\)

#### JSON output               $ docker buildx history ls --format json     [       {         "ID": "qu2gsuo8ejqrwdfii23xkkckt",         "Name": ".dev/2850",         "Status": "Completed",         "CreatedAt": "2025-04-15T12:33:00Z",         "Duration": "1.4s"       },       {         "ID": "qsiifiuf1ad9pa9qvppc0z1l3",         "Name": ".dev/2850",         "Status": "Completed",         "CreatedAt": "2025-04-15T12:29:00Z",         "Duration": "1.3s"       }     ]     

#### Go template output               $ docker buildx history ls --format '{{.Name}} - {{.Duration}}'     .dev/2850 - 1.4s     .dev/2850 - 1.3s     .dev/3120 - 2.1s