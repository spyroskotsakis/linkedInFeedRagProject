# docker model pull | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/model/pull/
**Word Count:** 843
**Links Count:** 484
**Scraped:** 2025-07-16 01:51:20
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker model pull

Description| Pull a model from Docker Hub or HuggingFace to your local environment   ---|---   Usage| `docker model pull MODEL`      **Experimental**

**This command is experimental.**

Experimental features are intended for testing and feedback as their functionality or design may change between releases without warning or can be removed entirely in a future release.

## Description

Pull a model to your local environment. Downloaded models also appear in the Docker Desktop Dashboard.

## Examples

### Pulling a model from Docker Hub               docker model pull ai/smollm2     

### Pulling from HuggingFace

You can pull GGUF models directly from [Hugging Face](https://huggingface.co/models?library=gguf).

**Note about quantization:** If no tag is specified, the command tries to pull the `Q4_K_M` version of the model. If `Q4_K_M` doesn't exist, the command pulls the first GGUF found in the **Files** view of the model on HuggingFace. To specify the quantization, provide it as a tag, for example: `docker model pull hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF:Q4_K_S`               docker model pull hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF