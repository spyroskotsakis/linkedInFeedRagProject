# Docker object labels | Docker Docs

**URL:** https://docs.docker.com/engine/manage-resources/labels
**Word Count:** 1552
**Links Count:** 667
**Scraped:** 2025-07-16 01:59:56
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Docker object labels

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Labels are a mechanism for applying metadata to Docker objects, including:

  * Images   * Containers   * Local daemons   * Volumes   * Networks   * Swarm nodes   * Swarm services

You can use labels to organize your images, record licensing information, annotate relationships between containers, volumes, and networks, or in any way that makes sense for your business or application.

## Label keys and values

A label is a key-value pair, stored as a string. You can specify multiple labels for an object, but each key must be unique within an object. If the same key is given multiple values, the most-recently-written value overwrites all previous values.

### Key format recommendations

A label key is the left-hand side of the key-value pair. Keys are alphanumeric strings which may contain periods \(`.`\), underscores \(`_`\), slashes \(`/`\), and hyphens \(`-`\). Most Docker users use images created by other organizations, and the following guidelines help to prevent inadvertent duplication of labels across objects, especially if you plan to use labels as a mechanism for automation.

  * Authors of third-party tools should prefix each label key with the reverse DNS notation of a domain they own, such as `com.example.some-label`.

  * Don't use a domain in your label key without the domain owner's permission.

  * The `com.docker.*`, `io.docker.*`, and `org.dockerproject.*` namespaces are reserved by Docker for internal use.

  * Label keys should begin and end with a lower-case letter and should only contain lower-case alphanumeric characters, the period character \(`.`\), and the hyphen character \(`-`\). Consecutive periods or hyphens aren't allowed.

  * The period character \(`.`\) separates namespace "fields". Label keys without namespaces are reserved for CLI use, allowing users of the CLI to interactively label Docker objects using shorter typing-friendly strings.

These guidelines aren't currently enforced and additional guidelines may apply to specific use cases.

### Value guidelines

Label values can contain any data type that can be represented as a string, including \(but not limited to\) JSON, XML, CSV, or YAML. The only requirement is that the value be serialized to a string first, using a mechanism specific to the type of structure. For instance, to serialize JSON into a string, you might use the `JSON.stringify()` JavaScript method.

Since Docker doesn't deserialize the value, you can't treat a JSON or XML document as a nested structure when querying or filtering by label value unless you build this functionality into third-party tooling.

## Manage labels on objects

Each type of object with support for labels has mechanisms for adding and managing them and using them as they relate to that type of object. These links provide a good place to start learning about how you can use labels in your Docker deployments.

Labels on images, containers, local daemons, volumes, and networks are static for the lifetime of the object. To change these labels you must recreate the object. Labels on Swarm nodes and services can be updated dynamically.

  * Images and containers

    * [Adding labels to images](https://docs.docker.com/reference/dockerfile/#label)     * [Overriding a container's labels at runtime](https://docs.docker.com/reference/cli/docker/container/run/#label)     * [Inspecting labels on images or containers](https://docs.docker.com/reference/cli/docker/inspect/)     * [Filtering images by label](https://docs.docker.com/reference/cli/docker/image/ls/#filter)     * [Filtering containers by label](https://docs.docker.com/reference/cli/docker/container/ls/#filter)   * Local Docker daemons

    * [Adding labels to a Docker daemon at runtime](https://docs.docker.com/reference/cli/dockerd/)     * [Inspecting a Docker daemon's labels](https://docs.docker.com/reference/cli/docker/system/info/)   * Volumes

    * [Adding labels to volumes](https://docs.docker.com/reference/cli/docker/volume/create/)     * [Inspecting a volume's labels](https://docs.docker.com/reference/cli/docker/volume/inspect/)     * [Filtering volumes by label](https://docs.docker.com/reference/cli/docker/volume/ls/#filter)   * Networks

    * [Adding labels to a network](https://docs.docker.com/reference/cli/docker/network/create/)     * [Inspecting a network's labels](https://docs.docker.com/reference/cli/docker/network/inspect/)     * [Filtering networks by label](https://docs.docker.com/reference/cli/docker/network/ls/#filter)   * Swarm nodes

    * [Adding or updating a Swarm node's labels](https://docs.docker.com/reference/cli/docker/node/update/#label-add)     * [Inspecting a Swarm node's labels](https://docs.docker.com/reference/cli/docker/node/inspect/)     * [Filtering Swarm nodes by label](https://docs.docker.com/reference/cli/docker/node/ls/#filter)   * Swarm services

    * [Adding labels when creating a Swarm service](https://docs.docker.com/reference/cli/docker/service/create/#label)     * [Updating a Swarm service's labels](https://docs.docker.com/reference/cli/docker/service/update/)     * [Inspecting a Swarm service's labels](https://docs.docker.com/reference/cli/docker/service/inspect/)     * [Filtering Swarm services by label](https://docs.docker.com/reference/cli/docker/service/ls/#filter)