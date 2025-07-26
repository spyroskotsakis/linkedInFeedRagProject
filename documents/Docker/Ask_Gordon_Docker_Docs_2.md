# Ask Gordon | Docker Docs

**URL:** https://docs.docker.com/ai/gordon/
**Word Count:** 2182
**Links Count:** 688
**Scraped:** 2025-07-16 01:46:03
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Ask Gordon

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Availability: Beta 

Requires: Docker Desktop [4.38.0](https://docs.docker.com/desktop/release-notes/#4380) or later

Ask Gordon is your personal AI assistant embedded in Docker Desktop and the Docker CLI. It's designed to streamline your workflow and help you make the most of the Docker ecosystem.

## Key features

Ask Gordon provides AI-powered assistance in Docker tools. It can:

  * Improve Dockerfiles   * Run and troubleshoot containers   * Interact with your images and code   * Find vulnerabilities or configuration issues   * Migrate a Dockerfile to use [Docker Hardened Images](https://docs.docker.com/dhi/)

It understands your local environment, including source code, Dockerfiles, and images, to provide personalized and actionable guidance.

Ask Gordon remembers conversations, allowing you to switch topics more easily.

Ask Gordon is not enabled by default, and is not production-ready. You may also encounter the term "Docker AI" as a broader reference to this technology.

> Note >  > Ask Gordon is powered by Large Language Models \(LLMs\). Like all LLM-based tools, its responses may sometimes be inaccurate. Always verify the information provided.

### What data does Gordon access?

When you use Ask Gordon, the data it accesses depends on the context of your query:

  * Local files: If you use the `docker ai` command, Ask Gordon can access files and directories in the current working directory where the command is executed. In Docker Desktop, if you ask about a specific file or directory in the **Ask Gordon** view, you'll be prompted to select the relevant context.   * Local images: Gordon integrates with Docker Desktop and can view all images in your local image store. This includes images you've built or pulled from a registry.

To provide accurate responses, Ask Gordon may send relevant files, directories, or image metadata to the Gordon backend along with your query. This data transfer occurs over the network but is never stored persistently or shared with third parties. It is used exclusively to process your request and formulate a response. For more information about privacy terms and conditions for Docker AI, review [Gordon's Supplemental Terms](https://www.docker.com/legal/docker-ai-supplemental-terms/).

All data transferred is encrypted in transit.

### How your data is collected and used

Docker collects anonymized data from your interactions with Ask Gordon to enhance the service. This includes the following:

  * Your queries: Questions you ask Gordon.   * Responses: Answers provided by Gordon.   * Feedback: Thumbs-up and thumbs-down ratings.

To ensure privacy and security:

  * Data is anonymized and cannot be traced back to you or your account.   * Docker does not use this data to train AI models or share it with third parties.

By using Ask Gordon, you help improve Docker AI's reliability and accuracy, making it more effective for all users.

If you have concerns about data collection or usage, you can disable the feature at any time.

## Enable Ask Gordon

  1. Sign in to your Docker account.

  2. Navigate to the **Beta features** tab in settings.

  3. Check the **Enable Docker AI** checkbox.

The Docker AI terms of service agreement is displayed. You must agree to the terms before you can enable the feature. Review the terms and select **Accept and enable** to continue.

  4. Select **Apply**.

> Important >  > For Docker Desktop versions 4.41 and earlier, this settings lived under the **Experimental features** tab on the **Features in development** page.

## Using Ask Gordon

You can access Gordon:

  * In Docker Desktop, in the **Ask Gordon** view.   * Via the Docker CLI, with the `docker ai` CLI command.

Once you've enabled the Docker AI features, you'll also find references to **Ask Gordon** in various other places throughout the Docker Desktop user interface. Whenever you encounter a button with the **Sparkles** \(â¨\) icon in the user interface, you can use the button to get contextual support from Ask Gordon.

## Example workflows

Ask Gordon is a general-purpose AI assistant created to help you with all your Docker-related tasks and workflows. If you need some inspiration, here are a few ways things you can try:

  * Troubleshoot a crashed container   * Get help with running a container   * Improve a Dockerfile   * Migrate a Dockerfile to DHI

For more examples, try asking Gordon directly. For example:               $ docker ai "What can you do?"     

### Troubleshoot a crashed container

If you try to start a container with an invalid configuration or command, you can use Ask Gordon to troubleshoot the error. For example, try starting a Postgres container without specifying a database password:               $ docker run postgres     Error: Database is uninitialized and superuser password is not specified.            You must specify POSTGRES_PASSWORD to a non-empty value for the            superuser. For example, "-e POSTGRES_PASSWORD=password" on "docker run".                 You may also use "POSTGRES_HOST_AUTH_METHOD=trust" to allow all            connections without a password. This is *not* recommended.                 See PostgreSQL documentation about "trust":            https://www.postgresql.org/docs/current/auth-trust.html     

In the **Containers** view in Docker Desktop, select the â¨ icon next to the container's name, or inspect the container and open the **Ask Gordon** tab.

### Get help with running a container

If you want to run a specific image but you're not sure how, Gordon might be able to help you get set up:

  1. Pull an image from Docker Hub \(for example, `postgres`\).   2. Open the **Images** view in Docker Desktop and select the image.   3. Select the **Run** button.

In the **Run a new container** dialog, you should see a message about **Ask Gordon**.

![Ask Gordon hint in Docker Desktop](https://docs.docker.com/images/gordon-run-ctr.png)

![Ask Gordon hint in Docker Desktop](https://docs.docker.com/images/gordon-run-ctr.png)

The linked text in the hint is a suggested prompt to start a conversation with Ask Gordon.

### Improve a Dockerfile

Gordon can analyze your Dockerfile and suggest improvements. To have Gordon evaluate your Dockerfile using the `docker ai` command:

  1. Navigate to your project directory:                    $ cd path/to/my/project          

  2. Use the `docker ai` command to rate your Dockerfile:                    $ docker ai rate my Dockerfile          

Gordon will analyze your Dockerfile and identify opportunities for improvement across several dimensions:

  * Build cache optimization   * Security   * Image size efficiency   * Best practices compliance   * Maintainability   * Reproducibility   * Portability   * Resource efficiency

### Migrate a Dockerfile to DHI

Migrating your Dockerfile to use [Docker Hardened Images](https://docs.docker.com/dhi/) helps you build more secure, minimal, and production-ready containers. DHIs are designed to reduce vulnerabilities, enforce best practices, and simplify compliance, making them a strong foundation for secure software supply chains.

To request Gordon's help for the migration:

  1. Ensure Gordon is [enabled](https://docs.docker.com/ai/gordon/#enable-ask-gordon).

  2. In Gordon's Toolbox, ensure Gordon's [Developer MCP toolkit is enabled](https://docs.docker.com/ai/gordon/mcp/built-in-tools/#configuration).

  3. In the terminal, navigate to the directory containing your Dockerfile.

  4. Start a conversation with Gordon:                    docker ai

  5. Type:                    "Migrate my dockerfile to DHI"          

  6. Follow the conversation with Gordon. Gordon will edit your Dockerfile, so when it requests access to the filesystem and more, type `yes` to allow Gordon to proceed.

> Note >  > To learn more about Gordon's data retention and the data it can access, see [Gordon](https://docs.docker.com/ai/gordon/#what-data-does-gordon-access).

When the migration is complete, you see a success message:               The migration to Docker Hardened Images (DHI) is complete. The updated Dockerfile     successfully builds the image, and no vulnerabilities were detected in the final image.     The functionality and optimizations of the original Dockerfile have been preserved.

> Important >  > As with any AI tool, you must verify Gordon's edits and test your image.

## Disable Ask Gordon

### For individual users

If you've enabled Ask Gordon and you want to disable it again:

  1. Open the **Settings** view in Docker Desktop.   2. Navigate to **Beta features**.   3. Clear the **Enable Docker AI** checkbox.   4. Select **Apply**.

### For organizations

If you want to disable Ask Gordon for your entire Docker organization, using [Settings Management](https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/), add the following property to your `admin-settings.json` file:               {       "enableDockerAI": {         "value": false,         "locked": true       }     }

Alternatively, you can disable all Beta features by setting `allowBetaFeatures` to false:               {       "allowBetaFeatures": {         "value": false,         "locked": true       }     }

## Feedback

We value your input on Ask Gordon and encourage you to share your experience. Your feedback helps us improve and refine Ask Gordon for all users. If you encounter issues, have suggestions, or simply want to share what you like, here's how you can get in touch:

  * Thumbs-up and thumbs-down buttons

Rate Ask Gordon's responses using the thumbs-up or thumbs-down buttons in the response.

  * Feedback survey

You can access the Ask Gordon survey by following the _Give feedback_ link in the **Ask Gordon** view in Docker Desktop, or from the CLI by running the `docker ai feedback` command.