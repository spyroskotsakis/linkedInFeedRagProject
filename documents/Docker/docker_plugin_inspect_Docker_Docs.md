# docker plugin inspect | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/plugin/inspect
**Word Count:** 808
**Links Count:** 487
**Scraped:** 2025-07-16 01:55:49
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker plugin inspect

Description| Display detailed information on one or more plugins   ---|---   Usage| `docker plugin inspect [OPTIONS] PLUGIN [PLUGIN...]`      ## Description

Returns information about a plugin. By default, this command renders all results in a JSON array.

## Options

Option| Default| Description   ---|---|---   `-f, --format`| | Format output using a custom template:   'json': Print in JSON format   'TEMPLATE': Print output using the given Go template.   Refer to <https://docs.docker.com/go/formatting/> for more information about formatting output with templates      ## Examples

### Inspect a plugin

The following example inspects the `tiborvass/sample-volume-plugin` plugin:               $ docker plugin inspect tiborvass/sample-volume-plugin:latest     

Output is in JSON format \(output below is formatted for readability\):               {       "Id": "8c74c978c434745c3ade82f1bc0acf38d04990eaf494fa507c16d9f1daa99c21",       "Name": "tiborvass/sample-volume-plugin:latest",       "PluginReference": "tiborvas/sample-volume-plugin:latest",       "Enabled": true,       "Config": {         "Mounts": [           {             "Name": "",             "Description": "",             "Settable": null,             "Source": "/data",             "Destination": "/data",             "Type": "bind",             "Options": [               "shared",               "rbind"             ]           },           {             "Name": "",             "Description": "",             "Settable": null,             "Source": null,             "Destination": "/foobar",             "Type": "tmpfs",             "Options": null           }         ],         "Env": [           "DEBUG=1"         ],         "Args": null,         "Devices": null       },       "Manifest": {         "ManifestVersion": "v0",         "Description": "A test plugin for Docker",         "Documentation": "/engine/extend/plugins/",         "Interface": {           "Types": [             "docker.volumedriver/1.0"           ],           "Socket": "plugins.sock"         },         "Entrypoint": [           "plugin-sample-volume-plugin",           "/data"         ],         "Workdir": "",         "User": {         },         "Network": {           "Type": "host"         },         "Capabilities": null,         "Mounts": [           {             "Name": "",             "Description": "",             "Settable": null,             "Source": "/data",             "Destination": "/data",             "Type": "bind",             "Options": [               "shared",               "rbind"             ]           },           {             "Name": "",             "Description": "",             "Settable": null,             "Source": null,             "Destination": "/foobar",             "Type": "tmpfs",             "Options": null           }         ],         "Devices": [           {             "Name": "device",             "Description": "a host device to mount",             "Settable": null,             "Path": "/dev/cpu_dma_latency"           }         ],         "Env": [           {             "Name": "DEBUG",             "Description": "If set, prints debug messages",             "Settable": null,             "Value": "1"           }         ],         "Args": {           "Name": "args",           "Description": "command line arguments",           "Settable": null,           "Value": [                ]         }       }     }

### Format the output \(--format\)               $ docker plugin inspect -f '{{.Id}}' tiborvass/sample-volume-plugin:latest          8c74c978c434745c3ade82f1bc0acf38d04990eaf494fa507c16d9f1daa99c21