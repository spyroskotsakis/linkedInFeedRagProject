# parse_agent_response — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/agents/langchain_aws.agents.utils.parse_agent_response.html
**Word Count:** 27
**Links Count:** 93
**Scraped:** 2025-07-21 08:28:38
**Status:** completed

---

# parse\_agent\_response\#

langchain\_aws.agents.utils.parse\_agent\_response\(

    _response : Any_, \) → List\[[BedrockAgentAction](https://python.langchain.com/api_reference/aws/agents/langchain_aws.agents.types.BedrockAgentAction.html#langchain_aws.agents.types.BedrockAgentAction "langchain_aws.agents.types.BedrockAgentAction")\] | [BedrockAgentFinish](https://python.langchain.com/api_reference/aws/agents/langchain_aws.agents.types.BedrockAgentFinish.html#langchain_aws.agents.types.BedrockAgentFinish "langchain_aws.agents.types.BedrockAgentFinish")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/agents/utils.html#parse_agent_response)\#     

Parses the raw response from Bedrock Agent

Parameters:     

**response** \(_Any_\) – The raw response from Bedrock Agent

Return type:     

_List_\[[_BedrockAgentAction_](https://python.langchain.com/api_reference/aws/agents/langchain_aws.agents.types.BedrockAgentAction.html#langchain_aws.agents.types.BedrockAgentAction "langchain_aws.agents.types.BedrockAgentAction")\] | [_BedrockAgentFinish_](https://python.langchain.com/api_reference/aws/agents/langchain_aws.agents.types.BedrockAgentFinish.html#langchain_aws.agents.types.BedrockAgentFinish "langchain_aws.agents.types.BedrockAgentFinish")

Returns     

Either a BedrockAgentAction or a BedrockAgentFinish

__On this page