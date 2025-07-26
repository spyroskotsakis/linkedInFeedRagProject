# convert_messages_to_prompt_anthropic — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/chat_models/langchain_aws.chat_models.bedrock.convert_messages_to_prompt_anthropic.html
**Word Count:** 51
**Links Count:** 95
**Scraped:** 2025-07-21 08:29:02
**Status:** completed

---

# convert\_messages\_to\_prompt\_anthropic\#

langchain\_aws.chat\_models.bedrock.convert\_messages\_to\_prompt\_anthropic\(

    _messages : List\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_,     _\*_ ,     _human\_prompt : str = '\n\nHuman:'_,     _ai\_prompt : str = '\n\nAssistant:'_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/chat_models/bedrock.html#convert_messages_to_prompt_anthropic)\#     

Format a list of messages into a full prompt for the Anthropic model     

Args:     

messages \(List\[BaseMessage\]\): List of BaseMessage to combine. human\_prompt \(str, optional\): Human prompt tag. Defaults to “

Human:”.     

ai\_prompt \(str, optional\): AI prompt tag. Defaults to “

Assistant:”.     

Returns:     

str: Combined string with necessary human\_prompt and ai\_prompt tags.

Parameters:     

  * **messages** \(_List_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]_\)

  * **human\_prompt** \(_str_\)

  * **ai\_prompt** \(_str_\)

Return type:     

str

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)