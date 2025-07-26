# Sign in | Docker Docs

**URL:** https://docs.docker.com/desktop/setup/sign-in/
**Word Count:** 1277
**Links Count:** 653
**Scraped:** 2025-07-16 01:48:09
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Sign in to Docker Desktop

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Docker recommends signing in with the **Sign in** option in the top-right corner of the Docker Dashboard.

In large enterprises where admin access is restricted, administrators can [enforce sign-in](https://docs.docker.com/enterprise/security/enforce-sign-in/).

> Tip >  > Explore [Docker's core subscriptions](https://www.docker.com/pricing/) to see what else Docker can offer you.

## Benefits of signing in

  * Access your Docker Hub repositories directly from Docker Desktop.

  * Increase your pull rate limit compared to anonymous users. See [Usage and limits](https://docs.docker.com/docker-hub/usage/).

  * Enhance your organizationâs security posture for containerized development with [Hardened Desktop](https://docs.docker.com/enterprise/security/hardened-desktop/).

> Note >  > Docker Desktop automatically signs you out after 90 days, or after 30 days of inactivity.

## Signing in with Docker Desktop for Linux

Docker Desktop for Linux relies on [`pass`](https://www.passwordstore.org/) to store credentials in GPG-encrypted files. Before signing in to Docker Desktop with your [Docker ID](https://docs.docker.com/accounts/create-account/), you must initialize `pass`. Docker Desktop displays a warning if `pass` is not configured.

  1. Generate a GPG key. You can initialize pass by using a gpg key. To generate a gpg key, run:                    $ gpg --generate-key          

  2. Enter your name and email once prompted.

Once confirmed, GPG creates a key pair. Look for the `pub` line that contains your GPG ID, for example:                    ...          pubrsa3072 2022-03-31 [SC] [expires: 2024-03-30]           3ABCD1234EF56G78          uid          Molly <molly@example.com>

  3. Copy the GPG ID and use it to initialize `pass`                    $ pass init <your_generated_gpg-id_public_key>          

You should see output similar to:                    mkdir: created directory '/home/molly/.password-store/'          Password store initialized for <generated_gpg-id_public_key>

Once you initialize `pass`, you can sign in and pull your private images. When Docker CLI or Docker Desktop use credentials, a user prompt may pop up for the password you set during the GPG key generation.               $ docker pull molly/privateimage     Using default tag: latest     latest: Pulling from molly/privateimage     3b9cc81c3203: Pull complete      Digest: sha256:3c6b73ce467f04d4897d7a7439782721fd28ec9bf62ea2ad9e81a5fb7fb3ff96     Status: Downloaded newer image for molly/privateimage:latest     docker.io/molly/privateimage:latest     

## What's next?

  * [Explore Docker Desktop](https://docs.docker.com/desktop/use-desktop/) and its features.   * Change your [Docker Desktop settings](https://docs.docker.com/desktop/settings-and-maintenance/settings/).   * [Browse common FAQs](https://docs.docker.com/desktop/troubleshoot-and-support/faqs/general/).