# agents — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/agents.html
**Word Count:** 35
**Links Count:** 94
**Scraped:** 2025-07-21 08:28:38
**Status:** completed

---

# `agents`\#

**Classes**

[`agents.base.BedrockAgentsRunnable`](https://python.langchain.com/api_reference/aws/agents/langchain_aws.agents.base.BedrockAgentsRunnable.html#langchain_aws.agents.base.BedrockAgentsRunnable "langchain_aws.agents.base.BedrockAgentsRunnable") | Invoke a Bedrock Agent   ---|---   [`agents.base.BedrockInlineAgentsRunnable`](https://python.langchain.com/api_reference/aws/agents/langchain_aws.agents.base.BedrockInlineAgentsRunnable.html#langchain_aws.agents.base.BedrockInlineAgentsRunnable "langchain_aws.agents.base.BedrockInlineAgentsRunnable") | Invoke Bedrock Inline Agent as a Runnable.   [`agents.types.BedrockAgentAction`](https://python.langchain.com/api_reference/aws/agents/langchain_aws.agents.types.BedrockAgentAction.html#langchain_aws.agents.types.BedrockAgentAction "langchain_aws.agents.types.BedrockAgentAction") | AgentAction with session id information.   [`agents.types.BedrockAgentFinish`](https://python.langchain.com/api_reference/aws/agents/langchain_aws.agents.types.BedrockAgentFinish.html#langchain_aws.agents.types.BedrockAgentFinish "langchain_aws.agents.types.BedrockAgentFinish") | AgentFinish with session id information.   [`agents.types.GuardrailConfiguration`](https://python.langchain.com/api_reference/aws/agents/langchain_aws.agents.types.GuardrailConfiguration.html#langchain_aws.agents.types.GuardrailConfiguration "langchain_aws.agents.types.GuardrailConfiguration") |    [`agents.types.InlineAgentConfiguration`](https://python.langchain.com/api_reference/aws/agents/langchain_aws.agents.types.InlineAgentConfiguration.html#langchain_aws.agents.types.InlineAgentConfiguration "langchain_aws.agents.types.InlineAgentConfiguration") | Configurations for an Inline Agent.   [`agents.types.KnowledgebaseConfiguration`](https://python.langchain.com/api_reference/aws/agents/langchain_aws.agents.types.KnowledgebaseConfiguration.html#langchain_aws.agents.types.KnowledgebaseConfiguration "langchain_aws.agents.types.KnowledgebaseConfiguration") |       **Functions**

[`agents.utils.get_boto_session`](https://python.langchain.com/api_reference/aws/agents/langchain_aws.agents.utils.get_boto_session.html#langchain_aws.agents.utils.get_boto_session "langchain_aws.agents.utils.get_boto_session")\(\[...\]\) | Construct the boto3 session   ---|---   [`agents.utils.parse_agent_response`](https://python.langchain.com/api_reference/aws/agents/langchain_aws.agents.utils.parse_agent_response.html#langchain_aws.agents.utils.parse_agent_response "langchain_aws.agents.utils.parse_agent_response")\(response\) | Parses the raw response from Bedrock Agent