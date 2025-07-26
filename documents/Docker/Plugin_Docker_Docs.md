# Plugin | Docker Docs

**URL:** https://docs.docker.com/compose/install/linux
**Word Count:** 1264
**Links Count:** 659
**Scraped:** 2025-07-16 02:01:22
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Install the Docker Compose plugin

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

This page contains instructions on how to install the Docker Compose plugin on Linux from the command line.

To install the Docker Compose plugin on Linux, you can either:

  * Set up Docker's repository on your Linux system.   * Install manually.

> Note >  > These instructions assume you already have Docker Engine and Docker CLI installed and now want to install the Docker Compose plugin.

## Install using the repository

  1. Set up the repository. Find distribution-specific instructions in:

[Ubuntu](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository) | [CentOS](https://docs.docker.com/engine/install/centos/#set-up-the-repository) | [Debian](https://docs.docker.com/engine/install/debian/#install-using-the-repository) | [Raspberry Pi OS](https://docs.docker.com/engine/install/raspberry-pi-os/#install-using-the-repository) | [Fedora](https://docs.docker.com/engine/install/fedora/#set-up-the-repository) | [RHEL](https://docs.docker.com/engine/install/rhel/#set-up-the-repository) | [SLES](https://docs.docker.com/engine/install/sles/#set-up-the-repository).

  2. Update the package index, and install the latest version of Docker Compose:

     * For Ubuntu and Debian, run:                        $ sudo apt-get update            $ sudo apt-get install docker-compose-plugin            

     * For RPM-based distributions, run:                        $ sudo yum update            $ sudo yum install docker-compose-plugin            

  3. Verify that Docker Compose is installed correctly by checking the version.                    $ docker compose version          

### Update Docker Compose

To update the Docker Compose plugin, run the following commands:

  * For Ubuntu and Debian, run:                  $ sudo apt-get update         $ sudo apt-get install docker-compose-plugin         

  * For RPM-based distributions, run:                  $ sudo yum update         $ sudo yum install docker-compose-plugin         

## Install the plugin manually

> Warning >  > Manual installations donât auto-update. For ease of maintenance, use the Docker repository method.

  1. To download and install the Docker Compose CLI plugin, run:                    $ DOCKER_CONFIG=${DOCKER_CONFIG:-$HOME/.docker}          $ mkdir -p $DOCKER_CONFIG/cli-plugins          $ curl -SL https://github.com/docker/compose/releases/download/v2.38.2/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/cli-plugins/docker-compose          

This command downloads and installs the latest release of Docker Compose for the active user under `$HOME` directory.

To install:

     * Docker Compose for _all users_ on your system, replace `~/.docker/cli-plugins` with `/usr/local/lib/docker/cli-plugins`.      * A different version of Compose, substitute `v2.38.2` with the version of Compose you want to use.      * For a different architecture, substitute `x86_64` with the [architecture you want](https://github.com/docker/compose/releases).   2. Apply executable permissions to the binary:                    $ chmod +x $DOCKER_CONFIG/cli-plugins/docker-compose          

or, if you chose to install Compose for all users:                    $ sudo chmod +x /usr/local/lib/docker/cli-plugins/docker-compose          

  3. Test the installation.                    $ docker compose version          

## What's next?

  * [Understand how Compose works](https://docs.docker.com/compose/intro/compose-application-model/)   * [Try the Quickstart guide](https://docs.docker.com/compose/gettingstarted/)