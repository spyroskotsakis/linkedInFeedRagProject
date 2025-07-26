# docker service ls | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/service/ls
**Word Count:** 1163
**Links Count:** 501
**Scraped:** 2025-07-16 01:57:18
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker service ls

Description| List services   ---|---   Usage| `docker service ls [OPTIONS]`   AliasesAn alias is a short or memorable alternative for a longer command.| `docker service list`      Swarm This command works with the Swarm orchestrator.

## Description

This command lists services that are running in the swarm.

> Note >  > This is a cluster management command, and must be executed on a swarm manager node. To learn about managers and workers, refer to the [Swarm mode section](https://docs.docker.com/engine/swarm/) in the documentation.

## Options

Option| Default| Description   ---|---|---   `-f, --filter`| | Filter output based on conditions provided   `--format`| | Format output using a custom template:   'table': Print output in table format with column headers \(default\)   'table TEMPLATE': Print output in table format using the given Go template   'json': Print in JSON format   'TEMPLATE': Print output using the given Go template.   Refer to <https://docs.docker.com/go/formatting/> for more information about formatting output with templates   `-q, --quiet`| | Only display IDs      ## Examples

On a manager node:               $ docker service ls          ID            NAME      MODE            REPLICAS             IMAGE     c8wgl7q4ndfd  frontend  replicated      5/5                  nginx:alpine     dmu1ept4cxcf  redis     replicated      3/3                  redis:7.4.1     iwe3278osahj  mongo     global          7/7                  mongo:3.3     hh08h9uu8uwr  job       replicated-job  1/1 (3/5 completed)  nginx:latest     

The `REPLICAS` column shows both the actual and desired number of tasks for the service. If the service is in `replicated-job` or `global-job`, it will additionally show the completion status of the job as completed tasks over total tasks the job will execute.

### Filtering \(--filter\)

The filtering flag \(`-f` or `--filter`\) format is of "key=value". If there is more than one filter, then pass multiple flags \(e.g., `--filter "foo=bar" --filter "bif=baz"`\).

The currently supported filters are:

  * [id](https://docs.docker.com/reference/cli/docker/service/ls/#id)   * [label](https://docs.docker.com/reference/cli/docker/service/ls/#label)   * [mode](https://docs.docker.com/reference/cli/docker/service/ls/#mode)   * [name](https://docs.docker.com/reference/cli/docker/service/ls/#name)

#### id

The `id` filter matches all or the prefix of a service's ID.

The following filter matches services with an ID starting with `0bcjw`:               $ docker service ls -f "id=0bcjw"     ID            NAME   MODE        REPLICAS  IMAGE     0bcjwfh8ychr  redis  replicated  1/1       redis:7.4.1     

#### label

The `label` filter matches services based on the presence of a `label` alone or a `label` and a value.

The following filter matches all services with a `project` label regardless of its value:               $ docker service ls --filter label=project     ID            NAME       MODE        REPLICAS  IMAGE     01sl1rp6nj5u  frontend2  replicated  1/1       nginx:alpine     36xvvwwauej0  frontend   replicated  5/5       nginx:alpine     74nzcxxjv6fq  backend    replicated  3/3       redis:7.4.1     

The following filter matches only services with the `project` label with the `project-a` value.               $ docker service ls --filter label=project=project-a     ID            NAME      MODE        REPLICAS  IMAGE     36xvvwwauej0  frontend  replicated  5/5       nginx:alpine     74nzcxxjv6fq  backend   replicated  3/3       redis:7.4.1     

#### mode

The `mode` filter matches on the mode \(either `replicated` or `global`\) of a service.

The following filter matches only `global` services.               $ docker service ls --filter mode=global     ID                  NAME                MODE                REPLICAS            IMAGE     w7y0v2yrn620        top                 global              1/1                 busybox     

#### name

The `name` filter matches on all or the prefix of a service's name.

The following filter matches services with a name starting with `redis`.               $ docker service ls --filter name=redis     ID            NAME   MODE        REPLICAS  IMAGE     0bcjwfh8ychr  redis  replicated  1/1       redis:7.4.1     

### Format the output \(--format\)

The formatting options \(`--format`\) pretty-prints services output using a Go template.

Valid placeholders for the Go template are listed below:

Placeholder| Description   ---|---   `.ID`| Service ID   `.Name`| Service name   `.Mode`| Service mode \(replicated, global\)   `.Replicas`| Service replicas   `.Image`| Service image   `.Ports`| Service ports published in ingress mode      When using the `--format` option, the `service ls` command will either output the data exactly as the template declares or, when using the `table` directive, includes column headers as well.

The following example uses a template without headers and outputs the `ID`, `Mode`, and `Replicas` entries separated by a colon \(`:`\) for all services:               $ docker service ls --format "{{.ID}}: {{.Mode}} {{.Replicas}}"          0zmvwuiu3vue: replicated 10/10     fm6uf97exkul: global 5/5     

To list all services in JSON format, use the `json` directive:               $ docker service ls --format json     {"ID":"ssniordqolsi","Image":"hello-world:latest","Mode":"replicated","Name":"hello","Ports":"","Replicas":"0/1"}