# MCP | Docker Docs

**URL:** https://docs.docker.com/ai/gordon/mcp
**Word Count:** 1121
**Links Count:** 640
**Scraped:** 2025-07-16 02:03:45
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# MCP

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## What is MCP?

[Model Context Protocol](https://modelcontextprotocol.io/introduction) \(MCP\) is an open protocol that standardizes how applications provide context and extra functionality to large language models. MCP functions as a client-server protocol, where the client, for example an application like Gordon, sends requests, and the server processes those requests to deliver the necessary context to the AI. This context may be gathered by the MCP server by executing some code to perform an action and getting the result of the action, calling external APIs, etc.

Gordon, along with other MCP clients like Claude Desktop or Cursor, can interact with MCP servers running as containers.

### [Built-in toolsUse the built-in tools.](https://docs.docker.com/ai/gordon/mcp/built-in-tools)

### [MCP configurationConfigure MCP tools on a per-project basis.](https://docs.docker.com/ai/gordon/mcp/yaml)