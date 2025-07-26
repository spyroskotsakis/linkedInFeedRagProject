# Just-in-Time | Docker Docs

**URL:** https://docs.docker.com/enterprise/security/provisioning/just-in-time
**Word Count:** 1594
**Links Count:** 648
**Scraped:** 2025-07-16 02:03:45
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Just-in-Time provisioning

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Subscription: Business

For: Administrators

Just-in-Time \(JIT\) provisioning automatically creates and updates user accounts after every successful single sign-on \(SSO\) authentication. JIT verifies that the user signing in belongs to the organization and the teams assigned to them in your identity provider \(IdP\). When you [create your SSO connection](https://docs.docker.com/enterprise/security/single-sign-on/), JIT provisioning is turned on by default.

## SSO authentication with JIT provisioning enabled

When a user signs in with SSO and your SSO configuration has JIT provisioning enabled, the following steps occur automatically:

  1. The system checks if a Docker account exists for the user's email address.

     * If an account exists: The system uses the existing account and updates the user's full name if necessary.      * If no account exists: A new Docker account is created using basic user attributes \(email, name, and surname\). A unique username is generated based on the user's email, name, and random numbers to ensure all usernames are unique across the platform.   2. The system checks for any pending invitations to the SSO organization.

     * Invitation found: The invitation is automatically accepted.      * Invitation includes a specific group: The user is added to that group within the SSO organization.   3. The system verifies if the IdP has shared group mappings during authentication.

     * Group mappings provided: The user is assigned to the relevant organizations and teams.      * No group mappings provided: The system checks if the user is already part of the organization. If not, the user is added to the default organization and team configured in the SSO connection.

The following graphic provides an overview of SSO authentication with JIT enabled:

![JIT provisioning enabled](https://docs.docker.com/enterprise/security/images/jit-enabled-flow.svg)

![JIT provisioning enabled](https://docs.docker.com/enterprise/security/images/jit-enabled-flow.svg)

## SSO authentication with JIT provisioning disabled

When JIT provisioning is disabled in your SSO connection, the following actions occur during authentication:

  1. The system checks if a Docker account exists for the user's email address.

     * If an account exists: The system uses the existing account and updates the user's full name if necessary.      * If no account exists: A new Docker account is created using basic user attributes \(email, name, and surname\). A unique username is generated based on the user's email, name, and random numbers to ensure all usernames are unique across the platform.   2. The system checks for any pending invitations to the SSO organization.

     * Invitation found: If the user is a member of the organization or has a pending invitation, sign-in is successful, and the invitation is automatically accepted.      * No invitation found: If the user is not a member of the organization and has no pending invitation, the sign-in fails, and an `Access denied` error appears. The user must contact an administrator to be invited to the organization.

With JIT disabled, group mapping is only available if you have [SCIM enabled](https://docs.docker.com/enterprise/security/provisioning/scim/#enable-scim-in-docker). If SCIM is not enabled, users won't be auto-provisioned to groups.

The following graphic provides an overview of SSO authentication with JIT disabled:

![JIT provisioning disabled](https://docs.docker.com/enterprise/security/images/jit-disabled-flow.svg)

![JIT provisioning disabled](https://docs.docker.com/enterprise/security/images/jit-disabled-flow.svg)

## Disable JIT provisioning

> Warning >  > Disabling JIT provisioning may disrupt your users' access and workflows. With JIT disabled, users will not be automatically added to your organization. Users must already be a member of the organization or have a pending invitation to successfully sign in through SSO. To auto-provision users with JIT disabled, [use SCIM](https://docs.docker.com/enterprise/security/provisioning/scim/).

You may want to disable JIT provisioning for reasons such as the following:

  * You have multiple organizations, have SCIM enabled, and want SCIM to be the source of truth for provisioning   * You want to control and restrict usage based on your organization's security configuration, and want to use SCIM to provision access

Users are provisioned with JIT by default. If you enable SCIM, you can disable JIT:

  1. In [Docker Home](https://app.docker.com/), select your organization.   2. Select **Admin Console** , then **SSO and SCIM**.   3. In the SSO connections table, select the **Action** icon and then **Disable JIT provisioning**.   4. Select **Disable** to confirm.