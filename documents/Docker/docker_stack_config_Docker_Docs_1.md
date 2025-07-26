# docker stack config | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/stack/config/
**Word Count:** 905
**Links Count:** 483
**Scraped:** 2025-07-16 01:52:00
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker stack config

Description| Outputs the final config file, after doing merges and interpolations   ---|---   Usage| `docker stack config [OPTIONS]`      Swarm This command works with the Swarm orchestrator.

## Description

Outputs the final Compose file, after doing the merges and interpolations of the input Compose files.

## Options

Option| Default| Description   ---|---|---   `-c, --compose-file`| | Path to a Compose file, or `-` to read from stdin   `--skip-interpolation`| | Skip interpolation and output only merged config      ## Examples

The following command outputs the result of the merge and interpolation of two Compose files.               $ docker stack config --compose-file docker-compose.yml --compose-file docker-compose.prod.yml     

The Compose file can also be provided as standard input with `--compose-file -`:               $ cat docker-compose.yml | docker stack config --compose-file -     

### Skipping interpolation

In some cases, it might be useful to skip interpolation of environment variables. For example, when you want to pipe the output of this command back to `stack deploy`.

If you have a regex for a redirect route in an environment variable for your webserver you would use two `$` signs to prevent `stack deploy` from interpolating `${1}`.                 service: webserver       environment:         REDIRECT_REGEX=http://host/redirect/$${1}

With interpolation, the `stack config` command will replace the environment variable in the Compose file with `REDIRECT_REGEX=http://host/redirect/${1}`, but then when piping it back to the `stack deploy` command it will be interpolated again and result in undefined behavior. That is why, when piping the output back to `stack deploy` one should always prefer the `--skip-interpolation` option.               $ docker stack config --compose-file web.yml --compose-file web.prod.yml --skip-interpolation | docker stack deploy --compose-file -