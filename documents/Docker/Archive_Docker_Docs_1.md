# Archive | Docker Docs

**URL:** https://docs.docker.com/docker-hub/repos/archive/
**Word Count:** 1201
**Links Count:** 644
**Scraped:** 2025-07-16 01:47:50
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Archive or unarchive a repository

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

You can archive a repository on Docker Hub to mark it as read-only and indicate that it's no longer actively maintained. This helps prevent the use of outdated or unsupported images in workflows. Archived repositories can also be unarchived if needed.

Docker Hub highlights repositories that haven't been updated in over a year by displaying an icon \( ![outdated icon](https://docs.docker.com/docker-hub/repos/images/outdated-icon.webp) \) next to them on the [**Repositories** page](https://hub.docker.com/repositories/). Consider reviewing these highlighted repositories and archiving them if necessary.

When a repository is archived, the following occurs:

  * The repository information can't be modified.   * New images can't be pushed to the repository.   * An **Archived** label is displayed on the public repository page.   * Users can still pull the images.

You can unarchive an archived repository to remove the archived state. When unarchived, the following occurs:

  * The repository information can be modified.   * New images can be pushed to the repository.   * The **Archived** label is removed on the public repository page.

## Archive a repository

  1. Sign in to [Docker Hub](https://hub.docker.com).

  2. Select **My Hub** > **Repositories**.

A list of your repositories appears.

  3. Select a repository.

The **General** page for the repository appears.

  4. Select the **Settings** tab.

  5. Select **Archive repository**.

  6. Enter the name of your repository to confirm.

  7. Select **Archive**.

## Unarchive a repository

  1. Sign in to [Docker Hub](https://hub.docker.com).

  2. Select **My Hub** > **Repositories**.

A list of your repositories appears.

  3. Select a repository.

The **General** page for the repository appears.

  4. Select the **Settings** tab.

  5. Select **Unarchive repository**.