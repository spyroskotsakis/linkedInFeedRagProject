# Backup and restore data | Docker Docs

**URL:** https://docs.docker.com/desktop/settings-and-maintenance/backup-and-restore/
**Word Count:** 1470
**Links Count:** 660
**Scraped:** 2025-07-16 01:46:47
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# How to back up and restore your Docker Desktop data

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Use this procedure to back up and restore your images and container data. This is useful if you want to reset your VM disk or to move your Docker environment to a new computer, or recover from a failed Docker Desktop update or installation.

> Important >  > If you use volumes or bind-mounts to store your container data, backing up your containers may not be needed, but make sure to remember the options that were used when creating the container or use a [Docker Compose file](https://docs.docker.com/reference/compose-file/) if you want to re-create your containers with the same configuration after re-installation.

## If Docker Desktop is functioning normally

### Save your data

  1. Commit your containers to an image with [`docker container commit`](https://docs.docker.com/reference/cli/docker/container/commit/).

Committing a container stores filesystem changes and some container configurations, such as labels and environment variables, as a local image. Be aware that environment variables may contain sensitive information such as passwords or proxy-authentication, so take care when pushing the resulting image to a registry.

Also note that filesystem changes in a volume that are attached to the container are not included in the image, and must be backed up separately.

If you used a [named volume](https://docs.docker.com/engine/storage/#more-details-about-mount-types) to store container data, such as databases, refer to the [back up, restore, or migrate data volumes](https://docs.docker.com/engine/storage/volumes/#back-up-restore-or-migrate-data-volumes) page in the storage section.

  2. Use [`docker push`](https://docs.docker.com/reference/cli/docker/image/push/) to push any images you have built locally and want to keep to the [Docker Hub registry](https://docs.docker.com/docker-hub/).

> Tip >  > [Set the repository visibility to private](https://docs.docker.com/docker-hub/repos/) if your image includes sensitive content.

Alternatively, use [`docker image save -o images.tar image1 [image2 ...]`](https://docs.docker.com/reference/cli/docker/image/save/) to save any images you want to keep to a local `.tar` file.

After backing up your data, you can uninstall the current version of Docker Desktop and [install a different version](https://docs.docker.com/desktop/release-notes/) or reset Docker Desktop to factory defaults.

### Restore your data

  1. Load your images.

     * If you pushed to Docker Hub:                        $ docker pull <my-backup-image>            

     * If you saved a `.tar` file:                        $ docker image load -i images.tar            

  2. Re-create your containers if needed, using [`docker run`](https://docs.docker.com/reference/cli/docker/container/run/), or [Docker Compose](https://docs.docker.com/compose/).

To restore volume data, refer to [backup, restore, or migrate data volumes](https://docs.docker.com/engine/storage/volumes/#back-up-restore-or-migrate-data-volumes).

## If Docker Desktop fails to start

If Docker Desktop cannot launch and must be reinstalled, you can back up its VM disk and image data directly from disk. Docker Desktop must be fully stopped before backing up these files.

Windows  Mac  Linux

  1. Back up Docker containers/images.

Backup the following file:                    %LOCALAPPDATA%\Docker\wsl\data\docker_data.vhdx          

Copy it to a safe location.

  2. Back up WSL distributions.

If you're running any WSL Linux distributions \(Ubuntu, Alpine, etc.\), back them up using [Microsoft's guide](https://learn.microsoft.com/en-us/windows/wsl/faq#how-can-i-back-up-my-wsl-distributions-).

  3. Restore.

After reinstalling Docker Desktop, restore the `docker_data.vhdx` to the same location and re-import your WSL distributions if needed.

  1. Back up Docker containers/images.

Backup the following file:                    ~/Library/Containers/com.docker.docker/Data/vms/0/data/Docker.raw          

Copy it to a safe location.

  2. Restore.

After reinstalling Docker Desktop, restore the `Docker.raw` to the same location.

  1. Back up Docker containers/images:

Backup the following file:                    ~/.docker/desktop/vms/0/data/Docker.raw          

Copy it to a safe location.

  2. Restore.

After reinstalling Docker Desktop, restore the `Docker.raw` to the same location.