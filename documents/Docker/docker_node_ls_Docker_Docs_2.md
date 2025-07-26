# docker node ls | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/node/ls/
**Word Count:** 1321
**Links Count:** 510
**Scraped:** 2025-07-16 01:51:40
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker node ls

Description| List nodes in the swarm   ---|---   Usage| `docker node ls [OPTIONS]`   AliasesAn alias is a short or memorable alternative for a longer command.| `docker node list`      Swarm This command works with the Swarm orchestrator.

## Description

Lists all the nodes that the Docker Swarm manager knows about. You can filter using the `-f` or `--filter` flag. Refer to the filtering section for more information about available filter options.

> Note >  > This is a cluster management command, and must be executed on a swarm manager node. To learn about managers and workers, refer to the [Swarm mode section](https://docs.docker.com/engine/swarm/) in the documentation.

## Options

Option| Default| Description   ---|---|---   `-f, --filter`| | Filter output based on conditions provided   `--format`| | Format output using a custom template:   'table': Print output in table format with column headers \(default\)   'table TEMPLATE': Print output in table format using the given Go template   'json': Print in JSON format   'TEMPLATE': Print output using the given Go template.   Refer to <https://docs.docker.com/go/formatting/> for more information about formatting output with templates   `-q, --quiet`| | Only display IDs      ## Examples               $ docker node ls          ID                           HOSTNAME        STATUS  AVAILABILITY  MANAGER STATUS     1bcef6utixb0l0ca7gxuivsj0    swarm-worker2   Ready   Active     38ciaotwjuritcdtn9npbnkuz    swarm-worker1   Ready   Active     e216jshn25ckzbvmwlnh5jr3g *  swarm-manager1  Ready   Active        Leader     

> Note >  > In the above example output, there is a hidden column of `.Self` that indicates if the node is the same node as the current docker daemon. A `*` \(e.g., `e216jshn25ckzbvmwlnh5jr3g *`\) means this node is the current docker daemon.

### Filtering \(--filter\)

The filtering flag \(`-f` or `--filter`\) format is of "key=value". If there is more than one filter, then pass multiple flags \(e.g., `--filter "foo=bar" --filter "bif=baz"`\)

The currently supported filters are:

  * id   * label   * node.label   * membership   * name   * role

#### id

The `id` filter matches all or part of a node's id.               $ docker node ls -f id=1          ID                         HOSTNAME       STATUS  AVAILABILITY  MANAGER STATUS     1bcef6utixb0l0ca7gxuivsj0  swarm-worker2  Ready   Active     

#### label

The `label` filter matches nodes based on engine labels and on the presence of a `label` alone or a `label` and a value. Engine labels are configured in the [daemon configuration](https://docs.docker.com/reference/cli/dockerd/#daemon-configuration-file). To filter on Swarm `node` labels, use `node.label` instead.

The following filter matches nodes with the `foo` label regardless of its value.               $ docker node ls -f "label=foo"          ID                         HOSTNAME       STATUS  AVAILABILITY  MANAGER STATUS     1bcef6utixb0l0ca7gxuivsj0  swarm-worker2  Ready   Active     

#### node.label

The `node.label` filter matches nodes based on node labels and on the presence of a `node.label` alone or a `node.label` and a value.

The following filter updates nodes to have a `region` node label:               $ docker node update --label-add region=region-a swarm-test-01     $ docker node update --label-add region=region-a swarm-test-02     $ docker node update --label-add region=region-b swarm-test-03     $ docker node update --label-add region=region-b swarm-test-04     

Show all nodes that have a `region` node label set:               $ docker node ls --filter node.label=region          ID                            HOSTNAME        STATUS    AVAILABILITY   MANAGER STATUS   ENGINE VERSION     yg550ettvsjn6g6t840iaiwgb *   swarm-test-01   Ready     Active         Leader           23.0.3     2lm9w9kbepgvkzkkeyku40e65     swarm-test-02   Ready     Active         Reachable        23.0.3     hc0pu7ntc7s4uvj4pv7z7pz15     swarm-test-03   Ready     Active         Reachable        23.0.3     n41b2cijmhifxxvz56vwrs12q     swarm-test-04   Ready     Active                          23.0.3     

Show all nodes that have a `region` node label, with value `region-a`:               $ docker node ls --filter node.label=region=region-a          ID                            HOSTNAME        STATUS    AVAILABILITY   MANAGER STATUS   ENGINE VERSION     yg550ettvsjn6g6t840iaiwgb *   swarm-test-01   Ready     Active         Leader           23.0.3     2lm9w9kbepgvkzkkeyku40e65     swarm-test-02   Ready     Active         Reachable        23.0.3     

#### membership

The `membership` filter matches nodes based on the presence of a `membership` and a value `accepted` or `pending`.

The following filter matches nodes with the `membership` of `accepted`.               $ docker node ls -f "membership=accepted"          ID                           HOSTNAME        STATUS  AVAILABILITY  MANAGER STATUS     1bcef6utixb0l0ca7gxuivsj0    swarm-worker2   Ready   Active     38ciaotwjuritcdtn9npbnkuz    swarm-worker1   Ready   Active     

#### name

The `name` filter matches on all or part of a node hostname.

The following filter matches the nodes with a name equal to `swarm-master` string.               $ docker node ls -f name=swarm-manager1          ID                           HOSTNAME        STATUS  AVAILABILITY  MANAGER STATUS     e216jshn25ckzbvmwlnh5jr3g *  swarm-manager1  Ready   Active        Leader     

#### role

The `role` filter matches nodes based on the presence of a `role` and a value `worker` or `manager`.

The following filter matches nodes with the `manager` role.               $ docker node ls -f "role=manager"          ID                           HOSTNAME        STATUS  AVAILABILITY  MANAGER STATUS     e216jshn25ckzbvmwlnh5jr3g *  swarm-manager1  Ready   Active        Leader     

### Format the output \(--format\)

The formatting options \(`--format`\) pretty-prints nodes output using a Go template.

Valid placeholders for the Go template are listed below:

Placeholder| Description   ---|---   `.ID`| Node ID   `.Self`| Node of the daemon \(`true/false`, `true`indicates that the node is the same as current docker daemon\)   `.Hostname`| Node hostname   `.Status`| Node status   `.Availability`| Node availability \("active", "pause", or "drain"\)   `.ManagerStatus`| Manager status of the node   `.TLSStatus`| TLS status of the node \("Ready", or "Needs Rotation" has TLS certificate signed by an old CA\)   `.EngineVersion`| Engine version      When using the `--format` option, the `node ls` command will either output the data exactly as the template declares or, when using the `table` directive, includes column headers as well.

The following example uses a template without headers and outputs the `ID`, `Hostname`, and `TLS Status` entries separated by a colon \(`:`\) for all nodes:               $ docker node ls --format "{{.ID}}: {{.Hostname}} {{.TLSStatus}}"          e216jshn25ckzbvmwlnh5jr3g: swarm-manager1 Ready     35o6tiywb700jesrt3dmllaza: swarm-worker1 Needs Rotation     

To list all nodes in JSON format, use the `json` directive:               $ docker node ls --format json     {"Availability":"Active","EngineVersion":"23.0.3","Hostname":"docker-desktop","ID":"k8f4w7qtzpj5sqzclcqafw35g","ManagerStatus":"Leader","Self":true,"Status":"Ready","TLSStatus":"Ready"}