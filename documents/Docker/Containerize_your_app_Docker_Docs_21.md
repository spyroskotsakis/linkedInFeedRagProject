# Containerize your app | Docker Docs

**URL:** https://docs.docker.com/guides/rag-ollama/containerize/
**Word Count:** 566
**Links Count:** 60
**Scraped:** 2025-07-16 01:46:03
**Status:** completed

---

Back

[Guides](https://docs.docker.com/guides/)

  * [Get started](https://docs.docker.com/get-started/)   * [Manuals](https://docs.docker.com/manuals/)   * [Reference](https://docs.docker.com/reference/)

* * *

[Build a RAG application using Ollama and Docker](https://docs.docker.com/guides/rag-ollama/)

This guide demonstrates how to use Docker to deploy Retrieval-Augmented Generation \(RAG\) models with Ollama.

[ AI](https://docs.docker.com/tags/ai/)

20 minutes

[1](https://docs.docker.com/guides/rag-ollama/containerize/)

[Containerize your app](https://docs.docker.com/guides/rag-ollama/containerize/)

[2](https://docs.docker.com/guides/rag-ollama/develop/)

[Develop your app](https://docs.docker.com/guides/rag-ollama/develop/)

[Â« Back to all guides](https://docs.docker.com/guides/)

# Containerize a RAG application

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Overview

This section walks you through containerizing a RAG application using Docker.

> Note >  > You can see more samples of containerized GenAI applications in the [GenAI Stack](https://github.com/docker/genai-stack) demo applications.

## Get the sample application

The sample application used in this guide is an example of RAG application, made by three main components, which are the building blocks for every RAG application. A Large Language Model hosted somewhere, in this case it is hosted in a container and served via [Ollama](https://ollama.ai/). A vector database, [Qdrant](https://qdrant.tech/), to store the embeddings of local data, and a web application, using [Streamlit](https://streamlit.io/) to offer the best user experience to the user.

Clone the sample application. Open a terminal, change directory to a directory that you want to work in, and run the following command to clone the repository:               $ git clone https://github.com/mfranzon/winy.git     

You should now have the following files in your `winy` directory.               âââ winy/     â âââ .gitignore     â âââ app/     â â âââ main.py     â â âââ Dockerfile     | | âââ requirements.txt     â âââ tools/     â â âââ create_db.py     â â âââ create_embeddings.py     â â âââ requirements.txt     â â âââ test.py     | | âââ download_model.sh     â âââ docker-compose.yaml     â âââ wine_database.db     â âââ LICENSE     â âââ README.md

## Containerizing your application: Essentials

Containerizing an application involves packaging it along with its dependencies into a container, which ensures consistency across different environments. Hereâs what you need to containerize an app like Winy :

  1. Dockerfile: A Dockerfile that contains instructions on how to build a Docker image for your application. It specifies the base image, dependencies, configuration files, and the command to run your application.

  2. Docker Compose File: Docker Compose is a tool for defining and running multi-container Docker applications. A Compose file allows you to configure your application's services, networks, and volumes in a single file.

## Run the application

Inside the `winy` directory, run the following command in a terminal.               $ docker compose up --build     

Docker builds and runs your application. Depending on your network connection, it may take several minutes to download all the dependencies. You'll see a message like the following in the terminal when the application is running.               server-1  |   You can now view your Streamlit app in your browser.     server-1  |     server-1  |   URL: http://0.0.0.0:8501     server-1  |     

Open a browser and view the application at <http://localhost:8501>. You should see a simple Streamlit application.

The application requires a Qdrant database service and an LLM service to work properly. If you have access to services that you ran outside of Docker, specify the connection information in the `docker-compose.yaml`.               winy:       build:         context: ./app         dockerfile: Dockerfile       environment:         - QDRANT_CLIENT=http://qdrant:6333 # Specifies the url for the qdrant database         - OLLAMA=http://ollama:11434 # Specifies the url for the ollama service       container_name: winy       ports:         - "8501:8501"       depends_on:         - qdrant         - ollama

If you don't have the services running, continue with this guide to learn how you can run some or all of these services with Docker. Remember that the `ollama` service is empty; it doesn't have any model. For this reason you need to pull a model before starting to use the RAG application. All the instructions are in the following page.

In the terminal, press `ctrl`+`c` to stop the application.

## Summary

In this section, you learned how you can containerize and run your RAG application using Docker.

## Next steps

In the next section, you'll learn how to properly configure the application with your preferred LLM model, completely locally, using Docker.

[Use containers for RAG development Â»](https://docs.docker.com/guides/rag-ollama/develop/)