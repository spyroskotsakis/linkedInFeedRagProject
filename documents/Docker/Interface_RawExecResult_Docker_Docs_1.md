# Interface: RawExecResult | Docker Docs

**URL:** https://docs.docker.com/reference/api/extensions-sdk/RawExecResult/
**Word Count:** 729
**Links Count:** 501
**Scraped:** 2025-07-16 01:53:07
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# Interface: RawExecResult

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

**`Since`**

0.2.0

## Hierarchy

  * **`RawExecResult`**

â³ [`ExecResult`](https://docs.docker.com/reference/api/extensions-sdk/ExecResult/)

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