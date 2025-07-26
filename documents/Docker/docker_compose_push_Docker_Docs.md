# docker compose push | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/compose/push
**Word Count:** 775
**Links Count:** 479
**Scraped:** 2025-07-16 01:55:49
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker compose push

Description| Push service images   ---|---   Usage| `docker compose push [OPTIONS] [SERVICE...]`      ## Description

Pushes images for services to their respective registry/repository.

The following assumptions are made:

  * You are pushing an image you have built locally   * You have access to the build key

Examples               services:       service1:         build: .         image: localhost:5000/yourimage  ## goes to local registry            service2:         build: .         image: your-dockerid/yourimage  ## goes to your repository on Docker Hub

## Options

Option| Default| Description   ---|---|---   `--ignore-push-failures`| | Push what it can and ignores images with push failures   `--include-deps`| | Also push images of services declared as dependencies   `-q, --quiet`| | Push without printing progress information