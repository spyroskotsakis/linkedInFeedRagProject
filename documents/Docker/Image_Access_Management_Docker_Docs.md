# Image Access Management | Docker Docs

**URL:** http://docs.docker.com/admin/organization/image-access
**Word Count:** 1667
**Links Count:** 653
**Scraped:** 2025-07-16 02:11:42
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](http://docs.docker.com/get-started/)   * [Guides](http://docs.docker.com/guides/)   * [Reference](http://docs.docker.com/reference/)

* * *

# Image Access Management

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Subscription: Business

For: Administrators

Image Access Management gives you control over which types of images, such as Docker Official Images, Docker Verified Publisher Images, or community images, your developers can pull from Docker Hub.

For example, a developer, who is part of an organization, building a new containerized application could accidentally use an untrusted, community image as a component of their application. This image could be malicious and pose a security risk to the company. Using Image Access Management, the organization owner can ensure that the developer can only access trusted content like Docker Official Images, Docker Verified Publisher Images, or the organizationâs own images, preventing such a risk.

## Prerequisites

You first need to [enforce sign-in](https://docs.docker.com/enterprise/security/enforce-sign-in/) to ensure that all Docker Desktop developers authenticate with your organization. Since Image Access Management requires a Docker Business subscription, enforced sign-in guarantees that only authenticated users have access and that the feature consistently takes effect across all users, even though it may still work without enforced sign-in.

> Important >  > You must use [personal access tokens \(PATs\)](https://docs.docker.com/security/for-developers/access-tokens/) with Image Access Management. Organization access tokens \(OATs\) are not compatible.

## Configure

Admin Console  Docker Hub

  1. Sign in to [Docker Home](https://app.docker.com/) and select your organization..   2. Select **Admin Console** , then **Image access**.   3. Enable Image Access Management to set the permissions for the following categories of images you can manage:

  * **Organization Images** : Images from your organization are always allowed by default. These images can be public or private created by members within your organization.   * **Docker Official Images** : A curated set of Docker repositories hosted on Hub. They provide OS repositories, best practices for Dockerfiles, drop-in solutions, and applies security updates on time.   * **Docker Verified Publisher Images** : Images published by Docker partners that are part of the Verified Publisher program and are qualified to be included in the developer secure supply chain.   * **Community Images** : These images are disabled by default when Image Access Management is enabled because various users contribute them and they may pose security risks. This category includes Docker-Sponsored Open Source images.

> Note >  > Image Access Management is turned off by default. However, owners in your organization have access to all images regardless of the settings.

  4. Select the category restrictions for your images by selecting **Allowed**. Once the restrictions are applied, your members can view the organization permissions page in a read-only format.

## Verify the restrictions

The new Image Access Management policy takes effect after the developer successfully authenticates to Docker Desktop using their organization credentials. If a developer attempts to pull a disallowed image type using Docker, they receive an error message.

> Important >  > Organization management is moving to the Admin Console. >  > Manage members, team, settings, and activity logs in the Docker Admin Console. Access to these features in Docker Hub will end soon. Explore the [Admin Console](https://app.docker.com/admin).

  1. Sign in to [Docker Hub](https://hub.docker.com).   2. Select **My Hub** , select your organization in the left navigation drop-down menu, and then select **Image access**.   3. Enable Image Access Management to set the permissions for the following categories of images you can manage:

  * **Organization Images** : Images from your organization are always allowed by default. These images can be public or private created by members within your organization.   * **Docker Official Images** : A curated set of Docker repositories hosted on Hub. They provide OS repositories, best practices for Dockerfiles, drop-in solutions, and applies security updates on time.   * **Docker Verified Publisher Images** : Images published by Docker partners that are part of the Verified Publisher program and are qualified to be included in the developer secure supply chain.   * **Community Images** : These images are disabled by default when Image Access Management is enabled because various users contribute them and they may pose security risks. This category includes Docker-Sponsored Open Source images.

> Note >  > Image Access Management is turned off by default. However, owners in your organization have access to all images regardless of the settings.

  4. Select the category restrictions for your images by selecting **Allowed**. Once the restrictions are applied, your members can view the organization permissions page in a read-only format.

## Verify the restrictions

The new Image Access Management policy takes effect after the developer successfully authenticates to Docker Desktop using their organization credentials. If a developer attempts to pull a disallowed image type using Docker, they receive an error message.

## More resources

  * [Video: Hardened Desktop Image Access Management](https://www.youtube.com/watch?v=r3QRKHA1A5U)