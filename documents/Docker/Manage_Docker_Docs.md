# Manage | Docker Docs

**URL:** https://docs.docker.com/enterprise/security/single-sign-on/manage
**Word Count:** 2089
**Links Count:** 693
**Scraped:** 2025-07-16 02:01:51
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Manage single sign-on

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Subscription: Business

For: Administrators

## Manage organizations

> Note >  > You must have a [company](https://docs.docker.com/admin/company/) to manage more than one organization.

### Connect an organization

  1. Sign in to [Docker Home](https://app.docker.com) and select your organization. Note that when an organization is part of a company, you must select the company and configure SSO for that organization at the company level. Each organization can have its own SSO configuration and domain, but it must be configured at the company level..   2. Select **Admin Console** , then **SSO and SCIM**.   3. In the SSO connections table, select the **Action** icon and then **Edit connection**.   4. Select **Next** to navigate to the section where connected organizations are listed.   5. In the **Organizations** drop-down, select the organization to add to the connection.   6. Select **Next** to confirm or change the default organization and team provisioning.   7. Review the **Connection Summary** and select **Update connection**.

### Remove an organization

  1. Sign in to [Docker Home](https://app.docker.com) and select your organization. Note that when an organization is part of a company, you must select the company and configure SSO for that organization at the company level. Each organization can have its own SSO configuration and domain, but it must be configured at the company level..   2. Select **Admin Console** , then **SSO and SCIM**.   3. In the SSO connections table, select the **Action** icon and then **Edit connection**.   4. Select **Next** to navigate to the section where connected organizations are listed.   5. In the **Organizations** drop-down, select **Remove** to remove the connection.   6. Select **Next** to confirm or change the default organization and team provisioning.   7. Review the **Connection Summary** and select **Update connection**.

## Manage domains

Admin Console  Docker Hub

### Remove a domain from an SSO connection

> Important >  > Docker supports multiple IdP configurations, where a single domain is used for multiple SSO identity providers. If you want to remove a domain from multiple SSO connections, you must remove it from each connection individually.

  1. Sign in to [Docker Home](https://app.docker.com) and select your organization. Note that when an organization is part of a company, you must select the company and configure SSO for that organization at the company level. Each organization can have its own SSO configuration and domain, but it must be configured at the company level..   2. Select **Admin Console** , then **SSO and SCIM**.   3. In the SSO connections table, select the **Action** icon and then **Edit connection**.   4. Select **Next** to navigate to the section where the connected domains are listed.   5. In the **Domain** drop-down, select the **x** icon next to the domain that you want to remove.   6. Select **Next** to confirm or change the connected organization\(s\).   7. Select **Next** to confirm or change the default organization and team provisioning selections.   8. Review the **Connection Summary** and select **Update connection**.

> Note >  > If you want to re-add the domain, a new TXT record value is assigned. You must then complete the verification steps with the new TXT record value.

> Important >  > Organization management is moving to the Admin Console. >  > Manage members, team, settings, and activity logs in the Docker Admin Console. Access to these features in Docker Hub will end soon. Explore the [Admin Console](https://app.docker.com/admin).

### Remove a domain from an SSO connection

> Important >  > Docker supports multiple IdP configurations, where a single domain is used for multiple SSO identity providers. If you want to remove a domain from multiple SSO connections, you must remove it from each connection individually.

  1. Sign in to [Docker Hub](https://hub.docker.com).   2. Navigate to the SSO settings page for your organization. Select **My Hub** , your organization, **Settings** , and then **Security**.   3. In the SSO connections table, select the **Action** icon and then **Edit connection**.   4. Select **Next** to navigate to the section where the connected domains are listed.   5. In the **Domain** drop-down, select the **x** icon next to the domain that you want to remove.   6. Select **Next** to confirm or change the connected organization\(s\).   7. Select **Next** to confirm or change the default organization and team provisioning selections.   8. Review the **Connection Summary** and select **Update connection**.

> Note >  > If you want to re-add the domain, a new TXT record value is assigned. You must then complete the verification steps with the new TXT record value.

## Manage SSO connections

Admin Console  Docker Hub

### Edit a connection

  1. Sign in to [Docker Home](https://app.docker.com) and select your organization. Note that when an organization is part of a company, you must select the company and configure SSO for that organization at the company level. Each organization can have its own SSO configuration and domain, but it must be configured at the company level..   2. Select **Admin Console** , then **SSO and SCIM**.   3. In the SSO connections table, select the **Action** icon.   4. Select **Edit connection**.   5. Follow the on-screen instructions to edit the connection.

### Delete a connection

  1. Sign in to [Docker Home](https://app.docker.com) and select your organization. Note that when an organization is part of a company, you must select the company and configure SSO for that organization at the company level. Each organization can have its own SSO configuration and domain, but it must be configured at the company level..   2. Select **Admin Console** , then **SSO and SCIM**.   3. In the SSO connections table, select the **Action** icon.   4. Select **Delete connection**.   5. Follow the on-screen instructions to delete a connection.

### Deleting SSO

When you disable SSO, you can delete the connection to remove the configuration settings and the added domains. Once you delete this connection, it can't be undone. If an SSO connection is deleted, Docker users must authenticate with their Docker ID and password.

> Important >  > Organization management is moving to the Admin Console. >  > Manage members, team, settings, and activity logs in the Docker Admin Console. Access to these features in Docker Hub will end soon. Explore the [Admin Console](https://app.docker.com/admin).

### Edit a connection

  1. Sign in to [Docker Hub](https://hub.docker.com).   2. Navigate to the SSO settings page for your organization. Select **My Hub** , your organization, **Settings** , and then **Security**.   3. In the SSO connections table, select the **Action** icon.   4. Select **Edit connection**.   5. Follow the on-screen instructions to edit the connection.

### Delete a connection

  1. Sign in to [Docker Hub](https://hub.docker.com).   2. Navigate to the SSO settings page for your organization. Select **My Hub** , your organization, **Settings** , and then **Security**.   3. In the SSO connections table, select the **Action** icon.   4. Select **Delete connection**.   5. Follow the on-screen instructions to delete a connection.

### Deleting SSO

When you disable SSO, you can delete the connection to remove the configuration settings and the added domains. Once you delete this connection, it can't be undone. If an SSO connection is deleted, Docker users must authenticate with their Docker ID and password.

## Manage users

> Important >  > SSO has Just-In-Time \(JIT\) Provisioning enabled by default unless you have [disabled it](https://docs.docker.com/enterprise/security/provisioning/just-in-time/#sso-authentication-with-jit-provisioning-disabled). This means your users are auto-provisioned to your organization. >  > You can change this on a per-app basis. To prevent auto-provisioning users, you can create a security group in your IdP and configure the SSO app to authenticate and authorize only those users that are in the security group. Follow the instructions provided by your IdP: >  >   * [Okta](https://help.okta.com/en-us/Content/Topics/Security/policies/configure-app-signon-policies.htm) >   * [Entra ID \(formerly Azure AD\)](https://learn.microsoft.com/en-us/azure/active-directory/develop/howto-restrict-your-app-to-a-set-of-users) > 

>  > Alternatively, see the [Provisioning overview](https://docs.docker.com/enterprise/security/provisioning/) guide.

### Add guest users when SSO is enabled

To add a guest that isn't verified through your IdP:

  1. Sign in to [Docker Home](https://app.docker.com/) and select your organization.   2. Select **Members**.   3. Select **Invite**.   4. Follow the on-screen instructions to invite the user.

### Remove users from the SSO company

To remove a user:

  1. Sign in to [Docker Home](https://app.docker.com/) and select your organization.   2. Select **Members**.   3. Select the action icon next to a userâs name, and then select **Remove member** , if you're an organization, or **Remove user** , if you're a company.   4. Follow the on-screen instructions to remove the user.

## Manage provisioning

Users are provisioned with Just-in-Time \(JIT\) provisioning by default. If you enable SCIM, you can disable JIT. For more information, see the [Provisioning overview](https://docs.docker.com/enterprise/security/provisioning/) guide.

## What's next?

  * [Set up SCIM](https://docs.docker.com/enterprise/security/provisioning/scim/)   * [Enable Group mapping](https://docs.docker.com/enterprise/security/provisioning/group-mapping/)