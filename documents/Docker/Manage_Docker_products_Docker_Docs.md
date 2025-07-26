# Manage Docker products | Docker Docs

**URL:** https://docs.docker.com/admin/organization/manage-products
**Word Count:** 1357
**Links Count:** 673
**Scraped:** 2025-07-16 02:02:47
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Manage Docker products

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Subscription: Team Business

For: Administrators

In this section, learn how to manage access and view usage of the Docker products for your organization. For more detailed information about each product, including how to set up and configure them, see the following manuals:

  * [Docker Desktop](https://docs.docker.com/desktop/)   * [Docker Hub](https://docs.docker.com/docker-hub/)   * [Docker Build Cloud](https://docs.docker.com/build-cloud/)   * [Docker Scout](https://docs.docker.com/scout/)   * [Testcontainers Cloud](https://testcontainers.com/cloud/docs/#getting-started)

## Manage product access for your organization

Access to the Docker products included in your subscription is turned on by default for all users. For an overview of products included in your subscription, see [Docker subscriptions and features](https://docs.docker.com/subscription/details/).

Docker Desktop  Docker Hub  Docker Build Cloud  Docker Scout  Testcontainers Cloud

### Manage Docker Desktop access

To manage Docker Desktop access:

  1. [Enforce sign-in](https://docs.docker.com/enterprise/security/enforce-sign-in/).   2. Manage members [manually](https://docs.docker.com/admin/organization/members/) or use [provisioning](https://docs.docker.com/enterprise/security/provisioning/).

With sign-in enforced, only users who are a member of your organization can use Docker Desktop after signing in.

### Manage Docker Hub access

To manage Docker Hub access, sign in to [Docker Home](https://app.docker.com/) and configure [Registry Access Management](https://docs.docker.com/enterprise/security/hardened-desktop/registry-access-management/) or [Image Access Management](https://docs.docker.com/enterprise/security/hardened-desktop/image-access-management/).

### Manage Docker Build Cloud access

To initially set up and configure Docker Build Cloud, sign in to [Docker Build Cloud](https://app.docker.com/build) and follow the on-screen instructions.

To manage Docker Build Cloud access:

  1. Sign in to [Docker Build Cloud](http://app.docker.com/build) as an organization owner.   2. Select **Account settings**.   3. Select **Lock access to Docker Build Account**.

### Manage Docker Scout access

To initially set up and configure Docker Scout, sign in to [Docker Scout](https://scout.docker.com/) and follow the on-screen instructions.

To manage Docker Scout access:

  1. Sign in to [Docker Scout](https://scout.docker.com/) as an organization owner.   2. Select your organization, then **Settings**.   3. To manage what repositories are enabled for Docker Scout analysis, select **Repository settings**. For more information on, see [repository settings](https://docs.docker.com/scout/explore/dashboard/#repository-settings).   4. To manage access to Docker Scout for use on local images with Docker Desktop, use [Settings Management](https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/) and set `sbomIndexing` to `false` to disable, or to `true` to enable.

### Manage Testcontainers Cloud access

To initially set up and configure Testcontainers Cloud, sign in to [Testcontainers Cloud](https://app.testcontainers.cloud/) and follow the on-screen instructions.

To manage access to Testcontainers Cloud:

  1. Sign in to the [Testcontainers Cloud](https://app.testcontainers.cloud/) and select **Account**.   2. Select **Settings** , then **Lock access to Testcontainers Cloud**.

## Monitor product usage for your organization

To view usage for Docker products:

  * Docker Desktop: View the **Insights** page in [Docker Home](https://app.docker.com/). For more details, see [Insights](https://docs.docker.com/admin/organization/insights/).   * Docker Hub: View the [**Usage** page](https://hub.docker.com/usage) in Docker Hub.   * Docker Build Cloud: View the **Build minutes** page in [Docker Build Cloud](http://app.docker.com/build).   * Docker Scout: View the [**Repository settings** page](https://scout.docker.com/settings/repos) in Docker Scout.   * Testcontainers Cloud: View the [**Billing** page](https://app.testcontainers.cloud/dashboard/billing) in Testcontainers Cloud.

If your usage or seat count exceeds your subscription amount, you can [scale your subscription](https://docs.docker.com/subscription/scale/) to meet your needs.