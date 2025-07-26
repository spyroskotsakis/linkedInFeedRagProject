# Containerize your app | Docker Docs

**URL:** https://docs.docker.com/guides/go-prometheus-monitoring/containerize
**Word Count:** 645
**Links Count:** 57
**Scraped:** 2025-07-16 02:04:56
**Status:** completed

---

Back

[Guides](https://docs.docker.com/guides/)

  * [Get started](https://docs.docker.com/get-started/)   * [Manuals](https://docs.docker.com/manuals/)   * [Reference](https://docs.docker.com/reference/)

* * *

[Monitor a Golang application with Prometheus and Grafana](https://docs.docker.com/guides/go-prometheus-monitoring/)

Learn how to containerize a Golang application and monitor it with Prometheus and Grafana.

![](https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/go/go-original.svg) Go

45 minutes

[1](https://docs.docker.com/guides/go-prometheus-monitoring/application/)

[Understand the application](https://docs.docker.com/guides/go-prometheus-monitoring/application/)

[2](https://docs.docker.com/guides/go-prometheus-monitoring/containerize/)

[Containerize your app](https://docs.docker.com/guides/go-prometheus-monitoring/containerize/)

[3](https://docs.docker.com/guides/go-prometheus-monitoring/compose/)

[Connecting services with Docker Compose](https://docs.docker.com/guides/go-prometheus-monitoring/compose/)

[4](https://docs.docker.com/guides/go-prometheus-monitoring/develop/)

[Develop your app](https://docs.docker.com/guides/go-prometheus-monitoring/develop/)

[Â« Back to all guides](https://docs.docker.com/guides/)

# Containerize a Golang application

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Containerization helps you bundle the application and its dependencies into a single package called a container. This package can run on any platform without worrying about the environment. In this section, you will learn how to containerize a Golang application using Docker.

To containerize a Golang application, you first need to create a Dockerfile. The Dockerfile contains instructions to build and run the application in a container. Also, when creating a Dockerfile, you can follow different sets of best practices to optimize the image size and make it more secure.

## Creating a Dockerfile

Create a new file named `Dockerfile` in the root directory of your Golang application. The Dockerfile contains instructions to build and run the application in a container.

The following is a Dockerfile for a Golang application. You will also find this file in the `go-prometheus-monitoring` directory.               # Use the official Golang image as the base     FROM golang:1.24-alpine AS builder          # Set environment variables     ENV CGO_ENABLED=0 \         GOOS=linux \         GOARCH=amd64          # Set working directory inside the container     WORKDIR /build          # Copy go.mod and go.sum files for dependency installation     COPY go.mod go.sum ./          # Download dependencies     RUN go mod download          # Copy the entire application source     COPY . .          # Build the Go binary     RUN go build -o /app .          # Final lightweight stage     FROM alpine:3.21 AS final          # Copy the compiled binary from the builder stage     COPY --from=builder /app /bin/app          # Expose the application's port     EXPOSE 8000          # Run the application     CMD ["bin/app"]

## Understanding the Dockerfile

The Dockerfile consists of two stages:

  1. **Build stage** : This stage uses the official Golang image as the base and sets the necessary environment variables. It also sets the working directory inside the container, copies the `go.mod` and `go.sum` files for dependency installation, downloads the dependencies, copies the entire application source, and builds the Go binary.

You use the `golang:1.24-alpine` image as the base image for the build stage. The `CGO_ENABLED=0` environment variable disables CGO, which is useful for building static binaries. You also set the `GOOS` and `GOARCH` environment variables to `linux` and `amd64`, respectively, to build the binary for the Linux platform.

  2. **Final stage** : This stage uses the official Alpine image as the base and copies the compiled binary from the build stage. It also exposes the application's port and runs the application.

You use the `alpine:3.21` image as the base image for the final stage. You copy the compiled binary from the build stage to the final image. You expose the application's port using the `EXPOSE` instruction and run the application using the `CMD` instruction.

Apart from the multi-stage build, the Dockerfile also follows best practices such as using the official images, setting the working directory, and copying only the necessary files to the final image. You can further optimize the Dockerfile by other best practices.

## Build the Docker image and run the application

One you have the Dockerfile, you can build the Docker image and run the application in a container.

To build the Docker image, run the following command in the terminal:               $ docker build -t go-api:latest .     

After building the image, you can run the application in a container using the following command:               $ docker run -p 8000:8000 go-api:latest     

The application will start running inside the container, and you can access it at `http://localhost:8000`. You can also check the running containers using the `docker ps` command.               $ docker ps     

## Summary

In this section, you learned how to containerize a Golang application using a Dockerfile. You created a multi-stage Dockerfile to build and run the application in a container. You also learned about best practices to optimize the Docker image size and make it more secure.

Related information:

  * [Dockerfile reference](https://docs.docker.com/reference/dockerfile/)   * [.dockerignore file](https://docs.docker.com/reference/dockerfile/#dockerignore-file)

## Next steps

In the next section, you will learn how to use Docker Compose to connect and run multiple services together to monitor a Golang application with Prometheus and Grafana.

[Connecting services with Docker Compose Â»](https://docs.docker.com/guides/go-prometheus-monitoring/compose/)