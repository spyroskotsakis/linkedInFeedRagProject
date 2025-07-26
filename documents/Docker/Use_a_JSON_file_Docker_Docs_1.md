# Use a JSON file | Docker Docs

**URL:** https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/configure-json-file/
**Word Count:** 2291
**Links Count:** 709
**Scraped:** 2025-07-16 01:46:47
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Configure Settings Management with a JSON file

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Subscription: Business

For: Administrators

This page explains how to use an `admin-settings.json` file to configure and enforce Docker Desktop settings. Use this method to standardize Docker Desktop environments in your organization.

## Prerequisites

  * [Enforce sign-in](https://docs.docker.com/enterprise/security/enforce-sign-in/) to ensure all users authenticate with your organization.   * A Docker Business subscription is required.

Docker Desktop only applies settings from the `admin-settings.json` file if both authentication and Docker Business license checks succeed.

> Important >  > If a user isn't signed in or isn't part of a Docker Business organization, the settings file is ignored.

## Limitation

  * The `admin-settings.json` file doesn't work in air-gapped or offline environments.   * The file is not compatible with environments that restrict authentication with Docker Hub.

## Step one: Create the settings file

You can:

  * Use the `--admin-settings` installer flag to auto-generate the file. See:     * [macOS](https://docs.docker.com/desktop/setup/install/mac-install/#install-from-the-command-line) install guide     * [Windows](https://docs.docker.com/desktop/setup/install/windows-install/#install-from-the-command-line) install guide   * Or create it manually and place it in the following locations:     * Mac: `/Library/Application\ Support/com.docker.docker/admin-settings.json`     * Windows: `C:\ProgramData\DockerDesktop\admin-settings.json`     * Linux: `/usr/share/docker-desktop/admin-settings.json`

> Important >  > Place the file in a protected directory to prevent modification. Use MDM tools like [Jamf](https://www.jamf.com/lp/en-gb/apple-mobile-device-management-mdm-jamf-shared/?attr=google_ads-brand-search-shared&gclid=CjwKCAjw1ICZBhAzEiwAFfvFhEXjayUAi8FHHv1JJitFPb47C_q_RCySTmF86twF1qJc_6GST-YDmhoCuJsQAvD_BwE) to distribute it at scale.

## Step two: Define settings

> Tip >  > For a complete list of available settings, their supported platforms, and which configuration methods they work with, see the [Settings reference](https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/settings-reference/).

The `admin-settings.json` file uses structured keys to define what can be configured and whether the values are enforced.

Each setting supports the `locked` field. When `locked` is set to `true`, users can't change that value in Docker Desktop, the CLI, or config files. When `locked` is set to `false`, the value acts like a default suggestion and users can still update it.

Settings where `locked` is set to `false` are ignored on existing installs if a user has already customized that value in `settings-store.json`, `settings.json`, or `daemon.json`.

> Note >  > Some settings are platform-specific or require a minimum Docker Desktop version. See the [Settings reference](https://docs.docker.com/enterprise/security/hardened-desktop/settings-management/settings-reference/) for details.

### Example settings file

The following file is an example `admin-settings.json` file. For a full list of configurable settings for the `admin-settings.json` file, see `admin-settings.json` configurations.

Show more               {       "configurationFileVersion": 2,       "exposeDockerAPIOnTCP2375": {         "locked": true,         "value": false       },       "proxy": {         "locked": true,         "mode": "system",         "http": "",         "https": "",         "exclude": [],         "windowsDockerdPort": 65000,         "enableKerberosNtlm": false       },       "containersProxy": {         "locked": true,         "mode": "manual",         "http": "",         "https": "",         "exclude": [],         "pac":"",         "transparentPorts": ""       },       "enhancedContainerIsolation": {         "locked": true,         "value": true,         "dockerSocketMount": {           "imageList": {             "images": [               "docker.io/localstack/localstack:*",               "docker.io/testcontainers/ryuk:*"             ]           },           "commandList": {             "type": "deny",             "commands": ["push"]           }         }       },       "linuxVM": {         "wslEngineEnabled": {           "locked": false,           "value": false         },         "dockerDaemonOptions": {           "locked": false,           "value":"{\"debug\": false}"         },         "vpnkitCIDR": {           "locked": false,           "value":"192.168.65.0/24"         }       },       "kubernetes": {          "locked": false,          "enabled": false,          "showSystemContainers": false,          "imagesRepository": ""       },       "windowsContainers": {         "dockerDaemonOptions": {           "locked": false,           "value":"{\"debug\": false}"         }       },       "disableUpdate": {         "locked": false,         "value": false       },       "analyticsEnabled": {         "locked": false,         "value": true       },       "extensionsEnabled": {         "locked": true,         "value": false       },       "scout": {         "locked": false,         "sbomIndexing": true,         "useBackgroundIndexing": true       },       "allowBetaFeatures": {         "locked": false,         "value": false       },       "blockDockerLoad": {         "locked": false,         "value": true       },       "filesharingAllowedDirectories": [         {           "path": "$HOME",           "sharedByDefault": true         },         {           "path":"$TMP",           "sharedByDefault": false         }       ],       "useVirtualizationFrameworkVirtioFS": {         "locked": true,         "value": true       },       "useVirtualizationFrameworkRosetta": {         "locked": true,         "value": true       },       "useGrpcfuse": {         "locked": true,         "value": true       },       "displayedOnboarding": {         "locked": true,         "value": true       },       "desktopTerminalEnabled": {         "locked": false,         "value": false       }     }

Hide

## Step three: Restart and apply settings

Settings apply after Docker Desktop is restarted and the user is signed in.

  * New installs: Launch Docker Desktop and sign in.   * Existing installs: Quit Docker Desktop fully and relaunch it.

> Important >  > Restarting Docker Desktop from the menu isn't enough. It must be fully quit and reopened.

## `admin-settings.json` configurations

### General

Parameter| OS| Description| Version   ---|---|---|---   `configurationFileVersion`| | Specifies the version of the configuration file format.|    `analyticsEnabled`| | If `value` is set to false, Docker Desktop doesn't send usage statistics to Docker.|    `disableUpdate`| | If `value` is set to true, checking for and notifications about Docker Desktop updates is disabled.|    `extensionsEnabled`| | If `value` is set to false, Docker extensions are disabled.|    `blockDockerLoad`| | If `value` is set to `true`, users are no longer able to run [`docker load`](https://docs.docker.com/reference/cli/docker/image/load/) and receive an error if they try to.|    `displayedOnboarding`| | If `value` is set to `true`, the onboarding survey will not be displayed to new users. Setting `value` to `false` has no effect.| Docker Desktop version 4.30 and later   `desktopTerminalEnabled`| | If `value` is set to `false`, developers cannot use the Docker terminal to interact with the host machine and execute commands directly from Docker Desktop.|    `exposeDockerAPIOnTCP2375`| Windows only| Exposes the Docker API on a specified port. If `value` is set to true, the Docker API is exposed on port 2375. Note: This is unauthenticated and should only be enabled if protected by suitable firewall rules.|       ### File sharing and emulation

Parameter| OS| Description| Version   ---|---|---|---   `filesharingAllowedDirectories`| | Specify which paths your developers can add file shares to. Also accepts `$HOME`, `$TMP`, or `$TEMP` as `path` variables. When a path is added, its subdirectories are allowed. If `sharedByDefault` is set to `true`, that path will be added upon factory reset or when Docker Desktop first starts.|    `useVirtualizationFrameworkVirtioFS`| macOS only| If `value` is set to `true`, VirtioFS is set as the file sharing mechanism. Note: If both `useVirtualizationFrameworkVirtioFS` and `useGrpcfuse` have `value` set to `true`, VirtioFS takes precedence. Likewise, if both `useVirtualizationFrameworkVirtioFS` and `useGrpcfuse` have `value` set to `false`, osxfs is set as the file sharing mechanism.|    `useGrpcfuse`| macOS only| If `value` is set to `true`, gRPC Fuse is set as the file sharing mechanism.|    `useVirtualizationFrameworkRosetta`| macOS only| If `value` is set to `true`, Docker Desktop turns on Rosetta to accelerate x86\_64/amd64 binary emulation on Apple Silicon. Note: This also automatically enables `Use Virtualization framework`.| Docker Desktop version 4.29 and later.      ### Docker Scout

Parameter| OS| Description| Version   ---|---|---|---   `scout`| | Setting `useBackgroundIndexing` to `false` disables automatic indexing of images loaded to the image store. Setting `sbomIndexing` to `false` prevents users from being able to index image by inspecting them in Docker Desktop or using `docker scout` CLI commands.|       ### Proxy

Parameter| OS| Description| Version   ---|---|---|---   `proxy`| | If `mode` is set to `system` instead of `manual`, Docker Desktop gets the proxy values from the system and ignores and values set for `http`, `https` and `exclude`. Change `mode` to `manual` to manually configure proxy servers. If the proxy port is custom, specify it in the `http` or `https` property, for example `"https": "http://myotherproxy.com:4321"`. The `exclude` property specifies a comma-separated list of hosts and domains to bypass the proxy.|    Â Â Â Â `windowsDockerdPort`| Windows only| Exposes Docker Desktop's internal proxy locally on this port for the Windows Docker daemon to connect to. If it is set to 0, a random free port is chosen. If the value is greater than 0, use that exact value for the port. The default value is -1 which disables the option.|    Â Â Â Â `enableKerberosNtlm`| | When set to `true`, Kerberos and NTLM authentication is enabled. Default is `false`. For more information, see the settings documentation.| Docker Desktop version 4.32 and later.      ### Container proxy

Parameter| OS| Description| Version   ---|---|---|---   `containersProxy`| | Creates air-gapped containers. For more information see [Air-Gapped Containers](https://docs.docker.com/enterprise/security/hardened-desktop/air-gapped-containers/).| Docker Desktop version 4.29 and later.      ### Linux VM

Parameter| OS| Description| Version   ---|---|---|---   `linuxVM`| | Parameters and settings related to Linux VM options - grouped together here for convenience.|    Â Â Â Â `wslEngineEnabled`| Windows only| If `value` is set to true, Docker Desktop uses the WSL 2 based engine. This overrides anything that may have been set at installation using the `--backend=<backend name>` flag.|    Â Â Â Â `dockerDaemonOptions`| | If `value` is set to true, it overrides the options in the Docker Engine config file. See the [Docker Engine reference](https://docs.docker.com/reference/cli/dockerd/#daemon-configuration-file). Note that for added security, a few of the config attributes may be overridden when Enhanced Container Isolation is enabled.|    Â Â Â Â `vpnkitCIDR`| | Overrides the network range used for vpnkit DHCP/DNS for `*.docker.internal`|       ### Windows containers

Parameter| OS| Description| Version   ---|---|---|---   `windowsContainers`| | Parameters and settings related to `windowsContainers` options - grouped together here for convenience.|    Â Â Â Â `dockerDaemonOptions`| | Overrides the options in the Linux daemon config file. See the [Docker Engine reference](https://docs.docker.com/reference/cli/dockerd/#daemon-configuration-file).|       > Note >  > This setting is not available to configure via the Docker Admin Console.

### Kubernetes

Parameter| OS| Description| Version   ---|---|---|---   `kubernetes`| | If `enabled` is set to true, a Kubernetes single-node cluster is started when Docker Desktop starts. If `showSystemContainers` is set to true, Kubernetes containers are displayed in the Docker Desktop Dashboard and when you run `docker ps`. The [imagesRepository](https://docs.docker.com/desktop/features/kubernetes/#configuring-a-custom-image-registry-for-kubernetes-control-plane-images) setting lets you specify which repository Docker Desktop pulls control-plane Kubernetes images from.|       > Note >  > When using the `imagesRepository` setting and Enhanced Container Isolation \(ECI\), add the following images to the ECI Docker socket mount image list: >  >   * \[imagesRepository\]/desktop-cloud-provider-kind:\* >   * \[imagesRepository\]/desktop-containerd-registry-mirror:\* > 

>  > These containers mount the Docker socket, so you must add the images to the ECI images list. If not, ECI will block the mount and Kubernetes won't start.

### Networking

Parameter| OS| Description| Version   ---|---|---|---   `defaultNetworkingMode`| Windows and Mac only| Defines the default IP protocol for new Docker networks: `dual-stack` \(IPv4 + IPv6, default\), `ipv4only`, or `ipv6only`.| Docker Desktop version 4.43 and later.   `dnsInhibition`| Windows and Mac only| Controls DNS record filtering returned to containers. Options: `auto` \(recommended\), `ipv4`, `ipv6`, `none`| Docker Desktop version 4.43 and later.      For more information, see [Networking](https://docs.docker.com/desktop/features/networking/#networking-mode-and-dns-behaviour-for-mac-and-windows).

### Beta features

> Important >  > For Docker Desktop versions 4.41 and earlier, some of these settings lived under the **Experimental features** tab on the **Features in development** page.

Parameter| OS| Description| Version   ---|---|---|---   `allowBetaFeatures`| | If `value` is set to `true`, beta features are enabled.|    `enableDockerAI`| | If `allowBetaFeatures` is true, setting `enableDockerAI` to `true` enables [Docker AI \(Ask Gordon\)](https://docs.docker.com/ai/gordon/) by default. You can independently control this setting from the `allowBetaFeatures` setting.|    `enableInference`| | If `allowBetaFeatures` is true, setting `enableInference` to `true` enables [Docker Model Runner](https://docs.docker.com/ai/model-runner/) by default. You can independently control this setting from the `allowBetaFeatures` setting.|    Â Â Â Â `enableInferenceTCP`| | Enable host-side TCP support. This setting requires Docker Model Runner setting to be enabled first.|    Â Â Â Â `enableInferenceTCPPort`| | Specifies the exposed TCP port. This setting requires Docker Model Runner setting to be enabled first.|    Â Â Â Â `enableInferenceCORS`| | Specifies the allowed CORS origins. Empty string to deny all,`*` to accept all, or a list of comma-separated values. This setting requires Docker Model Runner setting to be enabled first.|    `enableDockerMCPToolkit`| | If `allowBetaFeatures` is true, setting `enableDockerMCPToolkit` to `true` enables the [MCP toolkit feature](https://docs.docker.com/ai/mcp-catalog-and-toolkit/toolkit/) by default. You can independently control this setting from the `allowBetaFeatures` setting.|    `allowExperimentalFeatures`| | If `value` is set to `true`, experimental features are enabled.| Docker Desktop version 4.41 and earlier      ### Enhanced Container Isolation

Parameter| OS| Description| Version   ---|---|---|---   `enhancedContainerIsolation`| | If `value` is set to true, Docker Desktop runs all containers as unprivileged, via the Linux user-namespace, prevents them from modifying sensitive configurations inside the Docker Desktop VM, and uses other advanced techniques to isolate them. For more information, see [Enhanced Container Isolation](https://docs.docker.com/enterprise/security/hardened-desktop/enhanced-container-isolation/).|    Â Â Â Â `dockerSocketMount`| | By default, enhanced container isolation blocks bind-mounting the Docker Engine socket into containers \(e.g., `docker run -v /var/run/docker.sock:/var/run/docker.sock ...`\). This lets you relax this in a controlled way. See [ECI Configuration](https://docs.docker.com/enterprise/security/hardened-desktop/enhanced-container-isolation/config/) for more info.|    Â Â Â Â Â Â Â `imageList`| | Indicates which container images are allowed to bind-mount the Docker Engine socket.|    Â Â Â Â Â Â Â `commandList`| | Restricts the commands that containers can issue via the bind-mounted Docker Engine socket.|