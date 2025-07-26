# docker compose exec | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/compose/exec/
**Word Count:** 809
**Links Count:** 479
**Scraped:** 2025-07-16 01:50:39
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker compose exec

Description| Execute a command in a running container   ---|---   Usage| `docker compose exec [OPTIONS] SERVICE COMMAND [ARGS...]`      ## Description

This is the equivalent of `docker exec` targeting a Compose service.

With this subcommand, you can run arbitrary commands in your services. Commands allocate a TTY by default, so you can use a command such as `docker compose exec web sh` to get an interactive prompt.

## Options

Option| Default| Description   ---|---|---   `-d, --detach`| | Detached mode: Run command in the background   `-e, --env`| | Set environment variables   `--index`| | Index of the container if service has multiple replicas   `-T, --no-TTY`| `true`| Disable pseudo-TTY allocation. By default `docker compose exec` allocates a TTY.      `--privileged`| | Give extended privileges to the process   `-u, --user`| | Run the command as this user   `-w, --workdir`| | Path to workdir directory for this command