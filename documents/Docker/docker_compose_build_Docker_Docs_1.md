# docker compose build | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/compose/build/
**Word Count:** 825
**Links Count:** 481
**Scraped:** 2025-07-16 01:50:39
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker compose build

Description| Build or rebuild services   ---|---   Usage| `docker compose build [OPTIONS] [SERVICE...]`      ## Description

Services are built once and then tagged, by default as `project-service`.

If the Compose file specifies an [image](https://github.com/compose-spec/compose-spec/blob/main/spec.md#image) name, the image is tagged with that name, substituting any variables beforehand. See [variable interpolation](https://github.com/compose-spec/compose-spec/blob/main/spec.md#interpolation).

If you change a service's `Dockerfile` or the contents of its build directory, run `docker compose build` to rebuild it.

## Options

Option| Default| Description   ---|---|---   `--build-arg`| | Set build-time variables for services   `--builder`| | Set builder to use   `--check`| | Check build configuration   `-m, --memory`| | Set memory limit for the build container. Not supported by BuildKit.      `--no-cache`| | Do not use cache when building the image   `--print`| | Print equivalent bake file   `--pull`| | Always attempt to pull a newer version of the image   `--push`| | Push service images   `-q, --quiet`| | Don't print anything to STDOUT   `--ssh`| | Set SSH authentications used when building service images. \(use 'default' for using your default SSH Agent\)      `--with-dependencies`| | Also build dependencies \(transitively\)