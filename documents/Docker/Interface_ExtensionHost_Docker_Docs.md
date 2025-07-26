# Interface: ExtensionHost | Docker Docs

**URL:** https://docs.docker.com/reference/api/extensions-sdk/ExtensionHost
**Word Count:** 793
**Links Count:** 483
**Scraped:** 2025-07-16 01:55:27
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# Interface: ExtensionHost

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

Executes a command in the host.

For example, execute the shipped binary `kubectl -h` command in the host:               await ddClient.extension.host.cli.exec("kubectl", ["-h"]);

* * *

Streams the output of the command executed in the backend container or in the host.

Provided the `kubectl` binary is shipped as part of your extension, you can spawn the `kubectl -h` command in the host:               await ddClient.extension.host.cli.exec("kubectl", ["-h"], {                stream: {                  onOutput(data): void {                      // As we can receive both `stdout` and `stderr`, we wrap them in a JSON object                      JSON.stringify(                        {                          stdout: data.stdout,                          stderr: data.stderr,                        },                        null,                        "  "                      );                  },                  onError(error: any): void {                    console.error(error);                  },                  onClose(exitCode: number): void {                    console.log("onClose with exit code " + exitCode);                  },                },              });