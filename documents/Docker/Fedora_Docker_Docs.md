# Fedora | Docker Docs

**URL:** https://docs.docker.com/desktop/setup/install/linux/fedora
**Word Count:** 1634
**Links Count:** 668
**Scraped:** 2025-07-16 02:01:22
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Install Docker Desktop on Fedora

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

> **Docker Desktop terms** >  > Commercial use of Docker Desktop in larger enterprises \(more than 250 employees OR more than $10 million USD in annual revenue\) requires a [paid subscription](https://www.docker.com/pricing/).

This page contains information on how to install, launch and upgrade Docker Desktop on a Fedora distribution.

## Prerequisites

To install Docker Desktop successfully, you must:

  * Meet the [general system requirements](https://docs.docker.com/desktop/setup/install/linux/#general-system-requirements).

  * Have a 64-bit version of Fedora 41 or Fedora 42.

  * For a GNOME desktop environment you must install AppIndicator and KStatusNotifierItem [GNOME extensions](https://extensions.gnome.org/extension/615/appindicator-support/).

  * If you're not using GNOME, you must install `gnome-terminal` to enable terminal access from Docker Desktop:                  $ sudo dnf install gnome-terminal         

## Install Docker Desktop

To install Docker Desktop on Fedora:

  1. Set up [Docker's package repository](https://docs.docker.com/engine/install/fedora/#set-up-the-repository).

  2. Download the latest [RPM package](https://desktop.docker.com/linux/main/amd64/docker-desktop-x86_64.rpm?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-linux-amd64). For checksums, see the [Release notes](https://docs.docker.com/desktop/release-notes/).

  3. Install the package with dnf as follows:                    $ sudo dnf install ./docker-desktop-x86_64.rpm          

By default, Docker Desktop is installed at `/opt/docker-desktop`.

The RPM package includes a post-install script that completes additional setup steps automatically.

The post-install script:

  * Sets the capability on the Docker Desktop binary to map privileged ports and set resource limits.   * Adds a DNS name for Kubernetes to `/etc/hosts`.   * Creates a symlink from `/usr/local/bin/com.docker.cli` to `/usr/bin/docker`. This is because the classic Docker CLI is installed at `/usr/bin/docker`. The Docker Desktop installer also installs a Docker CLI binary that includes cloud-integration capabilities and is essentially a wrapper for the Compose CLI, at`/usr/local/bin/com.docker.cli`. The symlink ensures that the wrapper can access the classic Docker CLI.

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

## Upgrade Docker Desktop

Once a new version for Docker Desktop is released, the Docker UI shows a notification. You need to first remove the previous version and then download the new package each time you want to upgrade Docker Desktop. Run:               $ sudo dnf remove docker-desktop     $ sudo dnf install ./docker-desktop-x86_64.rpm     

## Next steps

  * Explore [Docker's subscriptions](https://www.docker.com/pricing/) to see what Docker can offer you.   * Take a look at the [Docker workshop](https://docs.docker.com/get-started/workshop/) to learn how to build an image and run it as a containerized application.   * [Explore Docker Desktop](https://docs.docker.com/desktop/use-desktop/) and all its features.   * [Troubleshooting](https://docs.docker.com/desktop/troubleshoot-and-support/troubleshoot/) describes common problems, workarounds, how to run and submit diagnostics, and submit issues.   * [FAQs](https://docs.docker.com/desktop/troubleshoot-and-support/faqs/general/) provide answers to frequently asked questions.   * [Release notes](https://docs.docker.com/desktop/release-notes/) lists component updates, new features, and improvements associated with Docker Desktop releases.   * [Back up and restore data](https://docs.docker.com/desktop/settings-and-maintenance/backup-and-restore/) provides instructions on backing up and restoring data related to Docker.