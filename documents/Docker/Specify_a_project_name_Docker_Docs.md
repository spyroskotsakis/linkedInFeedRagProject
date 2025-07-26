# Specify a project name | Docker Docs

**URL:** https://docs.docker.com/compose/how-tos/project-name
**Word Count:** 1306
**Links Count:** 651
**Scraped:** 2025-07-16 01:59:28
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Specify a project name

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

By default, Compose assigns the project name based on the name of the directory that contains the Compose file. You can override this with several methods.

This page offers examples of scenarios where custom project names can be helpful, outlines the various methods to set a project name, and provides the order of precedence for each approach.

> Note >  > The default project directory is the base directory of the Compose file. A custom value can also be set for it using the [`--project-directory` command line option](https://docs.docker.com/reference/cli/docker/compose/#options).

## Example use cases

Compose uses a project name to isolate environments from each other. There are multiple contexts where a project name is useful:

  * On a development host: Create multiple copies of a single environment, useful for running stable copies for each feature branch of a project.   * On a CI server: Prevent interference between builds by setting the project name to a unique build number.   * On a shared or development host: Avoid interference between different projects that might share the same service names.

## Set a project name

Project names must contain only lowercase letters, decimal digits, dashes, and underscores, and must begin with a lowercase letter or decimal digit. If the base name of the project directory or current directory violates this constraint, alternative mechanisms are available.

The precedence order for each method, from highest to lowest, is as follows:

  1. The `-p` command line flag.   2. The [COMPOSE\_PROJECT\_NAME environment variable](https://docs.docker.com/compose/how-tos/environment-variables/envvars/).   3. The [top-level `name:` attribute](https://docs.docker.com/reference/compose-file/version-and-name/) in your Compose file. Or the last `name:` if you [specify multiple Compose files](https://docs.docker.com/compose/how-tos/multiple-compose-files/merge/) in the command line with the `-f` flag.   4. The base name of the project directory containing your Compose file. Or the base name of the first Compose file if you [specify multiple Compose files](https://docs.docker.com/compose/how-tos/multiple-compose-files/merge/) in the command line with the `-f` flag.   5. The base name of the current directory if no Compose file is specified.

## What's next?

  * Read up on [working with multiple Compose files](https://docs.docker.com/compose/how-tos/multiple-compose-files/).   * Explore some [sample apps](https://docs.docker.com/compose/support-and-feedback/samples-for-compose/).