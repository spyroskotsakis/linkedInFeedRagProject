# Docker for GitHub Copilot | Docker Docs

**URL:** https://docs.docker.com/copilot/
**Word Count:** 1266
**Links Count:** 644
**Scraped:** 2025-07-16 01:48:31
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Docker for GitHub Copilot

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Availability: Early Access 

The [Docker for GitHub Copilot](https://github.com/marketplace/docker-for-github-copilot) extension integrates Docker's capabilities with GitHub Copilot, providing assistance with containerizing applications, generating Docker assets, and analyzing project vulnerabilities. This extension helps you streamline Docker-related tasks wherever GitHub Copilot Chat is available.

## Key features

Key features of the Docker for GitHub Copilot extension include:

  * Ask questions and receive responses about containerization in any context where GitHub Copilot Chat is available, such as on GitHub.com and in Visual Studio Code.   * Automatically generate Dockerfiles, Docker Compose files, and `.dockerignore` files for a project.   * Open pull requests with generated Docker assets directly from the chat interface.   * Get summaries of project vulnerabilities from [Docker Scout](https://docs.docker.com/scout/) and receive next steps via the CLI.

## Data Privacy

The Docker agent is trained exclusively on Docker's documentation and tools to assist with containerization and related tasks. It does not have access to your project's data outside the context of the questions you ask.

When using the Docker Extension for GitHub Copilot, GitHub Copilot may include a reference to the currently open file in its request if authorized by the user. The Docker agent can read the file to provide context-aware responses.

If the agent is requested to check for vulnerabilities or generate Docker-related assets, it will clone the referenced repository into in-memory storage to perform the necessary actions.

Source code or project metadata is never persistently stored. Questions and answers are retained for analytics and troubleshooting. Data processed by the Docker agent is never shared with third parties.

## Supported languages

The Docker Extension for GitHub Copilot supports the following programming languages for tasks involving containerizing a project from scratch:

  * Go   * Java   * JavaScript   * Python   * Rust   * TypeScript