# Antivirus software and Docker | Docker Docs

**URL:** https://docs.docker.com/engine/security/antivirus/
**Word Count:** 1107
**Links Count:** 635
**Scraped:** 2025-07-16 01:49:39
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Antivirus software and Docker

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

* * *

When antivirus software scans files used by Docker, these files may be locked in a way that causes Docker commands to hang.

One way to reduce these problems is to add the Docker data directory \(`/var/lib/docker` on Linux, `%ProgramData%\docker` on Windows Server, or `$HOME/Library/Containers/com.docker.docker/` on Mac\) to the antivirus's exclusion list. However, this comes with the trade-off that viruses or malware in Docker images, writable layers of containers, or volumes are not detected. If you do choose to exclude Docker's data directory from background virus scanning, you may want to schedule a recurring task that stops Docker, scans the data directory, and restarts Docker.