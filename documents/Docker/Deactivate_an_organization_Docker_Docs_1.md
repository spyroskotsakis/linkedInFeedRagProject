# Deactivate an organization | Docker Docs

**URL:** https://docs.docker.com/admin/organization/deactivate-account/
**Word Count:** 1202
**Links Count:** 649
**Scraped:** 2025-07-16 01:48:31
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Deactivate an organization

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

For: Administrators

Learn how to deactivate a Docker organization, including required prerequisite steps. For information about deactivating user accounts, see [Deactivate a user account](https://docs.docker.com/accounts/deactivate-user-account/).

> Warning >  > All Docker products and services that use your Docker account or organization account will be inaccessible after deactivating your account.

## Prerequisites

You must complete all the following steps before you can deactivate your organization:

  * Download any images and tags you want to keep: `docker pull -a <image>:<tag>`.   * If you have an active Docker subscription, [downgrade it to a free subscription](https://docs.docker.com/subscription/change/).   * Remove all other members within the organization.   * Unlink your [GitHub and Bitbucket accounts](https://docs.docker.com/docker-hub/repos/manage/builds/link-source/#unlink-a-github-user-account).   * For Business organizations, [remove your SSO connection](https://docs.docker.com/enterprise/security/single-sign-on/manage/#remove-an-organization).

## Deactivate

You can deactivate your organization using either the Admin Console or Docker Hub.

> Warning >  > This cannot be undone. Be sure you've gathered all the data you need from your organization before deactivating it.

Admin Console  Docker Hub

  1. Sign in to [Docker Home](https://app.docker.com) and select the organization you want to deactivate.   2. Select **Admin Console** , then **Deactivate**. If the **Deactivate** button is unavailable, confirm you've completed all Prerequisites.   3. Enter the organization name to confirm deactivation.   4. Select **Deactivate organization**.

> Important >  > Organization management is moving to the Admin Console. >  > Manage members, team, settings, and activity logs in the Docker Admin Console. Access to these features in Docker Hub will end soon. Explore the [Admin Console](https://app.docker.com/admin).

  1. Sign in to [Docker Hub](https://hub.docker.com).   2. Choose the organization you want to deactivate.   3. In **Settings** , select **Deactivate org**.   4. Select **Deactivate organization**.