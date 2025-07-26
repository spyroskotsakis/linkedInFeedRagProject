# Container | Docker Docs

**URL:** https://docs.docker.com/security/faqs/containers/
**Word Count:** 1416
**Links Count:** 646
**Scraped:** 2025-07-16 01:46:47
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Container security FAQs

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

### How are containers isolated from the host in Docker Desktop?

Docker Desktop runs all containers inside a customized / minimal Linux virtual machine \(except for native Windows containers\). This adds a strong layer of isolation between containers and the host the machine, even if containers are running rootful.

However note the following:

  * Containers have access to host files configured for file sharing via Settings -> Resources -> File Sharing \(see the next FAQ question below for more info\).

  * By default, containers run as root but with limited capabilities inside the Docker Desktop VM. Containers running with elevated privileges \(e.g., `--privileged`, `--pid=host`, `--cap-add`, etc.\) run as root with elevated privileges inside the Docker Desktop VM which gives them access to Docker Desktop VM internals, including the Docker Engine. Thus, users must be careful which containers they run with such privileges to avoid security breaches by malicious container images.

  * If [Enhanced Container Isolation \(ECI\)](https://docs.docker.com/enterprise/security/hardened-desktop/enhanced-container-isolation/) mode is enabled, then each container runs within a dedicated Linux User Namespace inside the Docker Desktop VM, which means the container has no privileges within the Docker Desktop VM. Even when using the `--privileged` flag or similar, the container processes will only be privileged within the container's logical boundary, but unprivileged otherwise. In addition, ECI protects uses other advanced techniques to ensure they can't easily breach the Docker Desktop VM and Docker Engine within \(see the ECI section for more info\). No changes to the containers or user workflows are required as the extra protection is added under the covers.

### To which portions of the host filesystem do containers have read and write access?

Containers can only access host files if these are shared via Settings -> Resources -> File Sharing, and only when such files are bind-mounted into the container \(e.g., `docker run -v /path/to/host/file:/mnt ...`\).

### Can containers running as root gain access to admin-owned files or directories on the host?

No; host file sharing \(bind mount from the host filesystem\) uses a user-space crafted file server \(running in `com.docker.backend` as the user running Docker Desktop\), so containers canât gain any access that the user on the host doesnât already have.