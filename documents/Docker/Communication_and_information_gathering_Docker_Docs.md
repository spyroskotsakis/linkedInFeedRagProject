# Communication and information gathering | Docker Docs

**URL:** https://docs.docker.com/guides/admin-set-up/comms-and-info-gathering
**Word Count:** 510
**Links Count:** 73
**Scraped:** 2025-07-16 02:04:08
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

# Communication and information gathering

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Step one: Communicate with your developers and IT teams

### Docker user communication

You may already have Docker Desktop users within your company, and some steps in this process may affect how they interact with the platform. It's highly recommended to communicate early with users, informing them that as part of the subscription onboarding, they will be upgraded to a supported version of Docker Desktop.

Additionally, communicate that settings will be reviewed to optimize productivity, and users will be required to sign in to the companyâs Docker organization using their business email to fully utilize the subscription benefits.

### MDM team communication

Device management solutions, such as Intune and Jamf, are commonly used for software distribution across enterprises, typically managed by a dedicated MDM team. It is recommended that you engage with this team early in the process to understand their requirements and the lead time for deploying changes.

Several key setup steps in this guide require the use of JSON files, registry keys, or .plist files that need to be distributed to developer machines. Itâs a best practice to use MDM tools for deploying these configuration files and ensuring their integrity is preserved.

## Step two: Identify Docker organizations

Some companies may have more than one [Docker organization](https://docs.docker.com/admin/organization/) created. These organizations may have been created for specific purposes, or may not be needed anymore. If you suspect your company has more than one Docker organization, it's recommended you survey your teams to see if they have their own organizations. You can also contact your Docker Customer Success representative to get a list of organizations with users whose emails match your domain name.

## Step three: Gather requirements

Through [Settings Management](https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/), Docker provides numerous configuration parameters that can be preset. The Docker organization owner, development lead, and infosec representative should review these settings to establish the companyâs baseline configuration, including security features and [enforcing sign-in](https://docs.docker.com/enterprise/security/enforce-sign-in/) for Docker Desktop users. Additionally, they should decide whether to take advantage of other Docker products, such as [Docker Scout](https://docs.docker.com/scout/), which is included in the subscription.

To view the parameters that can be preset, see [Configure Settings Management](https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/configure-json-file/#step-two-configure-the-settings-you-want-to-lock-in).

## Optional step four: Meet with the Docker Implementation team

The Docker Implementation team can help you step through setting up your organization, configuring SSO, enforcing sign-in, and configuring Docker. You can reach out to set up a meeting by emailing [successteam@docker.com](mailto:successteam@docker.com).

[Finalize plans and begin setup Â»](https://docs.docker.com/guides/admin-set-up/finalize-plans-and-setup/)