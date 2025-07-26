# Create your organization | Docker Docs

**URL:** https://docs.docker.com/admin/organization/orgs/
**Word Count:** 2025
**Links Count:** 675
**Scraped:** 2025-07-16 01:46:25
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Create your organization

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Subscription: Team Business

For: Administrators

This page describes how to create an organization.

## Prerequisites

Before you begin creating an organization:

  * You need a [Docker ID](https://docs.docker.com/accounts/create-account/)   * Review the [Docker subscriptions and features](https://docs.docker.com/subscription/details/) to determine what subscription to choose for your organization

## Create an organization

There are multiple ways to create an organization. You can either:

  * Create a new organization using the **Create Organization** option in the Admin Console or Docker Hub   * Convert an existing user account to an organization

The following section contains instructions on how to create a new organization. For prerequisites and detailed instructions on converting an existing user account to an organization, see [Convert an account into an organization](https://docs.docker.com/admin/organization/convert-account/).

Admin Console  Docker Hub

To create an organization:

  1. Sign in to [Docker Home](https://app.docker.com/) and navigate to the bottom of the organization list.

  2. Select **Create new organization**.

  3. Choose a subscription for your organization, a billing cycle, and specify how many seats you need. See [Docker Pricing](https://www.docker.com/pricing/) for details on the features offered in the Team and Business subscription.

  4. Select **Continue to profile**.

  5. Select **Create an organization** to create a new one.

  6. Enter an **Organization namespace**. This is the official, unique name for your organization in Docker Hub. It's not possible to change the name of the organization after you've created it.

> Note >  > You can't use the same name for the organization and your Docker ID. If you want to use your Docker ID as the organization name, then you must first [convert your account into an organization](https://docs.docker.com/admin/organization/convert-account/).

  7. Enter your **Company name**. This is the full name of your company. Docker displays the company name on your organization page and in the details of any public images you publish. You can update the company name anytime by navigating to your organization's **Settings** page.

  8. Select **Continue to billing** to continue.

  9. Enter your organization's billing information and select **Continue to payment** to continue to the billing portal.

  10. Provide your payment details and select **Purchase**.

You've now created an organization.

> Important >  > Organization management is moving to the Admin Console. >  > Manage members, team, settings, and activity logs in the Docker Admin Console. Access to these features in Docker Hub will end soon. Explore the [Admin Console](https://app.docker.com/admin).

  1. Sign in to [Docker Hub](https://hub.docker.com/) using your Docker ID, your email address, or your social provider.

  2. Select **My Hub** , select the account drop-down, and then **Create Organization** to create a new organization.

  3. Choose a subscription for your organization, a billing cycle, and specify how many seats you need. See [Docker Pricing](https://www.docker.com/pricing/) for details on the features offered in the Team and Business subscription.

  4. Select **Continue to profile**.

  5. Enter an **Organization namespace**. This is the official, unique name for your organization in Docker Hub. It's not possible to change the name of the organization after you've created it.

> Note >  > You can't use the same name for the organization and your Docker ID. If you want to use your Docker ID as the organization name, then you must first [convert your account into an organization](https://docs.docker.com/admin/organization/convert-account/).

  6. Enter your **Company name**. This is the full name of your company. Docker displays the company name on your organization page and in the details of any public images you publish. You can update the company name anytime by navigating to your organization's **Settings** page.

  7. Select **Continue to billing** to continue.

  8. Enter your organization's billing information and select **Continue to payment** to continue to the billing portal.

  9. Provide your card details and select **Purchase**.

You've now created an organization.

## View an organization

Admin Console  Docker Hub

To view an organization in the Admin Console:

  1. Sign in to [Docker Home](https://app.docker.com) and select your organization.   2. From the left-hand navigation menu, select **Admin Console**.

The Admin Console contains many options that let you to configure your organization.

> Important >  > Organization management is moving to the Admin Console. >  > Manage members, team, settings, and activity logs in the Docker Admin Console. Access to these features in Docker Hub will end soon. Explore the [Admin Console](https://app.docker.com/admin).

To view an organization:

  1. Sign in to [Docker Hub](https://hub.docker.com) with a user account that is a member of any team in the organization.

> Note >  > You can't _directly_ sign in to an organization. This is especially important to note if you create an organization by [converting a user account](https://docs.docker.com/admin/organization/convert-account/), as conversion means you lose the ability to log into that "account", since it no longer exists. To view the organization you need to sign in with the new owner account assigned during the conversion or another account that was added as a member. If you don't see the organization after logging in, then you are neither a member or an owner of it. An organization administrator needs to add you as a member of the organization.

  2. Select **My Hub** in the top navigation bar, then choose your organization from the list.

The organization landing page displays various options that let you to configure your organization.

  * **Members** : Displays a list of team members. You can invite new members using the **Invite members** button. See [Manage members](https://docs.docker.com/admin/organization/members/) for details.   * **Teams** : Displays a list of existing teams and the number of members in each team. See [Create a team](https://docs.docker.com/admin/organization/manage-a-team/) for details.   * **Repositories** : Displays a list of repositories associated with the organization. See [Repositories](https://docs.docker.com/docker-hub/repos/) for detailed information about working with repositories.   * **Activity** Displays the audit logs, a chronological list of activities that occur at organization and repository levels. It provides the org owners a report of all their team member activities. See [Audit logs](https://docs.docker.com/admin/organization/activity-logs/) for details.   * **Settings** : Displays information about your organization, and you to view and change your repository privacy settings, configure org permissions such as [Image Access Management](https://docs.docker.com/enterprise/security/hardened-desktop/image-access-management/), configure notification settings, and [deactivate](https://docs.docker.com/admin/organization/deactivate-account/#deactivate-an-organization) You can also update your organization name and company name that appear on your organization landing page. You must be an owner to access the organization's **Settings** page.   * **Billing** : Displays information about your existing [Docker subscription](https://docs.docker.com/subscription/), including the number of seats and next payment due date. For how to access the billing history and payment methods for your organization, see [View billing history](https://docs.docker.com/billing/history/).

## Merge organizations

> Warning >  > If you are merging organizations, it is recommended to do so at the _end_ of your billing cycle. When you merge an organization and downgrade another, you will lose seats on your downgraded organization. Docker does not offer refunds for downgrades.

If you have multiple organizations that you want to merge into one, complete the following steps:

  1. Based on the number of seats from the secondary organization, [purchase additional seats](https://docs.docker.com/subscription/manage-seats/) for the primary organization account that you want to keep.   2. Manually add users to the primary organization and remove existing users from the secondary organization.   3. Manually move over your data, including all repositories.   4. Once you're done moving all of your users and data, [downgrade](https://docs.docker.com/subscription/change/) the secondary account to a free subscription. Note that Docker does not offer refunds for downgrading organizations mid-billing cycle.

> Tip >  > If your organization has a Docker Business subscription with a purchase order, contact Support or your Account Manager at Docker.

## More resources

  * [Video: Docker Hub Organizations](https://www.youtube.com/watch?v=WKlT1O-4Du8)