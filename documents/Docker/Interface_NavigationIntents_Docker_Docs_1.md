# Interface: NavigationIntents | Docker Docs

**URL:** https://docs.docker.com/reference/api/extensions-sdk/NavigationIntents/
**Word Count:** 983
**Links Count:** 532
**Scraped:** 2025-07-16 01:53:07
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# Interface: NavigationIntents

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

**`Since`**

0.2.0

## Container Methods

### viewContainers

â¸ **viewContainers**\(\): `Promise`<`void`>

Navigate to the **Containers** tab in Docker Desktop.               ddClient.desktopUI.navigate.viewContainers()

#### Returns

`Promise`<`void`>

* * *

### viewContainer

â¸ **viewContainer**\(`id`\): `Promise`<`void`>

Navigate to the **Container** tab in Docker Desktop.               await ddClient.desktopUI.navigate.viewContainer(id)

#### Parameters

Name| Type| Description   ---|---|---   `id`| `string`| The full container id, e.g. `46b57e400d801762e9e115734bf902a2450d89669d85881058a46136520aca28`. You can use the `--no-trunc` flag as part of the `docker ps` command to display the full container id.      #### Returns

`Promise`<`void`>

A promise that fails if the container doesn't exist.

* * *

### viewContainerLogs

â¸ **viewContainerLogs**\(`id`\): `Promise`<`void`>

Navigate to the **Container logs** tab in Docker Desktop.               await ddClient.desktopUI.navigate.viewContainerLogs(id)

#### Parameters

Name| Type| Description   ---|---|---   `id`| `string`| The full container id, e.g. `46b57e400d801762e9e115734bf902a2450d89669d85881058a46136520aca28`. You can use the `--no-trunc` flag as part of the `docker ps` command to display the full container id.      #### Returns

`Promise`<`void`>

A promise that fails if the container doesn't exist.

* * *

### viewContainerInspect

â¸ **viewContainerInspect**\(`id`\): `Promise`<`void`>

Navigate to the **Inspect container** view in Docker Desktop.               await ddClient.desktopUI.navigate.viewContainerInspect(id)

#### Parameters

Name| Type| Description   ---|---|---   `id`| `string`| The full container id, e.g. `46b57e400d801762e9e115734bf902a2450d89669d85881058a46136520aca28`. You can use the `--no-trunc` flag as part of the `docker ps` command to display the full container id.      #### Returns

`Promise`<`void`>

A promise that fails if the container doesn't exist.

* * *

### viewContainerTerminal

â¸ **viewContainerTerminal**\(`id`\): `Promise`<`void`>

Navigate to the container terminal window in Docker Desktop.               await ddClient.desktopUI.navigate.viewContainerTerminal(id)

**`Since`**

0.3.4

#### Parameters

Name| Type| Description   ---|---|---   `id`| `string`| The full container id, e.g. `46b57e400d801762e9e115734bf902a2450d89669d85881058a46136520aca28`. You can use the `--no-trunc` flag as part of the `docker ps` command to display the full container id.      #### Returns

`Promise`<`void`>

A promise that fails if the container doesn't exist.

* * *

### viewContainerStats

â¸ **viewContainerStats**\(`id`\): `Promise`<`void`>

Navigate to the container stats to see the CPU, memory, disk read/write and network I/O usage.               await ddClient.desktopUI.navigate.viewContainerStats(id)

#### Parameters

Name| Type| Description   ---|---|---   `id`| `string`| The full container id, e.g. `46b57e400d801762e9e115734bf902a2450d89669d85881058a46136520aca28`. You can use the `--no-trunc` flag as part of the `docker ps` command to display the full container id.      #### Returns

`Promise`<`void`>

A promise that fails if the container doesn't exist.

* * *

## Images Methods

### viewImages

â¸ **viewImages**\(\): `Promise`<`void`>

Navigate to the **Images** tab in Docker Desktop.               await ddClient.desktopUI.navigate.viewImages()

#### Returns

`Promise`<`void`>

* * *

### viewImage

â¸ **viewImage**\(`id`, `tag`\): `Promise`<`void`>

Navigate to a specific image referenced by `id` and `tag` in Docker Desktop. In this navigation route you can find the image layers, commands, created time and size.               await ddClient.desktopUI.navigate.viewImage(id, tag)

#### Parameters

Name| Type| Description   ---|---|---   `id`| `string`| The full image id \(including sha\), e.g. `sha256:34ab3ae068572f4e85c448b4035e6be5e19cc41f69606535cd4d768a63432673`.   `tag`| `string`| The tag of the image, e.g. `latest`, `0.0.1`, etc.      #### Returns

`Promise`<`void`>

A promise that fails if the image doesn't exist.

* * *

## Volume Methods

### viewVolumes

â¸ **viewVolumes**\(\): `Promise`<`void`>

Navigate to the **Volumes** tab in Docker Desktop.               ddClient.desktopUI.navigate.viewVolumes()

#### Returns

`Promise`<`void`>

* * *

### viewVolume

â¸ **viewVolume**\(`volume`\): `Promise`<`void`>

Navigate to a specific volume in Docker Desktop.               await ddClient.desktopUI.navigate.viewVolume(volume)

#### Parameters

Name| Type| Description   ---|---|---   `volume`| `string`| The name of the volume, e.g. `my-volume`.      #### Returns

`Promise`<`void`>