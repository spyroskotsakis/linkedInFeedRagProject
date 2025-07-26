# Use service profiles | Docker Docs

**URL:** https://docs.docker.com/compose/how-tos/profiles
**Word Count:** 1541
**Links Count:** 659
**Scraped:** 2025-07-16 02:01:22
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Using profiles with Compose

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Profiles help you adjust your Compose application for different environments or use cases by selectively activating services. Services can be assigned to one or more profiles; unassigned services start/stop by default, while assigned ones only start/stop when their profile is active. This setup means specific services, like those for debugging or development, to be included in a single `compose.yml` file and activated only as needed.

## Assigning profiles to services

Services are associated with profiles through the [`profiles` attribute](https://docs.docker.com/reference/compose-file/services/#profiles) which takes an array of profile names:               services:       frontend:         image: frontend         profiles: [frontend]            phpmyadmin:         image: phpmyadmin         depends_on: [db]         profiles: [debug]            backend:         image: backend            db:         image: mysql

Here the services `frontend` and `phpmyadmin` are assigned to the profiles `frontend` and `debug` respectively and as such are only started when their respective profiles are enabled.

Services without a `profiles` attribute are always enabled. In this case running `docker compose up` would only start `backend` and `db`.

Valid profiles names follow the regex format of `[a-zA-Z0-9][a-zA-Z0-9_.-]+`.

> Tip >  > The core services of your application shouldn't be assigned `profiles` so they are always enabled and automatically started.

## Start specific profiles

To start a specific profile supply the `--profile` [command-line option](https://docs.docker.com/reference/cli/docker/compose/) or use the [`COMPOSE_PROFILES` environment variable](https://docs.docker.com/compose/how-tos/environment-variables/envvars/#compose_profiles):               $ docker compose --profile debug up                    $ COMPOSE_PROFILES=debug docker compose up     

Both commands start the services with the `debug` profile enabled. In the previous `compose.yaml` file, this starts the services `db`, `backend` and `phpmyadmin`.

### Start multiple profiles

You can also enable multiple profiles, e.g. with `docker compose --profile frontend --profile debug up` the profiles `frontend` and `debug` will be enabled.

Multiple profiles can be specified by passing multiple `--profile` flags or a comma-separated list for the `COMPOSE_PROFILES` environment variable:               $ docker compose --profile frontend --profile debug up                    $ COMPOSE_PROFILES=frontend,debug docker compose up     

If you want to enable all profiles at the same time, you can run `docker compose --profile "*"`.

## Auto-starting profiles and dependency resolution

When you explicitly target a service on the command line that has one or more profiles assigned, you do not need to enable the profile manually as Compose runs that service regardless of whether its profile is activated. This is useful for running one-off services or debugging tools.

Only the targeted service \(and any of its declared dependencies via `depends_on`\) is started. Other services that share the same profile will not be started unless:

  * They are also explicitly targeted, or   * The profile is explicitly enabled using `--profile` or `COMPOSE_PROFILES`.

When a service with assigned `profiles` is explicitly targeted on the command line its profiles are started automatically so you don't need to start them manually. This can be used for one-off services and debugging tools. As an example consider the following configuration:               services:       backend:         image: backend            db:         image: mysql            db-migrations:         image: backend         command: myapp migrate         depends_on:           - db         profiles:           - tools               # Only start backend and db (no profiles involved)     $ docker compose up -d          # Run the db-migrations service without manually enabling the 'tools' profile     $ docker compose run db-migrations

In this example, `db-migrations` runs even though it is assigned to the tools profile, because it was explicitly targeted. The `db` service is also started automatically because it is listed in `depends_on`.

If the targeted service has dependencies that are also gated behind a profile, you must ensure those dependencies are either:

  * In the same profile   * Started separately   * Not assigned to any profile so are always enabled

## Stop application and services with specific profiles

As with starting specific profiles, you can use the `--profile` [command-line option](https://docs.docker.com/reference/cli/docker/compose/#use--p-to-specify-a-project-name) or use the [`COMPOSE_PROFILES` environment variable](https://docs.docker.com/compose/how-tos/environment-variables/envvars/#compose_profiles):               $ docker compose --profile debug down                    $ COMPOSE_PROFILES=debug docker compose down     

Both commands stop and remove services with the `debug` profile and services without a profile. In the following `compose.yaml` file, this stops the services `db`, `backend` and `phpmyadmin`.               services:       frontend:         image: frontend         profiles: [frontend]            phpmyadmin:         image: phpmyadmin         depends_on: [db]         profiles: [debug]            backend:         image: backend            db:         image: mysql

if you only want to stop the `phpmyadmin` service, you can run               $ docker compose down phpmyadmin     

or               $ docker compose stop phpmyadmin     

> Note >  > Running `docker compose down` only stops `backend` and `db`.

## Reference information

[`profiles`](https://docs.docker.com/reference/compose-file/services/#profiles)