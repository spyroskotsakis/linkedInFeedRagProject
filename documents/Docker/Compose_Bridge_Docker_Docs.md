# Compose Bridge | Docker Docs

**URL:** http://docs.docker.com/compose/bridge
**Word Count:** 1195
**Links Count:** 645
**Scraped:** 2025-07-16 02:09:15
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](http://docs.docker.com/get-started/)   * [Guides](http://docs.docker.com/guides/)   * [Reference](http://docs.docker.com/reference/)

* * *

# Overview of Compose Bridge

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Requires: Docker Desktop 4.43.0 and later

Compose Bridge converts your Docker Compose configuration into platform-specific formatsâprimarily Kubernetes manifests. The default transformation generates Kubernetes manifests and a Kustomize overlay which are designed for deployment on Docker Desktop with Kubernetes enabled.

It's a flexible tool that lets you either take advantage of the [default transformation](https://docs.docker.com/compose/bridge/usage/) or [create a custom transformation](https://docs.docker.com/compose/bridge/customize/) to suit specific project needs and requirements.

Compose Bridge significantly simplifies the transition from Docker Compose to Kubernetes, making it easier for you to leverage the power of Kubernetes while maintaining the simplicity and efficiency of Docker Compose.

## How it works

Compose Bridge uses transformations to let you convert a Compose model into another form.

A transformation is packaged as a Docker image that receives the fully resolved Compose model as `/in/compose.yaml` and can produce any target format file under `/out`.

Compose Bridge provides its own transformation for Kubernetes using Go templates, so that it is easy to extend for customization by replacing or appending your own templates.

For more detailed information on how these transformations work and how you can customize them for your projects, see [Customize](https://docs.docker.com/compose/bridge/customize/).

## What's next?

  * [Use Compose Bridge](https://docs.docker.com/compose/bridge/usage/)   * [Explore how you can customize Compose Bridge](https://docs.docker.com/compose/bridge/customize/)