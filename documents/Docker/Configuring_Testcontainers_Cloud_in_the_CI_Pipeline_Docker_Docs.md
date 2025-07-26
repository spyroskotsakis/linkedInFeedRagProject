# Configuring Testcontainers Cloud in the CI Pipeline | Docker Docs

**URL:** https://docs.docker.com/guides/testcontainers-cloud/demo-ci
**Word Count:** 277
**Links Count:** 47
**Scraped:** 2025-07-16 02:05:18
**Status:** completed

---

Back

[Guides](https://docs.docker.com/guides/)

  * [Get started](https://docs.docker.com/get-started/)   * [Manuals](https://docs.docker.com/manuals/)   * [Reference](https://docs.docker.com/reference/)

* * *

[Mastering Testcontainers Cloud by Docker: streamlining integration testing with containers](https://docs.docker.com/guides/testcontainers-cloud/)

Automate, scale, and optimize testing workflows with Testcontainers Cloud

[ Product demo](https://docs.docker.com/tags/product-demo/)

12 minutes

[1](https://docs.docker.com/guides/testcontainers-cloud/why/)

[Why Testcontainers Cloud?](https://docs.docker.com/guides/testcontainers-cloud/why/)

[2](https://docs.docker.com/guides/testcontainers-cloud/demo-local/)

[Setting up Testcontainers Cloud by Docker](https://docs.docker.com/guides/testcontainers-cloud/demo-local/)

[3](https://docs.docker.com/guides/testcontainers-cloud/demo-ci/)

[Configuring Testcontainers Cloud in the CI Pipeline](https://docs.docker.com/guides/testcontainers-cloud/demo-ci/)

[4](https://docs.docker.com/guides/testcontainers-cloud/common-questions/)

[Common challenges and questions](https://docs.docker.com/guides/testcontainers-cloud/common-questions/)

Resources:

  * [Testcontainers Guides](https://testcontainers.com/guides)   * [Testcontainers Best Practices](https://www.docker.com/blog/testcontainers-best-practices/)   * [Simple local development with Testcontainers Desktop](https://testcontainers.com/guides/simple-local-development-with-testcontainers-desktop/)   * [Streamlining Local Development with Dev Containers and Testcontainers Cloud](https://www.docker.com/blog/streamlining-local-development-with-dev-containers-and-testcontainers-cloud/)   * [Running Testcontainers Tests Using GitHub Actions and Testcontainers Cloud](https://www.docker.com/blog/running-testcontainers-tests-using-github-actions/)   * [Testcontainers Cloud on the Docker Blog](https://www.docker.com/search/?_sf_s=testcontainers%20cloud)

[Â« Back to all guides](https://docs.docker.com/guides/)

# Configuring Testcontainers Cloud in the CI Pipeline

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

* * *

This demo shows how Testcontainers Cloud can be seamlessly integrated into a Continuous Integration \(CI\) pipeline using GitHub Workflows, providing a powerful solution for running containerized integration tests without overloading local or CI runner resources. By leveraging GitHub Actions, developers can automate the process of spinning up and managing containers for testing in the cloud, ensuring faster and more reliable test execution. With just a few configuration steps, including setting up Testcontainers Cloud authentication and adding it to your workflow, you can offload container orchestration to the cloud. This approach improves the scalability of your pipeline, ensures consistency across tests, and simplifies resource management, making it an ideal solution for modern, containerized development workflows.

  * Understand how to set up a GitHub Actions workflow to automate the build and testing of a project.   * Learn how to configure Testcontainers Cloud within GitHub Actions to offload containerized testing to the cloud, improving efficiency and resource management.   * Explore how Testcontainers Cloud integrates with GitHub workflows to run integration tests that require containerized services, such as databases and message brokers.

[Common challenges and questions Â»](https://docs.docker.com/guides/testcontainers-cloud/common-questions/)