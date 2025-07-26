# Test your deployment | Docker Docs

**URL:** https://docs.docker.com/guides/r/deploy/
**Word Count:** 429
**Links Count:** 62
**Scraped:** 2025-07-16 01:48:52
**Status:** completed

---

Back

[Guides](https://docs.docker.com/guides/)

  * [Get started](https://docs.docker.com/get-started/)   * [Manuals](https://docs.docker.com/manuals/)   * [Reference](https://docs.docker.com/reference/)

* * *

[R language-specific guide](https://docs.docker.com/guides/r/)

This guide details how to containerize R applications using Docker.

![](https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/r/r-original.svg) R

10 minutes

[1](https://docs.docker.com/guides/r/containerize/)

[Containerize your app](https://docs.docker.com/guides/r/containerize/)

[2](https://docs.docker.com/guides/r/develop/)

[Develop your app](https://docs.docker.com/guides/r/develop/)

[3](https://docs.docker.com/guides/r/configure-ci-cd/)

[Configure CI/CD](https://docs.docker.com/guides/r/configure-ci-cd/)

[4](https://docs.docker.com/guides/r/deploy/)

[Test your deployment](https://docs.docker.com/guides/r/deploy/)

[Â« Back to all guides](https://docs.docker.com/guides/)

# Test your R deployment

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Prerequisites

  * Complete all the previous sections of this guide, starting with [Containerize a R application](https://docs.docker.com/guides/r/containerize/).   * [Turn on Kubernetes](https://docs.docker.com/desktop/features/kubernetes/#install-and-turn-on-kubernetes) in Docker Desktop.

## Overview

In this section, you'll learn how to use Docker Desktop to deploy your application to a fully-featured Kubernetes environment on your development machine. This allows you to test and debug your workloads on Kubernetes locally before deploying.

## Create a Kubernetes YAML file

In your `r-docker-dev` directory, create a file named `docker-r-kubernetes.yaml`. Open the file in an IDE or text editor and add the following contents. Replace `DOCKER_USERNAME/REPO_NAME` with your Docker username and the name of the repository that you created in [Configure CI/CD for your R application](https://docs.docker.com/guides/r/configure-ci-cd/).               apiVersion: apps/v1     kind: Deployment     metadata:       name: docker-r-demo       namespace: default     spec:       replicas: 1       selector:         matchLabels:           service: shiny       template:         metadata:           labels:             service: shiny         spec:           containers:             - name: shiny-service               image: DOCKER_USERNAME/REPO_NAME               imagePullPolicy: Always               env:                 - name: POSTGRES_PASSWORD                   value: mysecretpassword     ---     apiVersion: v1     kind: Service     metadata:       name: service-entrypoint       namespace: default     spec:       type: NodePort       selector:         service: shiny       ports:         - port: 3838           targetPort: 3838           nodePort: 30001

In this Kubernetes YAML file, there are two objects, separated by the `---`:

  * A Deployment, describing a scalable group of identical pods. In this case, you'll get just one replica, or copy of your pod. That pod, which is described under `template`, has just one container in it. The container is created from the image built by GitHub Actions in [Configure CI/CD for your R application](https://docs.docker.com/guides/r/configure-ci-cd/).   * A NodePort service, which will route traffic from port 30001 on your host to port 3838 inside the pods it routes to, allowing you to reach your app from the network.

To learn more about Kubernetes objects, see the [Kubernetes documentation](https://kubernetes.io/docs/home/).

## Deploy and check your application

  1. In a terminal, navigate to `r-docker-dev` and deploy your application to Kubernetes.                    $ kubectl apply -f docker-r-kubernetes.yaml          

You should see output that looks like the following, indicating your Kubernetes objects were created successfully.                    deployment.apps/docker-r-demo created          service/service-entrypoint created

  2. Make sure everything worked by listing your deployments.                    $ kubectl get deployments          

Your deployment should be listed as follows:                    NAME                 READY   UP-TO-DATE   AVAILABLE   AGE          docker-r-demo   1/1     1            1           15s

This indicates all one of the pods you asked for in your YAML are up and running. Do the same check for your services.                    $ kubectl get services          

You should get output like the following.                    NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE          kubernetes           ClusterIP   10.96.0.1       <none>        443/TCP          23h          service-entrypoint   NodePort    10.99.128.230   <none>        3838:30001/TCP   75s

In addition to the default `kubernetes` service, you can see your `service-entrypoint` service, accepting traffic on port 30001/TCP.

  3. In a browser, visit the following address. Note that a database was not deployed in this example.                    http://localhost:30001/          

  4. Run the following command to tear down your application.                    $ kubectl delete -f docker-r-kubernetes.yaml          

## Summary

In this section, you learned how to use Docker Desktop to deploy your application to a fully-featured Kubernetes environment on your development machine.

Related information:

  * [Kubernetes documentation](https://kubernetes.io/docs/home/)   * [Deploy on Kubernetes with Docker Desktop](https://docs.docker.com/desktop/features/kubernetes/)   * [Swarm mode overview](https://docs.docker.com/engine/swarm/)