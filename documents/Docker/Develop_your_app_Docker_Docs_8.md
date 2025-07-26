# Develop your app | Docker Docs

**URL:** https://docs.docker.com/guides/dotnet/develop
**Word Count:** 1180
**Links Count:** 86
**Scraped:** 2025-07-16 02:04:23
**Status:** completed

---

Back

[Guides](https://docs.docker.com/guides/)

  * [Get started](https://docs.docker.com/get-started/)   * [Manuals](https://docs.docker.com/manuals/)   * [Reference](https://docs.docker.com/reference/)

* * *

[.NET language-specific guide](https://docs.docker.com/guides/dotnet/)

Learn how to containerize .NET applications using Docker.

![](https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/csharp/csharp-original.svg) C\#

20 minutes

[1](https://docs.docker.com/guides/dotnet/containerize/)

[Containerize your app](https://docs.docker.com/guides/dotnet/containerize/)

[2](https://docs.docker.com/guides/dotnet/develop/)

[Develop your app](https://docs.docker.com/guides/dotnet/develop/)

[3](https://docs.docker.com/guides/dotnet/run-tests/)

[Run your tests](https://docs.docker.com/guides/dotnet/run-tests/)

[4](https://docs.docker.com/guides/dotnet/configure-ci-cd/)

[Configure CI/CD](https://docs.docker.com/guides/dotnet/configure-ci-cd/)

[5](https://docs.docker.com/guides/dotnet/deploy/)

[Test your deployment](https://docs.docker.com/guides/dotnet/deploy/)

[Â« Back to all guides](https://docs.docker.com/guides/)

# Use containers for .NET development

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Prerequisites

Complete [Containerize a .NET application](https://docs.docker.com/guides/dotnet/containerize/).

## Overview

In this section, you'll learn how to set up a development environment for your containerized application. This includes:

  * Adding a local database and persisting data   * Configuring Compose to automatically update your running Compose services as you edit and save your code   * Creating a development container that contains the .NET Core SDK tools and dependencies

## Update the application

This section uses a different branch of the `docker-dotnet-sample` repository that contains an updated .NET application. The updated application is on the `add-db` branch of the repository you cloned in [Containerize a .NET application](https://docs.docker.com/guides/dotnet/containerize/).

To get the updated code, you need to checkout the `add-db` branch. For the changes you made in [Containerize a .NET application](https://docs.docker.com/guides/dotnet/containerize/), for this section, you can stash them. In a terminal, run the following commands in the `docker-dotnet-sample` directory.

  1. Stash any previous changes.                    $ git stash -u          

  2. Check out the new branch with the updated application.                    $ git checkout add-db          

In the `add-db` branch, only the .NET application has been updated. None of the Docker assets have been updated yet.

You should now have the following in your `docker-dotnet-sample` directory.               âââ docker-dotnet-sample/     â âââ .git/     â âââ src/     â â âââ Data/     â â âââ Models/     â â âââ Pages/     â â âââ Properties/     â â âââ wwwroot/     â â âââ appsettings.Development.json     â â âââ appsettings.json     â â âââ myWebApp.csproj     â â âââ Program.cs     â âââ tests/     â â âââ tests.csproj     â â âââ UnitTest1.cs     â â âââ Usings.cs     â âââ .dockerignore     â âââ .gitignore     â âââ compose.yaml     â âââ Dockerfile     â âââ README.Docker.md     â âââ README.md

## Add a local database and persist data

You can use containers to set up local services, like a database. In this section, you'll update the `compose.yaml` file to define a database service and a volume to persist data.

Open the `compose.yaml` file in an IDE or text editor. You'll notice it already contains commented-out instructions for a PostgreSQL database and volume.

Open `docker-dotnet-sample/src/appsettings.json` in an IDE or text editor. You'll notice the connection string with all the database information. The `compose.yaml` already contains this information, but it's commented out. Uncomment the database instructions in the `compose.yaml` file.

The following is the updated `compose.yaml` file.               services:       server:         build:           context: .           target: final         ports:           - 8080:8080         depends_on:           db:             condition: service_healthy       db:         image: postgres         restart: always         user: postgres         secrets:           - db-password         volumes:           - db-data:/var/lib/postgresql/data         environment:           - POSTGRES_DB=example           - POSTGRES_PASSWORD_FILE=/run/secrets/db-password         expose:           - 5432         healthcheck:           test: ["CMD", "pg_isready"]           interval: 10s           timeout: 5s           retries: 5     volumes:       db-data:     secrets:       db-password:         file: db/password.txt

> Note >  > To learn more about the instructions in the Compose file, see [Compose file reference](https://docs.docker.com/reference/compose-file/).

Before you run the application using Compose, notice that this Compose file uses `secrets` and specifies a `password.txt` file to hold the database's password. You must create this file as it's not included in the source repository.

In the `docker-dotnet-sample` directory, create a new directory named `db` and inside that directory create a file named `password.txt`. Open `password.txt` in an IDE or text editor and add the following password. The password must be on a single line, with no additional lines in the file.               example

Save and close the `password.txt` file.

You should now have the following in your `docker-dotnet-sample` directory.               âââ docker-dotnet-sample/     â âââ .git/     â âââ db/     â â âââ password.txt     â âââ src/     â âââ tests/     â âââ .dockerignore     â âââ .gitignore     â âââ compose.yaml     â âââ Dockerfile     â âââ README.Docker.md     â âââ README.md

Run the following command to start your application.               $ docker compose up --build     

Open a browser and view the application at <http://localhost:8080>. You should see a simple web application with the text `Student name is`.

The application doesn't display a name because the database is empty. For this application, you need to access the database and then add records.

## Add records to the database

For the sample application, you must access the database directly to create sample records.

You can run commands inside the database container using the `docker exec` command. Before running that command, you must get the ID of the database container. Open a new terminal window and run the following command to list all your running containers.               $ docker container ls     

You should see output like the following.               CONTAINER ID   IMAGE                  COMMAND                  CREATED              STATUS                        PORTS                    NAMES     cb36e310aa7e   docker-dotnet-server   "dotnet myWebApp.dll"    About a minute ago   Up About a minute             0.0.0.0:8080->8080/tcp   docker-dotnet-server-1     39fdcf0aff7b   postgres               "docker-entrypoint.sâ¦"   About a minute ago   Up About a minute (healthy)   5432/tcp                 docker-dotnet-db-1     

In the previous example, the container ID is `39fdcf0aff7b`. Run the following command to connect to the postgres database in the container. Replace the container ID with your own container ID.               $ docker exec -it 39fdcf0aff7b psql -d example -U postgres     

And finally, insert a record into the database.               example=# INSERT INTO "Students" ("ID", "LastName", "FirstMidName", "EnrollmentDate") VALUES (DEFAULT, 'Whale', 'Moby', '2013-03-20');     

You should see output like the following.               INSERT 0 1     

Close the database connection and exit the container shell by running `exit`.               example=# exit     

## Verify that data persists in the database

Open a browser and view the application at <http://localhost:8080>. You should see a simple web application with the text `Student name is Whale Moby`.

Press `ctrl+c` in the terminal to stop your application.

In the terminal, run `docker compose rm` to remove your containers and then run `docker compose up` to run your application again.               $ docker compose rm     $ docker compose up --build     

Refresh <http://localhost:8080> in your browser and verify that the student name persisted, even after the containers were removed and ran again.

Press `ctrl+c` in the terminal to stop your application.

## Automatically update services

Use Compose Watch to automatically update your running Compose services as you edit and save your code. For more details about Compose Watch, see [Use Compose Watch](https://docs.docker.com/compose/how-tos/file-watch/).

Open your `compose.yaml` file in an IDE or text editor and then add the Compose Watch instructions. The following is the updated `compose.yaml` file.               services:       server:         build:           context: .           target: final         ports:           - 8080:8080         depends_on:           db:             condition: service_healthy         develop:           watch:             - action: rebuild               path: .       db:         image: postgres         restart: always         user: postgres         secrets:           - db-password         volumes:           - db-data:/var/lib/postgresql/data         environment:           - POSTGRES_DB=example           - POSTGRES_PASSWORD_FILE=/run/secrets/db-password         expose:           - 5432         healthcheck:           test: ["CMD", "pg_isready"]           interval: 10s           timeout: 5s           retries: 5     volumes:       db-data:     secrets:       db-password:         file: db/password.txt

Run the following command to run your application with Compose Watch.               $ docker compose watch     

Open a browser and verify that the application is running at <http://localhost:8080>.

Any changes to the application's source files on your local machine will now be immediately reflected in the running container.

Open `docker-dotnet-sample/src/Pages/Index.cshtml` in an IDE or text editor and update the student name text on line 13 from `Student name is` to `Student name:`.               -    <p>Student Name is @Model.StudentName</p>     +    <p>Student name: @Model.StudentName</p>     

Save the changes to `Index.cshmtl` and then wait a few seconds for the application to rebuild. Refresh <http://localhost:8080> in your browser and verify that the updated text appears.

Press `ctrl+c` in the terminal to stop your application.

## Create a development container

At this point, when you run your containerized application, it's using the .NET runtime image. While this small image is good for production, it lacks the SDK tools and dependencies you may need when developing. Also, during development, you may not need to run `dotnet publish`. You can use multi-stage builds to build stages for both development and production in the same Dockerfile. For more details, see [Multi-stage builds](https://docs.docker.com/build/building/multi-stage/).

Add a new development stage to your Dockerfile and update your `compose.yaml` file to use this stage for local development.

The following is the updated Dockerfile.               # syntax=docker/dockerfile:1          FROM --platform=$BUILDPLATFORM mcr.microsoft.com/dotnet/sdk:8.0-alpine AS build     ARG TARGETARCH     COPY . /source     WORKDIR /source/src     RUN --mount=type=cache,id=nuget,target=/root/.nuget/packages \         dotnet publish -a ${TARGETARCH/amd64/x64} --use-current-runtime --self-contained false -o /app          FROM mcr.microsoft.com/dotnet/sdk:8.0-alpine AS development     COPY . /source     WORKDIR /source/src     CMD dotnet run --no-launch-profile          FROM mcr.microsoft.com/dotnet/aspnet:8.0-alpine AS final     WORKDIR /app     COPY --from=build /app .     ARG UID=10001     RUN adduser \         --disabled-password \         --gecos "" \         --home "/nonexistent" \         --shell "/sbin/nologin" \         --no-create-home \         --uid "${UID}" \         appuser     USER appuser     ENTRYPOINT ["dotnet", "myWebApp.dll"]

The following is the updated `compose.yaml` file.               services:       server:         build:           context: .           target: development         ports:           - 8080:8080         depends_on:           db:             condition: service_healthy         develop:           watch:             - action: rebuild               path: .         environment:           - ASPNETCORE_ENVIRONMENT=Development       db:         image: postgres         restart: always         user: postgres         secrets:           - db-password         volumes:           - db-data:/var/lib/postgresql/data         environment:           - POSTGRES_DB=example           - POSTGRES_PASSWORD_FILE=/run/secrets/db-password         expose:           - 5432         healthcheck:           test: ["CMD", "pg_isready"]           interval: 10s           timeout: 5s           retries: 5     volumes:       db-data:     secrets:       db-password:         file: db/password.txt

Your containerized application will now use the `mcr.microsoft.com/dotnet/sdk:8.0-alpine` image, which includes development tools like `dotnet test`. Continue to the next section to learn how you can run `dotnet test`.

## Summary

In this section, you took a look at setting up your Compose file to add a local database and persist data. You also learned how to use Compose Watch to automatically rebuild and run your container when you update your code. And finally, you learned how to create a development container that contains the SDK tools and dependencies needed for development.

Related information:

  * [Compose file reference](https://docs.docker.com/reference/compose-file/)   * [Compose file watch](https://docs.docker.com/compose/how-tos/file-watch/)   * [Multi-stage builds](https://docs.docker.com/build/building/multi-stage/)

## Next steps

In the next section, you'll learn how to run unit tests using Docker.

[Run .NET tests in a container Â»](https://docs.docker.com/guides/dotnet/run-tests/)