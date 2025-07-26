# containerd image store | Docker Docs

**URL:** https://docs.docker.com/engine/storage/containerd
**Word Count:** 1178
**Links Count:** 639
**Scraped:** 2025-07-16 02:02:47
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# containerd image store with Docker Engine

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Availability: Experimental 

containerd, the industry-standard container runtime, uses snapshotters instead of the classic storage drivers for storing image and container data. While the `overlay2` driver still remains the default driver for Docker Engine, you can opt in to using containerd snapshotters as an experimental feature.

To learn more about the containerd image store and its benefits, refer to [containerd image store on Docker Desktop](https://docs.docker.com/desktop/features/containerd/).

## Enable containerd image store on Docker Engine

Switching to containerd snapshotters causes you to temporarily lose images and containers created using the classic storage drivers. Those resources still exist on your filesystem, and you can retrieve them by turning off the containerd snapshotters feature.

The following steps explain how to enable the containerd snapshotters feature.

  1. Add the following configuration to your `/etc/docker/daemon.json` configuration file:                    {            "features": {              "containerd-snapshotter": true            }          }

  2. Save the file.

  3. Restart the daemon for the changes to take effect.                    $ sudo systemctl restart docker          

After restarting the daemon, running `docker info` shows that you're using containerd snapshotter storage drivers.               $ docker info -f '{{ .DriverStatus }}'     [[driver-type io.containerd.snapshotter.v1]]     

Docker Engine uses the `overlayfs` containerd snapshotter by default.