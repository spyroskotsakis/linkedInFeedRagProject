# Tabs | Docker Docs

**URL:** https://docs.docker.com/contribute/components/tabs/
**Word Count:** 146
**Links Count:** 65
**Scraped:** 2025-07-16 01:54:28
**Status:** completed

---

Back

[Contribute](https://docs.docker.com/contribute/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Tabs

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

The tabs component consists of two shortcodes:

  * `{{< tabs >}}`   * `{{< tab name="name of the tab" >}}`

The `{{< tabs >}}` shortcode is a parent, component, wrapping a number of `tabs`. Each `{{< tab >}}` is given a name using the `name` attribute.

You can optionally specify a `group` attribute for the `tabs` wrapper to indicate that a tab section should belong to a group of tabs. See Groups.

## Example

JavaScript  Go               console.log("hello world")               fmt.Println("hello world")

## Markup               {{< tabs >}}     {{< tab name="JavaScript" >}}          ```js     console.log("hello world")     ```          {{< /tab >}}     {{< tab name="Go" >}}          ```go     fmt.Println("hello world")     ```          {{< /tab >}}     {{< /tabs >}}

## Groups

You can optionally specify a tab group on the `tabs` shortcode. Doing so will synchronize the tab selection for all of the tabs that belong to the same group.

### Tab group example

The following example shows two tab sections belonging to the same group.

JavaScript  Go               console.log("hello world")               fmt.Println("hello world")

JavaScript  Go               const res = await fetch("/users/1")               resp, err := http.Get("/users/1")