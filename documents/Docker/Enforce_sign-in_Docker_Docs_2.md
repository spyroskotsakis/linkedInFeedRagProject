# Enforce sign-in | Docker Docs

**URL:** https://docs.docker.com/enterprise/security/enforce-sign-in/
**Word Count:** 1376
**Links Count:** 653
**Scraped:** 2025-07-16 01:47:29
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Enforce sign-in for Docker Desktop

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Subscription: Team Business

For: Administrators

By default, members of your organization can use Docker Desktop without signing in. When users donât sign in as a member of your organization, they donât receive the [benefits of your organizationâs subscription](https://docs.docker.com/subscription/details/) and they can circumvent [Dockerâs security features](https://docs.docker.com/enterprise/security/hardened-desktop/) for your organization.

There are multiple methods for enforcing sign-in, depending on your companies' set up and preferences:

  * [Registry key method \(Windows only\)](https://docs.docker.com/enterprise/security/enforce-sign-in/methods/#registry-key-method-windows-only) New   * [Configuration profiles method \(Mac only\)](https://docs.docker.com/enterprise/security/enforce-sign-in/methods/#configuration-profiles-method-mac-only) New   * [`.plist` method \(Mac only\)](https://docs.docker.com/enterprise/security/enforce-sign-in/methods/#plist-method-mac-only) New   * [`registry.json` method \(All\)](https://docs.docker.com/enterprise/security/enforce-sign-in/methods/#registryjson-method-all)

## How is sign-in enforced?

When Docker Desktop starts and it detects a registry key, `.plist` file, or `registry.json` file, the following occurs:

  * A **Sign in required\!** prompt appears requiring the user to sign in as a member of your organization to use Docker Desktop.![Enforce Sign-in Prompt](https://docs.docker.com/enterprise/images/enforce-sign-in.png)

![Enforce Sign-in Prompt](https://docs.docker.com/enterprise/images/enforce-sign-in.png)

  * When a user signs in to an account that isnât a member of your organization, they are automatically signed out and canât use Docker Desktop. The user can select **Sign in** and try again.   * When a user signs in to an account that is a member of your organization, they can use Docker Desktop.   * When a user signs out, the **Sign in required\!** prompt appears and they can no longer use Docker Desktop.

> Note >  > Enforcing sign-in for Docker Desktop does not impact accessing the Docker CLI. CLI access is only impacted for organizations that enforce single sign-on.

## Enforcing sign-in versus enforcing single sign-on \(SSO\)

[Enforcing SSO](https://docs.docker.com/enterprise/security/single-sign-on/connect/#optional-enforce-sso) and enforcing sign-in are different features. The following table provides a description and benefits when using each feature.

Enforcement| Description| Benefits   ---|---|---   Enforce sign-in only| Users must sign in before using Docker Desktop.| Ensures users receive the benefits of your subscription and ensures security features are applied. In addition, you gain insights into usersâ activity.   Enforce single sign-on \(SSO\) only| If users sign in, they must sign in using SSO.| Centralizes authentication and enforces unified policies set by the identity provider.   Enforce both| Users must sign in using SSO before using Docker Desktop.| Ensures users receive the benefits of your subscription and ensures security features are applied. In addition, you gain insights into usersâ activity. Finally, it centralizes authentication and enforces unified policies set by the identity provider.   Enforce neither| If users sign in, they can use SSO or their Docker credentials.| Lets users access Docker Desktop without barriers, but at the cost of reduced security and insights.      ## What's next?

  * To enforce sign-in, review the [Methods](https://docs.docker.com/enterprise/security/enforce-sign-in/methods/) guide.   * To enforce SSO, review the [Enforce SSO](https://docs.docker.com/enterprise/security/single-sign-on/connect/) steps.