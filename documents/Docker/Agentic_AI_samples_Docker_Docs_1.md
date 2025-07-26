# Agentic AI samples | Docker Docs

**URL:** https://docs.docker.com/reference/samples/agentic-ai/
**Word Count:** 1143
**Links Count:** 483
**Scraped:** 2025-07-16 01:49:39
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# Agentic AI samples

Name| Description   ---|---   [Agent-to-Agent](https://github.com/docker/compose-for-agents/tree/main/a2a)| This app is a modular AI agent runtime built on Google's Agent Development Kit \(ADK\) and the A2A \(Agent-to-Agent\) protocol. It wraps a large language model \(LLM\)-based agent in an HTTP API and uses structured execution flows with streaming responses, memory, and tools. It is designed to make agents callable as network services and composable with other agents.   [ADK Multi-Agent Fact Checker](https://github.com/docker/compose-for-agents/tree/main/adk)| This project demonstrates a collaborative multi-agent system built with the Agent Development Kit \(ADK\), where a top-level Auditor agent coordinates the workflow to verify facts. The Critic agent gathers evidence via live internet searches using DuckDuckGo through the Model Context Protocol \(MCP\), while the Reviser agent analyzes and refines the conclusion using internal reasoning alone. The system showcases how agents with distinct roles and tools can collaborate under orchestration.   [DevDuck agents](https://github.com/docker/compose-for-agents/tree/main/adk-cerebras)| A multi-agent system for Go programming assistance built with Google Agent Development Kit \(ADK\). This project features a coordinating agent \(DevDuck\) that manages two specialized sub-agents \(Bob and Cerebras\) for different programming tasks.   [Agno](https://github.com/docker/compose-for-agents/tree/main/agno)| This app is a multi-agent orchestration system powered by LLMs \(like Qwen and OpenAI\) and connected to tools via a Model Control Protocol \(MCP\) gateway. Its purpose is to retrieve, summarize, and document GitHub issuesâautomatically creating Notion pages from the summaries. It also supports file content summarization from GitHub.   [CrewAI](https://github.com/docker/compose-for-agents/tree/main/crew-ai)| This project showcases an autonomous, multi-agent virtual marketing team built with CrewAI. It automates the creation of a high-quality, end-to-end marketing strategy â from research to copywriting â using task delegation, web search, and creative synthesis.   [SQL Agent with LangGraph](https://github.com/docker/compose-for-agents/tree/main/langgraph)| This project demonstrates a zero-config AI agent that uses LangGraph to answer natural language questions by querying a SQL database â all orchestrated with Docker Compose.   [Spring AI Brave Search Example - Model Context Protocol \(MCP\)](https://github.com/docker/compose-for-agents/tree/main/spring-ai)| This example demonstrates how to create a Spring AI Model Context Protocol \(MCP\) client that communicates with the Brave Search MCP Server. The application shows how to build an MCP client that enables natural language interactions with Brave Search, allowing you to perform internet searches through a conversational interface. This example uses Spring Boot autoconfiguration to set up the MCP client through configuration files.   [MCP UI with Vercel AI SDK](https://github.com/docker/compose-for-agents/tree/main/a2a)| Start an MCP UI application that uses the Vercel AI SDK to provide a chat interface for local models, provided by the Docker Model Runner, with access to MCPs from the Docker MCP Catalog.      ## Looking for more samples?

Visit the following GitHub repositories for more Docker samples.

  * [Awesome Compose](https://github.com/docker/awesome-compose): A curated repository containing over 30 Docker Compose samples. These samples offer a starting point for how to integrate different services using a Compose file.

  * [Docker Samples](https://github.com/dockersamples?q=&type=all&language=&sort=stargazers): A collection of over 30 repositories that offer sample containerized demo applications, tutorials, and labs.