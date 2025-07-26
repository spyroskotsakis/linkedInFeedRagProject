# Docker Scout environment variables | Docker Docs

**URL:** https://docs.docker.com/scout/how-tos/configure-cli
**Word Count:** 1176
**Links Count:** 639
**Scraped:** 2025-07-16 02:00:53
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Configure Docker Scout with environment variables

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

The following environment variables are available to configure the Docker Scout CLI commands, and the corresponding `docker/scout-cli` container image:

Name| Format| Description   ---|---|---   DOCKER\_SCOUT\_CACHE\_FORMAT| String| Format of the local image cache; can be `oci` or `tar` \(default: `oci`\)   DOCKER\_SCOUT\_CACHE\_DIR| String| Directory where the local SBOM cache is stored \(default: `$HOME/.docker/scout`\)   DOCKER\_SCOUT\_NO\_CACHE| Boolean| When set to `true`, disables the use of local SBOM cache   DOCKER\_SCOUT\_OFFLINE| Boolean| Use offline mode when indexing SBOM   DOCKER\_SCOUT\_REGISTRY\_TOKEN| String| Token for authenticating to a registry when pulling images   DOCKER\_SCOUT\_REGISTRY\_USER| String| Username for authenticating to a registry when pulling images   DOCKER\_SCOUT\_REGISTRY\_PASSWORD| String| Password or personal access token for authenticating to a registry when pulling images   DOCKER\_SCOUT\_HUB\_USER| String| Docker Hub username for authenticating to the Docker Scout backend   DOCKER\_SCOUT\_HUB\_PASSWORD| String| Docker Hub password or personal access token for authenticating to the Docker Scout backend   DOCKER\_SCOUT\_NEW\_VERSION\_WARN| Boolean| Warn about new versions of the Docker Scout CLI   DOCKER\_SCOUT\_EXPERIMENTAL\_WARN| Boolean| Warn about experimental features   DOCKER\_SCOUT\_EXPERIMENTAL\_POLICY\_OUTPUT| Boolean| Disable experimental output for policy evaluation      ## Offline mode

Under normal operation, Docker Scout cross-references external systems, such as npm, NuGet, or proxy.golang.org, to retrieve additional information about packages found in your image.

When `DOCKER_SCOUT_OFFLINE` is set to `true`, Docker Scout image analysis runs in offline mode. Offline mode means Docker Scout doesn't make outbound requests to external systems.

To use offline mode:               $ export DOCKER_SCOUT_OFFLINE=true