# docker container kill | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/container/kill/
**Word Count:** 953
**Links Count:** 487
**Scraped:** 2025-07-16 01:50:59
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker container kill

Description| Kill one or more running containers   ---|---   Usage| `docker container kill [OPTIONS] CONTAINER [CONTAINER...]`   AliasesAn alias is a short or memorable alternative for a longer command.| `docker kill`      ## Description

The `docker kill` subcommand kills one or more containers. The main process inside the container is sent `SIGKILL` signal \(default\), or the signal that is specified with the `--signal` option. You can reference a container by its ID, ID-prefix, or name.

The `--signal` flag sets the system call signal that is sent to the container. This signal can be a signal name in the format `SIG<NAME>`, for instance `SIGINT`, or an unsigned number that matches a position in the kernel's syscall table, for instance `2`.

While the default \(`SIGKILL`\) signal will terminate the container, the signal set through `--signal` may be non-terminal, depending on the container's main process. For example, the `SIGHUP` signal in most cases will be non-terminal, and the container will continue running after receiving the signal.

> Note >  > `ENTRYPOINT` and `CMD` in the _shell_ form run as a child process of `/bin/sh -c`, which does not pass signals. This means that the executable is not the containerâs PID 1 and does not receive Unix signals.

## Options

Option| Default| Description   ---|---|---   `-s, --signal`| | Signal to send to the container      ## Examples

### Send a KILL signal to a container

The following example sends the default `SIGKILL` signal to the container named `my_container`:               $ docker kill my_container     

### Send a custom signal to a container \(--signal\)

The following example sends a `SIGHUP` signal to the container named `my_container`:               $ docker kill --signal=SIGHUP  my_container     

You can specify a custom signal either by _name_ , or _number_. The `SIG` prefix is optional, so the following examples are equivalent:               $ docker kill --signal=SIGHUP my_container     $ docker kill --signal=HUP my_container     $ docker kill --signal=1 my_container     

Refer to the [`signal(7)`](https://man7.org/linux/man-pages/man7/signal.7.html) man-page for a list of standard Linux signals.