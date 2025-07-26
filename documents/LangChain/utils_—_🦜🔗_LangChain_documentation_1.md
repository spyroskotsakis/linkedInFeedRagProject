# utils — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/utils.html
**Word Count:** 72
**Links Count:** 90
**Scraped:** 2025-07-21 08:28:38
**Status:** completed

---

# `utils`\#

**Classes**

[`utils.ContentHandlerBase`](https://python.langchain.com/api_reference/aws/utils/langchain_aws.utils.ContentHandlerBase.html#langchain_aws.utils.ContentHandlerBase "langchain_aws.utils.ContentHandlerBase")\(\) | A handler class to transform input from LLM and BaseChatModel to a   ---|---      **Functions**

[`utils.anthropic_tokens_supported`](https://python.langchain.com/api_reference/aws/utils/langchain_aws.utils.anthropic_tokens_supported.html#langchain_aws.utils.anthropic_tokens_supported "langchain_aws.utils.anthropic_tokens_supported")\(\) | Check if all requirements for Anthropic count\_tokens\(\) are met.   ---|---   [`utils.create_aws_client`](https://python.langchain.com/api_reference/aws/utils/langchain_aws.utils.create_aws_client.html#langchain_aws.utils.create_aws_client "langchain_aws.utils.create_aws_client")\(service\_name\[, ...\]\) | Helper function to validate AWS credentials and create an AWS client.   [`utils.enforce_stop_tokens`](https://python.langchain.com/api_reference/aws/utils/langchain_aws.utils.enforce_stop_tokens.html#langchain_aws.utils.enforce_stop_tokens "langchain_aws.utils.enforce_stop_tokens")\(text, stop\) | Cut off the text as soon as any stop words occur.   [`utils.get_num_tokens_anthropic`](https://python.langchain.com/api_reference/aws/utils/langchain_aws.utils.get_num_tokens_anthropic.html#langchain_aws.utils.get_num_tokens_anthropic "langchain_aws.utils.get_num_tokens_anthropic")\(text\) | Get the number of tokens in a string of text.   [`utils.get_token_ids_anthropic`](https://python.langchain.com/api_reference/aws/utils/langchain_aws.utils.get_token_ids_anthropic.html#langchain_aws.utils.get_token_ids_anthropic "langchain_aws.utils.get_token_ids_anthropic")\(text\) | Get the token ids for a string of text.   [`utils.thinking_in_params`](https://python.langchain.com/api_reference/aws/utils/langchain_aws.utils.thinking_in_params.html#langchain_aws.utils.thinking_in_params "langchain_aws.utils.thinking_in_params")\(params\) | Check if the thinking parameter is enabled in the request.