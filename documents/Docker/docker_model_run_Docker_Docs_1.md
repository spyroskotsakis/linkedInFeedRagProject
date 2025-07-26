# docker model run | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/model/run
**Word Count:** 895
**Links Count:** 485
**Scraped:** 2025-07-16 01:56:56
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker model run

Description| Run a model and interact with it using a submitted prompt or chat mode   ---|---   Usage| `docker model run MODEL [PROMPT]`      **Experimental**

**This command is experimental.**

Experimental features are intended for testing and feedback as their functionality or design may change between releases without warning or can be removed entirely in a future release.

## Description

When you run a model, Docker calls an inference server API endpoint hosted by the Model Runner through Docker Desktop. The model stays in memory until another model is requested, or until a pre-defined inactivity timeout is reached \(currently 5 minutes\).

You do not have to use Docker model run before interacting with a specific model from a host process or from within a container. Model Runner transparently loads the requested model on-demand, assuming it has been pulled and is locally available.

You can also use chat mode in the Docker Desktop Dashboard when you select the model in the **Models** tab.

## Options

Option| Default| Description   ---|---|---   `--debug`| | Enable debug logging      ## Examples

### One-time prompt               docker model run ai/smollm2 "Hi"     

Output:               Hello! How can I assist you today?     

### Interactive chat               docker model run ai/smollm2     

Output:               Interactive chat mode started. Type '/bye' to exit.     > Hi     Hi there! It's SmolLM, AI assistant. How can I help you today?     > /bye     Chat session ended.