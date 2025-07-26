# Configure CI/CD | Docker Docs

**URL:** https://docs.docker.com/guides/java/configure-ci-cd
**Word Count:** 521
**Links Count:** 73
**Scraped:** 2025-07-16 02:04:23
**Status:** completed

---

Back

[Guides](https://docs.docker.com/guides/)

  * [Get started](https://docs.docker.com/get-started/)   * [Manuals](https://docs.docker.com/manuals/)   * [Reference](https://docs.docker.com/reference/)

* * *

[Java language-specific guide](https://docs.docker.com/guides/java/)

This guide demonstrates how to containerize Java applications using Docker.

![](https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/java/java-original.svg) Java

20 minutes

[1](https://docs.docker.com/guides/java/containerize/)

[Containerize your app](https://docs.docker.com/guides/java/containerize/)

[2](https://docs.docker.com/guides/java/develop/)

[Develop your app](https://docs.docker.com/guides/java/develop/)

[3](https://docs.docker.com/guides/java/run-tests/)

[Run your tests](https://docs.docker.com/guides/java/run-tests/)

[4](https://docs.docker.com/guides/java/configure-ci-cd/)

[Configure CI/CD](https://docs.docker.com/guides/java/configure-ci-cd/)

[5](https://docs.docker.com/guides/java/deploy/)

[Test your deployment](https://docs.docker.com/guides/java/deploy/)

[Â« Back to all guides](https://docs.docker.com/guides/)

# Configure CI/CD for your Java application

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Prerequisites

Complete the previous sections of this guide, starting with [Containerize your app](https://docs.docker.com/guides/java/containerize/). You must have a [GitHub](https://github.com/signup) account and a [Docker](https://hub.docker.com/signup) account to complete this section.

## Overview

In this section, you'll learn how to set up and use GitHub Actions to build and push your Docker image to Docker Hub. You will complete the following steps:

  1. Create a new repository on GitHub.   2. Define the GitHub Actions workflow.   3. Run the workflow.

## Step one: Create the repository

Create a GitHub repository, configure the Docker Hub credentials, and push your source code.

  1. [Create a new repository](https://github.com/new) on GitHub.

  2. Open the repository **Settings** , and go to **Secrets and variables** > **Actions**.

  3. Create a new **Repository variable** named `DOCKER_USERNAME` and your Docker ID as a value.

  4. Create a new [Personal Access Token \(PAT\)](https://docs.docker.com/security/for-developers/access-tokens/#create-an-access-token) for Docker Hub. You can name this token `docker-tutorial`. Make sure access permissions include Read and Write.

  5. Add the PAT as a **Repository secret** in your GitHub repository, with the name `DOCKERHUB_TOKEN`.

  6. In your local repository on your machine, run the following command to change the origin to the repository you just created. Make sure you change `your-username` to your GitHub username and `your-repository` to the name of the repository you created.                    $ git remote set-url origin https://github.com/your-username/your-repository.git          

  7. Run the following commands to stage, commit, and push your local repository to GitHub.                    $ git add -A          $ git commit -m "my commit"          $ git push -u origin main          

## Step two: Set up the workflow

Set up your GitHub Actions workflow for building, testing, and pushing the image to Docker Hub.

  1. Go to your repository on GitHub and then select the **Actions** tab. The project already has the `maven-build` workflow to build and test your Java application with Maven. If you want, you can optionally disable this workflow because you won't use it in this guide. You'll create a new, alternate workflow to build, test, and push your image.

  2. Select **New workflow**.

  3. Select **set up a workflow yourself**.

This takes you to a page for creating a new GitHub actions workflow file in your repository, under `.github/workflows/main.yml` by default.

  4. In the editor window, copy and paste the following YAML configuration.                    name: ci                    on:            push:              branches:                - main                    jobs:            build:              runs-on: ubuntu-latest              steps:                - name: Login to Docker Hub                  uses: docker/login-action@v3                  with:                    username: ${{ vars.DOCKER_USERNAME }}                    password: ${{ secrets.DOCKERHUB_TOKEN }}                          - name: Set up Docker Buildx                  uses: docker/setup-buildx-action@v3                          - name: Build and test                  uses: docker/build-push-action@v6                  with:                    target: test                    load: true                          - name: Build and push                  uses: docker/build-push-action@v6                  with:                    platforms: linux/amd64,linux/arm64                    push: true                    target: final                    tags: ${{ vars.DOCKER_USERNAME }}/${{ github.event.repository.name }}:latest

For more information about the YAML syntax for `docker/build-push-action`, refer to the [GitHub Action README](https://github.com/docker/build-push-action/blob/master/README.md).

## Step three: Run the workflow

Save the workflow file and run the job.

  1. Select **Commit changes...** and push the changes to the `main` branch.

After pushing the commit, the workflow starts automatically.

  2. Go to the **Actions** tab. It displays the workflow.

Selecting the workflow shows you the breakdown of all the steps.

  3. When the workflow is complete, go to your [repositories on Docker Hub](https://hub.docker.com/repositories).

If you see the new repository in that list, it means the GitHub Actions successfully pushed the image to Docker Hub.

## Summary

In this section, you learned how to set up a GitHub Actions workflow for your application.

Related information:

  * [Introduction to GitHub Actions](https://docs.docker.com/guides/gha/)   * [Docker Build GitHub Actions](https://docs.docker.com/build/ci/github-actions/)   * [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)

## Next steps

Next, learn how you can locally test and debug your workloads on Kubernetes before deploying.

[Test your Java deployment Â»](https://docs.docker.com/guides/java/deploy/)