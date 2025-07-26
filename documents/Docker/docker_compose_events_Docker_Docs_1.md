# docker compose events | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/compose/events/
**Word Count:** 758
**Links Count:** 480
**Scraped:** 2025-07-16 01:50:39
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker compose events

Description| Receive real time events from containers   ---|---   Usage| `docker compose events [OPTIONS] [SERVICE...]`      ## Description

Stream container events for every container in the project.

With the `--json` flag, a json object is printed one per line with the format:               {         "time": "2015-11-20T18:01:03.615550",         "type": "container",         "action": "create",         "id": "213cf7...5fc39a",         "service": "web",         "attributes": {           "name": "application_web_1",           "image": "alpine:edge"         }     }

The events that can be received using this can be seen [here](https://docs.docker.com/reference/cli/docker/system/events/#object-types).

## Options

Option| Default| Description   ---|---|---   `--json`| | Output events as a stream of json objects