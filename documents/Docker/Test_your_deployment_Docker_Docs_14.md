# Test your deployment | Docker Docs

**URL:** https://docs.docker.com/guides/nodejs/deploy
**Word Count:** 433
**Links Count:** 64
**Scraped:** 2025-07-16 02:04:38
**Status:** completed

---

Back

[Guides](https://docs.docker.com/guides/)

  * [Get started](https://docs.docker.com/get-started/)   * [Manuals](https://docs.docker.com/manuals/)   * [Reference](https://docs.docker.com/reference/)

* * *

[Node.js language-specific guide](https://docs.docker.com/guides/nodejs/)

This guide explains how to containerize Node.js applications using Docker.

![](https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg) JavaScript

20 minutes

[1](https://docs.docker.com/guides/nodejs/containerize/)

[Containerize your app](https://docs.docker.com/guides/nodejs/containerize/)

[2](https://docs.docker.com/guides/nodejs/develop/)

[Develop your app](https://docs.docker.com/guides/nodejs/develop/)

[3](https://docs.docker.com/guides/nodejs/run-tests/)

[Run your tests](https://docs.docker.com/guides/nodejs/run-tests/)

[4](https://docs.docker.com/guides/nodejs/configure-ci-cd/)

[Configure CI/CD](https://docs.docker.com/guides/nodejs/configure-ci-cd/)

[5](https://docs.docker.com/guides/nodejs/deploy/)

[Test your deployment](https://docs.docker.com/guides/nodejs/deploy/)

[Â« Back to all guides](https://docs.docker.com/guides/)

# Test your Node.js deployment

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Prerequisites

  * Complete all the previous sections of this guide, starting with [Containerize a Node.js application](https://docs.docker.com/guides/nodejs/containerize/).   * [Turn on Kubernetes](https://docs.docker.com/desktop/features/kubernetes/#install-and-turn-on-kubernetes) in Docker Desktop.

## Overview

In this section, you'll learn how to use Docker Desktop to deploy your application to a fully-featured Kubernetes environment on your development machine. This allows you to test and debug your workloads on Kubernetes locally before deploying.

## Create a Kubernetes YAML file

In the cloned repository's directory, create a file named `docker-node-kubernetes.yaml`. Open the file in an IDE or text editor and add the following contents. Replace `DOCKER_USERNAME/REPO_NAME` with your Docker username and the name of the repository that you created in [Configure CI/CD for your Node.js application](https://docs.docker.com/guides/nodejs/configure-ci-cd/).               apiVersion: apps/v1     kind: Deployment     metadata:       name: docker-nodejs-demo       namespace: default     spec:       replicas: 1       selector:         matchLabels:           todo: web       template:         metadata:           labels:             todo: web         spec:           containers:             - name: todo-site               image: DOCKER_USERNAME/REPO_NAME               imagePullPolicy: Always     ---     apiVersion: v1     kind: Service     metadata:       name: todo-entrypoint       namespace: default     spec:       type: NodePort       selector:         todo: web       ports:         - port: 3000           targetPort: 3000           nodePort: 30001

In this Kubernetes YAML file, there are two objects, separated by the `---`:

  * A Deployment, describing a scalable group of identical pods. In this case, you'll get just one replica, or copy of your pod. That pod, which is described under `template`, has just one container in it. The container is created from the image built by GitHub Actions in [Configure CI/CD for your Node.js application](https://docs.docker.com/guides/nodejs/configure-ci-cd/).   * A NodePort service, which will route traffic from port 30001 on your host to port 3000 inside the pods it routes to, allowing you to reach your app from the network.

To learn more about Kubernetes objects, see the [Kubernetes documentation](https://kubernetes.io/docs/home/).

## Deploy and check your application

  1. In a terminal, navigate to where you created `docker-node-kubernetes.yaml` and deploy your application to Kubernetes.                    $ kubectl apply -f docker-node-kubernetes.yaml          

You should see output that looks like the following, indicating your Kubernetes objects were created successfully.                    deployment.apps/docker-nodejs-demo created          service/todo-entrypoint created

  2. Make sure everything worked by listing your deployments.                    $ kubectl get deployments          

Your deployment should be listed as follows:                    NAME                 READY   UP-TO-DATE   AVAILABLE   AGE          docker-nodejs-demo   1/1     1            1           6s

This indicates all one of the pods you asked for in your YAML are up and running. Do the same check for your services.                    $ kubectl get services          

You should get output like the following.                    NAME              TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE          kubernetes        ClusterIP   10.96.0.1        <none>        443/TCP          7d22h          todo-entrypoint   NodePort    10.111.101.229   <none>        3000:30001/TCP   33s

In addition to the default `kubernetes` service, you can see your `todo-entrypoint` service, accepting traffic on port 30001/TCP.

  3. Open a browser and visit your app at `localhost:30001`. You should see your application.

  4. Run the following command to tear down your application.                    $ kubectl delete -f docker-node-kubernetes.yaml          

## Summary

In this section, you learned how to use Docker Desktop to deploy your application to a fully-featured Kubernetes environment on your development machine.

Related information:

  * [Kubernetes documentation](https://kubernetes.io/docs/home/)   * [Deploy on Kubernetes with Docker Desktop](https://docs.docker.com/desktop/features/kubernetes/)   * [Swarm mode overview](https://docs.docker.com/engine/swarm/)