# docker context update | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/context/update
**Word Count:** 741
**Links Count:** 484
**Scraped:** 2025-07-16 01:56:56
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker context update

Description| Update a context   ---|---   Usage| `docker context update [OPTIONS] CONTEXT`      ## Description

Updates an existing `context`. See [context create](https://docs.docker.com/reference/cli/docker/context/create/).

## Options

Option| Default| Description   ---|---|---   `--description`| | Description of the context   `--docker`| | set the docker endpoint      ## Examples

### Update an existing context               $ docker context update \         --description "some description" \         --docker "host=tcp://myserver:2376,ca=~/ca-file,cert=~/cert-file,key=~/key-file" \         my-context