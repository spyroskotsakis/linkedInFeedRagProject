# Quickstart | Docker Docs

**URL:** https://docs.docker.com/extensions/extensions-sdk/quickstart
**Word Count:** 1487
**Links Count:** 668
**Scraped:** 2025-07-16 01:59:28
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Quickstart

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Follow this guide to get started with creating a basic Docker extension. The Quickstart guide automatically generates boilerplate files for you.

## Prerequisites

  * [Docker Desktop](https://docs.docker.com/desktop/release-notes/)   * [NodeJS](https://nodejs.org/)   * [Go](https://go.dev/dl/)

> Note >  > NodeJS and Go are only required when you follow the quickstart guide to create an extension. It uses the `docker extension init` command to automatically generate boilerplate files. This command uses a template based on a ReactJS and Go application.

In Docker Desktop settings, ensure you can install the extension you're developing. You may need to navigate to the **Extensions** tab in Docker Desktop settings and deselect **Allow only extensions distributed through the Docker Marketplace**.

## Step one: Set up your directory

To set up your directory, use the `init` subcommand and provide a name for your extension.               $ docker extension init <my-extension>     

The command asks a series of questions about your extension, such as its name, a description, and the name of your Hub repository. This helps the CLI generate a set of boilerplate files for you to get started. It stores the boilerplate files in the `my-extension` directory.

The automatically generated extension contains:

  * A Go backend service in the `backend` folder that listens on a socket. It has one endpoint `/hello` that returns a JSON payload.   * A React frontend in the `frontend` folder that can call the backend and output the backendâs response.

For more information and guidelines on building the UI, see the [Design and UI styling section](https://docs.docker.com/extensions/extensions-sdk/design/design-guidelines/).

## Step two: Build the extension

To build the extension, move into the newly created directory and run:               $ docker build -t <name-of-your-extension> .     

`docker build` builds the extension and generates an image named the same as the chosen hub repository. For example, if you typed `john/my-extension` as the answer to the following question:               ? Hub repository (eg. namespace/repository on hub): john/my-extension`     

The `docker build` generates an image with name `john/my-extension`.

## Step three: Install and preview the extension

To install the extension in Docker Desktop, run:               $ docker extension install <name-of-your-extension>     

To preview the extension in Docker Desktop, once the installation is complete and you should see a **Quickstart** item underneath the **Extensions** menu. Selecting this item opens the extension's frontend.

> Tip >  > During UI development, itâs helpful to use hot reloading to test your changes without rebuilding your entire extension. See [Preview whilst developing the UI](https://docs.docker.com/extensions/extensions-sdk/dev/test-debug/#hot-reloading-whilst-developing-the-ui) for more information.

You may also want to inspect the containers that belong to the extension. By default, extension containers are hidden from the Docker Dashboard. You can change this in **Settings** , see [how to show extension containers](https://docs.docker.com/extensions/extensions-sdk/dev/test-debug/#show-the-extension-containers) for more information.

## Step four: Submit and publish your extension to the Marketplace

If you want to make your extension available to all Docker Desktop users, you can submit it for publication in the Marketplace. For more information, see [Publish](https://docs.docker.com/extensions/extensions-sdk/extensions/).

## Clean up

To remove the extension, run:               $ docker extension rm <name-of-your-extension>     

## What's next

  * Build a more [advanced frontend](https://docs.docker.com/extensions/extensions-sdk/build/frontend-extension-tutorial/) for your extension.   * Learn how to [test and debug](https://docs.docker.com/extensions/extensions-sdk/dev/test-debug/) your extension.   * Learn how to [setup CI for your extension](https://docs.docker.com/extensions/extensions-sdk/dev/continuous-integration/).   * Learn more about extensions [architecture](https://docs.docker.com/extensions/extensions-sdk/architecture/).   * Learn more about [designing the UI](https://docs.docker.com/extensions/extensions-sdk/design/design-guidelines/).