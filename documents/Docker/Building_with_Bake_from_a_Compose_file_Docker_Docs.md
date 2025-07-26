# Building with Bake from a Compose file | Docker Docs

**URL:** https://docs.docker.com/build/bake/compose-file
**Word Count:** 1157
**Links Count:** 645
**Scraped:** 2025-07-16 02:02:47
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Building with Bake from a Compose file

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Bake supports the [Compose file format](https://docs.docker.com/reference/compose-file/) to parse a Compose file and translate each service to a [target](https://docs.docker.com/build/bake/reference/#target).               # compose.yaml     services:       webapp-dev:         build: &build-dev           dockerfile: Dockerfile.webapp           tags:             - docker.io/username/webapp:latest           cache_from:             - docker.io/username/webapp:cache           cache_to:             - docker.io/username/webapp:cache            webapp-release:         build:           <<: *build-dev           x-bake:             platforms:               - linux/amd64               - linux/arm64            db:         image: docker.io/username/db         build:           dockerfile: Dockerfile.db               $ docker buildx bake --print                    {       "group": {         "default": {           "targets": ["db", "webapp-dev", "webapp-release"]         }       },       "target": {         "db": {           "context": ".",           "dockerfile": "Dockerfile.db",           "tags": ["docker.io/username/db"]         },         "webapp-dev": {           "context": ".",           "dockerfile": "Dockerfile.webapp",           "tags": ["docker.io/username/webapp:latest"],           "cache-from": [             {               "ref": "docker.io/username/webapp:cache",               "type": "registry"             }           ],           "cache-to": [             {               "ref": "docker.io/username/webapp:cache",               "type": "registry"             }           ]         },         "webapp-release": {           "context": ".",           "dockerfile": "Dockerfile.webapp",           "tags": ["docker.io/username/webapp:latest"],           "cache-from": [             {               "ref": "docker.io/username/webapp:cache",               "type": "registry"             }           ],           "cache-to": [             {               "ref": "docker.io/username/webapp:cache",               "type": "registry"             }           ],           "platforms": ["linux/amd64", "linux/arm64"]         }       }     }

The compose format has some limitations compared to the HCL format:

  * Specifying variables or global scope attributes is not yet supported   * `inherits` service field is not supported, but you can use [YAML anchors](https://docs.docker.com/reference/compose-file/fragments/) to reference other services, as demonstrated in the previous example with `&build-dev`.

## `.env` file

You can declare default environment variables in an environment file named `.env`. This file will be loaded from the current working directory, where the command is executed and applied to compose definitions passed with `-f`.               # compose.yaml     services:       webapp:         image: docker.io/username/webapp:${TAG:-v1.0.0}         build:           dockerfile: Dockerfile               # .env     TAG=v1.1.0               $ docker buildx bake --print                    {       "group": {         "default": {           "targets": ["webapp"]         }       },       "target": {         "webapp": {           "context": ".",           "dockerfile": "Dockerfile",           "tags": ["docker.io/username/webapp:v1.1.0"]         }       }     }

> Note >  > System environment variables take precedence over environment variables in `.env` file.

## Extension field with `x-bake`

Where some fields are not available in the compose specification, you can use the [special extension](https://docs.docker.com/reference/compose-file/extension/) field `x-bake` in your compose file to evaluate extra fields:               # compose.yaml     services:       addon:         image: ct-addon:bar         build:           context: .           dockerfile: ./Dockerfile           args:             CT_ECR: foo             CT_TAG: bar           x-bake:             tags:               - ct-addon:foo               - ct-addon:alp             platforms:               - linux/amd64               - linux/arm64             cache-from:               - user/app:cache               - type=local,src=path/to/cache             cache-to:               - type=local,dest=path/to/cache             pull: true            aws:         image: ct-fake-aws:bar         build:           dockerfile: ./aws.Dockerfile           args:             CT_ECR: foo             CT_TAG: bar           x-bake:             secret:               - id=mysecret,src=./secret               - id=mysecret2,src=./secret2             platforms: linux/arm64             output: type=docker             no-cache: true               $ docker buildx bake --print                    {       "group": {         "default": {           "targets": ["addon", "aws"]         }       },       "target": {         "addon": {           "context": ".",           "dockerfile": "./Dockerfile",           "args": {             "CT_ECR": "foo",             "CT_TAG": "bar"           },           "tags": ["ct-addon:foo", "ct-addon:alp"],           "cache-from": [             {               "ref": "user/app:cache",               "type": "registry"             },             {               "src": "path/to/cache",               "type": "local"             }           ],           "cache-to": [             {               "dest": "path/to/cache",               "type": "local"             }           ],           "platforms": ["linux/amd64", "linux/arm64"],           "pull": true         },         "aws": {           "context": ".",           "dockerfile": "./aws.Dockerfile",           "args": {             "CT_ECR": "foo",             "CT_TAG": "bar"           },           "tags": ["ct-fake-aws:bar"],           "secret": [             {               "id": "mysecret",               "src": "./secret"             },             {               "id": "mysecret2",               "src": "./secret2"             }           ],           "platforms": ["linux/arm64"],           "output": [             {               "type": "docker"             }           ],           "no-cache": true         }       }     }

Complete list of valid fields for `x-bake`:

  * `cache-from`   * `cache-to`   * `contexts`   * `no-cache`   * `no-cache-filter`   * `output`   * `platforms`   * `pull`   * `secret`   * `ssh`   * `tags`