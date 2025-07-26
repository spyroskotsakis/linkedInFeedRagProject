# docker network inspect | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/network/inspect/
**Word Count:** 770
**Links Count:** 480
**Scraped:** 2025-07-16 01:51:40
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker network inspect

Description| Display detailed information on one or more networks   ---|---   Usage| `docker network inspect [OPTIONS] NETWORK [NETWORK...]`      ## Description

Returns information about one or more networks. By default, this command renders all results in a JSON object.

## Options

Option| Default| Description   ---|---|---   `-f, --format`| | Format output using a custom template:   'json': Print in JSON format   'TEMPLATE': Print output using the given Go template.   Refer to <https://docs.docker.com/go/formatting/> for more information about formatting output with templates   `-v, --verbose`| | Verbose output for diagnostics