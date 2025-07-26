# Use the Admin Console | Docker Docs

**URL:** https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/configure-admin-console/
**Word Count:** 1305
**Links Count:** 654
**Scraped:** 2025-07-16 01:47:29
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Configure Settings Management with the Admin Console

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Subscription: Business

For: Administrators

This page explains how administrators can use the Docker Admin Console to create and apply settings policies for Docker Desktop. These policies help standardize and secure Docker Desktop environments across your organization.

## Prerequisites

  * [Install Docker Desktop 4.37.1 or later](https://docs.docker.com/desktop/release-notes/).   * [Verify your domain](https://docs.docker.com/enterprise/security/single-sign-on/configure/#step-one-add-and-verify-your-domain).   * [Enforce sign-in](https://docs.docker.com/enterprise/security/enforce-sign-in/) to ensure users authenticate to your organization.   * A Docker Business subscription is required.

> Important >  > You must add users to your verified domain for settings to take effect.

## Create a settings policy

  1. Sign in to [Docker Home](https://app.docker.com/) and select your organization.

  2. Select **Admin Console** , then **Desktop Settings Management**.

  3. Select **Create a settings policy**.

  4. Provide a name and optional description.

> Tip >  > You can upload an existing `admin-settings.json` file to pre-fill the form. Admin Console policies override local `admin-settings.json` files.

  5. Choose who the policy applies to:

     * All users

     * Specific users

> Note >  > User-specific policies override the global default. Test your policy with a few users before rolling it out globally.

  6. Configure the state for each setting:

     * **User-defined** : Users can change the setting.

     * **Always enabled** : Setting is on and locked.

     * **Enabled** : Setting is on but can be changed.

     * **Always disabled** : Setting is off and locked.

     * **Disabled** : Setting is off but can be changed.

> Tip >  > For a complete list of available settings, their supported platforms, and which configuration methods they work with, see the [Settings reference](https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/settings-reference/).

  7. Select **Create**.

To apply the policy:

  * New installs: Launch Docker Desktop and sign in.   * Existing installs: Fully quit and relaunch Docker Desktop.

> Important >  > Restarting from the Docker Desktop menu isn't enough. Users must fully quit and relaunch Docker Desktop.

Docker Desktop checks for policy updates at launch and every 60 minutes. To roll back a policy, either delete it or set individual settings to **User-defined**.

## Manage policies

From the **Actions** menu on the **Settings Management** page, you can:

  * Edit or delete an existing settings policy   * Export a settings policy as an `admin-settings.json` file   * Promote a user-specific policy to be the new global default

## Learn more

To see how each Docker Desktop setting maps across the Docker Dashboard, `admin-settings.json` file, and Admin Console, see the [Settings reference](https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/settings-reference/).