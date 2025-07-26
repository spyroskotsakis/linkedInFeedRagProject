# windowsfilter storage driver | Docker Docs

**URL:** https://docs.docker.com/engine/storage/drivers/windowsfilter-driver
**Word Count:** 1156
**Links Count:** 645
**Scraped:** 2025-07-16 02:00:24
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# windowsfilter storage driver

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

The windowsfilter storage driver is the default storage driver for Docker Engine on Windows. The windowsfilter driver uses Windows-native file system layers to for storing Docker layers and volume data on disk. The windowsfilter storage driver only works on file systems formatted with NTFS.

## Configure the windowsfilter storage driver

For most use case, no configuring the windowsfilter storage driver is not necessary.

The default storage limit for Docker Engine on Windows is 127GB. To use a different storage size, set the `size` option for the windowsfilter storage driver. See [windowsfilter options](https://docs.docker.com/reference/cli/dockerd/#windowsfilter-options).

Data is stored on the Docker host in `image` and `windowsfilter` subdirectories within `C:\ProgramData\docker` by default. You can change the storage location by configuring the `data-root` option in the [Daemon configuration file](https://docs.docker.com/reference/cli/dockerd/#on-windows):               {       "data-root": "d:\\docker"     }

You must restart the daemon for the configuration change to take effect.

## Additional information

For more information about how container storage works on Windows, refer to Microsoft's [Containers on Windows documentation](https://learn.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/container-storage).