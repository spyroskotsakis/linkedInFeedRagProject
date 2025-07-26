# Interface: ExecResultV0 | Docker Docs

**URL:** https://docs.docker.com/reference/api/extensions-sdk/ExecResultV0
**Word Count:** 757
**Links Count:** 512
**Scraped:** 2025-07-16 01:55:49
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# Interface: ExecResultV0

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Properties

### cmd

â¢ `Optional` `Readonly` **cmd** : `string`

* * *

### killed

â¢ `Optional` `Readonly` **killed** : `boolean`

* * *

### signal

â¢ `Optional` `Readonly` **signal** : `string`

* * *

### code

â¢ `Optional` `Readonly` **code** : `number`

* * *

### stdout

â¢ `Readonly` **stdout** : `string`

* * *

### stderr

â¢ `Readonly` **stderr** : `string`

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