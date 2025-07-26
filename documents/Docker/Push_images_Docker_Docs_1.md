# Push images | Docker Docs

**URL:** https://docs.docker.com/docker-hub/repos/manage/hub-images/push/
**Word Count:** 1123
**Links Count:** 637
**Scraped:** 2025-07-16 01:47:50
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Push images to a repository

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

* * *

To add content to a repository on Docker Hub, you need to tag your Docker image and then push it to your repository. This process lets you share your images with others or use them in different environments.

  1. Tag your Docker image.

The `docker tag` command assigns a tag to your Docker image, which includes your Docker Hub namespace and the repository name. The general syntax is:                    $ docker tag [SOURCE_IMAGE[:TAG]] [NAMESPACE/REPOSITORY[:TAG]]          

Example:

If your local image is called `my-app` and you want to tag it for the repository `my-namespace/my-repo` with the tag `v1.0`, run:                    $ docker tag my-app my-namespace/my-repo:v1.0          

  2. Push the image to Docker Hub.

Use the `docker push` command to upload your tagged image to the specified repository on Docker Hub.

Example:                    $ docker push my-namespace/my-repo:v1.0          

This command pushes the image tagged `v1.0` to the `my-namespace/my-repo` repository.

  3. Verify the image on Docker Hub.