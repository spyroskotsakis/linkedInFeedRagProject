# Interface: OpenDialogResult | Docker Docs

**URL:** https://docs.docker.com/reference/api/extensions-sdk/OpenDialogResult
**Word Count:** 772
**Links Count:** 488
**Scraped:** 2025-07-16 01:56:12
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# Interface: OpenDialogResult

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

**`Since`**

0.2.3

## Properties

### canceled

â¢ `Readonly` **canceled** : `boolean`

Whether the dialog was canceled.

* * *

### filePaths

â¢ `Readonly` **filePaths** : `string`\[\]

An array of file paths chosen by the user. If the dialog is cancelled this will be an empty array.

* * *

### bookmarks

â¢ `Optional` `Readonly` **bookmarks** : `string`\[\]

macOS only. An array matching the `filePaths` array of `base64` encoded strings which contains security scoped bookmark data. `securityScopedBookmarks` must be enabled for this to be populated.