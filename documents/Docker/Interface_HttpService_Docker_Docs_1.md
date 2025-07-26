# Interface: HttpService | Docker Docs

**URL:** https://docs.docker.com/reference/api/extensions-sdk/HttpService/
**Word Count:** 831
**Links Count:** 515
**Scraped:** 2025-07-16 01:53:07
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# Interface: HttpService

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

**`Since`**

0.2.0

## Methods

### get

â¸ **get**\(`url`\): `Promise`<`unknown`>

Performs an HTTP GET request to a backend service.               ddClient.extension.vm.service      .get("/some/service")      .then((value: any) => console.log(value)

#### Parameters

Name| Type| Description   ---|---|---   `url`| `string`| The URL of the backend service.      #### Returns

`Promise`<`unknown`>

* * *

### post

â¸ **post**\(`url`, `data`\): `Promise`<`unknown`>

Performs an HTTP POST request to a backend service.               ddClient.extension.vm.service      .post("/some/service", { ... })      .then((value: any) => console.log(value));

#### Parameters

Name| Type| Description   ---|---|---   `url`| `string`| The URL of the backend service.   `data`| `any`| The body of the request.      #### Returns

`Promise`<`unknown`>

* * *

### put

â¸ **put**\(`url`, `data`\): `Promise`<`unknown`>

Performs an HTTP PUT request to a backend service.               ddClient.extension.vm.service      .put("/some/service", { ... })      .then((value: any) => console.log(value));

#### Parameters

Name| Type| Description   ---|---|---   `url`| `string`| The URL of the backend service.   `data`| `any`| The body of the request.      #### Returns

`Promise`<`unknown`>

* * *

### patch

â¸ **patch**\(`url`, `data`\): `Promise`<`unknown`>

Performs an HTTP PATCH request to a backend service.               ddClient.extension.vm.service      .patch("/some/service", { ... })      .then((value: any) => console.log(value));

#### Parameters

Name| Type| Description   ---|---|---   `url`| `string`| The URL of the backend service.   `data`| `any`| The body of the request.      #### Returns

`Promise`<`unknown`>

* * *

### delete

â¸ **delete**\(`url`\): `Promise`<`unknown`>

Performs an HTTP DELETE request to a backend service.               ddClient.extension.vm.service      .delete("/some/service")      .then((value: any) => console.log(value));

#### Parameters

Name| Type| Description   ---|---|---   `url`| `string`| The URL of the backend service.      #### Returns

`Promise`<`unknown`>

* * *

### head

â¸ **head**\(`url`\): `Promise`<`unknown`>

Performs an HTTP HEAD request to a backend service.               ddClient.extension.vm.service      .head("/some/service")      .then((value: any) => console.log(value));

#### Parameters

Name| Type| Description   ---|---|---   `url`| `string`| The URL of the backend service.      #### Returns

`Promise`<`unknown`>

* * *

### request

â¸ **request**\(`config`\): `Promise`<`unknown`>

Performs an HTTP request to a backend service.               ddClient.extension.vm.service      .request({ url: "/url", method: "GET", headers: { 'header-key': 'header-value' }, data: { ... }})      .then((value: any) => console.log(value));

#### Parameters

Name| Type| Description   ---|---|---   `config`| [`RequestConfig`](https://docs.docker.com/reference/api/extensions-sdk/RequestConfig/)| The URL of the backend service.      #### Returns

`Promise`<`unknown`>