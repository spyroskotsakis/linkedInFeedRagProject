# Tags | Docker Docs

**URL:** https://docs.docker.com/docker-hub/repos/manage/hub-images/tags/
**Word Count:** 1212
**Links Count:** 648
**Scraped:** 2025-07-16 01:46:47
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Tags on Docker Hub

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Tags let you manage multiple versions of images within a single Docker Hub repository. By adding a specific `:<tag>` to each image, such as `docs/base:testing`, you can organize and differentiate image versions for various use cases. If no tag is specified, the image defaults to the `latest` tag.

## Tag a local image

To tag a local image, use one of the following methods:

  * When you build an image, use `docker build -t <org-or-user-namespace>/<repo-name>[:<tag>`.   * Re-tag an existing local image with `docker tag <existing-image> <org-or-user-namespace>/<repo-name>[:<tag>]`.   * When you commit changes, use `docker commit <existing-container> <org-or-user-namespace>/<repo-name>[:<tag>]`.

Then, you can push this image to the repository designated by its name or tag:               $ docker push <org-or-user-namespace>/<repo-name>:<tag>     

The image is then uploaded and available for use in Docker Hub.

## View repository tags

You can view the available tags and the size of the associated image.

  1. Sign in to [Docker Hub](https://hub.docker.com).

  2. Select **My Hub** > **Repositories**.

A list of your repositories appears.

  3. Select a repository.

The **General** page for the repository appears.

  4. Select the **Tags** tab.

You can select a tag's digest to see more details.

## Delete repository tags

Only the repository owner or other team members with granted permissions can delete tags.

  1. Sign in to [Docker Hub](https://hub.docker.com).

  2. Select **My Hub** > **Repositories**.

A list of your repositories appears.

  3. Select a repository.

The **General** page for the repository appears.

  4. Select the **Tags** tab.

  5. Select the corresponding checkbox next to the tags to delete.

  6. Select **Delete**.

A confirmation dialog appears.

  7. Select **Delete**.