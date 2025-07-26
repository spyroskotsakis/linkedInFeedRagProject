# Use multiple Compose files | Docker Docs

**URL:** https://docs.docker.com/compose/how-tos/multiple-compose-files/
**Word Count:** 1206
**Links Count:** 639
**Scraped:** 2025-07-16 01:49:17
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Use multiple Compose files

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

* * *

This section contains information on the ways you can work with multiple Compose files.

Using multiple Compose files lets you customize a Compose application for different environments or workflows. This is useful for large applications that may use dozens of containers, with ownership distributed across multiple teams. For example, if your organization or team uses a monorepo, each team may have their own âlocalâ Compose file to run a subset of the application. They then need to rely on other teams to provide a reference Compose file that defines the expected way to run their own subset. Complexity moves from the code in to the infrastructure and the configuration file.

The quickest way to work with multiple Compose files is to [merge](https://docs.docker.com/compose/how-tos/multiple-compose-files/merge/) Compose files using the `-f` flag in the command line to list out your desired Compose files. However, [merging rules](https://docs.docker.com/compose/how-tos/multiple-compose-files/merge/#merging-rules) means this can soon get quite complicated.

Docker Compose provides two other options to manage this complexity when working with multiple Compose files. Depending on your project's needs, you can:

  * [Extend a Compose file](https://docs.docker.com/compose/how-tos/multiple-compose-files/extends/) by referring to another Compose file and selecting the bits you want to use in your own application, with the ability to override some attributes.   * [Include other Compose files](https://docs.docker.com/compose/how-tos/multiple-compose-files/include/) directly in your Compose file.