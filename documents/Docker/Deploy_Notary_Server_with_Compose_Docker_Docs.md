# Deploy Notary Server with Compose | Docker Docs

**URL:** https://docs.docker.com/engine/security/trust/deploying_notary
**Word Count:** 1157
**Links Count:** 645
**Scraped:** 2025-07-16 02:01:51
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Deploy Notary Server with Compose

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

The easiest way to deploy Notary Server is by using Docker Compose. To follow the procedure on this page, you must have already [installed Docker Compose](https://docs.docker.com/compose/install/).

  1. Clone the Notary repository.                    $ git clone https://github.com/theupdateframework/notary.git          

  2. Build and start Notary Server with the sample certificates.                    $ docker compose up -d           

For more detailed documentation about how to deploy Notary Server, see the [instructions to run a Notary service](https://github.com/theupdateframework/notary/blob/master/docs/running_a_service.md) as well as [the Notary repository](https://github.com/theupdateframework/notary) for more information.

  3. Make sure that your Docker or Notary client trusts Notary Server's certificate before you try to interact with the Notary server.

See the instructions for [Docker](https://docs.docker.com/reference/cli/docker/#notary) or for [Notary](https://github.com/docker/notary#using-notary) depending on which one you are using.

## If you want to use Notary in production

Check back here for instructions after Notary Server has an official stable release. To get a head start on deploying Notary in production, see [the Notary repository](https://github.com/theupdateframework/notary).