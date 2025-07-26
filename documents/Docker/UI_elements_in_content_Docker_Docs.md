# UI elements in content | Docker Docs

**URL:** https://docs.docker.com/contribute/ui
**Word Count:** 344
**Links Count:** 66
**Scraped:** 2025-07-16 02:04:38
**Status:** completed

---

Back

[Contribute](https://docs.docker.com/contribute/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)   * [Reference](https://docs.docker.com/reference/)

* * *

# UI elements in content

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Use this guide when writing documentation that refers to buttons, fields, menus, dialogs, or other user interface \(UI\) elements. It explains how to format UI terms, write task-focused instructions, and refer to common UI patterns consistently and clearly.

## Format UI element names

Use bold formatting for the visible names of UI elements:

  * Buttons   * Dialogs   * Windows   * Tabs   * Menu items   * List items   * Form labels   * Section headings

For example:

_Select**Create** , then fill out the **Name** field._

Do not bold product names or features unless they appear exactly as a label in the UI.

### Capitalization

  * Follow the capitalization as it appears in the UI.   * If UI labels are all uppercase or inconsistent, use sentence case in your docs for readability.

## Write task-focused instructions

When possible, guide users based on what theyâre trying to do, not just what they should select. This makes docs more goal-oriented and adaptable to UI changes.

Do this| Avoid this   ---|---   Expand the **Advanced options** section.| Select the zippy to expand the **Advanced options** section.   Choose a base image for your container.| Select a dropdown and pick something.      ## Use correct prepositions with UI elements

Choose the right preposition based on the type of UI element you're referencing.

Preposition| Use with...| Example   ---|---|---   **in**|  dialogs, fields, lists, menus, panes, windows| In the **Name** field, enter your project name.   **on**|  pages, tabs, toolbars| On the **Settings** tab, select **General**.      ## Use consistent UI element terms

Use these standard terms when referring to elements in Docker products:

Preferred Term| Use When Referring To...   ---|---   **button**|  A clickable action element \(e.g., **Start**\)   **field**|  A place to enter text or select a value   **menu** / **menu item**|  A drop-down or navigation option   **drop-down**|  A drop-down menu item   **context switcher**|  Specific to toggling on cloud mode   **tab**|  A selectable view within a window or page   **dialog**|  A popup window for confirmations or options   **section**|  A logical grouping of content on a page   **list** / **list item**|  A scrollable list of selectable entries   **toggle**|  A binary control \(on/off\)   **checkbox**|  A multi-select control   **tooltip**|  Text that appears on hover      Finally, instead of saying âclick the control,â say âselect the **Create** button.â