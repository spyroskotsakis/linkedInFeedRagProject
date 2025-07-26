# Interface: Dialog | Docker Docs

**URL:** https://docs.docker.com/reference/api/extensions-sdk/Dialog/
**Word Count:** 752
**Links Count:** 487
**Scraped:** 2025-07-16 01:53:07
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# Interface: Dialog

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Allows opening native dialog boxes.

**`Since`**

0.2.3

## Methods

### showOpenDialog

â¸ **showOpenDialog**\(`dialogProperties`\): `Promise`<[`OpenDialogResult`](https://docs.docker.com/reference/api/extensions-sdk/OpenDialogResult/)>

Display a native open dialog. Lets you select a file or a folder.               ddClient.desktopUI.dialog.showOpenDialog({properties: ['openFile']});

#### Parameters

Name| Type| Description   ---|---|---   `dialogProperties`| `any`| Properties to specify the open dialog behaviour, see <https://www.electronjs.org/docs/latest/api/dialog#dialogshowopendialogbrowserwindow-options>.      #### Returns

`Promise`<[`OpenDialogResult`](https://docs.docker.com/reference/api/extensions-sdk/OpenDialogResult/)>