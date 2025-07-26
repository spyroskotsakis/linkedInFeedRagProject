# llms — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/llms.html
**Word Count:** 49
**Links Count:** 94
**Scraped:** 2025-07-21 08:44:55
**Status:** completed

---

# `llms`\#

**Classes**

[`llms.bedrock.AnthropicTool`](https://python.langchain.com/api_reference/aws/llms/langchain_aws.llms.bedrock.AnthropicTool.html#langchain_aws.llms.bedrock.AnthropicTool "langchain_aws.llms.bedrock.AnthropicTool") |    ---|---   [`llms.bedrock.BedrockBase`](https://python.langchain.com/api_reference/aws/llms/langchain_aws.llms.bedrock.BedrockBase.html#langchain_aws.llms.bedrock.BedrockBase "langchain_aws.llms.bedrock.BedrockBase") | Base class for Bedrock models.   [`llms.bedrock.BedrockLLM`](https://python.langchain.com/api_reference/aws/llms/langchain_aws.llms.bedrock.BedrockLLM.html#langchain_aws.llms.bedrock.BedrockLLM "langchain_aws.llms.bedrock.BedrockLLM") | Bedrock models.   [`llms.bedrock.LLMInputOutputAdapter`](https://python.langchain.com/api_reference/aws/llms/langchain_aws.llms.bedrock.LLMInputOutputAdapter.html#langchain_aws.llms.bedrock.LLMInputOutputAdapter "langchain_aws.llms.bedrock.LLMInputOutputAdapter")\(\) | Adapter class to prepare the inputs from Langchain to a format that LLM model expects.   [`llms.sagemaker_endpoint.LLMContentHandler`](https://python.langchain.com/api_reference/aws/llms/langchain_aws.llms.sagemaker_endpoint.LLMContentHandler.html#langchain_aws.llms.sagemaker_endpoint.LLMContentHandler "langchain_aws.llms.sagemaker_endpoint.LLMContentHandler")\(\) | Content handler for LLM class.   [`llms.sagemaker_endpoint.LineIterator`](https://python.langchain.com/api_reference/aws/llms/langchain_aws.llms.sagemaker_endpoint.LineIterator.html#langchain_aws.llms.sagemaker_endpoint.LineIterator "langchain_aws.llms.sagemaker_endpoint.LineIterator")\(stream\) | A helper class for parsing the byte stream input.   [`llms.sagemaker_endpoint.SagemakerEndpoint`](https://python.langchain.com/api_reference/aws/llms/langchain_aws.llms.sagemaker_endpoint.SagemakerEndpoint.html#langchain_aws.llms.sagemaker_endpoint.SagemakerEndpoint "langchain_aws.llms.sagemaker_endpoint.SagemakerEndpoint") | Sagemaker Inference Endpoint models.      **Functions**

[`llms.bedrock.extract_tool_calls`](https://python.langchain.com/api_reference/aws/llms/langchain_aws.llms.bedrock.extract_tool_calls.html#langchain_aws.llms.bedrock.extract_tool_calls "langchain_aws.llms.bedrock.extract_tool_calls")\(content\) |    ---|---   [`llms.sagemaker_endpoint.enforce_stop_tokens`](https://python.langchain.com/api_reference/aws/llms/langchain_aws.llms.sagemaker_endpoint.enforce_stop_tokens.html#langchain_aws.llms.sagemaker_endpoint.enforce_stop_tokens "langchain_aws.llms.sagemaker_endpoint.enforce_stop_tokens")\(...\) | Cut off the text as soon as any stop words occur.