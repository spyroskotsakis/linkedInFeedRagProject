# Create and manage a team | Docker Docs

**URL:** https://docs.docker.com/admin/organization/manage-a-team
**Word Count:** 1730
**Links Count:** 671
**Scraped:** 2025-07-16 01:59:56
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Create and manage a team

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Subscription: Team Business

For: Administrators

You can create teams for your organization in the Admin Console or Docker Hub, and configure team repository access in Docker Hub.

A team is a group of Docker users that belong to an organization. An organization can have multiple teams. An organization owner can create new teams and add members to an existing team using their Docker ID or email address. Members aren't required to be part of a team to be associated with an organization.

The organization owner can add additional organization owners to help them manage users, teams, and repositories in the organization by assigning them the owner role.

## What is an organization owner?

An organization owner is an administrator who has the following permissions:

  * Manage repositories and add team members to the organization   * Access private repositories, all teams, billing information, and organization settings   * Specify permissions for each team in the organization   * Enable [SSO](https://docs.docker.com/enterprise/security/single-sign-on/) for the organization

When SSO is enabled for your organization, the organization owner can also manage users. Docker can auto-provision Docker IDs for new end-users or users who'd like to have a separate Docker ID for company use through SSO enforcement.

Organization owners can add others with the owner role to help them manage users, teams, and repositories in the organization.

For more information on roles, see [Roles and permissions](https://docs.docker.com/enterprise/security/roles-and-permissions/).

## Create a team

Admin Console  Docker Hub

  1. Sign in to [Docker Home](https://app.docker.com) and select your organization.   2. Select **Teams**.

> Important >  > Organization management is moving to the Admin Console. >  > Manage members, team, settings, and activity logs in the Docker Admin Console. Access to these features in Docker Hub will end soon. Explore the [Admin Console](https://app.docker.com/admin).

  1. Sign in to [Docker Hub](https://hub.docker.com).   2. Select **My Hub** and choose your organization.   3. Select the **Teams** and then select **Create Team**.   4. Fill out your team's information and select **Create**.   5. [Add members to your team](https://docs.docker.com/admin/organization/members/#add-a-member-to-a-team).

## Set team repository permissions

Organization owners can configure repository permissions on a per-team basis. For example, you can specify that all teams within an organization have "Read and Write" access to repositories A and B, whereas only specific teams have "Admin" access.

Note that organization owners have full administrative access to all repositories within the organization.

To give a team access to a repository:

  1. Sign in to [Docker Hub](https://hub.docker.com).   2. Select **My Hub** and choose your organization.   3. In the **Teams** section, select the team you want to configure repository access for.   4. Select the **Permissions** tab and select a repository from the **Repository** drop-down.   5. Choose a permission from the **Permissions** drop-down list and select **Add**.

Organization owners can also assign members the editor role to grant partial administrative access. For more information on the editor role, see [Roles and permissions](https://docs.docker.com/enterprise/security/roles-and-permissions/).

### Permissions reference

  * `Read-only` access lets users view, search, and pull a private repository in the same way as they can a public repository.   * `Read & Write` access lets users pull, push, and view a repository. In addition, it lets users view, cancel, retry or trigger builds.   * `Admin` access lets users pull, push, view, edit, and delete a repository. You can also edit build settings and update the repositoryâs description, collaborator permissions, public/private visibility, and delete.

Permissions are cumulative. For example, if you have "Read & Write" permissions, you automatically have "Read-only" permissions.

The following table shows what each permission level allows users to do:

Action| Read-only| Read & Write| Admin   ---|---|---|---   Pull a Repository| â | â | â    View a Repository| â | â | â    Push a Repository| â| â | â    Edit a Repository| â| â| â    Delete a Repository| â| â| â    Update a Repository Description| â| â| â    View Builds| â | â | â    Cancel Builds| â| â | â    Retry Builds| â| â | â    Trigger Builds| â| â | â    Edit Build Settings| â| â| â       > Note >  > A user who hasn't verified their email address only has `Read-only` access to the repository, regardless of the rights their team membership has given them.

## View team permissions for all repositories

To view a team's permissions across all repositories:

  1. Sign in to [Docker Hub](https://hub.docker.com).   2. Select **My Hub** and choose your organization.   3. Select **Teams** and choose your team name.   4. Select the **Permissions** tab, where you can view the repositories this team can access.

## Delete a team

Organization owners can delete a team. When you remove a team from your organization, this action revokes member access to the team's permitted resources. It won't remove users from other teams that they belong to, and it won't delete any resources.

Admin Console  Docker Hub

  1. Sign in to [Docker Home](https://app.docker.com/) and select your organization.   2. Select **Teams**.   3. Select the **Actions** icon next to the name of the team you want to delete.   4. Select **Delete team**.   5. Review the confirmation message, then select **Delete**.

> Important >  > Organization management is moving to the Admin Console. >  > Manage members, team, settings, and activity logs in the Docker Admin Console. Access to these features in Docker Hub will end soon. Explore the [Admin Console](https://app.docker.com/admin).

  1. Sign in to [Docker Hub](https://hub.docker.com).   2. Select **My Hub** and choose your organization.   3. Select **Teams**.   4. Select the name of the team that you want to delete.   5. Select **Settings**.   6. Select **Delete Team**.   7. Review the confirmation message, then select **Delete**.

## More resources

  * [Video: Docker teams](https://youtu.be/WKlT1O-4Du8?feature=shared&t=348)   * [Video: Roles, teams, and repositories](https://youtu.be/WKlT1O-4Du8?feature=shared&t=435)