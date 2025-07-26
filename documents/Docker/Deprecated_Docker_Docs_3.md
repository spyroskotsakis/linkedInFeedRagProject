# Deprecated | Docker Docs

**URL:** https://docs.docker.com/reference/api/hub/deprecated/
**Word Count:** 929
**Links Count:** 503
**Scraped:** 2025-07-16 01:46:03
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# Deprecated Docker Hub API endpoints

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

This page provides an overview of endpoints that are deprecated in Docker Hub API.

## Endpoint deprecation policy

As changes are made to Docker there may be times when existing endpoints need to be removed or replaced with newer endpoints. Before an existing endpoint is removed it is labeled as "deprecated" within the documentation. After some time it may be removed.

## Deprecated endpoints

The following table provides an overview of the current status of deprecated endpoints:

**Deprecated** : the endpoint is marked "deprecated" and should no longer be used.

The endpoint may be removed, disabled, or change behavior in a future release.

**Removed** : the endpoint was removed, disabled, or hidden.

* * *

Status| Feature| Date   ---|---|---   Deprecated| Deprecate /v2/repositories/\{namespace\}| 2025-06-27   | Create deprecation log table| 2025-06-27   Removed| Docker Hub API v1 deprecation| 2022-08-23      * * *

### Deprecate legacy ListNamespaceRepositories

Deprecate undocumented endpoint `GET /v2/repositories/{namespace}` replaced by [List repositories](https://docs.docker.com/reference/api/hub/latest/#tag/repositories/operation/listNamespaceRepositories).

* * *

### Create deprecation log table

Reformat page

* * *

### Docker Hub API v1 deprecation

Docker Hub API v1 has been deprecated. Use Docker Hub API v2 instead.

The following API routes within the v1 path will no longer work and will return a 410 status code:

  * `/v1/repositories/{name}/images`   * `/v1/repositories/{name}/tags`   * `/v1/repositories/{name}/tags/{tag_name}`   * `/v1/repositories/{namespace}/{name}/images`   * `/v1/repositories/{namespace}/{name}/tags`   * `/v1/repositories/{namespace}/{name}/tags/{tag_name}`

If you want to continue using the Docker Hub API in your current applications, update your clients to use v2 endpoints.

**OLD**| **NEW**   ---|---   [/v1/repositories/\{name\}/tags](https://github.com/moby/moby/blob/v1.8.3/docs/reference/api/registry_api.md#list-repository-tags)| [/v2/namespaces/\{namespace\}/repositories/\{repository\}/tags](https://docs.docker.com/reference/api/hub/latest/#tag/repositories/operation/ListRepositoryTags)   [/v1/repositories/\{namespace\}/\{name\}/tags](https://github.com/moby/moby/blob/v1.8.3/docs/reference/api/registry_api.md#list-repository-tags)| [/v2/namespaces/\{namespace\}/repositories/\{repository\}/tags](https://docs.docker.com/reference/api/hub/latest.md/#tag/repositories/operation/ListRepositoryTags)   [/v1/repositories/\{namespace\}/\{name\}/tags](https://github.com/moby/moby/blob/v1.8.3/docs/reference/api/registry_api.md#get-image-id-for-a-particular-tag)| [/v2/namespaces/\{namespace\}/repositories/\{repository\}/tags/\{tag\}](https://docs.docker.com/reference/api/hub/latest/#tag/repositories/operation/GetRepositoryTag)   [/v1/repositories/\{namespace\}/\{name\}/tags/\{tag\_name\}](https://github.com/moby/moby/blob/v1.8.3/docs/reference/api/registry_api.md#get-image-id-for-a-particular-tag)| [/v2/namespaces/\{namespace\}/repositories/\{repository\}/tags/\{tag\}](https://docs.docker.com/reference/api/hub/latest/#tag/repositories/operation/GetRepositoryTag)      * * *