# Cards | Docker Docs

**URL:** https://docs.docker.com/contribute/components/cards/
**Word Count:** 275
**Links Count:** 67
**Scraped:** 2025-07-16 01:49:59
**Status:** completed

---

Back

[Contribute](https://docs.docker.com/contribute/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Cards

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Cards can be added to a page using the `card` shortcode. The parameters for this shortcode are:

Parameter| Description   ---|---   title| The title of the card   icon| The icon slug of the card   image| Use a custom image instead of an icon \(mutually exclusive with icon\)   link| \(Optional\) The link target of the card, when clicked   description| A description text, in Markdown      > Note >  > There's a known limitation with the Markdown description of cards, in that they can't contain relative links, pointing to other .md documents. Such links won't render correctly. Instead, use an absolute link to the URL path of the page that you want to link to. >  > For example, instead of linking to `../install/linux.md`, write: `/engine/install/linux/`.

## Example

### [Get your Docker onBuild, share, and run your apps with Docker](https://docs.docker.com/)

## Markup               {{< card       title="Get your Docker on"       icon=favorite       link=https://docs.docker.com/       description="Build, share, and run your apps with Docker"     >}}

### Grid

There's also a built-in `grid` shortcode that generates a... well, grid... of cards. The grid size is 3x3 on large screens, 2x2 on medium, and single column on small.

### [Docker DesktopDocker on your Desktop.](https://docs.docker.com/desktop/)

### [Docker EngineVrrrrooooommm](https://docs.docker.com/engine/)

### [Docker BuildClang bang](https://docs.docker.com/build/)

### [Docker ComposeFiggy\!](https://docs.docker.com/compose/)

### [Docker Hubso much content, oh wow](https://docs.docker.com/docker-hub/)

Grid is a separate shortcode from `card`, but it implements the same component under the hood. The markup you use to insert a grid is slightly unconventional. The grid shortcode takes no arguments. All it does is let you specify where on a page you want your grid to appear.               {{< grid >}}

The data for the grid is defined in the front matter of the page, under the `grid` key, as follows:               # front matter section of a page     title: some page     grid:       - title: "Docker Engine"         description: Vrrrrooooommm         icon: "developer_board"         link: "/engine/"       - title: "Docker Build"         description: Clang bang         icon: "build"         link: "/build/"