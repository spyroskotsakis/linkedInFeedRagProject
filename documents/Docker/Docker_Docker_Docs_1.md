# Docker | Docker Docs

**URL:** https://docs.docker.com/extensions/extensions-sdk/dev/api/docker
**Word Count:** 1297
**Links Count:** 646
**Scraped:** 2025-07-16 01:58:59
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Docker

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Docker objects

â¸ **listContainers**\(`options?`\): `Promise`<`unknown`>

To get the list of containers:               const containers = await ddClient.docker.listContainers();

â¸ **listImages**\(`options?`\): `Promise`<`unknown`>

To get the list of local container images:               const images = await ddClient.docker.listImages();

See the [Docker API reference](https://docs.docker.com/reference/api/extensions-sdk/Docker/) for details about these methods.

> Deprecated access to Docker objects >  > The methods below are deprecated and will be removed in a future version. Use the methods specified above.               const containers = await window.ddClient.listContainers();          const images = await window.ddClient.listImages();

## Docker commands

Extensions can also directly execute the `docker` command line.

â¸ **exec**\(`cmd`, `args`\): `Promise`< [`ExecResult`](https://docs.docker.com/reference/api/extensions-sdk/ExecResult/)>               const result = await ddClient.docker.cli.exec("info", [       "--format",       '"{{ json . }}"',     ]);

The result contains both the standard output and the standard error of the executed command:               {       "stderr": "...",       "stdout": "..."     }

In this example, the command output is JSON. For convenience, the command result object also has methods to easily parse it:

  * `result.lines(): string[]` splits output lines.   * `result.parseJsonObject(): any` parses a well-formed json output.   * `result.parseJsonLines(): any[]` parses each output line as a json object.

â¸ **exec**\(`cmd`, `args`, `options`\): `void`

The command above streams the output as a result of the execution of a Docker command. This is useful if you need to get the output as a stream or the output of the command is too long.               await ddClient.docker.cli.exec("logs", ["-f", "..."], {       stream: {         onOutput(data) {           if (data.stdout) {             console.error(data.stdout);           } else {             console.log(data.stderr);           }         },         onError(error) {           console.error(error);         },         onClose(exitCode) {           console.log("onClose with exit code " + exitCode);         },         splitOutputLines: true,       },     });

The child process created by the extension is killed \(`SIGTERM`\) automatically when you close the dashboard in Docker Desktop or when you exit the extension UI. If needed, you can also use the result of the `exec(streamOptions)` call in order to kill \(`SIGTERM`\) the process.               const logListener = await ddClient.docker.cli.exec("logs", ["-f", "..."], {       stream: {         // ...       },     });          // when done listening to logs or before starting a new one, kill the process     logListener.close();

This `exec(streamOptions)` API can also be used to listen to docker events:               await ddClient.docker.cli.exec(       "events",       ["--format", "{{ json . }}", "--filter", "container=my-container"],       {         stream: {           onOutput(data) {             if (data.stdout) {               const event = JSON.parse(data.stdout);               console.log(event);             } else {               console.log(data.stderr);             }           },           onClose(exitCode) {             console.log("onClose with exit code " + exitCode);           },           splitOutputLines: true,         },       }     );

> Note >  > You cannot use this to chain commands in a single `exec()` invocation \(like `docker kill $(docker ps -q)` or using pipe between commands\). >  > You need to invoke `exec()` for each command and parse results to pass parameters to the next command if needed.

See the [Exec API reference](https://docs.docker.com/reference/api/extensions-sdk/Exec/) for details about these methods.

> Deprecated execution of Docker commands >  > This method is deprecated and will be removed in a future version. Use the one specified just below.               const output = await window.ddClient.execDockerCmd(       "info",       "--format",       '"{{ json . }}"'     );          window.ddClient.spawnDockerCmd("logs", ["-f", "..."], (data, error) => {       console.log(data.stdout);     });