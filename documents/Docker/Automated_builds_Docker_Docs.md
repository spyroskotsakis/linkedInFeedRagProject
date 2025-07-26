# Automated builds | Docker Docs

**URL:** https://docs.docker.com/docker-hub/repos/manage/builds
**Word Count:** 1241
**Links Count:** 638
**Scraped:** 2025-07-16 02:02:47
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Automated builds

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

* * *

Subscription: Pro Team Business

Docker Hub can automatically build images from source code in an external repository and automatically push the built image to your Docker repositories.

![An automated build dashboard](https://docs.docker.com/docker-hub/repos/manage/builds/images/index-dashboard.png)

![An automated build dashboard](https://docs.docker.com/docker-hub/repos/manage/builds/images/index-dashboard.png)

When you set up automated builds, also called autobuilds, you create a list of branches and tags that you want to build into Docker images. When you push code to a source-code branch, for example in GitHub, for one of those listed image tags, the push uses a webhook to trigger a new build, which produces a Docker image. The built image is then pushed to Docker Hub.

> Note >  > You can still use `docker push` to push pre-built images to repositories with automated builds configured.

If you have automated tests configured, these run after building, but before pushing to the registry. You can use these tests to create a continuous integration workflow where a build that fails its tests doesn't push the built image. Automated tests don't push images to the registry on their own. [Learn about automated image testing](https://docs.docker.com/docker-hub/repos/manage/builds/automated-testing/).

Depending on your [subscription](https://www.docker.com/pricing), you may get concurrent builds, which means that `N` autobuilds can be run at the same time. `N` is configured according to your subscription. Once `N+1` builds are running, any additional builds go into a queue to be run later.

The maximum number of pending builds in the queue is 30 and Docker Hub discards further requests. The number of concurrent builds for Pro is 5 and for Team and Business is 15. Automated builds can handle images of up to 10 GB in size.