# Debug a container | Docker Docs

**URL:** https://docs.docker.com/dhi/how-to/debug/
**Word Count:** 1283
**Links Count:** 646
**Scraped:** 2025-07-16 01:48:52
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Debug a Docker Hardened Image container

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Subscription: Docker Hardened Images

Docker Hardened Images \(DHI\) prioritize minimalism and security, which means they intentionally leave out many common debugging tools \(like shells or package managers\). This makes direct troubleshooting difficult without introducing risk. To address this, you can use [Docker Debug](https://docs.docker.com/reference/cli/docker/debug/), a secure workflow that temporarily attaches an ephemeral debug container to a running service or image without modifying the original image.

This guide shows how to debug Docker Hardened Images locally during development. You can also debug containers remotely using the `--host` option.

The following example uses a mirrored `dhi-python:3.13` image, but the same steps apply to any image.

## Step 1: Run a container from a Hardened Image

Start with a DHI-based container that simulates an issue:               $ docker run -d --name myapp <YOUR_ORG>/dhi-python:3.13 python -c "import time; time.sleep(300)"     

This container doesn't include a shell or tools like `ps`, `top`, or `cat`.

If you try:               $ docker exec -it myapp sh     

You'll see:               exec: "sh": executable file not found in $PATH     

## Step 2: Use Docker Debug to inspect the container

Use the `docker debug` command to attach a temporary, tool-rich debug container to the running instance.               $ docker debug myapp     

From here, you can inspect running processes, network status, or mounted files.

For example, to check running processes:               $ ps aux     

Exit the debug session with:               $ exit     

## What's next

Docker Debug helps you troubleshoot hardened containers without compromising the integrity of the original image. Because the debug container is ephemeral and separate, it avoids introducing security risks into production environments.

If you encounter issues related to permissions, ports, missing shells, or package managers, see [Troubleshoot Docker Hardened Images](https://docs.docker.com/dhi/troubleshoot/) for recommended solutions and workarounds.