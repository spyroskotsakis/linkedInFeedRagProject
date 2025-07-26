# View Docker Scout policy status | Docker Docs

**URL:** https://docs.docker.com/scout/policy/view/
**Word Count:** 1489
**Links Count:** 651
**Scraped:** 2025-07-16 01:54:44
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# View Docker Scout policy status

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

You can track policy status for your artifacts from the Docker Scout Dashboard, or using the CLI.

## Dashboard

The **Overview** tab of the [Docker Scout Dashboard](https://scout.docker.com/) displays a summary of recent changes in policy for your repositories. This summary shows images that have seen the most change in their policy evaluation between the most recent image and the previous image.

![Policy overview](https://docs.docker.com/scout/images/policy-overview.webp)

![Policy overview](https://docs.docker.com/scout/images/policy-overview.webp)

### Policy status per repository

The **Images** tab shows the current policy status, and recent policy trend, for all images in the selected environment. The **Policy status** column in the list shows:

  * Number of fulfilled policies versus the total number of policies   * Recent policy trends

![Policy status in the image list](https://docs.docker.com/scout/images/policy-image-list.webp)

![Policy status in the image list](https://docs.docker.com/scout/images/policy-image-list.webp)

The policy trend, denoted by the directional arrows, indicates whether an image is better, worse, or unchanged in terms of policy, compared to the previous image in the same environment.

  * The green arrow pointing upwards shows the number of policies that got better in the latest pushed image.   * The red arrow pointing downwards shows the number of policies that got worse in the latest pushed image.   * The bidirectional gray arrow shows the number of policies that were unchanged in the latest version of this image.

If you select a repository, you can open the **Policy** tab for a detailed description of the policy delta for the most recently analyzed image and its predecessor.

### Detailed results and remediation

To view the full evaluation results for an image, navigate to the image tag in the Docker Scout Dashboard and open the **Policy** tab. This shows a breakdown for all policy violations for the current image.

![Detailed Policy Evaluation results](https://docs.docker.com/scout/images/policy-detailed-results.webp)

![Detailed Policy Evaluation results](https://docs.docker.com/scout/images/policy-detailed-results.webp)

This view also provides recommendations on how to improve improve policy status for violated policies.

![Policy details in the tag view](https://docs.docker.com/scout/images/policy-tag-view.webp)

![Policy details in the tag view](https://docs.docker.com/scout/images/policy-tag-view.webp)

For vulnerability-related policies, the policy details view displays the fix version that removes the vulnerability, when a fix version is available. To fix the issue, upgrade the package version to the fix version.

For licensing-related policies, the list shows all packages whose license doesn't meet the policy criteria. To fix the issue, find a way to remove the dependency to the violating package, for example by looking for an alternative package distributed under a more appropriate license.

## CLI

To view policy status for an image from the CLI, use the `docker scout policy` command.               $ docker scout policy \       --org dockerscoutpolicy \       --platform linux/amd64 \       dockerscoutpolicy/email-api-service:0.0.2              â Pulled         â Policy evaluation results found               â## Overview     â     â             â               Analyzed Image     âââââââââââââââ¼ââââââââââââââââââââââââââââââââââââââââââââââ     â  Target     â  dockerscoutpolicy/email-api-service:0.0.2     â    digest   â  17b1fde0329c     â    platform â linux/amd64     â     â     â## Policies     â     âPolicy status  FAILED  (2/8 policies met, 3 missing data)     â     â  Status â                  Policy                             â           Results     âââââââââââ¼ââââââââââââââââââââââââââââââââââââââââââââââââââââââ¼ââââââââââââââââââââââââââââââ     â  â      â No copyleft licenses                                â    0 packages     â  !      â Default non-root user                               â     â  !      â No fixable critical or high vulnerabilities         â    2C     1H     0M     0L     â  â      â No high-profile vulnerabilities                     â    0C     0H     0M     0L     â  ?      â No outdated base images                             â    No data     â         â                                                     â    Learn more â     â  ?      â SonarQube quality gates passed                      â    No data     â         â                                                     â    Learn more â     â  !      â Supply chain attestations                           â    2 deviations     â  ?      â No unapproved base images                           â    No data          ...     

For more information about the command, refer to the [CLI reference](https://docs.docker.com/reference/cli/docker/scout/policy/).