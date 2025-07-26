# Interface: ExecResult | Docker Docs

**URL:** https://docs.docker.com/reference/api/extensions-sdk/ExecResult/
**Word Count:** 763
**Links Count:** 534
**Scraped:** 2025-07-16 01:53:07
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# Interface: ExecResult

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

**`Since`**

0.2.0

## Hierarchy

  * [`RawExecResult`](https://docs.docker.com/reference/api/extensions-sdk/RawExecResult/)

â³ **`ExecResult`**

## Methods

### lines

â¸ **lines**\(\): `string`\[\]

Split output lines.

#### Returns

`string`\[\]

The list of lines.

* * *

### parseJsonLines

â¸ **parseJsonLines**\(\): `any`\[\]

Parse each output line as a JSON object.

#### Returns

`any`\[\]

The list of lines where each line is a JSON object.

* * *

### parseJsonObject

â¸ **parseJsonObject**\(\): `any`

Parse a well-formed JSON output.

#### Returns

`any`

The JSON object.

## Properties

### cmd

â¢ `Optional` `Readonly` **cmd** : `string`

#### Inherited from

[RawExecResult](https://docs.docker.com/reference/api/extensions-sdk/RawExecResult/).[cmd](https://docs.docker.com/reference/api/extensions-sdk/RawExecResult/#cmd)

* * *

### killed

â¢ `Optional` `Readonly` **killed** : `boolean`

#### Inherited from

[RawExecResult](https://docs.docker.com/reference/api/extensions-sdk/RawExecResult/).[killed](https://docs.docker.com/reference/api/extensions-sdk/RawExecResult/#killed)

* * *

### signal

â¢ `Optional` `Readonly` **signal** : `string`

#### Inherited from

[RawExecResult](https://docs.docker.com/reference/api/extensions-sdk/RawExecResult/).[signal](https://docs.docker.com/reference/api/extensions-sdk/RawExecResult/#signal)

* * *

### code

â¢ `Optional` `Readonly` **code** : `number`

#### Inherited from

[RawExecResult](https://docs.docker.com/reference/api/extensions-sdk/RawExecResult/).[code](https://docs.docker.com/reference/api/extensions-sdk/RawExecResult/#code)

* * *

### stdout

â¢ `Readonly` **stdout** : `string`

#### Inherited from

[RawExecResult](https://docs.docker.com/reference/api/extensions-sdk/RawExecResult/).[stdout](https://docs.docker.com/reference/api/extensions-sdk/RawExecResult/#stdout)

* * *

### stderr

â¢ `Readonly` **stderr** : `string`

#### Inherited from

[RawExecResult](https://docs.docker.com/reference/api/extensions-sdk/RawExecResult/).[stderr](https://docs.docker.com/reference/api/extensions-sdk/RawExecResult/#stderr)