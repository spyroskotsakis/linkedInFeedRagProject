# Monitor with Prometheus and Grafana | Docker Docs

**URL:** https://docs.docker.com/guides/go-prometheus-monitoring
**Word Count:** 359
**Links Count:** 51
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

# Monitor a Golang application with Prometheus and Grafana

Table of contents

* * *

The guide teaches you how to containerize a Golang application and monitor it with Prometheus and Grafana.

> **Acknowledgment** >  > Docker would like to thank [Pradumna Saraf](https://twitter.com/pradumna_saraf) for his contribution to this guide.

## Overview

To make sure your application is working as intended, monitoring is important. One of the most popular monitoring tools is Prometheus. Prometheus is an open-source monitoring and alerting toolkit that is designed for reliability and scalability. It collects metrics from monitored targets by scraping metrics HTTP endpoints on these targets. To visualize the metrics, you can use Grafana. Grafana is an open-source platform for monitoring and observability that allows you to query, visualize, alert on, and understand your metrics no matter where they are stored.

In this guide, you will be creating a Golang server with some endpoints to simulate a real-world application. Then you will expose metrics from the server using Prometheus. Finally, you will visualize the metrics using Grafana. You will containerize the Golang application, and using the Docker Compose file, you will connect all the services: Golang, Prometheus, and Grafana.

## What will you learn?

  * Create a Golang application with custom Prometheus metrics.   * Containerize a Golang application.   * Use Docker Compose to run multiple services and connect them together to monitor a Golang application with Prometheus and Grafana.   * Visualize the metrics using Grafana dashboards.

## Prerequisites

  * A good understanding of Golang is assumed.   * You must me familiar with Prometheus and creating dashboards in Grafana.   * You must have familiarity with Docker concepts like containers, images, and Dockerfiles. If you are new to Docker, you can start with the [Docker basics](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/) guide.

## Next steps

You will create a Golang server and expose metrics using Prometheus.

## Modules

  1. [Understand the application](https://docs.docker.com/guides/go-prometheus-monitoring/application/)

Learn how to create a Golang server to register metrics with Prometheus.

  2. [Containerize your app](https://docs.docker.com/guides/go-prometheus-monitoring/containerize/)

Learn how to containerize a Golang application.

  3. [Connecting services with Docker Compose](https://docs.docker.com/guides/go-prometheus-monitoring/compose/)

Learn how to connect services with Docker Compose to monitor a Golang application with Prometheus and Grafana.

  4. [Develop your app](https://docs.docker.com/guides/go-prometheus-monitoring/develop/)

Learn how to develop the Golang application with Docker.