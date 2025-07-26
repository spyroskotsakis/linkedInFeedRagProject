# Tables | Docker Docs

**URL:** https://docs.docker.com/contribute/components/tables/
**Word Count:** 188
**Links Count:** 70
**Scraped:** 2025-07-16 01:54:28
**Status:** completed

---

Back

[Contribute](https://docs.docker.com/contribute/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Tables

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Example

### Basic table

Permission level| Access   ---|---   **Bold** or _italic_ within a table cell. Next cell is empty on purpose.|    | Previous cell is empty. A `--flag` in mono text.   Read| Pull   Read/Write| Pull, push   Admin| All of the above, plus update description, create, and delete      ### Feature-support table

Platform| x86\_64 / amd64   ---|---   Ubuntu| â    Debian| â    Fedora|    Arch \(btw\)| â       ## Markdown

### Basic table               | Permission level                                                         | Access                                                        |     | :----------------------------------------------------------------------- | :------------------------------------------------------------ |     | **Bold** or _italic_ within a table cell. Next cell is empty on purpose. |                                                               |     |                                                                          | Previous cell is empty. A `--flag` in mono text.              |     | Read                                                                     | Pull                                                          |     | Read/Write                                                               | Pull, push                                                    |     | Admin                                                                    | All of the above, plus update description, create, and delete |

The alignment of the cells in the source doesn't really matter. The ending pipe character is optional \(unless the last cell is supposed to be empty\).

### Feature-support table               | Platform   | x86_64 / amd64 |     | :--------- | :------------: |     | Ubuntu     |       â       |     | Debian     |       â       |     | Fedora     |                |     | Arch (btw) |       â       |