# Secrets in Compose | Docker Docs

**URL:** http://docs.docker.com/compose/how-tos/use-secrets
**Word Count:** 1325
**Links Count:** 661
**Scraped:** 2025-07-16 02:08:05
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](http://docs.docker.com/get-started/)   * [Guides](http://docs.docker.com/guides/)   * [Reference](http://docs.docker.com/reference/)

* * *

# Manage secrets securely in Docker Compose

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

A secret is any piece of data, such as a password, certificate, or API key, that shouldnât be transmitted over a network or stored unencrypted in a Dockerfile or in your applicationâs source code.

Docker Compose provides a way for you to use secrets without having to use environment variables to store information. If youâre injecting passwords and API keys as environment variables, you risk unintentional information exposure. Services can only access secrets when explicitly granted by a `secrets` attribute within the `services` top-level element.

Environment variables are often available to all processes, and it can be difficult to track access. They can also be printed in logs when debugging errors without your knowledge. Using secrets mitigates these risks.

## Use secrets

Secrets are mounted as a file in `/run/secrets/<secret_name>` inside the container.

Getting a secret into a container is a two-step process. First, define the secret using the [top-level secrets element in your Compose file](https://docs.docker.com/reference/compose-file/secrets/). Next, update your service definitions to reference the secrets they require with the [secrets attribute](https://docs.docker.com/reference/compose-file/services/#secrets). Compose grants access to secrets on a per-service basis.

Unlike the other methods, this permits granular access control within a service container via standard filesystem permissions.

## Examples

### Single-service secret injection

In the following example, the frontend service is given access to the `my_secret` secret. In the container, `/run/secrets/my_secret` is set to the contents of the file `./my_secret.txt`.               services:       myapp:         image: myapp:latest         secrets:           - my_secret     secrets:       my_secret:         file: ./my_secret.txt

### Multi-service secret sharing and password management               services:        db:          image: mysql:latest          volumes:            - db_data:/var/lib/mysql          environment:            MYSQL_ROOT_PASSWORD_FILE: /run/secrets/db_root_password            MYSQL_DATABASE: wordpress            MYSQL_USER: wordpress            MYSQL_PASSWORD_FILE: /run/secrets/db_password          secrets:            - db_root_password            - db_password             wordpress:          depends_on:            - db          image: wordpress:latest          ports:            - "8000:80"          environment:            WORDPRESS_DB_HOST: db:3306            WORDPRESS_DB_USER: wordpress            WORDPRESS_DB_PASSWORD_FILE: /run/secrets/db_password          secrets:            - db_password               secrets:        db_password:          file: db_password.txt        db_root_password:          file: db_root_password.txt          volumes:         db_data:

In the advanced example above:

  * The `secrets` attribute under each service defines the secrets you want to inject into the specific container.   * The top-level `secrets` section defines the variables `db_password` and `db_root_password` and provides the `file` that populates their values.   * The deployment of each container means Docker creates a temporary filesystem mount under `/run/secrets/<secret_name>` with their specific values.

> Note >  > The `_FILE` environment variables demonstrated here are a convention used by some images, including Docker Official Images like [mysql](https://hub.docker.com/_/mysql) and [postgres](https://hub.docker.com/_/postgres).

### Build secrets

In the following example, the `npm_token` secret is made available at build time. Its value is taken from the `NPM_TOKEN` environment variable.               services:       myapp:         build:           secrets:             - npm_token           context: .          secrets:       npm_token:         environment: NPM_TOKEN

## Resources

  * [Secrets top-level element](https://docs.docker.com/reference/compose-file/secrets/)   * [Secrets attribute for services top-level element](https://docs.docker.com/reference/compose-file/services/#secrets)   * [Build secrets](https://docs.docker.com/build/building/secrets/)