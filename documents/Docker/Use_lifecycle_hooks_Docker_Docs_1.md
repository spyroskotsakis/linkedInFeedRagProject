# Use lifecycle hooks | Docker Docs

**URL:** https://docs.docker.com/compose/how-tos/lifecycle/
**Word Count:** 1257
**Links Count:** 651
**Scraped:** 2025-07-16 01:47:29
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Using lifecycle hooks with Compose

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Requires: Docker Compose [2.30.0](https://docs.docker.com/compose/releases/release-notes/#2300) and later

## Services lifecycle hooks

When Docker Compose runs a container, it uses two elements, [ENTRYPOINT and COMMAND](https://docs.docker.com/engine/containers/run/#default-command-and-options), to manage what happens when the container starts and stops.

However, it can sometimes be easier to handle these tasks separately with lifecycle hooks - commands that run right after the container starts or just before it stops.

Lifecycle hooks are particularly useful because they can have special privileges \(like running as the root user\), even when the container itself runs with lower privileges for security. This means that certain tasks requiring higher permissions can be done without compromising the overall security of the container.

### Post-start hooks

Post-start hooks are commands that run after the container has started, but there's no set time for when exactly they will execute. The hook execution timing is not assured during the execution of the container's `entrypoint`.

In the example provided:

  * The hook is used to change the ownership of a volume to a non-root user \(because volumes are created with root ownership by default\).   * After the container starts, the `chown` command changes the ownership of the `/data` directory to user `1001`.

              services:       app:         image: backend         user: 1001         volumes:           - data:/data             post_start:           - command: chown -R /data 1001:1001             user: root          volumes:       data: {} # a Docker volume is created with root ownership

### Pre-stop hooks

Pre-stop hooks are commands that run before the container is stopped by a specific command \(like `docker compose down` or stopping it manually with `Ctrl+C`\). These hooks won't run if the container stops by itself or gets killed suddenly.

In the following example, before the container stops, the `./data_flush.sh` script is run to perform any necessary cleanup.               services:       app:         image: backend         pre_stop:           - command: ./data_flush.sh

## Reference information

  * [`post_start`](https://docs.docker.com/reference/compose-file/services/#post_start)   * [`pre_stop`](https://docs.docker.com/reference/compose-file/services/#pre_stop)