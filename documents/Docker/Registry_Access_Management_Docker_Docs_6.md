# Registry Access Management | Docker Docs

**URL:** https://docs.docker.com/security/for-admins/hardened-desktop/registry-access-management
**Word Count:** 2062
**Links Count:** 663
**Scraped:** 2025-07-16 02:04:23
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Registry Access Management

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Subscription: Business

For: Administrators

With Registry Access Management \(RAM\), administrators can ensure that their developers using Docker Desktop only access allowed registries. This is done through the Registry Access Management dashboard in Docker Hub or the Docker Admin Console.

Registry Access Management supports both cloud and on-prem registries. This feature operates at the DNS level and therefore is compatible with all registries. You can add any hostname or domain name youâd like to include in the list of allowed registries. However, if the registry redirects to other domains such as `s3.amazon.com`, then you must add those domains to the list.

Example registries administrators can allow include:

  * Docker Hub. This is enabled by default.   * Amazon ECR   * GitHub Container Registry   * Google Container Registry   * GitLab Container Registry   * Nexus   * Artifactory

## Prerequisites

You must [enforce sign-in](https://docs.docker.com/enterprise/security/enforce-sign-in/). For Registry Access Management to take effect, Docker Desktop users must authenticate to your organization. Enforcing sign-in ensures that your Docker Desktop developers always authenticate to your organization, even though they can authenticate without it and the feature will take effect. Enforcing sign-in guarantees the feature always takes effect.

> Important >  > You must use [personal access tokens \(PATs\)](https://docs.docker.com/security/for-developers/access-tokens/) with Registry Access Management. Organization access tokens \(OATs\) are not compatible.

## Configure Registry Access Management permissions

Admin Console  Docker Hub

To configure Registry Access Management permissions, perform the following steps:

  1. Sign in to [Docker Home](https://app.docker.com/) and select your organization..

  2. Select **Admin Console** , then **Registry access**.

  3. Enable Registry Access Management to set the permissions for your registry.

> Note >  > When enabled, the Docker Hub registry is set by default; however you can also restrict this registry for your developers.

  4. Select **Add registry** and enter your registry details in the applicable fields, and then select **Create** to add the registry to your list. You can add up to 100 registries/domains.

  5. Verify that the registry appears in your list and select **Save changes**.

Once you add a registry, it can take up to 24 hours for the changes to be enforced on your developersâ machines.

If you want to apply the changes sooner, you must force a Docker signout on your developersâ machine and have the developers re-authenticate for Docker Desktop. See the Caveats section below to learn more about limitations.

> Important >  > Starting with Docker Desktop version 4.36, you can enforce sign-in for multiple organizations. If a developer belongs to multiple organizations with different RAM policies, only the RAM policy for the first organization listed in the `registry.json` file, `.plist` file, or registry key is enforced.

> Tip >  > Since RAM sets policies about where content can be fetched from, the [ADD](https://docs.docker.com/reference/dockerfile/#add) instruction of the Dockerfile when the parameter of the ADD instruction is a URL is also subject to registry restrictions. >  > If you're using ADD to fetch an image or artifact from a trusted registry via URL, make sure the registry's domain is included in your organzation's allowed registries list. >  > RAM is not intended to restrict access to general-purpose external URLs, for example, package mirrors or storage services. Attempting to add too many domains may cause errors or hit system limits.

> Important >  > Organization management is moving to the Admin Console. >  > Manage members, team, settings, and activity logs in the Docker Admin Console. Access to these features in Docker Hub will end soon. Explore the [Admin Console](https://app.docker.com/admin).

To configure Registry Access Management permissions, perform the following steps:

  1. Sign in to [Docker Hub](https://hub.docker.com).

  2. Select **My Hub** , your organization, **Settings** , and then select **Registry Access**.

  3. Enable Registry Access Management to set the permissions for your registry.

> Note >  > When enabled, the Docker Hub registry is set by default; however you can also restrict this registry for your developers.

  4. Select **Add registry** and enter your registry details in the applicable fields, and then select **Create** to add the registry to your list. You can add up to 100 registries/domains.

  5. Verify that the registry appears in your list and select **Save changes**.

Once you add a registry, it can take up to 24 hours for the changes to be enforced on your developersâ machines.

If you want to apply the changes sooner, you must force a Docker signout on your developersâ machine and have the developers re-authenticate for Docker Desktop. See the Caveats section below to learn more about limitations.

> Important >  > Starting with Docker Desktop version 4.36, you can enforce sign-in for multiple organizations. If a developer belongs to multiple organizations with different RAM policies, only the RAM policy for the first organization listed in the `registry.json` file, `.plist` file, or registry key is enforced.

> Tip >  > Since RAM sets policies about where content can be fetched from, the [ADD](https://docs.docker.com/reference/dockerfile/#add) instruction of the Dockerfile when the parameter of the ADD instruction is a URL is also subject to registry restrictions. >  > If you're using ADD to fetch an image or artifact from a trusted registry via URL, make sure the registry's domain is included in your organzation's allowed registries list. >  > RAM is not intended to restrict access to general-purpose external URLs, for example, package mirrors or storage services. Attempting to add too many domains may cause errors or hit system limits.

## Verify the restrictions

The new Registry Access Management policy takes effect after the developer successfully authenticates to Docker Desktop using their organization credentials. If a developer attempts to pull an image from a disallowed registry via the Docker CLI, they receive an error message that the organization has disallowed this registry.

## Caveats

There are certain limitations when using Registry Access Management:

  * You can add up to 100 registries/domains.   * Windows image pulls and image builds are not restricted by default. For Registry Access Management to take effect on Windows Container mode, you must allow the Windows Docker daemon to use Docker Desktop's internal proxy by selecting the [Use proxy for Windows Docker daemon](https://docs.docker.com/desktop/settings-and-maintenance/settings/#proxies) setting.   * Builds such as `docker buildx` using a Kubernetes driver are not restricted.   * Builds such as `docker buildx` using a custom docker-container driver are not restricted.   * Blocking is DNS-based. You must use a registry's access control mechanisms to distinguish between âpushâ and âpullâ.   * WSL 2 requires at least a 5.4 series Linux kernel \(this does not apply to earlier Linux kernel series\).   * Under the WSL 2 network, traffic from all Linux distributions is restricted. This will be resolved in the updated 5.15 series Linux kernel.   * Images pulled by Docker Desktop when Docker Debug or Kubernetes is enabled, are not restricted by default even if Docker Hub is blocked by RAM.   * If Docker Hub access is restricted by RAM, pulls on images originating from Docker Hub are restricted even if the image has been previously cached by a registry mirror. See [Using Registry Access Management \(RAM\) with a registry mirror](https://docs.docker.com/docker-hub/image-library/mirror/).

Also, Registry Access Management operates on the level of hosts, not IP addresses. Developers can bypass this restriction within their domain resolution, for example by running Docker against a local proxy or modifying their operating system's `sts` file. Blocking these forms of manipulation is outside the remit of Docker Desktop.

## More resources

  * [Video: Hardened Desktop Registry Access Management](https://www.youtube.com/watch?v=l9Z6WJdJC9A)