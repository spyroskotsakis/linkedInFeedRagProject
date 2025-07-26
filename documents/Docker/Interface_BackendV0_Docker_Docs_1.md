# Interface: BackendV0 | Docker Docs

**URL:** https://docs.docker.com/reference/api/extensions-sdk/BackendV0/
**Word Count:** 999
**Links Count:** 548
**Scraped:** 2025-07-16 01:53:07
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# Interface: BackendV0

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Container Methods

### execInContainer

â¸ **execInContainer**\(`container`, `cmd`\): `Promise`<[`ExecResultV0`](https://docs.docker.com/reference/api/extensions-sdk/ExecResultV0/)>

Executes a command inside a container.               const output = await window.ddClient.backend.execInContainer(container, cmd);          console.log(output);

> Warning >  > It will be removed in a future version.

#### Parameters

Name| Type| Description   ---|---|---   `container`| `string`| -   `cmd`| `string`| The command to be executed.      #### Returns

`Promise`<[`ExecResultV0`](https://docs.docker.com/reference/api/extensions-sdk/ExecResultV0/)>

* * *

## HTTP Methods

### get

â¸ **get**\(`url`\): `Promise`<`unknown`>

Performs an HTTP GET request to a backend service.               window.ddClient.backend      .get("/some/service")      .then((value: any) => console.log(value));

> Warning >  > It will be removed in a future version. Use [get](https://docs.docker.com/reference/api/extensions-sdk/HttpService/#get) instead.

#### Parameters

Name| Type| Description   ---|---|---   `url`| `string`| The URL of the backend service.      #### Returns

`Promise`<`unknown`>

* * *

### post

â¸ **post**\(`url`, `data`\): `Promise`<`unknown`>

Performs an HTTP POST request to a backend service.               window.ddClient.backend      .post("/some/service", { ... })      .then((value: any) => console.log(value));

> Warning >  > It will be removed in a future version. Use [post](https://docs.docker.com/reference/api/extensions-sdk/HttpService/#post) instead.

#### Parameters

Name| Type| Description   ---|---|---   `url`| `string`| The URL of the backend service.   `data`| `any`| The body of the request.      #### Returns

`Promise`<`unknown`>

* * *

### put

â¸ **put**\(`url`, `data`\): `Promise`<`unknown`>

Performs an HTTP PUT request to a backend service.               window.ddClient.backend      .put("/some/service", { ... })      .then((value: any) => console.log(value));

> Warning >  > It will be removed in a future version. Use [put](https://docs.docker.com/reference/api/extensions-sdk/HttpService/#put) instead.

#### Parameters

Name| Type| Description   ---|---|---   `url`| `string`| The URL of the backend service.   `data`| `any`| The body of the request.      #### Returns

`Promise`<`unknown`>

* * *

### patch

â¸ **patch**\(`url`, `data`\): `Promise`<`unknown`>

Performs an HTTP PATCH request to a backend service.               window.ddClient.backend      .patch("/some/service", { ... })      .then((value: any) => console.log(value));

> Warning >  > It will be removed in a future version. Use [patch](https://docs.docker.com/reference/api/extensions-sdk/HttpService/#patch) instead.

#### Parameters

Name| Type| Description   ---|---|---   `url`| `string`| The URL of the backend service.   `data`| `any`| The body of the request.      #### Returns

`Promise`<`unknown`>

* * *

### delete

â¸ **delete**\(`url`\): `Promise`<`unknown`>

Performs an HTTP DELETE request to a backend service.               window.ddClient.backend      .delete("/some/service")      .then((value: any) => console.log(value));

> Warning >  > It will be removed in a future version. Use [delete](https://docs.docker.com/reference/api/extensions-sdk/HttpService/#delete) instead.

#### Parameters

Name| Type| Description   ---|---|---   `url`| `string`| The URL of the backend service.      #### Returns

`Promise`<`unknown`>

* * *

### head

â¸ **head**\(`url`\): `Promise`<`unknown`>

Performs an HTTP HEAD request to a backend service.               window.ddClient.backend      .head("/some/service")      .then((value: any) => console.log(value));

> Warning >  > It will be removed in a future version. Use [head](https://docs.docker.com/reference/api/extensions-sdk/HttpService/#head) instead.

#### Parameters

Name| Type| Description   ---|---|---   `url`| `string`| The URL of the backend service.      #### Returns

`Promise`<`unknown`>

* * *

### request

â¸ **request**\(`config`\): `Promise`<`unknown`>

Performs an HTTP request to a backend service.               window.ddClient.backend      .request({ url: "/url", method: "GET", headers: { 'header-key': 'header-value' }, data: { ... }})      .then((value: any) => console.log(value));

> Warning >  > It will be removed in a future version. Use [request](https://docs.docker.com/reference/api/extensions-sdk/HttpService/#request) instead.

#### Parameters

Name| Type| Description   ---|---|---   `config`| [`RequestConfigV0`](https://docs.docker.com/reference/api/extensions-sdk/RequestConfigV0/)| The URL of the backend service.      #### Returns

`Promise`<`unknown`>

* * *

## VM Methods

### execInVMExtension

â¸ **execInVMExtension**\(`cmd`\): `Promise`<[`ExecResultV0`](https://docs.docker.com/reference/api/extensions-sdk/ExecResultV0/)>

Executes a command inside the backend container. If your extensions ships with additional binaries that should be run inside the backend container you can use the `execInVMExtension` function.               const output = await window.ddClient.backend.execInVMExtension(       `cliShippedInTheVm xxx`     );          console.log(output);

> Warning >  > It will be removed in a future version. Use [exec](https://docs.docker.com/reference/api/extensions-sdk/ExtensionCli/#exec) instead.

#### Parameters

Name| Type| Description   ---|---|---   `cmd`| `string`| The command to be executed.      #### Returns

`Promise`<[`ExecResultV0`](https://docs.docker.com/reference/api/extensions-sdk/ExecResultV0/)>

* * *

### spawnInVMExtension

â¸ **spawnInVMExtension**\(`cmd`, `args`, `callback`\): `void`

Returns a stream from the command executed in the backend container.               window.ddClient.spawnInVMExtension(       `cmd`,       [`arg1`, `arg2`],       (data: any, err: any) => {         console.log(data.stdout, data.stderr);         // Once the command exits we get the status code         if (data.code) {           console.log(data.code);         }       }     );

> Warning >  > It will be removed in a future version.

#### Parameters

Name| Type| Description   ---|---|---   `cmd`| `string`| The command to be executed.   `args`| `string`\[\]| The arguments of the command to execute.   `callback`| \(`data`: `any`, `error`: `any`\) => `void`| The callback function where to listen from the command output data and errors.      #### Returns

`void`