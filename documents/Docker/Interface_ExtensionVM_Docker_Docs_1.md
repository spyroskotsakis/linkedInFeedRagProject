# Interface: ExtensionVM | Docker Docs

**URL:** https://docs.docker.com/reference/api/extensions-sdk/ExtensionVM/
**Word Count:** 829
**Links Count:** 487
**Scraped:** 2025-07-16 01:53:07
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# Interface: ExtensionVM

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

**`Since`**

0.2.0

## Properties

### cli

â¢ `Readonly` **cli** : [`ExtensionCli`](https://docs.docker.com/reference/api/extensions-sdk/ExtensionCli/)

Executes a command in the backend container.

Example: Execute the command `ls -l` inside the backend container:               await ddClient.extension.vm.cli.exec(       "ls",       ["-l"]     );

Streams the output of the command executed in the backend container.

When the extension defines its own `compose.yaml` file with multiple containers, the command is executed on the first container defined. Change the order in which containers are defined to execute commands on another container.

Example: Spawn the command `ls -l` inside the backend container:               await ddClient.extension.vm.cli.exec("ls", ["-l"], {                stream: {                  onOutput(data): void {                      // As we can receive both `stdout` and `stderr`, we wrap them in a JSON object                      JSON.stringify(                        {                          stdout: data.stdout,                          stderr: data.stderr,                        },                        null,                        "  "                      );                  },                  onError(error: any): void {                    console.error(error);                  },                  onClose(exitCode: number): void {                    console.log("onClose with exit code " + exitCode);                  },                },              });

**`Param`**

Command to execute.

**`Param`**

Arguments of the command to execute.

**`Param`**

The callback function where to listen from the command output data and errors.

* * *

### service

â¢ `Optional` `Readonly` **service** : [`HttpService`](https://docs.docker.com/reference/api/extensions-sdk/HttpService/)