# Troubleshoot | Docker Docs

**URL:** https://docs.docker.com/offload/troubleshoot/
**Word Count:** 1136
**Links Count:** 636
**Scraped:** 2025-07-16 01:49:17
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Troubleshoot Docker Offload

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

* * *

Docker Offload requires:

  * Authentication   * An active internet connection   * No restrictive proxy or firewall blocking traffic to Docker Cloud   * Beta access to Docker Offload   * Docker Desktop 4.43 or later

Docker Desktop uses Offload to run both builds and containers in the cloud. If builds or containers are failing to run, falling back to local, or reporting session errors, use the following steps to help resolve the issue.

  1. Ensure Docker Offload is enabled in Docker Desktop:

     1. Open Docker Desktop and sign in.      2. Go to **Settings** > **Beta features**.      3. Ensure that **Docker Offload** is checked.   2. Use the following command to check if the connection is active:                    $ docker offload status          

  3. To get more information, run the following command:                    $ docker offload diagnose          

  4. If you're not connected, start a new session:                    $ docker offload start          

  5. Verify authentication with `docker login`.

  6. If needed, you can sign out and then sign in again:                    $ docker logout          $ docker login          

  7. Verify your usage and billing. For more information, see [Docker Offload usage](https://docs.docker.com/offload/usage/).