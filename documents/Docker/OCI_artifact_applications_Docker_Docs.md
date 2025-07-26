# OCI artifact applications | Docker Docs

**URL:** https://docs.docker.com/compose/how-tos/oci-artifact
**Word Count:** 1671
**Links Count:** 663
**Scraped:** 2025-07-16 02:01:51
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Package and deploy Docker Compose applications as OCI artifacts

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Requires: Docker Compose [2.34.0](https://docs.docker.com/compose/releases/release-notes/#2340) and later

Docker Compose supports working with [OCI artifacts](https://docs.docker.com/docker-hub/repos/manage/hub-images/oci-artifacts/), allowing you to package and distribute your Compose applications through container registries. This means you can store your Compose files alongside your container images, making it easier to version, share, and deploy your multi-container applications.

## Publish your Compose application as an OCI artifact

To distribute your Compose application as an OCI artifact, you can use the `docker compose publish` command, to publish it to an OCI-compliant registry. This allows others to then deploy your application directly from the registry.

The publish function supports most of the composition capabilities of Compose, like overrides, extends or include, with some limitations.

### General steps

  1. Navigate to your Compose application's directory.   Ensure you're in the directory containing your `compose.yml` file or that you are specifying your Compose file with the `-f` flag.

  2. In your terminal, sign in to your Docker account so you're authenticated with Docker Hub.                    $ docker login          

  3. Use the `docker compose publish` command to push your application as an OCI artifact:                    $ docker compose publish username/my-compose-app:latest          

If you have multiple Compose files, run:                    $ docker compose -f compose-base.yml -f compose-production.yml publish username/my-compose-app:latest          

### Advanced publishing options

When publishing, you can pass additional options:

  * `--oci-version`: Specify the OCI version \(default is automatically determined\).   * `--resolve-image-digests`: Pin image tags to digests.   * `--with-env`: Include environment variables in the published OCI artifact.

Compose checks to make sure there isn't any sensitive data in your configuration and displays your environment variables to confirm you want to publish them.               ...     you are about to publish sensitive data within your OCI artifact.     please double check that you are not leaking sensitive data     AWS Client ID     "services.serviceA.environment.AWS_ACCESS_KEY_ID": xxxxxxxxxx     AWS Secret Key     "services.serviceA.environment.AWS_SECRET_ACCESS_KEY": aws"xxxx/xxxx+xxxx+"     Github authentication     "GITHUB_TOKEN": ghp_xxxxxxxxxx     JSON Web Token     "": xxxxxxx.xxxxxxxx.xxxxxxxx     Private Key     "": -----BEGIN DSA PRIVATE KEY-----     xxxxx     -----END DSA PRIVATE KEY-----     Are you ok to publish these sensitive data? [y/N]:y          you are about to publish environment variables within your OCI artifact.     please double check that you are not leaking sensitive data     Service/Config  serviceA     FOO=bar     Service/Config  serviceB     FOO=bar     QUIX=     BAR=baz     Are you ok to publish these environment variables? [y/N]: 

If you decline, the publish process stops without sending anything to the registry.

## Limitations

There are limitations to publishing Compose applications as OCI artifacts. You can't publish a Compose configuration:

  * With service\(s\) containing bind mounts   * With service\(s\) containing only a `build` section   * That includes local files with the `include` attribute. To publish successfully, ensure that any included local files are also published. You can then use `include` to reference these files as remote `include` is supported.

## Start an OCI artifact application

To start a Docker Compose application that uses an OCI artifact, you can use the `-f` \(or `--file`\) flag followed by the OCI artifact reference. This allows you to specify a Compose file stored as an OCI artifact in a registry.

The `oci://` prefix indicates that the Compose file should be pulled from an OCI-compliant registry rather than loaded from the local filesystem.               $ docker compose -f oci://docker.io/username/my-compose-app:latest up     

To then run the Compose application, use the `docker compose up` command with the `-f` flag pointing to your OCI artifact:               $ docker compose -f oci://docker.io/username/my-compose-app:latest up     

### Troubleshooting

When you run an application from an OCI artifact, Compose may display warning messages that require you to confirm the following so as to limit the risk of running a malicious application:

  * A list of the interpolation variables used along with their values   * A list of all environment variables used by the application   * If your OCI artifact application is using another remote resources, for example via [`include`](https://docs.docker.com/reference/compose-file/include/).

              $ REGISTRY=myregistry.com docker compose -f oci://docker.io/username/my-compose-app:latest up          Found the following variables in configuration:     VARIABLE     VALUE                SOURCE        REQUIRED    DEFAULT     REGISTRY     myregistry.com      command-line   yes              TAG          v1.0                environment    no          latest     DOCKERFILE   Dockerfile          default        no          Dockerfile     API_KEY      <unset>             none           no                    Do you want to proceed with these variables? [Y/n]:y          Warning: This Compose project includes files from remote sources:     - oci://registry.example.com/stack:latest     Remote includes could potentially be malicious. Make sure you trust the source.     Do you want to continue? [y/N]: 

If you agree to start the application, Compose displays the directory where all the resources from the OCI artifact have been downloaded:               ...     Do you want to continue? [y/N]: y          Your compose stack "oci://registry.example.com/stack:latest" is stored in "~/Library/Caches/docker-compose/964e715660d6f6c3b384e05e7338613795f7dcd3613890cfa57e3540353b9d6d"

The `docker compose publish` command supports non-interactive execution, letting you skip the confirmation prompt by including the `-y` \(or `--yes`\) flag:               $ docker compose publish -y username/my-compose-app:latest     

## Next steps

  * [Learn about OCI artifacts in Docker Hub](https://docs.docker.com/docker-hub/repos/manage/hub-images/oci-artifacts/)   * [Compose publish command](https://docs.docker.com/reference/cli/docker/compose/publish/)   * [Understand `include`](https://docs.docker.com/reference/compose-file/include/)