# Troubleshoot provisioning | Docker Docs

**URL:** https://docs.docker.com/security/troubleshoot/troubleshoot-provisioning/
**Word Count:** 1329
**Links Count:** 652
**Scraped:** 2025-07-16 01:54:28
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Troubleshoot provisioning

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

If you experience issues with user roles, attributes, or unexpected account behavior with user provisioning, this guide provides troubleshooting recommendations to resolve conflicts.

## SCIM attribute values are overwritten or ignored

### Error message

Typically, this scenario does not produce an error message in Docker or your IdP. This issue ususally surfaces as incorrect role or team assignment.

### Possible causes

  * JIT provisioning is enabled, and Docker is using values from your IdP's SSO login flow to provision the user, which overrides SCIM-provided attributes.   * SCIM was enabled after the user was already provisioned via JIT, so SCIM updates don't take effect.

### Affected environments

  * Docker organizations using SCIM with SSO   * Users provisioned via JIT prior to SCIM setup

### Steps to replicate

  1. Enable JIT and SSO for your Docker organization.   2. Sign in to Docker as a user via SSO.   3. Enable SCIM and set role/team attributes for that user.   4. SCIM attempts to update the user's attributes, but the role or team assignment does not reflect changes.

### Solutions

#### Disable JIT provisioning \(recommended\)

  1. Sign in to [Docker Home](https://app.docker.com/).   2. Select **Admin Console** , then **SSO and SCIM**.   3. Find the relevant SSO connection.   4. Select the **actions menu** and choose **Edit**.   5. Disable **Just-in-Time provisioning**.   6. Save your changes.

With JIT disabled, Docker uses SCIM as the source of truth for user creation and role assignment.

**Keep JIT enabled and match attributes**

If you prefer to keep JIT enabled:

  * Make sure your IdP's SSO attribute mappings match the values being sent by SCIM.   * Avoid configuring SCIM to override attributes already set via JIT.

This option requires strict coordination between SSO and SCIM attributes in your IdP configuration.

## SCIM updates don't apply to existing users

### Possible causes

User accounts were originally created manually or via JIT, and SCIM is not linked to manage them.

### Solution

SCIM only manages users that it provisions. To allow SCIM to manage an existing user:

  1. Remove the user manually from the Docker [Admin Console](https://app.docker.com/admin).   2. Trigger provisioning from your IdP.   3. SCIM will re-create the user with correct attributes.

> Warning >  > Deleting a user removes their resource ownership \(e.g., repositories\). Transfer ownership before removing the user.