# Jenkins | Docker Docs

**URL:** https://docs.docker.com/scout/integrations/ci/jenkins
**Word Count:** 1145
**Links Count:** 637
**Scraped:** 2025-07-16 01:59:56
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Integrate Docker Scout with Jenkins

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

* * *

You can add the following stage and steps definition to a `Jenkinsfile` to run Docker Scout as part of a Jenkins pipeline. The pipeline needs a `DOCKER_HUB` credential containing the username and password for authenticating to Docker Hub. It also needs an environment variable defined for the image and tag.               pipeline {         agent {             // Agent details         }              environment {             DOCKER_HUB = credentials('jenkins-docker-hub-credentials')             IMAGE_TAG  = 'myorg/scout-demo-service:latest'         }              stages {             stage('Analyze image') {                 steps {                     // Install Docker Scout                     sh 'curl -sSfL https://raw.githubusercontent.com/docker/scout-cli/main/install.sh | sh -s -- -b /usr/local/bin'                          // Log into Docker Hub                     sh 'echo $DOCKER_HUB_PSW | docker login -u $DOCKER_HUB_USR --password-stdin'                          // Analyze and fail on critical or high vulnerabilities                     sh 'docker-scout cves $IMAGE_TAG --exit-code --only-severity critical,high'                 }             }         }     }

This installs Docker Scout, logs into Docker Hub, and then runs Docker Scout to generate a CVE report for an image and tag. It only shows critical or high-severity vulnerabilities.

> Note >  > If you're seeing a `permission denied` error related to the image cache, try setting the [`DOCKER_SCOUT_CACHE_DIR`](https://docs.docker.com/scout/how-tos/configure-cli/) environment variable to a writable directory. Or alternatively, disable local caching entirely with `DOCKER_SCOUT_NO_CACHE=true`.