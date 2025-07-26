# Onboarding and managing roles and permissions in Docker | Docker Docs

**URL:** https://docs.docker.com/guides/admin-user-management/onboard/
**Word Count:** 514
**Links Count:** 73
**Scraped:** 2025-07-16 01:47:07
**Status:** completed

---

Back

[Guides](https://docs.docker.com/guides/)

  * [Get started](https://docs.docker.com/get-started/)   * [Manuals](https://docs.docker.com/manuals/)   * [Reference](https://docs.docker.com/reference/)

* * *

[Mastering user and access management](https://docs.docker.com/guides/admin-user-management/)

Simplify user access while ensuring security and efficiency in Docker.

[ Administration](https://docs.docker.com/tags/admin/)

20 minutes

[1](https://docs.docker.com/guides/admin-user-management/setup/)

[Setting up roles and permissions in Docker](https://docs.docker.com/guides/admin-user-management/setup/)

[2](https://docs.docker.com/guides/admin-user-management/onboard/)

[Onboarding and managing roles and permissions in Docker](https://docs.docker.com/guides/admin-user-management/onboard/)

[3](https://docs.docker.com/guides/admin-user-management/audit-and-monitor/)

[Monitoring and insights](https://docs.docker.com/guides/admin-user-management/audit-and-monitor/)

Resources:

  * [Overview of Administration in Docker](https://docs.docker.com/admin/)   * [Single sign-on](https://docs.docker.com/security/for-admins/single-sign-on/)   * [Onboard your organization](https://docs.docker.com/admin/organization/onboard/)   * [Roles and permissions](https://docs.docker.com/security/for-admins/roles-and-permissions/)   * [Insights](https://docs.docker.com/admin/organization/insights/)   * [Activity logs](https://docs.docker.com/admin/organization/activity-logs/)

[Â« Back to all guides](https://docs.docker.com/guides/)

# Onboarding and managing roles and permissions in Docker

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

This page guides you through onboarding owners and members, and using tools like SSO and SCIM to future-proof onboarding going forward.

## Step 1: Invite owners

When you create a Docker organization, you automatically become its sole owner. While optional, adding additional owners can significantly ease the process of onboarding and managing your organization by distributing administrative responsibilities. It also ensures continuity and does not cause a blocker if the primary owner is unavailable.

For detailed information on owners, see [Roles and permissions](https://docs.docker.com/enterprise/security/roles-and-permissions/).

## Step 2: Invite members and assign roles

Members are granted controlled access to resources and enjoy enhanced organizational benefits. When you invite members to join you Docker organization, you immediately assign them a role.

### Benefits of inviting members

  * Enhanced visibility: Gain insights into user activity, making it easier to monitor access and enforce security policies.

  * Streamlined collaboration: Help members collaborate effectively by granting access to shared resources and repositories.

  * Improved resource management: Organize and track users within your organization, ensuring optimal allocation of resources.

  * Access to enhanced features: Members benefit from organization-wide perks, such as increased pull limits and access to premium Docker features.

  * Security control: Apply and enforce security settings at an organizational level, reducing risks associated with unmanaged accounts.

For detailed information, see [Manage organization members](https://docs.docker.com/admin/organization/members/).

## Step 3: Future-proof user management

A robust, future-proof approach to user management combines automated provisioning, centralized authentication, and dynamic access control. Implementing these practices ensures a scalable, secure, and efficient environment.

### Secure user authentication with single sign-on \(SSO\)

Integrating Docker with your identity provider streamlines user access and enhances security.

SSO:

  * Simplifies sign in, as users sign in with their organizational credentials.

  * Reduces password-related vulnerabilities.

  * Simplifies onboarding as it works seamlessly with SCIM and group mapping for automated provisioning.

[SSO documentation](https://docs.docker.com/enterprise/security/single-sign-on/).

### Automate onboarding with SCIM and JIT provisioning

Streamline user provisioning and role management with [SCIM](https://docs.docker.com/enterprise/security/provisioning/scim/) and [Just-in-Time \(JIT\) provisioning](https://docs.docker.com/enterprise/security/provisioning/just-in-time/).

With SCIM you can:

  * Sync users and roles automatically with your identity provider.

  * Automate adding, updating, or removing users based on directory changes.

With JIT provisioning you can:

  * Automatically add users upon first sign in based on group mapping.

  * Reduce overhead by eliminating pre-invite steps.

### Simplify access with group mapping

Group mapping automates permissions management by linking identity provider groups to Docker roles and teams.

It also:

  * Reduces manual errors in role assignments.

  * Ensures consistent access control policies.

  * Help you scale permissions as teams grow or change.

For more information on how it works, see [Group mapping](https://docs.docker.com/enterprise/security/provisioning/group-mapping/).

[Monitoring and insights Â»](https://docs.docker.com/guides/admin-user-management/audit-and-monitor/)