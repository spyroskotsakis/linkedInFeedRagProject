# Interface: DockerDesktopClient | Docker Docs

**URL:** https://docs.docker.com/reference/api/extensions-sdk/DockerDesktopClient/
**Word Count:** 1508
**Links Count:** 652
**Scraped:** 2025-07-16 01:53:07
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# Interface: DockerDesktopClient

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

An amalgam of the v0 and v1 interfaces of the Docker Desktop API client, provided for backwards compatibility reasons. Unless you're working with a legacy extension, use the v1 type instead.

## Properties

### backend

â¢ `Readonly` **backend** : `undefined` | [`BackendV0`](https://docs.docker.com/reference/api/extensions-sdk/BackendV0/)

The `window.ddClient.backend` object can be used to communicate with the backend defined in the vm section of the extension metadata. The client is already connected to the backend.

> Warning >  > It will be removed in a future version. Use [extension](https://docs.docker.com/reference/api/extensions-sdk/DockerDesktopClient/#extension) instead.

#### Inherited from

DockerDesktopClientV0.backend

* * *

### extension

â¢ `Readonly` **extension** : [`Extension`](https://docs.docker.com/reference/api/extensions-sdk/Extension/)

The `ddClient.extension` object can be used to communicate with the backend defined in the vm section of the extension metadata. The client is already connected to the backend.

#### Inherited from

DockerDesktopClientV1.extension

* * *

### desktopUI

â¢ `Readonly` **desktopUI** : [`DesktopUI`](https://docs.docker.com/reference/api/extensions-sdk/DesktopUI/)

#### Inherited from

DockerDesktopClientV1.desktopUI

* * *

### host

â¢ `Readonly` **host** : [`Host`](https://docs.docker.com/reference/api/extensions-sdk/Host/)

#### Inherited from

DockerDesktopClientV1.host

* * *

### docker

â¢ `Readonly` **docker** : [`Docker`](https://docs.docker.com/reference/api/extensions-sdk/Docker/)

#### Inherited from

DockerDesktopClientV1.docker

## Container Methods

### listContainers

â¸ **listContainers**\(`options`\): `Promise`<`unknown`>

Get the list of running containers \(same as `docker ps`\).

By default, this will not list stopped containers. You can use the option `{"all": true}` to list all the running and stopped containers.               const containers = await window.ddClient.listContainers();

> Warning >  > It will be removed in a future version. Use [listContainers](https://docs.docker.com/reference/api/extensions-sdk/Docker/#listcontainers) instead.

#### Parameters

Name| Type| Description   ---|---|---   `options`| `never`| \(Optional\). A JSON like `{ "all": true, "limit": 10, "size": true, "filters": JSON.stringify({ status: ["exited"] }), }` For more information about the different properties see [the Docker API endpoint documentation](https://docs.docker.com/engine/api/v1.41/#operation/ContainerList).      #### Returns

`Promise`<`unknown`>

#### Inherited from

DockerDesktopClientV0.listContainers

* * *

## Image Methods

### listImages

â¸ **listImages**\(`options`\): `Promise`<`unknown`>

Get the list of images               const images = await window.ddClient.listImages();

> Warning >  > It will be removed in a future version. Use [listImages](https://docs.docker.com/reference/api/extensions-sdk/Docker/#listimages) instead.

#### Parameters

Name| Type| Description   ---|---|---   `options`| `never`| \(Optional\). A JSON like `{ "all": true, "filters": JSON.stringify({ dangling: ["true"] }), "digests": true }` For more information about the different properties see [the Docker API endpoint documentation](https://docs.docker.com/engine/api/v1.41/#tag/Image).      #### Returns

`Promise`<`unknown`>

#### Inherited from

DockerDesktopClientV0.listImages

* * *

## Navigation Methods

### navigateToContainers

â¸ **navigateToContainers**\(\): `void`

Navigate to the container's window in Docker Desktop.               window.ddClient.navigateToContainers();

> Warning >  > It will be removed in a future version. Use [viewContainers](https://docs.docker.com/reference/api/extensions-sdk/NavigationIntents/#viewcontainers) instead.

#### Returns

`void`

#### Inherited from

DockerDesktopClientV0.navigateToContainers

* * *

### navigateToContainer

â¸ **navigateToContainer**\(`id`\): `Promise`<`any`>

Navigate to the container window in Docker Desktop.               await window.ddClient.navigateToContainer(id);

> Warning >  > It will be removed in a future version.

#### Parameters

Name| Type| Description   ---|---|---   `id`| `string`| The full container id, e.g. `46b57e400d801762e9e115734bf902a2450d89669d85881058a46136520aca28`. You can use the `--no-trunc` flag as part of the `docker ps` command to display the full container id.      #### Returns

`Promise`<`any`>

A promise that fails if the container doesn't exist.

#### Inherited from

DockerDesktopClientV0.navigateToContainer

* * *

### navigateToContainerLogs

â¸ **navigateToContainerLogs**\(`id`\): `Promise`<`any`>

Navigate to the container logs window in Docker Desktop.               await window.ddClient.navigateToContainerLogs(id);

> Warning >  > It will be removed in a future version.

#### Parameters

Name| Type| Description   ---|---|---   `id`| `string`| The full container id, e.g. `46b57e400d801762e9e115734bf902a2450d89669d85881058a46136520aca28`. You can use the `--no-trunc` flag as part of the `docker ps` command to display the full container id.      #### Returns

`Promise`<`any`>

A promise that fails if the container doesn't exist.

#### Inherited from

DockerDesktopClientV0.navigateToContainerLogs

* * *

### navigateToContainerInspect

â¸ **navigateToContainerInspect**\(`id`\): `Promise`<`any`>

Navigate to the container inspect window in Docker Desktop.               await window.ddClient.navigateToContainerInspect(id);

> Warning >  > It will be removed in a future version.

#### Parameters

Name| Type| Description   ---|---|---   `id`| `string`| The full container id, e.g. `46b57e400d801762e9e115734bf902a2450d89669d85881058a46136520aca28`. You can use the `--no-trunc` flag as part of the `docker ps` command to display the full container id.      #### Returns

`Promise`<`any`>

A promise that fails if the container doesn't exist.

#### Inherited from

DockerDesktopClientV0.navigateToContainerInspect

* * *

### navigateToContainerStats

â¸ **navigateToContainerStats**\(`id`\): `Promise`<`any`>

Navigate to the container stats to see the CPU, memory, disk read/write and network I/O usage.               await window.ddClient.navigateToContainerStats(id);

> Warning >  > It will be removed in a future version.

#### Parameters

Name| Type| Description   ---|---|---   `id`| `string`| The full container id, e.g. `46b57e400d801762e9e115734bf902a2450d89669d85881058a46136520aca28`. You can use the `--no-trunc` flag as part of the `docker ps` command to display the full container id.      #### Returns

`Promise`<`any`>

A promise that fails if the container doesn't exist.

#### Inherited from

DockerDesktopClientV0.navigateToContainerStats

* * *

### navigateToImages

â¸ **navigateToImages**\(\): `void`

Navigate to the images window in Docker Desktop.               await window.ddClient.navigateToImages(id);

> Warning >  > It will be removed in a future version. Use [viewImages](https://docs.docker.com/reference/api/extensions-sdk/NavigationIntents/#viewimages) instead.

#### Returns

`void`

#### Inherited from

DockerDesktopClientV0.navigateToImages

* * *

### navigateToImage

â¸ **navigateToImage**\(`id`, `tag`\): `Promise`<`any`>

Navigate to a specific image referenced by `id` and `tag` in Docker Desktop. In this navigation route you can find the image layers, commands, created time and size.               await window.ddClient.navigateToImage(id, tag);

> Warning >  > It will be removed in a future version. Use [viewImage](https://docs.docker.com/reference/api/extensions-sdk/NavigationIntents/#viewimage) instead.

#### Parameters

Name| Type| Description   ---|---|---   `id`| `string`| The full image id \(including sha\), e.g. `sha256:34ab3ae068572f4e85c448b4035e6be5e19cc41f69606535cd4d768a63432673`.   `tag`| `string`| The tag of the image, e.g. `latest`, `0.0.1`, etc.      #### Returns

`Promise`<`any`>

A promise that fails if the container doesn't exist.

#### Inherited from

DockerDesktopClientV0.navigateToImage

* * *

### navigateToVolumes

â¸ **navigateToVolumes**\(\): `void`

Navigate to the volumes window in Docker Desktop.               await window.ddClient.navigateToVolumes();

> Warning >  > It will be removed in a future version. Use [viewVolumes](https://docs.docker.com/reference/api/extensions-sdk/NavigationIntents/#viewvolumes) instead.

#### Returns

`void`

#### Inherited from

DockerDesktopClientV0.navigateToVolumes

* * *

### navigateToVolume

â¸ **navigateToVolume**\(`volume`\): `void`

Navigate to a specific volume in Docker Desktop.               window.ddClient.navigateToVolume(volume);

> Warning >  > It will be removed in a future version. Use [viewVolume](https://docs.docker.com/reference/api/extensions-sdk/NavigationIntents/#viewvolume) instead.

#### Parameters

Name| Type| Description   ---|---|---   `volume`| `string`| The name of the volume, e.g. `my-volume`.      #### Returns

`void`

#### Inherited from

DockerDesktopClientV0.navigateToVolume

* * *

## Other Methods

### execHostCmd

â¸ **execHostCmd**\(`cmd`\): `Promise`<[`ExecResultV0`](https://docs.docker.com/reference/api/extensions-sdk/ExecResultV0/)>

You can run binaries defined in the host section in the extension metadata.               window.ddClient.execHostCmd(`cliShippedOnHost xxx`).then((cmdResult: any) => {      console.log(cmdResult);     });

> Warning >  > It will be removed in a future version. Use [exec](https://docs.docker.com/reference/api/extensions-sdk/ExtensionCli/#exec) instead.

#### Parameters

Name| Type| Description   ---|---|---   `cmd`| `string`| The command to be executed.      #### Returns

`Promise`<[`ExecResultV0`](https://docs.docker.com/reference/api/extensions-sdk/ExecResultV0/)>

#### Inherited from

DockerDesktopClientV0.execHostCmd

* * *

### spawnHostCmd

â¸ **spawnHostCmd**\(`cmd`, `args`, `callback`\): `void`

Invoke an extension binary on your host and get the output stream.               window.ddClient.spawnHostCmd(       `cliShippedOnHost`,       [`arg1`, `arg2`],       (data: any, err: any) => {         console.log(data.stdout, data.stderr);         // Once the command exits we get the status code         if (data.code) {           console.log(data.code);         }       }     );

> Warning >  > It will be removed in a future version. Use [exec](https://docs.docker.com/reference/api/extensions-sdk/ExtensionCli/#exec) instead.

#### Parameters

Name| Type| Description   ---|---|---   `cmd`| `string`| The command to be executed.   `args`| `string`\[\]| The arguments of the command to execute.   `callback`| \(`data`: `any`, `error`: `any`\) => `void`| The callback function where to listen from the command output data and errors.      #### Returns

`void`

#### Inherited from

DockerDesktopClientV0.spawnHostCmd

* * *

### execDockerCmd

â¸ **execDockerCmd**\(`cmd`, `...args`\): `Promise`<[`ExecResultV0`](https://docs.docker.com/reference/api/extensions-sdk/ExecResultV0/)>

You can also directly execute the Docker binary.               const output = await window.ddClient.execDockerCmd("info");

> Warning >  > It will be removed in a future version. Use [exec](https://docs.docker.com/reference/api/extensions-sdk/DockerCommand/#exec) instead.

#### Parameters

Name| Type| Description   ---|---|---   `cmd`| `string`| The command to execute.   `...args`| `string`\[\]| The arguments of the command to execute.      #### Returns

`Promise`<[`ExecResultV0`](https://docs.docker.com/reference/api/extensions-sdk/ExecResultV0/)>

The result will contain both the standard output and the standard error of the executed command:               {       "stderr": "...",       "stdout": "..."     }

For convenience, the command result object also has methods to easily parse it depending on the output format:

  * `output.lines(): string[]` splits output lines.   * `output.parseJsonObject(): any` parses a well-formed JSON output.   * `output.parseJsonLines(): any[]` parses each output line as a JSON object.

If the output of the command is too long, or you need to get the output as a stream you can use the

  * spawnDockerCmd function:

              window.ddClient.spawnDockerCmd("logs", ["-f", "..."], (data, error) => {       console.log(data.stdout);     });

#### Inherited from

DockerDesktopClientV0.execDockerCmd

* * *

### spawnDockerCmd

â¸ **spawnDockerCmd**\(`cmd`, `args`, `callback`\): `void`

> Warning >  > It will be removed in a future version. Use [exec](https://docs.docker.com/reference/api/extensions-sdk/DockerCommand/#exec) instead.

#### Parameters

Name| Type   ---|---   `cmd`| `string`   `args`| `string`\[\]   `callback`| \(`data`: `any`, `error`: `any`\) => `void`      #### Returns

`void`

#### Inherited from

DockerDesktopClientV0.spawnDockerCmd

* * *

### openExternal

â¸ **openExternal**\(`url`\): `void`

Opens an external URL with the system default browser.               window.ddClient.openExternal("https://docker.com");

> Warning >  > It will be removed in a future version. Use [openExternal](https://docs.docker.com/reference/api/extensions-sdk/Host/#openexternal) instead.

#### Parameters

Name| Type| Description   ---|---|---   `url`| `string`| The URL the browser opens \(must have the protocol `http` or `https`\).      #### Returns

`void`

#### Inherited from

DockerDesktopClientV0.openExternal

* * *

## Toast Methods

### toastSuccess

â¸ **toastSuccess**\(`msg`\): `void`

Display a toast message of type success.               window.ddClient.toastSuccess("message");

> **Warning\`** >  > It will be removed in a future version. Use [success](https://docs.docker.com/reference/api/extensions-sdk/Toast/#success) instead.

#### Parameters

Name| Type| Description   ---|---|---   `msg`| `string`| The message to display in the toast.      #### Returns

`void`

#### Inherited from

DockerDesktopClientV0.toastSuccess

* * *

### toastWarning

â¸ **toastWarning**\(`msg`\): `void`

Display a toast message of type warning.               window.ddClient.toastWarning("message");

> Warning >  > It will be removed in a future version. Use [warning](https://docs.docker.com/reference/api/extensions-sdk/Toast/#warning) instead.

#### Parameters

Name| Type| Description   ---|---|---   `msg`| `string`| The message to display in the toast.      #### Returns

`void`

#### Inherited from

DockerDesktopClientV0.toastWarning

* * *

### toastError

â¸ **toastError**\(`msg`\): `void`

Display a toast message of type error.               window.ddClient.toastError("message");

> Warning >  > It will be removed in a future version. Use [error](https://docs.docker.com/reference/api/extensions-sdk/Toast/#error) instead.

#### Parameters

Name| Type| Description   ---|---|---   `msg`| `string`| The message to display in the toast.      #### Returns

`void`

#### Inherited from

DockerDesktopClientV0.toastError