# docker context inspect | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/context/inspect
**Word Count:** 777
**Links Count:** 484
**Scraped:** 2025-07-16 01:56:12
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker context inspect

Description| Display detailed information on one or more contexts   ---|---   Usage| `docker context inspect [OPTIONS] [CONTEXT] [CONTEXT...]`      ## Description

Inspects one or more contexts.

## Options

Option| Default| Description   ---|---|---   `-f, --format`| | Format output using a custom template:   'json': Print in JSON format   'TEMPLATE': Print output using the given Go template.   Refer to <https://docs.docker.com/go/formatting/> for more information about formatting output with templates      ## Examples

### Inspect a context by name               $ docker context inspect "local+aks"          [       {         "Name": "local+aks",         "Metadata": {           "Description": "Local Docker Engine",           "StackOrchestrator": "swarm"         },         "Endpoints": {           "docker": {             "Host": "npipe:////./pipe/docker_engine",             "SkipTLSVerify": false           }         },         "TLSMaterial": {},         "Storage": {           "MetadataPath": "C:\\Users\\simon\\.docker\\contexts\\meta\\cb6d08c0a1bfa5fe6f012e61a442788c00bed93f509141daff05f620fc54ddee",           "TLSPath": "C:\\Users\\simon\\.docker\\contexts\\tls\\cb6d08c0a1bfa5fe6f012e61a442788c00bed93f509141daff05f620fc54ddee"         }       }     ]