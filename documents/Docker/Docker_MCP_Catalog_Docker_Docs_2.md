# Docker MCP Catalog | Docker Docs

**URL:** https://docs.docker.com/ai/mcp-catalog-and-toolkit/catalog/
**Word Count:** 1309
**Links Count:** 654
**Scraped:** 2025-07-16 01:51:20
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Docker MCP Catalog

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

The [Docker MCP Catalog](https://hub.docker.com/mcp) is a centralized, trusted registry for discovering, sharing, and running MCP-compatible tools. Seamlessly integrated into Docker Hub, it offers verified, versioned, and curated MCP servers packaged as Docker images. The catalog is also available in Docker Desktop.

The catalog solves common MCP server challenges:

  * Environment conflicts: Tools often need specific runtimes that may clash with existing setups.   * Lack of isolation: Traditional setups risk exposing the host system.   * Setup complexity: Manual installation and configuration result in slow adoption.   * Inconsistency across platforms: Tools may behave unpredictably on different OSes.

With Docker, each MCP server runs as a self-contained container so it is portable, isolated, and consistent. You can launch tools instantly using Docker CLI or Docker Desktop, without worrying about dependencies or compatibility.

## Key features

  * Over 100 verified MCP servers in one place   * Publisher verification and versioned releases   * Pull-based distribution using Docker's infrastructure   * Tools provided by partners such as New Relic, Stripe, Grafana, and more

## How it works

Each tool in the MCP Catalog is packaged as a Docker image with metadata:

  * Discover tools via Docker Hub under the `mcp/` namespace.   * Connect tools to their preferred agents with simple configuration through the [MCP Toolkit](https://docs.docker.com/ai/mcp-catalog-and-toolkit/toolkit/).   * Pull and run tools using Docker Desktop or the CLI.

Each catalog entry displays:

  * Tool description and metadata   * Version history   * List of tools provided by the MCP server   * Example configuration for agent integration

## Use an MCP server from the catalog

To use an MCP server from the catalog, see [MCP toolkit](https://docs.docker.com/ai/mcp-catalog-and-toolkit/toolkit/).

## Contribute an MCP server to the catalog

The MCP server registry is available at <https://github.com/docker/mcp-registry>. To submit an MCP server, follow the [contributing guidelines](https://github.com/docker/mcp-registry/blob/main/CONTRIBUTING.md).

When your pull request is reviewed and approved, your MCP server is available in 24 hours on:

  * Docker Desktop's [MCP Toolkit feature](https://docs.docker.com/ai/mcp-catalog-and-toolkit/toolkit/)   * The [Docker MCP catalog](https://hub.docker.com/mcp)   * The [Docker Hub](https://hub.docker.com/u/mcp) `mcp` namespace \(for MCP servers built by Docker\)