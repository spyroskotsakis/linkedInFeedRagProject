# Validate | Docker Docs

**URL:** https://docs.docker.com/extensions/extensions-sdk/extensions/validate
**Word Count:** 1118
**Links Count:** 638
**Scraped:** 2025-07-16 02:03:45
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Validate your extension

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

* * *

Validate your extension before you share or publish it. Validating the extension ensures that the extension:

  * Is built with the [image labels](https://docs.docker.com/extensions/extensions-sdk/extensions/labels/) it requires to display correctly in the marketplace   * Installs and runs without problems

The Extensions CLI lets you validate your extension before installing and running it locally.

The validation checks if the extensionâs `Dockerfile` specifies all the required labels and if the metadata file is valid against the JSON schema file.

To validate, run:               $ docker extension validate <name-of-your-extension>     

If your extension is valid, the following message displays:               The extension image "name-of-your-extension" is valid     

Before the image is built, it's also possible to validate only the `metadata.json` file:               $ docker extension validate /path/to/metadata.json     

The JSON schema used to validate the `metadata.json` file against can be found under the [releases page](https://github.com/docker/extensions-sdk/releases/latest).