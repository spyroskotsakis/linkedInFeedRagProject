# Models | Docker Docs

**URL:** https://docs.docker.com/reference/compose-file/models/
**Word Count:** 873
**Links Count:** 489
**Scraped:** 2025-07-16 01:49:17
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# Models

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Requires: Docker Compose [2.38.0](https://docs.docker.com/compose/releases/release-notes/#2380) and later

The top-level `models` section declares AI models that are used by your Compose application. These models are typically pulled as OCI artifacts, run by a model runner, and exposed as an API that your service containers can consume.

Services can only access models when explicitly granted by a [`models` attribute](https://docs.docker.com/reference/compose-file/services/#models) within the `services` top-level element.

## Examples

### Example 1               services:       app:         image: app         models:           - ai_model               models:       ai_model:         model: ai/model

In this basic example:

  * The app service uses the `ai_model`.   * The `ai_model` is defined as an OCI artifact \(`ai/model`\) that is pulled and served by the model runner.   * Docker Compose injects connection info, for example `AI_MODEL_URL`, into the container.

### Example 2               services:       app:         image: app         models:           my_model:             endpoint_var: MODEL_URL          models:       my_model:         model: ai/model         context_size: 1024         runtime_flags:            - "--a-flag"           - "--another-flag=42"

In this advanced setup:

  * The service app references `my_model` using the long syntax.   * Compose injects the model runner's URL as the environment variable `MODEL_URL`.

## Attributes

  * `model` \(required\): The OCI artifact identifier for the model. This is what Compose pulls and runs via the model runner.   * `context_size`: Defines the maximum token context size for the model.   * `runtime_flags`: A list of raw command-line flags passed to the inference engine when the model is started.