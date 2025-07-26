# MCP Catalog and Toolkit | Docker Docs

**URL:** https://docs.docker.com/ai/mcp-catalog-and-toolkit/
**Word Count:** 1291
**Links Count:** 638
**Scraped:** 2025-07-16 01:47:50
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Docker MCP Catalog and Toolkit

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

The Model Context Protocol \(MCP\) is a modern standard that transforms AI agents from passive responders into action-oriented systems. By standardizing how tools are described, discovered, and invoked, MCP enables agents to securely query APIs, access data, and execute services across diverse environments.

As agents move into production, MCP solves common integration challenges â interoperability, reliability, and security â by providing a consistent, decoupled, and scalable interface between agents and tools. Just as containers redefined software deployment, MCP is reshaping how AI systems interact with the world.

> **Example** >  > In simple terms, an MCP server is a way for an LLM to interact with an external system. >  > For example: If you ask a model to create a meeting, it needs to communicate with your calendar app to do that. An MCP server for your calendar app provides _tools_ that perform atomic actions, such as: "getting the details of a meeting" or "creating a new meeting".

## What is Docker MCP Catalog and Toolkit?

Docker MCP Catalog and Toolkit is a comprehensive solution for securely building, sharing, and running MCP tools. It simplifies the developer experience across these key areas:

  * Discovery: A central catalog with verified, versioned tools   * Credential Management: OAuth-based and secure by default   * Execution: Tools run in isolated, containerized environments   * Portability: Use MCP tools across Claude, Cursor, VS Code, and more â no code changes needed

With Docker Hub and the MCP Toolkit, you can:

  * Launch MCP servers in seconds   * Add tools via CLI or GUI   * Rely on Docker's pull-based infrastructure for trusted delivery

### [MCP CatalogLearn about the benefits of the MCP Catalog, how you can use it, and how you can contribute](https://docs.docker.com/ai/mcp-catalog-and-toolkit/catalog/)

### [MCP ToolkitLearn about the MCP toolkit to manage MCP servers and clients](https://docs.docker.com/ai/mcp-catalog-and-toolkit/toolkit/)