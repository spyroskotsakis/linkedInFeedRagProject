# Deploy | Docker Docs

**URL:** https://docs.docker.com/guides/admin-set-up/deploy
**Word Count:** 221
**Links Count:** 54
**Scraped:** 2025-07-16 02:04:23
**Status:** completed

---

Back

[Guides](https://docs.docker.com/guides/)

  * [Get started](https://docs.docker.com/get-started/)   * [Manuals](https://docs.docker.com/manuals/)   * [Reference](https://docs.docker.com/reference/)

* * *

[Set up your company for success with Docker](https://docs.docker.com/guides/admin-set-up/)

Get the most out of Docker by streamlining workflows, standardizing development environments, and ensuring smooth deployments across your company.

[ Administration](https://docs.docker.com/tags/admin/)

20 minutes

[1](https://docs.docker.com/guides/admin-set-up/comms-and-info-gathering/)

[Communication and information gathering](https://docs.docker.com/guides/admin-set-up/comms-and-info-gathering/)

[2](https://docs.docker.com/guides/admin-set-up/finalize-plans-and-setup/)

[Finalize plans and begin setup](https://docs.docker.com/guides/admin-set-up/finalize-plans-and-setup/)

[3](https://docs.docker.com/guides/admin-set-up/testing/)

[Testing](https://docs.docker.com/guides/admin-set-up/testing/)

[4](https://docs.docker.com/guides/admin-set-up/deploy/)

[Deploy](https://docs.docker.com/guides/admin-set-up/deploy/)

Resources:

  * [Overview of Administration in Docker](https://docs.docker.com/admin/)   * [Single sign-on](https://docs.docker.com/security/for-admins/single-sign-on/)   * [Enforce sign-in](https://docs.docker.com/security/for-admins/enforce-sign-in/)   * [Roles and permissions](https://docs.docker.com/security/for-admins/roles-and-permissions/)   * [Settings Management](https://docs.docker.com/security/for-admins/hardened-desktop/settings-management/)   * [Registry Access Management](https://docs.docker.com/security/for-admins/hardened-desktop/registry-access-management/)   * [Image Access Management](https://docs.docker.com/security/for-admins/hardened-desktop/image-access-management/)   * [Docker subscription information](https://docs.docker.com/subscription/details/)

[Â« Back to all guides](https://docs.docker.com/guides/)

# Deploy

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

> Warning >  > Ensure you communicate with your users before proceeding, and confirm that your IT and MDM teams are prepared to handle any unexpected issues, as these steps will affect all existing users signing into your Docker organization.

## Step one: Enforce SSO

Enforcing SSO means that anyone who has a Docker profile with an email address that matches your verified domain must sign in using your SSO connection. Make sure the Identity provider groups associated with your SSO connection cover all the developer groups that you want to have access to the Docker subscription.

## Step two: Deploy configuration settings and enforce sign-in to users

Have the MDM team deploy the configuration files for Docker to all users.

Congratulations, you have successfully completed the admin implementation process for Docker.