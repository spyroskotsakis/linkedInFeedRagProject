# docker plugin enable | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/plugin/enable/
**Word Count:** 778
**Links Count:** 482
**Scraped:** 2025-07-16 01:51:40
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker plugin enable

Description| Enable a plugin   ---|---   Usage| `docker plugin enable [OPTIONS] PLUGIN`      ## Description

Enables a plugin. The plugin must be installed before it can be enabled, see [`docker plugin install`](https://docs.docker.com/reference/cli/docker/plugin/install/).

## Options

Option| Default| Description   ---|---|---   `--timeout`| `30`| HTTP client timeout \(in seconds\)      ## Examples

The following example shows that the `sample-volume-plugin` plugin is installed, but disabled:               $ docker plugin ls          ID            NAME                                    DESCRIPTION                ENABLED     69553ca1d123  tiborvass/sample-volume-plugin:latest   A test plugin for Docker   false     

To enable the plugin, use the following command:               $ docker plugin enable tiborvass/sample-volume-plugin          tiborvass/sample-volume-plugin          $ docker plugin ls          ID            NAME                                    DESCRIPTION                ENABLED     69553ca1d123  tiborvass/sample-volume-plugin:latest   A test plugin for Docker   true