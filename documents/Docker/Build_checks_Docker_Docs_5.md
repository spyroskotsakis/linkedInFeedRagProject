# Build checks | Docker Docs

**URL:** https://docs.docker.com/go/build-checks-experimental
**Word Count:** 2008
**Links Count:** 671
**Scraped:** 2025-07-16 02:05:41
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Checking your build configuration

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Availability: Beta 

Requires: Docker Buildx [0.15.0](https://docs.docker.com/compose/releases/release-notes/#0150) and later

Build checks are a feature introduced in Dockerfile 1.8. It lets you validate your build configuration and conduct a series of checks prior to executing your build. Think of it as an advanced form of linting for your Dockerfile and build options, or a dry-run mode for builds.

You can find the list of checks available, and a description of each, in the [Build checks reference](https://docs.docker.com/reference/build-checks/).

## How build checks work

Typically, when you run a build, Docker executes the build steps in your Dockerfile and build options as specified. With build checks, rather than executing the build steps, Docker checks the Dockerfile and options you provide and reports any issues it detects.

Build checks are useful for:

  * Validating your Dockerfile and build options before running a build.   * Ensuring that your Dockerfile and build options are up-to-date with the latest best practices.   * Identifying potential issues or anti-patterns in your Dockerfile and build options.

> Tip >  > Want a better editing experience for Dockerfiles in VS Code? Check out the [Docker VS Code Extension \(Beta\)](https://marketplace.visualstudio.com/items?itemName=docker.docker) for linting, code navigation, and vulnerability scanning.

## Build with checks

Build checks are supported in:

  * Buildx version 0.15.0 and later   * [docker/build-push-action](https://github.com/docker/build-push-action) version 6.6.0 and later   * [docker/bake-action](https://github.com/docker/bake-action) version 5.6.0 and later

Invoking a build runs the checks by default, and displays any violations in the build output. For example, the following command both builds the image and runs the checks:               $ docker build .     [+] Building 3.5s (11/11) FINISHED     ...          1 warning found (use --debug to expand):       - Lint Rule 'JSONArgsRecommended': JSON arguments recommended for CMD to prevent unintended behavior related to OS signals (line 7)     

In this example, the build ran successfully, but a [JSONArgsRecommended](https://docs.docker.com/reference/build-checks/json-args-recommended/) warning was reported, because `CMD` instructions should use JSON array syntax.

With the GitHub Actions, the checks display in the diff view of pull requests.               name: Build and push Docker images     on:       push:          jobs:       build:         runs-on: ubuntu-latest         steps:           - name: Build and push             uses: docker/build-push-action@v6.6.0

![GitHub Actions build check annotations](https://docs.docker.com/build/images/gha-check-annotations.png)

![GitHub Actions build check annotations](https://docs.docker.com/build/images/gha-check-annotations.png)

### More verbose output

Check warnings for a regular `docker build` display a concise message containing the rule name, the message, and the line number of where in the Dockerfile the issue originated. If you want to see more detailed information about the checks, you can use the `--debug` flag. For example:               $ docker --debug build .     [+] Building 3.5s (11/11) FINISHED     ...           1 warning found:      - JSONArgsRecommended: JSON arguments recommended for CMD to prevent unintended behavior related to OS signals (line 4)     JSON arguments recommended for ENTRYPOINT/CMD to prevent unintended behavior related to OS signals     More info: https://docs.docker.com/go/dockerfile/rule/json-args-recommended/     Dockerfile:4     --------------------        2 |        3 |     FROM alpine        4 | >>> CMD echo "Hello, world!"        5 |     --------------------     

With the `--debug` flag, the output includes a link to the documentation for the check, and a snippet of the Dockerfile where the issue was found.

## Check a build without building

To run build checks without actually building, you can use the `docker build` command as you typically would, but with the addition of the `--check` flag. Here's an example:               $ docker build --check .     

Instead of executing the build steps, this command only runs the checks and reports any issues it finds. If there are any issues, they will be reported in the output. For example:

Output with --check               [+] Building 1.5s (5/5) FINISHED     => [internal] connecting to local controller     => [internal] load build definition from Dockerfile     => => transferring dockerfile: 253B     => [internal] load metadata for docker.io/library/node:22     => [auth] library/node:pull token for registry-1.docker.io     => [internal] load .dockerignore     => => transferring context: 50B     JSONArgsRecommended - https://docs.docker.com/go/dockerfile/rule/json-args-recommended/     JSON arguments recommended for ENTRYPOINT/CMD to prevent unintended behavior related to OS signals     Dockerfile:7     --------------------     5 |     6 |     COPY index.js .     7 | >>> CMD node index.js     8 |     --------------------

This output with `--check` shows the verbose message for the check.

Unlike a regular build, if any violations are reported when using the `--check` flag, the command exits with a non-zero status code.

## Fail build on check violations

Check violations for builds are reported as warnings, with exit code 0, by default. You can configure Docker to fail the build when violations are reported, using a `check=error=true` directive in your Dockerfile. This will cause the build to error out when after the build checks are run, before the actual build gets executed.

Dockerfile               1     2     3     4     5     

|                # syntax=docker/dockerfile:1     # check=error=true          FROM alpine     CMD echo "Hello, world!"      ---|---      Without the `# check=error=true` directive, this build would complete with an exit code of 0. However, with the directive, build check violation results in non-zero exit code:               $ docker build .     [+] Building 1.5s (5/5) FINISHED     ...           1 warning found (use --debug to expand):      - JSONArgsRecommended: JSON arguments recommended for CMD to prevent unintended behavior related to OS signals (line 5)     Dockerfile:1     --------------------        1 | >>> # syntax=docker/dockerfile:1        2 |     # check=error=true        3 |     --------------------     ERROR: lint violation found for rules: JSONArgsRecommended     $ echo $?     1     

You can also set the error directive on the CLI by passing the `BUILDKIT_DOCKERFILE_CHECK` build argument:               $ docker build --check --build-arg "BUILDKIT_DOCKERFILE_CHECK=error=true" .     

## Skip checks

By default, all checks are run when you build an image. If you want to skip specific checks, you can use the `check=skip` directive in your Dockerfile. The `skip` parameter takes a CSV string of the check IDs you want to skip. For example:

Dockerfile               # syntax=docker/dockerfile:1     # check=skip=JSONArgsRecommended,StageNameCasing          FROM alpine AS BASE_STAGE     CMD echo "Hello, world!"

Building this Dockerfile results in no check violations.

You can also skip checks by passing the `BUILDKIT_DOCKERFILE_CHECK` build argument with a CSV string of check IDs you want to skip. For example:               $ docker build --check --build-arg "BUILDKIT_DOCKERFILE_CHECK=skip=JSONArgsRecommended,StageNameCasing" .     

To skip all checks, use the `skip=all` parameter:

Dockerfile               # syntax=docker/dockerfile:1     # check=skip=all

## Combine error and skip parameters for check directives

To both skip specific checks and error on check violations, pass both the `skip` and `error` parameters separated by a semi-colon \(`;`\) to the `check` directive in your Dockerfile or in a build argument. For example:

Dockerfile               # syntax=docker/dockerfile:1     # check=skip=JSONArgsRecommended,StageNameCasing;error=true

Build argument               $ docker build --check --build-arg "BUILDKIT_DOCKERFILE_CHECK=skip=JSONArgsRecommended,StageNameCasing;error=true" .     

## Experimental checks

Before checks are promoted to stable, they may be available as experimental checks. Experimental checks are disabled by default. To see the list of experimental checks available, refer to the [Build checks reference](https://docs.docker.com/reference/build-checks/).

To enable all experimental checks, set the `BUILDKIT_DOCKERFILE_CHECK` build argument to `experimental=all`:               $ docker build --check --build-arg "BUILDKIT_DOCKERFILE_CHECK=experimental=all" .     

You can also enable experimental checks in your Dockerfile using the `check` directive:

Dockerfile               # syntax=docker/dockerfile:1     # check=experimental=all

To selectively enable experimental checks, you can pass a CSV string of the check IDs you want to enable, either to the `check` directive in your Dockerfile or as a build argument. For example:

Dockerfile               # syntax=docker/dockerfile:1     # check=experimental=JSONArgsRecommended,StageNameCasing

Note that the `experimental` directive takes precedence over the `skip` directive, meaning that experimental checks will run regardless of the `skip` directive you have set. For example, if you set `skip=all` and enable experimental checks, the experimental checks will still run:

Dockerfile               # syntax=docker/dockerfile:1     # check=skip=all;experimental=all

## Further reading

For more information about using build checks, see:

  * [Build checks reference](https://docs.docker.com/reference/build-checks/)   * [Validating build configuration with GitHub Actions](https://docs.docker.com/build/ci/github-actions/checks/)