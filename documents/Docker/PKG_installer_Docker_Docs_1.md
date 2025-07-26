# PKG installer | Docker Docs

**URL:** https://docs.docker.com/enterprise/enterprise-deployment/pkg-install-and-configure/
**Word Count:** 1252
**Links Count:** 651
**Scraped:** 2025-07-16 01:47:07
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# PKG installer

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Subscription: Business

Requires: Docker Desktop [4.36](https://docs.docker.com/desktop/release-notes/#4360) and later

For: Administrators

The PKG package supports various MDM \(Mobile Device Management\) solutions, making it ideal for bulk installations and eliminating the need for manual setups by individual users. With this package, IT administrators can ensure standardized, policy-driven installations of Docker Desktop, enhancing efficiency and software management across their organizations.

## Install interactively

  1. In [Docker Home](http://app.docker.com), choose your organization.   2. Select **Admin Console** , then **Enterprise deployment**.   3. From the **macOS** tab, select the **Download PKG installer** button.   4. Once downloaded, double-click `Docker.pkg` to run the installer.   5. Follow the instructions on the installation wizard to authorize the installer and proceed with the installation.      * **Introduction** : Select **Continue**.      * **License** : Review the license agreement and select **Agree**.      * **Destination Select** : This step is optional. It is recommended that you keep the default installation destination \(usually `Macintosh HD`\). Select **Continue**.      * **Installation Type** : Select **Install**.      * **Installation** : Authenticate using your administrator password or Touch ID.      * **Summary** : When the installation completes, select **Close**.

> Note >  > When installing Docker Desktop with the PKG, in-app updates are automatically disabled. This ensures organizations can maintain version consistency and prevent unapproved updates. For Docker Desktop installed with the `.dmg` installer, in-app updates remain supported. >  > Docker Desktop notifies you when an update is available. To update Docker Desktop, download the latest installer from the Docker Admin Console. Navigate to the **Enterprise deployment** page. >  > To keep up to date with new releases, check the [release notes](https://docs.docker.com/desktop/release-notes/) page.

## Install from the command line

  1. In [Docker Home](http://app.docker.com), choose your organization.

  2. Select **Admin Console** , then **Enterprise deployment**.

  3. From the **macOS** tab, select the **Download PKG installer** button.

  4. From your terminal, run the following command:                    $ sudo installer -pkg "/path/to/Docker.pkg" -target /Applications          

## Additional resources

  * See how you can deploy Docker Desktop for Mac using [Intune](https://docs.docker.com/enterprise/enterprise-deployment/use-intune/) or [Jamf Pro](https://docs.docker.com/enterprise/enterprise-deployment/use-jamf-pro/)   * Explore how to [Enforce sign-in](https://docs.docker.com/enterprise/security/enforce-sign-in/methods/#plist-method-mac-only) for your users.