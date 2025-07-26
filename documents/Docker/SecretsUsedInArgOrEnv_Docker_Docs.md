# SecretsUsedInArgOrEnv | Docker Docs

**URL:** https://docs.docker.com/reference/build-checks/secrets-used-in-arg-or-env
**Word Count:** 809
**Links Count:** 484
**Scraped:** 2025-07-16 01:56:34
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# SecretsUsedInArgOrEnv

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Output               Potentially sensitive data should not be used in the ARG or ENV commands

## Description

While it is common to pass secrets to running processes through environment variables during local development, setting secrets in a Dockerfile using `ENV` or `ARG` is insecure because they persist in the final image. This rule reports violations where `ENV` and `ARG` keys indicate that they contain sensitive data.

Instead of `ARG` or `ENV`, you should use secret mounts, which expose secrets to your builds in a secure manner, and do not persist in the final image or its metadata. See [Build secrets](https://docs.docker.com/build/building/secrets/).

## Examples

â Bad: `AWS_SECRET_ACCESS_KEY` is a secret value.               FROM scratch     ARG AWS_SECRET_ACCESS_KEY