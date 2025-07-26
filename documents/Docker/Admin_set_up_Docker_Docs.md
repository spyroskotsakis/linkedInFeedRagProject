# Admin set up | Docker Docs

**URL:** https://docs.docker.com/guides/admin-set-up
**Word Count:** 584
**Links Count:** 61
**Scraped:** 2025-07-16 02:04:23
**Status:** completed

---

Back

[Guides](https://docs.docker.com/guides/)

  * [Get started](https://docs.docker.com/get-started/)   * [Manuals](https://docs.docker.com/manuals/)   * [Reference](https://docs.docker.com/reference/)

* * *

[Set up your company for success with Docker](https://docs.docker.com/guides/admin-set-up/)

Get the most out of Docker by streamlining workflows, standardizing development environments, and ensuring smooth deployments across your company.

[ Administration](https://docs.docker.com/tags/admin/)

20 minutes

[1](https://docs.docker.com/guides/admin-set-up/comms-and-info-gathering/)

[Communication and information gathering](https://docs.docker.com/guides/admin-set-up/comms-and-info-gathering/)

[2](https://docs.docker.com/guides/admin-set-up/finalize-plans-and-setup/)

[Finalize plans and begin setup](https://docs.docker.com/guides/admin-set-up/finalize-plans-and-setup/)

[3](https://docs.docker.com/guides/admin-set-up/testing/)

[Testing](https://docs.docker.com/guides/admin-set-up/testing/)

[4](https://docs.docker.com/guides/admin-set-up/deploy/)

[Deploy](https://docs.docker.com/guides/admin-set-up/deploy/)

Resources:

  * [Overview of Administration in Docker](https://docs.docker.com/admin/)   * [Single sign-on](https://docs.docker.com/security/for-admins/single-sign-on/)   * [Enforce sign-in](https://docs.docker.com/security/for-admins/enforce-sign-in/)   * [Roles and permissions](https://docs.docker.com/security/for-admins/roles-and-permissions/)   * [Settings Management](https://docs.docker.com/security/for-admins/hardened-desktop/settings-management/)   * [Registry Access Management](https://docs.docker.com/security/for-admins/hardened-desktop/registry-access-management/)   * [Image Access Management](https://docs.docker.com/security/for-admins/hardened-desktop/image-access-management/)   * [Docker subscription information](https://docs.docker.com/subscription/details/)

[Â« Back to all guides](https://docs.docker.com/guides/)

# Set up your company for success with Docker

Table of contents

* * *

Docker's tools provide a scalable, secure platform that empowers your developers to create, ship, and run applications faster. As an administrator, you have the ability to streamline workflows, standardize development environments, and ensure smooth deployments across your organization.

By configuring Docker products to suit your companyâs needs, you can optimize performance, simplify user management, and maintain control over resources. This guide will help you set up and configure Docker products to maximize productivity and success for your team whilst meeting compliance and security policies

## Whoâs this for?

  * Administrators responsible for managing Docker environments within their organization   * IT leaders looking to streamline development and deployment workflows   * Teams aiming to standardize application environments across multiple users   * Organizations seeking to optimize their use of Docker products for greater scalability and efficiency   * Organizations with [Docker Business subscriptions](https://www.docker.com/pricing/).

## What youâll learn

  * The importance of signing in to the company's Docker organization for access to usage data and enhanced functionality.   * How to standardize Docker Desktop versions and settings to create a consistent baseline for all users, while allowing flexibility for advanced developers.   * Strategies for implementing Dockerâs security configurations to meet company IT and software development security requirements without hindering developer productivity.

## Features covered

  * Organizations. These are the core structure for managing your Docker environment, grouping users, teams, and image repositories. Your organization was created with your subscription and is managed by one or more Owners. Users signed into the organization are assigned seats based on the purchased subscription.   * Enforce sign-in. By default, Docker Desktop does not require sign-in. However, you can configure settings to enforce this and ensure your developers sign in to your Docker organization.   * SSO. Without SSO, user management in a Docker organization is manual. Setting up an SSO connection between your identity provider and Docker ensures compliance with your security policy and automates user provisioning. Adding SCIM further automates user provisioning and de-provisioning.   * General and security settings. Configuring key settings will ensure smooth onboarding and usage of Docker products within your environment. Additionally, you can enable security features based on your company's specific security needs.

## Who needs to be involved?

  * Docker organization owner: A Docker organization owner must be involved in the process and will be required for several key steps.   * DNS team: The DNS team is needed during the SSO setup to verify the company domain.   * MDM team: Responsible for distributing Docker-specific configuration files to developer machines.   * Identity Provider team: Required for configuring the identity provider and establishing the SSO connection during setup.   * Development lead: A development lead with knowledge of Docker configurations to help establish a baseline for developer settings.   * IT team: An IT representative familiar with company desktop policies to assist with aligning Docker configuration to those policies.   * Infosec: A security team member with knowledge of company development security policies to help configure security features.   * Docker testers: A small group of developers to test the new settings and configurations before full deployment.

## Tools integration

Okta,Â Entra ID SAML 2.0,Â Azure Connect \(OIDC\), MDM solutions like Intune

## Modules

  1. [Communication and information gathering](https://docs.docker.com/guides/admin-set-up/comms-and-info-gathering/)

Gather your company's requirements from key stakeholders and communicate to your developers.

  2. [Finalize plans and begin setup](https://docs.docker.com/guides/admin-set-up/finalize-plans-and-setup/)

Collaborate with your MDM team to distribute configurations and set up SSO and Docker product trials.

  3. [Testing](https://docs.docker.com/guides/admin-set-up/testing/)

Test your Docker setup.

  4. [Deploy](https://docs.docker.com/guides/admin-set-up/deploy/)

Deploy your Docker setup across your company.