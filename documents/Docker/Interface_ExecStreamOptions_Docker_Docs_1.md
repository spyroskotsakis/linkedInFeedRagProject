# Interface: ExecStreamOptions | Docker Docs

**URL:** https://docs.docker.com/reference/api/extensions-sdk/ExecStreamOptions/
**Word Count:** 850
**Links Count:** 500
**Scraped:** 2025-07-16 01:53:07
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# Interface: ExecStreamOptions

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

**`Since`**

0.2.2

## Properties

### onOutput

â¢ `Optional` **onOutput** : \(`data`: \{ `stdout`: `string` ; `stderr?`: `undefined` \} | \{ `stdout?`: `undefined` ; `stderr`: `string` \}\) => `void`

#### Type declaration

â¸ \(`data`\): `void`

Invoked when receiving output from command execution. By default, the output is split into chunks at arbitrary boundaries. If you prefer the output to be split into complete lines, set `splitOutputLines` to true. The callback is then invoked once for each line.

**`Since`**

0.2.0

##### Parameters

Name| Type| Description   ---|---|---   `data`| `{ stdout: string; stderr?: undefined } | { stdout?: undefined; stderr: string }`| Output content. Can include either stdout string, or stderr string, one at a time.      ##### Returns

`void`

* * *

### onError

â¢ `Optional` **onError** : \(`error`: `any`\) => `void`

#### Type declaration

â¸ \(`error`\): `void`

Invoked to report error if the executed command errors.

##### Parameters

Name| Type| Description   ---|---|---   `error`| `any`| The error happening in the executed command      ##### Returns

`void`

* * *

### onClose

â¢ `Optional` **onClose** : \(`exitCode`: `number`\) => `void`

#### Type declaration

â¸ \(`exitCode`\): `void`

Invoked when process exits.

##### Parameters

Name| Type| Description   ---|---|---   `exitCode`| `number`| The process exit code      ##### Returns

`void`

* * *

### splitOutputLines

â¢ `Optional` `Readonly` **splitOutputLines** : `boolean`

Specifies the behaviour invoking `onOutput(data)`. Raw output by default, splitting output at any position. If set to true, `onOutput` will be invoked once for each line.