# Dashboard | Docker Docs

**URL:** https://docs.docker.com/extensions/extensions-sdk/dev/api/dashboard/
**Word Count:** 1226
**Links Count:** 663
**Scraped:** 2025-07-16 01:49:59
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Dashboard

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## User notifications

Toasts provide a brief notification to the user. They appear temporarily and shouldn't interrupt the user experience. They also don't require user input to disappear.

### success

â¸ **success**\(`msg`\): `void`

Use to display a toast message of type success.               ddClient.desktopUI.toast.success("message");

### warning

â¸ **warning**\(`msg`\): `void`

Use to display a toast message of type warning.               ddClient.desktopUI.toast.warning("message");

### error

â¸ **error**\(`msg`\): `void`

Use to display a toast message of type error.               ddClient.desktopUI.toast.error("message");

For more details about method parameters and the return types available, see [Toast API reference](https://docs.docker.com/reference/api/extensions-sdk/Toast/).

> Deprecated user notifications >  > These methods are deprecated and will be removed in a future version. Use the methods specified above.               window.ddClient.toastSuccess("message");     window.ddClient.toastWarning("message");     window.ddClient.toastError("message");

## Open a file selection dialog

This function opens a file selector dialog that asks the user to select a file or folder.

â¸ **showOpenDialog**\(`dialogProperties`\): `Promise`< [`OpenDialogResult`](https://docs.docker.com/reference/api/extensions-sdk/OpenDialogResult/)>:

The `dialogProperties` parameter is a list of flags passed to Electron to customize the dialog's behaviour. For example, you can pass `multiSelections` to allow a user to select multiple files. See [Electron's documentation](https://www.electronjs.org/docs/latest/api/dialog) for a full list.               const result = await ddClient.desktopUI.dialog.showOpenDialog({       properties: ["openDirectory"],     });     if (!result.canceled) {       console.log(result.paths);     }

## Open a URL

This function opens an external URL with the system default browser.

â¸ **openExternal**\(`url`\): `void`               ddClient.host.openExternal("https://docker.com");

> The URL must have the protocol `http` or `https`.

For more details about method parameters and the return types available, see [Desktop host API reference](https://docs.docker.com/reference/api/extensions-sdk/Host/).

> Deprecated user notifications >  > This method is deprecated and will be removed in a future version. Use the methods specified above.               window.ddClient.openExternal("https://docker.com");

## Navigation to Dashboard routes

From your extension, you can also [navigate](https://docs.docker.com/extensions/extensions-sdk/dev/api/dashboard-routes-navigation/) to other parts of the Docker Desktop Dashboard.