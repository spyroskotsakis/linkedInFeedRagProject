# Desktop settings reporting | Docker Docs

**URL:** https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/compliance-reporting
**Word Count:** 1680
**Links Count:** 659
**Scraped:** 2025-07-16 01:59:56
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Desktop settings reporting

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Subscription: Business

Availability: Early Access 

Requires: Docker Desktop 4.40 and later

For: Administrators

Desktop settings reporting is a feature of Desktop Settings Management that tracks and reports user compliance with the settings policies that are assigned to them. This lets administrators track the application of settings and monitor what actions they need to take to make users compliant.

This guide provides steps for accessing Desktop settings reporting, viewing compliance status, and resolving non-compliant users.

## Access Desktop settings reporting

> Important >  > Desktop settings reporting is in Early Access and is being rolled out gradually. You may not see this setting in the Admin Console yet.

  1. Sign in to [Docker Home](https://app.docker.com) and select your organization.   2. Select **Admin Console** , then **Desktop settings reporting**.

This opens the Desktop settings reporting page. From here you can:

  * Use the **Search** field to search by username or email address   * Filter by policies   * Hide or un-hide compliant users   * View a userâs compliance status and what policy is assigned to the user   * Download a CSV file of user compliance information

## View compliance status

> Warning >  > Users on Docker Desktop versions older than 4.40 may appear non-compliant because older versions can't report compliance. To ensure accurate compliance status, users must update to Docker Desktop version 4.40 and later.

  1. Sign in to [Docker Home](https://app.docker.com) and select your organization.   2. Select **Admin Console** , then **Desktop settings reporting**.   3. Optional. Select the **Hide compliant users** checkbox to show both compliant and non-compliant users.   4. Use the **Search** field to search by username or email address.   5. Hover over a userâs compliance status indicator to quickly view their status.   6. Select a username to view more details about their compliance status, and for steps to resolve non-compliant users.

## Understand compliance status

Docker evaluates compliance status based on:

  * Compliance status: Whether a user has fetched and applied the latest settings. This is the primary label shown on the reporting page.   * Domain status: Whether the user's email matches a verified domain.   * Settings status: Whether a settings policy is applied to the user.

The combination of these statuses determines what actions you need to take.

### Compliance status reference

This reference explains how each status is determined in the reporting dashboard based on user domain and settings data. The Admin Console displays the highest-priority applicable status according to the following rules.

**Compliance status**

Compliance status| What it means   ---|---   Uncontrolled domain| The user's email domain is not verified.   No policy assigned| The user does not have any policy assigned to them.   Non-compliant| The user fetched the correct policy, but hasn't applied it.   Outdated| The user fetched a previous version of the policy.   Compliant| The user fetched and applied the latest assigned policy.      **Domain status**

This reflects how the userâs email domain is evaluated based on the organizationâs domain setup.

Domain status| What it means   ---|---   Verified| The userâs email domain is verified.   Guest user| The user's email domain is not verified.   Domainless| Your organization has no verified domains, and the user's domain is unknown.      **Settings status**

This shows whether and how the user is assigned a settings policy.

Settings status| What it means   ---|---   Global policy| The user is assigned your organzation's default policy.   User policy| The user is assigned a specific custom policy.   No policy assigned| The user is not assigned to any policy.      ## Resolve compliance status

To resolve compliance status, you must view a user's compliance status details by selecting their username from the Desktop settings reporting page. These details include the following information:

  * **Compliance status** : Indicates whether the user is compliant with the settings applied to them   * **Domain status** : Indicates whether the userâs email address is associated with a verified domain   * **Settings status** : Indicates whether the user has settings applied to them   * **Resolution steps** : If a user is non-compliant, this provides information on how to resolve the userâs compliance status

### Compliant

When a user is compliant, a **Compliant** icon appears next to their name on the Desktop settings reporting dashboard. Select a compliant user to open their compliance status details. Compliant users have the following status details:

  * **Compliance status** : Compliant   * **Domain status** : Verified   * **Settings status** : Global policy or user policy   * **User is compliant** indicator

No resolution steps are needed for compliant users.

### Non-compliant

When a user is non-compliant, a **Non-compliant** or **Unknown** icon appears next to their name on the Desktop settings reporting dashboard. Non-compliant users must have their compliance status resolved:

  1. Select a username from the Desktop settings reporting dashboard.   2. On the compliance status details page, follow the resolution steps provided to resolve the compliance status.   3. Refresh the page to ensure the resolution steps resolved the compliance status.