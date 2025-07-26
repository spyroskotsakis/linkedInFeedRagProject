# Troubleshoot | Docker Docs

**URL:** https://docs.docker.com/docker-hub/troubleshoot
**Word Count:** 1273
**Links Count:** 659
**Scraped:** 2025-07-16 01:58:31
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Troubleshoot Docker Hub

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

If you experience issues with Docker Hub, refer to the following solutions.

## You have reached your pull rate limit \(429 response code\)

### Error message

When this issue occurs, you receive following error message in the Docker CLI or in the Docker Engine logs:               You have reached your pull rate limit. You may increase the limit by authenticating and upgrading: https://www.docker.com/increase-rate-limits

### Possible causes

  * You have reached your pull rate limit as an authenticated Docker Personal user.   * You have reached your pull rate limit as an unauthenticated user based on your IPv4 address or IPv6 /64 subnet.

### Solution

You can use one of the following solutions:

  * [Authenticate](https://docs.docker.com/docker-hub/usage/pulls/#authentication) or [upgrade](https://docs.docker.com/subscription/change/#upgrade-your-subscription) your Docker account.   * [View your pull rate limit](https://docs.docker.com/docker-hub/usage/pulls/#view-hourly-pull-rate-and-limit), wait until your pull rate limit decreases, and then try again.

## Too many requests \(429 response code\)

### Error message

When this issue occurs, you receive following error message in the Docker CLI or in the Docker Engine logs:               Too Many Requests

### Possible causes

  * You have reached the [Abuse rate limit](https://docs.docker.com/docker-hub/usage/#abuse-rate-limit).

### Solution

  1. Check for broken CI/CD pipelines accessing Docker Hub and fix them.   2. Implement a retry with back-off solution in your automated scripts to ensure that you're not resending thousands of requests per minute.

## 500 response code

### Error message

When this issue occurs, the following error message is common in the Docker CLI or in the Docker Engine logs:               Unexpected status code 500

### Possible causes

  * There is a temporary Docker Hub service issue.

### Solution

  1. View the [Docker System Status Page](https://www.dockerstatus.com/) and verify that all services are operational.   2. Try accessing Docker Hub again. It may be a temporary issue.   3. [Contact Docker Support](https://www.docker.com/support/) to report the issue.