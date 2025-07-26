# docker volume ls | Docker Docs

**URL:** http://docs.docker.com/reference/cli/docker/volume/ls
**Word Count:** 1138
**Links Count:** 499
**Scraped:** 2025-07-16 02:10:49
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](http://docs.docker.com/get-started/)   * [Guides](http://docs.docker.com/guides/)   * [Manuals](http://docs.docker.com/manuals/)

* * *

# docker volume ls

Description| List volumes   ---|---   Usage| `docker volume ls [OPTIONS]`   AliasesAn alias is a short or memorable alternative for a longer command.| `docker volume list`      ## Description

List all the volumes known to Docker. You can filter using the `-f` or `--filter` flag. Refer to the filtering section for more information about available filter options.

## Options

Option| Default| Description   ---|---|---   `--cluster`| | API 1.42+ Swarm Display only cluster volumes, and use cluster volume list formatting      `-f, --filter`| | Provide filter values \(e.g. `dangling=true`\)   `--format`| | Format output using a custom template:   'table': Print output in table format with column headers \(default\)   'table TEMPLATE': Print output in table format using the given Go template   'json': Print in JSON format   'TEMPLATE': Print output using the given Go template.   Refer to <https://docs.docker.com/go/formatting/> for more information about formatting output with templates   `-q, --quiet`| | Only display volume names      ## Examples

### Create a volume               $ docker volume create rosemary          rosemary          $ docker volume create tyler          tyler          $ docker volume ls          DRIVER              VOLUME NAME     local               rosemary     local               tyler     

### Filtering \(--filter\)

The filtering flag \(`-f` or `--filter`\) format is of "key=value". If there is more than one filter, then pass multiple flags \(e.g., `--filter "foo=bar" --filter "bif=baz"`\)

The currently supported filters are:

  * dangling \(Boolean - true or false, 0 or 1\)   * driver \(a volume driver's name\)   * label \(`label=<key>` or `label=<key>=<value>`\)   * name \(a volume's name\)

#### dangling

The `dangling` filter matches on all volumes not referenced by any containers               $ docker run -d  -v tyler:/tmpwork  busybox          f86a7dd02898067079c99ceacd810149060a70528eff3754d0b0f1a93bd0af18     $ docker volume ls -f dangling=true     DRIVER              VOLUME NAME     local               rosemary     

#### driver

The `driver` filter matches volumes based on their driver.

The following example matches volumes that are created with the `local` driver:               $ docker volume ls -f driver=local          DRIVER              VOLUME NAME     local               rosemary     local               tyler     

#### label

The `label` filter matches volumes based on the presence of a `label` alone or a `label` and a value.

First, create some volumes to illustrate this;               $ docker volume create the-doctor --label is-timelord=yes          the-doctor     $ docker volume create daleks --label is-timelord=no          daleks     

The following example filter matches volumes with the `is-timelord` label regardless of its value.               $ docker volume ls --filter label=is-timelord          DRIVER              VOLUME NAME     local               daleks     local               the-doctor     

As the above example demonstrates, both volumes with `is-timelord=yes`, and `is-timelord=no` are returned.

Filtering on both `key` _and_ `value` of the label, produces the expected result:               $ docker volume ls --filter label=is-timelord=yes          DRIVER              VOLUME NAME     local               the-doctor     

Specifying multiple label filter produces an "and" search; all conditions should be met;               $ docker volume ls --filter label=is-timelord=yes --filter label=is-timelord=no          DRIVER              VOLUME NAME     

#### name

The `name` filter matches on all or part of a volume's name.

The following filter matches all volumes with a name containing the `rose` string.               $ docker volume ls -f name=rose          DRIVER              VOLUME NAME     local               rosemary     

### Format the output \(--format\)

The formatting options \(`--format`\) pretty-prints volumes output using a Go template.

Valid placeholders for the Go template are listed below:

Placeholder| Description   ---|---   `.Name`| Volume name   `.Driver`| Volume driver   `.Scope`| Volume scope \(local, global\)   `.Mountpoint`| The mount point of the volume on the host   `.Labels`| All labels assigned to the volume   `.Label`| Value of a specific label for this volume. For example `{{.Label "project.version"}}`      When using the `--format` option, the `volume ls` command will either output the data exactly as the template declares or, when using the `table` directive, includes column headers as well.

The following example uses a template without headers and outputs the `Name` and `Driver` entries separated by a colon \(`:`\) for all volumes:               $ docker volume ls --format "{{.Name}}: {{.Driver}}"          vol1: local     vol2: local     vol3: local     

To list all volumes in JSON format, use the `json` directive:               $ docker volume ls --format json     {"Driver":"local","Labels":"","Links":"N/A","Mountpoint":"/var/lib/docker/volumes/docker-cli-dev-cache/_data","Name":"docker-cli-dev-cache","Scope":"local","Size":"N/A"}