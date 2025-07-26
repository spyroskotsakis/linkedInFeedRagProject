# docker secret create | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/secret/create/
**Word Count:** 870
**Links Count:** 490
**Scraped:** 2025-07-16 01:52:00
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker secret create

Description| Create a secret from a file or STDIN as content   ---|---   Usage| `docker secret create [OPTIONS] SECRET [file|-]`      Swarm This command works with the Swarm orchestrator.

## Description

Creates a secret using standard input or from a file for the secret content.

For detailed information about using secrets, refer to [manage sensitive data with Docker secrets](https://docs.docker.com/engine/swarm/secrets/).

> Note >  > This is a cluster management command, and must be executed on a swarm manager node. To learn about managers and workers, refer to the [Swarm mode section](https://docs.docker.com/engine/swarm/) in the documentation.

## Options

Option| Default| Description   ---|---|---   `-d, --driver`| | API 1.31+ Secret driver   `-l, --label`| | Secret labels   `--template-driver`| | API 1.37+ Template driver      ## Examples

### Create a secret               $ printf "my super secret password" | docker secret create my_secret -          onakdyv307se2tl7nl20anokv          $ docker secret ls          ID                          NAME                CREATED             UPDATED     onakdyv307se2tl7nl20anokv   my_secret           6 seconds ago       6 seconds ago     

### Create a secret with a file               $ docker secret create my_secret ./secret.json          dg426haahpi5ezmkkj5kyl3sn          $ docker secret ls          ID                          NAME                CREATED             UPDATED     dg426haahpi5ezmkkj5kyl3sn   my_secret           7 seconds ago       7 seconds ago     

### Create a secret with labels \(--label\)               $ docker secret create \       --label env=dev \       --label rev=20170324 \       my_secret ./secret.json          eo7jnzguqgtpdah3cm5srfb97                    $ docker secret inspect my_secret          [         {             "ID": "eo7jnzguqgtpdah3cm5srfb97",             "Version": {                 "Index": 17             },             "CreatedAt": "2017-03-24T08:15:09.735271783Z",             "UpdatedAt": "2017-03-24T08:15:09.735271783Z",             "Spec": {                 "Name": "my_secret",                 "Labels": {                     "env": "dev",                     "rev": "20170324"                 }             }         }     ]