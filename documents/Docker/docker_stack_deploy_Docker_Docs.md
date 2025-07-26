# docker stack deploy | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/stack/deploy
**Word Count:** 979
**Links Count:** 485
**Scraped:** 2025-07-16 01:55:27
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker stack deploy

Description| Deploy a new stack or update an existing stack   ---|---   Usage| `docker stack deploy [OPTIONS] STACK`   AliasesAn alias is a short or memorable alternative for a longer command.| `docker stack up`      Swarm This command works with the Swarm orchestrator.

## Description

Create and update a stack from a `compose` file on the swarm.

> Note >  > This is a cluster management command, and must be executed on a swarm manager node. To learn about managers and workers, refer to the [Swarm mode section](https://docs.docker.com/engine/swarm/) in the documentation.

## Options

Option| Default| Description   ---|---|---   `-c, --compose-file`| | API 1.25+ Path to a Compose file, or `-` to read from stdin   `-d, --detach`| `true`| Exit immediately instead of waiting for the stack services to converge      `--prune`| | API 1.27+ Prune services that are no longer referenced   `-q, --quiet`| | Suppress progress output   `--resolve-image`| `always`| API 1.30+ Query the registry to resolve image digest and supported platforms \(`always`, `changed`, `never`\)      `--with-registry-auth`| | Send registry authentication details to Swarm agents      ## Examples

### Compose file \(--compose-file\)

The `deploy` command supports Compose file version `3.0` and above.               $ docker stack deploy --compose-file docker-compose.yml vossibility          Ignoring unsupported options: links          Creating network vossibility_vossibility     Creating network vossibility_default     Creating service vossibility_nsqd     Creating service vossibility_logstash     Creating service vossibility_elasticsearch     Creating service vossibility_kibana     Creating service vossibility_ghollector     Creating service vossibility_lookupd     

The Compose file can also be provided as standard input with `--compose-file -`:               $ cat docker-compose.yml | docker stack deploy --compose-file - vossibility          Ignoring unsupported options: links          Creating network vossibility_vossibility     Creating network vossibility_default     Creating service vossibility_nsqd     Creating service vossibility_logstash     Creating service vossibility_elasticsearch     Creating service vossibility_kibana     Creating service vossibility_ghollector     Creating service vossibility_lookupd     

If your configuration is split between multiple Compose files, e.g. a base configuration and environment-specific overrides, you can provide multiple `--compose-file` flags.               $ docker stack deploy --compose-file docker-compose.yml -c docker-compose.prod.yml vossibility          Ignoring unsupported options: links          Creating network vossibility_vossibility     Creating network vossibility_default     Creating service vossibility_nsqd     Creating service vossibility_logstash     Creating service vossibility_elasticsearch     Creating service vossibility_kibana     Creating service vossibility_ghollector     Creating service vossibility_lookupd     

You can verify that the services were correctly created:               $ docker service ls          ID            NAME                               MODE        REPLICAS  IMAGE     29bv0vnlm903  vossibility_lookupd                replicated  1/1       nsqio/nsq@sha256:eeba05599f31eba418e96e71e0984c3dc96963ceb66924dd37a47bf7ce18a662     4awt47624qwh  vossibility_nsqd                   replicated  1/1       nsqio/nsq@sha256:eeba05599f31eba418e96e71e0984c3dc96963ceb66924dd37a47bf7ce18a662     4tjx9biia6fs  vossibility_elasticsearch          replicated  1/1       elasticsearch@sha256:12ac7c6af55d001f71800b83ba91a04f716e58d82e748fa6e5a7359eed2301aa     7563uuzr9eys  vossibility_kibana                 replicated  1/1       kibana@sha256:6995a2d25709a62694a937b8a529ff36da92ebee74bafd7bf00e6caf6db2eb03     9gc5m4met4he  vossibility_logstash               replicated  1/1       logstash@sha256:2dc8bddd1bb4a5a34e8ebaf73749f6413c101b2edef6617f2f7713926d2141fe     axqh55ipl40h  vossibility_vossibility-collector  replicated  1/1       icecrime/vossibility-collector@sha256:f03f2977203ba6253988c18d04061c5ec7aab46bca9dfd89a9a1fa4500989fba