# Binaries | Docker Docs

**URL:** http://docs.docker.com/engine/install/binaries
**Word Count:** 2041
**Links Count:** 677
**Scraped:** 2025-07-16 02:09:54
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](http://docs.docker.com/get-started/)   * [Guides](http://docs.docker.com/guides/)   * [Reference](http://docs.docker.com/reference/)

* * *

# Install Docker Engine from binaries

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

> Important >  > This page contains information on how to install Docker using binaries. These instructions are mostly suitable for testing purposes. We do not recommend installing Docker using binaries in production environments as they don't have automatic security updates. The Linux binaries described on this page are statically linked, which means that vulnerabilities in build-time dependencies are not automatically patched by security updates of your Linux distribution. >  > Updating binaries is also slightly more involved when compared to Docker packages installed using a package manager or through Docker Desktop, as it requires \(manually\) updating the installed version whenever there is a new release of Docker. >  > Also, static binaries may not include all functionalities provided by the dynamic packages. >  > On Windows and Mac, we recommend that you install [Docker Desktop](https://docs.docker.com/desktop/) instead. For Linux, we recommend that you follow the instructions specific for your distribution.

If you want to try Docker or use it in a testing environment, but you're not on a supported platform, you can try installing from static binaries. If possible, you should use packages built for your operating system, and use your operating system's package management system to manage Docker installation and upgrades.

Static binaries for the Docker daemon binary are only available for Linux \(as `dockerd`\) and Windows \(as `dockerd.exe`\). Static binaries for the Docker client are available for Linux, Windows, and macOS \(as `docker`\).

This topic discusses binary installation for Linux, Windows, and macOS:

  * Install daemon and client binaries on Linux   * Install client binaries on macOS   * Install server and client binaries on Windows

## Install daemon and client binaries on Linux

### Prerequisites

Before attempting to install Docker from binaries, be sure your host machine meets the prerequisites:

  * A 64-bit installation   * Version 3.10 or higher of the Linux kernel. The latest version of the kernel available for your platform is recommended.   * `iptables` version 1.4 or higher   * `git` version 1.7 or higher   * A `ps` executable, usually provided by `procps` or a similar package.   * [XZ Utils](https://tukaani.org/xz/) 4.9 or higher   * A [properly mounted](https://github.com/tianon/cgroupfs-mount/blob/master/cgroupfs-mount) `cgroupfs` hierarchy; a single, all-encompassing `cgroup` mount point is not sufficient. See Github issues [\#2683](https://github.com/moby/moby/issues/2683), [\#3485](https://github.com/moby/moby/issues/3485), [\#4568](https://github.com/moby/moby/issues/4568)\).

#### Secure your environment as much as possible

##### OS considerations

Enable SELinux or AppArmor if possible.

It is recommended to use AppArmor or SELinux if your Linux distribution supports either of the two. This helps improve security and blocks certain types of exploits. Review the documentation for your Linux distribution for instructions for enabling and configuring AppArmor or SELinux.

> **Security warning** >  > If either of the security mechanisms is enabled, do not disable it as a work-around to make Docker or its containers run. Instead, configure it correctly to fix any problems.

##### Docker daemon considerations

  * Enable `seccomp` security profiles if possible. See [Enabling `seccomp` for Docker](https://docs.docker.com/engine/security/seccomp/).

  * Enable user namespaces if possible. See the [Daemon user namespace options](http://docs.docker.com/reference/cli/dockerd/#daemon-user-namespace-options).

### Install static binaries

  1. Download the static binary archive. Go to <https://download.docker.com/linux/static/stable/>, choose your hardware platform, and download the `.tgz` file relating to the version of Docker Engine you want to install.

  2. Extract the archive using the `tar` utility. The `dockerd` and `docker` binaries are extracted.                    $ tar xzvf /path/to/<FILE>.tar.gz          

  3. **Optional** : Move the binaries to a directory on your executable path, such as `/usr/bin/`. If you skip this step, you must provide the path to the executable when you invoke `docker` or `dockerd` commands.                    $ sudo cp docker/* /usr/bin/          

  4. Start the Docker daemon:                    $ sudo dockerd &          

If you need to start the daemon with additional options, modify the above command accordingly or create and edit the file `/etc/docker/daemon.json` to add the custom configuration options.

  5. Verify that Docker is installed correctly by running the `hello-world` image.                    $ sudo docker run hello-world          

This command downloads a test image and runs it in a container. When the container runs, it prints a message and exits.

You have now successfully installed and started Docker Engine.

> Tip >  > Receiving errors when trying to run without root? >  > The `docker` user group exists but contains no users, which is why youâre required to use `sudo` to run Docker commands. Continue to [Linux postinstall](http://docs.docker.com/engine/install/linux-postinstall) to allow non-privileged users to run Docker commands and for other optional configuration steps.

## Install client binaries on macOS

> Note >  > The following instructions are mostly suitable for testing purposes. The macOS binary includes the Docker client only. It does not include the `dockerd` daemon which is required to run containers. Therefore, we recommend that you install [Docker Desktop](https://docs.docker.com/desktop/) instead.

The binaries for Mac also do not contain:

  * A runtime environment. You must set up a functional engine either in a Virtual Machine, or on a remote Linux machine.   * Docker components such as `buildx` and `docker compose`.

To install client binaries, perform the following steps:

  1. Download the static binary archive. Go to <https://download.docker.com/mac/static/stable/> and select `x86_64` \(for Mac on Intel chip\) or `aarch64` \(for Mac on Apple silicon\), and then download the `.tgz` file relating to the version of Docker Engine you want to install.

  2. Extract the archive using the `tar` utility. The `docker` binary is extracted.                    $ tar xzvf /path/to/<FILE>.tar.gz          

  3. Clear the extended attributes to allow it run.                    $ sudo xattr -rc docker          

Now, when you run the following command, you can see the Docker CLI usage instructions:                    $ docker/docker          

  4. **Optional** : Move the binary to a directory on your executable path, such as `/usr/local/bin/`. If you skip this step, you must provide the path to the executable when you invoke `docker` or `dockerd` commands.                    $ sudo cp docker/docker /usr/local/bin/          

  5. Verify that Docker is installed correctly by running the `hello-world` image. The value of `<hostname>` is a hostname or IP address running the Docker daemon and accessible to the client.                    $ sudo docker -H <hostname> run hello-world          

This command downloads a test image and runs it in a container. When the container runs, it prints a message and exits.

## Install server and client binaries on Windows

> Note >  > The following section describes how to install the Docker daemon on Windows Server which allows you to run Windows containers only. When you install the Docker daemon on Windows Server, the daemon doesn't contain Docker components such as `buildx` and `compose`. If you're running Windows 10 or 11, we recommend that you install [Docker Desktop](https://docs.docker.com/desktop/) instead.

Binary packages on Windows include both `dockerd.exe` and `docker.exe`. On Windows, these binaries only provide the ability to run native Windows containers \(not Linux containers\).

To install server and client binaries, perform the following steps:

  1. Download the static binary archive. Go to <https://download.docker.com/win/static/stable/x86_64> and select the latest version from the list.

  2. Run the following PowerShell commands to install and extract the archive to your program files:                    PS C:\> Expand-Archive /path/to/<FILE>.zip -DestinationPath $Env:ProgramFiles

  3. Register the service and start the Docker Engine:                    PS C:\> &$Env:ProgramFiles\Docker\dockerd --register-service          PS C:\> Start-Service docker

  4. Verify that Docker is installed correctly by running the `hello-world` image.                    PS C:\> &$Env:ProgramFiles\Docker\docker run hello-world:nanoserver

This command downloads a test image and runs it in a container. When the container runs, it prints a message and exits.

## Upgrade static binaries

To upgrade your manual installation of Docker Engine, first stop any `dockerd` or `dockerd.exe` processes running locally, then follow the regular installation steps to install the new version on top of the existing version.

## Next steps

  * Continue to [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/).