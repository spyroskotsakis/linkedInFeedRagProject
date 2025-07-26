# docker plugin set | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/plugin/set/
**Word Count:** 879
**Links Count:** 487
**Scraped:** 2025-07-16 01:51:40
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker plugin set

Description| Change settings for a plugin   ---|---   Usage| `docker plugin set PLUGIN KEY=VALUE [KEY=VALUE...]`      ## Description

Change settings for a plugin. The plugin must be disabled.

The settings currently supported are:

  * env variables   * source of mounts   * path of devices   * args

## Examples

### Change an environment variable

The following example change the env variable `DEBUG` on the `sample-volume-plugin` plugin.               $ docker plugin inspect -f {{.Settings.Env}} tiborvass/sample-volume-plugin     [DEBUG=0]          $ docker plugin set tiborvass/sample-volume-plugin DEBUG=1          $ docker plugin inspect -f {{.Settings.Env}} tiborvass/sample-volume-plugin     [DEBUG=1]     

### Change the source of a mount

The following example change the source of the `mymount` mount on the `myplugin` plugin.               $ docker plugin inspect -f '{{with $mount := index .Settings.Mounts 0}}{{$mount.Source}}{{end}}' myplugin     /foo          $ docker plugins set myplugin mymount.source=/bar          $ docker plugin inspect -f '{{with $mount := index .Settings.Mounts 0}}{{$mount.Source}}{{end}}' myplugin     /bar     

> Note >  > Since only `source` is settable in `mymount`, `docker plugins set mymount=/bar myplugin` would work too.

### Change a device path

The following example change the path of the `mydevice` device on the `myplugin` plugin.               $ docker plugin inspect -f '{{with $device := index .Settings.Devices 0}}{{$device.Path}}{{end}}' myplugin          /dev/foo          $ docker plugins set myplugin mydevice.path=/dev/bar          $ docker plugin inspect -f '{{with $device := index .Settings.Devices 0}}{{$device.Path}}{{end}}' myplugin          /dev/bar     

> Note >  > Since only `path` is settable in `mydevice`, `docker plugins set mydevice=/dev/bar myplugin` would work too.

### Change the source of the arguments

The following example change the value of the args on the `myplugin` plugin.               $ docker plugin inspect -f '{{.Settings.Args}}' myplugin          ["foo", "bar"]          $ docker plugins set myplugin myargs="foo bar baz"          $ docker plugin inspect -f '{{.Settings.Args}}' myplugin          ["foo", "bar", "baz"]