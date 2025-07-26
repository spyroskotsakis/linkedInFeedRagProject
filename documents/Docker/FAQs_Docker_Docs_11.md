# FAQs | Docker Docs

**URL:** https://docs.docker.com/enterprise/security/hardened-desktop/enhanced-container-isolation/faq/
**Word Count:** 1751
**Links Count:** 658
**Scraped:** 2025-07-16 01:48:09
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Enhanced Container Isolation FAQs

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

### Do I need to change the way I use Docker when ECI is switched on?

No, you can continue to use Docker as usual. ECI works under the covers by creating a more secure container.

### Do all container workloads work well with ECI?

The great majority of container workloads run fine with ECI enabled, but a few do not \(yet\). For the few workloads that don't yet work with Enhanced Container Isolation, Docker is continuing to improve the feature to reduce this to a minimum.

### Can I run privileged containers with ECI?

Yes, you can use the `--privileged` flag in containers but unlike privileged containers without ECI, the container can only use it's elevated privileges to access resources assigned to the container. It can't access global kernel resources in the Docker Desktop Linux VM. This lets you run privileged containers securely \(including Docker-in-Docker\). For more information, see [Key features and benefits](https://docs.docker.com/enterprise/security/hardened-desktop/enhanced-container-isolation/features-benefits/#privileged-containers-are-also-secured).

### Will all privileged container workloads run with ECI?

No. Privileged container workloads that want to access global kernel resources inside the Docker Desktop Linux VM won't work. For example, you can't use a privileged container to load a kernel module.

### Why not just restrict usage of the `--privileged` flag?

Privileged containers are typically used to run advanced workloads in containers, for example Docker-in-Docker or Kubernetes-in-Docker, to perform kernel operations such as loading modules, or to access hardware devices.

ECI allows the running of advanced workloads, but denies the ability to perform kernel operations or access hardware devices.

### Does ECI restrict bind mounts inside the container?

Yes, it restricts bind mounts of directories located in the Docker Desktop Linux VM into the container.

It doesn't restrict bind mounts of your host machine files into the container, as configured via Docker Desktop's **Settings** > **Resources** > **File Sharing**.

### Can I mount the host's Docker Socket into a container when ECI is enabled?

By default, ECI blocks bind-mounting the host's Docker socket into containers, for security reasons. However, there are legitimate use cases for this, such as when using [Testcontainers](https://testcontainers.com/) for local testing.

To enable such use cases, it's possible to configure ECI to allow Docker socket mounts into containers, but only for your chosen \(i.e,. trusted\) container images, and even restrict what commands the container can send to the Docker Engine via the socket. See [ECI Docker socket mount permissions](https://docs.docker.com/enterprise/security/hardened-desktop/enhanced-container-isolation/config/#docker-socket-mount-permissions).

### Does ECI protect all containers launched with Docker Desktop?

Not yet. It protects all containers launched by users via `docker create` and `docker run`.

For containers implicitly created by `docker build` as well as Docker Desktop's integrated Kubernetes, protection varies depending on the Docker Desktop version \(see the following two FAQs\).

### Does ECI protect containers implicitly used by `docker build`?

Prior to Docker Desktop 4.19, ECI did not protect containers used implicitly by `docker build` during the build process.

Since Docker Desktop 4.19, ECI protects containers used by `docker build` when using the [Docker container driver](https://docs.docker.com/build/builders/drivers/).

In addition, since Docker Desktop 4.30, ECI also protects containers used by `docker build` when using the default "docker" build driver, on all platforms supported by Docker Desktop except Windows with WSL 2.

### Does ECI protect Kubernetes in Docker Desktop?

Prior to Docker Desktop 4.38, ECI did not protect the Kubernetes cluster integrated in Docker Desktop.

Since Docker Desktop 4.38, ECI protects the integrated Kubernetes cluster when using the new **kind** provisioner \(see [Deploy On Kubernetes](https://docs.docker.com/desktop/features/kubernetes/)\). In this case, each node in the multi-node Kubernetes cluster is actually an ECI protected container. With ECI disabled, each node in the Kubernetes cluster is a less-secure fully privileged container.

ECI does not protect the integrated Kubernetes cluster when using the older **Kubeadm** single-node cluster provisioner.

### Does ECI protect containers launched prior to enabling ECI?

No. Containers created prior to switching on ECI are not protected. Therefore, it is recommended you remove all containers prior to switching on ECI.

### Does ECI affect the performance of containers?

ECI has little impact on the performance of containers. The exception is for containers that perform lots of `mount` and `umount` system calls, as these are trapped and vetted by the Sysbox container runtime to ensure they are not being used to breach the container's filesystem.

### With ECI, can the user still override the `--runtime` flag from the CLI ?

No. With ECI enabled, Sysbox is set as the default \(and only\) runtime for containers deployed by Docker Desktop users. If a user attempts to override the runtime \(e.g., `docker run --runtime=runc`\), this request is ignored and the container is created through the Sysbox runtime.

The reason `runc` is disallowed is it lets users run as "true root" on the Docker Desktop Linux VM, thereby providing them with implicit control of the VM and the ability to modify the administrative configurations for Docker Desktop.

### How is ECI different from Docker Engine's userns-remap mode?

See [How does it work](https://docs.docker.com/enterprise/security/hardened-desktop/enhanced-container-isolation/how-eci-works/#enhanced-container-isolation-vs-docker-userns-remap-mode).

### How is ECI different from Rootless Docker?

See [How does it work](https://docs.docker.com/enterprise/security/hardened-desktop/enhanced-container-isolation/how-eci-works/#enhanced-container-isolation-vs-rootless-docker)