# docker image inspect | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/image/inspect
**Word Count:** 788
**Links Count:** 480
**Scraped:** 2025-07-16 01:55:27
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker image inspect

Description| Display detailed information on one or more images   ---|---   Usage| `docker image inspect [OPTIONS] IMAGE [IMAGE...]`      ## Description

Display detailed information on one or more images

## Options

Option| Default| Description   ---|---|---   `-f, --format`| | Format output using a custom template:   'json': Print in JSON format   'TEMPLATE': Print output using the given Go template.   Refer to <https://docs.docker.com/go/formatting/> for more information about formatting output with templates   `--platform`| | API 1.49+ Inspect a specific platform of the multi-platform image.   If the image or the server is not multi-platform capable, the command will error out if the platform does not match.   'os\[/arch\[/variant\]\]': Explicit platform \(eg. linux/amd64\)