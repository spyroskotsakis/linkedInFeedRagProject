# docker scout push | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/scout/push/
**Word Count:** 798
**Links Count:** 483
**Scraped:** 2025-07-16 01:52:00
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker scout push

Description| Push an image or image index to Docker Scout   ---|---   Usage| `docker scout push IMAGE`      ## Description

The `docker scout push` command lets you push an image or analysis result to Docker Scout.

## Options

Option| Default| Description   ---|---|---   `--author`| | Name of the author of the image   `--dry-run`| | Do not push the image but process it   `--org`| | Namespace of the Docker organization to which image will be pushed   `-o, --output`| | Write the report to a file   `--platform`| | Platform of image to be pushed   `--sbom`| | Create and upload SBOMs   `--secrets`| | Scan for secrets in the image   `--timestamp`| | Timestamp of image or tag creation      ## Examples

### Push an image to Docker Scout               $ docker scout push --org my-org registry.example.com/repo:tag