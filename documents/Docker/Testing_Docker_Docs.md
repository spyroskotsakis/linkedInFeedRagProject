# Testing | Docker Docs

**URL:** https://docs.docker.com/guides/admin-set-up/testing
**Word Count:** 369
**Links Count:** 69
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

# Testing

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## SSO and SCIM testing

You can test SSO and SCIM by signing in to Docker Desktop or Docker Hub with the email address linked to a Docker account that is part of the verified domain. Developers who sign in using their Docker usernames will remain unaffected by the SSO and/or SCIM setup.

> Important >  > Some users may need CLI based logins to Docker Hub, and for this they will need a [personal access token \(PAT\)](https://docs.docker.com/security/for-developers/access-tokens/).

## Test RAM and IAM

> Warning >  > Be sure to communicate with your users before proceeding, as this step will impact all existing users signing into your Docker organization

If you plan to use [Registry Access Management \(RAM\)](https://docs.docker.com/enterprise/security/hardened-desktop/registry-access-management/) and/or [Image Access Management \(IAM\)](https://docs.docker.com/enterprise/security/hardened-desktop/image-access-management/), ensure your test developer signs in to Docker Desktop using their organization credentials. Once authenticated, have them attempt to pull an unauthorized image or one from a disallowed registry via the Docker CLI. They should receive an error message indicating that the registry is restricted by the organization.

## Deploy settings and enforce sign in to test group

Deploy the Docker settings and enforce sign-in for a small group of test users via MDM. Have this group test their development workflows with containers on Docker Desktop and Docker Hub to ensure all settings and the sign-in enforcement function as expected.

## Test Docker Build Cloud capabilities

Have one of your Docker Desktop testers [connect to the cloud builder you created and use it to build](https://docs.docker.com/build-cloud/usage/).

## Verify Docker Scout monitoring of repositories

Check the [Docker Scout dashboard](https://scout.docker.com/) to confirm that data is being properly received for the repositories where Docker Scout has been enabled.

[Deploy Â»](https://docs.docker.com/guides/admin-set-up/deploy/)