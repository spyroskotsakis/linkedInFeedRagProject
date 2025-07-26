# JSONArgsRecommended | Docker Docs

**URL:** https://docs.docker.com/reference/build-checks/json-args-recommended/
**Word Count:** 997
**Links Count:** 489
**Scraped:** 2025-07-16 01:53:28
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# JSONArgsRecommended

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Output               JSON arguments recommended for ENTRYPOINT/CMD to prevent unintended behavior related to OS signals

## Description

`ENTRYPOINT` and `CMD` instructions both support two different syntaxes for arguments:

  * Shell form: `CMD my-cmd start`   * Exec form: `CMD ["my-cmd", "start"]`

When you use shell form, the executable runs as a child process to a shell, which doesn't pass signals. This means that the program running in the container can't detect OS signals like `SIGTERM` and `SIGKILL` and respond to them correctly.

## Examples

â Bad: the `ENTRYPOINT` command doesn't receive OS signals.               FROM alpine     ENTRYPOINT my-program start     # entrypoint becomes: /bin/sh -c my-program start

To make sure the executable can receive OS signals, use the exec form for `CMD` and `ENTRYPOINT`, which lets you run the executable as the main process \(`PID 1`\) in the container, avoiding a shell parent process.

â Good: the `ENTRYPOINT` receives OS signals.               FROM alpine     ENTRYPOINT ["my-program", "start"]     # entrypoint becomes: my-program start

Note that running programs as PID 1 means the program now has the special responsibilities and behaviors associated with PID 1 in Linux, such as reaping child processes.

### Workarounds

There might still be cases when you want to run your containers under a shell. When using exec form, shell features such as variable expansion, piping \(`|`\) and command chaining \(`&&`, `||`, `;`\), are not available. To use such features, you need to use shell form.

Here are some ways you can achieve that. Note that this still means that executables run as child-processes of a shell.

#### Create a wrapper script

You can create an entrypoint script that wraps your startup commands, and execute that script with a JSON-formatted `ENTRYPOINT` command.

â Good: the `ENTRYPOINT` uses JSON format.               FROM alpine     RUN apk add bash     COPY --chmod=755 <<EOT /entrypoint.sh     #!/usr/bin/env bash     set -e     my-background-process &     my-program start     EOT     ENTRYPOINT ["/entrypoint.sh"]

#### Explicitly specify the shell

You can use the [`SHELL`](https://docs.docker.com/reference/dockerfile/#shell) Dockerfile instruction to explicitly specify a shell to use. This will suppress the warning since setting the `SHELL` instruction indicates that using shell form is a conscious decision.

â Good: shell is explicitly defined.               FROM alpine     RUN apk add bash     SHELL ["/bin/bash", "-c"]     ENTRYPOINT echo "hello world"