# Roles and permissions | Docker Docs

**URL:** https://docs.docker.com/security/for-admins/roles-and-permissions
**Word Count:** 1486
**Links Count:** 657
**Scraped:** 2025-07-16 02:04:08
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Roles and permissions

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

For: Administrators

This guide outlines Docker's organization roles and their permission scopes.

## Roles

When you invite users to your organization, you assign them a role. A role is a collection of permissions. Roles define whether users can create repositories, pull images, create teams, and configure organization settings.

The following roles are available to assign:

  * Member: Non-administrative role. Members can view other members that are in the same organization.   * Editor: Partial administrative access to the organization. Editors can create, edit, and delete repositories. They can also edit an existing team's access permissions.   * Owner: Full organization administrative access. Owners can manage organization repositories, teams, members, settings, and billing.

Owners can manage roles for members of an organization using Docker Hub or the Admin Console:

  * Update a member role in [Docker Hub](https://docs.docker.com/admin/organization/members/#update-a-member-role)   * Update an organization's members or company in the [Admin Console](https://docs.docker.com/admin/company/users/#update-a-member-role)   * Learn more about [organizations and companies](https://docs.docker.com/admin/)

## Permissions

> Note >  > Company owners have the same access as owners for all associated organizations. For more information, see [Company overview](https://docs.docker.com/admin/company/).

The following sections describe the permissions for each role.

### Content and registry permissions

The following table outlines content and registry permissions for member, editor, and owner roles. These permissions and roles apply to the entire organization, including all the repositories in the namespace for the organization.

Permission| Member| Editor| Owner   ---|---|---|---   Explore images and extensions| â | â | â    Star, favorite, vote, and comment on content| â | â | â    Pull images| â | â | â    Create and publish an extension| â | â | â    Become a Verified, Official, or Open Source publisher| â| â| â    Observe content engagement as a publisher| â| â| â    Create public and private repositories| â| â | â    Edit and delete repositories| â| â | â    Manage tags| â| â | â    View repository activity| â| â| â    Set up Automated builds| â| â| â    Edit build settings| â| â| â    View teams| â | â | â    Assign team permissions to repositories| â| â | â       When you add members to a team, you can manage their repository permissions. For team repository permissions, see [Create and manage a team permissions reference](https://docs.docker.com/admin/organization/manage-a-team/#permissions-reference).

The following diagram provides an example of how permissions may work for a user. In this example, the first permission check is for the role: member or editor. Editors have administrative permissions for repositories across the namespace of the organization. Members may have administrative permissions for a repository if they're a member of a team that grants those permissions.

![User repository permissions within an organization](https://docs.docker.com/enterprise/images/roles-and-permissions-member-editor-roles.png)

![User repository permissions within an organization](https://docs.docker.com/enterprise/images/roles-and-permissions-member-editor-roles.png)

### Organization management permissions

The following table outlines organization management permissions for member, editor, owner, and company owner roles.

Permission| Member| Editor| Owner   ---|---|---|---   Create teams| â| â| â    Manage teams \(including delete\)| â| â| â    Configure the organization's settings \(including linked services\)| â| â| â    Add organizations to a company| â| â| â    Invite members| â| â| â    Manage members| â| â| â    Manage member roles and permissions| â| â| â    View member activity| â| â| â    Export and reporting| â| â| â    Image Access Management| â| â| â    Registry Access Management| â| â| â    Set up Single Sign-On \(SSO\) and SCIM| â| â| â \*   Require Docker Desktop sign-in| â| â| â \*   Manage billing information \(for example, billing address\)| â| â| â    Manage payment methods \(for example, credit card or invoice\)| â| â| â    View billing history| â| â| â    Manage subscriptions| â| â| â    Manage seats| â| â| â    Upgrade and downgrade plans| â| â| â        _\* If not part of a company_

### Docker Scout permissions

The following table outlines Docker Scout management permissions for member, editor, and owner roles.

Permission| Member| Editor| Owner   ---|---|---|---   View and compare analysis results| â | â | â    Upload analysis records| â | â | â    Activate and deactivate Docker Scout for a repository| â| â | â    Create environments| â| â| â    Manage registry integrations| â| â| â       ### Docker Build Cloud permissions

The following table outlines Docker Build Cloud management permissions for member, editor, and owner roles.

Permission| Member| Editor| Owner   ---|---|---|---   Use a cloud builder| â | â | â    Create and remove builders| â | â | â    Configure builder settings| â | â | â    Buy minutes| â| â| â    Manage subscription| â| â| â