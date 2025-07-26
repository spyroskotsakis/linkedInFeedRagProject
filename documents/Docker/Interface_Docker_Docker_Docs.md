# Interface: Docker | Docker Docs

**URL:** https://docs.docker.com/reference/api/extensions-sdk/Docker
**Word Count:** 892
**Links Count:** 499
**Scraped:** 2025-07-16 01:55:05
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# Interface: Docker

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

â¢ `Readonly` **cli** : [`DockerCommand`](https://docs.docker.com/reference/api/extensions-sdk/DockerCommand/)

You can also directly execute the Docker binary.               const output = await ddClient.docker.cli.exec("volume", [       "ls",       "--filter",       "dangling=true"     ]);

Output:               {       "stderr": "...",       "stdout": "..."     }

For convenience, the command result object also has methods to easily parse it depending on output format. See [ExecResult](https://docs.docker.com/reference/api/extensions-sdk/ExecResult/) instead.

* * *

Streams the output as a result of the execution of a Docker command. It is useful when the output of the command is too long, or you need to get the output as a stream.               await ddClient.docker.cli.exec("logs", ["-f", "..."], {       stream: {         onOutput(data): void {             // As we can receive both `stdout` and `stderr`, we wrap them in a JSON object             JSON.stringify(               {                 stdout: data.stdout,                 stderr: data.stderr,               },               null,               "  "             );         },         onError(error: any): void {           console.error(error);         },         onClose(exitCode: number): void {           console.log("onClose with exit code " + exitCode);         },       },     });

## Methods

### listContainers

â¸ **listContainers**\(`options?`\): `Promise`<`unknown`>

Get the list of running containers \(same as `docker ps`\).

By default, this will not list stopped containers. You can use the option `{"all": true}` to list all the running and stopped containers.               const containers = await ddClient.docker.listContainers();

#### Parameters

Name| Type| Description   ---|---|---   `options?`| `any`| \(Optional\). A JSON like `{ "all": true, "limit": 10, "size": true, "filters": JSON.stringify({ status: ["exited"] }), }` For more information about the different properties see [the Docker API endpoint documentation](https://docs.docker.com/engine/api/v1.41/#operation/ContainerList).      #### Returns

`Promise`<`unknown`>

* * *

### listImages

â¸ **listImages**\(`options?`\): `Promise`<`unknown`>

Get the list of local container images               const images = await ddClient.docker.listImages();

#### Parameters

Name| Type| Description   ---|---|---   `options?`| `any`| \(Optional\). A JSON like `{ "all": true, "filters": JSON.stringify({ dangling: ["true"] }), "digests": true * }` For more information about the different properties see [the Docker API endpoint documentation](https://docs.docker.com/engine/api/v1.41/#tag/Image).      #### Returns

`Promise`<`unknown`>