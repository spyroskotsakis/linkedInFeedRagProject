# agents — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/agents.html
**Word Count:** 170
**Links Count:** 104
**Scraped:** 2025-07-21 07:54:58
**Status:** completed

---

# `agents`\#

Schema definitions for representing agent actions, observations, and return values.

**ATTENTION** The schema definitions are provided for backwards compatibility.

> New agents should be built using the langgraph library \([langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)\)\), which provides a simpler and more flexible way to define agents. >  > Please see the migration guide for information on how to migrate existing agents to modern langgraph agents: <https://python.langchain.com/docs/how_to/migrate_agent/>

Agents use language models to choose a sequence of actions to take.

A basic agent works in the following manner:

  1. Given a prompt an agent uses an LLM to request an action to take \(e.g., a tool to run\).

  2. The agent executes the action \(e.g., runs the tool\), and receives an observation.

  3. The agent returns the observation to the LLM, which can then be used to generate the next action.

  4. When the agent reaches a stopping condition, it returns a final return value.

The schemas for the agents themselves are defined in langchain.agents.agent.

**Classes**

[`agents.AgentAction`](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction") | Represents a request to execute an action by an agent.   ---|---   [`agents.AgentActionMessageLog`](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentActionMessageLog.html#langchain_core.agents.AgentActionMessageLog "langchain_core.agents.AgentActionMessageLog") | Representation of an action to be executed by an agent.   [`agents.AgentFinish`](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentFinish.html#langchain_core.agents.AgentFinish "langchain_core.agents.AgentFinish") | Final return value of an ActionAgent.   [`agents.AgentStep`](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentStep.html#langchain_core.agents.AgentStep "langchain_core.agents.AgentStep") | Result of running an AgentAction.