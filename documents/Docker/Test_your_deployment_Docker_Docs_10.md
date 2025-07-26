# Test your deployment | Docker Docs

**URL:** https://docs.docker.com/guides/golang/deploy
**Word Count:** 481
**Links Count:** 66
**Scraped:** 2025-07-16 02:04:08
**Status:** completed

---

Back

[Guides](https://docs.docker.com/guides/)

  * [Get started](https://docs.docker.com/get-started/)   * [Manuals](https://docs.docker.com/manuals/)   * [Reference](https://docs.docker.com/reference/)

* * *

[Go language-specific guide](https://docs.docker.com/guides/golang/)

This guide teaches you how to containerize Go applications using Docker.

![](https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/go/go-original.svg) Go

30 minutes

[1](https://docs.docker.com/guides/golang/build-images/)

[Build images](https://docs.docker.com/guides/golang/build-images/)

[2](https://docs.docker.com/guides/golang/run-containers/)

[Run containers](https://docs.docker.com/guides/golang/run-containers/)

[3](https://docs.docker.com/guides/golang/develop/)

[Develop your app](https://docs.docker.com/guides/golang/develop/)

[4](https://docs.docker.com/guides/golang/run-tests/)

[Run your tests](https://docs.docker.com/guides/golang/run-tests/)

[5](https://docs.docker.com/guides/golang/configure-ci-cd/)

[Configure CI/CD](https://docs.docker.com/guides/golang/configure-ci-cd/)

[6](https://docs.docker.com/guides/golang/deploy/)

[Test your deployment](https://docs.docker.com/guides/golang/deploy/)

[Â« Back to all guides](https://docs.docker.com/guides/)

# Test your Go deployment

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Prerequisites

  * Complete all the previous sections of this guide, starting with [Build your Go image](https://docs.docker.com/guides/golang/build-images/).   * [Turn on Kubernetes](https://docs.docker.com/desktop/features/kubernetes/#install-and-turn-on-kubernetes) in Docker Desktop.

## Overview

In this section, you'll learn how to use Docker Desktop to deploy your application to a fully-featured Kubernetes environment on your development machine. This allows you to test and debug your workloads on Kubernetes locally before deploying.

## Create a Kubernetes YAML file

In your project directory, create a file named `docker-go-kubernetes.yaml`. Open the file in an IDE or text editor and add the following contents. Replace `DOCKER_USERNAME/REPO_NAME` with your Docker username and the name of the repository that you created in [Configure CI/CD for your Go application](https://docs.docker.com/guides/golang/configure-ci-cd/).               apiVersion: apps/v1     kind: Deployment     metadata:       labels:         service: server       name: server       namespace: default     spec:       replicas: 1       selector:         matchLabels:           service: server       strategy: {}       template:         metadata:           labels:             service: server         spec:           initContainers:             - name: wait-for-db               image: busybox:1.28               command:                 [                   "sh",                   "-c",                   'until nc -zv db 5432; do echo "waiting for db"; sleep 2; done;',                 ]           containers:             - env:                 - name: PGDATABASE                   value: mydb                 - name: PGPASSWORD                   value: whatever                 - name: PGHOST                   value: db                 - name: PGPORT                   value: "5432"                 - name: PGUSER                   value: postgres               image: DOCKER_USERNAME/REPO_NAME               name: server               imagePullPolicy: Always               ports:                 - containerPort: 8080                   hostPort: 8080                   protocol: TCP               resources: {}           restartPolicy: Always     status: {}     ---     apiVersion: apps/v1     kind: Deployment     metadata:       labels:         service: db       name: db       namespace: default     spec:       replicas: 1       selector:         matchLabels:           service: db       strategy:         type: Recreate       template:         metadata:           labels:             service: db         spec:           containers:             - env:                 - name: POSTGRES_DB                   value: mydb                 - name: POSTGRES_PASSWORD                   value: whatever                 - name: POSTGRES_USER                   value: postgres               image: postgres               name: db               ports:                 - containerPort: 5432                   protocol: TCP               resources: {}           restartPolicy: Always     status: {}     ---     apiVersion: v1     kind: Service     metadata:       labels:         service: server       name: server       namespace: default     spec:       type: NodePort       ports:         - name: "8080"           port: 8080           targetPort: 8080           nodePort: 30001       selector:         service: server     status:       loadBalancer: {}     ---     apiVersion: v1     kind: Service     metadata:       labels:         service: db       name: db       namespace: default     spec:       ports:         - name: "5432"           port: 5432           targetPort: 5432       selector:         service: db     status:       loadBalancer: {}

In this Kubernetes YAML file, there are four objects, separated by the `---`. In addition to a Service and Deployment for the database, the other two objects are:

  * A Deployment, describing a scalable group of identical pods. In this case, you'll get just one replica, or copy of your pod. That pod, which is described under `template`, has just one container in it. The container is created from the image built by GitHub Actions in [Configure CI/CD for your Go application](https://docs.docker.com/guides/golang/configure-ci-cd/).   * A NodePort service, which will route traffic from port 30001 on your host to port 8080 inside the pods it routes to, allowing you to reach your app from the network.

To learn more about Kubernetes objects, see the [Kubernetes documentation](https://kubernetes.io/docs/home/).

## Deploy and check your application

  1. In a terminal, navigate to the project directory and deploy your application to Kubernetes.                    $ kubectl apply -f docker-go-kubernetes.yaml          

You should see output that looks like the following, indicating your Kubernetes objects were created successfully.                    deployment.apps/db created          service/db created          deployment.apps/server created          service/server created

  2. Make sure everything worked by listing your deployments.                    $ kubectl get deployments          

Your deployment should be listed as follows:                    NAME     READY   UP-TO-DATE   AVAILABLE   AGE          db       1/1     1            1           76s          server   1/1     1            1           76s

This indicates all of the pods are up and running. Do the same check for your services.                    $ kubectl get services          

You should get output like the following.                    NAME         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE          db           ClusterIP   10.96.156.90    <none>        5432/TCP         2m8s          kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP          164m          server       NodePort    10.102.94.225   <none>        8080:30001/TCP   2m8s

In addition to the default `kubernetes` service, you can see your `server` service and `db` service. The `server` service is accepting traffic on port 30001/TCP.

  3. Open a terminal and curl your application to verify that it's working.                    $ curl --request POST \            --url http://localhost:30001/send \            --header 'content-type: application/json' \            --data '{"value": "Hello, Oliver!"}'          

You should get the following message back.                    { "value": "Hello, Oliver!" }

  4. Run the following command to tear down your application.                    $ kubectl delete -f docker-go-kubernetes.yaml          

## Summary

In this section, you learned how to use Docker Desktop to deploy your application to a fully-featured Kubernetes environment on your development machine.

Related information:

  * [Kubernetes documentation](https://kubernetes.io/docs/home/)   * [Deploy on Kubernetes with Docker Desktop](https://docs.docker.com/desktop/features/kubernetes/)   * [Swarm mode overview](https://docs.docker.com/engine/swarm/)