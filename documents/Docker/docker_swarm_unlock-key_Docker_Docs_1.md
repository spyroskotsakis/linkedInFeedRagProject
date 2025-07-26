# docker swarm unlock-key | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/swarm/unlock-key/
**Word Count:** 933
**Links Count:** 488
**Scraped:** 2025-07-16 01:52:00
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker swarm unlock-key

Description| Manage the unlock key   ---|---   Usage| `docker swarm unlock-key [OPTIONS]`      Swarm This command works with the Swarm orchestrator.

## Description

An unlock key is a secret key needed to unlock a manager after its Docker daemon restarts. These keys are only used when the autolock feature is enabled for the swarm.

You can view or rotate the unlock key using `swarm unlock-key`. To view the key, run the `docker swarm unlock-key` command without any arguments:

> Note >  > This is a cluster management command, and must be executed on a swarm manager node. To learn about managers and workers, refer to the [Swarm mode section](https://docs.docker.com/engine/swarm/) in the documentation.

## Options

Option| Default| Description   ---|---|---   `-q, --quiet`| | Only display token   `--rotate`| | Rotate unlock key      ## Examples               $ docker swarm unlock-key          To unlock a swarm manager after it restarts, run the `docker swarm unlock`     command and provide the following key:              SWMKEY-1-fySn8TY4w5lKcWcJPIpKufejh9hxx5KYwx6XZigx3Q4          Remember to store this key in a password manager, since without it you     will not be able to restart the manager.     

Use the `--rotate` flag to rotate the unlock key to a new, randomly-generated key:               $ docker swarm unlock-key --rotate          Successfully rotated manager unlock key.          To unlock a swarm manager after it restarts, run the `docker swarm unlock`     command and provide the following key:              SWMKEY-1-7c37Cc8654o6p38HnroywCi19pllOnGtbdZEgtKxZu8          Remember to store this key in a password manager, since without it you     will not be able to restart the manager.     

The `-q` \(or `--quiet`\) flag only prints the key:               $ docker swarm unlock-key -q          SWMKEY-1-7c37Cc8654o6p38HnroywCi19pllOnGtbdZEgtKxZu8     

### `--rotate`

This flag rotates the unlock key, replacing it with a new randomly-generated key. The old unlock key will no longer be accepted.

### `--quiet`

Only print the unlock key, without instructions.