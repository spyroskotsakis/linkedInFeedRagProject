# Interface: Toast | Docker Docs

**URL:** https://docs.docker.com/reference/api/extensions-sdk/Toast
**Word Count:** 789
**Links Count:** 494
**Scraped:** 2025-07-16 01:57:18
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# Interface: Toast

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Toasts provide a brief notification to the user. They appear temporarily and shouldn't interrupt the user experience. They also don't require user input to disappear.

**`Since`**

0.2.0

## Methods

### success

â¸ **success**\(`msg`\): `void`

Display a toast message of type success.               ddClient.desktopUI.toast.success("message");

#### Parameters

Name| Type| Description   ---|---|---   `msg`| `string`| The message to display in the toast.      #### Returns

`void`

* * *

### warning

â¸ **warning**\(`msg`\): `void`

Display a toast message of type warning.               ddClient.desktopUI.toast.warning("message");

#### Parameters

Name| Type| Description   ---|---|---   `msg`| `string`| The message to display in the warning.      #### Returns

`void`

* * *

### error

â¸ **error**\(`msg`\): `void`

Display a toast message of type error.               ddClient.desktopUI.toast.error("message");

#### Parameters

Name| Type| Description   ---|---|---   `msg`| `string`| The message to display in the toast.      #### Returns

`void`