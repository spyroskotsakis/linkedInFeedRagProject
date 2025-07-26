# count_tokens_approximately — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/messages/langchain_core.messages.utils.count_tokens_approximately.html
**Word Count:** 177
**Links Count:** 153
**Scraped:** 2025-07-21 07:53:34
**Status:** completed

---

# count\_tokens\_approximately\#

langchain\_core.messages.utils.count\_tokens\_approximately\(

    _messages : Iterable\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") | list\[str\] | tuple\[str, str\] | str | dict\[str, Any\]\]_,     _\*_ ,     _chars\_per\_token : float = 4.0_,     _extra\_tokens\_per\_message : float = 3.0_,     _count\_name : bool = True_, \) → int[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/messages/utils.html#count_tokens_approximately)\#     

Approximate the total number of tokens in messages.

The token count includes stringified message content, role, and \(optionally\) name. \- For AI messages, the token count also includes stringified tool calls. \- For tool messages, the token count also includes the tool call ID.

Parameters:     

  * **messages** \(_Iterable_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _|__list_ _\[__str_ _\]__|__tuple_ _\[__str_ _,__str_ _\]__|__str_ _|__dict_ _\[__str_ _,__Any_ _\]__\]_\) – List of messages to count tokens for.

  * **chars\_per\_token** \(_float_\) – Number of characters per token to use for the approximation. Default is 4 \(one token corresponds to ~4 chars for common English text\). You can also specify float values for more fine-grained control. See more here: <https://platform.openai.com/tokenizer>

  * **extra\_tokens\_per\_message** \(_float_\) – Number of extra tokens to add per message. Default is 3 \(special tokens, including beginning/end of message\). You can also specify float values for more fine-grained control. See more here: [openai/openai-cookbook](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb)

  * **count\_name** \(_bool_\) – Whether to include message names in the count. Enabled by default.

Returns:     

Approximate number of tokens in the messages.

Return type:     

int

Note

This is a simple approximation that may not match the exact token count used by specific models. For accurate counts, use model-specific tokenizers.

Warning

This function does not currently support counting image tokens.

Added in version 0.3.46.

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)