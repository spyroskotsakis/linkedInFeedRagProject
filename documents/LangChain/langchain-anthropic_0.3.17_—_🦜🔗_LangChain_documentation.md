# langchain-anthropic: 0.3.17 — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/anthropic/index.html
**Word Count:** 44
**Links Count:** 84
**Scraped:** 2025-07-21 07:48:33
**Status:** completed

---

# langchain-anthropic: 0.3.17\#

## [chat\_models](https://python.langchain.com/api_reference/anthropic/chat_models.html#langchain-anthropic-chat-models)\#

**Classes**

[`chat_models.AnthropicTool`](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.AnthropicTool.html#langchain_anthropic.chat_models.AnthropicTool "langchain_anthropic.chat_models.AnthropicTool") | Anthropic tool definition.   ---|---   [`chat_models.ChatAnthropic`](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html#langchain_anthropic.chat_models.ChatAnthropic "langchain_anthropic.chat_models.ChatAnthropic") | Anthropic chat models.      **Functions**

[`chat_models.convert_to_anthropic_tool`](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.convert_to_anthropic_tool.html#langchain_anthropic.chat_models.convert_to_anthropic_tool "langchain_anthropic.chat_models.convert_to_anthropic_tool")\(tool\) | Convert a tool-like object to an Anthropic tool definition.   ---|---      **Deprecated classes**

[`chat_models.ChatAnthropicMessages`](https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropicMessages.html#langchain_anthropic.chat_models.ChatAnthropicMessages "langchain_anthropic.chat_models.ChatAnthropicMessages") |    ---|---      ## [experimental](https://python.langchain.com/api_reference/anthropic/experimental.html#langchain-anthropic-experimental)\#

**Functions**

[`experimental.get_system_message`](https://python.langchain.com/api_reference/anthropic/experimental/langchain_anthropic.experimental.get_system_message.html#langchain_anthropic.experimental.get_system_message "langchain_anthropic.experimental.get_system_message")\(tools\) | Generate a system message that describes the available tools.   ---|---      **Deprecated classes**

[`experimental.ChatAnthropicTools`](https://python.langchain.com/api_reference/anthropic/experimental/langchain_anthropic.experimental.ChatAnthropicTools.html#langchain_anthropic.experimental.ChatAnthropicTools "langchain_anthropic.experimental.ChatAnthropicTools") |    ---|---      ## [llms](https://python.langchain.com/api_reference/anthropic/llms.html#langchain-anthropic-llms)\#

**Classes**

[`llms.AnthropicLLM`](https://python.langchain.com/api_reference/anthropic/llms/langchain_anthropic.llms.AnthropicLLM.html#langchain_anthropic.llms.AnthropicLLM "langchain_anthropic.llms.AnthropicLLM") | Anthropic large language model.   ---|---      **Deprecated classes**

[`llms.Anthropic`](https://python.langchain.com/api_reference/anthropic/llms/langchain_anthropic.llms.Anthropic.html#langchain_anthropic.llms.Anthropic "langchain_anthropic.llms.Anthropic") |    ---|---      ## [output\_parsers](https://python.langchain.com/api_reference/anthropic/output_parsers.html#langchain-anthropic-output-parsers)\#

**Classes**

[`output_parsers.ToolsOutputParser`](https://python.langchain.com/api_reference/anthropic/output_parsers/langchain_anthropic.output_parsers.ToolsOutputParser.html#langchain_anthropic.output_parsers.ToolsOutputParser "langchain_anthropic.output_parsers.ToolsOutputParser") | Output parser for tool calls.   ---|---      **Functions**

[`output_parsers.extract_tool_calls`](https://python.langchain.com/api_reference/anthropic/output_parsers/langchain_anthropic.output_parsers.extract_tool_calls.html#langchain_anthropic.output_parsers.extract_tool_calls "langchain_anthropic.output_parsers.extract_tool_calls")\(content\) | Extract tool calls from a list of content blocks.   ---|---