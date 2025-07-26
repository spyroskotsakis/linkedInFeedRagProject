# Enhanced Container Isolation | Docker Docs

**URL:** http://docs.docker.com/security/for-admins/hardened-desktop/enhanced-container-isolation
**Word Count:** 1995
**Links Count:** 672
**Scraped:** 2025-07-16 02:08:05
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](http://docs.docker.com/get-started/)   * [Guides](http://docs.docker.com/guides/)   * [Reference](http://docs.docker.com/reference/)

* * *

# What is Enhanced Container Isolation?

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Subscription: Business

For: Administrators

Enhanced Container Isolation \(ECI\) provides an additional layer of security to prevent malicious workloads running in containers from compromising Docker Desktop or the host.

It uses a variety of advanced techniques to harden container isolation, but without impacting developer productivity.

Enhanced Container Isolation ensures stronger container isolation and also locks in any security configurations that have been created by administrators, for instance through [Registry Access Management policies](https://docs.docker.com/enterprise/security/hardened-desktop/registry-access-management/) or with [Settings Management](https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/).

> Note >  > ECI is in addition to other container security techniques used by Docker. For example, reduced Linux Capabilities, seccomp, and AppArmor.

## Who is it for?

  * For organizations and developers that want to prevent container attacks and reduce vulnerabilities in developer environments.   * For organizations that want to ensure stronger container isolation that is easy and intuitive to implement on developers' machines.

## What happens when Enhanced Container Isolation is turned on?

When Enhanced Container Isolation is turned on, the following features and security techniques are enabled:

  * All user containers are automatically run in Linux user namespaces which ensures stronger isolation. Each container runs in a dedicated Linux user-namespace.   * The root user in the container maps to an unprivileged user inside the Docker Desktop Linux VM.   * Containers become harder to breach. For example, sensitive system calls are vetted and portions of `/proc` and `/sys` are emulated inside the container.   * Users can continue using containers as usual, including bind mounting host directories, volumes, etc.   * No change in the way developers run containers, and no special container images are required.   * Privileged containers \(e.g., `--privileged` flag\) work, but they are only privileged within the container's Linux user namespace, not in the Docker Desktop VM. Therefore they can't be used to breach the Docker Desktop VM.   * Docker-in-Docker and even Kubernetes-in-Docker works, but run unprivileged inside the Docker Desktop Linux VM.

In addition, the following restrictions are imposed:

  * Containers can no longer share namespaces with the Docker Desktop VM \(e.g., `--network=host`, `--pid=host` are disallowed\).   * Containers can no longer modify configuration files inside the Docker Desktop VM \(e.g., mounting any VM directory into the container is disallowed\).   * Containers can no longer access the Docker Engine. For example, mounting the Docker Engine's socket into the container is restricted which prevents malicious containers from gaining control of the Docker Engine. Administrators can relax this for [trusted container images](https://docs.docker.com/enterprise/security/hardened-desktop/enhanced-container-isolation/config/).   * Console access to the Docker Desktop VM is forbidden for all users.

These features and restrictions ensure that containers are better secured at runtime, with minimal impact to developer experience and productivity. Developers can continue to use Docker Desktop as usual, but the containers they launch are more strongly isolated.

For more information on how Enhanced Container Isolation work, see [How does it work](https://docs.docker.com/enterprise/security/hardened-desktop/enhanced-container-isolation/how-eci-works/).

> Important >  > ECI protection for Docker builds and [Kubernetes in Docker Desktop](https://docs.docker.com/desktop/features/kubernetes/) varies according to the Docker Desktop version. Later versions include more protection than earlier versions. Also, ECI does not yet protect extension containers. For more information on known limitations and workarounds, see [FAQs](https://docs.docker.com/enterprise/security/hardened-desktop/enhanced-container-isolation/faq/).

## How do I enable Enhanced Container Isolation?

### As a developer

To enable Enhanced Container Isolation as a developer:

  1. Ensure your organization has a Docker Business subscription.   2. Sign in to your organization in Docker Desktop. This will ensure the ECI feature is available to you in Docker Desktop's Settings menu.   3. Stop and remove all existing containers.   4. Navigate to **Settings** > **General** in Docker Desktop.   5. Next to **Use Enhanced Container Isolation** , select the checkbox.   6. Select **Apply and restart** to save your settings.

> Important >  > Enhanced Container Isolation does not protect containers created prior to enabling ECI. For more information on known limitations and workarounds, see [FAQs](https://docs.docker.com/enterprise/security/hardened-desktop/enhanced-container-isolation/faq/).

### As an administrator

#### Prerequisite

You first need to [enforce sign-in](https://docs.docker.com/enterprise/security/enforce-sign-in/) to ensure that all Docker Desktop developers authenticate with your organization. Since Settings Management requires a Docker Business subscription, enforced sign-in guarantees that only authenticated users have access and that the feature consistently takes effect across all users, even though it may still work without enforced sign-in.

#### Setup

[Create and configure the `admin-settings.json` file](https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/configure-json-file/) and specify:               {       "configurationFileVersion": 2,       "enhancedContainerIsolation": {         "value": true,         "locked": true       }     }

Setting `"value": true` ensures ECI is enabled by default. By setting `"locked": true`, ECI can't be disabled by developers. If you want to give developers the ability to disable the feature, set `"locked": false`.

In addition, you can also [configure Docker socket mount permissions for containers](https://docs.docker.com/enterprise/security/hardened-desktop/enhanced-container-isolation/config/).

For this to take effect:

  * On a new install, developers need to launch Docker Desktop and authenticate to their organization.   * On an existing install, developers need to quit Docker Desktop through the Docker menu, and then relaunch Docker Desktop. If they are already signed in, they donât need to sign in again for the changes to take effect.

> Important >  > Selecting **Restart** from the Docker menu isn't enough as it only restarts some components of Docker Desktop.

## What do users see when this setting is enforced by an administrator?

> Tip >  > You can now also configure these settings in the [Docker Admin Console](https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/configure-admin-console/).

When Enhanced Container Isolation is enabled, users see:

  * **Use Enhanced Container Isolation** toggled on in **Settings** > **General**.   * Containers run within a Linux user namespace.

To check, run:               $ docker run --rm alpine cat /proc/self/uid_map     

The following output displays:                        0     100000      65536

This indicates that the container's root user \(0\) maps to unprivileged user \(100000\) in the Docker Desktop VM, and that the mapping extends for a range of 64K user-IDs. If a container process were to escape the container, it would find itself without privileges at the VM level. The user-ID mapping varies with each new container, as each container gets an exclusive range of host User-IDs for isolation. User-ID mapping is automatically managed by Docker Desktop. For further details, see [How Enhanced Container Isolation works](https://docs.docker.com/enterprise/security/hardened-desktop/enhanced-container-isolation/how-eci-works/).

In contrast, without ECI the Linux user namespace is not used for containers, the following displays:                        0          0 4294967295

This means that the root user in the container \(0\) is in fact the root user in the Docker Desktop VM \(0\) which reduces container isolation.

Since Enhanced Container Isolation [uses the Sysbox container runtime](https://docs.docker.com/enterprise/security/hardened-desktop/enhanced-container-isolation/how-eci-works/) embedded in the Docker Desktop Linux VM, another way to determine if a container is running with Enhanced Container Isolation is by using `docker inspect`:               $ docker inspect --format='{{.HostConfig.Runtime}}' my_container     

It outputs:               sysbox-runc

Without Enhanced Container Isolation, `docker inspect` outputs `runc`, which is the standard OCI runtime.

## More resources

  * [Video: Enhanced Container Isolation](https://www.youtube.com/watch?v=oA1WQZWnTAk)