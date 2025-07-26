# Code blocks | Docker Docs

**URL:** https://docs.docker.com/contribute/components/code-blocks/
**Word Count:** 314
**Links Count:** 92
**Scraped:** 2025-07-16 01:49:59
**Status:** completed

---

Back

[Contribute](https://docs.docker.com/contribute/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Code blocks

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Rouge provides lots of different code block "hints". If you leave off the hint, it tries to guess and sometimes gets it wrong. These are just a few hints that we use often.

## Variables

If your example contains a placeholder value that's subject to change, use the format `<[A-Z_]+>` for the placeholder value: `<MY_VARIABLE>`               export name=<MY_NAME>

This syntax is reserved for variable names, and will cause the variable to be rendered in a special color and font style.

## Highlight lines               incoming := map[string]interface{}{         "asdf": 1,         "qwer": []interface{}{},         "zxcv": []interface{}{             map[string]interface{}{},             true,             int(1e9),             "tyui",         },     }                   ```go {hl_lines=[7,8]}     incoming := map[string]interface{}{         "asdf": 1,         "qwer": []interface{}{},         "zxcv": []interface{}{             map[string]interface{}{},             true,             int(1e9),             "tyui",         },     }        ```

## Collapsible code blocks

Show more               # syntax=docker/dockerfile:1          ARG GO_VERSION="1.21"          FROM golang:${GO_VERSION}-alpine AS base     ENV CGO_ENABLED=0     ENV GOPRIVATE="github.com/foo/*"     RUN apk add --no-cache file git rsync openssh-client     RUN mkdir -p -m 0700 ~/.ssh && ssh-keyscan github.com >> ~/.ssh/known_hosts     WORKDIR /src          FROM base AS vendor     # this step configure git and checks the ssh key is loaded     RUN --mount=type=ssh <<EOT       set -e       echo "Setting Git SSH protocol"       git config --global url."git@github.com:".insteadOf "https://github.com/"       (         set +e         ssh -T git@github.com         if [ ! "$?" = "1" ]; then           echo "No GitHub SSH key loaded exiting..."           exit 1         fi       )     EOT     # this one download go modules     RUN --mount=type=bind,target=. \         --mount=type=cache,target=/go/pkg/mod \         --mount=type=ssh \         go mod download -x          FROM vendor AS build     RUN --mount=type=bind,target=. \         --mount=type=cache,target=/go/pkg/mod \         --mount=type=cache,target=/root/.cache \         go build ...

Hide

## Bash

Use the `bash` language code block when you want to show a Bash script:               #!/usr/bin/bash     echo "deb https://download.docker.com/linux/ubuntu noble stable" | sudo tee /etc/apt/sources.list.d/docker.list

If you want to show an interactive shell, use `console` instead. In cases where you use `console`, make sure to add a dollar character for the user sign:               $ echo "deb https://download.docker.com/linux/ubuntu noble stable" | sudo tee /etc/apt/sources.list.d/docker.list     

## Go               incoming := map[string]interface{}{         "asdf": 1,         "qwer": []interface{}{},         "zxcv": []interface{}{             map[string]interface{}{},             true,             int(1e9),             "tyui",         },     }

## PowerShell               Install-Module DockerMsftProvider -Force     Install-Package Docker -ProviderName DockerMsftProvider -Force     [System.Environment]::SetEnvironmentVariable("DOCKER_FIPS", "1", "Machine")     Expand-Archive docker-18.09.1.zip -DestinationPath $Env:ProgramFiles -Force

## Python               return html.format(name=os.getenv('NAME', "world"), hostname=socket.gethostname(), visits=visits)

## Ruby               docker_service 'default' do       action [:create, :start]     end

## JSON               "server": {       "http_addr": ":4443",       "tls_key_file": "./fixtures/notary-server.key",       "tls_cert_file": "./fixtures/notary-server.crt"     }

#### HTML               <!DOCTYPE html>     <html>     <head>     <title>Welcome to nginx!</title>     </head>     </html>

## Markdown               # Hello

If you want to include a triple-fenced code block inside your code block, you can wrap your block in a quadruple-fenced code block:               ````markdown     # Hello          ```go     log.Println("did something")     ```     ````

## ini               [supervisord]     nodaemon=true          [program:sshd]     command=/usr/sbin/sshd -D

## Dockerfile               # syntax=docker/dockerfile:1          FROM ubuntu          RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8          RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" > /etc/apt/sources.list.d/pgdg.list          RUN apt-get update && apt-get install -y python-software-properties software-properties-common postgresql-9.3 postgresql-client-9.3 postgresql-contrib-9.3          # Note: The official Debian and Ubuntu images automatically ``apt-get clean``     # after each ``apt-get``          USER postgres          RUN    /etc/init.d/postgresql start &&\         psql --command "CREATE USER docker WITH SUPERUSER PASSWORD 'docker';" &&\         createdb -O docker docker          RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.3/main/pg_hba.conf          RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf          EXPOSE 5432          VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]          CMD ["/usr/lib/postgresql/9.3/bin/postgres", "-D", "/var/lib/postgresql/9.3/main", "-c", "config_file=/etc/postgresql/9.3/main/postgresql.conf"]

## YAML               authorizedkeys:       image: dockercloud/authorizedkeys       deployment_strategy: every_node       autodestroy: always       environment:         - AUTHORIZED_KEYS=ssh-rsa AAAAB3Nsomelongsshkeystringhereu9UzQbVKy9o00NqXa5jkmZ9Yd0BJBjFmb3WwUR8sJWZVTPFL       volumes:         /root:/user:rw