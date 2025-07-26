# Domains | Docker Docs

**URL:** https://docs.docker.com/security/faqs/single-sign-on/domain-faqs
**Word Count:** 1337
**Links Count:** 654
**Scraped:** 2025-07-16 01:59:00
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# FAQs for SSO and domains

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

### Can I add sub-domains?

Yes, you can add sub-domains to your SSO connection, however all email addresses should also be on that domain. Verify that your DNS provider supports multiple TXT records for the same domain.

### Can the DNS provider configure it once for one-time verification and remove it later or will it be needed permanently?

You can do it one time to add the domain to a connection. If your organization ever changes IdPs and has to set up SSO again, your DNS provider will need to verify again.

### Is adding domain required to configure SSO? What domains should I be adding? And how do I add it?

Adding and verifying a domain is required to enable and enforce SSO. See [Configure single sign-on](https://docs.docker.com/enterprise/security/single-sign-on/configure/) for more information. This should include all email domains users will use to access Docker. Public domains, for example `gmail.com` or `outlook.com`, are not permitted. Also, the email domain should be set as the primary email.

### Is IdP-initiated authentication supported?

IdP-initiated authentication isn't supported by Docker SSO. Users must initiate sign-in through Docker Desktop or Hub.

### Can I verify the same domain on multiple organizations?

You can't verify the same domain for multiple orgnaizations at the organization level. If you want to verify one domain for multiple organizations, you must have a Docker Business subscription, and [create a company](https://docs.docker.com/admin/company/new-company/). A company enables centralized management of organizations and allows domain verification at the company level.