# docker stack ls | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/stack/ls
**Word Count:** 910
**Links Count:** 486
**Scraped:** 2025-07-16 01:56:34
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker stack ls

Description| List stacks   ---|---   Usage| `docker stack ls [OPTIONS]`   AliasesAn alias is a short or memorable alternative for a longer command.| `docker stack list`      Swarm This command works with the Swarm orchestrator.

## Description

Lists the stacks.

> Note >  > This is a cluster management command, and must be executed on a swarm manager node. To learn about managers and workers, refer to the [Swarm mode section](https://docs.docker.com/engine/swarm/) in the documentation.

## Options

Option| Default| Description   ---|---|---   `--format`| | Format output using a custom template:   'table': Print output in table format with column headers \(default\)   'table TEMPLATE': Print output in table format using the given Go template   'json': Print in JSON format   'TEMPLATE': Print output using the given Go template.   Refer to <https://docs.docker.com/go/formatting/> for more information about formatting output with templates      ## Examples

The following command shows all stacks and some additional information:               $ docker stack ls          ID                 SERVICES            ORCHESTRATOR     myapp              2                   Kubernetes     vossibility-stack  6                   Swarm     

### Format the output \(--format\)

The formatting option \(`--format`\) pretty-prints stacks using a Go template.

Valid placeholders for the Go template are listed below:

Placeholder| Description   ---|---   `.Name`| Stack name   `.Services`| Number of services   `.Orchestrator`| Orchestrator name   `.Namespace`| Namespace      When using the `--format` option, the `stack ls` command either outputs the data exactly as the template declares or, when using the `table` directive, includes column headers as well.

The following example uses a template without headers and outputs the `Name` and `Services` entries separated by a colon \(`:`\) for all stacks:               $ docker stack ls --format "{{.Name}}: {{.Services}}"     web-server: 1     web-cache: 4     

To list all stacks in JSON format, use the `json` directive:               $ docker stack ls --format json     {"Name":"myapp","Namespace":"","Orchestrator":"Swarm","Services":"3"}