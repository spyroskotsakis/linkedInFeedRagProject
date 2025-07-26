# Settings Management | Docker Docs

**URL:** https://docs.docker.com/enterprise/security/hardened-desktop/settings-management
**Word Count:** 1317
**Links Count:** 669
**Scraped:** 2025-07-16 02:03:45
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# What is Settings Management?

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Subscription: Business

For: Administrators

Settings Management lets administrators configure and enforce Docker Desktop settings across end-user machines. It helps maintain consistent configurations and enhances security within your organization.

## Who is it for?

Settings Management is designed for organizations that:

  * Require centralized control over Docker Desktop configurations.   * Aim to standardize Docker Desktop environments across teams.   * Operate in regulated environments and need to enforce compliance.

This feature is available with a Docker Business subscription.

## How it works

Administrators can define settings using one of the following methods:

  * [Admin Console](https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/configure-admin-console/): Create and assign settings policies through the Docker Admin Console.   * [`admin-settings.json` file](https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/configure-json-file/): Place a configuration file on the user's machine to enforce settings.

Enforced settings override user-defined configurations and can't be modified by developers.

## Configurable settings

Settings Management supports a broad range of Docker Desktop features, including proxies, network configurations, and container isolation.

For a full list of settings you can enforce, see the [Settings reference](https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/settings-reference/).

## Set up Settings Management

  1. [Enforce sign-in](https://docs.docker.com/enterprise/security/enforce-sign-in/) to ensure all developers authenticate with your organization.   2. Choose a configuration method:      * Use the `--admin-settings` installer flag on [macOS](https://docs.docker.com/desktop/setup/install/mac-install/#install-from-the-command-line) or [Windows](https://docs.docker.com/desktop/setup/install/windows-install/#install-from-the-command-line) to automatically create the `admin-settings.json`.      * Manually create and configure the [`admin-settings.json` file](https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/configure-json-file/).      * Create a settings policy in the [Docker Admin Console](https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/configure-admin-console/).

After configuration, developers receive the enforced setting when they:

  * Quit and relaunch Docker Desktop, then sign in.   * Launch and sign in to Docker Desktop for the first time.

> Note >  > Docker Desktop does not automatically prompt users to restart or re-authenticate after a settings change.

## Developer experience

When settings are enforced:

  * Options appear grayed out in Docker Desktop and can't be modified via the Dashboard, CLI, or configuration files.   * If Enhanced Container Isolation is enabled, developers can't use privileged containers or similar methods to alter enforced settings within the Docker Desktop Linux VM.

## What's next?

  * [Configure Settings Management with the `admin-settings.json` file](https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/configure-json-file/)   * [Configure Settings Management with the Docker Admin Console](https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/configure-admin-console/)

## Learn more

  * To see how each Docker Desktop setting maps across the Docker Dashboard, `admin-settings.json` file, and Admin Console, see the [Settings reference](https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/settings-reference/).   * Read the [Settings Management blog post](https://www.docker.com/blog/settings-management-for-docker-desktop-now-generally-available-in-the-admin-console/).