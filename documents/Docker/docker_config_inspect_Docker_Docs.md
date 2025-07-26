# docker config inspect | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/config/inspect
**Word Count:** 916
**Links Count:** 490
**Scraped:** 2025-07-16 01:57:18
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker config inspect

Description| Display detailed information on one or more configs   ---|---   Usage| `docker config inspect [OPTIONS] CONFIG [CONFIG...]`      Swarm This command works with the Swarm orchestrator.

## Description

Inspects the specified config.

By default, this renders all results in a JSON array. If a format is specified, the given template will be executed for each result.

Go's [text/template](https://pkg.go.dev/text/template) package describes all the details of the format.

For detailed information about using configs, refer to [store configuration data using Docker Configs](https://docs.docker.com/engine/swarm/configs/).

> Note >  > This is a cluster management command, and must be executed on a Swarm manager node. To learn about managers and workers, refer to the [Swarm mode section](https://docs.docker.com/engine/swarm/) in the documentation.

## Options

Option| Default| Description   ---|---|---   `-f, --format`| | Format output using a custom template:   'json': Print in JSON format   'TEMPLATE': Print output using the given Go template.   Refer to <https://docs.docker.com/go/formatting/> for more information about formatting output with templates   `--pretty`| | Print the information in a human friendly format      ## Examples

### Inspect a config by name or ID

You can inspect a config, either by its _name_ , or _ID_

For example, given the following config:               $ docker config ls          ID                          NAME                CREATED             UPDATED     eo7jnzguqgtpdah3cm5srfb97   my_config           3 minutes ago       3 minutes ago                    $ docker config inspect config.json     

The output is in JSON format, for example:               [       {         "ID": "eo7jnzguqgtpdah3cm5srfb97",         "Version": {           "Index": 17         },         "CreatedAt": "2017-03-24T08:15:09.735271783Z",         "UpdatedAt": "2017-03-24T08:15:09.735271783Z",         "Spec": {           "Name": "my_config",           "Labels": {             "env": "dev",             "rev": "20170324"           },           "Data": "aGVsbG8K"         }       }     ]

### Format the output \(--format\)

You can use the --format option to obtain specific information about a config. The following example command outputs the creation time of the config.               $ docker config inspect --format='{{.CreatedAt}}' eo7jnzguqgtpdah3cm5srfb97          2017-03-24 08:15:09.735271783 +0000 UTC