# Standalone | Docker Docs

**URL:** https://docs.docker.com/compose/install/standalone/
**Word Count:** 1280
**Links Count:** 647
**Scraped:** 2025-07-16 01:47:29
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Install the Docker Compose standalone

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

This page contains instructions on how to install Docker Compose standalone on Linux or Windows Server, from the command line.

> Warning >  > The Docker Compose standalone uses the `-compose` syntax instead of the current standard syntax `compose`.   > For example, you must type `docker-compose up` when using Docker Compose standalone, instead of `docker compose up`. Use it only for backward compatibility.

## On Linux

  1. To download and install the Docker Compose standalone, run:                    $ curl -SL https://github.com/docker/compose/releases/download/v2.38.2/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose          

  2. Apply executable permissions to the standalone binary in the target path for the installation.                    $ chmod +x /usr/local/bin/docker-compose          

  3. Test and execute Docker Compose commands using `docker-compose`.

> Tip >  > If the command `docker-compose` fails after installation, check your path. You can also create a symbolic link to `/usr/bin` or any other directory in your path. For example: >      >      >     $ sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose >     

## On Windows Server

Follow these instructions if you are [running the Docker daemon directly on Microsoft Windows Server](https://docs.docker.com/engine/install/binaries/#install-server-and-client-binaries-on-windows) and want to install Docker Compose.

  1. Run PowerShell as an administrator. In order to proceed with the installation, select **Yes** when asked if you want this app to make changes to your device.

  2. Optional. Ensure TLS1.2 is enabled. GitHub requires TLS1.2 for secure connections. If youâre using an older version of Windows Server, for example 2016, or suspect that TLS1.2 is not enabled, run the following command in PowerShell:                    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

  3. Download the latest release of Docker Compose \(v2.38.2\). Run the following command:                    Start-BitsTransfer -Source "https://github.com/docker/compose/releases/download/v2.38.2/docker-compose-windows-x86_64.exe" -Destination $Env:ProgramFiles\Docker\docker-compose.exe

To install a different version of Docker Compose, substitute `v2.38.2` with the version of Compose you want to use.

> Note >  > On Windows Server 2019 you can add the Compose executable to `$Env:ProgramFiles\Docker`. Because this directory is registered in the system `PATH`, you can run the `docker-compose --version` command on the subsequent step with no additional configuration.

  4. Test the installation.                    $ docker-compose.exe version          Docker Compose version v2.38.2          

## What's next?

  * [Understand how Compose works](https://docs.docker.com/compose/intro/compose-application-model/)   * [Try the Quickstart guide](https://docs.docker.com/compose/gettingstarted/)