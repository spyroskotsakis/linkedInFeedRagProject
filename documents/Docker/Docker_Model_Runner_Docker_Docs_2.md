# Docker Model Runner | Docker Docs

**URL:** https://docs.docker.com/ai/model-runner/
**Word Count:** 2401
**Links Count:** 718
**Scraped:** 2025-07-16 01:47:07
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Docker Model Runner

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Availability: Beta 

Requires: Docker Engine or Docker Desktop \(Windows\) 4.41+ or Docker Desktop \(MacOS\) 4.40+

For: See Requirements section below

Docker Model Runner makes it easy to manage, run, and deploy AI models using Docker. Designed for developers, Docker Model Runner streamlines the process of pulling, running, and serving large language models \(LLMs\) and other AI models directly from Docker Hub or any OCI-compliant registry.

With seamless integration into Docker Desktop and Docker Engine, you can serve models via OpenAI-compatible APIs, package GGUF files as OCI Artifacts, and interact with models from both the command line and graphical interface.

Whether you're building generative AI applications, experimenting with machine learning workflows, or integrating AI into your software development lifecycle, Docker Model Runner provides a consistent, secure, and efficient way to work with AI models locally.

## Key features

  * [Pull and push models to and from Docker Hub](https://hub.docker.com/u/ai)   * Serve models on OpenAI-compatible APIs for easy integration with existing apps   * Package GGUF files as OCI Artifacts and publish them to any Container Registry   * Run and interact with AI models directly from the command line or from the Docker Desktop GUI   * Manage local models and display logs

## Requirements

Docker Model Runner is supported on the following platforms:

Windows  MacOS  Linux

Windows\(amd64\):

  * NVIDIA GPUs   * NVIDIA drivers 576.57+

Windows\(arm64\):

  * OpenCL for Adreno

  * Qualcomm Adreno GPU \(6xx series and later\)

> Note >  > Some llama.cpp features might not be fully supported on the 6xx series.

  * Apple Silicon

Docker Engine only:

  * Linux CPU & Linux NVIDIA   * NVIDIA drivers 575.57.08+

## How it works

Models are pulled from Docker Hub the first time they're used and stored locally. They're loaded into memory only at runtime when a request is made, and unloaded when not in use to optimize resources. Since models can be large, the initial pull may take some time â but after that, they're cached locally for faster access. You can interact with the model using OpenAI-compatible APIs.

> Tip >  > Using Testcontainers or Docker Compose? [Testcontainers for Java](https://java.testcontainers.org/modules/docker_model_runner/) and [Go](https://golang.testcontainers.org/modules/dockermodelrunner/), and [Docker Compose](https://docs.docker.com/ai/compose/models-and-compose/) now support Docker Model Runner.

## Enable Docker Model Runner

### Enable DMR in Docker Desktop

  1. In the settings view, navigate to the **Beta features** tab.   2. Tick the **Enable Docker Model Runner** setting.   3. If you are running on Windows with a supported NVIDIA GPU, you should also see and be able to tick the **Enable GPU-backed inference** setting.   4. Optional: If you want to enable TCP support, select the **Enable host-side TCP support**      1. In the **Port** field, type the port of your choice.      2. If you are interacting with Model Runner from a local frontend web app, in **CORS Allows Origins** , select the origins that Model Runner should accept requests from. An origin is the URL where your web app is running, for example `http://localhost:3131`.

You can now use the `docker model` command in the CLI and view and interact with your local models in the **Models** tab in the Docker Desktop Dashboard.

> Important >  > For Docker Desktop versions 4.41 and earlier, this setting lived under the **Experimental features** tab on the **Features in development** page.

### Enable DMR in Docker Engine

  1. Ensure you have installed [Docker Engine](https://docs.docker.com/engine/install/).

  2. DMR is available as a package. To install it, run:

Ubuntu/Debian  RPM-base distributions                    $ sudo apt-get update          $ sudo apt-get install docker-model-plugin                              $ sudo dnf update          $ sudo dnf install docker-model-plugin          

  3. Test the installation:                    $ docker model version          $ docker model run ai/smollm2          

  4. Optional: To enable TCP support, set the port with the `DMR_RUNNER_PORT` environment variable.

  5. Optional: If you enabled TCP support, you can configure CORS allowed origins with the `DMR_ORIGINS` environment variable. Possible values are:

     * `*`: Allow all origins      * Comma-separated list of allowed origins      * When unspecified, all origins are denied.

## Pull a model

Models are cached locally.

> Note >  > When working with the Docker CLI, you can also pull models directly from [HuggingFace](https://huggingface.co/).

From Docker Desktop  From the Docker CLI

  1. Select **Models** and select the **Docker Hub** tab.   2. Find the model of your choice and select **Pull**.

![screencapture of the Docker Hub view](https://docs.docker.com/ai/model-runner/images/dmr-catalog.png)

![screencapture of the Docker Hub view](https://docs.docker.com/ai/model-runner/images/dmr-catalog.png)

Use the [`docker model pull` command](https://docs.docker.com/reference/cli/docker/model/pull/). For example:

Pulling from Docker Hub               docker model pull ai/smollm2:360M-Q4_K_M

Pulling from HuggingFace               docker model pull hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF

## Run a model

From Docker Desktop  From the Docker CLI

  1. Select **Models** and select the **Local** tab   2. Click the play button. The interactive chat screen opens.

![screencapture of the Local view](https://docs.docker.com/ai/model-runner/images/dmr-run.png)

![screencapture of the Local view](https://docs.docker.com/ai/model-runner/images/dmr-run.png)

Use the [`docker model run` command](https://docs.docker.com/reference/cli/docker/model/run/).

## Troubleshooting

To troubleshoot potential issues, display the logs:

From Docker Desktop  From the Docker CLI

Select **Models** and select the **Logs** tab.

![screencapture of the Models view](https://docs.docker.com/ai/model-runner/images/dmr-logs.png)

![screencapture of the Models view](https://docs.docker.com/ai/model-runner/images/dmr-logs.png)

Use the [`docker model logs` command](https://docs.docker.com/reference/cli/docker/model/logs/).

## Publish a model

> Note >  > This works for any Container Registry supporting OCI Artifacts, not only Docker Hub.

You can tag existing models with a new name and publish them under a different namespaceand repository:               # Tag a pulled model under a new name     $ docker model tag ai/smollm2 myorg/smollm2          # Push it to Docker Hub     $ docker model push myorg/smollm2     

For more details, see the [`docker model tag`](https://docs.docker.com/reference/cli/docker/model/tag) and [`docker model push`](https://docs.docker.com/reference/cli/docker/model/push) command documentation.

You can also directly package a model file in GGUF format as an OCI Artifact and publish it to Docker Hub.               # Download a model file in GGUF format, e.g. from HuggingFace     $ curl -L -o model.gguf https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF/resolve/main/mistral-7b-v0.1.Q4_K_M.gguf          # Package it as OCI Artifact and push it to Docker Hub     $ docker model package --gguf "$(pwd)/model.gguf" --push myorg/mistral-7b-v0.1:Q4_K_M     

For more details, see the [`docker model package`](https://docs.docker.com/reference/cli/docker/model/package/) command documentation.

## Example: Integrate Docker Model Runner into your software development lifecycle

You can now start building your Generative AI application powered by the Docker Model Runner.

If you want to try an existing GenAI application, follow these instructions.

  1. Set up the sample app. Clone and run the following repository:                    $ git clone https://github.com/docker/hello-genai.git          

  2. In your terminal, navigate to the `hello-genai` directory.

  3. Run `run.sh` for pulling the chosen model and run the app\(s\):

  4. Open you app in the browser at the addresses specified in the repository [README](https://github.com/docker/hello-genai).

You'll see the GenAI app's interface where you can start typing your prompts.

You can now interact with your own GenAI app, powered by a local model. Try a few prompts and notice how fast the responses are â all running on your machine with Docker.

## FAQs

### What models are available?

All the available models are hosted in the [public Docker Hub namespace of `ai`](https://hub.docker.com/u/ai).

### What CLI commands are available?

See [the reference docs](https://docs.docker.com/reference/cli/docker/model/).

### What API endpoints are available?

Once the feature is enabled, new API endpoints are available under the following base URLs:

Docker Desktop  Docker Engine

  * From containers: `http://model-runner.docker.internal/`   * From host processes: `http://localhost:12434/`, assuming TCP host access is enabled on the default port \(12434\).

  * From containers: `http://172.17.0.1:12434/` \(with `172.17.0.1` representing the host gateway address\)   * From host processes: `http://localhost:12434/`

> Note >  > The `172.17.0.1` interface may not be available by default to containers within a Compose project. In this case, add an `extra_hosts` directive to your Compose service YAML: >      >      >     extra_hosts: >       - "model-runner.docker.internal:host-gateway" >  > Then you can access the Docker Model Runner APIs at <http://model-runner.docker.internal:12434/>

Docker Model management endpoints:               POST /models/create     GET /models     GET /models/{namespace}/{name}     DELETE /models/{namespace}/{name}

OpenAI endpoints:               GET /engines/llama.cpp/v1/models     GET /engines/llama.cpp/v1/models/{namespace}/{name}     POST /engines/llama.cpp/v1/chat/completions     POST /engines/llama.cpp/v1/completions     POST /engines/llama.cpp/v1/embeddings

To call these endpoints via a Unix socket \(`/var/run/docker.sock`\), prefix their path with with `/exp/vDD4.40`.

> Note >  > You can omit `llama.cpp` from the path. For example: `POST /engines/v1/chat/completions`.

### How do I interact through the OpenAI API?

#### From within a container

To call the `chat/completions` OpenAI endpoint from within another container using `curl`:               #!/bin/sh          curl http://model-runner.docker.internal/engines/llama.cpp/v1/chat/completions \         -H "Content-Type: application/json" \         -d '{             "model": "ai/smollm2",             "messages": [                 {                     "role": "system",                     "content": "You are a helpful assistant."                 },                 {                     "role": "user",                     "content": "Please write 500 words about the fall of Rome."                 }             ]         }'

#### From the host using TCP

To call the `chat/completions` OpenAI endpoint from the host via TCP:

  1. Enable the host-side TCP support from the Docker Desktop GUI, or via the [Docker Desktop CLI](https://docs.docker.com/desktop/features/desktop-cli/). For example: `docker desktop enable model-runner --tcp <port>`.

If you are running on Windows, also enable GPU-backed inference. See Enable Docker Model Runner.

  2. Interact with it as documented in the previous section using `localhost` and the correct port.

              #!/bin/sh          	curl http://localhost:12434/engines/llama.cpp/v1/chat/completions \         -H "Content-Type: application/json" \         -d '{             "model": "ai/smollm2",             "messages": [                 {                     "role": "system",                     "content": "You are a helpful assistant."                 },                 {                     "role": "user",                     "content": "Please write 500 words about the fall of Rome."                 }             ]         }'

#### From the host using a Unix socket

To call the `chat/completions` OpenAI endpoint through the Docker socket from the host using `curl`:               #!/bin/sh          curl --unix-socket $HOME/.docker/run/docker.sock \         localhost/exp/vDD4.40/engines/llama.cpp/v1/chat/completions \         -H "Content-Type: application/json" \         -d '{             "model": "ai/smollm2",             "messages": [                 {                     "role": "system",                     "content": "You are a helpful assistant."                 },                 {                     "role": "user",                     "content": "Please write 500 words about the fall of Rome."                 }             ]         }'

## Known issues

### `docker model` is not recognised

If you run a Docker Model Runner command and see:               docker: 'model' is not a docker command

It means Docker can't find the plugin because it's not in the expected CLI plugins directory.

To fix this, create a symlink so Docker can detect it:               $ ln -s /Applications/Docker.app/Contents/Resources/cli-plugins/docker-model ~/.docker/cli-plugins/docker-model     

Once linked, rerun the command.

### No safeguard for running oversized models

Currently, Docker Model Runner doesn't include safeguards to prevent you from launching models that exceed your system's available resources. Attempting to run a model that is too large for the host machine may result in severe slowdowns or may render the system temporarily unusable. This issue is particularly common when running LLMs without sufficient GPU memory or system RAM.

### No consistent digest support in Model CLI

The Docker Model CLI currently lacks consistent support for specifying models by image digest. As a temporary workaround, you should refer to models by name instead of digest.

## Share feedback

Thanks for trying out Docker Model Runner. Give feedback or report any bugs you may find through the **Give feedback** link next to the **Enable Docker Model Runner** setting.