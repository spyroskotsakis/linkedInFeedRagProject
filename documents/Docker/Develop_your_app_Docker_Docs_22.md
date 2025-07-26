# Develop your app | Docker Docs

**URL:** https://docs.docker.com/guides/python/develop
**Word Count:** 1275
**Links Count:** 69
**Scraped:** 2025-07-16 02:04:38
**Status:** completed

---

Back

[Guides](https://docs.docker.com/guides/)

  * [Get started](https://docs.docker.com/get-started/)   * [Manuals](https://docs.docker.com/manuals/)   * [Reference](https://docs.docker.com/reference/)

* * *

[Python language-specific guide](https://docs.docker.com/guides/python/)

This guide explains how to containerize Python applications using Docker.

![](https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg) Python

20 minutes

[1](https://docs.docker.com/guides/python/containerize/)

[Containerize your app](https://docs.docker.com/guides/python/containerize/)

[2](https://docs.docker.com/guides/python/develop/)

[Develop your app](https://docs.docker.com/guides/python/develop/)

[3](https://docs.docker.com/guides/python/lint-format-typing/)

[Linting and typing](https://docs.docker.com/guides/python/lint-format-typing/)

[4](https://docs.docker.com/guides/python/configure-github-actions/)

[Automate your builds with GitHub Actions](https://docs.docker.com/guides/python/configure-github-actions/)

[5](https://docs.docker.com/guides/python/deploy/)

[Test your deployment](https://docs.docker.com/guides/python/deploy/)

[Â« Back to all guides](https://docs.docker.com/guides/)

# Use containers for Python development

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Prerequisites

Complete [Containerize a Python application](https://docs.docker.com/guides/python/containerize/).

## Overview

In this section, you'll learn how to set up a development environment for your containerized application. This includes:

  * Adding a local database and persisting data   * Configuring Compose to automatically update your running Compose services as you edit and save your code

## Get the sample application

You'll need to clone a new repository to get a sample application that includes logic to connect to the database.

  1. Change to a directory where you want to clone the repository and run the following command.                    $ git clone https://github.com/estebanx64/python-docker-dev-example          

  2. In the cloned repository's directory, manually create the Docker assets or run `docker init` to create the necessary Docker assets.

Use Docker Init  Manually create assets

In the cloned repository's directory, run `docker init`. Refer to the following example to answer the prompts from `docker init`.                    $ docker init          Welcome to the Docker Init CLI!                    This utility will walk you through creating the following files with sensible defaults for your project:            - .dockerignore            - Dockerfile            - compose.yaml            - README.Docker.md                    Let's get started!                    ? What application platform does your project use? Python          ? What version of Python do you want to use? 3.12          ? What port do you want your app to listen on? 8001          ? What is the command to run your app? python3 -m uvicorn app:app --host=0.0.0.0 --port=8001          

Create a file named `.gitignore` with the following contents.

.gitignore

Show more                    # Byte-compiled / optimized / DLL files          __pycache__/          *.py[cod]          *$py.class                    # C extensions          *.so                    # Distribution / packaging          .Python          build/          develop-eggs/          dist/          downloads/          eggs/          .eggs/          lib/          lib64/          parts/          sdist/          var/          wheels/          share/python-wheels/          *.egg-info/          .installed.cfg          *.egg          MANIFEST                    # Unit test / coverage reports          htmlcov/          .tox/          .nox/          .coverage          .coverage.*          .cache          nosetests.xml          coverage.xml          *.cover          *.py,cover          .hypothesis/          .pytest_cache/          cover/                    # PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm          __pypackages__/                    # Environments          .env          .venv          env/          venv/          ENV/          env.bak/          venv.bak/

Hide

If you don't have Docker Desktop installed or prefer creating the assets manually, you can create the following files in your project directory.

Create a file named `Dockerfile` with the following contents.

Dockerfile

Show more                    # syntax=docker/dockerfile:1                    # Comments are provided throughout this file to help you get started.          # If you need more help, visit the Dockerfile reference guide at          # https://docs.docker.com/go/dockerfile-reference/                    # Want to help us make this template better? Share your feedback here: https://   forms.gle/ybq9Krt8jtBL3iCk7                    ARG PYTHON_VERSION=3.12          FROM python:${PYTHON_VERSION}-slim                    # Prevents Python from writing pyc files.          ENV PYTHONDONTWRITEBYTECODE=1                    # Keeps Python from buffering stdout and stderr to avoid situations where          # the application crashes without emitting any logs due to buffering.          ENV PYTHONUNBUFFERED=1                    WORKDIR /app                    # Create a non-privileged user that the app will run under.          # See https://docs.docker.com/go/dockerfile-user-best-practices/          ARG UID=10001          RUN adduser \              --disabled-password \              --gecos "" \              --home "/nonexistent" \              --shell "/sbin/nologin" \              --no-create-home \              --uid "${UID}" \              appuser                    # Download dependencies as a separate step to take advantage of Docker's    caching.          # Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.          # Leverage a bind mount to requirements.txt to avoid having to copy them into          # into this layer.          RUN --mount=type=cache,target=/root/.cache/pip \              --mount=type=bind,source=requirements.txt,target=requirements.txt \              python -m pip install -r requirements.txt                    # Switch to the non-privileged user to run the application.          USER appuser                    # Copy the source code into the container.          COPY . .                    # Expose the port that the application listens on.          EXPOSE 8001                    # Run the application.          CMD ["python3", "-m", "uvicorn", "app:app", "--host=0.0.0.0", "--port=8001"]

Hide

Create a file named `compose.yaml` with the following contents.

compose.yaml

Show more                    # Comments are provided throughout this file to help you get started.          # If you need more help, visit the Docker Compose reference guide at          # https://docs.docker.com/go/compose-spec-reference/                    # Here the instructions define your application as a service called "server".          # This service is built from the Dockerfile in the current directory.          # You can add other services your application may depend on here, such as a          # database or a cache. For examples, see the Awesome Compose repository:          # https://github.com/docker/awesome-compose          services:            server:              build:                context: .              ports:                - 8001:8001          # The commented out section below is an example of how to define a PostgreSQL          # database that your application can use. `depends_on` tells Docker Compose to          # start the database before your application. The `db-data` volume persists the          # database data between container restarts. The `db-password` secret is used          # to set the database password. You must create `db/password.txt` and add          # a password of your choosing to it before running `docker compose up`.          #     depends_on:          #       db:          #         condition: service_healthy          #   db:          #     image: postgres          #     restart: always          #     user: postgres          #     secrets:          #       - db-password          #     volumes:          #       - db-data:/var/lib/postgresql/data          #     environment:          #       - POSTGRES_DB=example          #       - POSTGRES_PASSWORD_FILE=/run/secrets/db-password          #     expose:          #       - 5432          #     healthcheck:          #       test: [ "CMD", "pg_isready" ]          #       interval: 10s          #       timeout: 5s          #       retries: 5          # volumes:          #   db-data:          # secrets:          #   db-password:          #     file: db/password.txt

Hide

Create a file named `.dockerignore` with the following contents.

.dockerignore

Show more                    # Include any files or directories that you don't want to be copied to your          # container here (e.g., local build artifacts, temporary files, etc.).          #          # For more help, visit the .dockerignore file reference guide at          # https://docs.docker.com/go/build-context-dockerignore/                    **/.DS_Store          **/__pycache__          **/.venv          **/.classpath          **/.dockerignore          **/.env          **/.git          **/.gitignore          **/.project          **/.settings          **/.toolstarget          **/.vs          **/.vscode          **/*.*proj.user          **/*.dbmdl          **/*.jfm          **/bin          **/charts          **/docker-compose*          **/compose.y*ml          **/Dockerfile*          **/node_modules          **/npm-debug.log          **/obj          **/secrets.dev.yaml          **/values.dev.yaml          LICENSE          README.md

Hide

Create a file named `.gitignore` with the following contents.

.gitignore

Show more                    # Byte-compiled / optimized / DLL files          __pycache__/          *.py[cod]          *$py.class                    # C extensions          *.so                    # Distribution / packaging          .Python          build/          develop-eggs/          dist/          downloads/          eggs/          .eggs/          lib/          lib64/          parts/          sdist/          var/          wheels/          share/python-wheels/          *.egg-info/          .installed.cfg          *.egg          MANIFEST                    # Unit test / coverage reports          htmlcov/          .tox/          .nox/          .coverage          .coverage.*          .cache          nosetests.xml          coverage.xml          *.cover          *.py,cover          .hypothesis/          .pytest_cache/          cover/                    # PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm          __pypackages__/                    # Environments          .env          .venv          env/          venv/          ENV/          env.bak/          venv.bak/

Hide

## Add a local database and persist data

You can use containers to set up local services, like a database. In this section, you'll update the `compose.yaml` file to define a database service and a volume to persist data.

In the cloned repository's directory, open the `compose.yaml` file in an IDE or text editor. `docker init` handled creating most of the instructions, but you'll need to update it for your unique application.

In the `compose.yaml` file, you need to uncomment all of the database instructions. In addition, you need to add the database password file as an environment variable to the server service and specify the secret file to use .

The following is the updated `compose.yaml` file.               services:       server:         build:           context: .         ports:           - 8001:8001         environment:           - POSTGRES_SERVER=db           - POSTGRES_USER=postgres           - POSTGRES_DB=example           - POSTGRES_PASSWORD_FILE=/run/secrets/db-password         depends_on:           db:             condition: service_healthy         secrets:           - db-password       db:         image: postgres         restart: always         user: postgres         secrets:           - db-password         volumes:           - db-data:/var/lib/postgresql/data         environment:           - POSTGRES_DB=example           - POSTGRES_PASSWORD_FILE=/run/secrets/db-password         expose:           - 5432         healthcheck:           test: ["CMD", "pg_isready"]           interval: 10s           timeout: 5s           retries: 5     volumes:       db-data:     secrets:       db-password:         file: db/password.txt

> Note >  > To learn more about the instructions in the Compose file, see [Compose file reference](https://docs.docker.com/reference/compose-file/).

Before you run the application using Compose, notice that this Compose file specifies a `password.txt` file to hold the database's password. You must create this file as it's not included in the source repository.

In the cloned repository's directory, create a new directory named `db` and inside that directory create a file named `password.txt` that contains the password for the database. Using your favorite IDE or text editor, add the following contents to the `password.txt` file.               mysecretpassword

Save and close the `password.txt` file.

You should now have the following contents in your `python-docker-dev-example` directory.               âââ python-docker-dev-example/     â âââ db/     â â âââ password.txt     â âââ app.py     â âââ config.py     â âââ requirements.txt     â âââ .dockerignore     â âââ .gitignore     â âââ compose.yaml     â âââ Dockerfile     â âââ README.Docker.md     â âââ README.md

Now, run the following `docker compose up` command to start your application.               $ docker compose up --build     

Now test your API endpoint. Open a new terminal then make a request to the server using the curl commands:

Let's create an object with a post method               $ curl -X 'POST' \       'http://localhost:8001/heroes/' \       -H 'accept: application/json' \       -H 'Content-Type: application/json' \       -d '{       "id": 1,       "name": "my hero",       "secret_name": "austing",       "age": 12     }'     

You should receive the following response:               {       "age": 12,       "id": 1,       "name": "my hero",       "secret_name": "austing"     }

Let's make a get request with the next curl command:               curl -X 'GET' \       'http://localhost:8001/heroes/' \       -H 'accept: application/json'     

You should receive the same response as above because it's the only one object we have in database.               {       "age": 12,       "id": 1,       "name": "my hero",       "secret_name": "austing"     }

Press `ctrl+c` in the terminal to stop your application.

## Automatically update services

Use Compose Watch to automatically update your running Compose services as you edit and save your code. For more details about Compose Watch, see [Use Compose Watch](https://docs.docker.com/compose/how-tos/file-watch/).

Open your `compose.yaml` file in an IDE or text editor and then add the Compose Watch instructions. The following is the updated `compose.yaml` file.               services:       server:         build:           context: .         ports:           - 8001:8001         environment:           - POSTGRES_SERVER=db           - POSTGRES_USER=postgres           - POSTGRES_DB=example           - POSTGRES_PASSWORD_FILE=/run/secrets/db-password         depends_on:           db:             condition: service_healthy         secrets:           - db-password         develop:           watch:             - action: rebuild               path: .       db:         image: postgres         restart: always         user: postgres         secrets:           - db-password         volumes:           - db-data:/var/lib/postgresql/data         environment:           - POSTGRES_DB=example           - POSTGRES_PASSWORD_FILE=/run/secrets/db-password         expose:           - 5432         healthcheck:           test: ["CMD", "pg_isready"]           interval: 10s           timeout: 5s           retries: 5     volumes:       db-data:     secrets:       db-password:         file: db/password.txt

Run the following command to run your application with Compose Watch.               $ docker compose watch     

In a terminal, curl the application to get a response.               $ curl http://localhost:8001     Hello, Docker!     

Any changes to the application's source files on your local machine will now be immediately reflected in the running container.

Open `python-docker-dev-example/app.py` in an IDE or text editor and update the `Hello, Docker!` string by adding a few more exclamation marks.               -    return 'Hello, Docker!'     +    return 'Hello, Docker!!!'     

Save the changes to `app.py` and then wait a few seconds for the application to rebuild. Curl the application again and verify that the updated text appears.               $ curl http://localhost:8001     Hello, Docker!!!     

Press `ctrl+c` in the terminal to stop your application.

## Summary

In this section, you took a look at setting up your Compose file to add a local database and persist data. You also learned how to use Compose Watch to automatically rebuild and run your container when you update your code.

Related information:

  * [Compose file reference](https://docs.docker.com/reference/compose-file/)   * [Compose file watch](https://docs.docker.com/compose/how-tos/file-watch/)   * [Multi-stage builds](https://docs.docker.com/build/building/multi-stage/)

## Next steps

In the next section, you'll learn how you can set up linting, formatting and type checking to follow the best practices in python apps.

[Linting, formatting, and type checking for Python Â»](https://docs.docker.com/guides/python/lint-format-typing/)