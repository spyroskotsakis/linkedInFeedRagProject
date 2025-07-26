# Extension UI API | Docker Docs

**URL:** https://docs.docker.com/extensions/extensions-sdk/dev/api/overview
**Word Count:** 1115
**Links Count:** 644
**Scraped:** 2025-07-16 02:01:22
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Extension UI API

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

* * *

The extensions UI runs in a sandboxed environment and doesn't have access to any electron or nodejs APIs.

The extension UI API provides a way for the frontend to perform different actions and communicate with the Docker Desktop dashboard or the underlying system.

JavaScript API libraries, with Typescript support, are available in order to get all the API definitions in to your extension code.

  * [@docker/extension-api-client](https://www.npmjs.com/package/@docker/extension-api-client) gives access to the extension API entrypoint `DockerDesktopClient`.   * [@docker/extension-api-client-types](https://www.npmjs.com/package/@docker/extension-api-client-types) can be added as a dev dependency in order to get types auto-completion in your IDE.

              import { createDockerDesktopClient } from '@docker/extension-api-client';          export function App() {       // obtain Docker Desktop client       const ddClient = createDockerDesktopClient();       // use ddClient to perform extension actions     }

The `ddClient` object gives access to various APIs:

  * [Extension Backend](https://docs.docker.com/extensions/extensions-sdk/dev/api/backend/)   * [Docker](https://docs.docker.com/extensions/extensions-sdk/dev/api/docker/)   * [Dashboard](https://docs.docker.com/extensions/extensions-sdk/dev/api/dashboard/)   * [Navigation](https://docs.docker.com/extensions/extensions-sdk/dev/api/dashboard-routes-navigation/)

Find the Extensions API reference [here](https://docs.docker.com/reference/api/extensions-sdk/).