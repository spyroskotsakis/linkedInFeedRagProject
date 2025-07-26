# Service accounts | Docker Docs

**URL:** https://docs.docker.com/docker-hub/service-accounts/
**Word Count:** 1178
**Links Count:** 638
**Scraped:** 2025-07-16 01:48:31
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Service accounts

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

> Important >  > As of December 10, 2024, Enhanced Service Account add-ons are no longer available. Existing Service Account agreements will be honored until their current term expires, but new purchases or renewals of Enhanced Service Account add-ons are no longer available and customers must renew under a new subscription. >  > Docker recommends transitioning to [Organization Access Tokens \(OATs\)](https://docs.docker.com/enterprise/security/access-tokens/), which can provide similar functionality.

A service account is a Docker ID used for automated management of container images or containerized applications. Service accounts are typically used in automated workflows, and don't share Docker IDs with the members in the organization. Common use cases for service accounts include mirroring content on Docker Hub, or tying in image pulls from your CI/CD process.

## Enhanced Service Account add-on tiers

Refer to the following table for details on the Enhanced Service Account add-ons:

Tier| Pull Rates Per Day\*   ---|---   1| 5,000-10,000   2| 10,000-25,000   3| 25,000-50,000   4| 50,000-100,000   5| 100,000+      \*The service account may exceed Pulls by up to 25% for up to 20 days during the year without incurring additional fees. Reports on consumption are available upon request.