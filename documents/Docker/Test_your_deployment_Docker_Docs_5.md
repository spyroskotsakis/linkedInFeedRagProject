# Test your deployment | Docker Docs

**URL:** https://docs.docker.com/guides/cpp/deploy/
**Word Count:** 446
**Links Count:** 67
**Scraped:** 2025-07-16 01:48:31
**Status:** completed

---

Back

[Guides](https://docs.docker.com/guides/)

  * [Get started](https://docs.docker.com/get-started/)   * [Manuals](https://docs.docker.com/manuals/)   * [Reference](https://docs.docker.com/reference/)

* * *

[C++ language-specific guide](https://docs.docker.com/guides/cpp/)

This guide explains how to containerize C++ applications using Docker.

![](https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/cplusplus/cplusplus-original.svg) C++

20 minutes

[1](https://docs.docker.com/guides/cpp/multistage/)

[Containerize your app using a multi-stage build](https://docs.docker.com/guides/cpp/multistage/)

[2](https://docs.docker.com/guides/cpp/containerize/)

[Build and run a C++ application using Docker Compose](https://docs.docker.com/guides/cpp/containerize/)

[3](https://docs.docker.com/guides/cpp/develop/)

[Develop your app](https://docs.docker.com/guides/cpp/develop/)

[4](https://docs.docker.com/guides/cpp/configure-ci-cd/)

[Configure CI/CD](https://docs.docker.com/guides/cpp/configure-ci-cd/)

[5](https://docs.docker.com/guides/cpp/deploy/)

[Test your deployment](https://docs.docker.com/guides/cpp/deploy/)

[6](https://docs.docker.com/guides/cpp/security/)

[Supply-chain security](https://docs.docker.com/guides/cpp/security/)

[Â« Back to all guides](https://docs.docker.com/guides/)

# Test your C++ deployment

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Prerequisites

  * Complete all the previous sections of this guide, starting with [Containerize a C++ application](https://docs.docker.com/guides/cpp/containerize/).   * [Turn on Kubernetes](https://docs.docker.com/desktop/features/kubernetes/#install-and-turn-on-kubernetes) in Docker Desktop.

## Overview

In this section, you'll learn how to use Docker Desktop to deploy your application to a fully-featured Kubernetes environment on your development machine. This allows you to test and debug your workloads on Kubernetes locally before deploying.

## Create a Kubernetes YAML file

In your `c-plus-plus-docker` directory, create a file named `docker-kubernetes.yml`. Open the file in an IDE or text editor and add the following contents. Replace `DOCKER_USERNAME/REPO_NAME` with your Docker username and the name of the repository that you created in [Configure CI/CD for your C++ application](https://docs.docker.com/guides/cpp/configure-ci-cd/).               apiVersion: apps/v1     kind: Deployment     metadata:       name: docker-c-plus-plus-demo       namespace: default     spec:       replicas: 1       selector:         matchLabels:           service: ok-api       template:         metadata:           labels:             service: ok-api         spec:           containers:             - name: ok-api-service               image: DOCKER_USERNAME/REPO_NAME               imagePullPolicy: Always     ---     apiVersion: v1     kind: Service     metadata:       name: service-entrypoint       namespace: default     spec:       type: NodePort       selector:         service: ok-api       ports:         - port: 8080           targetPort: 8080           nodePort: 30001

In this Kubernetes YAML file, there are two objects, separated by the `---`:

  * A Deployment, describing a scalable group of identical pods. In this case, you'll get just one replica, or copy of your pod. That pod, which is described under `template`, has just one container in it. The container is created from the image built by GitHub Actions in [Configure CI/CD for your C++ application](https://docs.docker.com/guides/cpp/configure-ci-cd/).   * A NodePort service, which will route traffic from port 30001 on your host to port 8080 inside the pods it routes to, allowing you to reach your app from the network.

To learn more about Kubernetes objects, see the [Kubernetes documentation](https://kubernetes.io/docs/home/).

## Deploy and check your application

  1. In a terminal, navigate to `c-plus-plus-docker` and deploy your application to Kubernetes.                    $ kubectl apply -f docker-kubernetes.yml          

You should see output that looks like the following, indicating your Kubernetes objects were created successfully.                    deployment.apps/docker-c-plus-plus-demo created          service/service-entrypoint created

  2. Make sure everything worked by listing your deployments.                    $ kubectl get deployments          

Your deployment should be listed as follows:                    NAME                     READY   UP-TO-DATE   AVAILABLE    AGE          docker-c-plus-plus-demo   1/1     1            1           10s

This indicates all one of the pods you asked for in your YAML are up and running. Do the same check for your services.                    $ kubectl get services          

You should get output like the following.                    NAME                 TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE          kubernetes           ClusterIP   10.96.0.1        <none>        443/TCP          88m          service-entrypoint   NodePort    10.105.145.223   <none>        8080:30001/TCP   83s

In addition to the default `kubernetes` service, you can see your `service-entrypoint` service, accepting traffic on port 30001/TCP.

  3. In a browser, visit the following address. You should see the message `{"Status" : "OK"}`.                    http://localhost:30001/          

  4. Run the following command to tear down your application.                    $ kubectl delete -f docker-kubernetes.yml          

## Summary

In this section, you learned how to use Docker Desktop to deploy your C++ application to a fully-featured Kubernetes environment on your development machine.

Related information:

  * [Kubernetes documentation](https://kubernetes.io/docs/home/)   * [Deploy on Kubernetes with Docker Desktop](https://docs.docker.com/desktop/features/kubernetes/)   * [Swarm mode overview](https://docs.docker.com/engine/swarm/)

[Supply-chain security for C++ Docker images Â»](https://docs.docker.com/guides/cpp/security/)