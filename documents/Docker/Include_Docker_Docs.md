# Include | Docker Docs

**URL:** https://docs.docker.com/compose/how-tos/multiple-compose-files/include
**Word Count:** 1431
**Links Count:** 650
**Scraped:** 2025-07-16 01:58:31
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Include

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Requires: Docker Compose [2.20.3](https://docs.docker.com/compose/releases/release-notes/#2203) and later

With `include`, you can incorporate a separate `compose.yaml` file directly in your current `compose.yaml` file. This makes it easy to modularize complex applications into sub-Compose files, which in turn enables application configurations to be made simpler and more explicit.

The [`include` top-level element](https://docs.docker.com/reference/compose-file/include/) helps to reflect the engineering team responsible for the code directly in the config file's organization. It also solves the relative path problem that [`extends`](https://docs.docker.com/compose/how-tos/multiple-compose-files/extends/) and [merge](https://docs.docker.com/compose/how-tos/multiple-compose-files/merge/) present.

Each path listed in the `include` section loads as an individual Compose application model, with its own project directory, in order to resolve relative paths.

Once the included Compose application loads, all resources are copied into the current Compose application model.

> Note >  > `include` applies recursively so an included Compose file which declares its own `include` section, causes those files to also be included.

## Example               include:       - my-compose-include.yaml  #with serviceB declared     services:       serviceA:         build: .         depends_on:           - serviceB #use serviceB directly as if it was declared in this Compose file

`my-compose-include.yaml` manages `serviceB` which details some replicas, web UI to inspect data, isolated networks, volumes for data persistence, etc. The application relying on `serviceB` doesnât need to know about the infrastructure details, and consumes the Compose file as a building block it can rely on.

This means the team managing `serviceB` can refactor its own database component to introduce additional services without impacting any dependent teams. It also means that the dependent teams don't need to include additional flags on each Compose command they run.               include:       - oci://docker.io/username/my-compose-app:latest # use a Compose file stored as an OCI artifact     services:       serviceA:         build: .         depends_on:           - serviceB 

`include` allows you to reference Compose files from remote sources, such as OCI artifacts or Git repositories.   Here `serviceB` is defined in a Compose file stored on Docker Hub.

## Using overrides with included Compose files

Compose reports an error if any resource from `include` conflicts with resources from the included Compose file. This rule prevents unexpected conflicts with resources defined by the included compose file author. However, there may be some circumstances where you might want to customize the included model. This can be achieved by adding an override file to the include directive:               include:       - path :            - third-party/compose.yaml           - override.yaml  # local override for third-party model

The main limitation with this approach is that you need to maintain a dedicated override file per include. For complex projects with multiple includes this would result in many Compose files.

The other option is to use a `compose.override.yaml` file. While conflicts will be rejected from the file using `include` when same resource is declared, a global Compose override file can override the resulting merged model, as demonstrated in following example:

Main `compose.yaml` file:               include:       - team-1/compose.yaml # declare service-1       - team-2/compose.yaml # declare service-2

Override `compose.override.yaml` file:               services:       service-1:         # override included service-1 to enable debugger port         ports:           - 2345:2345            service-2:         # override included service-2 to use local data folder containing test data         volumes:           - ./data:/data

Combined together, this allows you to benefit from third-party reusable components, and adjust the Compose model for your needs.

## Reference information

[`include` top-level element](https://docs.docker.com/reference/compose-file/include/)