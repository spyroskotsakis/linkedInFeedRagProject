# Personal settings | Docker Docs

**URL:** https://docs.docker.com/docker-hub/repos/settings/
**Word Count:** 1214
**Links Count:** 649
**Scraped:** 2025-07-16 01:48:31
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Personal settings for repositories

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

For your account, you can set personal settings for repositories, including default repository privacy and autobuild notifications.

## Default repository privacy

When creating a new repository in Docker Hub, you are able to specify the repository visibility. You can also change the visibility at any time in Docker Hub.

The default setting is useful if you use the `docker push` command to push to a repository that doesn't exist yet. In this case, Docker Hub automatically creates the repository with your default repository privacy.

### Configure default repository privacy

  1. Sign in to [Docker Hub](https://hub.docker.com).

  2. Select **My Hub** > **Settings** > **Default privacy**.

  3. Select the **Default privacy** for any new repository created.

     * **Public** : All new repositories appear in Docker Hub search results and can be pulled by everyone.      * **Private** : All new repositories don't appear in Docker Hub search results and are only accessible to you and collaborators. In addition, if the repository is created in an organization's namespace, then the repository is accessible to those with applicable roles or permissions.   4. Select **Save**.

## Autobuild notifications

You can send notifications to your email for all your repositories using autobuilds.

### Configure autobuild notifications

  1. Sign in to [Docker Hub](https://hub.docker.com).

  2. Select **My Hub** > **Repositories** > **Settings** > **Notifications**.

  3. Select the notifications to receive by email.

     * **Off** : No notifications.      * **Only failures** : Only notifications about failed builds.      * **Everything** : Notifications for successful and failed builds.   4. Select **Save**.