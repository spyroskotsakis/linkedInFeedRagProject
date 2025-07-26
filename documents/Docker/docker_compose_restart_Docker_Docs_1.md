# docker compose restart | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/compose/restart/
**Word Count:** 788
**Links Count:** 481
**Scraped:** 2025-07-16 01:50:39
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker compose restart

Description| Restart service containers   ---|---   Usage| `docker compose restart [OPTIONS] [SERVICE...]`      ## Description

Restarts all stopped and running services, or the specified services only.

If you make changes to your `compose.yml` configuration, these changes are not reflected after running this command. For example, changes to environment variables \(which are added after a container is built, but before the container's command is executed\) are not updated after restarting.

If you are looking to configure a service's restart policy, refer to [restart](https://github.com/compose-spec/compose-spec/blob/main/spec.md#restart) or [restart\_policy](https://github.com/compose-spec/compose-spec/blob/main/deploy.md#restart_policy).

## Options

Option| Default| Description   ---|---|---   `--no-deps`| | Don't restart dependent services   `-t, --timeout`| | Specify a shutdown timeout in seconds