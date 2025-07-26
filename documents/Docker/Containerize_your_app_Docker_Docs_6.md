# Containerize your app | Docker Docs

**URL:** https://docs.docker.com/guides/genai-pdf-bot/containerize
**Word Count:** 682
**Links Count:** 74
**Scraped:** 2025-07-16 02:04:23
**Status:** completed

---

Back

[Guides](https://docs.docker.com/guides/)

  * [Get started](https://docs.docker.com/get-started/)   * [Manuals](https://docs.docker.com/manuals/)   * [Reference](https://docs.docker.com/reference/)

* * *

[PDF analysis and chat](https://docs.docker.com/guides/genai-pdf-bot/)

Learn how to build a PDF bot for parsing PDF documents and generating responses using Docker and generative AI.

[ AI](https://docs.docker.com/tags/ai/)

20 minutes

[1](https://docs.docker.com/guides/genai-pdf-bot/containerize/)

[Containerize your app](https://docs.docker.com/guides/genai-pdf-bot/containerize/)

[2](https://docs.docker.com/guides/genai-pdf-bot/develop/)

[Develop your app](https://docs.docker.com/guides/genai-pdf-bot/develop/)

[Â« Back to all guides](https://docs.docker.com/guides/)

# Containerize a generative AI application

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Prerequisites

> Note >  > GenAI applications can often benefit from GPU acceleration. Currently Docker Desktop supports GPU acceleration only on [Windows with the WSL2 backend](https://docs.docker.com/desktop/features/gpu/#using-nvidia-gpus-with-wsl2). Linux users can also access GPU acceleration using a native installation of the [Docker Engine](https://docs.docker.com/engine/install/).

  * You have installed the latest version of [Docker Desktop](https://docs.docker.com/get-started/get-docker/) or, if you are a Linux user and are planning to use GPU acceleration, [Docker Engine](https://docs.docker.com/engine/install/). Docker adds new features regularly and some parts of this guide may work only with the latest version of Docker Desktop.   * You have a [git client](https://git-scm.com/downloads). The examples in this section use a command-line based git client, but you can use any client.

## Overview

This section walks you through containerizing a generative AI \(GenAI\) application using Docker Desktop.

> Note >  > You can see more samples of containerized GenAI applications in the [GenAI Stack](https://github.com/docker/genai-stack) demo applications.

## Get the sample application

The sample application used in this guide is a modified version of the PDF Reader application from the [GenAI Stack](https://github.com/docker/genai-stack) demo applications. The application is a full stack Python application that lets you ask questions about a PDF file.

The application uses [LangChain](https://www.langchain.com/) for orchestration, [Streamlit](https://streamlit.io/) for the UI, [Ollama](https://ollama.ai/) to run the LLM, and [Neo4j](https://neo4j.com/) to store vectors.

Clone the sample application. Open a terminal, change directory to a directory that you want to work in, and run the following command to clone the repository:               $ git clone https://github.com/craig-osterhout/docker-genai-sample     

You should now have the following files in your `docker-genai-sample` directory.               âââ docker-genai-sample/     â âââ .gitignore     â âââ app.py     â âââ chains.py     â âââ env.example     â âââ requirements.txt     â âââ util.py     â âââ LICENSE     â âââ README.md

## Initialize Docker assets

Now that you have an application, you can use `docker init` to create the necessary Docker assets to containerize your application. Inside the `docker-genai-sample` directory, run the `docker init` command. `docker init` provides some default configuration, but you'll need to answer a few questions about your application. For example, this application uses Streamlit to run. Refer to the following `docker init` example and use the same answers for your prompts.               $ docker init     Welcome to the Docker Init CLI!          This utility will walk you through creating the following files with sensible defaults for your project:       - .dockerignore       - Dockerfile       - compose.yaml       - README.Docker.md          Let's get started!          ? What application platform does your project use? Python     ? What version of Python do you want to use? 3.11.4     ? What port do you want your app to listen on? 8000     ? What is the command to run your app? streamlit run app.py --server.address=0.0.0.0 --server.port=8000     

You should now have the following contents in your `docker-genai-sample` directory.               âââ docker-genai-sample/     â âââ .dockerignore     â âââ .gitignore     â âââ app.py     â âââ chains.py     â âââ compose.yaml     â âââ env.example     â âââ requirements.txt     â âââ util.py     â âââ Dockerfile     â âââ LICENSE     â âââ README.Docker.md     â âââ README.md

To learn more about the files that `docker init` added, see the following:

  * [Dockerfile](https://docs.docker.com/reference/dockerfile/)   * [.dockerignore](https://docs.docker.com/reference/dockerfile/#dockerignore-file)   * [compose.yaml](https://docs.docker.com/reference/compose-file/)

## Run the application

Inside the `docker-genai-sample` directory, run the following command in a terminal.               $ docker compose up --build     

Docker builds and runs your application. Depending on your network connection, it may take several minutes to download all the dependencies. You'll see a message like the following in the terminal when the application is running.               server-1  |   You can now view your Streamlit app in your browser.     server-1  |     server-1  |   URL: http://0.0.0.0:8000     server-1  |     

Open a browser and view the application at <http://localhost:8000>. You should see a simple Streamlit application. The application may take a few minutes to download the embedding model. While the download is in progress, **Running** appears in the top-right corner.

The application requires a Neo4j database service and an LLM service to function. If you have access to services that you ran outside of Docker, specify the connection information and try it out. If you don't have the services running, continue with this guide to learn how you can run some or all of these services with Docker.

In the terminal, press `ctrl`+`c` to stop the application.

## Summary

In this section, you learned how you can containerize and run your GenAI application using Docker.

Related information:

  * [docker init CLI reference](https://docs.docker.com/reference/cli/docker/init/)

## Next steps

In the next section, you'll learn how you can run your application, database, and LLM service all locally using Docker.

[Use containers for generative AI development Â»](https://docs.docker.com/guides/genai-pdf-bot/develop/)