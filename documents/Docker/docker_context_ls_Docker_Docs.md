# docker context ls | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/context/ls
**Word Count:** 806
**Links Count:** 482
**Scraped:** 2025-07-16 01:56:12
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker context ls

Description| List contexts   ---|---   Usage| `docker context ls [OPTIONS]`   AliasesAn alias is a short or memorable alternative for a longer command.| `docker context list`      ## Description

List contexts

## Options

Option| Default| Description   ---|---|---   `--format`| | Format output using a custom template:   'table': Print output in table format with column headers \(default\)   'table TEMPLATE': Print output in table format using the given Go template   'json': Print in JSON format   'TEMPLATE': Print output using the given Go template.   Refer to <https://docs.docker.com/go/formatting/> for more information about formatting output with templates   `-q, --quiet`| | Only show context names      ## Examples

Use `docker context ls` to print all contexts. The currently active context is indicated with an `*`:               $ docker context ls          NAME                DESCRIPTION                               DOCKER ENDPOINT                      ORCHESTRATOR     default *           Current DOCKER_HOST based configuration   unix:///var/run/docker.sock          swarm     production                                                    tcp:///prod.corp.example.com:2376     staging                                                       tcp:///stage.corp.example.com:2376