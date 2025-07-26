# Install | Docker Docs

**URL:** https://docs.docker.com/scout/install/
**Word Count:** 1300
**Links Count:** 652
**Scraped:** 2025-07-16 01:46:25
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Install Docker Scout

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

The Docker Scout CLI plugin comes pre-installed with Docker Desktop.

If you run Docker Engine without Docker Desktop, Docker Scout doesn't come pre-installed, but you can install it as a standalone binary.

## Installation script

To install the latest version of the plugin, run the following commands:               $ curl -fsSL https://raw.githubusercontent.com/docker/scout-cli/main/install.sh -o install-scout.sh     $ sh install-scout.sh     

> Note >  > Always examine scripts downloaded from the internet before running them locally. Before installing, make yourself familiar with potential risks and limitations of the convenience script.

## Manual installation

Linux  macOS  Windows

  1. Download the latest release from the [releases page](https://github.com/docker/scout-cli/releases).

  2. Create a subdirectory under `$HOME/.docker` called `scout`.                    $ mkdir -p $HOME/.docker/scout          

  3. Extract the archive and move the `docker-scout` binary to the `$HOME/.docker/scout` directory.

  4. Make the binary executable: `chmod +x $HOME/.docker/scout/docker-scout`.

  5. Add the `scout` subdirectory to your `.docker/config.json` as a plugin directory:                    {            "cliPluginsExtraDirs": [              "/home/<USER>/.docker/scout"            ]          }

Substitute `<USER>` with your username on the system.

> Note >  > The path for `cliPluginsExtraDirs` must be an absolute path.

  1. Download the latest release from the [releases page](https://github.com/docker/scout-cli/releases).

  2. Create a subdirectory under `$HOME/.docker` called `scout`.                    $ mkdir -p $HOME/.docker/scout          

  3. Extract the archive and move the `docker-scout` binary to the `$HOME/.docker/scout` directory.

  4. Make the binary executable:                    $ chmod +x $HOME/.docker/scout/docker-scout          

  5. Authorize the binary to be executable on macOS:                    xattr -d com.apple.quarantine $HOME/.docker/scout/docker-scout          

  6. Add the `scout` subdirectory to your `.docker/config.json` as a plugin directory:                    {            "cliPluginsExtraDirs": [              "/Users/<USER>/.docker/scout"            ]          }

Substitute `<USER>` with your username on the system.

> Note >  > The path for `cliPluginsExtraDirs` must be an absolute path.

  1. Download the latest release from the [releases page](https://github.com/docker/scout-cli/releases).

  2. Create a subdirectory under `%USERPROFILE%/.docker` called `scout`.                    % mkdir %USERPROFILE%\.docker\scout          

  3. Extract the archive and move the `docker-scout.exe` binary to the `%USERPROFILE%\.docker\scout` directory.

  4. Add the `scout` subdirectory to your `.docker\config.json` as a plugin directory:                    {            "cliPluginsExtraDirs": [              "C:\Users\<USER>\.docker\scout"            ]          }

Substitute `<USER>` with your username on the system.

> Note >  > The path for `cliPluginsExtraDirs` must be an absolute path.

## Container image

The Docker Scout CLI plugin is also available as a [container image](https://hub.docker.com/r/docker/scout-cli). Use the `docker/scout-cli` to run `docker scout` commands without installing the CLI plugin on your host.               $ docker run -it \       -e DOCKER_SCOUT_HUB_USER=<your Docker Hub user name> \       -e DOCKER_SCOUT_HUB_PASSWORD=<your Docker Hub PAT>  \       docker/scout-cli <command>     

## GitHub Action

The Docker Scout CLI plugin is also available as a [GitHub action](https://github.com/docker/scout-action). You can use it in your GitHub workflows to automatically analyze images and evaluate policy compliance with each push.

Docker Scout also integrates with many more CI/CD tools, such as Jenkins, GitLab, and Azure DevOps. Learn more about the [integrations](https://docs.docker.com/scout/integrations/) available for Docker Scout.