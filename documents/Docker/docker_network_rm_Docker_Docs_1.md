# docker network rm | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/network/rm/
**Word Count:** 850
**Links Count:** 485
**Scraped:** 2025-07-16 01:51:40
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker network rm

Description| Remove one or more networks   ---|---   Usage| `docker network rm NETWORK [NETWORK...]`   AliasesAn alias is a short or memorable alternative for a longer command.| `docker network remove`      ## Description

Removes one or more networks by name or identifier. To remove a network, you must first disconnect any containers connected to it.

## Options

Option| Default| Description   ---|---|---   `-f, --force`| | Do not error if the network does not exist      ## Examples

### Remove a network

To remove the network named 'my-network':               $ docker network rm my-network     

### Remove multiple networks

To delete multiple networks in a single `docker network rm` command, provide multiple network names or ids. The following example deletes a network with id `3695c422697f` and a network named `my-network`:               $ docker network rm 3695c422697f my-network     

When you specify multiple networks, the command attempts to delete each in turn. If the deletion of one network fails, the command continues to the next on the list and tries to delete that. The command reports success or failure for each deletion.