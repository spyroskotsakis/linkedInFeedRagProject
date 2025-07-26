# docker image load | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/image/load/
**Word Count:** 1004
**Links Count:** 489
**Scraped:** 2025-07-16 01:51:20
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker image load

Description| Load an image from a tar archive or STDIN   ---|---   Usage| `docker image load [OPTIONS]`   AliasesAn alias is a short or memorable alternative for a longer command.| `docker load`      ## Description

Load an image or repository from a tar archive \(even if compressed with gzip, bzip2, xz or zstd\) from a file or STDIN. It restores both images and tags.

## Options

Option| Default| Description   ---|---|---   `-i, --input`| | Read from tar archive file, instead of STDIN   `--platform`| | API 1.48+ Load only the given platform variant. Formatted as `os[/arch[/variant]]` \(e.g., `linux/amd64`\)      `-q, --quiet`| | Suppress the load output      ## Examples               $ docker image ls          REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE     

### Load images from STDIN               $ docker load < busybox.tar.gz          Loaded image: busybox:latest     $ docker images     REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE     busybox             latest              769b9341d937        7 weeks ago         2.489 MB     

### Load images from a file \(--input\)               $ docker load --input fedora.tar          Loaded image: fedora:rawhide     Loaded image: fedora:20          $ docker images          REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE     busybox             latest              769b9341d937        7 weeks ago         2.489 MB     fedora              rawhide             0d20aec6529d        7 weeks ago         387 MB     fedora              20                  58394af37342        7 weeks ago         385.5 MB     fedora              heisenbug           58394af37342        7 weeks ago         385.5 MB     fedora              latest              58394af37342        7 weeks ago         385.5 MB     

### Load a specific platform \(--platform\)

The `--platform` option allows you to specify which platform variant of the image to load. By default, `docker load` loads all platform variants that are present in the archive. Use the `--platform` option to specify which platform variant of the image to load. An error is produced if the given platform is not present in the archive.

The platform option takes the `os[/arch[/variant]]` format; for example, `linux/amd64` or `linux/arm64/v8`. Architecture and variant are optional, and default to the daemon's native architecture if omitted.

The following example loads the `linux/amd64` variant of an `alpine` image from an archive that contains multiple platform variants.               $ docker image load -i image.tar --platform=linux/amd64     Loaded image: alpine:latest     

The following example attempts to load a `linux/ppc64le` image from an archive, but the given platform is not present in the archive;               $ docker image load -i image.tar --platform=linux/ppc64le     requested platform (linux/ppc64le) not found: image might be filtered out