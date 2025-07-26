# Linux | Docker Docs

**URL:** https://docs.docker.com/desktop/setup/install/linux/
**Word Count:** 1967
**Links Count:** 672
**Scraped:** 2025-07-16 01:48:52
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Install Docker Desktop on Linux

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

> **Docker Desktop terms** >  > Commercial use of Docker Desktop in larger enterprises \(more than 250 employees or more than $10 million USD in annual revenue\) requires a [paid subscription](https://www.docker.com/pricing/).

This page contains information about general system requirements, supported platforms, and instructions on how to install Docker Desktop for Linux.

> Important >  > Docker Desktop on Linux runs a Virtual Machine \(VM\) which creates and uses a custom docker context, `desktop-linux`, on startup. >  > This means images and containers deployed on the Linux Docker Engine \(before installation\) are not available in Docker Desktop for Linux. >  > Docker Desktop vs Docker Engine: What's the difference? >
>> Important >>  >> For commercial use of Docker Engine obtained via Docker Desktop within larger enterprises \(exceeding 250 employees or with annual revenue surpassing $10 million USD\), a [paid subscription](https://www.docker.com/pricing/) is required. >  > Docker Desktop for Linux provides a user-friendly graphical interface that simplifies the management of containers and services. It includes Docker Engine as this is the core technology that powers Docker containers. Docker Desktop for Linux also comes with additional features like Docker Scout and Docker Extensions. >  > #### Installing Docker Desktop and Docker Engine >  > Docker Desktop for Linux and Docker Engine can be installed side-by-side on the same machine. Docker Desktop for Linux stores containers and images in an isolated storage location within a VM and offers controls to restrict [its resources](https://docs.docker.com/desktop/settings-and-maintenance/settings/#resources). Using a dedicated storage location for Docker Desktop prevents it from interfering with a Docker Engine installation on the same machine. >  > While it's possible to run both Docker Desktop and Docker Engine simultaneously, there may be situations where running both at the same time can cause issues. For example, when mapping network ports \(`-p` / `--publish`\) for containers, both Docker Desktop and Docker Engine may attempt to reserve the same port on your machine, which can lead to conflicts \("port already in use"\). >  > We generally recommend stopping the Docker Engine while you're using Docker Desktop to prevent the Docker Engine from consuming resources and to prevent conflicts as described above. >  > Use the following command to stop the Docker Engine service: >      >      >     $ sudo systemctl stop docker docker.socket containerd >      >  > Depending on your installation, the Docker Engine may be configured to automatically start as a system service when your machine starts. Use the following command to disable the Docker Engine service, and to prevent it from starting automatically: >      >      >     $ sudo systemctl disable docker docker.socket containerd >      >  > ### Switching between Docker Desktop and Docker Engine >  > The Docker CLI can be used to interact with multiple Docker Engines. For example, you can use the same Docker CLI to control a local Docker Engine and to control a remote Docker Engine instance running in the cloud. [Docker Contexts](https://docs.docker.com/engine/manage-resources/contexts/) allow you to switch between Docker Engines instances. >  > When installing Docker Desktop, a dedicated "desktop-linux" context is created to interact with Docker Desktop. On startup, Docker Desktop automatically sets its own context \(`desktop-linux`\) as the current context. This means that subsequent Docker CLI commands target Docker Desktop. On shutdown, Docker Desktop resets the current context to the `default` context. >  > Use the `docker context ls` command to view what contexts are available on your machine. The current context is indicated with an asterisk \(`*`\). >      >      >     $ docker context ls >     NAME            DESCRIPTION                               DOCKER ENDPOINT                                  ... >     default *       Current DOCKER_HOST based configuration   unix:///var/run/docker.sock                      ... >     desktop-linux                                             unix:///home/<user>/.docker/desktop/docker.sock  ...         >      >  > If you have both Docker Desktop and Docker Engine installed on the same machine, you can run the `docker context use` command to switch between the Docker Desktop and Docker Engine contexts. For example, use the "default" context to interact with the Docker Engine: >      >      >     $ docker context use default >     default >     Current context is now "default" >      >  > And use the `desktop-linux` context to interact with Docker Desktop: >      >      >     $ docker context use desktop-linux >     desktop-linux >     Current context is now "desktop-linux" >      >  > Refer to the [Docker Context documentation](https://docs.docker.com/engine/manage-resources/contexts/) for more details.

## Supported platforms

Docker provides `.deb` and `.rpm` packages for the following Linux distributions and architectures:

Platform| x86\_64 / amd64   ---|---   [Ubuntu](https://docs.docker.com/desktop/setup/install/linux/ubuntu/)| â    [Debian](https://docs.docker.com/desktop/setup/install/linux/debian/)| â    [Red Hat Enterprise Linux \(RHEL\)](https://docs.docker.com/desktop/setup/install/linux/rhel/)| â    [Fedora](https://docs.docker.com/desktop/setup/install/linux/fedora/)| â       An experimental package is available for [Arch](https://docs.docker.com/desktop/setup/install/linux/archlinux/)-based distributions. Docker has not tested or verified the installation.

Docker supports Docker Desktop on the current LTS release of the aforementioned distributions and the most recent version. As new versions are made available, Docker stops supporting the oldest version and supports the newest version.

## General system requirements

To install Docker Desktop successfully, your Linux host must meet the following general requirements:

  * 64-bit kernel and CPU support for virtualization.   * KVM virtualization support. Follow the KVM virtualization support instructions to check if the KVM kernel modules are enabled and how to provide access to the KVM device.   * QEMU must be version 5.2 or later. We recommend upgrading to the latest version.   * systemd init system.   * GNOME, KDE, or MATE desktop environment.     * For many Linux distributions, the GNOME environment does not support tray icons. To add support for tray icons, you need to install a GNOME extension. For example, [AppIndicator](https://extensions.gnome.org/extension/615/appindicator-support/).   * At least 4 GB of RAM.   * Enable configuring ID mapping in user namespaces, see [File sharing](https://docs.docker.com/desktop/troubleshoot-and-support/faqs/linuxfaqs/#how-do-i-enable-file-sharing). Note that for Docker Desktop version 4.35 and later, this is not required anymore.   * Recommended: [Initialize `pass`](https://docs.docker.com/desktop/setup/sign-in/#credentials-management-for-linux-users) for credentials management.

Docker Desktop for Linux runs a Virtual Machine \(VM\). For more information on why, see [Why Docker Desktop for Linux runs a VM](https://docs.docker.com/desktop/troubleshoot-and-support/faqs/linuxfaqs/#why-does-docker-desktop-for-linux-run-a-vm).

> Note >  > Docker does not provide support for running Docker Desktop for Linux in nested virtualization scenarios. We recommend that you run Docker Desktop for Linux natively on supported distributions.

### KVM virtualization support

Docker Desktop runs a VM that requires [KVM support](https://www.linux-kvm.org).

The `kvm` module should load automatically if the host has virtualization support. To load the module manually, run:               $ modprobe kvm     

Depending on the processor of the host machine, the corresponding module must be loaded:               $ modprobe kvm_intel  # Intel processors          $ modprobe kvm_amd    # AMD processors     

If the above commands fail, you can view the diagnostics by running:               $ kvm-ok     

To check if the KVM modules are enabled, run:               $ lsmod | grep kvm     kvm_amd               167936  0     ccp                   126976  1 kvm_amd     kvm                  1089536  1 kvm_amd     irqbypass              16384  1 kvm     

#### Set up KVM device user permissions

To check ownership of `/dev/kvm`, run :               $ ls -al /dev/kvm     

Add your user to the kvm group in order to access the kvm device:               $ sudo usermod -aG kvm $USER     

Sign out and sign back in so that your group membership is re-evaluated.

## Where to go next

  * Install Docker Desktop for Linux for your specific Linux distribution:     * [Install on Ubuntu](https://docs.docker.com/desktop/setup/install/linux/ubuntu/)     * [Install on Debian](https://docs.docker.com/desktop/setup/install/linux/debian/)     * [Install on Red Hat Enterprise Linux \(RHEL\)](https://docs.docker.com/desktop/setup/install/linux/rhel/)     * [Install on Fedora](https://docs.docker.com/desktop/setup/install/linux/fedora/)     * [Install on Arch](https://docs.docker.com/desktop/setup/install/linux/archlinux/)