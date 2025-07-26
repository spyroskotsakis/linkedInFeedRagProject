# Deactivate an account | Docker Docs

**URL:** https://docs.docker.com/accounts/deactivate-user-account
**Word Count:** 1226
**Links Count:** 645
**Scraped:** 2025-07-16 02:03:45
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Deactivate an account

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

You can deactivate an account at any time. This section describes the prerequisites and steps to deactivate a user account. For information on deactivating an organization, see [Deactivating an organization](https://docs.docker.com/admin/organization/deactivate-account/).

> Warning >  > All Docker products and services that use your Docker account will be inaccessible after deactivating your account.

## Prerequisites

Before deactivating your Docker account, ensure you meet the following requirements:

  * For owners, you must leave your organization or company before deactivating your Docker account. To do this:

    1. Sign in to [Docker Home](https://app.docker.com/admin) and choose your organization.     2. Select **Members** and find your username.     3. Select the **Actions** menu and then select **Leave organization**.   * If you are the sole owner of an organization, you must assign the owner role to another member of the organization and then remove yourself from the organization, or deactivate the organization. Similarly, if you are the sole owner of a company, either add someone else as a company owner and then remove yourself, or deactivate the company.

  * If you have an active Docker subscription, [downgrade it to a Docker Personal subscription](https://docs.docker.com/subscription/change/).

  * Download any images and tags you want to keep. Use `docker pull -a <image>:<tag>`.

  * Unlink your [GitHub and Bitbucket accounts](https://docs.docker.com/docker-hub/repos/manage/builds/link-source/#unlink-a-github-user-account).

## Deactivate

Once you have completed all the previous steps, you can deactivate your account.

> Warning >  > This cannot be undone. Be sure you've gathered all the data you need from your account before deactivating it.

  1. Sign in to [Docker Home](https://app.docker.com/login).   2. Select your avatar to open the drop-down menu.   3. Select **Account settings**.   4. Select **Deactivate**.   5. Select **Deactivate account**.   6. To confirm, select **Deactivate account**.