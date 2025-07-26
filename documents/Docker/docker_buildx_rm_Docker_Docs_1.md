# docker buildx rm | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/buildx/rm/
**Word Count:** 884
**Links Count:** 499
**Scraped:** 2025-07-16 01:50:20
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker buildx rm

Description| Remove one or more builder instances   ---|---   Usage| `docker buildx rm [OPTIONS] [NAME...]`      ## Description

Removes the specified or current builder. It is a no-op attempting to remove the default builder.

## Options

Option| Default| Description   ---|---|---   `--all-inactive`| | Remove all inactive builders   `-f, --force`| | Do not prompt for confirmation   `--keep-daemon`| | Keep the BuildKit daemon running   `--keep-state`| | Keep BuildKit state      ## Examples

### Remove all inactive builders \(--all-inactive\)

Remove builders that are not in running state.               $ docker buildx rm --all-inactive     WARNING! This will remove all builders that are not in running state. Are you sure you want to continue? [y/N] y     

### Override the configured builder instance \(--builder\)

Same as [`buildx --builder`](https://docs.docker.com/reference/cli/docker/buildx/#builder).

### Do not prompt for confirmation \(--force\)

Do not prompt for confirmation before removing inactive builders.               $ docker buildx rm --all-inactive --force     

### Keep the BuildKit daemon running \(--keep-daemon\)

Keep the BuildKit daemon running after the buildx context is removed. This is useful when you manage BuildKit daemons and buildx contexts independently. Only supported by the [`docker-container`](https://docs.docker.com/build/drivers/docker-container/) and [`kubernetes`](https://docs.docker.com/build/drivers/kubernetes/) drivers.

### Keep BuildKit state \(--keep-state\)

Keep BuildKit state, so it can be reused by a new builder with the same name. Currently, only supported by the [`docker-container` driver](https://docs.docker.com/build/drivers/docker-container/).