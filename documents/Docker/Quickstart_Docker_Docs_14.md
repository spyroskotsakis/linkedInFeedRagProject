# Quickstart | Docker Docs

**URL:** https://docs.docker.com/offload/quickstart/
**Word Count:** 1415
**Links Count:** 654
**Scraped:** 2025-07-16 01:46:25
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Docker Offload quickstart

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Availability: Beta 

Requires: Docker Desktop 4.43 and later

This quickstart helps you get started with Docker Offload. Docker Offload lets you build and run container images faster by offloading resource-intensive tasks to the cloud. It provides a cloud-based environment that mirrors your local Docker Desktop experience.

## Step 1: Sign up and subscribe to Docker Offload for access

To access Docker Offload, you must [sign up](https://www.docker.com/products/docker-offload/) and subscribe.

## Step 2: Start Docker Offload

> Note >  > After subscribing to Docker Offload, the first time you start Docker Desktop and sign in, you may be prompted to start Docker Offload. If you start Docker Offload via this prompt, you can skip the following steps. Note that you can use the following steps to start Docker Offload at any time.

  1. Start Docker Desktop and sign in.

  2. Open a terminal and run the following command to start Docker Offload:                    $ docker offload start          

  3. When prompted, select your account to use for Docker Offload. This account will consume credits for your Docker Offload usage.

  4. When prompted, select whether to enable GPU support. If you choose to enable GPU support, Docker Offload will run in an instance with an NVIDIA L4 GPU, which is useful for machine learning or compute-intensive workloads.

> Note >  > Enabling GPU support consumes more budget. For more details, see [Docker Offload usage](https://docs.docker.com/offload/usage/).

When Docker Offload is started, you'll see a cloud icon \( ![Offload mode icon](https://docs.docker.com/offload/images/cloud-mode.png) \) in the Docker Desktop Dashboard header, and the Docker Desktop Dashboard appears purple. You can run `docker offload status` in a terminal to check the status of Docker Offload.

## Step 3: Run a container with Docker Offload

After starting Docker Offload, Docker Desktop connects to a secure cloud environment that mirrors your local experience. When you run builds or containers, they execute remotely, but behave just like local ones.

To verify that Docker Offload is working, run a container:               $ docker run --rm hello-world     

If you enabled GPU support, you can also run a GPU-enabled container:               $ docker run --rm --gpus all hello-world     

If Docker Offload is working, you'll see `Hello from Docker!` in the terminal output.

## Step 4: Stop Docker Offload

When you're done using Docker Offload, you can stop it. When stopped, you build images and run containers locally.               $ docker offload stop     

To start Docker Offload again, run the `docker offload start` command.

## What's next

  * [Configure Docker Offload](https://docs.docker.com/offload/configuration/).   * Try [Docker Model Runner](https://docs.docker.com/ai/model-runner/) or [Compose](https://docs.docker.com/ai/compose/models-and-compose/) to run AI models using Docker Offload.