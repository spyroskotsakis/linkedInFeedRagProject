# Finalize plans and begin setup | Docker Docs

**URL:** https://docs.docker.com/guides/admin-set-up/finalize-plans-and-setup
**Word Count:** 540
**Links Count:** 77
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

# Finalize plans and begin setup

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Step one: Send finalized settings files to the MDM team

After reaching an agreement with the relevant teams about your baseline and security configurations as outlined in module one, configure Settings Management using either the [Docker Admin Console](https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/configure-admin-console/) or an [`admin-settings.json` file](https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/configure-json-file/).

Once the file is ready, collaborate with your MDM team to deploy your chosen settings, along with your chosen method for [enforcing sign-in](https://docs.docker.com/enterprise/security/enforce-sign-in/).

> Important >  > Itâs highly recommended that you test this first with a small number of Docker Desktop developers to verify the functionality works as expected before deploying more widely.

## Step two: Manage your organizations

If you have more than one organization, itâs recommended that you either consolidate them into one organization or create a [Docker company](https://docs.docker.com/admin/company/) to manage multiple organizations. Work with the Docker Customer Success and Implementation teams to make this happen.

## Step three: Begin setup

### Set up single sign-on SSO domain verification

Single sign-on \(SSO\) lets developers authenticate using their identity providers \(IdPs\) to access Docker. SSO is available for a whole company, and all associated organizations, or an individual organization that has a Docker Business subscription. For more information, see the [documentation](https://docs.docker.com/enterprise/security/single-sign-on/).

You can also enable [SCIM](https://docs.docker.com/enterprise/security/provisioning/scim/) for further automation of provisioning and deprovisioning of users.

### Set up Docker product entitlements included in the subscription

[Docker Build Cloud](https://docs.docker.com/build-cloud/) significantly reduces build times, both locally and in CI, by providing a dedicated remote builder and shared cache. Powered by the cloud, developer time and local resources are freed up so your team can focus on more important things, like innovation. To get started, [set up a cloud builder](https://app.docker.com/build/).

[Docker Scout](https://docs.docker.com/scout/) is a solution for proactively enhancing your software supply chain security. By analyzing your images, Docker Scout compiles an inventory of components, also known as a Software Bill of Materials \(SBOM\). The SBOM is matched against a continuously updated vulnerability database to pinpoint security weaknesses. To get started, see [Quickstart](https://docs.docker.com/scout/quickstart/).

### Ensure you're running a supported version of Docker Desktop

> Warning >  > This step could affect the experience for users on older versions of Docker Desktop.

Existing users may be running outdated or unsupported versions of Docker Desktop. It is highly recommended that all users update to a supported version. Docker Desktop versions released within the past 6 months from the latest release are supported.

It's recommended that you use a MDM solution to manage the version of Docker Desktop for users. Users may also get Docker Desktop directly from Docker or through a company software portal.

[Testing Â»](https://docs.docker.com/guides/admin-set-up/testing/)