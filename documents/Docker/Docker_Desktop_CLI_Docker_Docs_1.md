# Docker Desktop CLI | Docker Docs

**URL:** https://docs.docker.com/desktop/features/desktop-cli/
**Word Count:** 1160
**Links Count:** 643
**Scraped:** 2025-07-16 01:49:17
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Use the Docker Desktop CLI

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Requires: Docker Desktop [4.37](https://docs.docker.com/desktop/release-notes/#4370) and later

The Docker Desktop CLI lets you perform key operations such as starting, stopping, restarting, and updating Docker Desktop directly from the command line.

The Docker Desktop CLI provides:

  * Simplified automation for local development: Execute Docker Desktop operations more efficiently in scripts and tests.   * An improved developer experience: Restart, quit, or reset Docker Desktop from the command line, reducing dependency on the Docker Desktop Dashboard and improving flexibility and efficiency.

## Usage               docker desktop COMMAND [OPTIONS]     

## Commands

Command| Description   ---|---   `start`| Starts Docker Desktop   `stop`| Stops Docker Desktop   `restart`| Restarts Docker Desktop   `status`| Displays whether Docker Desktop is running or stopped.   `engine ls`| Lists available engines \(Windows only\)   `engine use`| Switch between Linux and Windows containers \(Windows only\)   `update`| Manage Docker Desktop updates. Available for Mac only with Docker Desktop version 4.38, or all OSs with Docker Desktop version 4.39 and later.   `logs`| Print log entries   `disable`| Disable a feature   `enable`| Enable a feature   `version`| Show the Docker Desktop CLI plugin version information   `module`| Manage Docker Desktop modules      For more details on each command, see the [Docker Desktop CLI reference](https://docs.docker.com/reference/cli/docker/desktop/).