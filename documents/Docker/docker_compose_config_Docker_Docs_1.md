# docker compose config | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/compose/config/
**Word Count:** 855
**Links Count:** 479
**Scraped:** 2025-07-16 01:50:39
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker compose config

Description| Parse, resolve and render compose file in canonical format   ---|---   Usage| `docker compose config [OPTIONS] [SERVICE...]`      ## Description

`docker compose config` renders the actual data model to be applied on the Docker Engine. It merges the Compose files set by `-f` flags, resolves variables in the Compose file, and expands short-notation into the canonical format.

## Options

Option| Default| Description   ---|---|---   `--environment`| | Print environment used for interpolation.   `--format`| | Format the output. Values: \[yaml | json\]   `--hash`| | Print the service config hash, one per line.   `--images`| | Print the image names, one per line.   `--lock-image-digests`| | Produces an override file with image digests   `--networks`| | Print the network names, one per line.   `--no-consistency`| | Don't check model consistency - warning: may produce invalid Compose output      `--no-env-resolution`| | Don't resolve service env files   `--no-interpolate`| | Don't interpolate environment variables   `--no-normalize`| | Don't normalize compose model   `--no-path-resolution`| | Don't resolve file paths   `-o, --output`| | Save to file \(default to stdout\)   `--profiles`| | Print the profile names, one per line.   `-q, --quiet`| | Only validate the configuration, don't print anything   `--resolve-image-digests`| | Pin image tags to digests   `--services`| | Print the service names, one per line.   `--variables`| | Print model variables and default values.   `--volumes`| | Print the volume names, one per line.