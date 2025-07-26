# Remediation | Docker Docs

**URL:** https://docs.docker.com/guides/docker-scout/remediation/
**Word Count:** 191
**Links Count:** 51
**Scraped:** 2025-07-16 01:48:52
**Status:** completed

---

Back

[Guides](https://docs.docker.com/guides/)

  * [Get started](https://docs.docker.com/get-started/)   * [Manuals](https://docs.docker.com/manuals/)   * [Reference](https://docs.docker.com/reference/)

* * *

[Securing your software supply chain with Docker Scout](https://docs.docker.com/guides/docker-scout/)

Enhance container security by automating vulnerability detection and remediation.

[ Product demo](https://docs.docker.com/tags/product-demo/)

20 minutes

[1](https://docs.docker.com/guides/docker-scout/why/)

[Why Docker Scout?](https://docs.docker.com/guides/docker-scout/why/)

[2](https://docs.docker.com/guides/docker-scout/demo/)

[Demo](https://docs.docker.com/guides/docker-scout/demo/)

[3](https://docs.docker.com/guides/docker-scout/s3c/)

[Software supply chain security](https://docs.docker.com/guides/docker-scout/s3c/)

[4](https://docs.docker.com/guides/docker-scout/sbom/)

[Software Bill of Materials](https://docs.docker.com/guides/docker-scout/sbom/)

[5](https://docs.docker.com/guides/docker-scout/attestations/)

[Attestations](https://docs.docker.com/guides/docker-scout/attestations/)

[6](https://docs.docker.com/guides/docker-scout/remediation/)

[Remediation](https://docs.docker.com/guides/docker-scout/remediation/)

[7](https://docs.docker.com/guides/docker-scout/common-questions/)

[Common challenges and questions](https://docs.docker.com/guides/docker-scout/common-questions/)

Resources:

  * [Docker Scout overview](https://docs.docker.com/scout/)   * [Docker Scout quickstart](https://docs.docker.com/scout/quickstart/)   * [Install Docker Scout](https://docs.docker.com/scout/install/)

[Â« Back to all guides](https://docs.docker.com/guides/)

# Remediation

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

* * *

Docker Scout's [remediation feature](https://docs.docker.com/scout/policy/remediation/) helps you address supply chain and security issues by offering tailored recommendations based on policy evaluations. These recommendations guide you in improving policy compliance or enhancing image metadata, allowing Docker Scout to perform more accurate evaluations in the future.

You can use this feature to ensure that your base images are up-to-date and that your supply chain attestations are complete. When a violation occurs, Docker Scout provides recommended fixes, such as updating your base image or adding missing attestations. If there isnât enough information to determine compliance, Docker Scout suggests actions to help resolve the issue.

In the Docker Scout Dashboard, you can view and act on these recommendations by reviewing violations or compliance uncertainties. With integrations like GitHub, you can even automate updates, directly fixing issues from the dashboard.

[Common challenges and questions Â»](https://docs.docker.com/guides/docker-scout/common-questions/)