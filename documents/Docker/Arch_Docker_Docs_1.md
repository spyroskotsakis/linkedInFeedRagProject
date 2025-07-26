# Arch | Docker Docs

**URL:** https://docs.docker.com/desktop/setup/install/linux/archlinux/
**Word Count:** 1482
**Links Count:** 663
**Scraped:** 2025-07-16 01:49:39
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Install Docker Desktop on Arch-based distributions

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Availability: Experimental 

> **Docker Desktop terms** >  > Commercial use of Docker Desktop in larger enterprises \(more than 250 employees OR more than $10 million USD in annual revenue\) requires a [paid subscription](https://www.docker.com/pricing/).

This page contains information on how to install, launch and upgrade Docker Desktop on an Arch-based distribution.

## Prerequisites

To install Docker Desktop successfully, you must meet the [general system requirements](https://docs.docker.com/desktop/setup/install/linux/#general-system-requirements).

## Install Docker Desktop

  1. [Install the Docker client binary on Linux](https://docs.docker.com/engine/install/binaries/#install-daemon-and-client-binaries-on-linux). Static binaries for the Docker client are available for Linux as `docker`. You can use:                    $ wget https://download.docker.com/linux/static/stable/x86_64/docker-28.3.2.tgz -qO- | tar xvfz - docker/docker --strip-components=1          $ mv ./docker /usr/local/bin          

  2. Download the latest Arch package from the [Release notes](https://docs.docker.com/desktop/release-notes/).

  3. Install the package:                    $ sudo pacman -U ./docker-desktop-x86_64.pkg.tar.zst          

By default, Docker Desktop is installed at `/opt/docker-desktop`.

## Launch Docker Desktop

To start Docker Desktop for Linux:

  1. Navigate to the Docker Desktop application in your Gnome/KDE Desktop.

  2. Select **Docker Desktop** to start Docker.

The Docker Subscription Service Agreement displays.

  3. Select **Accept** to continue. Docker Desktop starts after you accept the terms.

Note that Docker Desktop won't run if you do not agree to the terms. You can choose to accept the terms at a later date by opening Docker Desktop.

For more information, see [Docker Desktop Subscription Service Agreement](https://www.docker.com/legal/docker-subscription-service-agreement). It is recommended that you also read the [FAQs](https://www.docker.com/pricing/faq).

Alternatively, open a terminal and run:               $ systemctl --user start docker-desktop     

When Docker Desktop starts, it creates a dedicated [context](https://docs.docker.com/engine/context/working-with-contexts) that the Docker CLI can use as a target and sets it as the current context in use. This is to avoid a clash with a local Docker Engine that may be running on the Linux host and using the default context. On shutdown, Docker Desktop resets the current context to the previous one.

The Docker Desktop installer updates Docker Compose and the Docker CLI binaries on the host. It installs Docker Compose V2 and gives users the choice to link it as docker-compose from the Settings panel. Docker Desktop installs the new Docker CLI binary that includes cloud-integration capabilities in `/usr/local/bin/com.docker.cli` and creates a symlink to the classic Docker CLI at `/usr/local/bin`.

After youâve successfully installed Docker Desktop, you can check the versions of these binaries by running the following commands:               $ docker compose version     Docker Compose version v2.29.1          $ docker --version     Docker version 27.1.1, build 6312585          $ docker version     Client:       Version:           23.0.5      API version:       1.42      Go version:        go1.21.12     <...>     

To enable Docker Desktop to start on sign in, from the Docker menu, select **Settings** > **General** > **Start Docker Desktop when you sign in to your computer**.

Alternatively, open a terminal and run:               $ systemctl --user enable docker-desktop     

To stop Docker Desktop, select the Docker menu icon to open the Docker menu and select **Quit Docker Desktop**.

Alternatively, open a terminal and run:               $ systemctl --user stop docker-desktop     

## Next steps

  * Explore [Docker's subscriptions](https://www.docker.com/pricing/) to see what Docker can offer you.   * Take a look at the [Docker workshop](https://docs.docker.com/get-started/workshop/) to learn how to build an image and run it as a containerized application.   * [Explore Docker Desktop](https://docs.docker.com/desktop/use-desktop/) and all its features.   * [Troubleshooting](https://docs.docker.com/desktop/troubleshoot-and-support/troubleshoot/) describes common problems, workarounds, how to run and submit diagnostics, and submit issues.   * [FAQs](https://docs.docker.com/desktop/troubleshoot-and-support/faqs/general/) provide answers to frequently asked questions.   * [Release notes](https://docs.docker.com/desktop/release-notes/) lists component updates, new features, and improvements associated with Docker Desktop releases.   * [Back up and restore data](https://docs.docker.com/desktop/settings-and-maintenance/backup-and-restore/) provides instructions on backing up and restoring data related to Docker.