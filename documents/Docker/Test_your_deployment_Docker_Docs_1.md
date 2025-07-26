# Test your deployment | Docker Docs

**URL:** https://docs.docker.com/guides/angular/deploy/
**Word Count:** 722
**Links Count:** 89
**Scraped:** 2025-07-16 01:48:52
**Status:** completed

---

Back

[Guides](https://docs.docker.com/guides/)

  * [Get started](https://docs.docker.com/get-started/)   * [Manuals](https://docs.docker.com/manuals/)   * [Reference](https://docs.docker.com/reference/)

* * *

[Angular language-specific guide](https://docs.docker.com/guides/angular/)

This guide explains how to containerize Angular applications using Docker.

![](https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg) JavaScript

20 minutes

[1](https://docs.docker.com/guides/angular/containerize/)

[Containerize](https://docs.docker.com/guides/angular/containerize/)

[2](https://docs.docker.com/guides/angular/develop/)

[Develop your app](https://docs.docker.com/guides/angular/develop/)

[3](https://docs.docker.com/guides/angular/run-tests/)

[Run your tests](https://docs.docker.com/guides/angular/run-tests/)

[4](https://docs.docker.com/guides/angular/configure-github-actions/)

[Automate your builds with GitHub Actions](https://docs.docker.com/guides/angular/configure-github-actions/)

[5](https://docs.docker.com/guides/angular/deploy/)

[Test your deployment](https://docs.docker.com/guides/angular/deploy/)

[Â« Back to all guides](https://docs.docker.com/guides/)

# Test your Angular deployment

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Prerequisites

Before you begin, make sure youâve completed the following:

  * Complete all the previous sections of this guide, starting with [Containerize Angular application](https://docs.docker.com/guides/angular/containerize/).   * [Enable Kubernetes](https://docs.docker.com/desktop/features/kubernetes/#install-and-turn-on-kubernetes) in Docker Desktop.

> **New to Kubernetes?**   >  Visit the [Kubernetes basics tutorial](https://kubernetes.io/docs/tutorials/kubernetes-basics/) to get familiar with how clusters, pods, deployments, and services work.

* * *

## Overview

This section guides you through deploying your containerized Angular application locally using [Docker Desktopâs built-in Kubernetes](https://docs.docker.com/desktop/kubernetes/). Running your app in a local Kubernetes cluster closely simulates a real production environment, enabling you to test, validate, and debug your workloads with confidence before promoting them to staging or production.

* * *

## Create a Kubernetes YAML file

Follow these steps to define your deployment configuration:

  1. In the root of your project, create a new file named: angular-sample-kubernetes.yaml

  2. Open the file in your IDE or preferred text editor.

  3. Add the following configuration, and be sure to replace `{DOCKER_USERNAME}` and `{DOCKERHUB_PROJECT_NAME}` with your actual Docker Hub username and repository name from the previous [Automate your builds with GitHub Actions](https://docs.docker.com/guides/angular/configure-github-actions/).

              apiVersion: apps/v1     kind: Deployment     metadata:       name: angular-sample       namespace: default     spec:       replicas: 1       selector:         matchLabels:           app: angular-sample       template:         metadata:           labels:             app: angular-sample         spec:           containers:             - name: angular-container               image: {DOCKER_USERNAME}/{DOCKERHUB_PROJECT_NAME}:latest               imagePullPolicy: Always               ports:                 - containerPort: 8080               resources:                 limits:                   cpu: "500m"                   memory: "256Mi"                 requests:                   cpu: "250m"                   memory: "128Mi"     ---     apiVersion: v1     kind: Service     metadata:       name: angular-sample-service       namespace: default     spec:       type: NodePort       selector:         app: angular-sample       ports:         - port: 8080           targetPort: 8080           nodePort: 30001

This manifest defines two key Kubernetes resources, separated by `---`:

  * Deployment Deploys a single replica of your Angular application inside a pod. The pod uses the Docker image built and pushed by your GitHub Actions CI/CD workflow   \(refer to [Automate your builds with GitHub Actions](https://docs.docker.com/guides/angular/configure-github-actions/)\).   The container listens on port `8080`, which is typically used by [Nginx](https://nginx.org/en/docs/) to serve your production Angular app.

  * Service \(NodePort\) Exposes the deployed pod to your local machine.   It forwards traffic from port `30001` on your host to port `8080` inside the container.   This lets you access the application in your browser at <http://localhost:30001>.

> Note >  > To learn more about Kubernetes objects, see the [Kubernetes documentation](https://kubernetes.io/docs/home/).

* * *

## Deploy and check your application

Follow these steps to deploy your containerized Angular app into a local Kubernetes cluster and verify that itâs running correctly.

### Step 1. Apply the Kubernetes configuration

In your terminal, navigate to the directory where your `angular-sample-kubernetes.yaml` file is located, then deploy the resources using:                 $ kubectl apply -f angular-sample-kubernetes.yaml     

If everything is configured properly, youâll see confirmation that both the Deployment and the Service were created:                 deployment.apps/angular-sample created       service/angular-sample-service created

This confirms that both the Deployment and the Service were successfully created and are now running inside your local cluster.

### Step 2. Check the Deployment status

Run the following command to check the status of your deployment:                 $ kubectl get deployments     

You should see output similar to the following:                 NAME                 READY   UP-TO-DATE   AVAILABLE   AGE       angular-sample       1/1     1            1           14s

This confirms that your pod is up and running with one replica available.

### Step 3. Verify the Service exposure

Check if the NodePort service is exposing your app to your local machine:               $ kubectl get services     

You should see something like:               NAME                     TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE     angular-sample-service   NodePort    10.100.185.105    <none>        8080:30001/TCP   1m

This output confirms that your app is available via NodePort on port 30001.

### Step 4. Access your app in the browser

Open your browser and navigate to <http://localhost:30001>.

You should see your production-ready Angular Sample application running â served by your local Kubernetes cluster.

### Step 5. Clean up Kubernetes resources

Once you're done testing, you can delete the deployment and service using:                 $ kubectl delete -f angular-sample-kubernetes.yaml     

Expected output:                 deployment.apps "angular-sample" deleted       service "angular-sample-service" deleted

This ensures your cluster stays clean and ready for the next deployment.

* * *

## Summary

In this section, you learned how to deploy your Angular application to a local Kubernetes cluster using Docker Desktop. This setup allows you to test and debug your containerized app in a production-like environment before deploying it to the cloud.

What you accomplished:

  * Created a Kubernetes Deployment and NodePort Service for your Angular app   * Used `kubectl apply` to deploy the application locally   * Verified the app was running and accessible at `http://localhost:30001`   * Cleaned up your Kubernetes resources after testing

* * *

## Related resources

Explore official references and best practices to sharpen your Kubernetes deployment workflow:

  * [Kubernetes documentation](https://kubernetes.io/docs/home/) â Learn about core concepts, workloads, services, and more.   * [Deploy on Kubernetes with Docker Desktop](https://docs.docker.com/desktop/features/kubernetes/) â Use Docker Desktopâs built-in Kubernetes support for local testing and development.   * [`kubectl` CLI reference](https://kubernetes.io/docs/reference/kubectl/) â Manage Kubernetes clusters from the command line.   * [Kubernetes Deployment resource](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) â Understand how to manage and scale applications using Deployments.   * [Kubernetes Service resource](https://kubernetes.io/docs/concepts/services-networking/service/) â Learn how to expose your application to internal and external traffic.