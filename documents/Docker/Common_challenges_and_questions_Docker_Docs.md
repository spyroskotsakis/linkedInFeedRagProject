# Common challenges and questions | Docker Docs

**URL:** https://docs.docker.com/guides/docker-build-cloud/common-questions
**Word Count:** 581
**Links Count:** 63
**Scraped:** 2025-07-16 02:04:56
**Status:** completed

---

Back

[Guides](https://docs.docker.com/guides/)

  * [Get started](https://docs.docker.com/get-started/)   * [Manuals](https://docs.docker.com/manuals/)   * [Reference](https://docs.docker.com/reference/)

* * *

[Docker Build Cloud: Reclaim your time with fast, multi-architecture builds](https://docs.docker.com/guides/docker-build-cloud/)

Build applications up to 39x faster using cloud-based resources, shared team cache, and native multi-architecture support.

[ Product demo](https://docs.docker.com/tags/product-demo/)

10 minutes

[1](https://docs.docker.com/guides/docker-build-cloud/why/)

[Why Docker Build Cloud?](https://docs.docker.com/guides/docker-build-cloud/why/)

[2](https://docs.docker.com/guides/docker-build-cloud/dev/)

[Demo: set up and use Docker Build Cloud in development](https://docs.docker.com/guides/docker-build-cloud/dev/)

[3](https://docs.docker.com/guides/docker-build-cloud/ci/)

[Demo: Using Docker Build Cloud in CI](https://docs.docker.com/guides/docker-build-cloud/ci/)

[4](https://docs.docker.com/guides/docker-build-cloud/common-questions/)

[Common challenges and questions](https://docs.docker.com/guides/docker-build-cloud/common-questions/)

Resources:

  * [Product page](https://www.docker.com/products/build-cloud/)   * [Docker Build Cloud overview](https://docs.docker.com/build-cloud/)   * [Subscriptions and features](https://docs.docker.com/subscription/details/)   * [Using Docker Build Cloud](https://docs.docker.com/build-cloud/usage/)

[Â« Back to all guides](https://docs.docker.com/guides/)

# Common challenges and questions

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

### Is Docker Build Cloud a standalone product or a part of Docker Desktop?

Docker Build Cloud is a service that can be used both with Docker Desktop and standalone. It lets you build your container images faster, both locally and in CI, with builds running on cloud infrastructure. The service uses a remote build cache, ensuring fast builds anywhere and for all team members.

When used with Docker Desktop, the [Builds view](https://docs.docker.com/desktop/use-desktop/builds/) works with Docker Build Cloud out-of-the-box. It shows information about your builds and those initiated by your team members using the same builder, enabling collaborative troubleshooting.

To use Docker Build Cloud without Docker Desktop, you must [download and install](https://docs.docker.com/build-cloud/setup/#use-docker-build-cloud-without-docker-desktop) a version of Buildx with support for Docker Build Cloud \(the `cloud` driver\). If you plan on building with Docker Build Cloud using the `docker compose build` command, you also need a version of Docker Compose that supports Docker Build Cloud.

### How does Docker Build Cloud work with Docker Compose?

Docker Compose works out of the box with Docker Build Cloud. Install the Docker Build Cloud-compatible client \(buildx\) and it works with both commands.

### How many minutes are included in Docker Build Cloud Team plans?

Pricing details for Docker Build Cloud can be found on the [pricing page](https://www.docker.com/pricing/).

### Iâm a Docker personal user. Can I try Docker Build Cloud?

Docker subscribers \(Pro, Team, Business\) receive a set number of minutes each month, shared across the account, to use Build Cloud.

If you do not have a Docker subscription, you may sign up for a free Personal account and start a trial of Docker Build Cloud. Personal accounts are limited to a single user.

For teams to receive the shared cache benefit, they must either be on a Docker Team or Docker Business subscription.

### Does Docker Build Cloud support CI platforms? Does it work with GitHub Actions?

Yes, Docker Build Cloud can be used with various CI platforms including GitHub Actions, CircleCI, Jenkins, and others. It can speed up your build pipelines, which means less time spent waiting and context switching.

Docker Build Cloud can be used with GitHub Actions to automate your build, test, and deployment pipeline. Docker provides a set of official GitHub Actions that you can use in your workflows.

Using GitHub Actions with Docker Build Cloud is straightforward. With a one-line change in your GitHub Actions configuration, everything else stays the same. You don't need to create new pipelines. Learn more in the [CI documentation](https://docs.docker.com/build-cloud/ci/) for Docker Build Cloud.